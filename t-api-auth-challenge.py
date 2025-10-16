#!/usr/bin/env vpython3
from ksef import Client
from ksef.api.auth import post_api_v2_auth_challenge

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    clt = Client(cfg.url)
    resp = post_api_v2_auth_challenge.sync(client=clt)
    print('post_api_v2_auth_challenge:', resp)

    data = resp.to_dict()
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
