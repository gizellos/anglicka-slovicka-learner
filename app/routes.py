# app/routes.py
# Hlavní blueprint pro routy appky – organizuje webové cesty (routy) do modulárních sekcí.
# Proč blueprint? Aby routy (např. / pro úvod, /quiz pro kvíz) byly oddělené, snadno rozšiřitelné.
# Registruje se v __init__.py – jako "připoj sekci menu k restauraci".

from flask import Blueprint, render_template  # Blueprint pro organizaci rout, render_template pro načtení šablon
from .models import Word  # Import modelu Word (pro práci se slovíčky – nahoře pro rychlost a čitelnost)
from .utils import generate_audio_url  # Import utility z utils.py

bp = Blueprint('main', __name__)  # Vytvoř blueprint 'main' – "sekce" pro úvodní routy (__name__ = cesta k souboru)

@bp.route('/')
def index():
    """Hlavní routa – zobrazí úvodní stránku s tabulkou slovíček z DB.

    Načte data z tabulky 'words', předá do šablony index.html pro dynamické zobrazení.
    Později přidáme filtr podle algoritmu (např. jen problematická slovíčka).

    Args:
        Žádné (používá globální DB z models.py).

    Returns:
        Renderovaná šablona: index.html s proměnnou words (seznam slovíček).

    Notes:
        words = Word.select(): Peewee query – načte všechny záznamy z DB.
        render_template: Flask načte HTML, Jinja2 vloží data ({{ word.english }} atd.).
    """
    # Načti data z DB – Word.select() vrátí seznam objektů (jako SQL "SELECT * FROM words")
    words = Word.select()

    # TODO: Zde můžeme přidat logiku pro vybírání podle algoritmu (např. .where(knowledge_level < 3) pro problematická)
    # Proč TODO? Abychom si pamatovali, kde rozšířit pro spaced repetition


    return render_template('index.html', words=words)  # Předej šabloně seznam slovíček – Jinja2 loop ho zobrazí
