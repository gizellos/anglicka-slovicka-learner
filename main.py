# main.py
# Hlavní vstupní bod appky – spouští Flask server lokálně.
# Proč oddělený soubor? Aby byl vývoj modularní: app/ obsahuje logiku, main.py jen spuštění.
# Na serveru (PythonAnywhere) se to nahradí WSGI konfigem (bez run()).

from app import create_app  # Import tovární funkce z app/__init__.py – vytvoří Flask instanci

app = create_app()  # Vytvoř Flask objekt (nastaví routy, DB atd.) – appka je "postavená", ale ne spuštěná

if __name__ == '__main__':  # Podmínka: Spusť run() jen pokud běžíš main.py přímo (ne importován)
    """Spuštění lokálního serveru v debug módu.

    Args:
        Žádné (používá app z továrny).

    Returns:
        Žádné (spustí server na localhost:5000).

    Notes:
        debug=True: Automatický restart po změnách kódu, chyby v prohlížeči.
        Pro produkci (deploy): Použij WSGI bez run().
    """
    app.run(debug=True)  # Naštartuj webový server – naslouchá na http://127.0.0.1:5000
