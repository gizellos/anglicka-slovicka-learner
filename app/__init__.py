# app/__init__.py
# Tovární funkce pro vytvoření Flask aplikace.
# Proč "továrna"? Protože funkce create_app() vyrábí Flask objekt – můžeš ji zavolat víckrát s různým nastavením.

from flask import Flask
from .models import create_tables
from app.constants import PROJECT_ROOT  # Import PROJECT_ROOT z constants pro centralizaci
import os

def create_app():
    """Vytvoří a nakonfiguruje Flask aplikaci.

    Returns:
        Flask: Připravená aplikace s routami a inicializovanou databází.
    """
    # Vytvoř základní Flask objekt
    # __name__ = 'app' – říká Flasku, kde hledat templates/ a static/
    app = Flask(__name__)

    # Nastav absolutní cestu ke static/ složce (použití konstanty)
    # Proč? Na Windowsu občas Flask nenajde relativní cestu správně
    app.static_folder = os.path.join(PROJECT_ROOT, 'static')  # Spojí cestu: PROJECT_ROOT + 'static'
    app.static_url_path = '/static'  # URL prefix – když napíšeš /static/style.css, Flask ví kam se podívat

    # Registruj routy (cesty jako / nebo /quiz)
    # Import je až tady, aby se vyhnul "cyklickému importu" (routes.py importuje app, app importuje routes)
    from . import routes
    app.register_blueprint(routes.bp)  # Připoj blueprint 'main' – všechny routy z routes.py teď fungují

    # Inicializuj databázi při prvním spuštění
    db_path = 'app.db'  # Soubor databáze (SQLite)

    # app_context() = "běž tento kód uvnitř Flask aplikace"
    # Proč? Peewee potřebuje vědět, že pracuje s Flask appkou (jinak by nevěděl, kde je databáze)
    with app.app_context():
        create_tables()  # Voláno vždy – Peewee přidá chybějící tabulky/sloupce
        print("Databáze inicializována (tabulky vytvořeny).")

    return app  # Vrať hotovou aplikaci – teď ji můžeš spustit přes app.run()