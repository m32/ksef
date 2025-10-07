#!/usr/bin/env vpython3
import json
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    resp = requests.get(
        cfg.url+f'/api/v2/auth/sessions',
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('session.list:', resp)
    if resp.status_code == 200:
        data = resp.text
        print(data)
    else:
        print(resp.text)
        print(resp.headers)
main()
