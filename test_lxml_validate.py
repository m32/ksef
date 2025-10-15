from lxml import etree

# Ścieżka do lokalnego pliku XSD
SCHEMA_PATH = "schemat.xsd"

# Przykładowy dokument XML zgodny ze schematem (fragment z kodem kraju UE)

EXAMPLE_XML = '''<?xml version="1.0" encoding="UTF-8"?>
<tns:Faktura xmlns:tns="http://crd.gov.pl/wzor/2025/06/25/13775/">
    <tns:Naglowek>
        <tns:KodFormularza kodSystemowy="FA (3)" wersjaSchemy="1-0E">FA</tns:KodFormularza>
        <tns:WariantFormularza>3</tns:WariantFormularza>
        <tns:DataWytworzeniaFa>2025-10-13T12:00:00Z</tns:DataWytworzeniaFa>
        <tns:SystemInfo>TestowySystem</tns:SystemInfo>
    </tns:Naglowek>
    <tns:Podmiot1>
        <tns:PrefiksPodatnika>PL</tns:PrefiksPodatnika>
        <tns:NrEORI>EORI123456</tns:NrEORI>
        <tns:DaneIdentyfikacyjne>
            <tns:NIP>1234567890</tns:NIP>
            <tns:Nazwa>Sprzedawca Sp. z o.o.</tns:Nazwa>
        </tns:DaneIdentyfikacyjne>
        <tns:Adres>
            <tns:KodKraju>PL</tns:KodKraju>
            <tns:AdresL1>ul. Przykładowa 1</tns:AdresL1>
            <tns:AdresL2>lok. 2</tns:AdresL2>
            <tns:GLN>1234567890123</tns:GLN>
        </tns:Adres>
        <tns:AdresKoresp>
            <tns:KodKraju>PL</tns:KodKraju>
            <tns:AdresL1>ul. Korespondencyjna 3</tns:AdresL1>
        </tns:AdresKoresp>
        <tns:DaneKontaktowe>
            <tns:Email>sprzedawca@example.com</tns:Email>
            <tns:Telefon>123456789</tns:Telefon>
        </tns:DaneKontaktowe>
        <tns:StatusInfoPodatnika>1</tns:StatusInfoPodatnika>
    </tns:Podmiot1>
    <tns:Podmiot2>
        <tns:NrEORI>EORI987654</tns:NrEORI>
        <tns:DaneIdentyfikacyjne>
            <tns:NIP>0987654321</tns:NIP>
            <tns:KodUE>DE</tns:KodUE>
            <tns:NrVatUE>DE123456789</tns:NrVatUE>
            <tns:Nazwa>Nabywca S.A.</tns:Nazwa>
        </tns:DaneIdentyfikacyjne>
        <tns:Adres>
            <tns:KodKraju>DE</tns:KodKraju>
            <tns:AdresL1>ul. Niemiecka 5</tns:AdresL1>
        </tns:Adres>
        <tns:AdresKoresp>
            <tns:KodKraju>DE</tns:KodKraju>
            <tns:AdresL1>ul. Korespondencyjna 6</tns:AdresL1>
        </tns:AdresKoresp>
        <tns:DaneKontaktowe>
            <tns:Email>nabywca@example.com</tns:Email>
            <tns:Telefon>987654321</tns:Telefon>
        </tns:DaneKontaktowe>
        <tns:NrKlienta>KL123</tns:NrKlienta>
        <tns:IDNabywcy>IDN987</tns:IDNabywcy>
        <tns:JST>2</tns:JST>
        <tns:GV>2</tns:GV>
    </tns:Podmiot2>
    <tns:Podmiot3>
        <tns:IDNabywcy>IDN333</tns:IDNabywcy>
        <tns:NrEORI>EORI333</tns:NrEORI>
        <tns:DaneIdentyfikacyjne>
            <tns:NIP>3333333333</tns:NIP>
            <tns:IDWew>3333333333-12345</tns:IDWew>
            <tns:KodUE>FR</tns:KodUE>
            <tns:NrVatUE>FR333333333</tns:NrVatUE>
            <tns:Nazwa>Podmiot Trzeci</tns:Nazwa>
        </tns:DaneIdentyfikacyjne>
        <tns:Adres>
            <tns:KodKraju>FR</tns:KodKraju>
            <tns:AdresL1>ul. Francuska 7</tns:AdresL1>
        </tns:Adres>
        <tns:AdresKoresp>
            <tns:KodKraju>FR</tns:KodKraju>
            <tns:AdresL1>ul. Korespondencyjna 8</tns:AdresL1>
        </tns:AdresKoresp>
        <tns:DaneKontaktowe>
            <tns:Email>trzeci@example.com</tns:Email>
            <tns:Telefon>333333333</tns:Telefon>
        </tns:DaneKontaktowe>
        <tns:Rola>1</tns:Rola>
        <tns:Udzial>50.000000</tns:Udzial>
        <tns:NrKlienta>KL333</tns:NrKlienta>
    </tns:Podmiot3>
    <tns:PodmiotUpowazniony>
        <tns:NrEORI>EORIUP123</tns:NrEORI>
        <tns:DaneIdentyfikacyjne>
            <tns:NIP>4444444444</tns:NIP>
            <tns:Nazwa>Upoważniony</tns:Nazwa>
        </tns:DaneIdentyfikacyjne>
        <tns:Adres>
            <tns:KodKraju>PL</tns:KodKraju>
            <tns:AdresL1>ul. Upoważniona 9</tns:AdresL1>
        </tns:Adres>
        <tns:DaneKontaktowe>
            <tns:Email>upowazniony@example.com</tns:Email>
            <tns:Telefon>444444444</tns:Telefon>
        </tns:DaneKontaktowe>
        <tns:Rola>3</tns:Rola>
    </tns:PodmiotUpowazniony>
    <!-- Przykładowe pola P_XXX -->
    <tns:P_22>1</tns:P_22>
    <tns:P_42_5>2</tns:P_42_5>
    <tns:P_22A>2025-10-13</tns:P_22A>
    <tns:P_NrWierszaNST>1</tns:P_NrWierszaNST>
    <tns:P_22BMK>MarkaTestowa</tns:P_22BMK>
    <tns:P_22BMD>ModelTestowy</tns:P_22BMD>
    <tns:P_22BK>KolorTestowy</tns:P_22BK>
    <tns:P_22BNR>ABC123</tns:P_22BNR>
    <tns:P_22BRP>2025</tns:P_22BRP>
    <tns:P_22B>10000</tns:P_22B>
    <tns:P_22B1>VIN123456789</tns:P_22B1>
    <tns:P_22B2>NADWOZIE123</tns:P_22B2>
    <tns:P_22B3>PODWOZIE123</tns:P_22B3>
    <tns:P_22B4>RAMA123</tns:P_22B4>
    <tns:P_22BT>TypTestowy</tns:P_22BT>
    <tns:P_22C>500</tns:P_22C>
    <tns:P_22C1>KADLUB123</tns:P_22C1>
    <tns:P_22D>200</tns:P_22D>
    <tns:P_22D1>FABRYKA123</tns:P_22D1>
    <tns:P_22N>1</tns:P_22N>
</tns:Faktura>
'''

def validate_xml(xml_string, schema_path):
    with open(schema_path, 'rb') as f:
        schema_doc = etree.parse(f)
        schema = etree.XMLSchema(schema_doc)
    xml_doc = etree.fromstring(xml_string.encode('utf-8'))
    try:
        schema.assertValid(xml_doc)
        print("XML jest zgodny ze schematem.")
    except etree.DocumentInvalid as e:
        print("Błąd walidacji:", e)

if __name__ == "__main__":
    validate_xml(EXAMPLE_XML, SCHEMA_PATH)
