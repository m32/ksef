#!/usr/bin/env vpython3
import os
import sys
import getopt
import configparser
import hashlib
import zipfile
from base64 import b64encode

if 1:
    from cryptography.hazmat.backends import default_backend
    backend = default_backend()
else:
    from cryptography.hazmat.backends.openssl.backend import backend
from cryptography.hazmat.primitives import serialization, padding, asymmetric
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Main:
    def __init__(self, server, user):
        self.server = server
        self.user = user
        self.config = configparser.ConfigParser()
        self.config.read('ksef.ini')
        self.key = os.urandom(256 // 8)
        self.iv = os.urandom(16)
        self.encryptor = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=backend).encryptor()

    def encryptmf(self, data):
        pemdata=self.config.get(self.server, 'publickey')
        public_key = serialization.load_pem_public_key(
            pemdata.encode()
        )
        return public_key.encrypt(
            data,
            asymmetric.padding.PKCS1v15()
        )

    def encrypt(self, data):
        padder = padding.PKCS7(algorithms.AES(self.key).block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        return self.encryptor.update(padded_data)

    def compress(self, files):
        fnameprefix = 'ksefbatch'

        fnamezip = '{}.zip'.format(fnameprefix)
        with zipfile.ZipFile(fnamezip, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
            for fname in files:
                zf.write(fname)
                os.rename(fname, 'send-{}'.format(fname))

        fnamepartfmt = '''\
            <ns2:PackagePartSignature>
                <ns3:OrdinalNumber>{nbno}</ns3:OrdinalNumber>
                <ns3:PartFileName>{fnamepart}</ns3:PartFileName>
                <ns3:PartFileHash>
                    <HashSHA>
                        <Algorithm>SHA-256</Algorithm>
                        <Encoding>Base64</Encoding>
                        <Value>{fnamepartsha256}</Value>
                    </HashSHA>
                    <FileSize>{fnamepartsize}</FileSize>
                </ns3:PartFileHash>
            </ns2:PackagePartSignature>\
'''
        fnamesha256 = hashlib.sha256()
        fnamezipsize = 0

        fnamezipe = '{}.zip-enc'.format(fnameprefix)
        with open(fnamezip, 'rb') as fi:
            with open(fnamezipe, 'wb') as fo:
                while True:
                    data = fi.read(4*1024*1024)
                    if not data:
                        break
                    fnamesha256.update(data)
                    fnamezipsize = len(data)
                    edata = self.encrypt(data)
                    assert edata != data
                    fo.write(edata)
                fo.write(self.encryptor.finalize())

        fnameparts = []
        fnamesplitsize = 49*1024*1024
        fnamesplitsize = 1024
        nbno = 0
        with open(fnamezipe, 'rb') as fe:
            while True:
                data = fe.read(fnamesplitsize)
                if not data:
                    break

                nbno += 1
                fnamepart = '{}.zip-enc-{}'.format(fnameprefix, nbno)
                with open(fnamepart, 'wb') as fo:
                    fo.write(data)

                fnamepartsha256 = hashlib.sha256(data).digest()
                fnameparts.append(fnamepartfmt.format(
                    nbno=nbno,
                    fnamepart=fnamepart,
                    fnamepartsha256=b64encode(fnamepartsha256).decode('ascii'),
                    fnamepartsize=len(data)
                ))

        fnamesha256 = fnamesha256.digest()
        fnameparts = '\n'.join(fnameparts)

        xml = '''\
<ns2:InitRequest
    xmlns="http://ksef.mf.gov.pl/schema/gtw/svc/types/2021/10/01/0001"
    xmlns:ns2="http://ksef.mf.gov.pl/schema/gtw/svc/batch/init/request/2021/10/01/0001"
    xmlns:ns3="http://ksef.mf.gov.pl/schema/gtw/svc/batch/types/2021/10/01/0001">
    <ns2:Identifier xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="SubjectIdentifierByCompanyType">
        <Identifier>{nip}</Identifier>
    </ns2:Identifier>
    <ns2:DocumentType>
        <Service>KSeF</Service>
        <FormCode>
            <SystemCode>FA (2)</SystemCode>
            <SchemaVersion>1-0E</SchemaVersion>
            <TargetNamespace>http://crd.gov.pl/wzor/2023/06/29/12648/</TargetNamespace>
            <Value>FA</Value>
        </FormCode>
    </ns2:DocumentType>
    <ns2:Encryption>
        <EncryptionKey>
            <Encoding>Base64</Encoding>
            <Algorithm>AES</Algorithm>
            <Size>256</Size>
            <Value>{key64}</Value>
        </EncryptionKey>
        <EncryptionInitializationVector>
            <Encoding>Base64</Encoding>
            <Bytes>16</Bytes>
            <Value>{iv64}</Value>
        </EncryptionInitializationVector>
        <EncryptionAlgorithmKey>
            <Algorithm>RSA</Algorithm>
            <Mode>ECB</Mode>
            <Padding>PKCS#1</Padding>
        </EncryptionAlgorithmKey>
        <EncryptionAlgorithmData>
            <Algorithm>AES</Algorithm>
            <Mode>CBC</Mode>
            <Padding>PKCS#7</Padding>
        </EncryptionAlgorithmData>
    </ns2:Encryption>
    <ns2:PackageSignature>
        <ns2:Package>
            <ns3:PackageType>split</ns3:PackageType>
            <ns3:CompressionType>zip</ns3:CompressionType>
            <ns3:Value>{fnamezip}</ns3:Value>
        </ns2:Package>
        <ns2:PackageFileHash>
            <HashSHA>
                <Algorithm>SHA-256</Algorithm>
                <Encoding>Base64</Encoding>
                <Value>{fnamesha256}</Value>
            </HashSHA>
            <FileSize>{fnamezipsize}</FileSize>
        </ns2:PackageFileHash>
        <ns2:PackagePartsList>
{fnameparts}
        </ns2:PackagePartsList>
    </ns2:PackageSignature>
</ns2:InitRequest>
'''.format(
    nip=self.config.get(self.user, 'nip'),
    key64=b64encode(self.encryptmf(self.key)).decode('ascii'),
    iv64=b64encode(self.iv).decode('ascii'),
    fnamezip=fnamezip,
    fnamesha256=b64encode(fnamesha256).decode('ascii'),
    fnameparts=fnameparts,
    fnamezipsize=fnamezipsize,
)
        fnamexml = '{}.xml'.format(fnameprefix)
        open(fnamexml, 'wt').write(xml)
        return fnamexml

def main():
    server = 'ksef-demo'
    user = 'user'
    opts, args = getopt.getopt(sys.argv[1:], '', [
        'server=',
        'user=',
    ])
    for o, a in opts:
        if o == '--server':
            server = a
        elif o == '--user':
            user = a
    cls = Main(server, user)
    cls.compress(args)

main()
