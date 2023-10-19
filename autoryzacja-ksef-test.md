Na stronie https://ksef-test.mf.gov.pl/web wybieramy:
1. Strona główna KSEF
- Uwirzytelnij się w krajowym Systemie e-Faktur
2. Kontekst logowania
- wybierasz identyfikator NIP
- w polu NIP firmy wpisujesz poprawny nip lub nip testowy, np.: 1111111111, 9999999999
- klikasz guzik uwierzytelnij
3. Wybierz sposób logowania
- profil zaufany, jeżeli już masz powiązanie z numerem NIP firmy do której zamirzasz się logować
- certyfikat kwalifikowany/pieczęć jeżeli tworzysz powiązanie do logowania lub posiadasz odpowiedni certyfikat
4. pierwsze logowanie lub logowanie certyfikatem
- certyfikat jest z numerem NIP lub PESEL -> TAK, odpowiednie certyfikaty tworzysz komendą: ./x-cert.sh
- klikasz dalej
- jeżeli już utworzyłeś poprzednio powiązanie to:
    - klikasz guzik "Pobierz dane autoryzacyjne", plik zapisz jako ksef-sesja.xml
    - na swoim komputerze podpisujesz plik ksef-sesja.xml
        - jeżeli masz powiązanie VAT-PESEL to: ./x-sign-endesive-xml.py x-cert-pesel ksef-sesja.xml
        - jeżeli masz powiązanie VAT-NIP to: ./x-sign-endesive-xml.py x-cert-nip ksef-sesja.xml
    - klikasz guzik "Dodaj plik"
    Po chwili powinieneś być zalogowany w KSEF-TEST
- jeżeli tworzysz powiązanie to w polu "Typ identyfikatora" wybierasz dowolną wartość (Pieczęć NIP/Podpis NIP/Podpis PESEL)
    - dla Pieczęć NIP w polu Numer NIP wpisujesz to samo co wpisałeś w pkt 2 w polu NIP firmy (1111111111 lub 9999999999 lub poprawny NIP)
    - dodatkowe dane certyfikatu - nie wiem do czego to jest
    - klikasz guzik "Uwierzytelnij do aplikacji testowej"
    Po chwili powinieneś być zalogowany w KSEF-TEST

Od tego momentu program KSEF-TEST nie różni się od KSEF-DEMO, czyli:

5. generujesz token: Tokeny/Generuj token
- nadajesz opis i ustawiasz role
- klikasz guzik "Generuj token" i pokazany token zapisujesz w pliku ksef.ini w nowej sekcji, np.
[firma1111111111]
nip=1111111111
token="tu wpisujesz to co zostało wygenerowane"
6. używasz wtedy, np.:
./demo-online.py \
--server=ksef-test \
--user=firma1111111111 \
--query=2 \
--date-from=2023-10-17T09:00:00T+0200 \
--date-to=2023-10-17T10:00:00T+0200
7. generujesz uprawnienie: Uprawnienie/Nadaj uprawnienie
- wybierasz rodzaj uprawnienia
- jeżeli chcesz się logować certyfikaten to:
    - wybierasz firmę i wpisujesz jej NIP, ten wygenerowany przez x-cert.sh
    - wybierasz osobę, to w polu "Wskaż rodzaj podmiotu uprawnionego" wybierasz "Osoba fizyczna" to:
        - wpisujesz jej NIP/PESEL, ten wygenerowany przez x-cert.sh
        - imię musi być identyczne jak w certyfikacie: Jan
        - nazwisko musi być identyczne jak w certyfikacie: Babacki
- klikasz guzik "Nadaj uprawnienie"

Od tego momentu możesz w pkt 4. logować się w ramach wygenerowanych uprawnień przy pomocy wygenerowanego certyfikatem
