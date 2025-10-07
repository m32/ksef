#
# http://generatory.it/
#
import sys
import configparser

class Config(configparser.ConfigParser):
    def __init__(self, firma:int=1, osoba:bool=False):
        super().__init__()
        self.read('ksef.ini')

        self.firma = firma
        self.osoba = osoba
        self.version = self.get('ksef', 'version')
        self.url = self.get(self.version, 'url')
        self.ksefcert = self.get(self.version, 'cert', fallback=None)
        self.ksefcertvalidfrom = self.get(self.version, 'validFrom', fallback=None)
        self.ksefcertvalidto = self.get(self.version, 'validTo', fallback=None)

        self.nip = self.get(f'firma{firma}', 'nip')
        self.nazwa = self.get(f'firma{firma}', 'nazwa')
        self.adres = self.get(f'firma{firma}', 'adres')

        self.pesel = self.get(f'firma{firma}', 'pesel')
        self.imie = self.get(f'firma{firma}', 'imie')
        self.nazwisko = self.get(f'firma{firma}', 'nazwisko')

        self.prefix = self.pesel if self.osoba else self.nip
