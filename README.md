# Module_13_4
# Biblioteka 2.0

**Biblioteka 2.0** to aplikacja webowa służąca do zarządzania zbiorami książek, autorami oraz wypożyczeniami. Projekt zbudowany jest na frameworku Flask, z wykorzystaniem bazy danych SQLite oraz narzędzi takich jak SQLAlchemy i Flask-Migrate.

## Funkcjonalności

- Dodawanie książek i autorów
- Obsługa relacji wiele-do-wielu (książka - autor)
- Śledzenie wypożyczeń i zwrotów książek
- Responsywny i przyjazny użytkownikowi interfejs

## Technologie

- Python 3.x
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite
- HTML, CSS (styling)

## Wymagania

- Python 3.x (zalecana wersja 3.8+)
- Wirtualne środowisko Python (opcja, ale zalecana)

## Instalacja

1. Klonowanie repozytorium

Najpierw sklonuj repozytorium do swojego lokalnego środowiska.


2. Wirtualne środowisko
Zaleca się utworzenie wirtualnego środowiska dla projektu:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows


3. Instalacja zależności
Zainstaluj wszystkie wymagane pakiety korzystając z pliku requirements.txt


4. Inicjalizacja bazy danych
Zainicjalizuj bazę danych oraz uruchom migracje:

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


5. Uruchomienie aplikacji
Uruchom serwer Flask:

flask run


6. Aplikacja będzie dostępna pod adresem http://127.0.0.1:5000


7. Przykładowe dane
Aby ułatwić testowanie aplikacji, można dodać przykładowe dane do bazy. W konsoli Python:

flask shell


8. Migracje bazy danych
Do zarządzania schematem bazy danych używamy Flask-Migrate. Aby wykonać nową migrację, użyj poniższych komend:

flask db migrate -m "Opis migracji"
flask db upgrade


9. Przydatne komendy: 

Uruchomienie serwera Flask: flask run
Inicjalizacja bazy danych: flask db init
Migracja bazy danych: flask db migrate
Aktualizacja bazy danych: flask db upgrade
