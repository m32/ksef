#!/usr/bin/env vpython3
import os
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

class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')
        self.section = 'ksef-demo'

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
            token, reference_number = open('SessionToken', 'rt').read().split('|')
        except:
            token = reference_number = None

        client = Client(
            base_url=self.config.get(self.section, 'api'),
            headers=self.headers
        )

        if token is None:
            response = api.sesja.authorisation_challenge.sync_detailed(
                client=client,
                json_body=models.AuthorisationChallengeRequest(
                    context_identifier=models.SubjectIdentifierByCompanyType(
                        type='onip',
                        identifier=self.config.get('user', 'nip')
                    )
                )
            )
            if response.status_code != 201:
                raise EOFError(response.status_code, response.parsed)
            #millisec = parser.parse(response.parsed.timestamp)
            millisec = response.parsed.timestamp.timestamp() * 1000
            millisec = str(int(millisec))

            token = self.encrypt(
                auth_token=self.config.get('user', 'token'),
                challenge_timestamp=millisec,
                pemdata=self.config.get(self.section, 'publickey'),
            )
            data = open('InitSessionTokenRequest.xml', 'rb').read()
            data = data.replace(b'{challenge}', response.parsed.challenge.encode('ascii'))
            data = data.replace(b'{nip}', self.config.get('user', 'nip').encode('ascii'))
            data = data.replace(b'{token}', token)
            data = types.Content(data)
            #data = models.InitSessionSignedRequest(data)

            response = api.sesja.init_token.sync_detailed(
                client=client,
                content=data
            )
            token = response.parsed.session_token.token
            reference_number = response.parsed.reference_number
            with open('SessionToken', 'wt') as fp:
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
            # czekamy na uruchomienie procesu roboczego
            if response.parsed.processing_code == 315:
                break
            time.sleep(5)

    def logout(self):
        os.unlink('SessionToken')
        response = api.sesja.terminate.sync_detailed(
            client=self.authclient,
        )

    def query1(self, datefrom, dateto):
        json_body = models.QueryInvoiceRequest(
            query_criteria=models.QueryCriteriaInvoiceRangeType(
                subject_type=models.QueryCriteriaInvoiceTypeSubjectType(
                    models.QueryCriteriaInvoiceTypeSubjectType.SUBJECT1
                ),
                type='range',
                invoicing_date_from=datefrom,
                invoicing_date_to=dateto,
            ),
        )
        response = api.zapytania.invoice.sync_detailed(
            client=self.authclient,
            json_body=json_body,
            page_size=100,
            page_offset=0,
        )
        self.querysave(response)

    def query2(self, datefrom, dateto):
        json_body = models.QueryInvoiceRequest(
            query_criteria=models.QueryCriteriaInvoiceRangeType(
                subject_type=models.QueryCriteriaInvoiceTypeSubjectType(
                    models.QueryCriteriaInvoiceTypeSubjectType.SUBJECT2
                ),
                type='range',
                invoicing_date_from=datefrom,
                invoicing_date_to=dateto,
            ),
        )
        response = api.zapytania.invoice.sync_detailed(
            client=self.authclient,
            json_body=json_body,
            page_size=100,
            page_offset=0,
        )
        self.querysave(response)

    def querysave(self, response):
        sh = self.authclient._headers.copy()
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
            open('%s.xml'%xno, 'wb').write(resp.parsed.additional_properties['content'])
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
        return response.parsed

    def upload(self, fname):
        data = open(fname, 'rb').read()
        response = self.uploaddata(data)
        no = response.element_reference_number
        # processingCode ma kilka stanow
        # 100 - zarejestrowany, 3??, 200 - w archiwum
        for i in range(4):
            response = api.faktury.status.sync_detailed(
                client=self.authclient,
                invoice_element_reference_number=no
            )
            time.sleep(5)

def main():
    cls = Main()
    try:
        cls.login()
        try:
            if 0:
                cls.query1(
                    datetime.datetime(2023, 10, 3, tzinfo=tzlocal()),
                    datetime.datetime(2023, 10, 3, 16, 46, 0, tzinfo=tzlocal()),
                )
            if 0:
                cls.query2(
                    datetime.datetime(2023, 9, 29, tzinfo=tzlocal()),
                    datetime.datetime(2023, 9, 30, tzinfo=tzlocal()),
                )
            if 0:
                for fname in (
                    'fv-1696621761.893093.xml',
                    'fv-1696621762.334318.xml',
                ):
                    cls.upload(fname)
        finally:
           cls.logout()
    except EOFError as e:
        print(e)

main()
