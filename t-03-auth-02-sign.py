#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
from lxml import etree
from cryptography import x509
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID

from endesive import xades

import sys


def load_pfx(file_path, password):
    with open(file_path, 'rb') as fp:
        return pkcs12.load_key_and_certificates(
            fp.read(),
            password.encode("utf8"),
            backends.default_backend()
        )


import ksefconfig as cfg

def main():
    with open(f'{cfg.prefix}-auth.xml', 'rb') as fp:
        data = fp.read()

    p12pk, p12pc, p12oc = load_pfx(cfg.prefix+'.p12', '1234')

    def signproc(tosign, algosig):
        sig = p12pk.sign(
            tosign,
            padding.PKCS1v15(),
            getattr(hashes, algosig.upper())(),
        )
        return sig

    cert = p12pc
    certcontent = cert.public_bytes(serialization.Encoding.DER)

    cls = xades.BES()
    doc = cls.enveloping(
        "dokument.xml",
        data,
        "application/xml",
        cert,
        certcontent,
        signproc,
        False,
        True,
    )
    data = etree.tostring(doc, encoding="UTF-8", xml_declaration=True, standalone=False)

    with open(f'{cfg.prefix}-auth.xml.xades', "wb") as fp:
        fp.write(data)


if __name__ == "__main__":
    main()
