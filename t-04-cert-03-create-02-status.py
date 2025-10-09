#!/usr/bin/env vpython3
import json
import base64
import datetime
#import rlogger
import requests

import sys
from ksefconfig import Config
from ksefcert import Certificate, serialization

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    with open(f'{cfg.prefix}-cert.json', 'rt') as fp:
        csr = json.loads(fp.read())

    resp = requests.get(
        cfg.url+f'/api/v2/certificates/enrollments/{csr["referenceNumber"]}',
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('result:', resp)
    if resp.status_code != 200:
        print(resp.text)
        print(resp.headers)
        return
    data = resp.json()
    if data['status']['code'] != 200:
        print('xxx',data)
        return
    csr['certificateSerialNumber'] = data['certificateSerialNumber']
    with open(f'{cfg.prefix}-cert.json', 'wt') as fp:
        fp.write(json.dumps(csr))

main()
