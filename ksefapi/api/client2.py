import os
import time
import json
from binascii import unhexlify
import datetime
import hashlib
from base64 import b64encode, b64decode

from asn1crypto import core
from lxml import etree
from dateutil import parser, tz
import requests
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
from cryptography import x509
from cryptography.hazmat import backends
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding, ec
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.x509.oid import NameOID

#from lib.libs.xades import xadesbes2
from endesive import xades

class KSEFError(Exception):
    def __init__(self, rc, text, jsontext=None):
        self.rc = rc
        self.text = text
        ecode = -1
        emsg = 'Brak opisu bledu'
        if jsontext is not None:
            try:
                data = json.loads(jsontext)
                errors = data["exception"]["exceptionDetailList"]
                ecode = errors[0]["exceptionCode"]
                emsg = errors[0]["exceptionDescription"].encode('cp1250')
            except:
                print('*'*40, 'KSEFError')
                print(jsontext)
                import traceback; traceback.print_exc()
        self.ecode = ecode
        self.emsg = emsg

    def __str__(self):
        return 'KSEFError(%s, %s)'%(self.rc, self.text)
    __repr__ = __str__

class KSEFSessionError(KSEFError):
    pass

class KSEFUploadError(KSEFError):
    pass

class KSeFZipCreateError(KSEFError):
    pass

class KSeFZipSizeError(KSEFError):
    pass


def u2a(u):
    return u.encode('ascii')

def u2adict(dct):
    result = {}
    for k, v in dct.items():
        if type(v) == type({}):
            v = u2adict(v)
        elif type(v) == type(u''):
            v = v.encode('cp1250')
        result[k.encode('cp1250')] = v
    return result

