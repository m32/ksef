# KSeF 2.0 – narzędzia integracyjne

Zestaw skryptów Python umożliwiających konfigurację, autoryzację i komunikację z systemem Krajowego Systemu e-Faktur (KSeF) w wersji 2.0.

firma = logowanie właścicielskie i zarządzanie dostępem innych osób

osoba = logowanie pracownika

W KSeF nie dasz rady pracować programem, który będzie logował się przy pomocy pieczęci (NIP) z tego powodu że w programie pracuje wielu ludzi na róźnych komputerach, a klucz sprzętowy jest podpinany tylko do jednego z nich. No chyba że dasz radę :).

Jako posiadacz JDG też nie popracujesz z wykorzystaniem e-dowodu lub PUAP-u.

OK. Możesz i dasz radę, ale będzie to upierdliwe.

W jednym i drugim przypadku logujesz się jako właściciel (NIP/PUAP) i tworzysz token lub generujesz certyfikat+klucz i przekazujesz go innej osobie (biuro rachunkowe lub program komputerowy).
Te rozwiązanie omija problem klucza sprzętowego - masz certyfikat i klucz lub token, który może (nie) przestanie być wspierany w końcem 2026 roku a jest prostszy w użyciu.

Ja dla moich klientów proponuję utworzenie certyfikatu w KSeF z uprawnieniem logowanie+odczyt+zapis faktur oraz tokenu z tymi samymi uprawnieniami.

Na potrzeby skryptów w tym repozytorium certyfikat+klucz musi być zamieniona na plik w formacie PKCS12 i zrobisz to programem cert/p12-ksef.py lub komendami z biblioteki OpenSSL.

m32


## Struktura projektu

### Pliki konfiguracyjne:
- **`ksef.ini`** – konfiguracja wielu firm oraz osób upoważnionych do ich obsługi.
- **`ksefconfig.py`** – moduł wczytujący konfigurację z `ksef.ini`, importowany przez pozostałe skrypty.



##  Skrypty inicjalizacyjne i konfiguracyjne

### `t-00-setup.py`
- Pobiera dane w `ksef.ini` (NIP/PESEL).
- Pobiera certyfikaty KSeF dla środowisk: **demo**, **test**, **prod**.
- Zapisuje certyfikaty w plikach odpowiednich dla wybranej wersji.

### `t-01-cert-make.py <indeks_firmy>`
- Generuje certyfikat self-signed z wymaganymi przez KSeF polami dla firmy oraz osoby o podanym numerze firmy.
- Zapisuje certyfikat w formacie wymaganym do dalszych operacji.
- **Przykład:** `t-01-cert-make.py 1`



##  Zarządzanie danymi testowymi

### Firmy:
- `t-02-test-data-firma-01-create.py <indeks>` – rejestruje firmę w KSeF.
- `t-02-test-data-firma-02-remove.py <indeks>` – usuwa firmę w KSeF.
- `t-02-test-data-firma-03-perm-01-grant.py <indeks>` – nadaje osobie uprawnienia do obsługi firmy.
- `t-02-test-data-firma-03-perm-02-query.py` – lista udzielonych uprawnień.

### Osoby:
- `t-02-test-data-osoba-01-create.py <indeks_firmy>` – dodaje osobę do firmy.
- `t-02-test-data-osoba-01-remove.py <indeks_firmy>` – usuwa osobę z firmy.



## Proces autoryzacji

Aby uzyskać tokeny dostępu do KSeF, wykonaj sekwencyjnie:

```bash
t-03-auth-01-challenge.py <indeks> <typ>
t-03-auth-02-sign.py <indeks> <typ>
t-03-auth-03-xades.py <indeks> <typ>
t-03-auth-04-reference.py <indeks> <typ>
t-03-auth-05-redeem.py <indeks> <typ>
```
### Przykład
```bash
    t-03-auth-01-challenge.py 1 f
    t-03-auth-02-sign.py 1 f
    t-03-auth-03-xades.py 1 f
    t-03-auth-04-reference.py 1 f
    t-03-auth-05-redeem.py 1 f
```

