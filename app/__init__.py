# app/__init__.py
# Tovární modul Flask appky – vytváří instanci appky s routami a inicializací.
# Proč továrna? Aby bylo snadné testovat/rozšiřovat (např. přidat config pro deploy).

from flask import Flask  # Import základní Flask třídy pro vytvoření appky
from .models import create_tables  # Import funkce pro vytvoření tabulek z models.py
import os  # Pro absolutní cesty (standardní Python)

def create_app():
    """Tovární funkce pro vytvoření Flask appky.

    Sestaví instanci s routami, blueprinty a inicializací DB.
    Volá se v main.py pro lokální spuštění nebo v wsgi.py pro deploy.

    Args:
        Žádné (používá defaulty; později přidej config='development').

    Returns:
        Flask: Hotová appka instance (s routami a DB).

    Notes:
        app_context(): 'Kontext' – umožňuje spuštění DB kódu uvnitř appky (jinak Peewee neví o Flasku).
        Pro deploy (PythonAnywhere): Nahraď run() WSGI konfigem.
    """
    app = Flask(__name__)  # Vytvoř prázdnou Flask instanci (__name__ = 'app' pro cesty k souborům)



    # Absolutní cesta k static z kořene projektu (řeší 404 na Windowsu)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Kořen (nad app/)
    app.static_folder = os.path.join(project_root, 'static')  # Plná cesta ke static/
    app.static_url_path = '/static'  # URL prefix (standard)


    # Načte soubor s routováním – import až zde, aby se vyhnul cyklickým importům
    from . import routes  # Relativní import: "z téže složky app/" (routes.py)
    app.register_blueprint(routes.bp)  # Registruj blueprint 'main' – připoj routy k appce

    # Inicializace DB: Vytvoř tabulky při spuštění appky (jen pokud DB neexistuje)
    db_path = 'app.db'  # Cesta k DB souboru (z models.py)

    with app.app_context():  # "Kontext" znamená "spusť to uvnitř appky" – Peewee potřebuje Flask prostředí pro DB
        if not os.path.exists(db_path):  # Kontrola: Pokud DB neexistuje, vytvoř tabulky
            create_tables()  # Volání z models.py – vytvoří tabulku 'words'
            print("DB tabulky vytvořeny poprvé!")  # Debug: Vidíš v konzoli, že to proběhlo
        else:
            print("DB už existuje – tabulky přeskočeny.")  # Debug: Pro klid duše

    return app  # Vrátí hotovou appku – připravenou na spuštění (run() v main.py)