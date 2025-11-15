#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
import sys
from lxml import etree
from cryptography import x509
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, utils, ec
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID

from signxml import XMLSigner, XMLVerifier, SignatureMethod, SignatureConstructionMethod


def load_pfx(file_path, password):
    with open(file_path, 'rb') as fp:
        return pkcs12.load_key_and_certificates(fp.read(), password.encode(), backends.default_backend())


def main():
    fnamekey = sys.argv[1]
    fnamexml = sys.argv[2]

    p12pk, p12pc, p12oc = load_pfx(fnamekey+'.p12', '1234')

    if isinstance(p12pk, rsa.RSAPrivateKey):
        signature_algorithm = SignatureMethod.RSA_SHA256
    else:
        signature_algorithm = SignatureMethod.ECDSA_SHA256

    with open(fnamexml, 'rb') as fp:
        root = etree.fromstring(fp.read())
    signed_root = XMLSigner(
        #signature_algorithm=SignatureMethod.ECDSA_SHA256,
        method=SignatureConstructionMethod.enveloping
    ).sign(
        root, key=p12pk, cert=[p12pc]
    )
    with open(fnamexml+'.xades', 'wb') as fp:
        data = etree.tostring(signed_root, encoding="UTF-8", xml_declaration=True, standalone=False)
        fp.write(data)
    verified_data = XMLVerifier().verify(signed_root).signed_xml

if __name__ == "__main__":
    main()
