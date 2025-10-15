#!/usr/bin/env vpython3
import json
import requests
import urllib.parse

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    params = {
        'pageSize': 10,
        'sessionType': 'Batch', # 'Online'
        'referenceNumber': '20251015-SB-31007BD000-53922AEC9B-B8',
        #'dateCreatedFrom': '',
        #'dateCreatedTo': '',
        #'dateClosedFrom': '',
        #'dateClosedTo': '',
        #'dateModifiedFrom': '',
        #'dateModifiedTo': '',
        'statuses[]': ["InProgress" "Succeeded" "Failed" "Cancelled"],
    }
    params = urllib.parse.urlencode(params)
    resp = requests.get(
        cfg.url+f'/api/v2/sessions?'+params,
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
