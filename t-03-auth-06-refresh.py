#!/usr/bin/env vpython3
import json
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    resp = requests.post(
        cfg.url+f'/api/v2/auth/token/refresh',
        headers={
            "Authorization": "Bearer "+auth['refreshToken']['token'],
        },
        timeout=5
    )
    print('token.refresh:', resp)
    if resp.status_code == 200:
        data = resp.json()
        auth.update(data)
        print(auth)
        with open(f'{cfg.prefix}-auth.json', 'wt') as fp:
            fp.write(json.dumps(auth))
    else:
        print(resp.text)
        print(resp.headers)
main()
