#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parser XML faktury KSeF - tylko dla FA(3).

Wyciąga wszystkie możliwe dane zgodnie z schematem XSD FA(3).

Moduł używany przez:
- invoice_xml_to_html.py
- invoice_xml_to_html_jinja.py

Przykład użycia:
    from invoice_xml_parser_FA3 import InvoiceXMLParserFA3
    
    parser = InvoiceXMLParserFA3(xml_content)
    invoice_data = parser.parse()
"""

import sys
from lxml import etree
from decimal import Decimal
from typing import Optional, List, Dict, Any

# Fix encoding dla Windows console
if sys.platform == 'win32':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class InvoiceXMLParserFA3:
    """Parser XML faktury KSeF - tylko FA(3)."""
    
    # Namespace dla FA(3)
    NAMESPACES = {
        'fa': 'http://crd.gov.pl/wzor/2025/06/25/13775/',
        'etd': 'http://crd.gov.pl/xml/schematy/dziedzinowe/mf/2022/01/05/eD/DefinicjeTypy/'
    }
    
    def __init__(self, xml_content: str):
        """
        Inicjalizacja parsera.
        
        Args:
            xml_content: String z XML faktury KSeF FA(3)
        """
        self.xml_content = xml_content
        self.root = None
        self.invoice_data = {}
        
    def parse(self) -> Dict[str, Any]:
        """
        Parsuje XML i zwraca słownik z danymi faktury.
        
        Returns:
            dict: Słownik z danymi faktury
        """
        try:
            self.root = etree.fromstring(self.xml_content.encode('utf-8'))
        except Exception as e:
            print(f"[!] Błąd parsowania XML: {e}", file=sys.stderr)
            raise
        
        #print(f"[+] Parsowanie FA(3)", file=sys.stderr)
        
        self.invoice_data = {
            # Nagłówek
            'naglowek': self._get_header(),
            
            # Podmioty
            'sprzedawca': self._get_seller(),
            'nabywca': self._get_buyer(),
            'podmiot3': self._get_subject3(),
            'podmiot_upowazniony': self._get_authorized_entity(),
            
            # Podstawowe dane faktury
            'numer': self._get_invoice_number(),
            'data_wystawienia': self._get_date_issue(),
            'miejsce_wystawienia': self._get_place_issue(),
            'data_sprzedazy': self._get_date_sale(),
            'okres_sprzedazy': self._get_sale_period(),
            'waluta': self._get_currency(),
            
            # Numery WZ
            'numery_wz': self._get_wz_numbers(),
            
            # Rodzaj faktury
            'rodzaj_faktury': self._get_invoice_type(),
            # Dane korekty (dla faktur korygujących)
            'korekta': self._get_correction_data(),
            
            # Typ cen (netto/brutto) - na podstawie pierwszego wiersza
            'typ_cen': self._get_price_type(),
            
            # Flagi specjalne (FP, TP)
            'flagi_specjalne': self._get_special_flags(),
            
            # Pozycje
            'pozycje': self._get_items(),
            
            # Podsumowanie
            'podsumowanie': self._get_summary(),
            'podsumowanie_szczegolowe': self._get_detailed_summary(),
            
            # Adnotacje
            'adnotacje': self._get_annotations(),
            
            # Dodatkowe opisy
            'dodatkowe_opisy': self._get_additional_descriptions(),
            
            # Faktury zaliczkowe
            'faktury_zaliczkowe': self._get_advance_invoices(),
            
            # Zamówienie (szczegółowe - dla faktur zaliczkowych)
            'zamowienie': self._get_order(),
            
            # Zwrot akcyzy
            'zwrot_akcyzy': self._get_excise_refund(),
            
            # Rozliczenie
            'rozliczenie': self._get_settlement(),
            
            # Płatność
            'platnosc': self._get_payment(),
            
            # Warunki transakcji
            'warunki_transakcji': self._get_transaction_terms(),
            
            # Zaliczki częściowe (ZaliczkaCzesciowa z Fa)
            'zaliczki_czesciowe': self._get_partial_advances(),
            
            # Stopka
            'stopka': self._get_footer(),
            
            # Załączniki
            'zalacznik': self._get_attachment(),
        }
        
        return self.invoice_data

    def _get_correction_data(self) -> Optional[Dict[str, Any]]:
        """
        Pobiera dane korekty z poziomu elementu Fa:
        - PrzyczynaKorekty
        - TypKorekty
        - DaneFaKorygowanej (lista, max 50000)
        """
        fa_xpath = './/*[local-name()="Fa"]'

        przyczyna = self._get_text(f'{fa_xpath}/*[local-name()="PrzyczynaKorekty"]')
        typ_korekty = self._get_text(f'{fa_xpath}/*[local-name()="TypKorekty"]')

        # DaneFaKorygowanej może wystąpić wiele razy
        dane_elements = self._xpath(f'{fa_xpath}/*[local-name()="DaneFaKorygowanej"]')
        dane_fa_korygowanej: List[Dict[str, str]] = []
        for elem in dane_elements:
            dane_fa_korygowanej.append({
                'data_wystawienia': self._get_text('*[local-name()="DataWystFaKorygowanej"]', element=elem),
                'numer': self._get_text('*[local-name()="NrFaKorygowanej"]', element=elem),
                'nr_ksef': self._get_text('*[local-name()="NrKSeF"]', element=elem),
                'nr_ksef_fa_korygowanej': self._get_text('*[local-name()="NrKSeFFaKorygowanej"]', element=elem),
            })

        if not (przyczyna or typ_korekty or dane_fa_korygowanej):
            return None

        return {
            'przyczyna_korekty': przyczyna,
            'typ_korekty': typ_korekty,
            'dane_fa_korygowanej': dane_fa_korygowanej,
        }
    
    def _xpath(self, xpath: str, element=None) -> list:
        """Helper do xpath - używa local-name() dla braku namespace."""
        elem = element if element is not None else self.root
        # Używamy local-name() żeby działało bez namespace
        return elem.xpath(xpath)
    
    def _get_text(self, xpath: str, default: str = '', element=None) -> str:
        """Pobiera tekst z xpath."""
        result = self._xpath(xpath, element)
        return result[0].text if result and result[0].text else default
    
    def _get_attr(self, xpath: str, attr: str, default: str = '', element=None) -> str:
        """Pobiera atrybut z xpath."""
        result = self._xpath(xpath, element)
        return result[0].get(attr, default) if result else default
    
    # ========================================================================
    # NAGŁÓWEK
    # ========================================================================
    
    def _get_header(self) -> Dict[str, Any]:
        """Pobiera dane z nagłówka."""
        return {
            'kod_formularza': self._get_text('.//*[local-name()="Naglowek"]/*[local-name()="KodFormularza"]'),
            'kod_systemowy': self._get_attr('.//*[local-name()="Naglowek"]/*[local-name()="KodFormularza"]', 'kodSystemowy'),
            'wersja_schemy': self._get_attr('.//*[local-name()="Naglowek"]/*[local-name()="KodFormularza"]', 'wersjaSchemy'),
            'wariant_formularza': self._get_text('.//*[local-name()="Naglowek"]/*[local-name()="WariantFormularza"]'),
            'data_wytworzenia': self._get_text('.//*[local-name()="Naglowek"]/*[local-name()="DataWytworzeniaFa"]'),
            'system_info': self._get_text('.//*[local-name()="Naglowek"]/*[local-name()="SystemInfo"]'),
        }
    
    # ========================================================================
    # PODMIOT 1 - SPRZEDAWCA
    # ========================================================================
    
    def _get_seller(self) -> Dict[str, Any]:
        """Pobiera dane sprzedawcy (Podmiot1)."""
        podmiot1_xpath = './/*[local-name()="Podmiot1"]'
        
        return {
            'prefiks_podatnika': self._get_text(f'{podmiot1_xpath}/*[local-name()="PrefiksPodatnika"]'),
            'nr_eori': self._get_text(f'{podmiot1_xpath}/*[local-name()="NrEORI"]'),
            
            # DaneIdentyfikacyjne
            'dane_identyfikacyjne': {
                'nip': self._get_text(f'{podmiot1_xpath}/*[local-name()="DaneIdentyfikacyjne"]/*[local-name()="NIP"]'),
                'nazwa': self._get_text(f'{podmiot1_xpath}/*[local-name()="DaneIdentyfikacyjne"]/*[local-name()="Nazwa"]'),
                'pelna_nazwa': self._get_text(f'{podmiot1_xpath}/*[local-name()="DaneIdentyfikacyjne"]/*[local-name()="PelnaNazwa"]'),
            },
            
            # Adres
            'adres': self._get_address(f'{podmiot1_xpath}/*[local-name()="Adres"]'),
            
            # Adres korespondencyjny
            'adres_koresp': self._get_address(f'{podmiot1_xpath}/*[local-name()="AdresKoresp"]'),
            
            # Dane kontaktowe
            'dane_kontaktowe': self._get_contact_data(podmiot1_xpath),
            
            # Status info podatnika
            'status_info_podatnika': self._get_text(f'{podmiot1_xpath}/*[local-name()="StatusInfoPodatnika"]'),
        }
    
    # ========================================================================
    # PODMIOT 2 - NABYWCA
    # ========================================================================
    
    def _get_buyer(self) -> Dict[str, Any]:
        """Pobiera dane nabywcy (Podmiot2)."""
        podmiot2_xpath = './/*[local-name()="Podmiot2"]'
        
        return {
            'nr_eori': self._get_text(f'{podmiot2_xpath}/*[local-name()="NrEORI"]'),
            
            # DaneIdentyfikacyjne
            'dane_identyfikacyjne': self._get_buyer_identification(podmiot2_xpath),
            
            # Adres
            'adres': self._get_address(f'{podmiot2_xpath}/*[local-name()="Adres"]'),
            
            # Adres korespondencyjny
            'adres_koresp': self._get_address(f'{podmiot2_xpath}/*[local-name()="AdresKoresp"]'),
            
            # Dane kontaktowe
            'dane_kontaktowe': self._get_contact_data(podmiot2_xpath),
            
            # Numer klienta
            'nr_klienta': self._get_text(f'{podmiot2_xpath}/*[local-name()="NrKlienta"]'),
            
            # ID nabywcy
            'id_nabywcy': self._get_text(f'{podmiot2_xpath}/*[local-name()="IDNabywcy"]'),
            
            # Znaczniki: faktura dotyczy jednostki podrzędnej JST lub członka grupy VAT
            'dotyczy_jst': self._get_text(f'{podmiot2_xpath}/*[local-name()="JST"]'),  # 1 = Tak, 2 = Nie
            'dotyczy_grupa_vat': self._get_text(f'{podmiot2_xpath}/*[local-name()="GV"]'),  # 1 = Tak, 2 = Nie
        }
    
    def _get_buyer_identification(self, podmiot2_xpath: str) -> Dict[str, Any]:
        """Pobiera dane identyfikacyjne nabywcy."""
        dane_id_xpath = f'{podmiot2_xpath}/*[local-name()="DaneIdentyfikacyjne"]'
        
        return {
            'nip': self._get_text(f'{dane_id_xpath}/*[local-name()="NIP"]'),
            'nip_ue': self._get_text(f'{dane_id_xpath}/*[local-name()="NIP_UE"]'),
            'nr_id': self._get_text(f'{dane_id_xpath}/*[local-name()="NrID"]'),
            'kod_kraju': self._get_text(f'{dane_id_xpath}/*[local-name()="KodKraju"]'),
            'nazwa': self._get_text(f'{dane_id_xpath}/*[local-name()="Nazwa"]'),
            'pelna_nazwa': self._get_text(f'{dane_id_xpath}/*[local-name()="PelnaNazwa"]'),
            'imie': self._get_text(f'{dane_id_xpath}/*[local-name()="Imie"]'),
            'nazwisko': self._get_text(f'{dane_id_xpath}/*[local-name()="Nazwisko"]'),
            'data_urodzenia': self._get_text(f'{dane_id_xpath}/*[local-name()="DataUrodzenia"]'),
        }
    
    # ========================================================================
    # PODMIOT 3 - PODMIOTY TRZECIE
    # ========================================================================
    
    def _get_role_description(self, rola_value: Optional[str]) -> Optional[str]:
        """Zwraca opis roli podmiotu trzeciego na podstawie wartości numerycznej z XSD."""
        if not rola_value:
            return None
        
        role_descriptions = {
            '1': 'Faktor',
            '2': 'Odbiorca',
            '3': 'Podmiot pierwotny',
            '4': 'Dodatkowy nabywca',
            '5': 'Wystawca faktury',
            '6': 'Dokonujący płatności',
            '7': 'Jednostka samorządu terytorialnego - wystawca',
            '8': 'Jednostka samorządu terytorialnego - odbiorca',
            '9': 'Członek grupy VAT - wystawca',
            '10': 'Członek grupy VAT - odbiorca',
            '11': 'Pracownik',
        }
        
        return role_descriptions.get(rola_value)
    
    def _get_subject3(self) -> List[Dict[str, Any]]:
        """Pobiera dane podmiotów trzecich (Podmiot3)."""
        subjects = []
        podmiot3_elements = self._xpath('.//*[local-name()="Podmiot3"]')
        
        for podmiot3 in podmiot3_elements:
            dane_id_xpath = '*[local-name()="DaneIdentyfikacyjne"]'
            
            rola_value = self._get_text('*[local-name()="Rola"]', element=podmiot3)
            rola_inna = self._get_text('*[local-name()="RolaInna"]', element=podmiot3)
            opis_roli = self._get_text('*[local-name()="OpisRoli"]', element=podmiot3)
            
            # Jeśli jest rola numeryczna, pobierz opis z XSD
            # Jeśli jest rola_inna, użyj OpisRoli z XML
            rola_opis = None
            if rola_value:
                rola_opis = self._get_role_description(rola_value)
            elif rola_inna == '1' and opis_roli:
                rola_opis = opis_roli
            
            subject_data = {
                # Elementy główne
                'id_nabywcy': self._get_text('*[local-name()="IDNabywcy"]', element=podmiot3),
                'nr_eori': self._get_text('*[local-name()="NrEORI"]', element=podmiot3),
                
                # DaneIdentyfikacyjne - wszystkie warianty identyfikacji
                'dane_identyfikacyjne': {
                    'nip': self._get_text(f'{dane_id_xpath}/*[local-name()="NIP"]', element=podmiot3),
                    'id_wew': self._get_text(f'{dane_id_xpath}/*[local-name()="IDWew"]', element=podmiot3),
                    'kod_ue': self._get_text(f'{dane_id_xpath}/*[local-name()="KodUE"]', element=podmiot3),
                    'nr_vat_ue': self._get_text(f'{dane_id_xpath}/*[local-name()="NrVatUE"]', element=podmiot3),
                    'kod_kraju': self._get_text(f'{dane_id_xpath}/*[local-name()="KodKraju"]', element=podmiot3),
                    'nr_id': self._get_text(f'{dane_id_xpath}/*[local-name()="NrID"]', element=podmiot3),
                    'brak_id': self._get_text(f'{dane_id_xpath}/*[local-name()="BrakID"]', element=podmiot3),
                    'nazwa': self._get_text(f'{dane_id_xpath}/*[local-name()="Nazwa"]', element=podmiot3),
                },
                
                # Adresy
                'adres': self._get_address_from_element('*[local-name()="Adres"]', podmiot3),
                'adres_koresp': self._get_address_from_element('*[local-name()="AdresKoresp"]', podmiot3),
                
                # Dane kontaktowe (może być do 3)
                'dane_kontaktowe': self._get_contact_data_from_element(podmiot3),
                
                # Rola
                'rola': rola_value,
                'rola_inna': rola_inna,
                'opis_roli': opis_roli,
                'rola_opis': rola_opis,  # Opis roli (z XSD lub z XML)
                
                # Pozostałe
                'udzial': self._get_text('*[local-name()="Udzial"]', element=podmiot3),
                'nr_klienta': self._get_text('*[local-name()="NrKlienta"]', element=podmiot3),
            }
            subjects.append(subject_data)
        
        return subjects
    
    def _get_address_from_element(self, xpath: str, element) -> Optional[Dict[str, str]]:
        """Pobiera adres z elementu jako kontekstu."""
        addr_elements = self._xpath(xpath, element)
        if not addr_elements:
            return None
        
        addr_elem = addr_elements[0]
        return {
            'kod_kraju': self._get_text('*[local-name()="KodKraju"]', element=addr_elem),
            'adres_l1': self._get_text('*[local-name()="AdresL1"]', element=addr_elem),
            'adres_l2': self._get_text('*[local-name()="AdresL2"]', element=addr_elem),
            'gln': self._get_text('*[local-name()="GLN"]', element=addr_elem),
        }
    
    def _get_contact_data_from_element(self, element) -> List[Dict[str, str]]:
        """Pobiera dane kontaktowe z elementu jako kontekstu."""
        contacts = []
        contact_elements = self._xpath('*[local-name()="DaneKontaktowe"]', element)
        
        for contact in contact_elements:
            contact_data = {
                'email': self._get_text('*[local-name()="Email"]', element=contact),
                'telefon': self._get_text('*[local-name()="Telefon"]', element=contact),
            }
            contacts.append(contact_data)
        
        return contacts
    
    # ========================================================================
    # PODMIOT UPOWAŻNIONY
    # ========================================================================
    
    def _get_authorized_entity(self) -> Optional[Dict[str, Any]]:
        """Pobiera dane podmiotu upoważnionego (PodmiotUpowazniony)."""
        podmiot_xpath = './/*[local-name()="PodmiotUpowazniony"]'
        
        if not self._xpath(podmiot_xpath):
            return None
        
        entity_data = {
            'nr_eori': self._get_text(f'{podmiot_xpath}/*[local-name()="NrEORI"]'),
            'dane_identyfikacyjne': {
                'nip': self._get_text(f'{podmiot_xpath}/*[local-name()="DaneIdentyfikacyjne"]/*[local-name()="NIP"]'),
                'nazwa': self._get_text(f'{podmiot_xpath}/*[local-name()="DaneIdentyfikacyjne"]/*[local-name()="Nazwa"]'),
            },
            'adres': self._get_address(f'{podmiot_xpath}/*[local-name()="Adres"]'),
            'adres_koresp': self._get_address(f'{podmiot_xpath}/*[local-name()="AdresKoresp"]'),
            'dane_kontaktowe': self._get_contact_data(podmiot_xpath),
        }
        
        return entity_data
    
    # ========================================================================
    # ADRES I DANE KONTAKTOWE - HELPERY
    # ========================================================================
    
    def _get_address(self, xpath_prefix: str) -> Optional[Dict[str, str]]:
        """Pobiera adres."""
        if not self._xpath(xpath_prefix):
            return None
        
        return {
            'kod_kraju': self._get_text(f'{xpath_prefix}/*[local-name()="KodKraju"]'),
            'adres_l1': self._get_text(f'{xpath_prefix}/*[local-name()="AdresL1"]'),
            'adres_l2': self._get_text(f'{xpath_prefix}/*[local-name()="AdresL2"]'),
            'gmina': self._get_text(f'{xpath_prefix}/*[local-name()="GLN"]'),
        }
    
    def _get_contact_data(self, podmiot_xpath: str) -> List[Dict[str, str]]:
        """Pobiera dane kontaktowe."""
        contacts = []
        contact_elements = self._xpath(f'{podmiot_xpath}/*[local-name()="DaneKontaktowe"]')
        
        for contact in contact_elements:
            contact_data = {
                'email': self._get_text('*[local-name()="Email"]', element=contact),
                'telefon': self._get_text('*[local-name()="Telefon"]', element=contact),
            }
            contacts.append(contact_data)
        
        return contacts
    
    # ========================================================================
    # PODSTAWOWE DANE FAKTURY
    # ========================================================================
    
    def _get_invoice_number(self) -> str:
        """Pobiera numer faktury (P_2)."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="P_2"]', 'BRAK')
    
    def _get_date_issue(self) -> str:
        """Pobiera datę wystawienia (P_1)."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="P_1"]', 'BRAK')
    
    def _get_place_issue(self) -> str:
        """Pobiera miejsce wystawienia (P_1M)."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="P_1M"]')
    
    def _get_date_sale(self) -> str:
        """Pobiera datę sprzedaży (P_6)."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="P_6"]')
    
    def _get_sale_period(self) -> Optional[Dict[str, str]]:
        """Pobiera okres sprzedaży (OkresFa)."""
        okres_xpath = './/*[local-name()="Fa"]/*[local-name()="OkresFa"]'
        if not self._xpath(okres_xpath):
            return None
        
        return {
            'od': self._get_text(f'{okres_xpath}/*[local-name()="P_6_Od"]'),
            'do': self._get_text(f'{okres_xpath}/*[local-name()="P_6_Do"]'),
        }
    
    def _get_currency(self) -> str:
        """Pobiera kod waluty."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="KodWaluty"]', 'PLN')
    
    def _get_wz_numbers(self) -> List[str]:
        """Pobiera numery WZ."""
        wz_elements = self._xpath('.//*[local-name()="Fa"]/*[local-name()="WZ"]')
        return [wz.text for wz in wz_elements if wz.text]
    
    def _get_invoice_type(self) -> str:
        """Pobiera rodzaj faktury."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="RodzajFaktury"]')
    
    def _get_price_type(self) -> str:
        """
        Określa typ cen na fakturze na podstawie pierwszego wiersza.
        
        Returns:
            str: 'netto' jeśli w pierwszym wierszu jest P_11 (wartość netto),
                 'brutto' w przeciwnym przypadku
        """
        # Sprawdź pierwszy wiersz faktury
        first_item = self._xpath('.//*[local-name()="Fa"]/*[local-name()="FaWiersz"][1]')
        if not first_item:
            return 'netto'  # Domyślnie netto jeśli brak wierszy
        
        # Sprawdź czy jest P_11 (wartość netto)
        p11 = self._get_text('*[local-name()="P_11"]', '', first_item[0])
        
        return 'netto' if p11 else 'brutto'
    
    def _get_special_flags(self) -> Dict[str, str]:
        """Pobiera specjalne flagi faktury (FP, TP)."""
        fa_xpath = './/*[local-name()="Fa"]'
        return {
            'fp': self._get_text(f'{fa_xpath}/*[local-name()="FP"]'),  # Faktura art. 109 ust. 3d
            'tp': self._get_text(f'{fa_xpath}/*[local-name()="TP"]'),  # Transakcja trójstronna
        }
    
    # ========================================================================
    # POZYCJE FAKTURY
    # ========================================================================
    
    def _get_items(self) -> List[Dict[str, Any]]:
        """Pobiera pozycje faktury (FaWiersz)."""
        items = []
        item_elements = self._xpath('.//*[local-name()="Fa"]/*[local-name()="FaWiersz"]')
        
        for item in item_elements:
            # Pobierz surowe wartości z XML
            netto_xml = self._get_text('*[local-name()="P_11"]', '', item)      # Wartość netto (opcjonalne)
            brutto_xml = self._get_text('*[local-name()="P_11A"]', '', item)    # Wartość brutto (opcjonalne)
            vat_kwota_xml = self._get_text('*[local-name()="P_11Vat"]', '', item)  # Kwota VAT (opcjonalne)
            # Stawka VAT (P_12) bywa całkowicie pominięta w XML — nie zamieniaj braku na "0"
            vat_percent = self._get_text('*[local-name()="P_12"]', '', item)
            vat_rate_missing = (not str(vat_percent).strip())
            
            # Ceny jednostkowe z XML
            cena_netto_xml = self._get_text('*[local-name()="P_9A"]', '', item)   # Cena netto (opcjonalne)
            cena_brutto_xml = self._get_text('*[local-name()="P_9B"]', '', item)  # Cena brutto (opcjonalne)
            
            # Oblicz brakujące wartości (wartości pozycji)
            netto_val, brutto_val, vat_val = self._calculate_item_values(
                netto_xml, brutto_xml, vat_kwota_xml, vat_percent
            )
            
            # Oblicz brakujące ceny jednostkowe
            cena_netto, cena_brutto = self._calculate_unit_prices(
                cena_netto_xml, cena_brutto_xml, vat_percent
            )
            
            # Fallback: gdy w XML brak P_11/P_11A/P_11Vat, wylicz wartości z cena × ilość
            if netto_val is None or brutto_val is None:
                try:
                    vat_pct = Decimal(str(vat_percent).replace(',', '.')) if (vat_percent and not vat_rate_missing) else Decimal('0')
                except Exception:
                    vat_pct = Decimal('0')
                ilosc_raw = self._get_text('*[local-name()="P_8B"]', '0', item)
                ilosc_dec = self._parse_decimal(ilosc_raw)
                if ilosc_dec is not None and ilosc_dec > 0:
                    # Z ceny brutto (P_9B lub wyliczonej): wartosc_brutto = cena_brutto × ilość
                    if brutto_val is None:
                        cena_b = self._parse_decimal(cena_brutto_xml)
                        if cena_b is None:
                            cena_b = self._parse_decimal(cena_brutto)
                        if cena_b is not None:
                            brutto_val = cena_b * ilosc_dec
                            # Nie przeliczaj brutto→netto jeśli stawka VAT nie jest znana
                            if vat_pct > 0 and not vat_rate_missing:
                                netto_val = brutto_val / (1 + vat_pct / 100)
                                vat_val = brutto_val - netto_val
                            elif not vat_rate_missing:
                                # Dla jawnego 0% VAT: netto = brutto, VAT = 0
                                netto_val = brutto_val
                                vat_val = Decimal('0')
                    # Z ceny netto (P_9A lub wyliczonej): wartosc_netto = cena_netto × ilość
                    if netto_val is None:
                        cena_n = self._parse_decimal(cena_netto_xml)
                        if cena_n is None:
                            cena_n = self._parse_decimal(cena_netto)
                        if cena_n is not None:
                            netto_val = cena_n * ilosc_dec
                            # Nie wyliczaj VAT/brutto jeśli stawka VAT nie jest znana
                            if not vat_rate_missing:
                                vat_val = netto_val * vat_pct / 100
                                brutto_val = netto_val + vat_val

            # Formatuj wartości do wyświetlenia (Decimal(0) jest w Pythonie "falsy" — używaj is not None)
            wartosc_netto = self._format_decimal(netto_val) if netto_val is not None else ''
            wartosc_brutto = self._format_decimal(brutto_val) if brutto_val is not None else ''
            kwota_vat = self._format_decimal(vat_val) if vat_val is not None else ''
            
            item_data = {
                'nr_wiersza': self._get_text('*[local-name()="NrWierszaFa"]', '', item),
                'uu_id': self._get_text('*[local-name()="UU_ID"]', '', item),
                'data_sprzedazy': self._get_text('*[local-name()="P_6A"]', '', item),
                'nazwa': self._get_text('*[local-name()="P_7"]', '', item),
                'indeks': self._get_text('*[local-name()="Indeks"]', '', item),
                'gtin': self._get_text('*[local-name()="GTIN"]', '', item),
                'pkwiu': self._get_text('*[local-name()="PKWiU"]', '', item),
                'cn': self._get_text('*[local-name()="CN"]', '', item),
                'pkob': self._get_text('*[local-name()="PKOB"]', '', item),
                'jednostka': self._get_text('*[local-name()="P_8A"]', 'szt', item),
                'ilosc': self._format_quantity(self._get_text('*[local-name()="P_8B"]', '0', item)),
                
                # Ceny jednostkowe - oryginalne z XML
                'cena_netto_xml': self._format_amount(cena_netto_xml),
                'cena_brutto_xml': self._format_amount(cena_brutto_xml),
                # Ceny jednostkowe - z XML lub obliczone
                'cena_netto': cena_netto,
                'cena_brutto': cena_brutto,
                
                'rabat': self._format_amount(self._get_text('*[local-name()="P_10"]', '', item)),
                
                # Wartości pozycji - oryginalne z XML
                'wartosc_netto_xml': self._format_amount(netto_xml),
                'wartosc_brutto_xml': self._format_amount(brutto_xml),
                'kwota_vat_xml': self._format_amount(vat_kwota_xml),
                # Wartości pozycji - z XML lub obliczone
                'wartosc_netto': wartosc_netto,
                'wartosc_brutto': wartosc_brutto,
                'kwota_vat': kwota_vat,
                
                'stawka_vat': '' if vat_rate_missing else vat_percent,
                'stawka_vat_xii': self._get_text('*[local-name()="P_12_XII"]', '', item),
                'zal_15': self._get_text('*[local-name()="P_12_Zal_15"]', '', item),
                'kwota_akcyzy': self._format_amount(self._get_text('*[local-name()="KwotaAkcyzy"]', '', item)),
                'gtu': self._get_gtu(item),
                'procedura': self._get_procedure(item),
                'kurs_waluty': self._get_text('*[local-name()="KursWaluty"]', '', item),
                'stan_przed': self._get_text('*[local-name()="StanPrzed"]', '', item),
            }
            items.append(item_data)
        
        return items
    
    def _calculate_item_values(self, netto_xml: str, brutto_xml: str, 
                                vat_kwota_xml: str, vat_percent: str) -> tuple:
        """
        Oblicza wartości netto, brutto i VAT dla pozycji faktury.
        
        Obsługuje różne przypadki:
        1. Faktura z cenami netto: P_11 + P_12 → oblicz brutto
        2. Faktura z cenami brutto: P_11A + P_11Vat → oblicz netto
        3. Pełne dane: P_11 + P_11A + P_11Vat → użyj bezpośrednio
        
        Returns:
            tuple: (netto_val, brutto_val, vat_val) jako Decimal lub None
        """
        netto_val = None
        brutto_val = None
        vat_val = None
        
        vat_rate_missing = (not str(vat_percent).strip())
        try:
            vat_pct = Decimal(vat_percent) if (vat_percent and not vat_rate_missing) else Decimal('0')
        except:
            vat_pct = Decimal('0')
        
        # Parsuj wartości z XML
        try:
            if netto_xml:
                netto_val = Decimal(netto_xml)
        except:
            pass
        
        try:
            if brutto_xml:
                brutto_val = Decimal(brutto_xml)
        except:
            pass
        
        try:
            if vat_kwota_xml:
                vat_val = Decimal(vat_kwota_xml)
        except:
            pass
        
        # PRZYPADEK 1: Mamy brutto (P_11A) - faktura z cenami brutto
        if brutto_val is not None:
            # Jeśli mamy VAT, oblicz netto
            if vat_val is not None and netto_val is None:
                netto_val = brutto_val - vat_val
            # Jeśli nie mamy VAT ale mamy netto, oblicz VAT
            elif netto_val is not None and vat_val is None:
                vat_val = brutto_val - netto_val
            # Jeśli nie mamy ani VAT ani netto, oblicz z % VAT (tylko gdy stawka VAT jest znana)
            elif vat_val is None and netto_val is None and vat_pct > 0 and not vat_rate_missing:
                netto_val = brutto_val / (1 + vat_pct / 100)
                vat_val = brutto_val - netto_val
        
        # PRZYPADEK 2: Mamy netto (P_11) ale nie mamy brutto - faktura z cenami netto
        elif netto_val is not None:
            # Jeśli mamy kwotę VAT, oblicz brutto
            if vat_val is not None:
                brutto_val = netto_val + vat_val
            # Jeśli nie mamy kwoty VAT, oblicz z % VAT (tylko gdy stawka VAT jest znana)
            elif not vat_rate_missing:
                vat_val = netto_val * vat_pct / 100
                brutto_val = netto_val + vat_val
        
        # PRZYPADEK 3: Mamy tylko VAT - spróbuj obliczyć netto i brutto
        elif vat_val is not None and vat_pct > 0 and not vat_rate_missing:
            netto_val = vat_val * 100 / vat_pct
            brutto_val = netto_val + vat_val
        
        return (netto_val, brutto_val, vat_val)
    
    def _calculate_unit_prices(self, cena_netto_xml: str, cena_brutto_xml: str, 
                                vat_percent: str) -> tuple:
        """
        Oblicza ceny jednostkowe netto i brutto.
        
        Jeśli brakuje jednej z cen, oblicza ją na podstawie drugiej i stawki VAT.
        
        Args:
            cena_netto_xml: Cena jednostkowa netto z XML (P_9A)
            cena_brutto_xml: Cena jednostkowa brutto z XML (P_9B)
            vat_percent: Stawka VAT w procentach (P_12)
        
        Returns:
            tuple: (cena_netto, cena_brutto) jako sformatowane stringi
        """
        cena_netto = ''
        cena_brutto = ''
        
        vat_rate_missing = (not str(vat_percent).strip())
        try:
            vat_pct = Decimal(vat_percent) if (vat_percent and not vat_rate_missing) else Decimal('0')
        except:
            vat_pct = Decimal('0')
        
        # Parsuj wartości z XML
        cena_netto_val = None
        cena_brutto_val = None
        
        try:
            if cena_netto_xml:
                cena_netto_val = Decimal(cena_netto_xml)
        except:
            pass
        
        try:
            if cena_brutto_xml:
                cena_brutto_val = Decimal(cena_brutto_xml)
        except:
            pass
        
        # PRZYPADEK 1: Mamy obie ceny - użyj bezpośrednio
        if cena_netto_val is not None and cena_brutto_val is not None:
            cena_netto = self._format_amount(cena_netto_xml)
            cena_brutto = self._format_amount(cena_brutto_xml)
        
        # PRZYPADEK 2: Mamy tylko brutto - oblicz netto
        elif cena_brutto_val is not None:
            cena_brutto = self._format_amount(cena_brutto_xml)
            if vat_pct > 0 and not vat_rate_missing:
                cena_netto_val = cena_brutto_val / (1 + vat_pct / 100)
                cena_netto = self._format_decimal(cena_netto_val)
            elif not vat_rate_missing:
                cena_netto = cena_brutto  # Dla 0% VAT: netto = brutto
        
        # PRZYPADEK 3: Mamy tylko netto - oblicz brutto
        elif cena_netto_val is not None:
            cena_netto = self._format_amount(cena_netto_xml)
            if not vat_rate_missing:
                cena_brutto_val = cena_netto_val * (1 + vat_pct / 100)
                cena_brutto = self._format_decimal(cena_brutto_val)
        
        return (cena_netto, cena_brutto)
    
    def _get_gtu(self, item) -> List[str]:
        """Pobiera oznaczenia GTU dla pozycji."""
        gtu_elements = self._xpath('*[local-name()="GTU"]', item)
        if not gtu_elements:
            return []
        
        gtu_values = []
        for gtu in gtu_elements:
            for i in range(1, 14):
                gtu_field = self._get_text(f'*[local-name()="GTU_{i:02d}"]', '', gtu)
                if gtu_field == '1':
                    gtu_values.append(f"GTU_{i:02d}")
        
        return gtu_values
    
    def _get_procedure(self, item) -> List[str]:
        """Pobiera oznaczenia procedur dla pozycji."""
        proc_elements = self._xpath('*[local-name()="Procedura"]', item)
        if not proc_elements:
            return []
        
        procedures = []
        for proc in proc_elements:
            for proc_name in ['TP', 'TT_WNT', 'TT_D', 'MR_T', 'MR_UZ', 'I_42', 'I_63', 'B_SPV', 'B_SPV_DOSTAWA', 'B_MPV_PROWIZJA', 'MPP']:
                proc_field = self._get_text(f'*[local-name()="{proc_name}"]', '', proc)
                if proc_field == '1':
                    procedures.append(proc_name)
        
        return procedures
    
    # ========================================================================
    # PODSUMOWANIE
    # ========================================================================
    
    def _get_summary(self) -> Dict[str, str]:
        """
        Pobiera podstawowe podsumowanie faktury.
        
        Netto: suma pól P_13_1–P_13_5, P_13_6_1–P_13_6_3, P_13_7–P_13_11 (wg XSD FA(3), brak P_13_6).
        VAT: suma P_14_1–P_14_5 (kwoty w PLN; bez pól P_14_*W).
        Brutto: P_15.
        """
        fa_xpath = './/*[local-name()="Fa"]'
        
        def safe_decimal(value_str: str) -> Decimal:
            """Konwertuje string na Decimal, zwraca 0 jeśli pusty lub nieprawidłowy."""
            if not value_str or value_str.strip() == '':
                return Decimal('0')
            try:
                return Decimal(value_str.replace(',', '.'))
            except (ValueError, TypeError):
                return Decimal('0')
        
        # Suma wartości netto — wszystkie P_13_* występujące w schemacie (bez P_13_6)
        netto_total = Decimal('0')
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_1"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_2"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_3"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_4"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_5"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_1"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_2"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_3"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_7"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_8"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_9"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_10"]'))
        netto_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_13_11"]'))
        
        # Suma kwot VAT — tylko P_14_1 … P_14_5 (w schemacie brak P_14_6_*)
        vat_total = Decimal('0')
        vat_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_14_1"]'))
        vat_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_14_2"]'))
        vat_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_14_3"]'))
        vat_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_14_4"]'))
        vat_total += safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_14_5"]'))
        
        # P_15 — należność ogółem (brutto)
        brutto_total = safe_decimal(self._get_text(f'{fa_xpath}/*[local-name()="P_15"]'))
        
        return {
            'netto': self._format_amount(str(netto_total)),
            'vat': self._format_amount(str(vat_total)),
            'brutto': self._format_amount(str(brutto_total)),
        }
    
    def _get_detailed_summary(self) -> Dict[str, Any]:
        """Szczegółowe podsumowanie wg pól P_13 / P_14 w XSD FA(3)."""
        fa_xpath = './/*[local-name()="Fa"]'
        
        def calculate_brutto(netto_str: str, vat_str: str) -> str:
            """Oblicza brutto (netto + vat); wejście może być już z _format_amount (ze spacjami)."""
            try:
                if not netto_str and not vat_str:
                    return ''
                netto = self._parse_decimal(netto_str) if netto_str else None
                vat = self._parse_decimal(vat_str) if vat_str else None
                netto = netto if netto is not None else Decimal('0')
                vat = vat if vat is not None else Decimal('0')
                return self._format_decimal(netto + vat)
            except (ValueError, TypeError, Exception):
                return ''
        
        def zero_rate_row(netto_fmt: str) -> Dict[str, str]:
            """Wiersz dla stawki 0% (brak VAT w PLN w sekcji Fa)."""
            return {
                'netto': netto_fmt,
                'vat': '0,00',
                'brutto': netto_fmt,
            }
        
        # Stawka podstawowa 22/23% — P_13_1, P_14_1, P_14_1W
        netto_23 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_1"]'))
        vat_23 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_1"]'))
        vat_23_w = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_1W"]'))
        
        # Stawka obniżona pierwsza 7/8% — P_13_2, P_14_2, P_14_2W
        netto_8 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_2"]'))
        vat_8 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_2"]'))
        vat_8_w = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_2W"]'))
        
        # Stawka obniżona druga 5% — P_13_3, P_14_3, P_14_3W
        netto_5 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_3"]'))
        vat_5 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_3"]'))
        vat_5_w = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_3W"]'))
        
        # Stawka obniżona trzecia (ryczałt m.in. taksówki) — P_13_4, P_14_4, P_14_4W
        netto_taxi = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_4"]'))
        vat_taxi = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_4"]'))
        vat_taxi_w = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_4W"]'))
        
        # Procedura szczególna (UE) — P_13_5, P_14_5 (brak P_14_5W)
        netto_proc_szczeg_ue = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_5"]'))
        vat_proc_szczeg_ue = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_14_5"]'))
        
        # 0% — P_13_6_1 krajowa, P_13_6_2 WDT, P_13_6_3 eksport (brak P_14_6_* w XSD)
        netto_6_1 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_1"]'))
        netto_6_2 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_2"]'))
        netto_6_3 = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_6_3"]'))
        
        netto_zw = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_7"]'))
        netto_np_I = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_8"]'))
        netto_np_II = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_9"]'))
        netto_oo = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_10"]'))
        netto_marza = self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_13_11"]'))
        
        summary = {
            'stawka_podstawowa': {
                'netto': netto_23,
                'vat': vat_23,
                'brutto': calculate_brutto(netto_23, vat_23),
                'vat_walucie': vat_23_w,
            },
            'stawka_8_proc': {
                'netto': netto_8,
                'vat': vat_8,
                'brutto': calculate_brutto(netto_8, vat_8),
                'vat_walucie': vat_8_w,
            },
            'stawka_5_proc': {
                'netto': netto_5,
                'vat': vat_5,
                'brutto': calculate_brutto(netto_5, vat_5),
                'vat_walucie': vat_5_w,
            },
            'stawka_obnizona_trzecia': {
                'netto': netto_taxi,
                'vat': vat_taxi,
                'brutto': calculate_brutto(netto_taxi, vat_taxi),
                'vat_walucie': vat_taxi_w,
            },
            'stawka_proc_szczeg_ue': {
                'netto': netto_proc_szczeg_ue,
                'vat': vat_proc_szczeg_ue,
                'brutto': calculate_brutto(netto_proc_szczeg_ue, vat_proc_szczeg_ue),
            },
            'stawka_0_proc_krajowa': zero_rate_row(netto_6_1),
            'stawka_0_proc_wdt': zero_rate_row(netto_6_2),
            'stawka_0_proc_exp': zero_rate_row(netto_6_3),
            'zwolnione': {
                'netto': netto_zw,
            },
            'nie_podlega_I': {
                'netto': netto_np_I,
            },
            'nie_podlega_II': {
                'netto': netto_np_II,
            },
            'odwrotne_obciazenie': {
                'netto': netto_oo,
            },
            'marza': {
                'netto': netto_marza,
            },
            'brutto': self._format_amount(self._get_text(f'{fa_xpath}/*[local-name()="P_15"]')),
        }
        
        return summary
    
    # ========================================================================
    # ADNOTACJE
    # ========================================================================
    
    def _get_annotations(self) -> Dict[str, Any]:
        """Pobiera adnotacje."""
        adnotacje_xpath = './/*[local-name()="Fa"]/*[local-name()="Adnotacje"]'
        
        if not self._xpath(adnotacje_xpath):
            return {}
        
        return {
            'metoda_kasowa': self._get_text(f'{adnotacje_xpath}/*[local-name()="P_16"]'),
            'samofakturowanie': self._get_text(f'{adnotacje_xpath}/*[local-name()="P_17"]'),
            'odwrotne_obciazenie': self._get_text(f'{adnotacje_xpath}/*[local-name()="P_18"]'),
            'mechanizm_podzielonej_platnosci': self._get_text(f'{adnotacje_xpath}/*[local-name()="P_18A"]'),
            
            # Zwolnienie
            'zwolnienie': self._get_exemption(adnotacje_xpath),
            
            # Nowe środki transportu (kompletne)
            'nowe_srodki_transportu': self._get_new_vehicles(adnotacje_xpath),
            
            # Inne
            'p_23': self._get_text(f'{adnotacje_xpath}/*[local-name()="P_23"]'),
            
            # Procedura marży (kompletne)
            'procedura_marzy': self._get_margin_procedure(adnotacje_xpath),
        }
    
    def _get_exemption(self, adnotacje_xpath: str) -> Dict[str, str]:
        """Pobiera dane o zwolnieniu."""
        zwolnienie_xpath = f'{adnotacje_xpath}/*[local-name()="Zwolnienie"]'
        
        return {
            'p_19': self._get_text(f'{zwolnienie_xpath}/*[local-name()="P_19"]'),
            'p_19a': self._get_text(f'{zwolnienie_xpath}/*[local-name()="P_19A"]'),
            'p_19b': self._get_text(f'{zwolnienie_xpath}/*[local-name()="P_19B"]'),
            'p_19c': self._get_text(f'{zwolnienie_xpath}/*[local-name()="P_19C"]'),
            'p_19n': self._get_text(f'{zwolnienie_xpath}/*[local-name()="P_19N"]'),
        }
    
    def _get_new_vehicles(self, adnotacje_xpath: str) -> Dict[str, Any]:
        """Pobiera dane o nowych środkach transportu."""
        nst_xpath = f'{adnotacje_xpath}/*[local-name()="NoweSrodkiTransportu"]'
        
        result = {
            'p_22': self._get_text(f'{nst_xpath}/*[local-name()="P_22"]'),
            'p_42_5': self._get_text(f'{nst_xpath}/*[local-name()="P_42_5"]'),
            'p_22n': self._get_text(f'{nst_xpath}/*[local-name()="P_22N"]'),
            'pojazdy': []
        }
        
        # Pobierz szczegóły pojazdów (max 10000)
        vehicle_elements = self._xpath(f'{nst_xpath}/*[local-name()="NowySrodekTransportu"]')
        
        for vehicle in vehicle_elements:
            vehicle_data = {
                'p_22a': self._get_text('*[local-name()="P_22A"]', element=vehicle),  # Data dopuszczenia
                'p_nr_wiersza_nst': self._get_text('*[local-name()="P_NrWierszaNST"]', element=vehicle),  # Nr wiersza
                'p_22bmk': self._get_text('*[local-name()="P_22BMK"]', element=vehicle),  # Marka
                'p_22bmd': self._get_text('*[local-name()="P_22BMD"]', element=vehicle),  # Model
                'p_22bk': self._get_text('*[local-name()="P_22BK"]', element=vehicle),  # Kolor
                'p_22bnr': self._get_text('*[local-name()="P_22BNR"]', element=vehicle),  # Nr rejestracyjny
                'p_22brp': self._get_text('*[local-name()="P_22BRP"]', element=vehicle),  # Rok produkcji
                # Pojazdy lądowe
                'p_22b': self._get_text('*[local-name()="P_22B"]', element=vehicle),  # Przebieg
                'p_22b1': self._get_text('*[local-name()="P_22B1"]', element=vehicle),  # VIN
                'p_22b2': self._get_text('*[local-name()="P_22B2"]', element=vehicle),  # Nr nadwozia
                'p_22b3': self._get_text('*[local-name()="P_22B3"]', element=vehicle),  # Nr podwozia
                'p_22b4': self._get_text('*[local-name()="P_22B4"]', element=vehicle),  # Nr ramy
                # Statki powietrzne
                'p_22c': self._get_text('*[local-name()="P_22C"]', element=vehicle),  # Liczba godzin pracy
                # Statki
                'p_22d': self._get_text('*[local-name()="P_22D"]', element=vehicle),  # Liczba motogodzin pracy
            }
            result['pojazdy'].append(vehicle_data)
        
        return result
    
    def _get_margin_procedure(self, adnotacje_xpath: str) -> Dict[str, str]:
        """Pobiera dane o procedurze marży."""
        pmarzy_xpath = f'{adnotacje_xpath}/*[local-name()="PMarzy"]'
        
        return {
            'p_pmarzy': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzy"]'),  # Znacznik ogólny
            'p_pmarzy_2': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzy_2"]'),  # Biura podróży
            'p_pmarzy_3_1': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzy_3_1"]'),  # Towary używane
            'p_pmarzy_3_2': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzy_3_2"]'),  # Dzieła sztuki
            'p_pmarzy_3_3': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzy_3_3"]'),  # Przedmioty kolekcjonerskie
            'p_pmarzyn': self._get_text(f'{pmarzy_xpath}/*[local-name()="P_PMarzyN"]'),  # Brak procedury marży
        }
    
    # ========================================================================
    # DODATKOWE OPISY
    # ========================================================================
    
    def _get_additional_descriptions(self) -> List[Dict[str, str]]:
        """Pobiera dodatkowe opisy (DodatkowyOpis)."""
        descriptions = []
        desc_elements = self._xpath('.//*[local-name()="Fa"]/*[local-name()="DodatkowyOpis"]')
        
        for desc in desc_elements:
            descriptions.append({
                'klucz': self._get_text('*[local-name()="Klucz"]', element=desc),
                'wartosc': self._get_text('*[local-name()="Wartosc"]', element=desc),
            })
        
        return descriptions
    
    # ========================================================================
    # FAKTURY ZALICZKOWE
    # ========================================================================
    
    def _get_advance_invoices(self) -> List[Dict[str, str]]:
        """Pobiera numery faktur zaliczkowych."""
        invoices = []
        inv_elements = self._xpath('.//*[local-name()="Fa"]/*[local-name()="FakturaZaliczkowa"]')
        
        for inv in inv_elements:
            invoice_data = {
                'nr_ksef_zn': self._get_text('*[local-name()="NrKSeFZN"]', element=inv),
                'nr_fa_zaliczkowej': self._get_text('*[local-name()="NrFaZaliczkowej"]', element=inv),
                'nr_ksef_fa_zaliczkowej': self._get_text('*[local-name()="NrKSeFFaZaliczkowej"]', element=inv),
            }
            invoices.append(invoice_data)
        
        return invoices
    
    def _get_excise_refund(self) -> str:
        """Pobiera informację o zwrocie akcyzy."""
        return self._get_text('.//*[local-name()="Fa"]/*[local-name()="ZwrotAkcyzy"]')
    
    # ========================================================================
    # ROZLICZENIE
    # ========================================================================
    
    def _get_settlement(self) -> Optional[Dict[str, Any]]:
        """Pobiera dane rozliczenia."""
        rozliczenie_xpath = './/*[local-name()="Fa"]/*[local-name()="Rozliczenie"]'
        
        if not self._xpath(rozliczenie_xpath):
            return None
        
        return {
            'obciazenia': self._get_charges(rozliczenie_xpath),
            'suma_obciazen': self._format_amount(self._get_text(f'{rozliczenie_xpath}/*[local-name()="SumaObciazen"]')),
            'odliczenia': self._get_deductions(rozliczenie_xpath),
            'suma_odliczen': self._format_amount(self._get_text(f'{rozliczenie_xpath}/*[local-name()="SumaOdliczen"]')),
            # CHOICE: DoZaplaty LUB DoRozliczenia
            'do_zaplaty': self._format_amount(self._get_text(f'{rozliczenie_xpath}/*[local-name()="DoZaplaty"]')),
            'do_rozliczenia': self._format_amount(self._get_text(f'{rozliczenie_xpath}/*[local-name()="DoRozliczenia"]')),
        }
    
    def _get_charges(self, rozliczenie_xpath: str) -> List[Dict[str, str]]:
        """Pobiera obciążenia."""
        charges = []
        charge_elements = self._xpath(f'{rozliczenie_xpath}/*[local-name()="Obciazenia"]')
        
        for charge in charge_elements:
            charges.append({
                'kwota': self._format_amount(self._get_text('*[local-name()="Kwota"]', element=charge)),
                'powod': self._get_text('*[local-name()="Powod"]', element=charge),
            })
        
        return charges
    
    def _get_deductions(self, rozliczenie_xpath: str) -> List[Dict[str, str]]:
        """Pobiera odliczenia."""
        deductions = []
        deduction_elements = self._xpath(f'{rozliczenie_xpath}/*[local-name()="Odliczenia"]')
        
        for deduction in deduction_elements:
            deductions.append({
                'kwota': self._format_amount(self._get_text('*[local-name()="Kwota"]', element=deduction)),
                'powod': self._get_text('*[local-name()="Powod"]', element=deduction),
            })
        
        return deductions
    
    # ========================================================================
    # PŁATNOŚĆ
    # ========================================================================
    
    def _get_payment(self) -> Optional[Dict[str, Any]]:
        """Pobiera dane płatności."""
        platnosc_xpath = './/*[local-name()="Fa"]/*[local-name()="Platnosc"]'
        
        if not self._xpath(platnosc_xpath):
            return None
        
        # Zaplacono - TWybor1 (1 = zapłacono), NIE kwota!
        zaplacono = self._get_text(f'{platnosc_xpath}/*[local-name()="Zaplacono"]')
        
        return {
            # CHOICE 1: Zaplacono + DataZaplaty
            'zaplacono': zaplacono,  # '1' = zapłacono
            'data_zaplaty': self._get_text(f'{platnosc_xpath}/*[local-name()="DataZaplaty"]'),
            
            # CHOICE 2: ZnacznikZaplatyCzesciowej + ZaplataCzesciowa[]
            'znacznik_zaplaty_czesciowej': self._get_text(f'{platnosc_xpath}/*[local-name()="ZnacznikZaplatyCzesciowej"]'),  # 1=część, 2=całość
            'zaplata_czesciowa': self._get_partial_payments(platnosc_xpath),
            
            # Termin płatności (może być wiele)
            'termin_platnosci': self._get_payment_terms(platnosc_xpath),
            
            # Forma płatności - CHOICE: FormaPlatnosci LUB (PlatnoscInna + OpisPlatnosci)
            'forma_platnosci': self._get_payment_form(platnosc_xpath),
            'platnosc_inna': self._get_text(f'{platnosc_xpath}/*[local-name()="PlatnoscInna"]'),
            'opis_platnosci': self._get_text(f'{platnosc_xpath}/*[local-name()="OpisPlatnosci"]'),
            
            # Rachunki bankowe
            'rachunki_bankowe': self._get_bank_accounts(platnosc_xpath),
            'rachunki_bankowe_faktora': self._get_bank_accounts_factor(platnosc_xpath),
            
            # Skonto
            'skonto': self._get_discount(platnosc_xpath),
            
            # Link i IPKSeF
            'link_do_platnosci': self._get_text(f'{platnosc_xpath}/*[local-name()="LinkDoPlatnosci"]'),
            'ipksef': self._get_text(f'{platnosc_xpath}/*[local-name()="IPKSeF"]'),
        }
    
    def _get_payment_terms(self, platnosc_xpath: str) -> List[Dict[str, Any]]:
        """Pobiera terminy płatności (może być wiele - max 100)."""
        terms = []
        term_elements = self._xpath(f'{platnosc_xpath}/*[local-name()="TerminPlatnosci"]')
        
        for term in term_elements:
            term_data = {
                'termin': self._get_text('*[local-name()="Termin"]', element=term),
                'termin_opis': self._get_payment_term_description(term),
            }
            terms.append(term_data)
        
        # Dla kompatybilności wstecznej - zwróć pierwszy jako dict jeśli jest tylko jeden
        if len(terms) == 1:
            return terms[0]
        elif len(terms) > 1:
            return terms
        else:
            return {}
    
    def _get_payment_term_description(self, term_element) -> Optional[Dict[str, str]]:
        """Pobiera opis terminu płatności."""
        opis_xpath = '*[local-name()="TerminOpis"]'
        
        if not self._xpath(opis_xpath, term_element):
            return None
        
        return {
            'ilosc': self._get_text(f'{opis_xpath}/*[local-name()="Ilosc"]', element=term_element),
            'jednostka': self._get_text(f'{opis_xpath}/*[local-name()="Jednostka"]', element=term_element),
            'zdarzenie_poczatkowe': self._get_text(f'{opis_xpath}/*[local-name()="ZdarzeniePoczatkowe"]', element=term_element),
        }
    
    def _get_payment_form(self, platnosc_xpath: str) -> Optional[Dict[str, str]]:
        """Pobiera formę płatności jako dict z kodem i opisem."""
        forma_code = self._get_text(f'{platnosc_xpath}/*[local-name()="FormaPlatnosci"]')
        
        if not forma_code:
            return None
        
        # Mapowanie kodów form płatności
        forma_mapping = {
            '1': 'Gotówka',
            '2': 'Karta',
            '3': 'Bon',
            '4': 'Czek',
            '5': 'Kredyt',
            '6': 'Przelew',
            '7': 'Mobilna',
        }
        
        return {
            'kod': forma_code,
            'nazwa': forma_mapping.get(forma_code, forma_code),
        }
    
    def _get_partial_payments(self, platnosc_xpath: str) -> List[Dict[str, Any]]:
        """Pobiera zapłaty częściowe (max 100)."""
        payments = []
        payment_elements = self._xpath(f'{platnosc_xpath}/*[local-name()="ZaplataCzesciowa"]')
        
        for payment in payment_elements:
            payment_data = {
                'kwota': self._format_amount(self._get_text('*[local-name()="KwotaZaplatyCzesciowej"]', element=payment)),
                'data': self._get_text('*[local-name()="DataZaplatyCzesciowej"]', element=payment),
                'forma_platnosci': self._get_text('*[local-name()="FormaPlatnosci"]', element=payment),
                'platnosc_inna': self._get_text('*[local-name()="PlatnoscInna"]', element=payment),
                'opis_platnosci': self._get_text('*[local-name()="OpisPlatnosci"]', element=payment),
            }
            payments.append(payment_data)
        
        return payments
    
    def _get_bank_accounts(self, platnosc_xpath: str) -> List[Dict[str, str]]:
        """Pobiera rachunki bankowe (max 100)."""
        accounts = []
        account_elements = self._xpath(f'{platnosc_xpath}/*[local-name()="RachunekBankowy"]')
        
        for account in account_elements:
            accounts.append({
                'nr_rb': self._get_text('*[local-name()="NrRB"]', element=account),
                'swift': self._get_text('*[local-name()="SWIFT"]', element=account),
                'nazwa_banku': self._get_text('*[local-name()="NazwaBanku"]', element=account),
                'opis_rachunku': self._get_text('*[local-name()="OpisRachunku"]', element=account),
            })
        
        return accounts
    
    def _get_bank_accounts_factor(self, platnosc_xpath: str) -> List[Dict[str, str]]:
        """Pobiera rachunki bankowe faktora (max 20)."""
        accounts = []
        account_elements = self._xpath(f'{platnosc_xpath}/*[local-name()="RachunekBankowyFaktora"]')
        
        for account in account_elements:
            accounts.append({
                'nr_rb': self._get_text('*[local-name()="NrRB"]', element=account),
                'swift': self._get_text('*[local-name()="SWIFT"]', element=account),
                'nazwa_banku': self._get_text('*[local-name()="NazwaBanku"]', element=account),
                'opis_rachunku': self._get_text('*[local-name()="OpisRachunku"]', element=account),
            })
        
        return accounts
    
    def _get_discount(self, platnosc_xpath: str) -> Optional[Dict[str, str]]:
        """Pobiera dane skonta."""
        skonto_xpath = f'{platnosc_xpath}/*[local-name()="Skonto"]'
        
        if not self._xpath(skonto_xpath):
            return None
        
        return {
            'warunki': self._get_text(f'{skonto_xpath}/*[local-name()="WarunkiSkonta"]'),
            'wysokosc': self._get_text(f'{skonto_xpath}/*[local-name()="WysokoscSkonta"]'),
        }
    
    # ========================================================================
    # WARUNKI TRANSAKCJI
    # ========================================================================
    
    def _get_transaction_terms(self) -> Optional[Dict[str, Any]]:
        """Pobiera warunki transakcji."""
        warunki_xpath = './/*[local-name()="Fa"]/*[local-name()="WarunkiTransakcji"]'
        
        if not self._xpath(warunki_xpath):
            return None
        
        return {
            'umowy': self._get_contracts(warunki_xpath),
            'zamowienia': self._get_orders_list(warunki_xpath),
            'numery_partii_towaru': self._get_batch_numbers(warunki_xpath),
            'warunki_dostawy': self._get_text(f'{warunki_xpath}/*[local-name()="WarunkiDostawy"]'),
            'kurs_umowny': self._get_text(f'{warunki_xpath}/*[local-name()="KursUmowny"]'),
            'waluta_umowna': self._get_text(f'{warunki_xpath}/*[local-name()="WalutaUmowna"]'),
            'transport': self._get_transport_list(warunki_xpath),
            'podmiot_posredniczacy': self._get_text(f'{warunki_xpath}/*[local-name()="PodmiotPosredniczacy"]'),
        }
    
    def _get_contracts(self, warunki_xpath: str) -> List[Dict[str, str]]:
        """Pobiera umowy (max 100)."""
        contracts = []
        contract_elements = self._xpath(f'{warunki_xpath}/*[local-name()="Umowy"]')
        
        for contract in contract_elements:
            contracts.append({
                'data_umowy': self._get_text('*[local-name()="DataUmowy"]', element=contract),
                'nr_umowy': self._get_text('*[local-name()="NrUmowy"]', element=contract),
            })
        
        return contracts
    
    def _get_orders_list(self, warunki_xpath: str) -> List[Dict[str, str]]:
        """Pobiera zamówienia z WarunkiTransakcji (max 100)."""
        orders = []
        order_elements = self._xpath(f'{warunki_xpath}/*[local-name()="Zamowienia"]')
        
        for order in order_elements:
            orders.append({
                'data_zamowienia': self._get_text('*[local-name()="DataZamowienia"]', element=order),
                'nr_zamowienia': self._get_text('*[local-name()="NrZamowienia"]', element=order),
            })
        
        return orders
    
    def _get_batch_numbers(self, warunki_xpath: str) -> List[str]:
        """Pobiera numery partii towaru (max 1000)."""
        batch_elements = self._xpath(f'{warunki_xpath}/*[local-name()="NrPartiiTowaru"]')
        return [batch.text for batch in batch_elements if batch.text]
    
    def _get_transport_list(self, warunki_xpath: str) -> List[Dict[str, Any]]:
        """Pobiera dane transportu (max 20)."""
        transports = []
        transport_elements = self._xpath(f'{warunki_xpath}/*[local-name()="Transport"]')
        
        for transport in transport_elements:
            transport_data = {
                # CHOICE: RodzajTransportu LUB (TransportInny + OpisInnegoTransportu)
                'rodzaj_transportu': self._get_text('*[local-name()="RodzajTransportu"]', element=transport),
                'transport_inny': self._get_text('*[local-name()="TransportInny"]', element=transport),
                'opis_innego_transportu': self._get_text('*[local-name()="OpisInnegoTransportu"]', element=transport),
                
                # Przewoźnik (opcjonalny)
                'przewoznik': self._get_carrier(transport),
                
                # Numer zlecenia
                'nr_zlecenia_transportu': self._get_text('*[local-name()="NrZleceniaTransportu"]', element=transport),
                
                # CHOICE: OpisLadunku LUB (LadunekInny + OpisInnegoLadunku)
                'opis_ladunku': self._get_text('*[local-name()="OpisLadunku"]', element=transport),
                'ladunek_inny': self._get_text('*[local-name()="LadunekInny"]', element=transport),
                'opis_innego_ladunku': self._get_text('*[local-name()="OpisInnegoLadunku"]', element=transport),
                
                # Jednostka opakowania
                'jednostka_opakowania': self._get_text('*[local-name()="JednostkaOpakowania"]', element=transport),
                
                # Daty transportu
                'data_godz_rozp_transportu': self._get_text('*[local-name()="DataGodzRozpTransportu"]', element=transport),
                'data_godz_zak_transportu': self._get_text('*[local-name()="DataGodzZakTransportu"]', element=transport),
                
                # Adresy wysyłki
                'wysylka_z': self._get_address_from_element('*[local-name()="WysylkaZ"]', transport),
                'wysylka_przez': self._get_shipping_via(transport),
                'wysylka_do': self._get_address_from_element('*[local-name()="WysylkaDo"]', transport),
            }
            transports.append(transport_data)
        
        return transports
    
    def _get_carrier(self, transport_element) -> Optional[Dict[str, Any]]:
        """Pobiera dane przewoźnika."""
        przewoznik_xpath = '*[local-name()="Przewoznik"]'
        
        if not self._xpath(przewoznik_xpath, transport_element):
            return None
        
        przewoznik = self._xpath(przewoznik_xpath, transport_element)[0]
        
        return {
            'dane_identyfikacyjne': self._get_carrier_identification(przewoznik),
            'adres': self._get_address_from_element('*[local-name()="AdresPrzewoznika"]', przewoznik),
        }
    
    def _get_carrier_identification(self, przewoznik_element) -> Dict[str, str]:
        """Pobiera dane identyfikacyjne przewoźnika (TPodmiot2)."""
        dane_id_xpath = '*[local-name()="DaneIdentyfikacyjne"]'
        
        return {
            'nip': self._get_text(f'{dane_id_xpath}/*[local-name()="NIP"]', element=przewoznik_element),
            'nip_ue': self._get_text(f'{dane_id_xpath}/*[local-name()="NIP_UE"]', element=przewoznik_element),
            'nr_id': self._get_text(f'{dane_id_xpath}/*[local-name()="NrID"]', element=przewoznik_element),
            'kod_kraju': self._get_text(f'{dane_id_xpath}/*[local-name()="KodKraju"]', element=przewoznik_element),
            'nazwa': self._get_text(f'{dane_id_xpath}/*[local-name()="Nazwa"]', element=przewoznik_element),
        }
    
    def _get_shipping_via(self, transport_element) -> List[Dict[str, str]]:
        """Pobiera adresy pośrednie wysyłki (max 20)."""
        addresses = []
        via_elements = self._xpath('*[local-name()="WysylkaPrzez"]', transport_element)
        
        for via in via_elements:
            addr = self._get_address_from_element('.', via)
            if addr:
                addresses.append(addr)
        
        return addresses
    
    
    # ========================================================================
    # ZAMÓWIENIE (dla faktur zaliczkowych)
    # ========================================================================
    
    def _get_order(self) -> Optional[Dict[str, Any]]:
        """Pobiera szczegółowe dane zamówienia (Zamowienie) - dla faktur zaliczkowych."""
        zamowienie_xpath = './/*[local-name()="Fa"]/*[local-name()="Zamowienie"]'
        
        if not self._xpath(zamowienie_xpath):
            return None
        
        order_lines = []
        line_elements = self._xpath(f'{zamowienie_xpath}/*[local-name()="ZamowienieWiersz"]')
        
        for line in line_elements:
            wartosc_netto_str = self._get_text('*[local-name()="P_11NettoZ"]', element=line)
            kwota_vat_str = self._get_text('*[local-name()="P_11VatZ"]', element=line)
            
            # Oblicz wartość brutto (netto + VAT)
            wartosc_brutto_str = ''
            if wartosc_netto_str and kwota_vat_str:
                try:
                    netto = Decimal(wartosc_netto_str.replace(',', '.'))
                    vat = Decimal(kwota_vat_str.replace(',', '.'))
                    brutto = netto + vat
                    wartosc_brutto_str = self._format_decimal(brutto)
                except (ValueError, TypeError):
                    pass
            
            line_data = {
                'nr_wiersza': self._get_text('*[local-name()="NrWierszaZam"]', element=line),
                'uu_id': self._get_text('*[local-name()="UU_IDZ"]', element=line),
                'nazwa': self._get_text('*[local-name()="P_7Z"]', element=line),
                'indeks': self._get_text('*[local-name()="IndeksZ"]', element=line),
                'jednostka': self._get_text('*[local-name()="P_8AZ"]', element=line),
                'ilosc': self._format_quantity(self._get_text('*[local-name()="P_8BZ"]', element=line)),
                'cena_netto': self._format_amount(self._get_text('*[local-name()="P_9AZ"]', element=line)),
                'wartosc_netto': self._format_amount(wartosc_netto_str),
                'kwota_vat': self._format_amount(kwota_vat_str),
                'wartosc_brutto': wartosc_brutto_str,
                'stawka_vat': self._get_text('*[local-name()="P_12Z"]', element=line),
                'pkwiu': self._get_text('*[local-name()="PKWIU"]', element=line),
                'cn': self._get_text('*[local-name()="CN"]', element=line),
                'pkob': self._get_text('*[local-name()="PKOB"]', element=line),
                'stan_przed': self._get_text('*[local-name()="StanPrzedZ"]', element=line),
            }
            order_lines.append(line_data)
        
        return {
            'wartosc_zamowienia': self._format_amount(self._get_text(f'{zamowienie_xpath}/*[local-name()="WartoscZamowienia"]')),
            'wiersze': order_lines,
        }
    
    # ========================================================================
    # STOPKA
    # ========================================================================
    
    def _get_footer(self) -> Optional[Dict[str, Any]]:
        """Pobiera dane stopki."""
        stopka_xpath = './/*[local-name()="Stopka"]'
        
        if not self._xpath(stopka_xpath):
            return None
        
        return {
            'informacje': self._get_footer_info(stopka_xpath),
            'rejestry': self._get_footer_registers(stopka_xpath),
        }
    
    def _get_footer_info(self, stopka_xpath: str) -> Dict[str, Any]:
        """Pobiera informacje ze stopki."""
        info_xpath = f'{stopka_xpath}/*[local-name()="Informacje"]'
        
        return {
            'stopka_faktury': self._get_text(f'{info_xpath}/*[local-name()="StopkaFaktury"]'),
            'warunki_dodatkowe': self._get_additional_terms(info_xpath),
        }
    
    def _get_additional_terms(self, info_xpath: str) -> List[str]:
        """Pobiera warunki dodatkowe."""
        terms = []
        term_elements = self._xpath(f'{info_xpath}/*[local-name()="WarunkiDodatkowe"]')
        
        for term in term_elements:
            if term.text:
                terms.append(term.text)
        
        return terms
    
    def _get_footer_registers(self, stopka_xpath: str) -> Dict[str, str]:
        """Pobiera rejestry ze stopki."""
        rejestry_xpath = f'{stopka_xpath}/*[local-name()="Rejestry"]'
        
        return {
            'krs': self._get_text(f'{rejestry_xpath}/*[local-name()="KRS"]'),
            'ceidg': self._get_text(f'{rejestry_xpath}/*[local-name()="CEIDG"]'),
            'regon': self._get_text(f'{rejestry_xpath}/*[local-name()="REGON"]'),
            'bdo': self._get_text(f'{rejestry_xpath}/*[local-name()="BDO"]'),
        }
    
    # ========================================================================
    # ZAŁĄCZNIK
    # ========================================================================
    
    def _get_attachment(self) -> Optional[Dict[str, Any]]:
        """
        Pobiera dane załącznika zgodnie ze schematem XSD FA(3).
        
        Struktura załącznika:
        - Zalacznik (0..1)
          - BlokDanych (1..1000) - bloki danych załącznika
            - ZNaglowek (0..1) - nagłówek bloku
            - MetaDane (1..1000) - pary klucz/wartość
              - ZKlucz
              - ZWartosc
            - Tekst (0..1)
              - Akapit (1..10) - akapity tekstowe
            - Tabela (0..1000) - tabele danych
              - TMetaDane (0..1000) - metadane tabeli
                - TKlucz
                - TWartosc
              - Opis (0..1)
              - TNaglowek - nagłówek tabeli
                - Kol (1..20) - kolumny z atrybutem Typ i wartością NKom
              - Wiersz (1..1000) - wiersze
                - WKom (1..20) - komórki
              - Suma (0..1) - wiersz podsumowania
                - SKom (1..20) - komórki sumy
        """
        zalacznik_xpath = './/*[local-name()="Zalacznik"]'
        
        zalacznik_elements = self._xpath(zalacznik_xpath)
        if not zalacznik_elements:
            return None
        
        zalacznik = zalacznik_elements[0]
        
        # Pobierz wszystkie BlokDanych
        bloki_danych = []
        blok_xpath = './*[local-name()="BlokDanych"]'
        
        for blok in self._xpath(blok_xpath, zalacznik):
            blok_data = self._parse_blok_danych(blok)
            bloki_danych.append(blok_data)
        
        return {
            'bloki_danych': bloki_danych
        }
    
    def _parse_blok_danych(self, blok) -> Dict[str, Any]:
        """Parsuje pojedynczy BlokDanych załącznika."""
        result = {}
        
        # Nagłówek bloku (opcjonalny)
        naglowek = self._get_text('./*[local-name()="ZNaglowek"]', '', blok)
        if naglowek:
            result['naglowek'] = naglowek
        
        # MetaDane - pary klucz/wartość (wymagane, 1..1000)
        meta_dane = []
        for meta in self._xpath('./*[local-name()="MetaDane"]', blok):
            klucz = self._get_text('./*[local-name()="ZKlucz"]', '', meta)
            wartosc = self._get_text('./*[local-name()="ZWartosc"]', '', meta)
            if klucz:
                meta_dane.append({
                    'klucz': klucz,
                    'wartosc': wartosc
                })
        if meta_dane:
            result['meta_dane'] = meta_dane
        
        # Tekst z akapitami (opcjonalny)
        tekst_elem = self._xpath('./*[local-name()="Tekst"]', blok)
        if tekst_elem:
            akapity = []
            for akapit in self._xpath('./*[local-name()="Akapit"]', tekst_elem[0]):
                if akapit.text:
                    akapity.append(akapit.text)
            if akapity:
                result['tekst'] = {'akapity': akapity}
        
        # Tabele (opcjonalne, 0..1000)
        tabele = []
        for tabela in self._xpath('./*[local-name()="Tabela"]', blok):
            tabela_data = self._parse_tabela_zalacznika(tabela)
            tabele.append(tabela_data)
        if tabele:
            result['tabele'] = tabele
        
        return result
    
    def _parse_tabela_zalacznika(self, tabela) -> Dict[str, Any]:
        """Parsuje pojedynczą tabelę z załącznika."""
        result = {}
        
        # Metadane tabeli (opcjonalne, 0..1000)
        t_meta_dane = []
        for tmeta in self._xpath('./*[local-name()="TMetaDane"]', tabela):
            tklucz = self._get_text('./*[local-name()="TKlucz"]', '', tmeta)
            twartosc = self._get_text('./*[local-name()="TWartosc"]', '', tmeta)
            if tklucz:
                t_meta_dane.append({
                    'klucz': tklucz,
                    'wartosc': twartosc
                })
        if t_meta_dane:
            result['meta_dane'] = t_meta_dane
        
        # Opis tabeli (opcjonalny)
        opis = self._get_text('./*[local-name()="Opis"]', '', tabela)
        if opis:
            result['opis'] = opis
        
        # Nagłówek tabeli z kolumnami
        naglowek = self._xpath('./*[local-name()="TNaglowek"]', tabela)
        if naglowek:
            kolumny = []
            for kol in self._xpath('./*[local-name()="Kol"]', naglowek[0]):
                typ = kol.get('Typ', 'txt')
                nazwa = self._get_text('./*[local-name()="NKom"]', '', kol)
                kolumny.append({
                    'typ': typ,
                    'nazwa': nazwa
                })
            if kolumny:
                result['naglowek'] = kolumny
        
        # Wiersze tabeli (1..1000)
        wiersze = []
        for wiersz in self._xpath('./*[local-name()="Wiersz"]', tabela):
            komorki = []
            for wkom in self._xpath('./*[local-name()="WKom"]', wiersz):
                # WKom może być pusty lub zawierać tekst
                komorki.append(wkom.text if wkom.text else '')
            wiersze.append(komorki)
        if wiersze:
            result['wiersze'] = wiersze
        
        # Suma (opcjonalna)
        suma_elem = self._xpath('./*[local-name()="Suma"]', tabela)
        if suma_elem:
            suma_komorki = []
            for skom in self._xpath('./*[local-name()="SKom"]', suma_elem[0]):
                suma_komorki.append(skom.text if skom.text else '')
            if suma_komorki:
                result['suma'] = suma_komorki
        
        return result
    
    # ========================================================================
    # HELPERY
    # ========================================================================
    
    def _get_partial_advances(self) -> List[Dict[str, Any]]:
        """
        Pobiera dane zaliczek częściowych (ZaliczkaCzesciowa) z poziomu Fa.
        
        Struktura wg XSD FA(3):
        - P_6Z  - data otrzymania płatności
        - P_15Z - kwota płatności (brutto)
        - KursWalutyZW - kurs waluty (opcjonalnie)
        """
        advances: List[Dict[str, Any]] = []

        zaliczka_elements = self._xpath('.//*[local-name()="Fa"]/*[local-name()="ZaliczkaCzesciowa"]')

        for elem in zaliczka_elements:
            kwota_raw = self._get_text('*[local-name()="P_15Z"]', element=elem)
            advance_data = {
                'data_platnosci': self._get_text('*[local-name()="P_6Z"]', element=elem),
                'kwota_platnosci': self._format_amount(kwota_raw),
                'kurs_waluty': self._get_text('*[local-name()="KursWalutyZW"]', element=elem),
            }
            advances.append(advance_data)

        return advances

    def _parse_decimal(self, value_str: str):
        """Parsuje string na Decimal (przecinek/kropka; ignoruje spacje/NBSP/U+202F jako separatory tysięcy)."""
        if not value_str or not str(value_str).strip():
            return None
        try:
            s = str(value_str).strip().replace('\u00a0', '').replace('\u202f', '').replace(' ', '')
            return Decimal(s.replace(',', '.'))
        except Exception:
            return None

    def _format_decimal(self, value) -> str:
        """Formatuje decimal: przecinek dziesiętny, U+202F (wąska spacja nierozdzielająca) co trzy cyfry."""
        formatted = f"{value:.2f}"
        negative = formatted.startswith('-')
        if negative:
            formatted = formatted[1:]
        int_part, frac_part = formatted.split('.')
        i = len(int_part)
        chunks = []
        while i > 0:
            start = max(0, i - 3)
            chunks.insert(0, int_part[start:i])
            i = start
        int_with_spaces = '\u202f'.join(chunks)
        prefix = '-' if negative else ''
        return f"{prefix}{int_with_spaces},{frac_part}"
    
    def _format_quantity(self, value: str) -> str:
        """Formatuje ilość - zamienia kropkę na przecinek jeśli jest liczbą dziesiętną."""
        if not value or value == '':
            return value
        # Zamień kropkę na przecinek dla polskiego formatu
        return value.replace('.', ',')
    
    def _format_amount(self, value: str) -> str:
        """Formatuje kwotę: 2 miejsca po przecinku, U+202F co trzy cyfry (jak _format_decimal)."""
        if not value or value == '':
            return ''
        try:
            decimal_value = Decimal(str(value).replace(',', '.'))
            return self._format_decimal(decimal_value)
        except Exception:
            return value


# ============================================================================
# CLI - tylko jeśli uruchomiony bezpośrednio (test parsera)
# ============================================================================

def main():
    """CLI dla testu parsera."""
    import argparse
    from pathlib import Path
    import json
    
    parser = argparse.ArgumentParser(
        description='Test parsera XML faktury KSeF FA(3)'
    )
    parser.add_argument('xml_file', help='Plik XML faktury')
    parser.add_argument('--json', action='store_true', help='Wypisz dane jako JSON')
    parser.add_argument('--full', action='store_true', help='Wypisz wszystkie dane')
    
    args = parser.parse_args()
    
    xml_path = Path(args.xml_file)
    
    if not xml_path.exists():
        print(f"[!] Plik nie istnieje: {xml_path}", file=sys.stderr)
        return 1
    
    print(f"[+] Parsowanie: {xml_path}")
    
    try:
        with open(xml_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        
        invoice_parser = InvoiceXMLParserFA3(xml_content)
        invoice_data = invoice_parser.parse()
        
        if args.json:
            print(json.dumps(invoice_data, ensure_ascii=False, indent=2))
        else:
            print(f"\n{'='*80}")
            print(f"FAKTURA FA(3) - SZCZEGÓŁOWE DANE")
            print(f"{'='*80}")
            
            # Nagłówek
            print(f"\n[NAGŁÓWEK]")
            print(f"  Kod systemowy: {invoice_data['naglowek']['kod_systemowy']}")
            print(f"  Wersja schemy: {invoice_data['naglowek']['wersja_schemy']}")
            print(f"  Data wytworzenia: {invoice_data['naglowek']['data_wytworzenia']}")
            print(f"  System: {invoice_data['naglowek']['system_info']}")
            
            # Podstawowe dane
            print(f"\n[DANE FAKTURY]")
            print(f"  Numer: {invoice_data['numer']}")
            print(f"  Data wystawienia: {invoice_data['data_wystawienia']}")
            if invoice_data['miejsce_wystawienia']:
                print(f"  Miejsce wystawienia: {invoice_data['miejsce_wystawienia']}")
            if invoice_data['data_sprzedazy']:
                print(f"  Data sprzedaży: {invoice_data['data_sprzedazy']}")
            if invoice_data['okres_sprzedazy']:
                print(f"  Okres sprzedaży: {invoice_data['okres_sprzedazy']['od']} - {invoice_data['okres_sprzedazy']['do']}")
            print(f"  Waluta: {invoice_data['waluta']}")
            if invoice_data['rodzaj_faktury']:
                print(f"  Rodzaj faktury: {invoice_data['rodzaj_faktury']}")
            
            # Sprzedawca
            print(f"\n[SPRZEDAWCA]")
            print(f"  Nazwa: {invoice_data['sprzedawca']['dane_identyfikacyjne']['nazwa']}")
            print(f"  NIP: {invoice_data['sprzedawca']['dane_identyfikacyjne']['nip']}")
            if invoice_data['sprzedawca']['adres']:
                addr = invoice_data['sprzedawca']['adres']
                print(f"  Adres: {addr['adres_l1']}, {addr['adres_l2']}")
            if invoice_data['sprzedawca']['dane_kontaktowe']:
                for i, contact in enumerate(invoice_data['sprzedawca']['dane_kontaktowe'], 1):
                    if contact['email']:
                        print(f"  Email {i}: {contact['email']}")
                    if contact['telefon']:
                        print(f"  Telefon {i}: {contact['telefon']}")
            
            # Nabywca
            print(f"\n[NABYWCA]")
            dane_id = invoice_data['nabywca']['dane_identyfikacyjne']
            print(f"  Nazwa: {dane_id['nazwa']}")
            if dane_id['nip']:
                print(f"  NIP: {dane_id['nip']}")
            if dane_id['nip_ue']:
                print(f"  NIP UE: {dane_id['nip_ue']}")
            if invoice_data['nabywca']['adres']:
                addr = invoice_data['nabywca']['adres']
                print(f"  Adres: {addr['adres_l1']}, {addr['adres_l2']}")
            if invoice_data['nabywca']['nr_klienta']:
                print(f"  Nr klienta: {invoice_data['nabywca']['nr_klienta']}")
            
            # Pozycje
            print(f"\n[POZYCJE] ({len(invoice_data['pozycje'])})")
            for i, item in enumerate(invoice_data['pozycje'], 1):
                print(f"  {i}. {item['nazwa']}")
                if item['ilosc'] and item['jednostka']:
                    print(f"     Ilość: {item['ilosc']} {item['jednostka']}")
                if item['cena_netto']:
                    print(f"     Cena netto: {item['cena_netto']}")
                print(f"     Wartość netto: {item['wartosc_netto']}")
                if item.get('stawka_vat'):
                    print(f"     Stawka VAT: {item['stawka_vat']}%")
                print(f"     Wartość brutto: {item['wartosc_brutto']}")
            
            # Podsumowanie
            print(f"\n[PODSUMOWANIE]")
            print(f"  Netto: {invoice_data['podsumowanie']['netto']} {invoice_data['waluta']}")
            print(f"  VAT: {invoice_data['podsumowanie']['vat']} {invoice_data['waluta']}")
            print(f"  Brutto: {invoice_data['podsumowanie']['brutto']} {invoice_data['waluta']}")
            
            # Rozliczenie
            if invoice_data['rozliczenie']:
                print(f"\n[ROZLICZENIE]")
                if invoice_data['rozliczenie']['suma_obciazen']:
                    print(f"  Suma obciążeń: {invoice_data['rozliczenie']['suma_obciazen']}")
                if invoice_data['rozliczenie']['suma_odliczen']:
                    print(f"  Suma odliczeń: {invoice_data['rozliczenie']['suma_odliczen']}")
                if invoice_data['rozliczenie']['do_zaplaty']:
                    print(f"  Do zapłaty: {invoice_data['rozliczenie']['do_zaplaty']} {invoice_data['waluta']}")
            
            # Płatność
            if invoice_data['platnosc']:
                print(f"\n[PŁATNOŚĆ]")
                if invoice_data['platnosc']['termin_platnosci']['termin']:
                    print(f"  Termin: {invoice_data['platnosc']['termin_platnosci']['termin']}")
                if invoice_data['platnosc']['forma_platnosci']:
                    print(f"  Forma: {invoice_data['platnosc']['forma_platnosci']}")
                if invoice_data['platnosc']['rachunki_bankowe']:
                    for i, account in enumerate(invoice_data['platnosc']['rachunki_bankowe'], 1):
                        print(f"  Rachunek {i}: {account['nr_rb']}")
                        if account['nazwa_banku']:
                            print(f"    Bank: {account['nazwa_banku']}")
            
            # Dodatkowe dane (tylko z --full)
            if args.full:
                # Adnotacje
                if invoice_data['adnotacje']:
                    print(f"\n[ADNOTACJE]")
                    for key, value in invoice_data['adnotacje'].items():
                        if value and value not in ['', '2', {}]:  # Pomijaj puste i domyślne "2" (=nie)
                            print(f"  {key}: {value}")
                
                # Dodatkowe opisy
                if invoice_data['dodatkowe_opisy']:
                    print(f"\n[DODATKOWE OPISY]")
                    for desc in invoice_data['dodatkowe_opisy']:
                        print(f"  {desc['klucz']}: {desc['wartosc']}")
                
                # Stopka
                if invoice_data['stopka']:
                    print(f"\n[STOPKA]")
                    if invoice_data['stopka']['informacje']['stopka_faktury']:
                        print(f"  {invoice_data['stopka']['informacje']['stopka_faktury']}")
                    if invoice_data['stopka']['rejestry']:
                        for key, value in invoice_data['stopka']['rejestry'].items():
                            if value:
                                print(f"  {key.upper()}: {value}")
            
            print(f"\n{'='*80}")
        
    except Exception as e:
        print(f"[!] BŁĄD: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

