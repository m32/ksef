# ksef
Jak dobrać się do KSeF 2.0 ?

Na ten moment to zestaw plików pokazujących jak ...:

ksef.ini:
- skonfigurować wiele firm i osób autoryzowanych do ich obsługi

ksefconfig.py, plik ten jest importowany przez pozostałe pliki, a użyte parametry kasuje z sys.argv
- wczytać konfigurację z pliku ksef.ini
- parametr wymagany to numer firmy
- opcjonalny drugi paramatr --osoba = czy będziemy pracowali jako osoba obsługująca firmę z pierwszego parametru ?

t-01-cert-make.py
- wygenerować certyfikat (selfsigned) i wypełnić wymagane pola przez KSeF

t-02-test-data-firma-01-create.py
- utworzyć firmę w KSef

t-02-test-data-firma-02-remove.py
- usunąć firmę

t-02-test-data-firma-03-perm-01-grant.py
- zezwolić osobie na obsługę firmy

t-02-test-data-firma-03-perm-02-query.py
- odpytać o udzielone zezwolenia

t-02-test-data-osoba-01-create.py
- utworzyć osobę w KSeF

t-02-test-data-osoba-01-remove.py
- usuniąć osobę

kroki które należy wykonać by uzyskać tokeny zezwalające na pracę z KSeF:
- t-03-auth-01-challenge.py
- t-03-auth-02-sign.py
- t-03-auth-03-xades.py
- t-03-auth-04-reference.py
- t-03-auth-05-redeem.py

odnowić token autoryzacyjny po jego unieważnieniu?
- t-03-auth-06-refresh.py

##############
Co po autoryzacji ?
- t-10-session-01-list.py
- t-50-get-fa-list.py
