#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
#
# p12-ksef.py file-name password
# utworzenie pliku <file-name>-user.p12 na podstawie <file-name>.key.pem i <file-name>.crt.pem
# z dołączonym certyfikatem pośrednim MF
# password - haslo do pliku <file-name>.key.pem
#
# pliki *.[key|crt].pem pochodzą ze strony MF
#
# ecdsa_der_raw.py i test_ecdsa_der_raw.py utworzyła AI - pokazanie jak zamienić wynik podpisania
# kluczem EC na alternatywną formę honorowaną przez API
#
# odnalezione w necie certyfikaty używane przez MF do generacji certyfikatów użytkowników:
# mf-imm.pem, mf-root.pem
# mf-test-imm.pem, mf-test-root.pem
#

import binascii
import os
import sys
import datetime
from OpenSSL import crypto
from cryptography import x509
from cryptography.hazmat import backends
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization, hashes


class X:
    def key_load(self, fname, password=None):
        if password is not None:
            password = password.encode("utf-8")
        with open(fname, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password, backends.default_backend()
            )
            return private_key

    def key_save_pub(self, fname, key):
        with open(fname, "wb") as f:
            f.write(
                key.public_key().public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )

    def key_save_priv(self, fname, key, password):
        with open(fname, "wb") as f:
            if not password:
                f.write(
                    key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
            else:
                f.write(
                    key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.TraditionalOpenSSL,
                        encryption_algorithm=serialization.BestAvailableEncryption(
                            password.encode("utf-8")
                        ),
                    )
                )

    def cert_load(self, fname):
        with open(fname, "rb") as f:
            return x509.load_pem_x509_certificate(f.read(), backends.default_backend())

    def cert_save(self, fname, data):
        with open(fname, "wb") as f:
            f.write(data.public_bytes(serialization.Encoding.PEM))
        with open(fname+'.cer', "wb") as f:
            f.write(data.public_bytes(serialization.Encoding.DER))

    def pk12_load(self, fname, password):
        with open(fname, "rb") as fp:
            return pkcs12.load_key_and_certificates(
                fp.read(), password.encode("utf-8"), backends.default_backend()
            )

    def pk12_save(self, fname, p12, password):
        with open(fname, "wb") as f:
            f.write(p12.export(password.encode("utf-8")))

    def pk12_save(self, fname, name, key, cert, othercerts, password):
        with open(fname, "wb") as f:
            f.write(
                pkcs12.serialize_key_and_certificates(
                    name.encode("utf-8"),
                    key,
                    cert,
                    othercerts,
                    serialization.BestAvailableEncryption(password.encode("utf-8")),
                )
            )

    def show(self, cert):
        print('***')
        print(hex(cert.serial_number))
        print(cert.subject)
        print(cert.issuer)
        for ext in cert.extensions:
            if isinstance(ext.value, x509.extensions.CRLDistributionPoints):
                print('CRLDistributionPoints:')
                for e in ext.value:
                    print('    issuer:', e.crl_issuer)
                    for name in e.full_name:
                        print('    url:',name.value)
            elif isinstance(ext.value, x509.extensions.AuthorityInformationAccess):
                print('AuthorityInformationAccess:')
                for e in ext.value:
                    print('   ', e.access_method._name, ':', e.access_location.value)
            elif isinstance(ext.value, x509.extensions.AuthorityKeyIdentifier):
                print('AuthorityKeyIdentifier:')
                print('    key:', binascii.hexlify(ext.value.key_identifier))
def main():
    cls = X()
    p12pk = cls.key_load(sys.argv[1]+'.key.pem', sys.argv[2])
    p12uc = cls.cert_load(sys.argv[1]+'.crt.pem')

    p12oc = [cls.cert_load('mf-test-imm.pem')]

    pk12fname = sys.argv[1]+'-user.p12'
    pk12pass = "1234"
    cls.pk12_save(pk12fname, 'ksef', p12pk, p12uc, p12oc, pk12pass)
    cls.cert_save(sys.argv[1]+'-user.crt.pem', p12uc)
    cls.key_save_priv(sys.argv[1]+'-user.key.pem', p12pk, '1234')

main()
