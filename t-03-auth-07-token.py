#!/usr/bin/env vpython3
import os
import sys
import json
import base64
import datetime
import calendar
import rlogger
import requests
import dateutil.parser

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding as apadding
from cryptography.hazmat.primitives import hashes

from ksefconfig import Config

EPOCH = 1970
_EPOCH_ORD = datetime.date(EPOCH, 1, 1).toordinal()
def timegm(tuple):
    year, month, day, hour, minute, second = tuple[:6]
    days = datetime.date(year, month, 1).toordinal() - _EPOCH_ORD + day - 1
    hours = days*24 + hour
    minutes = hours*60 + minute
    seconds = minutes*60 + second
    return seconds

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')

    if not os.path.exists('certificates.json'):
        # 1. certificate
        url = cfg.url+"/api/v2/security/public-key-certificates"
        resp = requests.get(
            url,
            timeout=15
        )
        print('*' * 20, url)
        print(resp)
        if resp.status_code != 200:
            print(f'unhandled response: {response}')
            return
        data = resp.json()
    else:
        with open('certificates.json', 'rt') as fp:
            data = json.loads(fp.read())
    with open('certificates.json', 'wt') as fp:
        fp.write(json.dumps(data))
    crt = next(e['certificate'] for e in data if 'KsefTokenEncryption' in e['usage'])
    crt = f'-----BEGIN CERTIFICATE-----\n{crt}\n-----END CERTIFICATE-----'
    certificate = x509.load_pem_x509_certificate(crt.encode('utf-8'))
    public_key = certificate.public_key()

    url = cfg.url+'/api/v2/auth/challenge'
    resp = requests.post(
        url,
        timeout=15
    )
    print('*' * 20, 'POST', url)
    print(resp)
    if resp.status_code != 200:
        print(f'unhandled response: {resp}')
        return
    datachallenge = resp.json()

    dt = dateutil.parser.isoparse(datachallenge['timestamp'])
    t = int(dt.timestamp()*1000)

    token = f"{cfg.kseftoken}|{t}".encode('utf-8')
    encrypted_token = public_key.encrypt(
        token,
        apadding.OAEP(
            mgf=apadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    data = {
        'challenge': datachallenge['challenge'],
        'contextIdentifier': {
            'type': 'Nip',
            'value': cfg.nip,
        },
        'encryptedToken': base64.b64encode(encrypted_token).decode(),
        #'authorizationPolicy': ?
    }

    url = cfg.url+"/api/v2/auth/ksef-token"
    resp = requests.post(
        url,
        json=data
    )
    print('*'*20, 'POST', url)
    print(resp)
    if resp.status_code != 202:
        print(f'unhandled response: {resp}')
        return
    data = resp.json()
    with open(f'{cfg.prefix}-auth.temp.json', 'wt') as fp:
        fp.write(json.dumps(data))

main()
