#!/usr/bin/env vpython3
import json
import requests

import ksefconfig as cfg

def main():
    with open(f'{cfg.prefix}-auth.temp.json', 'rt') as fp:
        auth = json.loads(fp.read())
    resp = requests.post(
        cfg.url+f'/api/v2/auth/token/redeem',
        headers={
            "Authorization": "Bearer "+auth['authenticationToken']['token'],
        },
        timeout=5
    )
    print('token.redeem:', resp)
    if resp.status_code == 200:
        data = resp.json()
        print(data)
        with open(f'{cfg.prefix}-auth.json', 'wt') as fp:
            fp.write(json.dumps(data))
    else:
        print(resp.headers)
        print('*'*20, 'text')
        print(resp.text)
main()
