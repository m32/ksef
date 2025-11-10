#!/usr/bin/env vpython3
import base64
import calendar
import datetime
import json

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa, padding as apadding
from cryptography.hazmat.primitives import hashes

from ksef import Client, AuthenticatedClient
from ksef.api.auth import (
    post_api_v2_auth_challenge,
    post_api_v2_auth_ksef_token,
    get_api_v_2_auth_reference_number,
    post_api_v2_auth_token_redeem
)
from ksef.api.publickey import get_api_v2_security_public_key_certificates
from ksef.models import (
    init_token_authentication_request,
    authentication_context_identifier,
    authentication_context_identifier_type,
    authorization_policy,
)

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2] == 'o')
    clt = Client(cfg.url)
    if not cfg.kseftoken:
        raise AssertionError('Cannot authenticate without a Ksef token')

    # 1. certificate
    resp = get_api_v2_security_public_key_certificates.sync(client=clt)
    print('*' * 20, 'get_api_v2_security_public_key_certificates')
    print(resp)
    data_crt = [r.to_dict() for r in resp]
    crt = next(e['certificate'] for e in data_crt if 'KsefTokenEncryption' in e['usage'])
    crt = f'-----BEGIN CERTIFICATE-----\n{crt}\n-----END CERTIFICATE-----'
    certificate = x509.load_pem_x509_certificate(crt.encode('utf-8'))
    public_key = certificate.public_key()

    # 2. challenge
    resp = post_api_v2_auth_challenge.sync(client=clt)
    print('*'*20, 'post_api_v2_auth_challenge')
    print(resp)
    data1 = resp.to_dict()

    # 3. token
    t = datetime.datetime.fromisoformat(data1['timestamp'])
    t = int((calendar.timegm(t.timetuple()) * 1000) + (t.microsecond / 1000))
    token = f"{cfg.kseftoken}|{t}".encode('utf-8')

    encrypted_token = public_key.encrypt(
        token,
        apadding.OAEP(
            mgf=apadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    resp = post_api_v2_auth_ksef_token.sync(client=clt,
        body=init_token_authentication_request.InitTokenAuthenticationRequest(
            challenge=data1['challenge'],
            context_identifier=authentication_context_identifier.AuthenticationContextIdentifier(
                type_=authentication_context_identifier_type.AuthenticationContextIdentifierType.NIP,
                value=cfg.nip
            ),
            encrypted_token=base64.b64encode(encrypted_token).decode(),
            #authorization_policy=,
        )
    )
    print('*'*20, 'post_api_v2_auth_ksef_token')
    print(resp)
    data2 = resp.to_dict()

    # 4. result
    clt = AuthenticatedClient(
        cfg.url,
        token=data2['authenticationToken']['token']
    )
    status = 100
    while status < 200:
        resp = get_api_v_2_auth_reference_number.sync(client=clt,
            reference_number=data2['referenceNumber']
        )
        print('*'*20, 'get_api_v_2_auth_reference_number')
        print(resp)
        data3 = resp.to_dict()
        status = data3['status']['code']

    if status != 200:  # Not Authenticated
        raise AssertionError(f'Authentication failed, status: {status} description: {data3["status"]['description']}')

    # 4. Authenticated
    resp = post_api_v2_auth_token_redeem.sync(client=clt)
    print('*' * 20, 'post_api_v2_auth_token_redeem')
    print(resp)
    data4 = resp.to_dict()
    with open(f'{cfg.prefix}-auth.json', 'wt') as fp:
        fp.write(json.dumps(data4))


main()
