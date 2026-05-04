# ZAI-Lab10
# System Szkoleniowy (Django + DRF)

Projekt zrealizowany w ramach Laboratorium 25-30 z przedmiotu Zaawansowane Aplikacje Internetowe.
Jest to platforma do zarządzania szkoleniami, oferująca panel administracyjny, interfejs publiczny oraz dedykowane REST API zrealizowane za pomocą Django REST Framework.

## Wymagania
* Python 3.11+
* Git

## Instrukcja wdrożenia (Setup)

Wykonaj poniższe kroki, aby uruchomić projekt lokalnie na swoim komputerze:

1. **Sklonuj repozytorium:**
   bash
   git clone [https://github.com/MarcherOV/ZAI-Lab10.git](https://github.com/MarcherOV/ZAI-Lab10.git)
   cd ZAI-Lab10

2. **Utwórz i aktywuj środowisko wirtualne:**

    Na Windows:
    python -m venv .venv
    .venv\Scripts\activate
    Na Linux/Mac:
    bash
    python -m venv .venv
    source .venv/bin/activate

3. **Zainstaluj wymagane pakiety:**
Zainstaluj Django oraz framework do budowy API:
    bash
    pip install django djangorestframework

4. **Wykonaj migracje bazy danych:**
W tym kroku utworzona zostanie lokalna baza SQLite (db.sqlite3) oraz odpowiednie tabele zdefiniowane w modelach.
    cd src
    python manage.py makemigrations
    python manage.py migrate

5. **Utwórz konto superużytkownika:**
   Aby mieć pełny dostęp do Panelu Zarządzania (`/offer-mng/`) oraz panelu administracyjnego (`/admin/`), stwórz konto:
    bash
    python manage.py createsuperuser

6. **Uruchom serwer developerski:**
    python manage.py runserver

## Struktura aplikacji i dostępne adresy URL
Po uruchomieniu serwera, poszczególne moduły aplikacji będą dostępne pod następującymi adresami bazującymi na http://127.0.0.1:8000/:

    -Oferta Publiczna: /offer/ - przeglądanie kategorii i dostępnych szkoleń.

    -Rejestracja na szkolenie: /offer/register/ - dostęp do formularza zgłoszeniowego na wybrane szkolenie.

    -Panel Zarządzania (wymaga logowania): /offer-mng/ - dodawanie i edycja szkoleń oraz kategorii z poziomu interfejsu aplikacji.

    -Zgłaszanie problemów (Issues): /issues/ - formularz kontaktowy do zgłaszania usterek w systemie.

    -Generator Formularzy (z Lab 6): /offer-mng/generator/ - narzędzie do dynamicznego budowania formularzy z możliwością zapisu wyników w formacie JSON oraz w bazie danych.

    -Panel Administracyjny Django: /admin/ - w pełni dostrojony widok z możliwością sortowania, filtrowania, wyszukiwania rekordów (QuerySet) i lepszymi etykietami.

    -Endpointy REST API: /api/... (np. /api/courses/, /api/problems/, /api/register/) - interfejs programistyczny zbudowany na klasach (CBV) w Django REST Framework do obsługi żądań GET oraz POST.

# Autor: Volodymyr Marchuk, 030375