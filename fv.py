#!/usr/bin/env vpython3
import sys
import time
from random import randint
import datetime
from dateutil.tz import tzlocal, tzutc
from dateutil import parser

class Main:
    def faktura(self, f1, f2):
        now = datetime.datetime.now(tz=tzlocal())
        serial = (now - datetime.datetime(1970, 1, 1, tzinfo=tzutc())).total_seconds()

        vcnetto = randint(10, 100)*1.0
        vilosc = randint(1, 5)
        vnetto = vcnetto * vilosc
        vpvat = 23
        vvat = vnetto * vpvat / 100.0
        vbrutto = vnetto + vvat

        data = '''\
<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<Faktura
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns="http://crd.gov.pl/wzor/2025/06/25/13775/">
  <Naglowek>
    <KodFormularza kodSystemowy="FA (3)" wersjaSchemy="1-0E">FA</KodFormularza>
    <WariantFormularza>3</WariantFormularza>
    <DataWytworzeniaFa>{datawytworzenia}</DataWytworzeniaFa>
    <SystemInfo>eRTa 11.10</SystemInfo>
  </Naglowek>
  <Podmiot1>
    <DaneIdentyfikacyjne>
      <NIP>{snip}</NIP>
      <Nazwa>{snazwa}</Nazwa>
    </DaneIdentyfikacyjne>
    <Adres>
      <KodKraju>PL</KodKraju>
      <AdresL1>{sadres}</AdresL1>
    </Adres>
  </Podmiot1>
  <Podmiot2>
    <DaneIdentyfikacyjne>
      <NIP>{dnip}</NIP>
      <Nazwa>{dnazwa}</Nazwa>
    </DaneIdentyfikacyjne>
    <NrKlienta>2</NrKlienta>
    <JST>2</JST>
    <GV>2</GV>
  </Podmiot2>
  <Fa>
    <KodWaluty>PLN</KodWaluty>
    <P_1>{rmd}</P_1>
    <P_1M>dom</P_1M>
    <P_2>{serial}</P_2>
    <P_13_1>{vnetto:.2f}</P_13_1>
    <P_14_1>{vvat:.2f}</P_14_1>
    <P_15>{vbrutto:.2f}</P_15>
    <Adnotacje>
      <P_16>2</P_16>
      <P_17>2</P_17>
      <P_18>2</P_18>
      <P_18A>2</P_18A>
      <Zwolnienie>
        <P_19N>1</P_19N>
      </Zwolnienie>
      <NoweSrodkiTransportu>
        <P_22N>1</P_22N>
      </NoweSrodkiTransportu>
      <P_23>2</P_23>
      <PMarzy>
        <P_PMarzyN>1</P_PMarzyN>
      </PMarzy>
    </Adnotacje>
    <RodzajFaktury>VAT</RodzajFaktury>
    <FaWiersz>
      <NrWierszaFa>1</NrWierszaFa>
      <P_7>test</P_7>
      <P_8A>szt</P_8A>
      <P_8B>{vilosc}</P_8B>
      <P_9A>{vcnetto:.2f}</P_9A>
      <P_11>{vnetto:.2f}</P_11>
      <P_12>{vpvat}</P_12>
    </FaWiersz>
  </Fa>
</Faktura>
'''
        data = data.format(
            datawytworzenia=now.isoformat(),
            snip=f1.nip, snazwa=f1.nazwa, sadres=f1.adres,
            dnip=f2.nip, dnazwa=f2.nazwa,
            rmd=now.strftime('%Y-%m-%d'),
            serial=serial,
            vnetto=vnetto,
            vpvat=vpvat,
            vvat=vvat,
            vbrutto=vbrutto,
            vilosc=vilosc,
            vcnetto=vcnetto,
        )
        open(f'{f1.nip}-{f2.nip}-{serial}.xml', 'wt').write(data)

    def main(self):
        from ksefconfig import Config
        f1 = Config(int(sys.argv[1]))
        f2 = Config(int(sys.argv[2]))
        n = int(sys.argv[3])
        for i in range(n):
            self.faktura(f1, f2)
            time.sleep(2)

def main():
    cls = Main()
    cls.main()

if __name__ == '__main__':
    main()
