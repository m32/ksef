#!/usr/bin/env vpython3
# *-* coding: utf-8 *-*
from lxml import etree
from cryptography import x509
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.x509.oid import NameOID

from signxml import XMLSigner, XMLVerifier, SignatureMethod, SignatureConstructionMethod
from endesive import xades

def load_pfx(file_path, password):
    with open(file_path, 'rb') as fp:
        return pkcs12.load_key_and_certificates(
            fp.read(),
            password.encode("utf8"),
            backends.default_backend()
        )


import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.xml', 'rb') as fp:
        data = fp.read()

    p12pk, p12pc, p12oc = load_pfx(cfg.prefix+'.p12', '1234')
    useenveloped = False
    useendesive = True
    if useendesive:
        assert isinstance(p12pk, rsa.RSAPrivateKey) or isinstance(p12pk, ec.EllipticCurvePrivateKey)
        assert isinstance(p12pc, x509.Certificate)
        if isinstance(p12pk, rsa.RSAPrivateKey):
            signaturemethod = None
        else:
            signaturemethod = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256'

        def signproc(tosign, algosig):
            if isinstance(p12pk, rsa.RSAPrivateKey):
                sig = p12pk.sign(
                    tosign,
                    padding.PKCS1v15(),
                    getattr(hashes, algosig.upper())(),
                )
            else:
                sig = p12pk.sign(
                    tosign,
                    ec.ECDSA(getattr(hashes, algosig.upper())())
                )
                from asn1crypto import core
                length = 32 #=256/8 czyli aes-256 TODO zamienić na zmienną zależną od długości klucza
                d = core.load(sig)
                dr = d[0].native.to_bytes(length, byteorder="big")
                ds = d[1].native.to_bytes(length, byteorder="big")
                sig = dr+ds
            return sig

        cert = p12pc
        certcontent = cert.public_bytes(serialization.Encoding.DER)

        cls = xades.BES()
        if useenveloped:
            doc = cls.enveloped(
                data,
                cert,
                certcontent,
                signproc,
                None,
                None,
                signaturemethod=signaturemethod
            )
        else:
            doc = cls.enveloping(
                "dokument.xml",
                data,
                "application/xml",
                cert,
                certcontent,
                signproc,
                False,
                True,
                signaturemethod=signaturemethod
            )
        data = etree.tostring(doc, encoding="UTF-8", xml_declaration=True, standalone=False)
    else:
        if isinstance(p12pk, rsa.RSAPrivateKey):
            signature_algorithm=SignatureMethod.RSA_SHA256
        elif isinstance(p12pk, ec.EllipticCurvePrivateKey):
            signature_algorithm=SignatureMethod.ECDSA_SHA256
        else:
            assert False, "Unsupported private key type"

        root = etree.fromstring(data)
        signed_root = XMLSigner(
            signature_algorithm=signature_algorithm,
            method=SignatureConstructionMethod.enveloped if useenveloped else SignatureConstructionMethod.enveloping
        ).sign(
            root, key=p12pk, cert=[p12pc]
        )
        data = etree.tostring(signed_root, encoding="UTF-8", xml_declaration=True, standalone=False)

    with open(f'{cfg.prefix}-auth.xml.xades', "wb") as fp:
        fp.write(data)


if __name__ == "__main__":
    main()
