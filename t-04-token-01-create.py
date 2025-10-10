#!/usr/bin/env vpython3
import os
import json
#import rlogger
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    resp = requests.post(
        cfg.url+'/api/v2/tokens',
        json={
            "permissions": ["InvoiceRead", "InvoiceWrite"],
            "description": "token",
        },
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('tokens:', resp)
    if resp.status_code != 202:
        print(resp.text)
        print(resp.headers)
        return
    else:
        if os.path.exists(f'{cfg.prefix}-tokens.json'):
            with open(f'{cfg.prefix}-tokens.json', 'rt') as fp:
                tokens = json.loads(fp.read())
        else:
            tokens = {}

        data = resp.json()
        tokens[data["referenceNumber"]] = data["token"]

        with open(f'{cfg.prefix}-tokens.json', 'wt') as fp:
            fp.write(json.dumps(auth))

main()
