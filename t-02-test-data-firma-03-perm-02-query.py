#!/usr/bin/env vpython3
import json
import datetime
import requests

import ksefconfig as cfg

def main():
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    data = {
        'contextIdentifier': {
            'type': 'nip',
            'value': cfg.nip,
        },
        'targetIdentifier': {
            'type': 'pesel',
            'value': cfg.pesel,
        },
        'permissionTypes': [
            "CredentialsManage",
            "CredentialsRead",
            "InvoiceWrite",
            "InvoiceRead",
            "Introspection",
            "SubunitManage",
            "EnforcementOperations",
        ],
        'permissionState': 'Active',
        #'permissionState': 'Inactive',
    }
    resp = requests.post(
        cfg.url+'/api/v2/testdata/permissions/query/personal/grants',
        json=data,
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('testdata.permissions:', resp)
    print('testdata.permissions:', resp.text)

main()
