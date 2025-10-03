import sys
import configparser

firma = sys.argv[1]
del sys.argv[1]

ini = configparser.ConfigParser()
ini.read('ksef.ini')

version = ini.get('ksef', 'version')

url = ini.get(version, 'url')

nip = ini.get(f'firma{firma}', 'nip')
nazwa = ini.get(f'firma{firma}', 'nazwa')

pesel = ini.get(f'firma{firma}', 'pesel')
imie = ini.get(f'firma{firma}', 'imie')
nazwisko = ini.get(f'firma{firma}', 'nazwisko')

if len(sys.argv)>1 and sys.argv[1] == '--osoba':
    del sys.argv[1]
    prefix = pesel
else:
    prefix = nip
