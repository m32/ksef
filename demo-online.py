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

from ksef.online import Client, AuthenticatedClient, models, types, errors
from ksef.online.api import sesja

class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')

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
        client = Client(
            base_url=self.config.get('ksef', 'api'),
            headers=self.headers
        )

        response = sesja.authorisation_challenge.sync_detailed(
            client=client,
            json_body=models.AuthorisationChallengeRequest(
                context_identifier=models.SubjectIdentifierByCompanyType(
                    type='onip',
                    identifier=self.config.get('ksef', 'nip')
                )
            )
        )
        if response.status_code != 201:
            raise EOFError(response.status_code, response.parsed)
        #millisec = parser.parse(response.parsed.timestamp)
        millisec = response.parsed.timestamp.timestamp() * 1000
        millisec = str(int(millisec))

        token = self.encrypt(
            auth_token=self.config.get('ksef', 'token'),
            challenge_timestamp=millisec,
            pemdata=self.config.get('ksef', 'publickey'),
        )
        data = open('InitSessionTokenRequest.xml', 'rb').read()
        data = data.replace(b'{challenge}', response.parsed.challenge.encode('ascii'))
        data = data.replace(b'{nip}', self.config.get('ksef', 'nip').encode('ascii'))
        data = data.replace(b'{token}', token)
        data = types.Content(data)
        #data = models.InitSessionSignedRequest(data)

        response = sesja.init_token.sync_detailed(
            client=client,
            content=data
        )

        aheaders = client._headers.copy()
        aheaders.update({
            'SessionToken': response.parsed.session_token.token,
            'Accept': 'application/json',
        })
        self.authclient = AuthenticatedClient(
            base_url=client._base_url,
            cookies=client._cookies.copy(),
            headers=aheaders,
            timeout=client._timeout,
            verify_ssl=client._verify_ssl,
            token=response.parsed.session_token.token,
        )
        self.sessiontoken = response.parsed.reference_number
        self.getStatus()

    def getStatus(self):
        while True:
            response = sesja.status_reference.sync_detailed(
                client=self.authclient,
                page_size=100,
                page_offset=0,
                reference_number=self.sessiontoken,
            )
            if response.parsed.processing_code == 315:
                break
            time.sleep(5)

    def logout(self):
        response = sesja.terminate.sync_detailed(
            client=self.authclient,
        )


def main():
    cls = Main()
    try:
        cls.login()
        cls.logout()
    except EOFError as e:
        print(e)

main()
