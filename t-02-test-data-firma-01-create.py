#!/usr/bin/env vpython3
import datetime
import requests

import ksefconfig as cfg

def main():
    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(hours=1)
    data = {
        'subjectNip': cfg.nip,
        'subjectType': 'EnforcementAuthority',
        #'subunits': None,
        'description': f'firma: {cfg.nip}',
        'createdDate': (dtnow-dtdiff).isoformat(),
    }
    print(data)
    resp = requests.post(
        cfg.url+'/api/v2/testdata/subject',
        json=data,
        timeout=5
    )
    print('testdata.subject:', resp)

main()
