#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Konwersja XML faktury FA(3) do HTML z szablonem A4 z kodem QR (KOD I, tryb online).

- JSON/dane faktury pochodzą z ``invoice_xml_parser_FA3.InvoiceXMLParserFA3`` (jak w
  ``invoice_xml_to_html_jinja_FA3``).
- Numer KSeF nie występuje w typowym XML eksportu — należy go podać; przy pracy na plikach
  domyślnie używana jest **nazwa pliku bez rozszerzenia** jako numer KSeF.
- URL weryfikacji (online) i hash budowane są funkcjami z ``ksef_qr_code_generator``;
  rasteryzacja QR do PNG (data URI do ``<img>``) wymaga ``qrcode`` + Pillow.

Czy trzeba „wstrzyknąć” wygenerowany kod QR do słownika danych przed Jinja2?
Tak: szablon oczekuje co najmniej ``ksef_qr_data_uri`` (oraz uzupełnionych ``nr_ksef`` /
``ksef_number`` dla podpisu KSeF). Generator HTML kopiuje słownik do kontekstu Jinja2
(ten sam mechanizm co w ``InvoiceHTMLGeneratorJinjaFA3``).

Przykłady
--------
    from pathlib import Path
    from invoice_xml_to_html_jinja_FA3_with_qr import (
        xml_to_html_with_qr,
        xml_file_to_html_with_qr,
    )

    html = xml_to_html_with_qr(xml_string, "7390202435-20251117-01000085B07B-62")
    html = xml_file_to_html_with_qr(Path("7390202435-20251117-01000085B07B-62.xml"))
