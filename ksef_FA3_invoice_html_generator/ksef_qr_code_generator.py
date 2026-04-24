"""
Moduł do generowania URL-i dla kodów QR w systemie KSeF.

Obsługuje:
- KOD I: Weryfikacja faktury (tryb online i offline)
- KOD II: Weryfikacja certyfikatu (tylko tryb offline)

Zgodnie z dokumentacją:
https://github.com/CIRFMF/ksef-docs/blob/main/kody-qr.md
"""

import base64
import hashlib
from datetime import datetime
from typing import Literal, Optional
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec, padding
from cryptography import x509


def base64url_encode(data: bytes) -> str:
    """
    Koduje dane w formacie Base64URL (RFC 4648 §5).
    
    Base64URL to Base64 z zamianą znaków i bez paddingu:
    - '+' -> '-'
    - '/' -> '_'
    - usuwa '=' (padding)
    
    Args:
        data: Bajty do zakodowania
        
    Returns:
        Zakodowany string w formacie Base64URL
    """
    return base64.b64encode(data).decode('ascii').rstrip('=').replace('+', '-').replace('/', '_')


def format_certificate_serial(serial_number: int) -> str:
    """
    Formatuje numer seryjny certyfikatu dla KSeF.
    
    Numer seryjny musi być w formacie hex uppercase z parzystą liczbą znaków.
    Jeśli numer ma nieparzystą liczbę cyfr, dodaje wiodące zero.
    
    Args:
        serial_number: Numer seryjny certyfikatu jako liczba całkowita
        
    Returns:
        Sformatowany numer seryjny (hex uppercase, parzysta liczba znaków)
        
    Example:
        >>> format_certificate_serial(0x10B07D0CBD18056)
        '010B07D0CBD18056'
        >>> format_certificate_serial(0x1F20A5D352AE590)
        '01F20A5D352AE590'
    """
    serial_hex = format(serial_number, 'X')
    # Dodaj wiodące zero jeśli liczba znaków jest nieparzysta
    if len(serial_hex) % 2 != 0:
        serial_hex = '0' + serial_hex
    return serial_hex


def compute_invoice_hash(invoice_xml_path: str) -> str:
    """
    Oblicza hash SHA-256 z pliku faktury XML.
    
    Args:
        invoice_xml_path: Ścieżka do pliku XML z fakturą
        
    Returns:
        Hash SHA-256 zakodowany w Base64 (standardowy, nie URL)
    """
    with open(invoice_xml_path, 'rb') as f:
        invoice_bytes = f.read()
    
    sha256_hash = hashlib.sha256(invoice_bytes).digest()
    return base64.b64encode(sha256_hash).decode('ascii')


def compute_invoice_hash_from_bytes(invoice_bytes: bytes) -> str:
    """
    Oblicza hash SHA-256 z zawartości faktury.
    
    Args:
        invoice_bytes: Zawartość faktury jako bajty
        
    Returns:
        Hash SHA-256 zakodowany w Base64 (standardowy, nie URL)
    """
    sha256_hash = hashlib.sha256(invoice_bytes).digest()
    return base64.b64encode(sha256_hash).decode('ascii')


def build_invoice_verification_url(
    nip: str,
    issue_date: datetime,
    invoice_hash_base64: str,
    base_url: str = "https://ksef-test.mf.gov.pl"
) -> str:
    """
    Buduje URL do weryfikacji faktury (KOD I).
    
    Ten kod QR służy do:
    - Weryfikacji faktury w systemie KSeF
    - Pobrania faktury w formacie XML
    
    Format URL:
    {base_url}/client-app/invoice/{nip}/{data_DD-MM-RRRR}/{hash_base64url}
    
    Args:
        nip: NIP sprzedawcy (10 cyfr)
        issue_date: Data wystawienia faktury (pole P_1)
        invoice_hash_base64: Hash SHA-256 faktury w formacie Base64 (standardowy)
        base_url: Bazowy URL KSeF (domyślnie środowisko testowe)
        
    Returns:
        Pełny URL do weryfikacji faktury
        
    Example:
        >>> build_invoice_verification_url(
        ...     nip="1111111111",
        ...     issue_date=datetime(2026, 2, 1),
        ...     invoice_hash_base64="UtQp9Gpc51y+u3xApZjIjgkpZ01js+J8KflSPW8WzIE="
        ... )
        'https://ksef-test.mf.gov.pl/client-app/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE'
    """
    # Konwertuj hash z Base64 do Base64URL
    hash_bytes = base64.b64decode(invoice_hash_base64)
    hash_base64url = base64url_encode(hash_bytes)
    
    # Format daty: DD-MM-RRRR
    date_str = issue_date.strftime("%d-%m-%Y")
    
    return f"{base_url}/client-app/invoice/{nip}/{date_str}/{hash_base64url}"


