# ZAI-Lab10 — System Szkoleniowy (Django + DRF)

Projekt zrealizowany w ramach Laboratorium 25-30 z przedmiotu **Zaawansowane Aplikacje Internetowe**.

Jest to platforma do zarządzania szkoleniami, oferująca panel administracyjny, interfejs publiczny oraz dedykowane REST API zrealizowane za pomocą Django REST Framework.

---

## Wymagania

- Python 3.11+
- Git

---

## Instrukcja wdrożenia (Setup)

Wykonaj poniższe kroki, aby uruchomić projekt lokalnie na swoim komputerze:

### 1. Sklonuj repozytorium

```bash
git clone https://github.com/MarcherOV/ZAI-Lab10.git
cd ZAI-Lab10
```

### 2. Utwórz i aktywuj środowisko wirtualne

**Na Windows:**
```bat
python -m venv .venv
.venv\Scripts\activate
```

**Na Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Zainstaluj wymagane pakiety

```bash
pip install django djangorestframework
```

### 4. Wykonaj migracje bazy danych

W tym kroku utworzona zostanie lokalna baza SQLite (`db.sqlite3`) oraz odpowiednie tabele zdefiniowane w modelach.

```bash
cd src
python manage.py makemigrations
python manage.py migrate
```

### 5. Utwórz konto superużytkownika

Aby mieć pełny dostęp do Panelu Zarządzania (`/offer-mng/`) oraz panelu administracyjnego (`/admin/`):

```bash
python manage.py createsuperuser
```

### 6. Uruchom serwer developerski

```bash
python manage.py runserver
```

---

## Struktura aplikacji i dostępne adresy URL

Po uruchomieniu serwera aplikacja będzie dostępna pod adresem bazowym: `http://127.0.0.1:8000/`

| Ścieżka | Opis |
|---|---|
| `/offer/` | Oferta Publiczna — przeglądanie kategorii i dostępnych szkoleń |
| `/offer/register/` | Rejestracja na szkolenie — formularz zgłoszeniowy |
| `/offer-mng/` | Panel Zarządzania *(wymaga logowania)* — dodawanie i edycja szkoleń oraz kategorii |
| `/issues/` | Zgłaszanie problemów — formularz kontaktowy do zgłaszania usterek |
| `/offer-mng/generator/` | Generator Formularzy *(z Lab 6)* — dynamiczne budowanie formularzy z zapisem JSON i do bazy danych |
| `/admin/` | Panel Administracyjny Django — sortowanie, filtrowanie, wyszukiwanie rekordów |
| `/api/...` | Endpointy REST API (np. `/api/courses/`, `/api/problems/`, `/api/register/`) — obsługa żądań GET i POST |

---

## Autor

**Volodymyr Marchuk**, 030375