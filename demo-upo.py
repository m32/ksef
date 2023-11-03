#!/usr/bin/env vpython3
import os
import sys
import getopt
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
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')

        self.headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }
        self.client = Client(
            base_url=self.config.get(server, 'api'),
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
            open('upo-{}-{}-{}.xml'.format(self.user, session, ksefid), 'wb').write(upo)

    def upo(self, session):
        response = api.status.status.sync_detailed(
            client=self.client,
            reference_number=session,
        )
        if response.status_code == 200 and response.parsed.processing_code == 200:
            upo = response.parsed.upo.payload
            upo = b64decode(upo.getvalue())
            open('upo-{}-{}.xml'.format(self.user, session), 'wb').write(upo)

def main():
    server = 'ksef-demo'
    user = 'user'
    opts, args = getopt.getopt(sys.argv[1:], '', [
        'server=',
        'user=',
    ])
    for o, a in opts:
        if o == '--server':
            server = a
        elif o == '--user':
            user = a
    cls = Main(server, user)
    try:
        for a in args:
            cls.upo(a)
        fname = 'upo-{}.csv'.format(user)
        if os.path.exists(fname):
            sessions = []
            with open(fname, 'rt') as fp:
                for line in fp.readlines():
                    session, ksefid = line.strip().split('|')
                    if session not in sessions:
                        cls.upo(session)
                        #cls.upo1(session, ksefid)
                        sessions.append(session)
            os.unlink(fname)
    except EOFError as e:
        print(e)

main()
