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

logging.basicConfig(level=logging.INFO)
with open("logging.ini", "rt") as fp:
    ini = configparser.ConfigParser()
    ini.read_file(fp)
    logging.config.fileConfig(ini)

import httpx

from dateutil.tz import tzlocal
from dateutil import parser

from ksef_client import Client, AuthenticatedClient, models, types
from ksef_client.api.interfejsy_interaktywne_sesja import *
from ksef_client.api.interfejsy_interaktywne_zapytania import *
from ksef_client.api.interfejsy_interaktywne_faktury import *

from ksef_client.types import Response
from KSeF_xml import KSeF_xml
from KSeF_token import generate_KSeF_token

def authorization_challange_call(client, identifier):
    data = dict(
        type = 'onip',
        identifier = identifier
    )
    
    context_identifier_type = models.SubjectIdentifierByType.from_dict(data)
    request_body = models.AuthorisationChallengeRequest(
        context_identifier=context_identifier_type
    )
    response: Response[models.AuthorisationChallengeResponse] = authorisation_challenge.sync_detailed(
        client=client, json_body=request_body
    )
    return response

def set_challenge(xml: KSeF_xml, challenge: str) -> KSeF_xml:
    element = xml.get_child_by_tag('Challenge')
    element.text = challenge
    return xml

def get_response_data(response, print_data = True):
    try:
        response_data = ast.literal_eval(response.content.decode('UTF-8'))     
        if print_data:
            print(response_data)
    except (ValueError, AttributeError)as e:
        print(e)
        print('----------')
        print(response)
        return response 
    return response_data

