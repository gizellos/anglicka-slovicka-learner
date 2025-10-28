# update_requirements.py
# Skript pro aktualizaci requirements.txt – exportuje nainstalované balíčky z .venv.
# Proč? Aby se závislosti (např. peewee, flask) snadno instalovaly na novém PC (pip install -r).
# Spusť po instalaci nového modulu (např. pip install flask-login), aby byl seznam aktuální.

import subprocess
import sys

def update_requirements():
    """Aktualizuje requirements.txt z aktuálního .venv prostředí."""
    try:
        # Volání pip freeze přes python modul pro kompatibilitu s .venv
        result = subprocess.run([sys.executable, '-m', 'pip', 'freeze'],
                                capture_output=True, text=True, check=True)
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write(result.stdout)
        print("requirements.txt aktualizován úspěšně.")
    except subprocess.CalledProcessError as e:
        print(f"Chyba při spuštění pip freeze: {e}")
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == '__main__':
    update_requirements()