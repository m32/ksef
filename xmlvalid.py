#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
import os
import sys
import getopt
import urllib.request
import base64
import zipfile
import io
from lxml import etree

top = os.getcwd()

def download(url):
    # http://crd.gov.pl/wzor/2014/12/22/1949/schemat.xsd
    if url[:7] == 'http://':
        fname = url.split('/')
        assert fname[2] in ('crd.gov.pl', 'jpk.mf.gov.pl')
        fname = '/'.join(fname[3:])
        filepath = '/'.join((top, fname))
    else:
        filepath = url
    #        print('download', url, filepath)
    if not os.path.isfile(filepath):
        dirname = '/'.join(filepath.split('/')[:-1])
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        print("Resolving URL '%s'" % url)
        response = urllib.request.urlopen(url)
        data = response.read()
        open(filepath, 'wb').write(data)
    return filepath

class DTDResolver(etree.Resolver):
    def resolve(self, url, id, context):
        filepath = download(url)
        return self.resolve_filename(filepath, context)

class Parser:
    namespaces={
        #        'dsig'  :"http://www.w3.org/2000/09/xmldsig#",
        #        'xsd'   :"http://www.w3.org/2001/XMLSchema",
        #        'soap'  :"http://www.w3.org/2003/05/soap-envelope",
    }

    def __init__(self, xml):
        self.xml = xml
        self.tree = etree.parse(io.BytesIO(xml))
        self.namespaces.update(self.tree.getroot().nsmap)

class Deklaracja:
    def __init__(self, xml):
        self.xml = xml
        self.xsd = None
        self.xsl = None
        self.url = None

        self.xsdformularz = None
        self.xsdwariant = None
        self.xsdwersja = None
        self.firmanip = None
        self.firmanazwa = None

        self.prepare()

    def prepare(self):
        self.tree = etree.parse(io.BytesIO(self.xml))
        self.root = self.tree.getroot()
        self.nsmap = self.root.nsmap.copy()
        try:
            self.url = self.root.nsmap[None]
            self.nsmap['doc'] = self.nsmap[None]
            del self.nsmap[None]
        except:
            pass

    def getxsd(self):
        if self.xsd:
            return self.xsd
        return download(self.url+'schemat.xsd')

    def getxsl(self):
        if self.xsl:
            return self.xsl
        return download(self.url+'styl.xsl')

    def validate(self):
        fxsd = self.getxsd()
        print('fxsd=', fxsd)
        xsdparser = etree.XMLParser(load_dtd=True)
        xsdparser.resolvers.add( DTDResolver() )

        schema_root = etree.XML(open(fxsd, 'rb').read(), xsdparser)
        schema = etree.XMLSchema(schema_root)

        xmlparser = etree.XMLParser(schema = schema)
        etree.clear_error_log()
        try:
            oot = etree.parse(io.BytesIO(self.xml), xmlparser)
        except etree.XMLSyntaxError as e:
            return e
        return None

    def showerror(self, e):
        for ee in e.error_log:
            print(ee.line, ee.column, ee.message)

    def html(self):
        fxsl = self.getxsl()

        xsdparser = etree.XMLParser(load_dtd=True)
        xsdparser.resolvers.add( DTDResolver() )

        xslt_root = etree.XML(open(fxsl, 'rb').read(), xsdparser)
        transform = etree.XSLT(xslt_root)

        result = transform(self.tree)
        result = etree.tostring(result)
        return result

    def info(self):
        self.info_naglowek()
        self.info_osoba()

    def info_naglowek(self):
        naglowek = '/doc:Deklaracja/doc:Naglowek'
        formularz = self.tree.xpath( naglowek+'/doc:KodFormularza', namespaces=self.nsmap )[0]
        wariant = self.tree.xpath( naglowek+'/doc:WariantFormularza', namespaces=self.nsmap )[0].text

        self.xsdformularz = formularz.text
        self.xsdwariant = wariant
        self.xsdwersja = formularz.get('wersjaSchemy')

    def info_osoba(self):
        path = '/doc:Deklaracja/doc:Podmiot1/etd:OsobaFizyczna'
        podmiot = self.tree.xpath( path, namespaces=self.nsmap )
        if podmiot:
            self.firmanip = self.tree.xpath( path+'/etd:NIP', namespaces=self.nsmap )[0].text
            imie = self.tree.xpath( path+'/etd:ImiePierwsze', namespaces=self.nsmap )[0].text
            nazwisko = self.tree.xpath( path+'/etd:Nazwisko', namespaces=self.nsmap )[0].text
            self.firmanazwa = imie+' '+nazwisko
        else:
            path = '/doc:Deklaracja/doc:Podmiot1/etd:OsobaNiefizyczna'
            podmiot = self.tree.xpath( path, namespaces=self.nsmap )
            self.firmanip = self.tree.xpath( path+'/etd:NIP', namespaces=self.nsmap )[0].text
            self.firmanazwa = self.tree.xpath( path+'/etd:PelnaNazwa', namespaces=self.nsmap )[0].text

class XADESParser(Parser):
    def __init__(self, xml):
        Parser.__init__(self, xml)
        self.dokument = None
        
        ns = [
            '/ds:Signature',
            '/ds:SignedInfo',
            '/ds:Reference',
            ]
        path = ''.join(ns)
        odpowiedz = self.tree.xpath( path, namespaces=self.namespaces )
        odpowiedz = odpowiedz[0]
        ref = odpowiedz.get('URI')[1:]
        ns = [
            '/ds:Signature',
            '/ds:Object',
            ]
        path = ''.join(ns)
        print(ref)
        for odpowiedz in self.tree.xpath( path, namespaces=self.namespaces ):
            print(odpowiedz.get('Id'))
            if ref == odpowiedz.get('Id'):
                print(dir(odpowiedz))
                dokument = odpowiedz.text
                print('dokument', dokument)
                dokument = base64.decodestring(dokument)
                fp = io.BytesIO(dokument)
                zfp = zipfile.ZipFile(fp, 'r', zipfile.ZIP_DEFLATED)
                self.dokument = zfp.read(zfp.namelist()[0])
                return

def main():
    opts, args = getopt.getopt(sys.argv[1:], '?', [
        'help',
        'validate',
        'xml=',
        'xsd=',
        'html=',
        'xsl=',
        'xades=',
    ])
    if args or '-?' in opts or '--help' in opts:
        print('''\
usage: %s opcje

opcje:
--help          = pokaz ten tekst
-?              = pokaz ten tekst
--validate      = sprawdz poprawnosc pliku (--xml|--xades)
--xsd=          = nazwa pliku xsd
--html=plik     = gdzie zapisac plik html
--xsl=          = nazwa pliku xsl
--xades=plik    = wczytaj plik xml z podpisanego pliku (xades)
--xml=plik      = wczytaj plik xml
''' % sys.argv[0])
        return
    dek = None
    for o, a in opts:
        if o == '--xml':
            xml=open(a, 'rb').read()
            dekok = Deklaracja(xml)
        elif o == '--xsd':
            dekok.xsd = a
        elif o == '--xsl':
            dekok.xsl = a
        elif o == '--xades':
            xml = open(a, 'rb').read()
            p = XADESParser(xml)
            dekok = Deklaracja(p.dokument)
        elif o == '--validate':
            print('*'*20, 'validate')
            e = dekok.validate()
            if e:
                dekok.showerror(e)
            else:
                print('OK')
        elif o == '--html':
            print('*'*20, 'html')
            lines = io.BytesIO(dekok.html()).readlines()
            html = []
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    html.append(line)
            html = b'\n'.join(html)
            open(a, 'wb').write(html)
            print('OK')

main()
