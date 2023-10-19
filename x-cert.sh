#!/bin/bash
# Za podpis można uznać certyfikat
# Który posiada w opisie podmiotu obowiązkowo pola imiona (OID.2.5.4.42) i nazwisko (OID.2.5.4.4)
# oraz opcjonalnie numer seryjny (OID.2.5.4.5) zgodnie z formatem:
#   (PNOPL|PESEL).*?(?<number>\\d{11})
#   lub (TINPL|NIP).*?(?<number>\\d{10})
#
# Za pieczęć można uznać certyfikat
# Który posiada w opisie podmiotu obowiązkowe pole identyfikatora organizacji (OID.2.5.4.97) zgodnie z formatem:
#   (VATPL).*?(?<number>\\d{10})
#
# PESEL=53081422566
# NIP=5330957838
# VAT=9450000157
cert-pesel(){
rm -f x-cert-pesel-key.pem x-cert-pesel.csr x-cert-pesel.pem x-cert-pesel.p12
openssl req -newkey rsa:2048 -nodes -keyout x-cert-pesel-key.pem -out x-cert-pesel.csr \
    -subj "/C=PL/ST=Mazowieckie/L=Warszawa/O=firmafirmowa/OU=IT/CN=Jan Babacki/2.5.4.42=Jan/2.5.4.4=Babacki/2.5.4.5=PESEL-53081422566"
openssl x509 -signkey x-cert-pesel-key.pem -in x-cert-pesel.csr -req -days 3650 -out x-cert-pesel.pem
openssl pkcs12 -export -out x-cert-pesel.p12 -inkey x-cert-pesel-key.pem -in x-cert-pesel.pem
}

cert-nip(){
rm -f x-cert-nip-key.pem x-cert-nip.csr x-cert-nip.pem x-cert-nip.p12
openssl req -newkey rsa:2048 -nodes -keyout x-cert-nip-key.pem -out x-cert-nip.csr \
    -subj "/C=PL/ST=Mazowieckie/L=Warszawa/O=firmafirmowa/OU=IT/CN=Firma Firmowa/emailAddress=biuro@firmafirmowa.pl/2.5.4.5=NIP-5330957838"
openssl x509 -signkey x-cert-nip-key.pem -in x-cert-nip.csr -req -days 3650 -out x-cert-nip.pem
openssl pkcs12 -export -out x-cert-nip.p12 -inkey x-cert-nip-key.pem -in x-cert-nip.pem
}

cert-vat(){
rm -f x-cert-vat-key.pem x-cert-vat.csr x-cert-vat.pem x-cert-vat.p12
openssl req -newkey rsa:2048 -nodes -keyout x-cert-vat-key.pem -out x-cert-vat.csr \
    -subj "/C=PL/ST=Mazowieckie/L=Warszawa/O=firmafirmowa/OU=IT/CN=Firma Firmowa/emailAddress=biuro@firmafirmowa.pl/2.5.4.97=VAT-9450000157"
openssl x509 -signkey x-cert-vat-key.pem -in x-cert-vat.csr -req -days 3650 -out x-cert-vat.pem
openssl pkcs12 -export -out x-cert-vat.p12 -inkey x-cert-vat-key.pem -in x-cert-vat.pem
}

echo "Hasło musi być zgodne z tym co jest wpisane w x-sign-endesive-xml.py, czyli: 12345678"
cert-pesel
cert-nip
cert-vat
