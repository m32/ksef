#!/usr/bin/env vpython3
import datetime
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]))
    data = {
        'subjectNip': cfg.nip,
    }
    print(data)
    resp = requests.post(
        cfg.url+'/api/v2/testdata/subject/remove',
        json=data,
        timeout=5
    )
    print('testdata.subject:', resp)

main()
