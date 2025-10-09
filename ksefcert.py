#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import typing
import datetime
import os, os.path
import sys
import glob
import uuid

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID

class Certificate(object):
    def key_create(self) -> rsa.RSAPrivateKey:
        return rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

    def key_save(self, fname: str, key: rsa.RSAPrivateKey, password: str) -> None:
        # Write our key to disk for safe keeping
        with open(fname, "wb") as f:
            if not password:
                f.write(
                    key.public_key().public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
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

    def key_load(self, fname: str, password: str) -> rsa.RSAPrivateKey:
        with open(fname, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password.encode("utf-8"), default_backend()
            )
            return private_key

    def cert_save(self, fname: str, data: x509.Certificate) -> None:
        with open(fname, "wb") as f:
            f.write(data.public_bytes(serialization.Encoding.PEM))
        with open(fname + ".cer", "wb") as f:
            f.write(data.public_bytes(serialization.Encoding.DER))
        cwd = os.getcwd()
        os.chdir("ca")
        os.symlink(fname, str(data.serial_number))
        os.chdir(cwd)

    def cert_load(self, fname: str) -> x509.Certificate:
        with open(fname, "rb") as f:
            return x509.load_pem_x509_certificate(f.read(), default_backend())

    def csr_load(self, fname: str) -> x509.CertificateSigningRequest:
        with open(fname, "rb") as f:
            return x509.load_pem_x509_csr(data=f.read(), backend=default_backend())

    def csr_create(
        self,
        key: rsa.RSAPrivateKey,
        country: typing.Union[str, None] = None,
        organization: typing.Union[str, None] = None,
        organizationIdentifier: typing.Union[str, None] = None,
        commonname: typing.Union[str, None] = None,
    ) -> x509.CertificateSigningRequest:
        names = []
        for t, v in (
            (NameOID.COUNTRY_NAME, country),
            (NameOID.ORGANIZATION_NAME, organization),
            (NameOID.ORGANIZATION_IDENTIFIER, organizationIdentifier),
            (NameOID.COMMON_NAME, commonname),
        ):
            if v:
                names.append(x509.NameAttribute(t, v))
        return (
            x509.CertificateSigningRequestBuilder()
            .subject_name(x509.Name(names))
            .sign(
                private_key=key,
                algorithm=hashes.SHA256(),
                rsa_padding=padding.PKCS1v15()
            )
        )

    def pk12_save(
        self,
        name: bytes,
        cert: x509.Certificate,
        key: rsa.RSAPrivateKey,
        fname: str,
        password: str,
    ) -> None:
        data = pkcs12.serialize_key_and_certificates(
            name=name,
            key=key,
            cert=cert,
            cas=[self.ca_sub_cert],
            encryption_algorithm=serialization.BestAvailableEncryption(
                password.encode("utf8")
            ),
        )
        with open(fname, "wb") as f:
            f.write(data)

    def pk12_load(self, fname: str, password: str) -> pkcs12.PKCS12KeyAndCertificates:
        with open(fname, "rb") as fp:
            return pkcs12.load_key_and_certificates(
                fp.read(), password.encode("utf-8"), default_backend()
            )
