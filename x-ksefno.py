#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import sys
from lxml import etree

with open(sys.argv[1], 'rb') as fp:
    tree = etree.parse(fp)
    namespaces = tree.getroot().nsmap.copy()
    namespaces['doc'] = namespaces[None]
    del namespaces[None]
    odpowiedz = tree.xpath( '/doc:Potwierdzenie/doc:Dokument/doc:NumerKSeFDokumentu', namespaces=namespaces )
    print(odpowiedz[0].text)
