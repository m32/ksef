import base64
import hashlib
from datetime import datetime
import sys
from dateutil.parser import isoparse
from typing import Literal
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa, ec, utils
from pathlib import Path
from ksefcert import Certificate

def base64url_encode(data: bytes) -> str:
    return base64.b64encode(data).decode('ascii').rstrip('=').replace('+', '-').replace('/', '_')

def compute_invoice_hash_from_bytes(invoice_bytes: bytes) -> bytes:
    return hashlib.sha256(invoice_bytes).digest()

def compute_invoice_hash_base64url_from_bytes(data: bytes) -> str:
    hash = compute_invoice_hash_from_bytes(data)
    return base64url_encode(hash)

def get_cert_serial_number_hex(cert) -> str:
    hex_serial = format(cert.serial_number, 'X')  # 'X' dla dużych liter
    # Upewnij się, że długość jest parzysta, wypełniając zerami z przodu jeśli potrzeba
    if len(hex_serial) % 2 != 0:
        hex_serial = '0' + hex_serial
    return hex_serial


def get_seller_nip_and_issue_date_from_invoice_xml_bytes(invoice_bytes: bytes) -> tuple[str, datetime]:

    import xml.etree.ElementTree as ET

    root = ET.fromstring(invoice_bytes)

    # Pobranie namespace z XMLa
    namespace = {'ns': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

    # Pobranie daty z XMLa
    data_wystawienia_elem = root.find('.//ns:Naglowek/ns:DataWytworzeniaFa', namespace) if namespace else root.find('.//Naglowek/DataWytworzeniaFa')
    if data_wystawienia_elem is None:
        raise ValueError("DataWytworzeniaFa element not found in XML")
    data_wystawienia = data_wystawienia_elem.text
    if data_wystawienia is None:
        raise ValueError("DataWytworzeniaFa element has no text content")
    # Obsługa formatu z datą i czasem (ISO 8601)
    #invoice_date = datetime.fromisoformat(data_wystawienia.replace('Z', '+00:00'))
    issue_date = isoparse(data_wystawienia)

    # Pobranie NIP sprzedawcy z XMLa
    nip_elem = root.find('.//ns:Podmiot1/ns:DaneIdentyfikacyjne/ns:NIP', namespace) if namespace else root.find('.//Podmiot1/DaneIdentyfikacyjne/NIP')
    if nip_elem is None:
        raise ValueError("NIP element not found in XML")
    seller_nip = nip_elem.text
    if seller_nip is None:
        raise ValueError("NIP element has no text content")

    return seller_nip, issue_date


def generate_qr_image(url: str, label: str, output_path: str):

    try:
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
        
        # Generuj kod QR
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.ERROR_CORRECT_L,
            box_size=5,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        # Twórz obrazek QR
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Dodaj miejsce na etykietę
        width, height = qr_img.size
        new_height = height + 40  # dodatkowe 40px na etykietę
        
        # Nowy obrazek z miejscem na etykietę
        final_img = Image.new('RGB', (width, new_height), 'white')
        # Konwertuj QR do RGB przed wklejeniem
        final_img.paste(qr_img.convert('RGB'), (0, 0))
        
        # Dodaj tekst etykiety
        draw = ImageDraw.Draw(final_img)
        
        # Spróbuj użyć czcionki systemowej lub domyślnej
        try:
            font = ImageFont.truetype("arial.ttf", 12)
        except:
            font = ImageFont.load_default()
        
        # Wycentruj tekst
        bbox = draw.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (width - text_width) // 2
        text_y = height + 10
        
        draw.text((text_x, text_y), label, fill='black', font=font)
        
        # Zapisz
        final_img.save(output_path)
        print(f"✅ Kod QR zapisany: {output_path}")
        
    except ImportError:
        print("⚠️  Aby generować obrazki QR, zainstaluj: pip install qrcode[pil]")
        print(f"📝 URL do ręcznego wygenerowania QR: {url}")

def build_invoice_verification_url(
    nip: str,
    issue_date: datetime,
    invoice_hash_base64url: str,
    base_url: str = "https://qr-test.ksef.mf.gov.pl"
) -> str:
    """
    Buduje URL do weryfikacji faktury (KOD I).
    
    Ten kod QR służy do:
    - Weryfikacji faktury w systemie KSeF
    - Pobrania faktury w formacie XML
    
    Format URL:
    {base_url}/invoice/{nip}/{data_DD-MM-RRRR}/{hash_base64url}
    
    Args:
        nip: NIP sprzedawcy (10 cyfr)
        issue_date: Data wystawienia faktury (pole P_1)
        invoice_hash_base64: Hash SHA-256 faktury w formacie Base64 (standardowy)
        base_url: Bazowy URL QR KSeF (domyślnie środowisko testowe)
        
    Returns:
        Pełny URL do weryfikacji faktury
        
    Example:
        >>> build_invoice_verification_url(
        ...     nip="1111111111",
        ...     issue_date=datetime(2026, 2, 1),
        ...     invoice_hash_base64="UtQp9Gpc51y+u3xApZjIjgkpZ01js+J8KflSPW8WzIE="
        ... )
        'https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE'
    """
    # # Konwertuj hash z Base64 do Base64URL
    # hash_bytes = base64.b64decode(invoice_hash_base64)
    # hash_base64url = base64url_encode(hash_bytes)
    
    # Format daty: DD-MM-RRRR
    date_str = issue_date.strftime("%d-%m-%Y")
    
    return f"{base_url}/invoice/{nip}/{date_str}/{invoice_hash_base64url}"


def get_offline_cert_path_sign_proc(private_key, ecdsa_sign_format: Literal['ieee_p1363','der'] = 'ieee_p1363'):
    
    def signproc(tosign):

        if isinstance(private_key, rsa.RSAPrivateKey):
            signature = private_key.sign(
                tosign,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=32
                ),
                hashes.SHA256(),
            )
        else:
            signature = private_key.sign(
                tosign,
                ec.ECDSA(hashes.SHA256())
            )

            if ecdsa_sign_format == 'ieee_p1363':

                ###v1
                # from asn1crypto import core
                # length =  (private_key.curve.key_size + 7) // 8 #oryginalnie z m32/ksef: 32 #=256/8 czyli aes-256 TODO zamienić na zmienną zależną od długości klucza
                # d = core.load(signature)
                # dr = d[0].native.to_bytes(length, byteorder="big")
                # ds = d[1].native.to_bytes(length, byteorder="big")
                # signature = dr+ds
                ###end v1

                ####v2
                from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
                r, s = decode_dss_signature(signature)
                # Konwertuj r i s do big-endian (dla P-256 to 32 bajty każdy)
                field_size_bytes = (private_key.curve.key_size + 7) // 8
                r_bytes = r.to_bytes(field_size_bytes, byteorder='big')
                s_bytes = s.to_bytes(field_size_bytes, byteorder='big')
                
                signature = r_bytes + s_bytes   
                ####end v2     


        return signature


    return signproc     


