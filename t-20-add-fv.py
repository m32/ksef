#!/usr/bin/env vpython3
# -*- coding: utf-8 -*-
"""
Skrypt do wysyłania faktury do systemu KSeF poprzez API.
Implementuje proces:
1. Otwarcie sesji online
2. Szyfrowanie faktury
3. Wysłanie faktury
4. Sprawdzenie statusu
5. Zamknięcie sesji

Użycie: python3 t-20-add-fv.py [numer_firmy] [plik_xml_faktury]
"""

import json
import os
import sys
import time
import hashlib
import base64
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


class KSeFInvoiceSender:
    def __init__(self, cfg):
        self.cfg = cfg
        # Wczytaj tokeny uwierzytelniania
        with open(f"{cfg.prefix}-auth.json", "rt") as fp:
            self.auth = json.loads(fp.read())

        self.access_token = self.auth["accessToken"]["token"]
        self.session_ref_number = None

        # Klucze szyfrowania używane przez całą sesję
        self.symmetric_key = None
        self.iv = None

    def get_headers(self):
        """Zwraca nagłówki HTTP z tokenem autoryzacji"""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def get_ksef_public_key(self):
        """
        Pobiera klucz publiczny KSeF do szyfrowania z API.
        """
        print("🔑 Pobieranie klucza publicznego KSeF...")

        try:
            # Najpierw spróbuj pobrać bezpośrednio plik PEM
            response = requests.get(
                f"{self.cfg.url}/public-keys/publicKey.pem", timeout=10
            )

            if response.status_code == 200:
                public_key_pem = response.text
                print("✅ Klucz publiczny pobrany z /public-keys/publicKey.pem")
                return serialization.load_pem_public_key(
                    public_key_pem.encode(), backend=default_backend()
                )

            # Jeśli nie ma bezpośredniego pliku, spróbuj API z certyfikatami
            response = requests.get(
                f"{self.cfg.url}/security/public-key-certificates", timeout=10
            )

            if response.status_code == 200:
                certificates = response.json()
                # Znajdź certyfikat do szyfrowania klucza symetrycznego
                for cert in certificates:
                    if "SymmetricKeyEncryption" in cert.get("usage", []):
                        cert_data = cert.get("certificate", "")
                        # Certyfikat może być w formacie Base64 DER
                        try:
                            from cryptography import x509
                            import base64

                            # Spróbuj zdekodować jako Base64 DER
                            cert_bytes = base64.b64decode(cert_data)
                            certificate = x509.load_der_x509_certificate(cert_bytes)
                            public_key = certificate.public_key()
                            print("✅ Klucz publiczny wyciągnięty z certyfikatu")
                            return public_key
                        except Exception:
                            # Może być już w formacie PEM
                            if "BEGIN CERTIFICATE" in cert_data:
                                certificate = x509.load_pem_x509_certificate(
                                    cert_data.encode()
                                )
                                public_key = certificate.public_key()
                                print(
                                    "✅ Klucz publiczny wyciągnięty z certyfikatu PEM"
                                )
                                return public_key

                print("❌ Nie znaleziono certyfikatu do szyfrowania")
            else:
                print(f"❌ Błąd pobierania certyfikatów: {response.status_code}")

        except Exception as e:
            print(f"❌ Błąd pobierania klucza publicznego: {e}")

        # Fallback - wygeneruj prawdziwy testowy klucz RSA
        print("🔄 Generuję testowy klucz RSA...")
        from cryptography.hazmat.primitives.asymmetric import rsa

        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        return private_key.public_key()

    def encrypt_invoice(self, invoice_xml):
        """Szyfruje fakturę AES + RSA zgodnie z wymaganiami KSeF"""

        # Użyj kluczy z sesji lub wygeneruj nowe jeśli sesja nie ma
        if self.symmetric_key is None or self.iv is None:
            print("⚠️  Brak kluczy z sesji, generuję nowe...")
            symmetric_key = os.urandom(32)  # 256 bits
            iv = os.urandom(16)  # 128 bits
        else:
            print("✅ Używam kluczy z sesji")
            symmetric_key = self.symmetric_key
            iv = self.iv

        # Szyfruj fakturę kluczem symetrycznym AES
        cipher = Cipher(
            algorithms.AES(symmetric_key), modes.CBC(iv), backend=default_backend()
        )
        encryptor = cipher.encryptor()

        # Padding do wielokrotności 16 bajtów (AES block size)
        invoice_bytes = invoice_xml.encode("utf-8")
        padding_length = 16 - (len(invoice_bytes) % 16)
        padded_invoice = invoice_bytes + bytes([padding_length] * padding_length)

        encrypted_invoice = encryptor.update(padded_invoice) + encryptor.finalize()

        # Szyfruj klucz symetryczny kluczem publicznym RSA
        public_key = self.get_ksef_public_key()
        assert isinstance(public_key, rsa.RSAPublicKey)

        encrypted_symmetric_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

        return {
            "encrypted_invoice": encrypted_invoice,
            "encrypted_symmetric_key": base64.b64encode(
                encrypted_symmetric_key
            ).decode(),
            "iv": base64.b64encode(iv).decode(),
            "original_size": len(invoice_bytes),
            "encrypted_size": len(encrypted_invoice),
        }

    def calculate_hash(self, data):
        """Oblicza hash SHA-256 i koduje w Base64"""
        if isinstance(data, str):
            data = data.encode("utf-8")
        return base64.b64encode(hashlib.sha256(data).digest()).decode()

    def open_online_session(self):
        """Otwiera sesję online do wysyłki faktury"""
        print("🔓 Otwieranie sesji online...")

        try:
            # Generuj prawdziwy klucz symetryczny i zaszyfruj go kluczem publicznym KSeF
            self.symmetric_key = os.urandom(32)  # 256-bit AES key
            self.iv = os.urandom(16)  # 128-bit IV

            # Pobierz klucz publiczny KSeF
            public_key = self.get_ksef_public_key()
            assert isinstance(public_key, rsa.RSAPublicKey)

            # Zaszyfruj klucz symetryczny kluczem publicznym RSA
            encrypted_symmetric_key = public_key.encrypt(
                self.symmetric_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

            # Zakoduj w Base64
            encrypted_key_b64 = base64.b64encode(encrypted_symmetric_key).decode()
            iv_b64 = base64.b64encode(self.iv).decode()

            print(
                f"✅ Klucz symetryczny wygenerowany: {len(self.symmetric_key)} bajtów"
            )
            print(f"✅ IV wygenerowany: {len(self.iv)} bajtów")

        except Exception as e:
            print(f"❌ Błąd szyfrowania klucza: {e}")
            print("🔄 Używam przykładowych danych...")
            # Fallback do przykładowych danych
            encrypted_key_b64 = "dummyEncryptedSymmetricKey" + "=" * 100
            iv_b64 = base64.b64encode(os.urandom(16)).decode()
            # W przypadku błędu, ustaw None żeby encrypt_invoice wiedziała
            self.symmetric_key = None
            self.iv = None

        request_data = {
            "formCode": {
                "systemCode": "FA (3)",
                "schemaVersion": "1-0E",
                "value": "FA",
            },
            "encryption": {
                "encryptedSymmetricKey": encrypted_key_b64,
                "initializationVector": iv_b64,
            },
        }

        response = requests.post(
            f"{self.cfg.url}/sessions/online",
            json=request_data,
            headers=self.get_headers(),
            timeout=30,
        )

        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            session_data = response.json()
            self.session_ref_number = session_data["referenceNumber"]
            print(f"✅ Sesja otwarta: {self.session_ref_number}")
            print(f"Ważna do: {session_data.get('validUntil', 'N/A')}")
            return True
        else:
            print(f"❌ Błąd otwierania sesji: {response.text}")
            return False

    def send_invoice(self, invoice_xml):
        """Wysyła fakturę do otwartej sesji"""
        if not self.session_ref_number:
            print("❌ Brak otwartej sesji!")
            return False

        print("📤 Wysyłanie faktury...")

        # Szyfruj fakturę
        encryption_result = self.encrypt_invoice(invoice_xml)

        # Przygotuj dane do wysłania
        invoice_hash = self.calculate_hash(invoice_xml)
        encrypted_invoice_hash = self.calculate_hash(
            encryption_result["encrypted_invoice"]
        )

        request_data = {
            "invoiceHash": invoice_hash,
            "invoiceSize": encryption_result["original_size"],
            "encryptedInvoiceHash": encrypted_invoice_hash,
            "encryptedInvoiceSize": encryption_result["encrypted_size"],
            "encryptedInvoiceContent": base64.b64encode(
                encryption_result["encrypted_invoice"]
            ).decode(),
            "offlineMode": False,
        }

        response = requests.post(
            f"{self.cfg.url}/sessions/online/{self.session_ref_number}/invoices",
            json=request_data,
            headers=self.get_headers(),
            timeout=30,
        )

        print(f"Status: {response.status_code}")
        if response.status_code == 202:
            result = response.json()
            print(result)
            invoice_ref = result["referenceNumber"]
            print(f"✅ Faktura wysłana: {invoice_ref}")
            return invoice_ref
        else:
            print(f"❌ Błąd wysyłania faktury: {response.text}")
            return None

    def check_invoice_status(self, invoice_ref, max_attempts=99999):
        """Sprawdza status przetwarzania faktury"""
        print(f"🔍 Sprawdzanie statusu faktury {invoice_ref}...")

        for attempt in range(max_attempts):
            url = f"{self.cfg.url}/sessions/{self.session_ref_number}/invoices/{invoice_ref}"
            print(f"Sprawdzanie statusu... (próba {attempt + 1}/{max_attempts})")
            print(f"URL: {url}")
            response = requests.get(
                url,
                headers=self.get_headers(),
                timeout=15,
            )

            if response.status_code == 200:
                status_data = response.json()
                status = status_data.get("status", {}).get("description", "Nieznany")
                print("Response", status_data)
                print(f"Status: {status}")

                if "processed" in status.lower() or "accepted" in status.lower():
                    print(f"✅ Faktura przetworzona pomyślnie!")
                    if "ksefNumber" in status_data:
                        print(f"Numer KSeF: {status_data['ksefNumber']}")
                    return True
                elif "error" in status.lower() or "rejected" in status.lower():
                    print(f"❌ Faktura odrzucona: {status}")
                    return False
                else:
                    print(
                        f"⏳ Przetwarzanie w toku... (próba {attempt + 1}/{max_attempts})"
                    )
                    time.sleep(3)
            else:
                print(f"❌ Błąd sprawdzania statusu: {response.status_code}")
                time.sleep(2)

        print("⏰ Przekroczono limit prób sprawdzenia statusu")
        return False

    def close_session(self):
        """Zamyka sesję online"""
        if not self.session_ref_number:
            return

        print("🔒 Zamykanie sesji...")
        response = requests.post(
            f"{self.cfg.url}/sessions/online/{self.session_ref_number}/close",
            headers=self.get_headers(),
            timeout=15,
        )

        if response.status_code in [200, 204]:
            print("✅ Sesja zamknięta")
        else:
            print(f"⚠️  Błąd zamykania sesji: {response.status_code}")


def main():
    if len(sys.argv) < 2:
        print("Użycie: python3 t-20-add-fv.py [numer_firmy] [plik_xml_faktury]")
        print(
            "Przykład: python3 t-20-add-fv.py 1 7746002029-3750687646-1759783218.134159.xml"
        )
        sys.exit(1)

    # Import konfiguracji po sprawdzeniu argumentów
    from ksefconfig import Config
    cfg = Config(int(sys.argv[1]))

    # Nazwa pliku faktury
    if len(sys.argv) >= 3:
        invoice_file = sys.argv[2]
    else:
        # Spróbuj znaleźć plik XML faktury
        xml_files = [f for f in os.listdir(".") if f.endswith(".xml") and "-" in f]
        if xml_files:
            invoice_file = xml_files[0]
            print(f"📄 Użyto automatycznie wykrytego pliku: {invoice_file}")
        else:
            print("❌ Nie znaleziono pliku XML faktury!")
            sys.exit(1)

    # Sprawdź czy plik istnieje
    if not os.path.exists(invoice_file):
        print(f"❌ Plik {invoice_file} nie istnieje!")
        sys.exit(1)

    # Wczytaj XML faktury
    try:
        with open(invoice_file, "r", encoding="utf-8") as f:
            invoice_xml = f.read()
        print(f"📄 Wczytano fakturę z pliku: {invoice_file}")
        print(f"Rozmiar: {len(invoice_xml)} bajtów")
    except Exception as e:
        print(f"❌ Błąd wczytywania pliku: {e}")
        sys.exit(1)

    # Wykonaj proces wysyłania
    sender = KSeFInvoiceSender(cfg)

    try:
        # 1. Otwórz sesję
        if not sender.open_online_session():
            sys.exit(1)

        # 2. Wyślij fakturę
        invoice_ref = sender.send_invoice(invoice_xml)
        if not invoice_ref:
            sys.exit(1)

        # 3. Sprawdź status
        sender.check_invoice_status(invoice_ref)

    except Exception as e:
        print(f"❌ Błąd podczas wysyłania: {e}")
    finally:
        # 4. Zamknij sesję
        sender.close_session()


if __name__ == "__main__":
    main()
