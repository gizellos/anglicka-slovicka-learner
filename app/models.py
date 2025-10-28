# app/models.py
# Modul pro modely databáze (Peewee ORM) – definuje strukturu tabulek pro slovíčka a uživatele.
# Proč Peewee? Jednoduché ORM pro SQLite – píšeš Python místo SQL, méně chyb a rychlejší vývoj.

from peewee import SqliteDatabase, Model, CharField, TextField, IntegerField  # Import Peewee typů pro sloupce
from datetime import date  # Pro datum last_reviewed (použijeme pro algoritmus opakování – např. spaced repetition)

# Připojení k databázi – relativní cesta z kořene projektu (vytvoří soubor 'app.db', pokud neexistuje)
db = SqliteDatabase('app.db')  # Globální připojení – sdílí se mezi všemi modely (Word, User atd.)

# Základní třída pro modely – dědičnost: Všechny modely (Word, User) z ní dědí společné nastavení (jako šablona)
class BaseModel(Model):
    """Základní třída pro všechny modely v appce.

    Nastavuje společnou databázi (SQLite) a defaulty pro dědící třídy.
    Proč dědičnost? Aby se nastavení (např. database) neopakovalo v každém modelu.

    Attributes:
        Meta.database: Připojení k 'app.db' – sdílené pro všechny modely.
    """
    class Meta:
        database = db  # Všechny dědící modely používají tuto DB (bezpečnost: jedna DB pro appku)

# Model pro slovíčko – reprezentuje jeden záznam (význam slovíčka) v tabulce 'words'
class Word(BaseModel):
    """Model pro slovíčko v databázi.

    Umožňuje duplicity pro různé významy (např. 'run' jako verb/noun).
    Používá se pro ukládání dat z API a pokroku učení (knowledge_level 0-5).
    Proč duplicity? Jazyk má více významů – každý má vlastní definici a znalost.

    Attributes:
        english (str): Anglické slovo (default prázdné pro bezpečnost při vytváření).
        part_of_speech (str): Časť řeči (např. 'noun', null=True/volitelné pro flexibilitu).
        czech (str): Český překlad (povinný, default prázdné).
        definition (str): Definice z API (volitelné, null=True – fallback v šabloně).
        pronunciation (str): Fonetická výslovnost z API (volitelné).
        audio (str): URL na audio výslovnost z API (volitelné – pro přehrání v prohlížeči).
        example (str): Příklad věty z API (volitelné).
        synonyms (str): Synonyma jako string s čárkami (např. 'hi,hallo', volitelné – parsuj split(',') v kódu).
        antonyms (str): Antonyma stejně (volitelné).
        knowledge_level (int): Úroveň znalosti (0=neučil se, 1=velmi problematické, 5=naučené, default=0 pro nové).
        correct_count (int): Počet správných odpovědí (pro algoritmus, default=0).
        wrong_count (int): Počet špatných odpovědí (default=0).
        last_reviewed (str): Datum posledního zkoušení (např. '2025-10-26', volitelné – pro spaced repetition).

    Meta:
        table_name: 'words' – plural pro logiku seznamu (default by byl 'word').
    """
    english = CharField(default='')  # Povinný klíč pro hledání – default prázdné pro bezpečnost
    part_of_speech = CharField(null=True, default=None)  # Volitelné – pro duplicity významů (noun vs. verb)
    czech = CharField(default='')  # Povinný – default prázdné, abys mohl vytvořit záznam bez chyby
    definition = TextField(null=True, default=None)  # Volitelné – pro definice z API (delší text)
    pronunciation = CharField(null=True, default=None)  # Volitelné – fonetika z API
    audio = CharField(null=True, default=None)  # Volitelné – URL pro zvuk (přidej <audio> v šabloně)
    example = TextField(null=True, default=None)  # Volitelné – příklad věty z API
    synonyms = TextField(null=True, default=None)  # Volitelné – string s čárkami (např. 'hi,hallo')
    antonyms = TextField(null=True, default=None)  # Volitelné – stejně jako synonyms
    knowledge_level = IntegerField(default=0)  # Klíč pro algoritmus – 0=nové, 5=naučené
    correct_count = IntegerField(default=0)  # Pro statistiky – počítá správné odpovědi v kvízu
    wrong_count = IntegerField(default=0)  # Pro statistiky – počítá chyby pro častější opakování
    last_reviewed = CharField(null=True, default=None)  # Volitelné – datum pro spaced repetition (např. 'YYYY-MM-DD')

    class Meta:
        table_name = 'words'  # Přejmenuje tabulku z default 'word' na plural 'words' – pro lepší logiku seznamu

# Funkce pro vytvoření tabulek – volá se při startu appky v __init__.py
def create_tables():
    """Vytvoří všechny tabulky v databázi na základě modelů.

    Args:
        Žádné (používá globální db z tohoto souboru).

    Returns:
        Žádné (Peewee to udělá automaticky – vytvoří 'words' tabulku se sloupci).

    Notes:
        Volá se v app_context() – proč? Aby Peewee věděl o Flask prostředí.
        Přidej další modely (např. User) do [Word, User] pro automatické vytvoření.
    """
    db.create_tables([Word])  # Seznam modelů – Peewee vytvoří tabulky podle definic (sloupce, typy)