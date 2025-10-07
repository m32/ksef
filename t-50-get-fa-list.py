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
    data = {
        'subjectType': 'Subject1',
        'dateRange': {
            'from': (dtnow-dtdiff).isoformat(),
            'to': (dtnow+dtdiff).isoformat(),
            'datetype': 'Issue',
        }
    }
    resp = requests.post(
        cfg.url+'/api/v2/invoices/query/metadata?PageOffset=0&pageSize=10',
        json=data,
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print(resp)
    print(resp.text)

main()
