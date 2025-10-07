#!/usr/bin/env vpython3
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    resp = requests.post(
        cfg.url+'/api/v2/auth/challenge',
        timeout=5
    )
    print('post_api_v2_auth_challenge:', resp)
    data = resp.json()
    print('challenge', data['challenge'])
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

    auth = f'''\
<?xml version="1.0" encoding="utf-8"?>
<AuthTokenRequest xmlns="http://ksef.mf.gov.pl/auth/token/2.0">
  <Challenge>{data['challenge']}</Challenge>
  <ContextIdentifier>
    <Nip>{cfg.nip}</Nip>
  </ContextIdentifier>
  <SubjectIdentifierType>certificateSubject</SubjectIdentifierType>
{policy}
</AuthTokenRequest>
'''
    with open(f'{cfg.prefix}-auth.xml', 'wt') as fp:
        fp.write(auth)

main()