class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')

        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }

    def login(self):
        try:
            token, sessiontoken = open('SessionToken', 'rt').read().split('|')
        except:
            token = sessiontoken = None
        client = Client(base_url=self.config.get('ksef', 'api'), headers=self.headers)
        if token is None:
            print('*'*20, 'authorization_challange_call')
            response = authorization_challange_call(client, self.config.get('ksef', 'nip'))
            print('*'*10, response.status_code, response.parsed)
            if response.status_code != 201:
                raise EOFError(response.status_code, response.parsed)
            r_data = get_response_data(response)

            ch = r_data.get('timestamp')
            millisec = parser.parse(ch)
            millisec = millisec.timestamp() * 1000
            millisec = str(int(millisec))

            print('*'*20, 'init_session_token.sync_detailed', millisec)
            token = generate_KSeF_token(
                auth_token=self.config.get('ksef', 'token'),
                challenge_timestamp=millisec,
                pemdata=self.config.get('ksef', 'publickey'),
            )
            data = open('InitSessionTokenRequest.xml', 'rb').read()
            data = data.replace(b'{challenge}', r_data.get('challenge').encode('ascii'))
            data = data.replace(b'{nip}', self.config.get('ksef', 'nip').encode('ascii'))
            data = data.replace(b'{token}', token)
            data = models.InitSessionSignedRequest(data)

            response = init_session_token.sync_detailed(
                client=client,
                request_body=data
            )
            print('*'*10, response)
            token = response.parsed.session_token.token
            sessiontoken = response.parsed.reference_number
            with open('SessionToken', 'wt') as fp:
                fp.write(token)
                fp.write('|')
                fp.write(sessiontoken)

        #ah = client.headers.copy()
        #ah['SessionToken'] = response.parsed.session_token.token
        aheaders = client.get_headers()
        aheaders.update({
            'SessionToken': token,
            'Accept': 'application/json',
        })
        acookies = client.get_cookies()
        self.authclient = AuthenticatedClient(
            base_url=client.base_url,
            cookies=acookies,
        #    headers=ah,
            headers=aheaders,
            timeout=client.get_timeout(),
            verify_ssl=client.verify_ssl,
            token=token,
        )
        self.sessiontoken = sessiontoken
        self.getStatus()

    def getStatus(self):
        while True:
            print('*'*20, 'session_status_reference_number.sync_detailed')
            response = session_status_reference_number.sync_detailed(
                client=self.authclient,
                page_size=100,
                page_offset=0,
                reference_number=self.sessiontoken,
            )
            print('*'*10, response.status_code, response.parsed)
            if response.parsed.processing_code == 315:
                break
            time.sleep(5)

    def logout(self):
        os.unlink('SessionToken')
        print('*'*20, 'terminate_session.sync_detailed')
        response = terminate_session.sync_detailed(
            client=self.authclient,
        )
        print('*'*10, response.status_code, response.parsed)

    def query1(self, datefrom, dateto):
        print('*'*20, 'query_invoice_async_init.sync_detailed')
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
        response = query_invoice_sync.sync_detailed(
            client=self.authclient,
            json_body=json_body,
            page_size=100,
            page_offset=0,
        )
        print('*'*10, response.status_code, response.parsed)
        self.querysave(response)

    def query2(self):
        print('*'*20, 'query_invoice_sync.sync_detailed')
        json_body = models.QueryInvoiceRequest(
            query_criteria=models.QueryCriteriaInvoiceRangeType(
                subject_type=models.QueryCriteriaInvoiceTypeSubjectType(
                    models.QueryCriteriaInvoiceTypeSubjectType.SUBJECT2
                ),
                type='range',
                invoicing_date_from=datetime.datetime(2023, 9, 29, tzinfo=tzlocal()),
                invoicing_date_to=datetime.datetime(2023, 9, 30, tzinfo=tzlocal()),
            ),
        )
        response = query_invoice_sync.sync_detailed(
            client=self.authclient,
            json_body=json_body,
            page_size=100,
            page_offset=0,
        )
        print('*'*10, response.status_code, response.parsed)
        self.querysave(response)

    def querysave(self, response):
        sh = self.authclient.get_headers()
        self.authclient.headers.update({
            'Accept': 'application/octet-stream'
            #'Accept': '*/*',
        })
        for no in range(response.parsed.number_of_elements):
            print('get_invoice.sync_detailed', no)
            rec = response.parsed.invoice_header_list[no]
            xno = rec.ksef_reference_number
            xdate = rec.invoicing_date
            xhash = rec.additional_properties['invoiceHash']['hashSHA']['value']
            resp = get_invoice.sync_detailed(
                client=self.authclient,
                k_se_f_reference_number=xno,
            )
            print('*'*10, no, resp.status_code, resp.parsed)
            open('%s.xml'%xno, 'wb').write(resp.parsed.additional_properties['content'])
        self.authclient.headers = sh

    def upload1data(self, data):
        print('*'*20, 'send_invoice.sync_detailed')
        size = len(data)
        crc = b64encode(hashlib.sha256(data).digest()).decode()
        data = b64encode(data).decode()
        json_body = models.SendInvoiceRequest(
            invoice_hash=models.File1MBHashType(
                hash_sha=models.HashSHAType(
                    algorithm="SHA-256",
                    encoding="Base64",
                    value=types.Bytes(
                        payload=crc
                    )
                ),
                file_size=size,
            ),
            invoice_payload=models.InvoicePayloadPlainType(
                type="plain",
                invoice_body=types.Bytes(
                    payload=data
                )
            )
        )
        response = send_invoice.sync_detailed(
            client=self.authclient,
            json_body=json_body,
        )
        print('*'*10, response.status_code, response.parsed)
        return response.parsed

    def upload1(self, fname):
        data = open(fname, 'rb').read()
        response = self.upload1data(data)
        print('*'*20, 'status_invoice.sync_detailed')
        response = status_invoice.sync_detailed(
            client=self.authclient,
            invoice_element_reference_number=response.element_reference_number
        )
        print('*'*10, response.status_code, response.parsed)
        return response.parsed

def main():
    cls = Main()
    try:
        cls.login()
        try:
            #cls.query1(
            #    datetime.datetime(2023, 10, 3, tzinfo=tzlocal()),
            #    datetime.datetime(2023, 10, 3, 16, 46, 0, tzinfo=tzlocal())
            #)
            #cls.query2()
            #cls.upload1('1696452019.114721.xml')
            pass
        finally:
            cls.logout()
            pass
    except EOFError as e:
        print(e)
main()