def sign_path_rsa(
    path_to_sign: str,
    private_key: rsa.RSAPrivateKey
) -> bytes:
    """
    Podpisuje ścieżkę URL kluczem prywatnym RSA (RSASSA-PSS).
    
    Parametry podpisu:
    - Funkcja skrótu: SHA-256
    - MGF: MGF1 z SHA-256
    - Długość soli: 32 bajty
    
    Args:
        path_to_sign: Ścieżka URL do podpisania (bez https:// i końcowego /)
        private_key: Klucz prywatny RSA (minimum 2048 bitów)
        
    Returns:
        Podpis jako bajty
    """
    # Konwertuj tekst na bajty
    # UWAGA: hashes.SHA256() w sign() SAM haszuje dane
    data = path_to_sign.encode('utf-8')
    
    # Podpisz dane używając RSASSA-PSS
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=32
        ),
        hashes.SHA256()
    )
    
    return signature


def sign_path_ecdsa(
    path_to_sign: str,
    private_key: ec.EllipticCurvePrivateKey,
    signature_format: Literal['ieee_p1363', 'der'] = 'ieee_p1363'
) -> bytes:
    """
    Podpisuje ścieżkę URL kluczem prywatnym ECDSA (P-256/SHA-256).
    
    Args:
        path_to_sign: Ścieżka URL do podpisania (bez https:// i końcowego /)
        private_key: Klucz prywatny ECDSA (krzywa P-256/secp256r1)
        signature_format: Format podpisu:
            - 'ieee_p1363' (rekomendowany): R || S (po 32 bajty big-endian)
            - 'der': ASN.1 DER SEQUENCE (RFC 3279)
        
    Returns:
        Podpis jako bajty
    """
    # Konwertuj tekst na bajty
    # UWAGA: ec.ECDSA(hashes.SHA256()) SAM haszuje dane algorytmem SHA-256
    data = path_to_sign.encode('utf-8')
    
    # Podpisz dane
    if signature_format == 'ieee_p1363':
        # IEEE P1363 Fixed Field Concatenation (rekomendowany)
        from cryptography.hazmat.primitives.asymmetric.utils import decode_dss_signature
        
        # ECDSA zwraca podpis w formacie DER, więc musimy go przekonwertować
        signature_der = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        r, s = decode_dss_signature(signature_der)
        
        # Konwertuj r i s do big-endian (dla P-256 to 32 bajty każdy)
        field_size_bytes = (private_key.curve.key_size + 7) // 8
        r_bytes = r.to_bytes(field_size_bytes, byteorder='big')
        s_bytes = s.to_bytes(field_size_bytes, byteorder='big')
        
        return r_bytes + s_bytes
    else:  # 'der'
        # ASN.1 DER SEQUENCE
        return private_key.sign(data, ec.ECDSA(hashes.SHA256()))


