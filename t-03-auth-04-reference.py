#!/usr/bin/env vpython3
import json
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.temp.json', 'rt') as fp:
        auth = json.loads(fp.read())
    resp = requests.get(
        cfg.url+f'/api/v2/auth/{auth["referenceNumber"]}',
        headers={
            "Authorization": "Bearer "+auth['authenticationToken']['token'],
        },
        timeout=5
    )
    print('token.status:', resp)
    if resp.status_code in (200, 202):
        data = resp.json()
        print(data)
        auth = data['status']
        print('start:', data['startDate'])
        print('method:', data['authenticationMethod'])
        print('redeem:', data['isTokenRedeemed'])
        print(auth)
        #auth['code'] == 200
    else:
        print(resp.text)
        print(resp.headers)
main()
