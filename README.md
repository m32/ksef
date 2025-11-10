# ksef
Jak dobrać się do KSeF 2.0 ?

Na ten moment to zestaw plików pokazujących jak ...:

ksef.ini:
- skonfigurować wiele firm i osób autoryzowanych do ich obsługi

ksefconfig.py, plik ten jest importowany przez pozostałe pliki, a wczytuje konfigurację z pliku ksef.ini

t-00-setup.py
- pobrać brakujące dane i wypełnić nimi plik ksef.ini

t-01-cert-make.py 1
- wygenerować certyfikat (selfsigned) i wypełnić wymagane pola przez KSeF dla firmy numer 1

t-02-test-data-firma-01-create.py 1
- utworzyć firmę numer 1 w KSef

t-02-test-data-firma-02-remove.py 1
- usunąć firmę numer 1

t-02-test-data-firma-03-perm-01-grant.py 1
- zezwolić osobie na obsługę firmy numer 1

t-02-test-data-firma-03-perm-02-query.py
- odpytać o udzielone zezwolenia

t-02-test-data-osoba-01-create.py 1
- utworzyć osobę firmie numer 1 w KSeF

t-02-test-data-osoba-01-remove.py 1
- usuniąć osobę z firmy numer 1

kroki które należy wykonać by uzyskać tokeny zezwalające na pracę z KSeF:
- t-03-auth-01-challenge.py 1 f
- t-03-auth-02-sign.py 1 f
- t-03-auth-03-xades.py 1 f
- t-03-auth-04-reference.py 1 f
- t-03-auth-05-redeem.py 1 f

odnowić token autoryzacyjny po jego unieważnieniu?
- t-03-auth-06-refresh.py 1 f

alternatywne uwierzytelnienie za pomocą tokenu  (ważne do końca 2026)
- t-api-auth-token.py 1 f

parametry:
- 1 f = oznacza pracę z uprawnieniami firmy
- 1 o = oznacza pracę z uprawnieniami osoby

## Co po autoryzacji ?

fv.py 1 2 5
- generacja przykładowych faktur wystawionych przez firmę 1 dla firmy 2 - 5 sztuk

t-10-session-01-list.py 1 f
- lista otwrtych sesji

t-50-get-fa-list.py 1 f
- wyświetlenie listy faktur wystawionych w ciągu ostatnich 30

t-50-get-fa-get.py 1 f ksef-number
- pobranie faktury po numerze KSeF

## Sesja online

- t-10-session-online.py 1 f -o|-c|-s faktura.xml|-t|-u faktura.xml


znaczenie parametrów:

-o = otwarcie sesji (utworzenie pliku {cfg.prefix}-session.json)

-c = zamknięcie sesji (usunięcie pliku {cfg.prefix}-session.json)

-s = wysłanie faktury

-t = odebranie statusu wysłanych faktur

-u = odebranie dokumentu upo dla faktura.xml, musi istnieć plik faktura.xml.ref


Skrypt można wołać wielokrotnie z parametrem -s lub -t lub -u,
wtedy skrypt będzie wysyłał lub pobierał kolejne informacje,
jeżeli token autoryzacyjny utraci ważność to należy go odnowić (t-03-auth-06-refresh.py 1 f).


## Sesja batch

- t-10-session-batch.py 1 f -z|-o|-s|-c|-t


znaczenie parametrów:

-z = przygouj dane do transmisji, czyli:
    * spakuj pliki wysyłane z firmy numer 1 do jednego pliku zip
    * usun składowe pliku zip
    * podziel plik zip na mniejsze części i zaszyfruj je
    * usuń plik zip

-o = otwórz sesję wsadową

-s = wyślij podzielone części pliku do KSeF
    * usuń każdą poprawnie wysłaną część (status 201)

-c = zakończ sesję wsadową

-t = pobierz status sesji

Jeżeli token autoryzacyjny utraci ważność (status 401) to należy go odnowić (t-03-auth-06-refresh.py 1 f).
Wielokrotnie można wołać tylko opcję -t, do momentu uzyskania statusu 200 sesji.
Każdy z kroków uzupełnia plik <ksef.cfg.prefix>-session.json o kolejne dane.
