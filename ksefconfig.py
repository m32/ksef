#
# http://generatory.it/
#
import os
import sys
import json
import base64
import configparser

from cryptography import x509

class Config(configparser.ConfigParser):
    def __init__(self, firma:int=1, osoba:bool=False, initialize:bool=False):
        super().__init__()
        self.read('ksef.ini')

        self.firma = firma
        self.osoba = osoba
        self.version = self.get('ksef', 'version')
        self.url = self.get(self.version, 'url')
        self.kseftoken = self.get(f'firma{firma}', 'token', fallback=None)

        self.nip = self.get(f'firma{firma}', 'nip')
        self.nazwa = self.get(f'firma{firma}', 'nazwa')
        self.adres = self.get(f'firma{firma}', 'adres')

        self.pesel = self.get(f'firma{firma}', 'pesel')
        self.imie = self.get(f'firma{firma}', 'imie')
        self.nazwisko = self.get(f'firma{firma}', 'nazwisko')

        self.prefix = self.pesel if self.osoba else self.nip

        if os.path.exists(f'certificates-{self.version}.json'):
            with open(f'certificates-{self.version}.json', 'rt') as fp:
                self.certificates = json.loads(fp.read())
        else:
            self.certificates = []

        if not initialize:
            assert self.nip and self.pesel

    def loadcertificate(self, cert_data):
        cert_bytes = base64.b64decode(cert_data)
        certificate = x509.load_der_x509_certificate(cert_bytes)
        public_key = certificate.public_key()
        return certificate, public_key

    def getcertificte(self, token=True):
        for cert in self.certificates:
            if token:
                if 'KsefTokenEncryption' in cert['usage']:
                    return self.loadcertificate(cert['certificate'])
            elif 'SymmetricKeyEncryption' in cert['usage']:
                return self.loadcertificate(cert['certificate'])
        return None, None
