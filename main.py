# main.py
# Vstupní bod aplikace – spouští Flask server lokálně.
# Když chceš spustit appku, napíšeš do terminálu: python main.py

from app import create_app

# Vytvoř Flask aplikaci pomocí tovární funkce
# create_app() vrátí hotový Flask objekt s routami a databází
app = create_app()

# if __name__ == '__main__':
# Co to znamená? "Spusť tento kód, jen když spouštím main.py přímo (ne když ho importuji)"
# Proč? Aby se server nespustil, když někdo udělá "from main import app"
if __name__ == '__main__':
    # app.run() spustí vývojový webový server
    # debug=True = automaticky restartuje server při změnách kódu a zobrazí chyby v prohlížeči
    app.run(debug=True)  # Server poběží na http://127.0.0.1:5000/