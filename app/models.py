# app/models.py
# Definice databázových modelů pomocí Peewee ORM.
# Co je ORM? Object-Relational Mapping – píšeš Python třídy místo SQL příkazů.

from peewee import SqliteDatabase, Model, CharField, TextField, IntegerField

# Připoj se k databázi
# SqliteDatabase vytvoří soubor 'app.db', pokud neexistuje
db = SqliteDatabase('app.db')

class BaseModel(Model):
    """Základní třída pro všechny modely.

    Všechny modely (Word, User atd.) dědí z této třídy.
    Proč? Aby všechny automaticky používaly stejnou databázi.
    """
    class Meta:
        database = db  # Každý model použije app.db

class Word(BaseModel):
    """Model pro jedno slovíčko (jeden záznam v tabulce 'words').

    Každý řádek v databázi = jeden Word objekt.
    Duplicity jsou povolené – např. "run" jako sloveso i podstatné jméno.

    Attributes:
        english: Anglické slovo (např. 'hello')
        part_of_speech: Slovní druh (např. 'noun', 'verb') – může být prázdné
        czech: Český překlad
        definition: Definice z API (delší text)
        pronunciation: Fonetická výslovnost (např. '/həˈloʊ/')
        audio: URL na audio soubor
        example: Příklad věty se slovem
        synonyms: Synonyma oddělená čárkami (např. 'hi,hallo')
        antonyms: Antonyma oddělená čárkami
        knowledge_level: Jak dobře slovo znáš (0=neučil jsem se, 5=perfektně umím)
        correct_count: Kolikrát jsi odpověděl správně
        wrong_count: Kolikrát jsi se spletl
        last_reviewed: Kdy jsi slovo naposledy opakoval (formát 'YYYY-MM-DD')
    """
    # CharField = krátký text (max ~255 znaků)
    # TextField = dlouhý text (tisíce znaků)
    # IntegerField = celé číslo
    # null=True = sloupec může být prázdný (None)
    # default='' = když nevyplníš hodnotu, bude prázdný string místo chyby

    english = CharField(default='')
    part_of_speech = CharField(null=True, default=None)  # Volitelné – může být None
    czech = CharField(default='')
    definition = TextField(null=True, default=None)  # Delší text než CharField
    pronunciation = CharField(null=True, default=None)
    audio = CharField(null=True, default=None)
    example = TextField(null=True, default=None)
    synonyms = TextField(null=True, default=None)
    antonyms = TextField(null=True, default=None)
    knowledge_level = IntegerField(default=0)  # 0-5 škála
    correct_count = IntegerField(default=0)
    wrong_count = IntegerField(default=0)
    last_reviewed = CharField(null=True, default=None)  # Datum jako string

    class Meta:
        table_name = 'words'  # Tabulka se bude jmenovat 'words' (ne 'word')

def create_tables():
    """Vytvoří tabulky v databázi podle definovaných modelů.

    Zavolá se při prvním spuštění aplikace v __init__.py.
    Peewee automaticky převede Python třídy na SQL CREATE TABLE příkazy.
    """
    db.create_tables([Word])  # Seznam modelů – přidej sem další (např. User)