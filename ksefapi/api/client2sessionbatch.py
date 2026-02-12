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

#import rlogger
import requests
from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization, padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as apadding
from cryptography.hazmat.primitives import hashes

from .client2 import KSEFError, KSEFSessionError, KSEFUploadError, KSEFZipCreateError, KSEFZipSizeError

class KSeFInvoiceSender:
    MB = 1024*1024

        
    maxzipsize = 5*1024*MB # max zip file size = 5GB
    maxzippartsize = 100*MB # maksymalny rozmiar jednej czesci podzielonego zipa
    #maxzippartsize = 4*1024 # do testow

    def __init__(self, client, session=None):
        self.session_ref_number = None

        if os.path.exists(self.cfg.prefix+"-session.json"):
            with open(self.cfg.prefix+"-session.json", "rt") as fp:
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
        with open(self.cfg.prefix+"-session.json", "wt") as fp:
            fp.write(json.dumps(self.session, indent=4))

    def zip_create(self):
        if os.path.exists(self.cfg.prefix+"-session.zip"):
            raise KSEFZipCreateError('zip created', None)
        if self.session['batchFile']:
            raise KSEFZipCreateError('batchFile created', None)
        fnames = glob.glob(self.cfg.nip+"-*-*.xml")
        with zipfile.ZipFile(self.cfg.prefix+"-session.zip",'w', zipfile.ZIP_DEFLATED) as zip:
            for fname in fnames:
                zip.write(fname)
                os.unlink(fname)

        fileSize = os.path.getsize(self.cfg.prefix+"-session.zip")
        # max zip file size = 5GB
        if fileSize > maxzipsize:
            raise KSEFZipSizeError('total size of xml files is too big', None)

        cipher = Cipher(
            algorithms.AES(base64.b64decode(self.session['symmetric_key'])),
            modes.CBC(base64.b64decode(self.session['iv'])),
            backend=default_backend()
        )

        crc = hashlib.sha256()
        with open(self.cfg.prefix+"-session.zip", 'rb') as fi:
            fileParts = []
            filePartNo = 0
            size = 0
            while size < fileSize:
                filePartNo += 1
                with open(self.cfg.prefix+"-session.aes.%d"%filePartNo, 'wb') as fo:
                    data = fi.read(self.maxzippartsize)
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
                        'fileName': 'dokumenty.%d'%filePartNo,
                        'fileSize': len(edata),
                        'fileHash': base64.b64encode(hashlib.sha256(edata).digest()).decode(),
                    })

        self.session.update({
            'files': fnames,
            'batchFile': {
                'fileName': 'dokumenty.zip',
                'fileSize': fileSize,
                'fileHash': base64.b64encode(crc.digest()).decode(),
                'fileParts': fileParts,
            },
        })
        self.session_save()
        os.unlink(self.cfg.prefix+"-session.zip")

    def session_open(self):
        if self.session["referenceNumber"]:
            raise KSEFSessionError('session is already open', None)
        if not self.session['batchFile']:
            raise KSEFZipCreateError('batchFile not exists', None)
        if not self.session['batchFile']['fileParts']:
            raise KSEFZipCreateError('batch File already splitted', None)

        cert_bytes = base64.b64decode(self.cfg.ksefcert)
        certificate = x509.load_der_x509_certificate(cert_bytes, backend=default_backend())
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

        url = self.client.apiurl+"/api/v2/sessions/batch"
        response = requests.post(
            url,
            json=data,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=30,
        )

        print('open:', response)
        if response.status_code != 201:
            raise KSEFSessionError('Error opening session.', response.text)

        data = response.json()
        self.session["referenceNumber"] = data["referenceNumber"]
        self.session["sessionData"] = data
        self.session_save()

    def session_send(self):
        if not self.session["referenceNumber"]:
            raise KSEFSessionError('session is closed', None)

        for part in self.session["sessionData"]['partUploadRequests']:
            m = part['method'].upper()
            ordinalNumber = part['ordinalNumber']
            filePart = self.session['batchFile']['fileParts'][ordinalNumber-1]
            assert filePart['ordinalNumber'] == ordinalNumber
            if not os.path.exists(self.cfg.prefix+"-session.aes.%d"%ordinalNumber):
                continue
            with open(self.cfg.prefix+"-session.aes.%d"%ordinalNumber, 'rb') as fp:
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
                os.unlink(self.cfg.prefix+"-session.aes.%d"%ordinalNumber)

    def session_close(self):
        if not self.session["referenceNumber"]:
            raise KSEFSessionError('session is closed', None)

        url = self.client.apiurl+"/api/v2/sessions/batch/"+self.session["referenceNumber"]+"/close"
        response = requests.post(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=15,
        )
        print('close:', response)
        print(response.text)

    def session_status(self):
        if self.session["status"]:
            raise KSEFSessionError('session status already downloaded', None)
        url = self.client.apiurl+"/api/v2/sessions/"+self.session["referenceNumber"]
        response = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
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
            raise KSEFSessionError('session status not downloaded', None)
        response = requests.get(
            self.session["status"]["upo"]["pages"][0]["downloadUrl"],
            timeout=5,
        )
        print('status:', response)
        if response.status_code != 200:
            print(response.text)
            return
        with open(self.cfg.prefix+"-session-upo.xml", 'wt') as fp:
            fp.write(response.text.encode('utf-8'))

    def session_invoices(self):
        if not self.session["status"]:
            raise KSEFSessionError('session status not downloaded', None)
        url = self.client.apiurl+"/api/v2/sessions/"+self.session["referenceNumber"]+"/invoices"
        response = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
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
            url = self.client.apiurl+"/api/v2/sessions/"+self.session["referenceNumber"]+"/invoices/"+inv["referenceNumber"]+"/upo"
            response = requests.get(
                url,
                headers={
                    "Authorization": "Bearer "+auth["accessToken"]["token"],
                },
                timeout=5
            )
            print('status:', response)
            if response.status_code != 200:
                print(inv["referenceNumber"], response.text)
                return
            with open(inv["invoiceFileName"]+'.upo.xml', 'wt') as fp:
                fp.write(response.text.encode("utf-8"))
