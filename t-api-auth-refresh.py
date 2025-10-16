#!/usr/bin/env vpython3
import sys
import json

from ksef import AuthenticatedClient
from ksef.api.auth import post_api_v2_auth_token_refresh

import sys
from ksefconfig import Config

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())

    clt = AuthenticatedClient(cfg.url, token=auth['refreshToken']['token'])
    resp = post_api_v2_auth_token_refresh.sync(client=clt)

    with open(f'{cfg.prefix}-auth.xml', 'wt') as fp:
        fp.write(json.dumps(resp.to_dict(), indent=4))

main()
