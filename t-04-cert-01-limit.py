#!/usr/bin/env vpython3
import json
#import rlogger
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    resp = requests.get(
        cfg.url+'/api/v2/certificates/limits',
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
    else:
        data = resp.json()
        print(data)

main()
