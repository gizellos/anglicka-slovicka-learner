# app/routes.py
# Definice rout (webových cest) pro aplikaci.
# Co je routa? Když napíšeš http://127.0.0.1:5000/ do prohlížeče, Flask spustí funkci pro tu cestu.

from flask import Blueprint, render_template
from .models import Word
from .utils import generate_audio_url

# Blueprint = skupina rout
# Proč? Aby se daly routy organizovat do modulů (např. 'main' pro úvodní stránky, 'quiz' pro kvízy)
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """Úvodní stránka – zobrazí všechna slovíčka z databáze.

    Co se stane:
    1. Word.select() načte všechna slovíčka z tabulky 'words'
    2. render_template() otevře index.html a předá mu proměnnou 'words'
    3. Jinja2 v šabloně udělá loop přes slovíčka a zobrazí je

    Returns:
        HTML: Vyrenderovaná stránka index.html se slovíčky
    """
    # Načti všechna slovíčka z databáze
    # Word.select() = SQL příkaz "SELECT * FROM words"
    words = Word.select()

    # Pošli slovíčka do šablony
    # render_template('soubor.html', promenna=hodnota)
    # V šabloně pak použiješ {{ words }} pro přístup k datům
    return render_template('index.html', words=words)