\# System Zarządzania Wypożyczalnią Sprzętu (Django REST API)



\## Autor

Adam Olszewski



\## Opis Projektu

Projekt to system REST API do zarządzania wypożyczalnią sprzętu (np. budowlanego lub ogrodniczego). Umożliwia ewidencję sprzętu, kategoryzację, rejestrację wypożyczeń oraz historię serwisową.



\## Funkcjonalności

\* Pełny system CRUD dla wszystkich modeli.

\* Uwierzytelnianie oparte na Tokenach (Token Authentication).

\* Autoryzacja z podziałem na role (Admin vs Pracownik).

\* Endpointy specjalne:

&nbsp;   \* Wyszukiwanie sprzętu po nazwie.

&nbsp;   \* Filtrowanie tylko dostępnych przedmiotów.



\## Struktura Modeli

1\. \*\*Category\*\*: Grupowanie sprzętu.

2\. \*\*Equipment\*\*: Dane o sprzęcie i jego dostępności.

3\. \*\*Rental\*\*: Rejestracja wypożyczeń przez użytkowników.

4\. \*\*Maintenance\*\*: Historia serwisowa i naprawy.



\## Poziomy Dostępu

\* \*\*Administrator\*\*: Pełne uprawnienia do edycji i usuwania wszystkich danych.

\* \*\*Pracownik\*\*: Możliwość przeglądania danych i dodawania wypożyczeń. Brak uprawnień do usuwania sprzętu i edycji kategorii.



\## Instrukcja Uruchomienia

1\. Instalacja wymaganych bibliotek:

&nbsp;  pip install -r requirements.txt



2\. Wykonanie migracji bazy danych:

&nbsp;  python manage.py migrate



3\. Uruchomienie serwera:

&nbsp;  python manage.py runserver



\## Dokumentacja API

\* `GET /api/equipment/` - Lista całego sprzętu.

\* `GET /api/equipment/available/` - Lista dostępnego sprzętu.

\* `GET /api/equipment/search/?name=fraza` - Wyszukiwanie sprzętu.

\* `POST /api/register/` - Rejestracja nowego użytkownika.

\* `POST /api/login/` - Pobranie tokena autoryzacji.

