#!/usr/bin/env vpython3
import os
import sys
import getopt
import hashlib
import time
import logging
import logging.config
import ast
import datetime
import configparser
import json
from base64 import b64encode

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

logging.basicConfig(level=logging.INFO)
with open("logging.ini", "rt") as fp:
    ini = configparser.ConfigParser()
    ini.read_file(fp)
    logging.config.fileConfig(ini)

import httpx

from dateutil.tz import tzlocal
from dateutil import parser

from ksef.online import Client, AuthenticatedClient, models, types, errors, api

class KSEFError(Exception):
    def __init__(self, rc, parsed):
        self.rc = rc
        self.parsed = parsed
        try:
            errors = parsed.exception.exception_detail_list
            krc = errors[0].exception_code
            kmsg = errors[0].exception_description
        except:
            krc = -1
            kmsg = 'unparsable'
            import traceback; traceback.print_exc()
        self.krc = krc
        self.kmsg = kmsg

    def __str__(self):
        return 'KSEFError: rc={} msg={}'.format(self.krc, self.kmsg)

    __repr__ = __str__


class Main:
    def __init__(self, user, server):
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')
        self.server = server
        self.user = user

        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }

    def encrypt(self, auth_token, challenge_timestamp, pemdata):
        
        token = (auth_token + "|" + challenge_timestamp).encode()
        public_key = serialization.load_pem_public_key(
            pemdata.encode()
        )
        encrypted = public_key.encrypt(
            token,
            padding.PKCS1v15()
        )
        return b64encode(encrypted)

    def login(self):
        try:
            token, reference_number = open('SessionToken-'+self.user, 'rt').read().split('|')
        except:
            token = reference_number = None

        client = Client(
            base_url=self.config.get(self.server, 'api'),
            headers=self.headers
        )

        if token is None:
            response = api.sesja.authorisation_challenge.sync_detailed(
                client=client,
                json_body=models.AuthorisationChallengeRequest(
                    context_identifier=models.SubjectIdentifierByCompanyType(
                        type='onip',
                        identifier=self.config.get(self.user, 'nip')
                    )
                )
            )
            if response.status_code != 201:
                raise KSEFError(response.status_code, response.parsed)
            #millisec = parser.parse(response.parsed.timestamp)
            millisec = response.parsed.timestamp.timestamp() * 1000
            millisec = str(int(millisec))

            token = self.encrypt(
                auth_token=self.config.get(self.user, 'token'),
                challenge_timestamp=millisec,
                pemdata=self.config.get(self.server, 'publickey'),
            )
            data = open('InitSessionTokenRequest.xml', 'rb').read()
            data = data.replace(b'{challenge}', response.parsed.challenge.encode('ascii'))
            data = data.replace(b'{nip}', self.config.get(self.user, 'nip').encode('ascii'))
            data = data.replace(b'{token}', token)
            data = types.Content(data)
            #data = models.InitSessionSignedRequest(data)

            response = api.sesja.init_token.sync_detailed(
                client=client,
                content=data
            )
            if response.status_code != 201:
                raise KSEFError(response.status_code, response.parsed)
            token = response.parsed.session_token.token
            reference_number = response.parsed.reference_number
            with open('SessionToken-'+self.user, 'wt') as fp:
                fp.write(token)
                fp.write('|')
                fp.write(reference_number)

        aheaders = client._headers.copy()
        aheaders.update({
            'SessionToken': token,
            'Accept': 'application/json',
        })
        self.authclient = AuthenticatedClient(
            base_url=client._base_url,
            cookies=client._cookies.copy(),
            headers=aheaders,
            timeout=client._timeout,
            verify_ssl=client._verify_ssl,
            token=token,
        )
        self.reference_number = reference_number
        self.getStatus()

    def getStatus(self):
        while True:
            response = api.sesja.status_reference.sync_detailed(
                client=self.authclient,
                page_size=100,
                page_offset=0,
                reference_number=self.reference_number,
            )
            if response.status_code != 200:
                if os.path.exists('SessionToken-'+self.user):
                    os.unlink('SessionToken-'+self.user)
                raise KSEFError(response.status_code, response.parsed)
            # czekamy na uruchomienie procesu roboczego
            if response.parsed.processing_code == 315:
                return response
            time.sleep(5)

    def logout(self):
        return
        os.unlink('SessionToken-'+self.user)
        response = api.sesja.terminate.sync_detailed(
            client=self.authclient,
        )

    def query(self, subject, datefrom, dateto, qtype):
        subjectType = getattr(models.QueryCriteriaInvoiceTypeSubjectType, 'SUBJECT'+subject)
        if qtype == 'incremental':
            json_body = models.QueryInvoiceRequest(
                query_criteria=models.QueryCriteriaInvoiceIncrementalType(
                    subject_type=models.QueryCriteriaInvoiceTypeSubjectType(
                        subjectType
                    ),
                    type='incremental',
                    acquisition_timestamp_threshold_from=datefrom,
                    acquisition_timestamp_threshold_to=dateto,
                ),
            )
        elif qtype == 'range':
            json_body = models.QueryInvoiceRequest(
                query_criteria=models.QueryCriteriaInvoiceRangeType(
                    subject_type=models.QueryCriteriaInvoiceTypeSubjectType(
                        subjectType
                    ),
                    type='range',
                    invoicing_date_from=datefrom,
                    invoicing_date_to=dateto,
                ),
            )
        else:
            raise ValueError(f'Niewspierany typ "{qtype}"')
        response = api.zapytania.invoice.sync_detailed(
            client=self.authclient,
            json_body=json_body,
            page_size=100,
            page_offset=0,
        )
        if response.status_code != 200:
            raise KSEFError(response.status_code, response.parsed)

        sh = self.authclient._headers.copy()
        try:
            self.authclient._headers.update({
                'Accept': 'application/octet-stream'
                #'Accept': '*/*',
            })
            for no in range(response.parsed.number_of_elements):
                rec = response.parsed.invoice_header_list[no]
                xno = rec.ksef_reference_number
                xdate = rec.invoicing_date
                xhash = rec.invoice_hash.hash_sha.value.payload.getvalue().decode()
                resp = api.faktury.get.sync_detailed(
                    client=self.authclient,
                    k_se_f_reference_number=xno,
                )
                with open('query-{}-{}.xml'.format(subject, xno), 'wb') as fp:
                    fp.write(resp.parsed.additional_properties['content'])
        finally:
            self.authclient._headers = sh

    def uploaddata(self, data):
        size = len(data)
        crc = b64encode(hashlib.sha256(data).digest()).decode()
        data = b64encode(data).decode()
        json_body = models.SendInvoiceRequest(
            invoice_hash=models.File1MBHashType(
                hash_sha=models.HashSHAType(
                    algorithm="SHA-256",
                    encoding="Base64",
                    value=types.Content(
                        payload=crc
                    )
                ),
                file_size=size,
            ),
            invoice_payload=models.InvoicePayloadPlainType(
                type="plain",
                invoice_body=types.Content(
                    payload=data
                )
            )
        )
        response = api.faktury.send.sync_detailed(
            client=self.authclient,
            json_body=json_body,
        )
        # 202 = accepted
        if response.status_code != 202:
            raise KSEFError(response.status_code, response.parsed)
        return response

    def upload(self, fname):
        data = open(fname, 'rb').read()
        response = self.uploaddata(data)
        no = response.parsed.element_reference_number
        while response.parsed.processing_code != 200 and response.parsed.processing_code < 400:
            response = api.faktury.status.sync_detailed(
                client=self.authclient,
                invoice_element_reference_number=no
            )
            if response.status_code == 400:
                break
            time.sleep(5)

        if response.status_code == 200 and response.parsed.processing_code == 200:
            with open('upo.csv', 'at') as fp:
                fp.write('{}|{}\n'.format(
                    self.reference_number, response.parsed.element_reference_number
                ))
        else:
            raise KSEFError(response.status_code, response.parsed)

