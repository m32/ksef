#!/usr/bin/env vpython3
import datetime
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]))
    perms = [
        {
            "description": "InvoiceRead",
            "premissionType": "InvoiceRead",
        },
        {
            "description": "InvoiceWrite",
            "premissionType": "InvoiceWrite",
        },
        {
            "description": "Introspection",
            "premissionType": "Introspection",
        },
        {
            "description": "CredentialsRead",
            "premissionType": "CredentialsRead",
        },
        {
            "description": "CredentialsManage",
            "premissionType": "CredentialsManage",
        },
        {
            "description": "EnforcementOperations",
            "premissionType": "EnforcementOperations",
        },
        {
            "description": "SubunitManage",
            "premissionType": "SubunitManage",
        },
    ]
    data = {
        'contextIdentifier': {'type': 'nip', 'value': cfg.nip,},
        'authorizedIdentifier': {'type': 'pesel', 'value': cfg.pesel,},
        'permissions': [perms[0], perms[1]],
        'description': f'firma: {cfg.nip}',
    }
    resp = requests.post(
        cfg.url+'/api/v2/testdata/permissions',
        json=data,
        timeout=5
    )
    print('testdata.permissions:', resp)
    print('testdata.permissions:', resp.text)

main()
