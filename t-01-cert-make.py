#!/usr/bin/env vpython3
import os
import sys
from ksefconfig import Config
import ksefcert

def main():
    print("Cenerating certificates")

    cfg = Config(int(sys.argv[1]))
    cls = ksefcert.Certificate()
    for (fn, ln, cn, nip, pesel) in (
        (None, None, cfg.nazwa, cfg.nip, None), # firma
        (cfg.imie, cfg.nazwisko, cfg.imie+' '+cfg.nazwisko, None, cfg.pesel), # osoba
    ):
        name = cfg.nazwa + ('-user' if not nip else '')
        if os.path.exists(f'config/{name}.key.pem'):
            continue
        pk = cls.key_create()
        cert = cls.createcert(pk, fn, ln, cn, nip, pesel)
        cls.key_save(f'{name}.key.pem', pk, "1234")
        cls.cert_save(f'{name}.crt.pem', cert)
        cls.pk12_save(b'cert', cert, pk, f'{name}.p12', "1234")

main()
