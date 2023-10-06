#!/usr/bin/env vpython3
from random import randint
import datetime
from dateutil.tz import tzlocal, tzutc
from dateutil import parser

now = datetime.datetime.now(tz=tzlocal())
serial = (now - datetime.datetime(1970, 1, 1, tzinfo=tzutc())).total_seconds()

vcnetto = randint(10, 2000)*1.0
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
    xmlns="http://crd.gov.pl/wzor/2023/06/29/12648/">
  <Naglowek>
    <KodFormularza kodSystemowy="FA (2)" wersjaSchemy="1-0E">FA</KodFormularza>
    <WariantFormularza>2</WariantFormularza>
    <DataWytworzeniaFa>{datawytworzenia}</DataWytworzeniaFa>
    <SystemInfo>eRTa 11.10</SystemInfo>
  </Naglowek>
  <Podmiot1>
    <DaneIdentyfikacyjne>
      <NIP>8511172404</NIP>
      <Nazwa>gm</Nazwa>
    </DaneIdentyfikacyjne>
    <Adres>
      <KodKraju>PL</KodKraju>
      <AdresL1>gm-adres</AdresL1>
    </Adres>
  </Podmiot1>
  <Podmiot2>
    <DaneIdentyfikacyjne>
      <NIP>8521008161</NIP>
      <Nazwa>dm</Nazwa>
    </DaneIdentyfikacyjne>
    <Adres>
      <KodKraju>PL</KodKraju>
      <AdresL1>dm-adres</AdresL1>
    </Adres>
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
    rmd=now.strftime('%Y-%m-%d'),
    serial=serial,
    vnetto=vnetto,
    vpvat=vpvat,
    vvat=vvat,
    vbrutto=vbrutto,
    vilosc=vilosc,
    vcnetto=vcnetto,
)
open('{}.xml'.format(serial), 'wt').write(data)
