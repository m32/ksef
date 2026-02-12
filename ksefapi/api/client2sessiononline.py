#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import json
import os
import sys
import datetime
import hashlib
import base64

import requests
from dateutil import tz, parser

from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

from .client2 import KSEFError, KSEFSessionError, KSEFUploadError


class KSEFSessionOnline:
    def __init__(self, client):
        self.client = client

        ksefcert = base64.b64decode(self.client.dbLoadKSeFCert(False))
        certificate = x509.load_der_x509_certificate(ksefcert, backend=default_backend())
        self.ksefkey = certificate.public_key()
        assert isinstance(self.ksefkey, rsa.RSAPublicKey)

        self.blank_session()

    def blank_session(self):
        self.session = {
            "symmetric_key": base64.b64encode(os.urandom(32)).decode(),
            "iv": base64.b64encode(os.urandom(16)).decode(),
            "referenceNumber": None,
            "validUntil": None,
        }

    def restore(self, session, force=False):
        if session is not None:
            if self.valid(session):
                self.session = session
            elif force:
                self.session = session

    def ref(self):
        return self.session["referenceNumber"]

    def valid(self, session=None):
        if session is None:
            session = self.session
        if not session or not session.get("validUntil", None):
            return False
        return self.remains(session, 15)

    def remains(self, session, minutes):
        dtnow = datetime.datetime.now(tz.tzutc())
        dtdiff = datetime.timedelta(minutes=minutes)
        dt = parser.isoparse(session["validUntil"])
        #print('remains:', dt > dtnow - dtdiff, 'end:', dt, 'now:', dtnow - dtdiff)
        return dtnow + dtdiff < dt

    def open(self):
        encrypted_symmetric_key = self.ksefkey.encrypt(
            base64.b64decode(self.session["symmetric_key"]),
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
            "encryption": {
                "encryptedSymmetricKey": base64.b64encode(encrypted_symmetric_key).decode(),
                "initializationVector": self.session["iv"],
            },
        }

        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/online"
        resp = requests.post(
            url,
            json=request_data,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout*2,
        )

        self.client.showResponse("POST", url, resp)
        if resp.status_code != 201:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online open)", None)

        data = resp.json()
        self.session["referenceNumber"] = data["referenceNumber"]
        self.session["validUntil"] = data["validUntil"]

    def close(self):
        if not self.session["referenceNumber"]:
            return

        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/online/"+self.session["referenceNumber"]+"/close"
        resp = requests.post(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout,
        )
        self.client.showResponse("POST", url, resp)
        if resp.status_code != 204:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online close)", None)

        self.blank_session()

    def calculate_hash(self, data):
        return base64.b64encode(hashlib.sha256(data).digest()).decode()

    def encrypt_invoice(self, invoice_bytes):
        cipher = Cipher(
            algorithms.AES(base64.b64decode(self.session["symmetric_key"])),
            modes.CBC(base64.b64decode(self.session["iv"])),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()

        pad = len(invoice_bytes) % 16
        if pad:
            padding_length = 16 - pad
            invoice_bytes += bytes([padding_length] * padding_length)
        encrypted_invoice = encryptor.update(invoice_bytes) + encryptor.finalize()

        encrypted_symmetric_key = self.ksefkey.encrypt(
            base64.b64decode(self.session["symmetric_key"]),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return encrypted_invoice

    def send(self, invoice):
        if not self.session["referenceNumber"]:
            raise KSEFSessionError(0, "Closed session", None)

        encrypted_invoice = self.encrypt_invoice(invoice)

        invoice_hash = self.calculate_hash(invoice)
        encrypted_invoice_hash = self.calculate_hash(encrypted_invoice)

        request_data = {
            "invoiceHash": invoice_hash,
            "invoiceSize": len(invoice),
            "encryptedInvoiceHash": encrypted_invoice_hash,
            "encryptedInvoiceSize": len(encrypted_invoice),
            "encryptedInvoiceContent": base64.b64encode(encrypted_invoice).decode(),
            "offlineMode": False,
        }

        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/online/"+self.session["referenceNumber"]+"/invoices"
        resp = requests.post(
            url,
            json=request_data,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout*2,
        )

        self.client.showResponse("POST", url, resp)
        if resp.status_code != 202:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online upload)", None)

        data = resp.json()
        invoice_ref = data["referenceNumber"]
        return invoice_ref

    def statusSession(self):
        if not self.session["referenceNumber"]:
            raise KSEFSessionError(0, "Closed session", None)

        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/"+self.session["referenceNumber"]
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout*2,
        )

        self.client.showResponse("GET", url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online status)", None)
        data = resp.json()
        return data

    def statusInvoice(self, invoice_ref):
        if not self.session["referenceNumber"]:
            raise KSEFSessionError(0, "Closed session", None)

        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/"+self.session["referenceNumber"]+"/invoices/"+invoice_ref
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout*2,
        )

        self.client.showResponse("GET", url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online status)", None)
        data = resp.json()
        return data

    def status(self, invoice_ref=None):
        if invoice_ref is None:
            return self.statusSession()
        return self.statusInvoice(invoice_ref)

    def upoSession(self, referenceNumber=None):
        if referenceNumber is None:
            referenceNumber = self.session["referenceNumber"]
        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/"+referenceNumber+"/invoices/upo"
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout,
        )
        self.client.showResponse("GET", url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online upo)", None)
        return resp.text.encode("utf-8")

    def upoInvoice(self, referenceNumber=None, ksefNumber=None, ksefData=None):
        if referenceNumber is None:
            referenceNumber = self.session["referenceNumber"]
        if not referenceNumber or not (ksefNumber or ksefData):
            raise KSEFSessionError(0, "Bad arguments.", None)
        if ksefNumber is None:
            ksefNumber = ksefData["ksefNumber"]
        auth = self.client.getauthdata()
        url = self.client.apiurl+"/api/v2/sessions/"+referenceNumber+"/invoices/"+ksefNumber+"/upo"
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth["accessToken"]["token"],
            },
            timeout=self.client.timeout,
        )
        self.client.showResponse("GET", url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, "Blad komunikacji (session online upo)", None)
        return resp.text.encode("utf-8")

    def invoices(self, referenceNumber=None):
        if referenceNumber is None:
            referenceNumber = self.session["referenceNumber"]
        auth = self.client.getauthdata()
        pageSize = 10
        url = self.client.apiurl+f"/api/v2/sessions/{referenceNumber}/invoices?pageSize={pageSize}"
        headers={
            "Authorization": "Bearer "+auth["accessToken"]["token"],
        }
        result = []
        while True:
            resp = requests.get(
                url,
                headers=headers,
                timeout=self.client.timeout,
            )
            self.client.showResponse("GET", url, resp)
            if resp.status_code != 200:
                raise KSEFError(resp.status_code, "Blad komunikacji (session online upo)", None)
            data = resp.json()
            result.extend(data["invoices"])
            if not data.get("continuationToken"):
                break
            headers["x-continuation-token"] = data["continuationToken"]
        return result

    def failedInvoices(self, referenceNumber=None):
        if referenceNumber is None:
            referenceNumber = self.session["referenceNumber"]
        auth = self.client.getauthdata()
        pageSize = 10
        url = self.client.apiurl+f"/api/v2/sessions/{referenceNumber}/invoices/failed?pageSize={pageSize}"
        headers={
            "Authorization": "Bearer "+auth["accessToken"]["token"],
        }
        result = []
        while True:
            resp = requests.get(
                url,
                headers=headers,
                timeout=self.client.timeout,
            )
            self.client.showResponse("GET", url, resp)
            if resp.status_code != 200:
                raise KSEFError(resp.status_code, "Blad komunikacji (session online invoices failed)", None)
            data = resp.json()
            result.extend(data["invoices"])
            if not data.get("continuationToken"):
                break
            headers["x-continuation-token"] = data["continuationToken"]
        return result
