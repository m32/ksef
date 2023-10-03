# ksef
Biblioteka do komunikacji z systemem KSeF

przykład w pliku demo.py
    - logowanie tokenem
    - odczekanie na poprawną inicjalizację sesji
    - pobranie informacji o własnych fakturach w zadanym okresie
    - pobranie obcych faktur w zadanym okresie i zapisanie ich w pliku xml
    - wylogowanie

konfiguracja w pliku ksef.ini:
[ksef]
api = adres serwera KSeF
publickey = klucz publiczny serwera
nip = numer nip firmy na konto której się logujemy
token = wygenerowany token po interaktywnym zalogowaniu się na konto firmy - lub podany przez właściciela firmy
