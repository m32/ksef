#!/usr/bin/env vpython3
import json
import base64
import datetime
#import rlogger
import requests

import sys
from ksefconfig import Config
from ksefcert import Certificate, serialization

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    with open(f'{cfg.prefix}-cert-enrollments.json', 'rt') as fp:
        enrollments = json.loads(fp.read())

    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(hours=1)

    cls = Certificate()
    key = cls.key_create()
    csr = cls.csr_create(
        key=key,
        country=enrollments["countryName"],
        organization=enrollments["organizationName"],
        organizationIdentifier=enrollments["organizationIdentifier"],
        commonname=enrollments["commonName"],
    )
    csrb64 = base64.b64encode(csr.public_bytes(serialization.Encoding.DER)).decode()
    resp = requests.post(
        cfg.url+'/api/v2/certificates/enrollments',
        json={
            "certificateName": "Joanna Kowalska - Authentication",
            "certificateType": "Authentication",
            "validFrom": (dtnow-dtdiff).isoformat(),
            "csr": csrb64,
        },
        headers={
            "Authorization": "Bearer "+auth['accessToken']['token'],
        },
        timeout=5
    )
    print('result:', resp)
    if resp.status_code != 202:
        print(resp.text)
        print(resp.headers)
        return
    data = resp.json()
    data['key_pub'] = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    ).decode()
    data['key_priv'] = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"1234"),
    ).decode()

    with open(f'{cfg.prefix}-cert.json', 'wt') as fp:
        fp.write(json.dumps(data))

main()