"""

from __future__ import annotations

import argparse
import base64
import io
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from invoice_xml_parser_FA3 import InvoiceXMLParserFA3
from invoice_xml_to_html_jinja_FA3 import InvoiceHTMLGeneratorJinjaFA3
from ksef_qr_code_generator import build_invoice_verification_url, compute_invoice_hash_from_bytes

# Fix encoding dla Windows console
if sys.platform == "win32":
    import codecs

    if hasattr(sys.stdout, "buffer"):
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, "strict")
        sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, "strict")


# ============================================================================
# Domyślna ścieżka szablonu
# ============================================================================


def get_default_template_path() -> Path:
    return Path(__file__).parent / "invoice_template_fa3_A4_with_qr.jinja2"


# ============================================================================
# Data P_1 + QR PNG (data URI)
# ============================================================================


def parse_data_wystawienia_to_datetime(data_wystawienia: str) -> datetime:
    """
    Parsuje ``data_wystawienia`` (pole P_1 z parsera) do ``datetime`` (data lokalna, godz. 0:0).
    Obsługiwane typowe formaty: YYYY-MM-DD, DD-MM-RRRR, DD.MM.RRRR.
    """
    raw = (data_wystawienia or "").strip()
    if not raw or raw.upper() == "BRAK":
        raise ValueError("Brak poprawnej daty wystawienia (P_1) w danych faktury")
    if "T" in raw:
        raw = raw.split("T", 1)[0]
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d.%m.%Y"):
        try:
            return datetime.strptime(raw[:10], fmt)
        except ValueError:
            continue
    raise ValueError(f"Nie udało się sparsować daty wystawienia: {data_wystawienia!r}")


def build_verification_url_online(
    xml_bytes: bytes,
    invoice_data: Dict[str, Any],
    ksef_base_url: str,
) -> str:
    """
    KOD I — tryb online: ten sam hash co w dokumentacji (SHA-256, Base64) i URL weryfikacji.
    """
    nip = (
        (invoice_data.get("sprzedawca") or {})
        .get("dane_identyfikacyjne", {})
        .get("nip", "")
    )
    if not (nip and str(nip).strip()):
        raise ValueError("Brak NIP sprzedawcy w danych faktury (wymagany do URL weryfikacji)")
    issue_date = parse_data_wystawienia_to_datetime(invoice_data.get("data_wystawienia", ""))
    invoice_hash = compute_invoice_hash_from_bytes(xml_bytes)
    return build_invoice_verification_url(
        nip=str(nip).strip(),
        issue_date=issue_date,
        invoice_hash_base64=invoice_hash,
        base_url=ksef_base_url,
    )


def verification_url_to_qr_png_data_uri(verification_url: str, box_size: int = 4, border: int = 2) -> str:
    """
    Koduje ``verification_url`` w obraz PNG i zwraca data URI (do ``<img src="...">``).
    Wymaga: ``pip install 'qrcode[pil]'``.
    """
    try:
        import qrcode
    except ImportError as e:
        raise ImportError(
            "Brak biblioteki qrcode. Zainstaluj: pip install 'qrcode[pil]'"
        ) from e

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=border,
    )
    qr.add_data(verification_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    b64 = base64.standard_b64encode(buf.getvalue()).decode("ascii")
    return f"data:image/png;base64,{b64}"


# ============================================================================
# Wzbogacenie danych faktury o KSeF + QR
# ============================================================================


def merge_invoice_data_with_ksef_and_qr(
    invoice_data: Dict[str, Any],
    xml_bytes: bytes,
    ksef_number: str,
    *,
    ksef_base_url: str = "https://ksef-test.mf.gov.pl",
) -> Dict[str, Any]:
    """
    Zwraca nowy słownik: dane faktury + ``nr_ksef``/``ksef_number`` + ``ksef_qr_data_uri`` + ``ksef_qr_url``.

    ``ksef_qr_url`` służy np. do debugowania; szablon A4 *with_qr* używa ``ksef_qr_data_uri``.
    """
    ksef = (ksef_number or "").strip()
    if not ksef:
        raise ValueError("Numer KSeF (ksef_number) jest pusty")

    url = build_verification_url_online(xml_bytes, invoice_data, ksef_base_url)
    data_uri = verification_url_to_qr_png_data_uri(url)

    out: Dict[str, Any] = dict(invoice_data)
    out["nr_ksef"] = ksef
    out["ksef_number"] = ksef
    out["ksef_qr_url"] = url
    out["ksef_qr_data_uri"] = data_uri
    return out


# ============================================================================
# HTML — API publiczne (łańcuchy i pliki)
# ============================================================================


def invoice_data_to_html(
    invoice_data: Dict[str, Any],
    template_path: Optional[Path] = None,
) -> str:
    """
    Generuje HTML z gotowego słownika danych (np. po ``merge_invoice_data_with_ksef_and_qr``).
    """
    t = template_path or get_default_template_path()
    gen = InvoiceHTMLGeneratorJinjaFA3(invoice_data, t)
    return gen.generate()


def xml_to_html_with_qr(
    xml_content: str,
    ksef_number: str,
    *,
    template_path: Optional[Path] = None,
    ksef_base_url: str = "https://ksef-test.mf.gov.pl",
) -> str:
    """
    Parsuje XML z łańcucha, wstrzykuje numer KSeF i dane QR, generuje HTML.

    ``ksef_number`` musi być przekazany explicite (XML sam w sobie go nie niesie).
    """
    xml_bytes = xml_content.encode("utf-8")
    parser = InvoiceXMLParserFA3(xml_content)
    invoice_data = parser.parse()
    merged = merge_invoice_data_with_ksef_and_qr(
        invoice_data, xml_bytes, ksef_number, ksef_base_url=ksef_base_url
    )
    return invoice_data_to_html(merged, template_path)


def xml_file_to_html_with_qr(
    xml_path: Path,
    *,
    ksef_number: Optional[str] = None,
    template_path: Optional[Path] = None,
    ksef_base_url: str = "https://ksef-test.mf.gov.pl",
) -> str:
    """
    Wczytuje plik XML. Numer KSeF: argument ``ksef_number`` lub **nazwa pliku bez rozszerzenia**.

    Hash SHA-256 do URL weryfikacji liczony jest z **surowych bajtów pliku** (jak w KSeF),
    nie z ponownej serializacji tekstu.
    """
    path = Path(xml_path)
    if not path.is_file():
        raise FileNotFoundError(f"Plik nie istnieje: {path}")
    xml_bytes = path.read_bytes()
    try:
        content = xml_bytes.decode("utf-8-sig")
    except UnicodeDecodeError:
        content = xml_bytes.decode("utf-8")
    kn = (ksef_number if ksef_number is not None else path.stem).strip()
    if not kn:
        raise ValueError("Numer KSeF jest pusty (podaj --ksef lub użyj nazwy pliku z numerem KSeF)")
    parser = InvoiceXMLParserFA3(content)
    invoice_data = parser.parse()
    merged = merge_invoice_data_with_ksef_and_qr(
        invoice_data, xml_bytes, kn, ksef_base_url=ksef_base_url
    )
    return invoice_data_to_html(merged, template_path)


# ============================================================================
# CLI
# ============================================================================


def main() -> int:
    ap = argparse.ArgumentParser(
        description="FA(3) XML → HTML (szablon A4 z QR online). Numer KSeF z nazwy pliku lub --ksef."
    )
    ap.add_argument("xml_file", help="Ścieżka do pliku XML faktury FA(3)")
    ap.add_argument("-o", "--output", help="Plik HTML wyjściowy (domyślnie: ta sama nazwa co XML, .html)")
    ap.add_argument(
        "-t",
        "--template",
        help="Szablon Jinja2 (domyślnie: invoice_template_fa3_A4_with_qr.jinja2 obok skryptu)",
    )
    ap.add_argument(
        "--ksef",
        help="Numer KSeF faktury (domyślnie: nazwa pliku XML bez rozszerzenia)",
    )
    ap.add_argument(
        "--base-url",
        default="https://ksef-test.mf.gov.pl",
        help="Bazowy URL KSeF dla linku weryfikacji (domyślnie produkcja)",
    )
    args = ap.parse_args()

    xml_path = Path(args.xml_file)
    out = Path(args.output) if args.output else xml_path.with_suffix(".html")
    template_path = Path(args.template) if args.template else None

    print(f"[+] Wejście: {xml_path}")
    print(f"[+] KSeF: {(args.ksef or xml_path.stem).strip()!r}")
    print(f"[+] Szablon: {template_path or get_default_template_path()}")
    print(f"[+] KSeF base URL: {args.base_url}")

    try:
        html = xml_file_to_html_with_qr(
            xml_path,
            ksef_number=args.ksef,
            template_path=template_path,
            ksef_base_url=args.base_url,
        )
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"[+] Zapisano: {out} ({len(html)} bajtów)")
    except Exception as e:
        print(f"[!] Błąd: {e}", file=sys.stderr)
        import traceback

        traceback.print_exc(file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
