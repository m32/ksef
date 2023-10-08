#!/usr/bin/env vpython3
import os
import sys
import logging
import logging.config
import configparser

logging.basicConfig(level=logging.INFO)
with open("logging.ini", "rt") as fp:
    ini = configparser.ConfigParser()
    ini.read_file(fp)
    logging.config.fileConfig(ini)

from ksef.common import Client, api
from base64 import b64decode

class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')

        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }
        self.client = Client(
            base_url=self.config.get('ksef-demo', 'api'),
            headers=self.headers
        )

    def upo1(self, session, ksefid):
        response = api.upo.upo.sync_detailed(
            client=self.client,
            reference_number=session,
            upo_reference_number=ksefid,
        )
        if response.parsed.processing_code == 200:
            upo = response.parsed.upo.payload
            upo = b64decode(upo.getvalue())
            open('upo-{}-{}.xml'.format(session, ksefid), 'wb').write(upo)

    def upo(self, session):
        response = api.status.status.sync_detailed(
            client=self.client,
            reference_number=session,
        )
        if response.status_code == 200 and response.parsed.processing_code == 200:
            upo = response.parsed.upo.payload
            upo = b64decode(upo.getvalue())
            open('upo-{}.xml'.format(session), 'wb').write(upo)

def main():
    cls = Main()
    try:
        for a in sys.argv:
            cls.upo(a)
        if os.path.exists('upo.csv'):
            sessions = []
            with open('upo.csv', 'rt') as fp:
                for line in fp.readlines():
                    session, ksefid = line.strip().split('|')
                    if session not in sessions:
                        cls.upo(session)
                        #cls.upo1(session, ksefid)
                        sessions.append(session)
            os.unlink('upo.csv')
    except EOFError as e:
        print(e)

main()