def build_certificate_verification_url(
    seller_nip: str,
    context_identifier_type: Literal['Nip', 'Pesel', 'Other'],
    context_identifier_value: str,
    certificate_serial: str,
    invoice_hash_base64: str,
    private_key,  # Union[rsa.RSAPrivateKey, ec.EllipticCurvePrivateKey]
    base_url: str = "https://ksef-test.mf.gov.pl",
    ecdsa_signature_format: Literal['ieee_p1363', 'der'] = 'ieee_p1363'
) -> str:
    """
    Buduje URL do weryfikacji certyfikatu KSeF (KOD II).
    
    Ten kod QR służy do potwierdzenia autentyczności wystawcy faktury offline.
    
    Format URL:
    {base_url}/client-app/certificate/{typ_id}/{wartość_id}/{nip_sprzedawcy}/{serial_cert}/{hash_base64url}/{podpis_base64url}
    
    Args:
        seller_nip: NIP sprzedawcy (10 cyfr)
        context_identifier_type: Typ identyfikatora kontekstu ('Nip', 'Pesel', 'Other')
        context_identifier_value: Wartość identyfikatora kontekstu
        certificate_serial: Numer seryjny certyfikatu KSeF (hex uppercase, parzysta liczba znaków)
                            Użyj format_certificate_serial() do poprawnego formatowania
        invoice_hash_base64: Hash SHA-256 faktury w formacie Base64 (standardowy)
        private_key: Klucz prywatny RSA lub ECDSA (typ określa algorytm podpisu)
        base_url: Bazowy URL KSeF (domyślnie środowisko testowe)
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
    """
    # Konwertuj hash z Base64 do Base64URL
    hash_bytes = base64.b64decode(invoice_hash_base64)
    hash_base64url = base64url_encode(hash_bytes)
    
    # Buduj ścieżkę do podpisania (bez https:// i bez końcowego /)
    path_without_signature = (
        f"{base_url}/client-app/certificate/"
        f"{context_identifier_type}/{context_identifier_value}/"
        f"{seller_nip}/{certificate_serial}/{hash_base64url}"
    )
    
    # Usuń https://
    path_to_sign = path_without_signature.replace("https://", "")
    
    # Podpisz ścieżkę odpowiednim algorytmem (określamy na podstawie typu klucza prywatnego)
    if isinstance(private_key, rsa.RSAPrivateKey):
        signature = sign_path_rsa(path_to_sign, private_key)
    elif isinstance(private_key, ec.EllipticCurvePrivateKey):
        signature = sign_path_ecdsa(path_to_sign, private_key, ecdsa_signature_format)
    else:
        raise ValueError(f"Nieobsługiwany typ klucza prywatnego: {type(private_key).__name__}")
    
    # Koduj podpis w Base64URL
    signature_base64url = base64url_encode(signature)
    
    return f"{path_without_signature}/{signature_base64url}"


def load_private_key_from_pem(pem_path: str, password: Optional[bytes] = None):
    """
    Wczytuje klucz prywatny z pliku PEM.
    
    Args:
        pem_path: Ścieżka do pliku PEM z kluczem prywatnym
        password: Opcjonalne hasło do klucza (jeśli jest zaszyfrowany)
        
    Returns:
        Klucz prywatny RSA lub ECDSA
    """
    with open(pem_path, 'rb') as f:
        pem_data = f.read()
    
    return serialization.load_pem_private_key(pem_data, password=password)


def load_certificate_from_pem(pem_path: str) -> x509.Certificate:
    """
    Wczytuje certyfikat z pliku PEM.
    
    Args:
        pem_path: Ścieżka do pliku PEM z certyfikatem
        
    Returns:
        Certyfikat X.509
    """
    with open(pem_path, 'rb') as f:
        pem_data = f.read()
    
    return x509.load_pem_x509_certificate(pem_data)


def load_certificate_from_base64(cert_base64: str) -> x509.Certificate:
    """
    Wczytuje certyfikat z Base64 (DER).
    
    Args:
        cert_base64: Certyfikat w formacie Base64
        
    Returns:
        Certyfikat X.509
    """
    cert_der = base64.b64decode(cert_base64)
    return x509.load_der_x509_certificate(cert_der)


if __name__ == "__main__":
    # Przykład użycia - KOD I
    print("=== Przykład KOD I - Weryfikacja faktury ===")
    
    # Załóżmy, że mamy hash faktury
    invoice_hash = "UtQp9Gpc51y+u3xApZjIjgkpZ01js+J8KflSPW8WzIE="
    
    url_online = build_invoice_verification_url(
        nip="1111111111",
        issue_date=datetime(2026, 2, 1),
        invoice_hash_base64=invoice_hash
    )
    
    print(f"URL dla KOD I (online): {url_online}")
    print(f"Etykieta pod kodem QR: [numer KSeF] lub 'OFFLINE'")
    print()
    
    print("=== Przykład obliczania hasha z pliku ===")
    print("# invoice_hash = compute_invoice_hash('faktura.xml')")
    print("# url = build_invoice_verification_url('1111111111', datetime.now(), invoice_hash)")

