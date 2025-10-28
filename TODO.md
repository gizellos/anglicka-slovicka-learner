# TODO - Seznam úkolů pro Anglická Slovíčka Learner

Tento soubor sleduje otevřené úkoly a plánované funkce. Priorita: **Vysoká** (blokuje další vývoj), **Střední** (důležité pro MVP), **Nízká** (nice-to-have). Odhadovaný čas je přibližný.

## Vysoká priorita
- [x] Nastavit databázi: Vytvořit `models.py` s Peewee modely pro slovíčka (slovo, definice, překlad, úroveň, pokrok). Inicializovat SQLite DB v `__init__.py`. (Odhad: 2-3 hodiny) – Hotovo: Model Word s duplicitami pro významy, knowledge_level (0-5), table_name='words', DB 'app.db'.
- [ ] Přidat autentizaci: Implementovat Flask-Login pro registraci/login. Vytvořit model User. (Odhad: 4-5 hodin)
- [ ] Základní routy pro CRUD slovíček: Přidat `/add_word`, `/edit_word`, `/delete_word` v `routes.py` s WTForms formuláři. (Odhad: 3-4 hodin)

## Střední priorita
- [ ] Integrace API: Vytvořit funkci pro volání dictionaryapi.dev (např. v utilitě) a zobrazovat definice/výslovnost v šablonách. (Odhad: 2 hodiny)
- [ ] Flashcards view: Nová routa `/flashcards` s Jinja2 šablonou pro zobrazení slovíček (přední/zadní strana). (Odhad: 3 hodiny)
- [ ] Kvíz mód: Routa `/quiz` s náhodným výběrem slovíček, body a ukládáním výsledků do DB. (Odhad: 4-6 hodin)

## Nízká priorita
- [ ] Statistika: Routa `/stats` s grafy pokroku (použít Chart.js nebo Matplotlib export). (Odhad: 3 hodiny)
- [ ] Personalizované seznamy: Modely pro kategorie slovíček, routy pro filtrování. (Odhad: 2-3 hodiny)
- [ ] Testy: Přidat unit testy pro modely a routy (pytest). (Odhad: 5+ hodin)
- [ ] Migrační systém: Nastavit peewee-migrate pro změny v DB. (Odhad: 1-2 hodiny)
- [ ] Styly: Rozšířit `style.css` o animace pro flashcards (CSS transitions). (Odhad: 1 hodina)
- [ ] Deploy úpravy: Vytvořit `wsgi.py` pro PythonAnywhere a otestovat na serveru. (Odhad: 1 hodina)

## Další poznámky
- Aktualizuj tento soubor při dokončení úkolu (přepni [ ] na [x]).
- Pro sledování: Použij GitHub Issues pro složitější tasky.
- Datum poslední aktualizace: 2025-10-26

Pokud se něco změní, upravte nebo přesuňte do README.