#!/usr/bin/env vpython3
import json
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.xml.xades', 'rb') as fp:
        xml = fp.read()
    resp = requests.post(
        cfg.url+'/api/v2/auth/xades-signature?verifyCertificateChain=false',
        data=xml,
        headers={
            "Content-Type": "application/xml",
        },
        timeout=5
    )
    print('post_api_v2_auth_xades_signature:', resp)
    if resp.status_code == 202:
        data = resp.json()
        with open(f'{cfg.prefix}-auth.temp.json', 'wt') as fp:
            fp.write(json.dumps(data))
        print('authenticationToken', data['authenticationToken'])
        print('a.token', data['authenticationToken']['token'])
        print('a.valid', data['authenticationToken']['validUntil'])
        print('referenceNumber', data['referenceNumber'])
    else:
        print(resp.text)
        print(resp.headers)
main()
