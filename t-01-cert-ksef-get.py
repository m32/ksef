#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import base64
import requests

import datetime
import requests

import sys
from ksefconfig import Config

def main():
    cfg = Config(1, False)

    dtnow = datetime.datetime.now(datetime.timezone.utc)
    dtdiff = datetime.timedelta(hours=1)
    if cfg.ksefcertvalidto is not None:
        dt = datetime.datetime.fromisoformat(cfg.ksefcertvalidto)
        if dt < dtnow - dtdiff or cfg.ksefcert is not None:
            return

    response = requests.get(
        f"{cfg.url}/api/v2/security/public-key-certificates",
        timeout=10
    )
    if response.status_code != 200:
        print(f'unhandled response: {response}')
        return

    certificates = response.json()
    for cert in certificates:
        if "SymmetricKeyEncryption" not in cert["usage"]:
            continue
        cfg.set(cfg.version, 'cert', cert["certificate"])
        cfg.set(cfg.version, 'validFrom', cert["validFrom"])
        cfg.set(cfg.version, 'validTo', cert["validTo"])
        with open('ksef.ini', 'wt') as fp:
            cfg.write(fp)
        break

main()
