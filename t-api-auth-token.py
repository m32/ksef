#!/usr/bin/env vpython3
import os
import sys
#import rlogger
import base64
#import calendar
import datetime
import json
import dateutil.parser

from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa, padding as apadding
from cryptography.hazmat.primitives import hashes

from ksef import Client, AuthenticatedClient
from ksef.api.auth import (
    post_auth_challenge,
    post_auth_ksef_token,
    get_auth_reference_number,
    post_auth_token_redeem
)
from ksef.api.publickey import get_security_public_key_certificates
from ksef.models import (
    init_token_authentication_request,
    authentication_context_identifier,
    authentication_context_identifier_type,
    authorization_policy,
)

from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2] == 'o')
    clt = Client(cfg.url)
    if not cfg.kseftoken:
        raise AssertionError('Cannot authenticate without a Ksef token')

    certificate, public_key = cfg.getcertificte(True)

    # 2. challenge
    resp = post_auth_challenge.sync(client=clt)
    print('*'*20, 'post_auth_challenge')
    print(resp)
    datachallenge = resp.to_dict()

    # 3. token
    if 'timestampMs' in datachallenge:
        t = int(datachallenge['timestampMs'])
    else:
        dt = dateutil.parser.isoparse(datachallenge['timestamp'])
        t = int(dt.timestamp()*1000)
        #dt = datetime.datetime.fromisoformat(datachallenge['timestamp'])
        #t = int((calendar.timegm(dt.timetuple()) * 1000) + (dt.microsecond / 1000))

    token = f"{cfg.kseftoken}|{t}".encode('utf-8')

    encrypted_token = public_key.encrypt(
        token,
        apadding.OAEP(
            mgf=apadding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    body=init_token_authentication_request.InitTokenAuthenticationRequest(
        challenge=datachallenge['challenge'],
        context_identifier=authentication_context_identifier.AuthenticationContextIdentifier(
            type_=authentication_context_identifier_type.AuthenticationContextIdentifierType.NIP,
            value=cfg.nip
        ),
        encrypted_token=base64.b64encode(encrypted_token).decode(),
        #authorization_policy=,
    )
    print('*'*20, 'body')
    print(body)
    resp = post_auth_ksef_token.sync(client=clt,
        body=body
    )
    print('*'*20, 'post_auth_ksef_token')
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
        raise AssertionError(f'Authentication failed, status: {status} description: {data3["status"]["description"]}')

    # 4. Authenticated
    resp = post_auth_token_redeem.sync(client=clt)
    print('*' * 20, 'post_auth_token_redeem')
    print(resp)
    data4 = resp.to_dict()
    with open(f'{cfg.prefix}-auth.json', 'wt') as fp:
        fp.write(json.dumps(data4))


main()
