#!/usr/bin/env vpython3
import json
import datetime
import requests

import ksefconfig as cfg

def main():
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    data = {
        'authorIdentifier': {
            'type': 'Nip',
            'value': cfg.nip,
        },
        'permissionTypes': [
            "InvoiceRead",
            "InvoiceWrite",
        ],
        'permissionState': 'Active',
        "queryType":"PermissionsInCurrentContext",
    }
    resp = requests.post(
        cfg.url+'/api/v2/permissions/query/persons/grants?pageOffset=0&pageSize=10',
        json=data,
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('testdata.permissions:', resp)
    print('testdata.permissions:', resp.text)

main()
