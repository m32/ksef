#!/usr/bin/env vpython3
import base64
import datetime
from datetime import time, timedelta
import time
import json
import os
import sys
from typing import List

import requests

from ksefconfig import Config
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.base import CipherContext
import zipfile
from pathlib import Path
import io

def ensure_output_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

def decrypt_aes_cbc(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor: CipherContext = cipher.decryptor()
    padded = decryptor.update(data) + decryptor.finalize()
    # Usuń PKCS#7
    pad_len = padded[-1]
    if not 1 <= pad_len <= 16:
        raise ValueError("Nieprawidłowa długość paddingu AES")
    return padded[:-pad_len]


def unzip_package(zip_bytes: bytes, output_dir: Path) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written_files: List[Path] = []
    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zf:
        for info in zf.infolist():
            target_path = output_dir / info.filename
            target_path.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(info) as source, open(target_path, "wb") as target:
                target.write(source.read())
            written_files.append(target_path)
    return written_files

def main():
    cfg = Config(int(sys.argv[1]), sys.argv[2]=='o')

    script_dir = os.path.dirname(os.path.abspath(__file__))

    #symmetric_encryption_key = api_security.get_ksef_public_key_from_file(filename=os.path.join(script_dir,'ksef','ksef_public_key_certificates.json'), usage="SymmetricKeyEncryption")
    symmetric_encryption_key = cfg.getcertificte(False)[1]

    #tutaj pobierz token dostępu
    #token_manager_instance = token_manager.TokenManager(ksef_config_file='ksef_conf.json')
    #access_token = token_manager_instance.get_access_token()
    with open(f'{cfg.prefix}-auth.json', 'rt') as fp:
        auth = json.loads(fp.read())
    ####

    headers = {
        #"Authorization": f"Bearer {access_token.token}"
        "Authorization": f"Bearer {auth['accessToken']['token']}",
    }

    data_od = datetime.datetime.now() - timedelta(days=30)
    data_do = datetime.datetime.now()

    filters = {
        'dateRange': {
            'dateType': 'PermanentStorage',#'Issue' - data wystawienia, 'Invoicing' - data przyjęcia faktury w systemie KSeF, 'PermanentStorage' - data trwałego zapisu w repozytorium KSeF
            'from': data_od.isoformat(),
            'to': data_do.isoformat(), #w takiej formie nie potrzebne, now jest domyślnie
        },
        'subjectType': 'Subject2' #'Subject1' - wystawca/sprzedawca, 'Subject2' - nabywca
    }



    aes_key = os.urandom(32)
    iv = os.urandom(16)


    encrypted_key = symmetric_encryption_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )
    encrypted_key_b64 = base64.b64encode(encrypted_key).decode("ascii")
    iv_b64=base64.b64encode(iv).decode("ascii")

    payload={
        "encryption": {
            "encryptedSymmetricKey": encrypted_key_b64,
            "initializationVector": iv_b64,
        },
        "filters": filters
    }
    url=f"{cfg.url}/api/v2/invoices/exports"
    response = requests.post(url,
                             json=payload,
                             headers=headers)  #do sprawdzenia czy headers["x-ksef-feature"] = "include-metadata" coś zmienia
    response.raise_for_status()
    response_data = response.json()
    ref_number = response_data["referenceNumber"]
    print(f"Zainicjowano eksport faktur. Numer referencyjny: {ref_number}")



    max_attempts = 20
    delay_seconds = 5
    for attempt in range(max_attempts):
        resp = requests.get(
            f"{cfg.url}/api/v2/invoices/exports/{ref_number}",
            headers=headers,
        )
        resp.raise_for_status()
        data = resp.json()
        status = data.get("status", {})
        code = status.get("code")
        if code == 200:
            break #return data
        if code not in (100, 150):
            data = None
            raise RuntimeError(f"Podejście nr {attempt + 1}: Eksport zwrócił kod {code}: {status.get('description')}")
        time.sleep(delay_seconds)
    
    if data is None:
        raise TimeoutError("Przekroczono czas oczekiwania na przygotowanie eksportu")

    package = data.get("package")
    if not package:
        raise Exception("[!] Operacja zakończona, ale brak paczki (być może brak faktur w zakresie).")
    else:
        print (f"[✅] Operacja zakończona, paczka faktur gotowa do pobrania.")
        print(f"Liczba faktur w paczce: {package.get('invoiceCount', 0)}")

    parts = package.get("parts", [])
    if not parts:
        raise Exception("[!] Paczka nie zawiera części do pobrania.")

    encrypted_parts: List[tuple[str, bytes]] = []
    for part in sorted(parts, key=lambda p: p.get("ordinalNumber", 0)):
        url = part["url"]
        resp = requests.get(url, 
                            #headers=headers
                            )
        resp.raise_for_status()
        encrypted_parts.append((part.get("partName", f"part-{part.get('ordinalNumber', 0)}"), resp.content))

    decrypted_combined = bytearray()
    for part_name, encrypted_payload in encrypted_parts:
        decrypted_part = decrypt_aes_cbc(encrypted_payload, aes_key, iv)
        decrypted_combined.extend(decrypted_part)

    decrypted_bytes = bytes(decrypted_combined)

    output_dir = ensure_output_dir(Path(script_dir) / "decrypted_invoices")
    zip_path = output_dir / f"{ref_number}.zip"
    zip_path.write_bytes(decrypted_bytes)
    print(f"[+] Zapisano odszyfrowaną paczkę ZIP: {zip_path}")

    extracted = unzip_package(decrypted_bytes, output_dir / ref_number)
    print(f"[+] Rozpakowano {len(extracted)} plików do katalogu {output_dir / ref_number}")

    metadata_files = [p for p in extracted if p.name.lower().endswith(".json")]
    if metadata_files:
        print(f"    Metadane: {metadata_files[0]}")
    xml_files = [p for p in extracted if p.suffix.lower() == ".xml"]
    if xml_files:
        print(f"    Faktury XML: {len(xml_files)} plików")

    if package.get("isTruncated"):
        print("[!] Paczka została obcięta (isTruncated=true) – należy ponowić eksport z odpowiednimi parametrami.")



if __name__ == "__main__":
    main()