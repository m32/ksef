import os
import json

import sqlalchemy as sa

from . import appdb, models, client2

class Version:
    test = 0
    demo = 1
    prod = 2

class KSEFFirma(client2.KSEF):
    def __init__(self, version, firma):
        super().__init__(version)
        self.sess = appdb.SessionLocal()
        t = models.firma.Firma
        stmt = sa.select(
            t
        ).where(
            t.id == firma
        )
        self.firma = self.sess.execute(stmt).scalar()

    def dbNIP(self):
        return self.firma.nip

    def dbLoadAuth(self):
        if not os.path.exists(f'config/x-{self.firma.nip}-auth.json') or not os.path.exists(f'config/x-{self.firma.nip}-reedem.json'):
            return None, None
        with open(f'config/x-{self.firma.nip}-auth.json', 'rt') as fp:
            auth = json.loads(fp.read())
        with open(f'config/x-{self.firma.nip}-reedem.json', 'rt') as fp:
            reedem = json.loads(fp.read())
        return reedem, auth

    def dbSaveAuth(self, reedem, auth):
        with open(f'config/x-{self.firma.nip}-reedem.json', 'wt') as fp:
            fp.write(json.dumps(reedem))
        auth = self.refresh(reedem)
        with open(f'config/x-{self.firma.nip}-auth.json', 'wt') as fp:
            fp.write(json.dumps(auth))

    def dbLoadSession(self):
        if not os.path.exists(f'config/x-{self.firma.nip}-session.json'):
            return None
        with open(f'config/x-{self.firma.nip}-session.json', 'rt') as fp:
            session = json.loads(fp.read())
        return session

    def dbLoadKSeFCert(self, auth):
        with open('certificates-test.json', 'rt') as fp:
            certs = json.loads(fp.read())
        what = {
            True: 'KsefTokenEncryption',
            False: 'SymmetricKeyEncryption',
        }[auth]
        for cert in certs:
            if what in cert['usage']:
                data = cert['certificate'].encode('ascii')
                return data
        return None

    def dbLoadCert(self):
        return (
            self.firma.firmacert,
            self.firma.firmakey,
            self.firma.firmapass.encode('ascii')
        )

