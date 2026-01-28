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
        'pageSize': 10,          # must be between 10 and 1000
        'sessionType': 'Online', # 'Online' albo 'Batch'
        'referenceNumber': '',   # Przykład 20251218-SO-2082369000-ADB23AFB6A-42
        'dateCreatedFrom': '',   # Przykład 2025-12-19
        'dateCreatedTo': '',     # Przykład 2025-12-19
        'dateClosedFrom': '',    # Przykład 2025-12-19
        'dateClosedTo': '',      # Przykład 2025-12-19
        'dateModifiedFrom': '',  # Przykład 2025-12-19
        'dateModifiedTo': '',    # Przykład 2025-12-19
        'statuses': "InProgress" # Lista pozycji do wyboru ["InProgress", "Succeeded", "Failed", "Cancelled"]
    }
    params = urllib.parse.urlencode(params)
    resp = requests.get(
        cfg.url+f'/sessions?'+params,
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
