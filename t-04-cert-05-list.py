#!/usr/bin/env vpython3
import json
import base64
import datetime
#import rlogger
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(days=30)
    pageSize = 10
    pageOffset = 0
    while True:
        data = {
            "status": "Active", # Active, Blocked, Revoked, Expired
            #"status": "Revoked", # Active, Blocked, Revoked, Expired
            #"expiresAfter": dtnow+dtdiff).isoformat(), # data końca ważności certyfikatu (opcjonalna)
            #"name": "", # nazwa certyfikatu (opcjonalny)
            #"type": "Authentication", # typ certyfikatu (Authentication, Offline) (opcjonalny)
            #"certificateSerialNumber": "", # numer seryjny certyfikatu (opcjonalny)
        }
        resp = requests.post(
            cfg.url+f'/api/v2/certificates/query?pageSize={pageSize}&pageOffset={pageOffset}',
            json=data,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=5
        )
        print('result:', resp)
        if resp.status_code != 200:
            print(resp.text)
            print(resp.headers)
            break
        data = resp.json()
        for cert in data['certificates']:
            print(cert)
        if not data['hasMore']:
            break
        pageOffset += pageSize

main()
