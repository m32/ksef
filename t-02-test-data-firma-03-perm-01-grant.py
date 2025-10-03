#!/usr/bin/env vpython3
import datetime
import requests

import ksefconfig as cfg

def main():
    perms = [
        {
            "description": "ok",
            "premissionType": "InvoiceRead",
        },
        {
            "description": "ok",
            "premissionType": "InvoiceWrite",
        },
        {
            "description": "ok",
            "premissionType": "Introspection",
        },
        {
            "description": "ok",
            "premissionType": "CredentialsRead",
        },
        {
            "description": "ok",
            "premissionType": "CredentialsManage",
        },
        {
            "description": "ok",
            "premissionType": "EnforcementOperations",
        },
        {
            "description": "ok",
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
