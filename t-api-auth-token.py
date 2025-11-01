#!/usr/bin/env vpython3
import hashlib
import base64

from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as apadding
from cryptography.hazmat.primitives import hashes

from ksef import Client, AuthenticatedClient
from ksef.api.auth import (
    post_api_v2_auth_challenge,
    post_api_v2_auth_ksef_token,
    get_api_v_2_auth_reference_number,
)
from ksef.models import (
    init_token_authentication_request,
    authentication_context_identifier,
    authentication_context_identifier_type,
    authorization_policy,
)

import sys
from ksefconfig import Config

def main():
    # 1. challenge
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    clt = Client(cfg.url)
    resp = post_api_v2_auth_challenge.sync(client=clt)
    print('*'*20, 'post_api_v2_auth_challenge')
    print(resp)
    data1 = resp.to_dict()
    # 2. token
    token = f"{data1['challenge']}|{data1['timestamp']}".encode('utf-8')
    cert_bytes = base64.b64decode(cfg.ksefcert)
    certificate = x509.load_der_x509_certificate(cert_bytes)
    public_key = certificate.public_key()
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
    # 3. result
    clt = AuthenticatedClient(cfg.url,
        token=data2['authenticationToken']['token']
    )
    resp = get_api_v_2_auth_reference_number.sync(client=clt,
        reference_number=data2['referenceNumber']
    )
    print('*'*20, 'get_api_v_2_auth_reference_number')
    print(resp)
    # 4. nie działa, error 450: invalid token encryption

main()