def build_certificate_verification_url(
    seller_nip: str,
    context_identifier_type: Literal['Nip', 'InternalId', 'NipVatUe', 'PeppolId'],
    context_identifier_value: str,
    certificate_serial: str,
    invoice_hash_base64url: str,
    private_key,  # Union[rsa.RSAPrivateKey, ec.EllipticCurvePrivateKey]
    base_url: str = "https://qr-test.ksef.mf.gov.pl",
    ecdsa_signature_format: Literal['ieee_p1363', 'der'] = 'ieee_p1363'
) -> str:
    """
    Buduje URL do weryfikacji certyfikatu KSeF (KOD II).
    
    Ten kod QR służy do potwierdzenia autentyczności wystawcy faktury offline.
    
    Format URL:
    {base_url}/certificate/{typ_id}/{wartość_id}/{nip_sprzedawcy}/{serial_cert}/{hash_base64url}/{podpis_base64url}
    
    Args:
        seller_nip: NIP sprzedawcy (10 cyfr)
        context_identifier_type: Typ identyfikatora kontekstu logowania ('Nip', 'InternalId', 'NipVatUe', 'PeppolId')
        context_identifier_value: Wartość identyfikatora kontekstu logowania - kto (jaka firma/Nip) wystawia w imieniu sprzedawcy, w ramach jakiego kontekstu (firmy / na "koncie" której firmy) jest wystawiony certyfikat offline, nawet jeśli wystawiony jest na PESEL, może być inny niż sprzedawca jeśli np. firma tutaj wskazana ma prawo wystawiać faktury w imieniu sprzedawcy
        certificate_serial: Numer seryjny certyfikatu KSeF (hex uppercase, parzysta liczba znaków) - certyfikat offline (do podpisywania linku weryfikacyjnego wystawcę), nie ważne czy wystawiony na NIP czy PESEL, ważne aby był w ramach (w kontekście/ na koncie) firmy/NIPu context_identifier_value 
        invoice_hash_base64: Hash SHA-256 faktury w formacie Base64 (standardowy)
        private_key: Klucz prywatny RSA lub ECDSA związany z certyfikatem offline
        base_url: Bazowy URL QR KSeF (domyślnie środowisko testowe)
        ecdsa_signature_format: Format podpisu ECDSA ('ieee_p1363' lub 'der')
        
    Returns:
        Pełny URL do weryfikacji certyfikatu
        
    Example:
        >>> # Przykład z RSA
        >>> build_certificate_verification_url(
        ...     seller_nip="1111111111",
        ...     context_identifier_type="Nip",
        ...     context_identifier_value="1111111111",
        ...     certificate_serial="01F20A5D352AE590",
        ...     invoice_hash_base64="UtQp9Gpc51y+u3xApZjIjgkpZ01js+J8KflSPW8WzIE=",
        ...     private_key=rsa_private_key
        ... )

    Dodatkowe objaśnienia dla seller_nip, context_identifier_type, context_identifier_value:
        - seller_nip: NIP sprzedawcy, na którego wystawiana jest faktura.
        - context_identifier_type: Typ identyfikatora kontekstu logowania, określa jakiego typu identyfikator jest używany do określenia "konta" lub "firmy", w ramach której wygenerowany jest certyfikat offline.
        - context_identifier_value: Wartość identyfikatora kontekstu logowania, określa konkretną firmę lub konto (np. NIP firmy), w ramach którego certyfikat offline jest ważny. Może to być inny NIP niż seller_nip, jeśli sam certyfikat offline jest wygenerowany w kontekście (w ramach konta) innej firmy wystawiającej faktury w imieniu sprzedawcy (nie ważne czy certyfikat jest na PESEL czy NIP).

        Przykład 1 - certyfikat wygenerowany w kontekście (na koncie) NIP "1111111111" będąc zalogowanym NIPem "1111111111" (certyfikat "zawierający" NIP), wystawca faktury to też NIP "1111111111"):
        - seller_nip: "1111111111" (NIP sprzedawcy)
        - context_identifier_type: "Nip"
        - context_identifier_value: "1111111111" (NIP konta/firmy, w ramach którego wygenerowano certyfikat offline)

        Przykład 2 - certyfikat wygenerowany w kontekście (na koncie) NIP "1111111111" będąc zalogowanym PESELem "22222222222" (certyfikat "zawierający" PESEL), wystawca faktury to też NIP "1111111111"):
        - seller_nip: "1111111111" (NIP sprzedawcy)
        - context_identifier_type: "Nip"
        - context_identifier_value: "1111111111" (NIP konta/firmy, w ramach którego wygenerowano certyfikat offline)

        Przykład 3 - certyfikat wygenerowany w kontekście (na koncie) NIP "3333333333" (firma trzecia, która ma prawo wystawiać faktury w imieniu firmy "1111111111") będąc zalogowanym PESELem lub NIPem (bez znaczenia), wystawca faktury to NIP "1111111111"):
        - seller_nip: "1111111111" (NIP sprzedawcy)
        - context_identifier_type: "Nip"
        - context_identifier_value: "3333333333" (NIP konta/firmy, w ramach którego wygenerowano certyfikat offline)

        Czyli nie ma znaczenia czy certyfikat został wygenerowany na PESEL czy NIP (czy w momencie generowania byliśmy zalogowani PESELem czy NIPem), ważne jest aby context_identifier_value wskazywał na firmę/NIP, w ramach której wygenerowano certyfikat offline, a ta firma/NIP jest wystawcą faktury lub ma prawo wystawiać faktury w imieniu sprzedawcy (seller_nip).
        W przypadku certyfikatów na PESEL w ramach konta sprzedawcy (przypadek bez trzeciej firmy) ważne są uprawnienia nadane temu PESELowi.
    """
    # # Konwertuj hash z Base64 do Base64URL
    # hash_bytes = base64.b64decode(invoice_hash_base64)
    # hash_base64url = base64url_encode(hash_bytes)
    
    # Buduj ścieżkę do podpisania (bez https:// i bez końcowego /)
    path_without_signature = (
        f"{base_url}/certificate/"
        f"{context_identifier_type}/{context_identifier_value}/"
        f"{seller_nip}/{certificate_serial}/{invoice_hash_base64url}"
    )
    
    # Usuń https://
    path_to_sign = path_without_signature.replace("https://", "")
    
    # Podpisz ścieżkę odpowiednim algorytmem

    # public_key = certificate.public_key()
    
    # if isinstance(public_key, rsa.RSAPublicKey):
    #     signature = sign_path_rsa(path_to_sign, private_key)
    # elif isinstance(public_key, ec.EllipticCurvePublicKey):
    #     signature = sign_path_ecdsa(path_to_sign, private_key, ecdsa_signature_format)
    # else:
    #     raise ValueError("Certyfikat musi używać RSA lub ECDSA")


    sign_proc = get_offline_cert_path_sign_proc(private_key, ecdsa_signature_format)
    signature = sign_proc(path_to_sign.encode('utf-8'))
    
    # Koduj podpis w Base64URL
    signature_base64url = base64url_encode(signature)
    
    return f"{path_without_signature}/{signature_base64url}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python3 qr_codes_generator.py [plik_xml_faktury] [numer_faktury_ksef] [plik_klucza_prywatnego_offline] [haslo_klucza_prywatnego_offline] [plik_certyfikatu_offline] [NIP_kontekstu_logowania_certyfikatu_offline]")
        print(
            "Przykład: python3 qr_codes_generator.py fa.xml 7390100344-20251121-010000779857-C4 offline_key.key tajne_haslo offline_cert.crt 1111111111"
        )
        sys.exit(1)

    from ksefconfig import Config
    cfg = Config(1) #(int(sys.argv[1]))  #na tym etapie tylko urla potrzebuję, więc bez znaczenia numer
    
    invoice_xml_path = sys.argv[1]
    invoice_ksef_number = sys.argv[2]
    offline_key_path = sys.argv[3]
    offline_key_password = sys.argv[4]
    offline_cert_path = sys.argv[5]
    context_nip = sys.argv[6]

    certicate = Certificate()
    offline_private_key = certicate.key_load(offline_key_path, offline_key_password)
    offline_certificate = certicate.cert_load(offline_cert_path)

    with open(invoice_xml_path, "rb") as f:
        invoice_xml_bytes = f.read()

    seller_nip, issue_date = get_seller_nip_and_issue_date_from_invoice_xml_bytes(invoice_xml_bytes)

    invoice_hash_base64url = compute_invoice_hash_base64url_from_bytes(invoice_xml_bytes)

    from pathlib import Path
    script_dir = Path(__file__).parent
    xml_file_path = Path(invoice_xml_path)

    base_url = cfg.url.replace("api", "qr")

    url = build_invoice_verification_url(
        nip=seller_nip,
        issue_date=issue_date,
        invoice_hash_base64url=invoice_hash_base64url,
        base_url=cfg.url
    )

    generate_qr_image(
        url=url,
        label="OFFLINE",
        output_path=script_dir / f'{xml_file_path.name}_offline.png'
    )

    generate_qr_image(
        url=url,
        label=invoice_ksef_number,
        output_path=script_dir / f'{xml_file_path.name}_ksef.png'
    )
    
    cert_serial_number = get_cert_serial_number_hex(offline_certificate)
    #albo stała (z parametru) bo tylko po to jest certyfikat offline potrzebny (powiązany klucz prywatny oczyście niezbędny):
    #cert_serial_number = config_manager_instance.offline_certificate_serial_number

    certyfikat_url = build_certificate_verification_url(
        seller_nip=seller_nip,
        context_identifier_type="Nip",
        context_identifier_value=context_nip,#NIP działającego w imieniu sprzedawcy, "właściciel" certyfikatu offline, jeśli certyfikat przygotowany na koncie sprzedawcy to NIP jest taki sam jak sprzedawcy
        certificate_serial=cert_serial_number,
        invoice_hash_base64url=invoice_hash_base64url,
        private_key=offline_private_key,  # Union[rsa.RSAPrivateKey, ec.EllipticCurvePrivateKey]
        base_url=cfg.url,
        ecdsa_signature_format= 'ieee_p1363'  #może być 'der' albo 'ieee_p1363'
        )
    
    generate_qr_image(
        url=certyfikat_url,
        label="CERTYFIKAT",
        output_path=script_dir / f'{xml_file_path.name}_certyfikat.png'
    )