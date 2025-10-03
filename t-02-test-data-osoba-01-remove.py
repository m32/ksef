#!/usr/bin/env vpython3
import datetime
import requests

import ksefconfig as cfg

def main():
    data = {
        'nip': cfg.nip,
    }
    print(data)
    resp = requests.post(
        cfg.url+'/api/v2/testdata/person/remove',
        json=data,
        timeout=5
    )
    print('testdata.person:', resp)

main()