### Odświeżanie tokena autoryzacyjnego
```bash
    t-03-auth-06-refresh.py <indeks> <typ>
```
Przykład:
```bash
t-03-auth-06-refresh.py 1 f
```

### Alternatywna autoryzacja tokenem (ważna do końca 2026):
```bash
t-api-auth-token.py <indeks> <typ>
t-03-auth-07-token.py <indeks>
```
**Parametry autoryzacji:**<br>
<indeks> f – uprawnienia w imieniu firmy (np. 1 f).<br>
<indeks> o – uprawnienia w imieniu osoby (np. 1 o).<br>

## Operacje na fakturach (po autoryzacji)
**Generowanie faktur testowych:**<br>

Przykład – generuje 5 faktur od firmy 1 dla firmy 2: 
```bash
fv.py 1 2 5
```

**Pobranie listy otwartych sesji:**<br>
```bash
t-10-session-01-list.py 1 f
```
**lista faktur wystawionych w ciągu ostatnich 30 dni:**
```bash
t-50-get-fa-list.py 1 f
```
**pobranie faktury po numerze KSeF:**
```bash
t-50-get-fa-get.py 1 f numer_ksef 
```

 **pobranie paczki faktur z ostatnich 30 dni jako archiwum ZIP.**
 ```bash
t-50-get-fa-package.py 1 f
```

## Sesja online
```bash
t-10-session-online.py 1 f [opcje]
```
Przykład - otwarcie sesji dla firmy 1:
```bash
t-10-session-online.py 1 f -o
```
Opcje:<br>
-o – otwarcie sesji (tworzy plik {cfg.prefix}-session.json).

-c – zamknięcie sesji (usuwa plik sesji).

-s <faktura.xml> – wysłanie pojedynczej faktury.

-t – sprawdzenie statusu wysłanych faktur.

-u <faktura.xml> – pobranie UPO dla faktury (wymaga pliku <faktura.xml>.ref).

**Uwaga:** Skrypt można wywoływać wielokrotnie z opcjami -s, -t, -u.
W przypadku wygaśnięcia tokena (401 Unauthorized) należy go odnowić (t-03-auth-06-refresh.py <indeks> <typ>).

## Sesja wsadowa (batch)
```bash
t-10-session-batch.py 1 f [opcje]
```
Przykład - przygotowanie faktur do wsyłki:
```bash
t-10-session-batch.py 1 f -z
```
Opcje:<br>
-z – **przygotowanie danych:**<br>
pakuje pliki firmy do archiwum ZIP,
dzieli archiwum na części i szyfruje je,
usuwa pliki źródłowe i archiwum.

-o – otwarcie sesji wsadowej.

-s – wysyłanie zaszyfrowanych części do KSeF (części z statusem 201 są usuwane lokalnie).

-c – zakończenie sesji wsadowej.

-t – pobranie statusu sesji.

**Uwaga:** Przy statusie 401 (token nieważny) należy go odnowić (t-03-auth-06-refresh.py <indeks> <typ>).
Opcję -t można wykonywać wielokrotnie aż do uzyskania końcowego statusu sesji (200).
Każdy krok aktualizuje plik {cfg.prefix}-session.json.

## Uwagi techniczne
1. **Wymagane jest środowisko Python z zainstalowanymi bibliotekami.**<br>
Jak stworzyć venv i zainstalować biblioteki (Należy wykonać po kolei w terminalu będąc w głównym katalogu repo):<br>
**Linux:**
    ```bash
    python3 -m venv venv
    source ./venv/bin/activate
    pip install -r ./requirements.txt
    ```
    **Windows**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r .\requirements.txt
    ```
    **Uwaga:** Może zdarzzyć się, że należy zamienić python3 na python albo na odwrót


2. Przed pierwszym użyciem należy skonfigurować ksef.ini i wykonać t-00-setup.py.

3. Wszystkie operacje wymagają ważnego tokena autoryzacyjnego.

4. Środowisko pracy (demo/test/prod) jest określane przez konfigurację w ksef.ini.
