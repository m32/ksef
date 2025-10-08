#!/usr/bin/env vpython3
import json
import datetime
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    ksefNumber = sys.argv[3]
    resp = requests.get(
        cfg.url+f'/api/v2/invoices/ksef/{ksefNumber}',
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print(resp)
    if resp.status_code == 200:
        with open(f'{ksefNumber}.xml', 'wt') as fp:
            fp.write(resp.text)

main()
