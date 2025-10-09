#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import typing
import datetime

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID

class Main(object):
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

    def cert_load(self, fname: str) -> x509.Certificate:
        with open(fname, "rb") as f:
            return x509.load_pem_x509_certificate(f.read(), default_backend())

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
            cas=[],
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

    def createcert(self, key: rsa.RSAPrivateKey, fn: str, ln: str, cn: str, nip: str|None = None, pesel: str|None = None) -> x509.Certificate:
        names = [
            x509.NameAttribute(NameOID.COMMON_NAME, cn),
            x509.NameAttribute(NameOID.COUNTRY_NAME, 'PL'),
        ]
        if nip:
            names.extend([
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, f'test'),
                x509.NameAttribute(NameOID.ORGANIZATION_IDENTIFIER, f'VATPL-{nip}'),
                x509.NameAttribute(NameOID.SERIAL_NUMBER, f'TINPL-{nip}'),
#                x509.NameAttribute(NameOID.SERIAL_NUMBER, f'VATPL-{nip}'),
            ])
        if pesel:
            names.extend([
                x509.NameAttribute(NameOID.GIVEN_NAME, fn),
                x509.NameAttribute(NameOID.SURNAME, ln),
                x509.NameAttribute(NameOID.SERIAL_NUMBER, f'PESEL-{pesel}'),
            ])
        subject = issuer = x509.Name(names)
        return (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.datetime.utcnow())
            .not_valid_after(
                # Our certificate will be valid for 40 years
                datetime.datetime.utcnow()
                + datetime.timedelta(days=40 * 365)
            ).add_extension(
                x509.BasicConstraints(
                    ca=True,
                    path_length=None,  # pathlen: is equal to the number of CAs/ICAs it can sign
                ),
                critical=True,
            ).add_extension(
                x509.AuthorityKeyIdentifier.from_issuer_public_key(key.public_key()),
                critical=False,
            ).add_extension(
                x509.SubjectKeyIdentifier.from_public_key(key.public_key()),
                critical=False,
            ).add_extension(
                x509.KeyUsage(
                    digital_signature=True,
                    content_commitment=False,  # nonRepudiation
                    key_encipherment=False,
                    data_encipherment=False,
                    key_agreement=False,
                    encipher_only=False,
                    decipher_only=False,
                    # ca
                    key_cert_sign=True,
                    crl_sign=True,
                ),
                critical=True,
            ).sign(
                key,
                hashes.SHA256(),
                #?default_backend(),
            )
        )

    def main(self) -> None:
        print("Cenerating certificates")
        import sys
        from ksefconfig import Config
        cfg = Config(int(sys.argv[1]))
        for (fn, ln, cn, nip, pesel) in (
            (None, None, cfg.nazwa, cfg.nip, None), # firma
            (cfg.imie, cfg.nazwisko, cfg.imie+' '+cfg.nazwisko, None, cfg.pesel), # osoba
        ):
            pk = self.key_create()
            cert = self.createcert(pk, fn, ln, cn, nip, pesel)
            name = nip if nip else pesel
            self.key_save(f'{name}.key.pem', pk, "1234")
            self.cert_save(f'{name}.pem', cert)
            self.pk12_save(b'cert', cert, pk, f'{name}.p12', "1234")

cls = Main()
cls.main()