def to_bytes(val, width, byteorder):
    fmt = '%%0%dx' % (width // 4)
    # prepend zero (0) to the width, to zero-pad the output
    s = unhexlify(fmt % val)

    if byteorder == 'little':
        s = s[::-1]
    return s

class KSEF:
    debug = False
    def __init__(self, version):
        if self.debug:
            http_client.HTTPConnection.debuglevel = 1
        self.timeout = 15
        self.apiurl = {
            'test': 'https://api-test.ksef.mf.gov.pl/v2',
            'demo': 'https://api-demo.ksef.mf.gov.pl/v2',
            'prod': 'https://api.ksef.mf.gov.pl/v2',
        }[version]

    def showResponse(self, op, url, resp):
        if self.debug:
            print('*'*20, op, url)
            print("rc.code=", resp.status_code)
            print('rc.headers=', resp.headers)
            print('rc.text=', resp.text)

    def certificate(self):
        url = self.apiurl+"/api/v2/security/public-key-certificates"
        resp = requests.get(
            url=url,
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (certificate)')
            return

        certificates = resp.json()
        for cert in certificates:
            if "SymmetricKeyEncryption" not in cert["usage"]:
                continue
            #cert["certificate"])
            #cert["validFrom"])
            #cert["validTo"])
            return cert
        raise KSEFError(-2, 'Brak certyfikatu')

    def challenge(self):
        url = self.apiurl+'/api/v2/auth/challenge'
        resp = requests.post(
            url,
            timeout=self.timeout
        )
        self.showResponse('POST', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (challenge)', resp)
        data = resp.json()

        policy = '''\
  <AuthorizationPolicy>
    <AllowedIps>
      <Ip4Address>37.30.32.28</Ip4Address>
      <Ip4Range>37.30.32.28-37.30.32.28</Ip4Range>
      <Ip4Mask>37.30.32.28/32</Ip4Mask>
    </AllowedIps>
  </AuthorizationPolicy>
'''
        policy = ''

        auth = '''\
<?xml version="1.0" encoding="utf-8"?>
<AuthTokenRequest xmlns="http://ksef.mf.gov.pl/auth/token/2.0">
  <Challenge>%(challenge)s</Challenge>
  <ContextIdentifier>
    <Nip>%(nip)s</Nip>
  </ContextIdentifier>
  <SubjectIdentifierType>certificateSubject</SubjectIdentifierType>
%(policy)s
</AuthTokenRequest>
'''%dict(
        challenge=data['challenge'],
        nip=self.dbNIP(),
        policy=policy,
)
        return ' '.join(auth.split())

    def xades(self, challengedata, cert, key, password):
        challengedata = challengedata.encode('utf-8')
        xkey = load_pem_private_key(key, password, backends.default_backend())
        xcert = x509.load_pem_x509_certificate(cert, backends.default_backend())
        certcontent = xcert.public_bytes(serialization.Encoding.DER)

        if isinstance(xkey, rsa.RSAPrivateKey):
            signaturemethod = None
        else:
            signaturemethod = 'http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256'

        def signproc(tosign, algosig):
            if isinstance(xkey, rsa.RSAPrivateKey):
                sig = xkey.sign(
                    tosign,
                    padding.PKCS1v15(),
                    getattr(hashes, algosig.upper())(),
                )
            else:
                sig = xkey.sign(
                    tosign,
                    ec.ECDSA(getattr(hashes, algosig.upper())())
                )
                length = 32 #=256/8 czyli aes-256 TODO zamienic na zmienna zalezna od dlugosci klucza
                d = core.load(sig)
                dr = to_bytes(d[0].native, length, byteorder="big")
                ds = to_bytes(d[1].native, length, byteorder="big")
                sig = dr+ds
            return sig

        cls = xades.BES()
        doc = cls.enveloping(
            "dokument.xml",
            challengedata,
            "application/xml",
            xcert,
            certcontent,
            signproc,
            False,
            True,
            signaturemethod=signaturemethod,
        )
        data = etree.tostring(doc, encoding="UTF-8", xml_declaration=True, standalone=False)

        url = self.apiurl+'/api/v2/auth/xades-signature?verifyCertificateChain=false'
        resp = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/xml",
            },
            timeout=self.timeout
        )
        self.showResponse('POST', url, resp)
        if resp.status_code != 202:
            raise KSEFError(resp.status_code, 'Blad komunikacji (xades)', resp)
        data = resp.json()
        return data

    def reference(self, xadesauth):
        url = self.apiurl+'/api/v2/auth/'+xadesauth["referenceNumber"]
        resp = requests.get(
            url=url,
            headers={
                "Authorization": "Bearer "+xadesauth['authenticationToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code not in (200, 202):
            raise KSEFError(resp.status_code, 'Blad komunikacji (reference)', resp)
        data = resp.json()
        return data

    def reedem(self, xadesauth):
        url = self.apiurl+'/api/v2/auth/token/redeem'
        resp = requests.post(
            url=url,
            headers={
                "Authorization": "Bearer "+xadesauth['authenticationToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('POST', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (reedem)', resp)
        data = resp.json()
        return data

    def refresh(self, reedemdata):
        url = self.apiurl+'/api/v2/auth/token/refresh'
        resp = requests.post(
            url,
            headers={
                "Authorization": "Bearer "+reedemdata['refreshToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (refresh)', resp)
        data = resp.json()
        return data

    def auth_token(self, challengedata, public_key, token):
        dt = dateutil.parser.isoparse(challengedata['timestamp'])
        t = int(dt.timestamp()*1000)

        token = token+("%d"%d)
        encrypted_token = public_key.encrypt(
            token,
            apadding.OAEP(
                mgf=apadding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        data = {
            'challenge': challengedata['challenge'],
            'contextIdentifier': {
                'type': 'Nip',
                'value': cfg.nip,
            },
            'encryptedToken': base64.b64encode(encrypted_token).decode(),
            #'authorizationPolicy': ?
        }

        url = self.apiurl+"/api/v2/auth/ksef-token"
        resp = requests.post(
            url,
            json=data
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 202:
            raise KSEFError(resp.status_code, 'Blad komunikacji (refresh)', resp)
        if resp.status_code != 202:
            print(f'unhandled response: {resp}')
            return
        data = resp.json()

    def certlimit(self):
        auth = self.getauthdata()

        url = self.apiurl+'/api/v2/certificates/limits'
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (cert limit)', resp)
        data = resp.json()
        return data

    def certenrollments(self):
        auth = self.getauthdata()

        url = self.apiurl+'/api/v2/certificates/enrollments/data'
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (cert enrollments)', resp)
        data = resp.json()
        return data

    def certlist(self, certtype="Authentication"):
        auth = self.getauthdata()

        result = []
        pageSize = 10
        pageOffset = 0
        while True:
            data = {
                #"status": "Active", # Active, Blocked, Revoked, Expired
                #"status": "Revoked", # Active, Blocked, Revoked, Expired
                #"expiresAfter": dtnow+dtdiff).isoformat(), # data konca waznosci certyfikatu (opcjonalna)
                #"name": "", # nazwa certyfikatu (opcjonalny)
                "type": certtype, # typ certyfikatu (Authentication, Offline) (opcjonalny)
                #"certificateSerialNumber": "", # numer seryjny certyfikatu (opcjonalny)
            }
            url = self.apiurl+'/api/v2/certificates/query?pageSize=%d&pageOffset=%d'%(pageSize, pageOffset)
            resp = requests.post(
                url,
                json=data,
                headers={
                    "Authorization": "Bearer "+auth['accessToken']['token'],
                },
                timeout=self.timeout
            )
            self.showResponse('POST', url, resp)
            if resp.status_code != 200:
                raise KSEFError(resp.status_code, 'Blad komunikacji (certlist)', resp)
            data = resp.json()
            result.extend(data['certificates'])
            if not data['hasMore']:
                break
            pageOffset += pageSize
        return result

    def sessionlist(self):
        auth = self.getauthdata()

        url = self.apiurl+'/api/v2/auth/sessions'
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (session list)', resp)
        data = resp.json()
        return data['items']

    def falist(self, subject=2, dtfrom=None, dtto=None):
        # 1=wystawione
        # 2=odebrane
        # 3=
        auth = self.getauthdata()

        if dtto is None:
            now = datetime.datetime.now(tz.tzutc())
            dtto = datetime.datetime(year=dtnow.year, month=dtnow.month, dtday=now.day)
        if dtfrom is None:
            dtdiff = datetime.timedelta(days=days)
            dt = dtto-dtdiff

        result = []
        pageSize = 10
        pageOffset = 0
        while True:
            data = {
                'dateRange': {
                    'dateType': 'Issue',
                    'from': dtfrom.isoformat(),
                    'to': dtto.isoformat(),
                },
                'subjectType': 'Subject%d'%subject,
            }
            url = self.apiurl+'/api/v2/invoices/query/metadata?pageOffset=%d&pageSize=%d'%(pageOffset, pageSize)
            resp = requests.post(
                url,
                json=data,
                headers={
                    "Authorization": "Bearer "+auth['accessToken']['token'],
                },
                timeout=self.timeout
            )
            self.showResponse('POST', url, resp)
            if resp.status_code != 200:
                raise KSEFError(resp.status_code, 'Blad komunikacji (falist)', resp)
            data = resp.json()
            result.extend(data['invoices'])
            if data['hasMore']:
                pageOffset += pageSize
            else:
                break
        return result

    def faget(self, ksefNumber):
        auth = self.getauthdata()

        url = self.apiurl+'/api/v2/invoices/ksef/'+ksefNumber
        resp = requests.get(
            url,
            headers={
                "Authorization": "Bearer "+auth['accessToken']['token'],
            },
            timeout=self.timeout
        )
        self.showResponse('GET', url, resp)
        if resp.status_code != 200:
            raise KSEFError(resp.status_code, 'Blad komunikacji (faget)', resp)
        return resp.text

    def getauthdata(self):
        dtnow = datetime.datetime.now(tz.tzutc())
        reedem, auth = self.dbLoadAuth()
        if auth is not None and reedem is not None:
            dtexp = parser.isoparse(auth['accessToken']['validUntil'])
            dtexp -= datetime.timedelta(minutes=3)
            if dtexp > dtnow:
                #print('auth not expired', dtexp)
                #print(dtexp.astimezone(tz.tzlocal()))
                return auth
            else:
                #print('reedem', dtexp)
                #print(dtexp.astimezone(tz.tzlocal()))
                dtexp = parser.isoparse(reedem['refreshToken']['validUntil'])
                dtexp -= datetime.timedelta(hours=1)
                if dtexp > dtnow:
                    #print('reedem not expired', dtexp)
                    #print(dtexp.astimezone(tz.tzlocal()))
                    auth = self.refresh(reedem)
                    self.dbSaveAuth(reedem, auth)
                    return auth

        #print('auth full')
        challenge = self.challenge()
        print('challenge', challenge)
        cert, key, password = self.dbLoadCert()
        xades = self.xades(challenge, cert, key, password)
        print('xades', xades)
        reference = self.reference(xades)
        reedem = self.reedem(xades)
        auth = {'accessToken': reedem['accessToken']}
        self.dbSaveAuth(reedem, auth)
        return auth
