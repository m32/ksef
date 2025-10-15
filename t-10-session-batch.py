#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import json
import os
import sys
import datetime
import hashlib
import base64
import glob
import zipfile
import pprint

import requests
from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class KSeFError(Exception):
    def __init__(self, msg, text):
        self.msg = msg
        self.text = text


class KSeFZipCreateError(KSeFError):
    pass

class KSeFZipSizeError(KSeFError):
    pass

class KSeFSessionError(KSeFError):
    pass


class KSeFUploadError(KSeFError):
    pass


class KSeFInvoiceSender:
    MB = 1024*1024
    def __init__(self, cfg):
        self.cfg = cfg
        # Wczytaj tokeny uwierzytelniania
        with open(f"{cfg.prefix}-auth.json", "rt") as fp:
            self.auth = json.loads(fp.read())

        self.access_token = self.auth["accessToken"]["token"]
        self.session_ref_number = None

        if os.path.exists(f"{self.cfg.prefix}-session.json"):
            with open(f"{self.cfg.prefix}-session.json", "rt") as fp:
                self.session = json.loads(fp.read())
        else:
            self.session = None
        if self.session is None:
            self.session = {
                'symmetric_key': base64.b64encode(os.urandom(32)).decode(),
                'iv': base64.b64encode(os.urandom(16)).decode(),
                'referenceNumber': None,
                'batchFile': None,
            }
            self.session_save()

    def session_save(self):
        with open(f"{self.cfg.prefix}-session.json", "wt") as fp:
            fp.write(json.dumps(self.session, indent=4))

    def zip_create(self):
        if self.session["referenceNumber"]:
            raise KSeFSessionError('session is already open', None)
        if self.session['batchFile']:
            raise KSeFZipCreateError('batchFile created', None)
        fnames = glob.glob(f'{self.cfg.nip}-*-*.xml')
        with zipfile.ZipFile(f"{self.cfg.prefix}-session.zip",'w', zipfile.ZIP_DEFLATED) as zip:
            for fname in fnames:
                zip.write(fname)
        fileSize = os.path.getsize(f"{self.cfg.prefix}-session.zip")
        # max zip file size = 5GB
        if fileSize > 5*1024*self.MB:
            raise KSeFZipSizeError('total size of xml files is too big', None)
        crc = hashlib.sha256()
        with open(f"{self.cfg.prefix}-session.zip", 'rb') as fi:
            nb = 0
            while nb < fileSize:
                data = fi.read(self.MB)
                crc.update(data)
                nb += len(data)
        self.session.update({
            'batchFile': {
                'fileName': 'dokumenty.zip',
                'fileSize': fileSize,
                'fileHash': base64.b64encode(crc.digest()).decode(),
                'fileParts': [],
            },
            'encrypted': False,
        })
        self.session_save()

    def zip_split(self):
        if self.session["referenceNumber"]:
            raise KSeFSessionError('session is already open', None)
        if not self.session['batchFile']:
            raise KSeFZipCreateError('batchFile not exists', None)
        if self.session['batchFile']['fileParts']:
            raise KSeFZipCreateError('batchFile already splitted', None)
        maxpartsize = 100*self.MB # max  part size
        maxpartsize = 4*1024
        fileParts = []
        with open(f"{self.cfg.prefix}-session.zip", 'rb') as fi:
            n = 1
            off = 0
            fileSize = self.session['batchFile']['fileSize']
            while off < fileSize:
                with open(f"{self.cfg.prefix}-session.zip.{n}", 'wb') as fo:
                    crc = hashlib.sha256()
                    nb = 0
                    while nb < maxpartsize:
                        left = fileSize - (off + nb)
                        if left <= 0:
                            break
                        data = fi.read(4096 if left > 4096 else left)
                        fo.write(data)
                        crc.update(data)
                        nb += len(data)
                fileParts.append({
                    'ordinalNumber': n,
                    'fileName': f'dokumenty.{n}',
                    'fileSize': nb,
                    'fileHash': base64.b64encode(crc.digest()).decode(),
                })
                off += nb
                n += 1
        self.session['batchFile']['fileParts'] = fileParts
        self.session['encrypted'] = False
        self.session_save()

    def zip_encrypt(self):
        if self.session["referenceNumber"]:
            raise KSeFSessionError('session is already open', None)
        if not self.session['batchFile']:
            raise KSeFZipCreateError('batchFile not exists', None)
        if not self.session['batchFile']['fileParts']:
            raise KSeFZipCreateError('batch File already splitted', None)
        if self.session['encrypted']:
            raise KSeFZipCreateError('split Files already encrypted', None)
        cipher = Cipher(
            algorithms.AES(base64.b64decode(self.session['symmetric_key'])),
            modes.CBC(base64.b64decode(self.session['iv'])),
            backend=default_backend()
        )
        for filePart in self.session['batchFile']['fileParts']:
            encryptor = cipher.encryptor()
            fnamer = f"{self.cfg.prefix}-session.zip.{filePart['ordinalNumber']}"
            pad = filePart['fileSize'] % 16
            if pad:
                padding_length = 16 - pad
                pad = bytes([padding_length] * padding_length)

            with open(fnamer, 'rb') as fp:
                fnamew = fnamer.replace('.zip.', '.aes.')
                with open(fnamew, 'wb') as fo:
                    while True:
                        data = fp.read(4096)
                        if not data:
                            break
                        if len(data) != 4096:
                            data += pad
                        edata = encryptor.update(data)
                        fo.write(edata)
                    fo.write(encryptor.finalize())
        self.session['encrypted'] = True
        self.session_save()

    def session_close(self):
        if not self.session["referenceNumber"]:
            raise KSeFSessionError('session is closed', None)

        response = requests.post(
            f'{self.cfg.url}/api/v2/sessions/batch/{self.session["referenceNumber"]}/close',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=15,
        )
        print('close:', response)
        print(response.text)
        return
        
        for filePart in self.session['batchFile']['fileParts']:
            fname = f"{self.cfg.prefix}-session.zip.{filePart['ordinalNumber']}"
            os.unlink(fname)
            fname = fname.replace('.zip.', '.aes.')
            os.unlink(fname)
        fname = f"{self.cfg.prefix}-session.zip"
        os.unlink(fname)
        fname = f"{self.cfg.prefix}-session.json"
        os.unlink(fname)

    def session_open(self):
        if self.session["referenceNumber"]:
            raise KSeFSessionError('session is already open', None)
        if not self.session['batchFile']:
            raise KSeFZipCreateError('batchFile not exists', None)
        if not self.session['batchFile']['fileParts']:
            raise KSeFZipCreateError('batch File already splitted', None)
        if not self.session['encrypted']:
            raise KSeFZipCreateError('split Files are not encrypted', None)

        cert_bytes = base64.b64decode(self.cfg.ksefcert)
        certificate = x509.load_der_x509_certificate(cert_bytes)
        public_key = certificate.public_key()
        assert isinstance(public_key, rsa.RSAPublicKey)

        encrypted_symmetric_key = public_key.encrypt(
            base64.b64decode(self.session['symmetric_key']),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        request_data = {
            "formCode": {
                "systemCode": "FA (3)",
                "schemaVersion": "1-0E",
                "value": "FA",
            },
            "batchFile": self.session["batchFile"],
            "encryption": {
                "encryptedSymmetricKey": base64.b64encode(encrypted_symmetric_key).decode(),
                "initializationVector": self.session['iv'],
            },
            "offline": False,
        }

        response = requests.post(
            f"{self.cfg.url}/api/v2/sessions/batch",
            json=request_data,
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=30,
        )

        print('open:', response)
        if response.status_code != 201:
            raise KSeFSessionError('Error opening session.', response.text)

        data = response.json()
        self.session["referenceNumber"] = data["referenceNumber"]
        self.session["sessionData"] = data
        self.session_save()

    def session_send(self):
        if not self.session["referenceNumber"]:
            raise KSeFSessionError('session is closed', None)

        for part in self.session["sessionData"]['partUploadRequests']:
            m = part['method'].upper()
            ordinalNumber = part['ordinalNumber']
            filePart = self.session['batchFile']['fileParts'][ordinalNumber-1]
            assert filePart['ordinalNumber'] == ordinalNumber
            with open(f"{self.cfg.prefix}-session.aes.{ordinalNumber}", 'rb') as fp:
                data = fp.read()
            if m == 'POST':
                response = requests.post(
                    part['url'],
                    data=data,
                    headers=part['headers'],
                    timeout=3600,
                )
            elif m == 'PUT':
                response = requests.put(
                    part['url'],
                    data=data,
                    headers=part['headers'],
                    timeout=3600,
                )
            else:
                raise IOError(2, 'unsupported method')
            print('send part:', filePart, response)

def main():
    from ksefconfig import Config
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')

    cls = KSeFInvoiceSender(cfg)

    import getopt
    opts, args = getopt.getopt(sys.argv[3:], '?z:s:')
    for o, a in opts:
        if o == '-?':
            print(sys.argv[0], '-z [c|s|e] -s [o|s|c]')
            print('-z c = zip create')
            print('-z s = zip split')
            print('-z e = zip encrypt')
            print('-s o = session open')
            print('-s s = session send')
            print('-s c = session close')
        if o == '-z':
            if a == 'c':
                cls.zip_create()
            elif a == 's':
                cls.zip_split()
            elif a == 'e':
                cls.zip_encrypt()
            else:
                print('bad argument')
        elif o == '-s':
            if a == 'o':
                cls.session_open()
            elif a == 's':
                cls.session_send()
            elif a == 'c':
                cls.session_close()
            else:
                print('bad argument')

if __name__ == "__main__":
    main()
