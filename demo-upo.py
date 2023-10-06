#!/usr/bin/env vpython3
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
        if response.parsed.processing_code == 200:
            upo = response.parsed.upo.payload
            upo = b64decode(upo.getvalue())
            open('upo-{}.xml'.format(session), 'wb').write(upo)

def main():
    cls = Main()
    try:
        cls.upo(sys.argv[1])
        #cls.upo1('20231006-SE-93381FAB12-BD2B9843ED-A2', '8511172404-20231006-9853C3051C26-95')
    except EOFError as e:
        print(e)

main()
