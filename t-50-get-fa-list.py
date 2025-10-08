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
    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(days=30)
    pageSize = 10
    pageOffset = 0
    while True:
        data = {
            'dateRange': {
                'dateType': 'Issue',
                'from': (dtnow-dtdiff).isoformat(),
                'to': dtnow.isoformat(),
            },
            'subjectType': 'Subject2',
        }
        resp = requests.post(
            cfg.url+f'/api/v2/invoices/query/metadata?pageOffset={pageOffset}&pageSize={pageSize}',
            json=data,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=5
        )
        print(resp)
        if resp.status_code != 200:
            print(resp.text)
            break
        data = resp.json()
        for inv in data['invoices']:
            print(data)
        if data['hasMore']:
            pageOffset += pageSize
        else:
            break

main()
