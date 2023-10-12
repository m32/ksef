# ksef
Biblioteka do komunikacji z systemem KSeF w wykorzystanniem generatora: https://github.com/openapi-generators/openapi-python-client

Generacja osbywa się komendą ./x-openapi-python-client-git all|batch|common|online
Przed uruchomieniem generatora należy doinstalować wymagane przez niego pakiety.

Generator nie obsługuje wszystkich typów użytych w ksef, w związku z tym po generacji należy dodać poprawki:
* patch -p1 <openapi_python_client.diff

Konfiguracja w pliku ksef.ini, należy wypełnić:
* nip = numer nip firmy na konto której się logujemy
* token = wygenerowany token po interaktywnym zalogowaniu się na konto firmy - lub podany przez właściciela firmy

komenda: demo-online.py [--date-from=] [--date-to=] [--query=1|2|3] [file1.xml ...]

parametry:
   * --date-from= początkowy okres wyszukiwania dokumentów (yyyy-mm-ddThh:mm:ss+02:00)
   * --date-to= końcowy okres wyszukiwania dokumentów
   * --query= jakie dokumenty są wyszukiwane (1=własne, 2=obce, 3=firmy trzeciej)
   * file.xml ... - lista dokumentów do wysłania

funkcje:
* login() - logowanie tokenem
* getStatus() - odczekanie na poprawną inicjalizację sesji
* query(subject, datefrom, dateto) - pobranie informacji o dokumentach w zadanym okresie z zapisaniem ich w plikach xml o nazwie query-${subject}-${ksef}.xml
* upload(filename) - wysłanie dokumentu do ksef z zapisaniem numeru sesji i numer ksef do pliku upo.csv
* logout() - wylogowanie

komenda: demo-upo.py [numer_sesji_ ...]

parametry:
* numer_sesji - wczytanie dokumentu upo dla wybranej sesji

jeżeli istnieje plik upo.csv (tworzony przez demo-online.py) to zostaną wczytane wszystkie dokumenty upo skojarzone z numerami sesji zapisanymi w tym pliku

