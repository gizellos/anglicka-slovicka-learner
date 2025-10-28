# Anglická Slovíčka Learner

## Popis
Toto je webová aplikace postavená na Flasku, která slouží k učení anglických slovíček. Uživatelé mohou přidávat nová slovíčka, prohlížet je v podobě flashcards, absolvovat kvízy a sledovat svůj pokrok. Aplikace integruje externí API pro získávání definic a výslovnosti slov. Databáze je řízena SQLite pro jednoduchost a přenositelnost. Plánované funkce zahrnují autentizaci uživatelů, personalizované seznamy slovíček a statistiky učení.

Aplikace je v rané fázi vývoje – zatím obsahuje základní strukturu s úvodní stránkou. Další funkce (jako modely databáze, formuláře a routy pro kvízy) budou přidány postupně.

## Požadavky
- Python 3.8+
- Pip pro instalaci závislostí

### Závislosti (z requirements.txt)
- `flask`: Webový framework pro backend a šablony.
- `peewee`: ORM pro práci s SQLite databází.
- `flask-login`: Řízení autentizace a session uživatelů.
- `flask-wtf`: Validace a renderování formulářů (včetně CSRF ochrany).

Po instalaci modulů spusťte `python update_requirements.py`, abyste aktualizovali `requirements.txt`.

## Instalace
1. Naklonujte repozitář (nebo vytvořte nový):
   git clone <váš-repo-url>
   cd anglicka-slovicka-learner

2. Vytvořte virtuální prostředí (doporučeno):
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate

3. Nainstalujte závislosti:
   pip install -r requirements.txt

4. Inicializujte databázi (po přidání modelů v Peewee):
   - Vytvořte soubor `app.db` (SQLite) ručně nebo přes migrační skript (plánováno).

## Spuštění
### Lokálně
1. Spusťte aplikaci:
   python main.py
   Aplikace bude dostupná na `http://127.0.0.1:5000/` v debug módu.

### Na serveru (PythonAnywhere)
- Nahrajte soubory na `eu.pythonanywhere.com`.
- Nastavte WSGI soubor (např. `wsgi.py`) s `from app import create_app; application = create_app()`.
- Konfigurujte statické soubory a šablony v dashboardu.
- Databáze SQLite bude umístěna v `/home/<uživatel>/mysite/app.db`.

## Struktura projektu
```tree
anglicka-slovicka-learner/
├── app/                  # Hlavní modul Flask aplikace
│   ├── __init__.py       # Tovární funkce create_app() a registrace blueprintů
│   ├── routes.py         # Routy (zatím jen úvodní stránka)
│   └── models.py         # (Plánováno) Peewee modely pro slovíčka, uživatele atd.
├── templates/            # Jinja2 šablony
│   ├── main.html         # Základní layout s Bootstrapem
│   ├── _word_snippet_.html  # HTML kód co generuje jedno slovíčko
│   └── index.html        # Úvodní stránka
├── static/               # Statické soubory
│   └── style.css         # Vlastní styly (zatím prázdný)
├── main.py               # Hlavní vstupní bod pro lokální spuštění
├── requirements.txt      # Seznam závislostí
├── TODO.txt              # Věci k dodělání
├── update_requirements.py # Skript pro aktualizaci requirements.txt
└── README.md             # Tento soubor
```

## Použité technologie a nástroje
- **Backend**: Flask (web framework), Peewee (ORM pro SQLite).
- **Frontend**: Bootstrap 5 (CSS/JS z CDN), Jinja2 (šablony), vlastní CSS.
- **Autentizace**: Flask-Login.
- **Formuláře**: WTForms / Flask-WTF.
- **Databáze**: SQLite (prohlížeč: [DB Browser for SQLite](https://sqlitebrowser.org/)).
- **API**: [Dictionary API](https://dictionaryapi.dev/) pro definice, výslovnost a příklady slov.
- **Deploy**: PythonAnywhere (`eu.pythonanywhere.com`).

## Plánované funkce (TODO)
- [ ] Modely Peewee pro slovíčka (slovo, definice, překlad, úroveň obtížnosti, pokrok uživatele).
- [ ] Routy pro přidávání/upravování slovíček (s formuláři WTForms).
- [ ] Flashcard zobrazení a kvíz mód.
- [ ] Integrace API pro automatické načítání dat o slově.
- [ ] Uživatelská autentizace (registrace, login).
- [ ] Statistika a personalizované seznamy.
- [ ] Testy (unittest nebo pytest).
- [ ] Migrační systém pro DB (Peewee-migrate).

## Přispívání
Pokud chcete přispět:
1. Forkněte repozitář.
2. Vytvořte branch (`git checkout -b feature/nova-funkce`).
3. Commitněte změny (`git commit -m 'Přidáno X'`).
4. Pushněte do branchu (`git push origin feature/nova-funkce`).
5. Otevřete Pull Request.

Používejte PEP 8 pro styl kódu. Testujte změny lokálně před odesláním.

## Licence
Tento projekt je licencován pod MIT licencí – viz `LICENSE` soubor (vytvořte ho, pokud chybí).

## Kontakt
- Autor: Pilda (kontakt přes GitHub nebo email).
- Otázky? Otevřete issue v repozitáři.

Díky za zájem o projekt!