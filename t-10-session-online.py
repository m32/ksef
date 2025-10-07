#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import json
import os
import sys
import datetime
import hashlib
import base64
import requests
from cryptography import x509
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class KSeFError(Exception):
    def __init__(self, msg, text):
        self.msg = msg
        self.text = text


class KSeFSessionError(KSeFError):
    pass


class KSeFUploadError(KSeFError):
    pass


class KSeFInvoiceSender:
    def __init__(self, cfg):
        self.cfg = cfg
        # Wczytaj tokeny uwierzytelniania
        with open(f"{cfg.prefix}-auth.json", "rt") as fp:
            self.auth = json.loads(fp.read())

        self.access_token = self.auth["accessToken"]["token"]
        self.session_ref_number = None

        if os.path.exists(f"{self.cfg.prefix}-session.json"):
            with open(f"{self.cfg.prefix}-session.json", "rt") as fp:
                session = json.loads(fp.read())
            dtnow = datetime.datetime.now(datetime.timezone.utc)
            dtdiff = datetime.timedelta(minutes=15)
            dt = datetime.datetime.fromisoformat(session['validUntil'])
            if dt < dtnow - dtdiff:
                session = None
        else:
            session = None
        if session is None:
            session = {
                'symmetric_key': base64.b64encode(os.urandom(32)).decode(),
                'iv': base64.b64encode(os.urandom(16)).decode(),
                'referenceNumber': None,
                'validUntil': None,
                'refs': {},
            }
        self.session = session

    def save_session(self):
        with open(f"{self.cfg.prefix}-session.json", "wt") as fp:
            fp.write(json.dumps(self.session))

    def open_session(self):
        public_key = self.get_ksef_public_key()

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
            "encryption": {
                "encryptedSymmetricKey": base64.b64encode(encrypted_symmetric_key).decode(),
                "initializationVector": self.session['iv'],
            },
        }

        response = requests.post(
            f"{self.cfg.url}/api/v2/sessions/online",
            json=request_data,
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=30,
        )

        print(f"Open session: {response}")
        if response.status_code != 201:
            raise KSeFSessionError('Error opening session.', response.text)

        data = response.json()
        self.session["referenceNumber"] = data["referenceNumber"]
        self.session["validUntil"] = data["validUntil"]
        self.save_session()

    def close_session(self):
        if not self.session["referenceNumber"]:
            return

        response = requests.post(
            f'{self.cfg.url}/api/v2/sessions/online/{self.session["referenceNumber"]}/close',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=15,
        )
        
        if os.path.exists(f"{self.cfg.prefix}-session.json"):
            os.unlink(f"{self.cfg.prefix}-session.json")

    def get_ksef_public_key(self):
        cert_bytes = base64.b64decode(self.cfg.ksefcert)
        certificate = x509.load_der_x509_certificate(cert_bytes)
        public_key = certificate.public_key()
        return public_key

    def calculate_hash(self, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        return base64.b64encode(hashlib.sha256(data).digest()).decode()

    def encrypt_invoice(self, invoice_bytes):
        cipher = Cipher(
            algorithms.AES(base64.b64decode(self.session['symmetric_key'])),
            modes.CBC(base64.b64decode(self.session['iv'])),
            backend=default_backend()
        )
        encryptor = cipher.encryptor()

        pad = len(invoice_bytes) % 16
        if pad:
            padding_length = 16 - pad
            invoice_bytes += bytes([padding_length] * padding_length)

        encrypted_invoice = encryptor.update(invoice_bytes) + encryptor.finalize()

        # Szyfruj klucz symetryczny kluczem publicznym RSA
        public_key = self.get_ksef_public_key()
        encrypted_symmetric_key = public_key.encrypt(
            base64.b64decode(self.session['symmetric_key']),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return encrypted_invoice

    def send_invoice(self, invoice):
        if not self.session["referenceNumber"]:
            raise KSeFSessionError("Closed session", None)

        with open(invoice, "rb") as f:
            invoice_xml = f.read()

        encrypted_invoice = self.encrypt_invoice(invoice_xml)

        invoice_hash = self.calculate_hash(invoice_xml)
        encrypted_invoice_hash = self.calculate_hash(encrypted_invoice)

        request_data = {
            "invoiceHash": invoice_hash,
            "invoiceSize": len(invoice_xml),
            "encryptedInvoiceHash": encrypted_invoice_hash,
            "encryptedInvoiceSize": len(encrypted_invoice),
            "encryptedInvoiceContent": base64.b64encode(encrypted_invoice).decode(),
            "offlineMode": False,
        }

        response = requests.post(
            f'{self.cfg.url}/api/v2/sessions/online/{self.session["referenceNumber"]}/invoices',
            json=request_data,
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=30,
        )

        print(f"Upload Status: {response}")
        if response.status_code != 202:
            print(response.text)
            raise KSeFUploadError("❌ Upload error", response.text)
        result = response.json()
        invoice_ref = result["referenceNumber"]
        self.session['refs'][invoice] = invoice_ref
        self.save_session()

    def check_invoice_status(self, invoice):
        invoice_ref = self.session['refs'][invoice]
        response = requests.get(
            f'{self.cfg.url}/api/v2/sessions/{self.session["referenceNumber"]}/invoices/{invoice_ref}',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=15,
        )

        print(f'INV Status: {response}')
        if response.status_code == 200:
            del self.session['refs'][invoice]
            data = response.json()
            with open(f'{invoice}.ref', 'wt') as fp:
                fp.write(json.dumps(data))
            self.save_session()
            if data['status']['code'] == 200:
                response = requests.get(data['upoDownloadUrl'])
                if response.status_code == 200:
                    with open(f'{invoice}.upo', 'wt') as fp:
                        fp.write(response.text)
            return True
        return False

    def upo(self, invoice):
        with open(f'{invoice}.ref', 'rt') as fp:
            data = json.loads(fp.read())
        if data['status']['code'] != 200:
            return
        response = requests.get(
            f'{self.cfg.url}/api/v2/sessions/{self.session["referenceNumber"]}/invoices/ksef/{data["ksefNumber"]}/upo',
            headers={
                "Authorization": f"Bearer {self.access_token}",
            },
            timeout=15,
        )
        print(f'UPO response: {response}')
        if response.status_code != 200:
            print(response.text)
            return
        with open(f'{invoice}.upo', 'wt') as fp:
            fp.write(response.text)

def main():
    from ksefconfig import Config
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')

    cls = KSeFInvoiceSender(cfg)

    import getopt
    opts, args = getopt.getopt(sys.argv[3:], 'ocs:t:u:')
    for o, a in opts:
        if o == '-o':
            # open
            cls.open_session()
        elif o == '-c':
            # close
            cls.close_session()
        elif o == '-s':
            # send
            cls.send_invoice(a)
        elif o == '-t':
            # status
            cls.check_invoice_status(a)
        elif o == '-u':
            # upo
            cls.upo(a)

if __name__ == "__main__":
    main()
