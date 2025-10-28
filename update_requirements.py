# update_requirements.py
# Skript pro aktualizaci requirements.txt – exportuje nainstalované balíčky z .venv.
# Proč? Aby se závislosti (např. peewee, flask) snadno instalovaly na novém PC (pip install -r).
# Spusť po instalaci nového modulu (např. pip install flask-login), aby byl seznam aktuální.

import subprocess  # Modul pro spuštění externích příkazů (jako volání pip z Pythonu)

"""Aktualizuje requirements.txt seznamem nainstalovaných balíčků.

    Args:
        Žádné (používá aktuální .venv).

    Returns:
        Žádné (přepíše soubor, vypíše zprávu).

    Notes:
        pip freeze: Exportuje všechny balíčky (jako 'peewee==3.17.0') do textu.
        stdout=open('w'): Přesměruje výstup do souboru (w = write, přepíše starý).
        Proč subprocess? Bezpečnější než os.system – zachytí chyby.
    """
subprocess.run(["python", "-m", "pip", "freeze"], stdout=open("requirements.txt", "w"))  # Spusť pip freeze – načte balíčky a zapíše do requirements.txt (přepíše)
print("requirements.txt aktualizován")  # Potvrzení – vypíše zprávu do konzole