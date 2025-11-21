#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import json
import random
import datetime
import base64
import requests
import dateutil

import sys
from ksefconfig import Config

def nip():
    prefix = [
        "107", "108", "109", "111", "112", "113", "114", "115", "116", "117", "118", "119", "121", "122", "123", "124",
        "125", "154", "156", "157", "158", "337", "338", "339", "341", "342", "355", "356", "375", "376", "377", "378",
        "379", "381", "389", "392", "393", "394", "416", "417", "496", "497", "509", "511", "512", "519", "521", "522",
        "523", "524", "525", "526", "527", "528", "529", "531", "532", "533", "534", "535", "536", "566", "567", "568",
        "569", "572", "601", "701", "757", "758", "759", "761", "762", "774", "776", "796", "797", "798", "799", "811",
        "812", "821", "822", "823", "826", "837", "838", "931", "932", "948", "951", "952", "965", "971", "978"
    ]

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    while True:
        base = f'{prefix[random.randint(0, len(prefix)-1)]}{random.randint(0, 999999):06d}'
        crc = sum([int(b)*w for b, w in zip(base, weights)]) % 11
        if crc <= 9:
            break
    return base + chr(crc+48)


def pesel(dt=None, sex=0, rnd=0):
    if dt is None:
        dtstart = datetime.datetime(1900, 1, 1)
        dtend = datetime.datetime.now()
        n = (dtend - dtstart).days-1
        start = random.randint(0, n)
        stop = random.randint(0, n)
        if start > stop:
            start, stop = stop, start
        dt = (dtstart + datetime.timedelta(days=random.randint(start, stop))).date()

    if sex == 0:
        sex = random.randint(0, 9)
    if sex == 1:
        sex = random.randint(0, 4) * 2 + 1
    elif sex == 2:
        sex = random.randint(0, 4) * 2

    y = dt.year % 100
    m = dt.month
    d = dt.day
    if dt.year >= 1800 and dt.year <= 1899:
        m += 80
    elif dt.year >= 2000 and dt.year <= 2099:
        m += 20
    elif dt.year >= 2100 and dt.year <= 2199:
        m += 40
    elif dt.year >= 2200 and dt.year <= 2299:
        m += 60;

    if rnd == 0:
        rnd = random.randint(0, 999)
    base = f'{y:02d}{m:02d}{d:02d}{rnd:03d}{sex}'
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    n = sum([int(b)*w for b, w in zip(base, weights)])
    crc = 10 - (n % 10)
    if crc == 10:
        crc = 0
    return base+chr(crc+48)


def main():
    firma = int(sys.argv[1], 10)
    cfg = Config(1, False, True)

    if not cfg.certificates:
        resp = requests.get(
            f"{cfg.url}/api/v2/security/public-key-certificates",
            timeout=10
        )
        if resp.status_code != 200:
            print(f'unhandled response: {response}')
            return

        with open(f'certificates-{cfg.version}.json', 'wt') as fp:
            fp.write(json.dumps(resp.json()))

    if not cfg.get(f'firma{firma}', 'nip'):
        cfg.set('firma{firma}', 'nip', nip())
    if not cfg.get(f'firma{firma}', 'pesel'):
        cfg.set('firma{firma}', 'pesel', pesel(datetime.datetime(1950, 1, 12), 1))

    with open('ksef.ini', 'wt') as fp:
        cfg.write(fp)

main()
