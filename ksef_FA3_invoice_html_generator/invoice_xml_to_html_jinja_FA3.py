#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moduł do konwersji XML faktury KSeF FA(3) do HTML z użyciem szablonów Jinja2.

Dedykowany dla FA(3) z pełnymi danymi z parsera FA(3).

Przykład użycia:
    from invoice_xml_to_html_jinja_FA3 import xml_to_html, xml_file_to_html
    
    # Z XML stringa
    html = xml_to_html(xml_content)
    
    # Z pliku XML
    html = xml_file_to_html('faktura.xml')
    
    # Z własnym szablonem
    html = xml_to_html(xml_content, template_path='my_template.jinja2')
    
    # Z szablonem kolorowym
    html = xml_to_html(xml_content, template_path='invoice_template_fa3_kolor.jinja2')
"""

import sys
from pathlib import Path
from typing import Optional

# Import parsera FA(3)
from invoice_xml_parser_FA3 import InvoiceXMLParserFA3

try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape, Template
    JINJA2_AVAILABLE = True
except ImportError:
    JINJA2_AVAILABLE = False

# Fix encoding dla Windows console
if sys.platform == 'win32':
    import codecs
    if hasattr(sys.stdout, 'buffer'):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


# ============================================================================
# Generator HTML z szablonami Jinja2 dla FA(3)
# ============================================================================

class InvoiceHTMLGeneratorJinjaFA3:
    """Generator HTML dla faktury FA(3) używający szablonów Jinja2."""
    
    def __init__(self, invoice_data: dict, template_path: Optional[Path] = None):
        """
        Inicjalizacja generatora.
        
        Args:
            invoice_data: Słownik z danymi faktury (z InvoiceXMLParserFA3)
            template_path: Ścieżka do szablonu Jinja2 (opcjonalnie)
        """
        if not JINJA2_AVAILABLE:
            raise ImportError(
                "Biblioteka jinja2 nie jest zainstalowana. "
                "Zainstaluj ją używając: pip install jinja2"
            )
        
        self.data = invoice_data
        self.template_path = template_path or self._get_default_template()
    
    def _get_default_template(self) -> Path:
        """Zwraca ścieżkę do domyślnego szablonu FA(3)."""
        script_dir = Path(__file__).parent
        return script_dir / 'invoice_template_fa3.jinja2'
    
    def _prepare_template_data(self) -> dict:
        """
        Przygotowuje dane dla szablonu Jinja2.
        Dodaje helpery i formatowanie.
        """
        # Kopiuj wszystkie dane
        template_data = self.data.copy()
        
        # Dodaj numer KSeF jeśli jest dostępny (może być w danych lub przekazany z zewnątrz)
        # Sprawdź czy jest w danych faktury (np. z zewnętrznego źródła)
        template_data['ksefNumber'] = self.data.get('nr_ksef', '') or self.data.get('ksef_number', '')
        
        # Dodaj helpery
        template_data['format_address'] = self._format_address
        template_data['format_contact'] = self._format_contact
        template_data['has_value'] = self._has_value
        
        return template_data
    
    def _format_address(self, addr: dict) -> str:
        """Formatuje adres do HTML."""
        if not addr:
            return ""
        
        parts = []
        if addr.get('adres_l1'):
            parts.append(addr['adres_l1'])
        if addr.get('adres_l2'):
            parts.append(addr['adres_l2'])
        
        return '<br>'.join(parts)
    
    def _format_contact(self, contacts: list) -> str:
        """Formatuje dane kontaktowe do HTML."""
        if not contacts:
            return ""
        
        contact_html = []
        for contact in contacts:
            if contact.get('email'):
                contact_html.append(f"✉ {contact['email']}")
            if contact.get('telefon'):
                contact_html.append(f"☎ {contact['telefon']}")
        
        return '<br>'.join(contact_html)
    
    def _has_value(self, value) -> bool:
        """Sprawdza czy wartość jest niepusta."""
        if value is None:
            return False
        if isinstance(value, str) and not value:
            return False
        if isinstance(value, (list, dict)) and not value:
            return False
        return True
    
    def generate(self) -> str:
        """
        Generuje HTML faktury z szablonu Jinja2.
        
        Returns:
            str: HTML faktury
        """
        template_path = Path(self.template_path)
        
        if not template_path.exists():
            raise FileNotFoundError(
                f"Szablon nie istnieje: {template_path}\n"
                f"Upewnij się, że plik invoice_template_fa3.jinja2 znajduje się w katalogu skryptu."
            )
        
        # Konfiguracja Jinja2 environment
        env = Environment(
            loader=FileSystemLoader(template_path.parent),
            autoescape=select_autoescape(['html', 'xml', 'jinja2']),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Dodaj niestandardowe filtry
        env.filters['has_value'] = self._has_value
        
        # Załaduj szablon
        template = env.get_template(template_path.name)
        
        # Przygotuj dane
        template_data = self._prepare_template_data()
        
        # Renderuj szablon z danymi faktury
        html = template.render(**template_data)
        
        return html


# ============================================================================
# PUBLICZNE API - Główne funkcje do użycia w innych skryptach
# ============================================================================

def xml_to_html(xml_content: str, template_path: Optional[Path] = None) -> str:
    """
    Konwertuje XML faktury KSeF FA(3) do HTML używając szablonu Jinja2.
    
    Args:
        xml_content: String z XML faktury FA(3)
        template_path: Ścieżka do szablonu Jinja2 (opcjonalnie)
    
    Returns:
        str: HTML faktury
    
    Example:
        >>> with open('faktura.xml', 'r', encoding='utf-8') as f:
        ...     xml_content = f.read()
        >>> html = xml_to_html(xml_content)
        >>> with open('faktura.html', 'w', encoding='utf-8') as f:
        ...     f.write(html)
        
        >>> # Z kolorowym szablonem
        >>> html = xml_to_html(xml_content, template_path='invoice_template_fa3_kolor.jinja2')
    """
    try:
        # Parsuj XML z parserem FA(3)
        parser = InvoiceXMLParserFA3(xml_content)
        invoice_data = parser.parse()
        
        # Generuj HTML z szablonu
        generator = InvoiceHTMLGeneratorJinjaFA3(invoice_data, template_path)
        html = generator.generate()
        
        return html
    except Exception as e:
        print(f"[!] Błąd konwersji XML → HTML: {e}", file=sys.stderr)
        raise


def xml_file_to_html(xml_path: Path, template_path: Optional[Path] = None) -> str:
    """
    Wczytuje plik XML faktury FA(3) i konwertuje do HTML używając szablonu Jinja2.
    
    Args:
        xml_path: Ścieżka do pliku XML faktury
        template_path: Ścieżka do szablonu Jinja2 (opcjonalnie)
    
    Returns:
        str: HTML faktury
    
    Example:
        >>> html = xml_file_to_html('faktura.xml')
        >>> with open('faktura.html', 'w', encoding='utf-8') as f:
        ...     f.write(html)
        
        >>> # Z własnym szablonem
        >>> html = xml_file_to_html('faktura.xml', template_path='custom_fa3.jinja2')
    """
    xml_path = Path(xml_path)
    
    if not xml_path.exists():
        raise FileNotFoundError(f"Plik nie istnieje: {xml_path}")
    
    with open(xml_path, 'r', encoding='utf-8') as f:
        xml_content = f.read()
    
    return xml_to_html(xml_content, template_path)


# ============================================================================
# CLI - tylko jeśli uruchomiony bezpośrednio
# ============================================================================

def main():
    """CLI dla testu modułu."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Konwersja XML faktury KSeF FA(3) do HTML (z szablonami Jinja2)'
    )
    parser.add_argument('xml_file', help='Plik XML faktury FA(3)')
    parser.add_argument('-o', '--output', help='Plik HTML wyjściowy (domyślnie: [nazwa].html)')
    parser.add_argument('-t', '--template', help='Własny szablon Jinja2 (opcjonalnie)')
    parser.add_argument('--kolor', action='store_true', help='Użyj kolorowego szablonu')
    
    args = parser.parse_args()
    
    xml_path = Path(args.xml_file)
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = xml_path.with_suffix('.html')
    
    # Wybierz szablon
    if args.template:
        template_path = Path(args.template)
    elif args.kolor:
        template_path = Path(__file__).parent / 'invoice_template_fa3_kolor.jinja2'
    else:
        template_path = None  # Użyj domyślnego
    
    print(f"[+] Konwertuję FA(3): {xml_path}")
    if template_path:
        print(f"[+] Szablon: {template_path.name}")
    else:
        print(f"[+] Szablon: invoice_template_fa3.jinja2 (domyślny)")
    
    try:
        html = xml_file_to_html(xml_path, template_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"[+] Zapisano HTML: {output_path}")
        print(f"[+] Rozmiar: {len(html)} bajtów")
        
    except Exception as e:
        print(f"[!] BŁĄD: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main())

