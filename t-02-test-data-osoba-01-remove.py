#!/usr/bin/env vpython3
import datetime
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]))
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