def main():
    dateto = datetime.datetime.now(tz=tzlocal())
    datefrom = datetime.datetime(year=dateto.year, month=dateto.month, day=dateto.day, tzinfo=tzlocal())
    query = None
    querytype = True
    server = 'ksef-demo'
    user = 'user'
    opts, args = getopt.getopt(sys.argv[1:], '', [
        'date-from=',
        'date-to=',
        'query=',
        'query-type=',
        'server=',
        'user=',
    ])
    for o, a in opts:
        if o == '--date-from':
            datefrom = parser.parse(a)
        elif o == '--date-to':
            dateto = parser.parse(a)
        elif o == '--query':
            assert a in '123'
            query = a
        elif o == '--query-type':
            assert a in ('incremental', 'range', 'detail')
            querytype = a
        elif o == '--server':
            server = a
        elif o == '--user':
            user = a
    if query is None and not args:
        print('Nic do zrobienia, podaj parametry query albo dodaj listę plików do zapisania w ksef')
        print(sys.argv[0], '[--query=1|2] [--query-type=incremental|range|detail] [--date-from=...] [--date-to=...] [--server=ksef-demo|ksef-prod|ksef-test] [--user=user??] [fv-1.xml fv-2.xml ...]')
        print('./demo-online.py --server=ksef-test --user=user3 --query=2 --date-from=2023-10-17T09:00:00+02:00 --date-to=2023-10-17T10:00:00+02:00')
        return
    cls = Main(user, server)
    try:
        cls.login()
        try:
            if query is not None:
                cls.query(query, datefrom, dateto, querytype)
            for fname in args:
                cls.upload(fname)
        finally:
            cls.logout()
            pass
    except KSEFError as e:
        print('+'*20, 'KSEFError')
        print(e)
        print(e.parsed)

main()
