# Anglická Slovíčka Learner

⚠️ **WORK IN PROGRESS** – Projekt je v aktivním vývoji, mnoho funkcí ještě není implementováno.

## Popis
Toto je moje osobní webová aplikace postavená na Flasku pro učení anglických slovíček. Mohu přidávat nová slovíčka, prohlížet je v podobě flashcards, absolvovat kvízy a sledovat svůj pokrok. Aplikace integruje externí API pro získávání definic a výslovnosti slov. Databáze je řízena SQLite pro jednoduchost a přenositelnost.

Aplikace je v rané fázi vývoje – zatím obsahuje základní strukturu s úvodní stránkou zobrazující slovíčka z databáze. Další funkce (jako lekce, formuláře pro přidávání slovíček a kvízy) budou přidány postupně.

## Požadavky
- Python 3.8+
- Pip pro instalaci závislostí

### Závislosti (z requirements.txt)
- `flask`: Webový framework pro backend a šablony.
- `peewee`: ORM pro práci s SQLite databází.
- `gTTS`: Generování audio výslovnosti pro slovíčka (US English).
- Další standardní závislosti: `requests`, `Jinja2`, `Werkzeug`.

Po instalaci nových modulů spusťte `python update_requirements.py`, abyste aktualizovali `requirements.txt`.

## Instalace
1. Naklonuj repozitář:
   ```bash
   git clone <url-repozitáře>
   cd anglicka-slovicka-learner
   ```

2. Vytvoř virtuální prostředí:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. Nainstaluj závislosti:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicializuj databázi:
   - Databáze `app.db` se vytvoří automaticky při prvním spuštění aplikace.
   - Tabulka `words` bude inicializována s potřebnými sloupci.

## Spuštění
### Lokálně
1. Spusť aplikaci:
   ```bash
   python main.py
   ```
   Aplikace bude dostupná na `http://127.0.0.1:5000/` v debug módu.

### Na serveru (PythonAnywhere)
- Nahraji soubory na `eu.pythonanywhere.com`.
- Nastavím WSGI soubor (např. `wsgi.py`) s `from app import create_app; application = create_app()`.
- Konfiguruji statické soubory a šablony v dashboardu.
- Databáze SQLite bude umístěna v `/home/<uživatel>/mysite/app.db`.

## Struktura projektu
```
anglicka-slovicka-learner/
├── app/                  # Hlavní modul Flask aplikace
│   ├── __init__.py       # Tovární funkce create_app() a registrace blueprintů
│   ├── routes.py         # Routy (úvodní stránka s načtením slovíček z DB)
│   ├── models.py         # Peewee modely (Word s plnou funkcionalitou)
│   └── utils.py          # Pomocné funkce (generování audio pro slovíčka)
├── templates/            # Jinja2 šablony
│   ├── main.html         # Základní layout s Bootstrapem
│   ├── _word_snippet.html # HTML kód pro zobrazení jednoho slovíčka
│   └── index.html        # Úvodní stránka s tabulkou slovíček
├── static/               # Statické soubory
│   ├── style.css         # Vlastní styly (audio tlačítka atd.)
│   ├── favicon.ico       # Ikona stránky
│   ├── js/
│   │   └── audio.js      # JS pro přehrávání audio výslovnosti
│   └── audio/            # Generované MP3 soubory (vytváří se automaticky)
├── app.db                # SQLite databáze (vytváří se automaticky)
├── main.py               # Hlavní vstupní bod pro lokální spuštění
├── requirements.txt      # Seznam závislostí
├── TODO.md               # Věci k dodělání
├── update_requirements.py # Skript pro aktualizaci requirements.txt
└── README.md             # Tento soubor
```

## Implementované funkce
### Databáze (Peewee ORM)
- **Model Word** s podporou duplicit pro různé významy:
  - Anglické slovo, část řeči, český překlad
  - Definice, výslovnost, příklady, synonyma, antonyma
  - Úroveň znalosti (0-5), počítadla správných/špatných odpovědí
  - Datum posledního zkoušení (pro spaced repetition)
- Automatická inicializace databáze při startu aplikace

### Audio výslovnost
- Generování US English audio pomocí gTTS
- Uložení MP3 do `static/audio/` (cache pro rychlost)
- Přehrávání na klik přes JavaScript (tlačítko 🔊)

### Webové rozhraní
- Úvodní stránka zobrazující všechna slovíčka z databáze
- Bootstrap 5 responsive design
- Snippet pro jednotlivé slovíčko s detaily

## Použité technologie a nástroje
- **Backend**: Flask (web framework), Peewee (ORM pro SQLite).
- **Frontend**: Bootstrap 5 (CSS/JS z CDN), Jinja2 (šablony), vlastní CSS/JS.
- **Audio**: gTTS (Google Text-to-Speech) pro US English výslovnost.
- **Databáze**: SQLite (prohlížeč: [DB Browser for SQLite](https://sqlitebrowser.org/)).
- **API**: [Dictionary API](https://dictionaryapi.dev/) (plánováno) pro definice a příklady.
- **Deploy**: PythonAnywhere (`eu.pythonanywhere.com`).

## Plánované funkce (TODO.md)
### Vysoká priorita
- [ ] Vytvořit tabulku pro lekce (propojení s Words, sledování pokroku)
- [ ] Přidat stránku Lekce s klikatelným seznamem
- [ ] Implementovat autentizaci (Flask-Login, model User)
- [ ] Základní CRUD routy pro slovíčka (přidávání/úpravy/mazání)

### Střední priorita
- [ ] Integrace Dictionary API pro automatické načítání dat
- [ ] Flashcards view s přední/zadní stranou
- [ ] Kvíz mód s náhodnými otázkami a ukládáním výsledků

### Nízká priorita
- [ ] Statistiky s grafy pokroku (Chart.js)
- [ ] Personalizované seznamy a kategorie
- [ ] Unit testy (pytest)
- [ ] Migrační systém (peewee-migrate)

Aktuální stav úkolů viz `TODO.md`.

## Poznámky
- Repozitář je public pouze pro sdílení kódu s AI asistenty – aplikace je určena výhradně pro osobní použití.
- Po instalaci nových modulů spustím `python update_requirements.py` pro aktualizaci `requirements.txt`.

## Kontakt
- Autor: Pilda