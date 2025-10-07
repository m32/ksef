# ksef
Jak dobrać się do KSeF 2.0 ?

Na ten moment to zestaw plików pokazujących jak ...:

ksef.ini:
- skonfigurować wiele firm i osób autoryzowanych do ich obsługi

ksefconfig.py, plik ten jest importowany przez pozostałe pliki, a użyte parametry kasuje z sys.argv
- wczytać konfigurację z pliku ksef.ini
- parametr wymagany to numer firmy
- opcjonalny drugi paramatr --osoba = czy będziemy pracowali jako osoba obsługująca firmę z pierwszego parametru ?

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

parametry:
- 1 f = oznacza pracę z uprawnieniami firmy
- 1 o = oznacza pracę z uprawnieniami osoby

##############
Co po autoryzacji ?
- t-10-session-01-list.py
- t-50-get-fa-list.py

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
