#!/usr/bin/env vpython3
import logging
import logging.config
import datetime
import configparser

logging.basicConfig(level=logging.INFO)
with open("../logging.ini", "rt") as fp:
    ini = configparser.ConfigParser()
    ini.read_file(fp)
    logging.config.fileConfig(ini)

import sys
sys.path.insert(1, 'xx')
import openapi_client as oa

class Main:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('../ksef.ini')

    def login(self):
        cfg = oa.Configuration(
            host=self.config.get('ksef', 'api')
        )
        client = oa.ApiClient(cfg)
        api = oa.SesjaApi(client)
        req = oa.AuthorisationChallengeRequest(
            context_identifier=oa.SubjectIdentifierByType(
                type=oa.SubjectIdentifierByCompanyType(
                    identifier=self.config.get('ksef', 'nip')
                )
            )
        )
        print('*'*20, 'online_session_authorisation_challenge')
        print(req)
        #resp = api.online_session_authorisation_challenge(req)
        resp = None
        print('*'*20, 'online_session_authorisation_challenge')
        print(resp)

    def logout(self):
        print('*'*20, 'terminate_session.sync_detailed')
        response = terminate_session.sync_detailed(
            client=self.authclient,
        )
        print('*'*10, response.status_code, response.parsed)

def main():
    cls = Main()
    try:
        cls.login()
        cls.logout()
    except EOFError as e:
        print(e)
main()
