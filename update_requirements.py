# update_requirements.py
# Skript pro aktualizaci requirements.txt – zaznamená všechny nainstalované balíčky.
# Proč? Když nainstaluju nový modul (pip install flask-login), musím ho přidat do requirements.txt,
# aby se dal nainstalovat na jiném PC přes: pip install -r requirements.txt

import subprocess
import sys

def update_requirements():
    """Aktualizuje requirements.txt podle aktuálně nainstalovaných modulů.

    Jak to funguje:
    1. Spustí příkaz 'pip freeze' (ukáže všechny nainstalované balíčky)
    2. Výstup uloží do requirements.txt
    """
    try:
        # subprocess.run() = spusť externí příkaz (jako v terminálu)
        # [sys.executable, '-m', 'pip', 'freeze'] = python -m pip freeze
        # Proč sys.executable? Aby použil Python z virtuálního prostředí (ne systémový Python)
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'freeze'],
            capture_output=True,  # Zachyť výstup do proměnné
            text=True,            # Vrať výstup jako string (ne bytes)
            check=True            # Pokud příkaz selže, vyvolá chybu
        )

        # Ulož výstup do souboru
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write(result.stdout)  # result.stdout = výstup z 'pip freeze'

        print("requirements.txt aktualizován úspěšně.")

    except subprocess.CalledProcessError as e:
        # Chyba při spuštění pip freeze (např. pip není nainstalovaný)
        print(f"Chyba při spuštění pip freeze: {e}")
    except Exception as e:
        # Jiná chyba (např. nemůžu zapsat do souboru)
        print(f"Chyba: {e}")

# Spusť funkci, když spustím tento soubor přímo
if __name__ == '__main__':
    update_requirements()