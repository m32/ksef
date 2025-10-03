#!/usr/bin/env vpython3
import datetime
import requests

import ksefconfig as cfg

def main():
    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(hours=1)
    data = {
        'nip': cfg.nip,
        'pesel': cfg.pesel,
        'isBailiff': False,
        'description': f'firma:{cfg.nip} osoba:{cfg.pesel}',
        'createdDate': (dtnow-dtdiff).isoformat(),
    }
    print(data)
    resp = requests.post(
        cfg.url+'/api/v2/testdata/person',
        json=data,
        timeout=5
    )
    print('testdata.person:', resp)

main()
