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

import rlogger
import requests
from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as apadding
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
                'status': None,
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
                os.unlink(fname)

        crc = hashlib.sha256()
        fileSize = os.path.getsize(f"{self.cfg.prefix}-session.zip")
        # max zip file size = 5GB
        if fileSize > 5*1024*self.MB:
            raise KSeFZipSizeError('total size of xml files is too big', None)

        cipher = Cipher(
            algorithms.AES(base64.b64decode(self.session['symmetric_key'])),
            modes.CBC(base64.b64decode(self.session['iv'])),
            backend=default_backend()
        )

        maxpartsize = 100*self.MB # max part size
        #maxpartsize = 4*1024

        with open(f"{self.cfg.prefix}-session.zip", 'rb') as fi:
            fileParts = []
            filePartNo = 0
            size = 0
            while size < fileSize:
                filePartNo += 1
                with open(f"{self.cfg.prefix}-session.aes.{filePartNo}", 'wb') as fo:
                    data = fi.read(maxpartsize)
                    crc.update(data)
                    size += len(data)

                    padder = padding.PKCS7(algorithms.AES(base64.b64decode(self.session['symmetric_key'])).block_size).padder()
                    padded_data = padder.update(data) + padder.finalize()
                    encryptor = cipher.encryptor()
                    edata = encryptor.update(padded_data)
                    fo.write(edata)
                    fo.write(encryptor.finalize())

                    fileParts.append({
                        'ordinalNumber': filePartNo,
                        #'fileName': f'dokumenty.{filePartNo}', # w dokumentacji oznaczony jako deprecated
                        'fileSize': len(edata),
                        'fileHash': base64.b64encode(hashlib.sha256(edata).digest()).decode(),
                    })

        self.session.update({
            'files': fnames,
            'batchFile': {
                #'fileName': 'dokumenty.zip', # nie ma takiego pola w dokumentacji
                'fileSize': fileSize,
                'fileHash': base64.b64encode(crc.digest()).decode(),
                'fileParts': fileParts,
            },
        })
        self.session_save()
        os.unlink(f"{self.cfg.prefix}-session.zip")

    def session_open(self):
        if self.session["referenceNumber"]:
            raise KSeFSessionError('session is already open', None)
        if not self.session['batchFile']:
            raise KSeFZipCreateError('batchFile not exists', None)
        if not self.session['batchFile']['fileParts']:
            raise KSeFZipCreateError('batch File already splitted', None)

        cert_bytes = base64.b64decode(self.cfg.ksefcert)
        certificate = x509.load_der_x509_certificate(cert_bytes)
        public_key = certificate.public_key()
        assert isinstance(public_key, rsa.RSAPublicKey)

        encrypted_symmetric_key = public_key.encrypt(
            base64.b64decode(self.session['symmetric_key']),
            apadding.OAEP(
                mgf=apadding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        data = {
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
            json=data,
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
            if not os.path.exists(f"{self.cfg.prefix}-session.aes.{ordinalNumber}"):
                continue
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
            print('send:', filePart, response)
            if response.status_code != 201:
                print(response.text)
            else:
                os.unlink(f"{self.cfg.prefix}-session.aes.{ordinalNumber}")

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

    def session_status(self):
        if self.session["status"]:
            raise KSeFSessionError('session status already downloaded', None)
        response = requests.get(
            self.cfg.url+f'/api/v2/sessions/{self.session["referenceNumber"]}',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=5
        )
        print('status:', response)
        if response.status_code != 200:
            print(response.text)
            return
        data = response.json()
        if data['status']['code'] < 200:
            pprint.pprint(data)
            return
        self.session["status"] = data
        self.session_save()

    def session_upo(self):
        if not self.session["status"]:
            raise KSeFSessionError('session status not downloaded', None)
        response = requests.get(
            self.session["status"]["upo"]["pages"][0]["downloadUrl"],
            timeout=5,
        )
        print('status:', response)
        if response.status_code != 200:
            print(response.text)
            return
        with open(f"{self.cfg.prefix}-session-upo.xml", 'wt') as fp:
            fp.write(response.text)

    def session_invoices(self):
        if not self.session["status"]:
            raise KSeFSessionError('session status not downloaded', None)
        response = requests.get(
            self.cfg.url+f'/api/v2/sessions/{self.session["referenceNumber"]}/invoices',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=5
        )
        print('status:', response)
        if response.status_code != 200:
            print(response.text)
            return
        data = response.json()
        self.session["invoices"] = data
        self.session_save()

        for inv in data["invoices"]:
            response = requests.get(
                self.cfg.url+f'/api/v2/sessions/{self.session["referenceNumber"]}/invoices/{inv["referenceNumber"]}/upo',
                headers={
                    "Authorization": f"Bearer {self.access_token}",
                },
                timeout=5
            )
            print('status:', response)
            if response.status_code != 200:
                print(inv["referenceNumber"], response.text)
                return
            with open(inv["invoiceFileName"]+'.upo.xml', 'wt') as fp:
                fp.write(response.text)

def main():
    from ksefconfig import Config
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')

    cls = KSeFInvoiceSender(cfg)

    import getopt
    opts, args = getopt.getopt(sys.argv[3:], '?zosctui')
    for o, a in opts:
        if o == '-?':
            print(sys.argv[0], '-z|-o|-s|-c|-u')
            print('-z = zip create/encrypt/split')
            print('-o = session open')
            print('-s = session send')
            print('-c = session close')
            print('-t = session status')
            print('-u = session upo')
            print('-i = session invoices metadata')
        if o == '-z':
            cls.zip_create()
        elif o == '-o':
            cls.session_open()
        elif o == '-s':
            cls.session_send()
        elif o == '-c':
            cls.session_close()
        elif o == '-t':
            cls.session_status()
        elif o == '-u':
            cls.session_upo()
        elif o == '-i':
            cls.session_invoices()

if __name__ == "__main__":
    main()
