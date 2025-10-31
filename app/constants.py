# app/constants.py
# Centrální konstanty pro appku – importuj from app.constants import * kde potřebuješ.
# Proč? Zabrání duplicitám, usnadní refaktoring (změna na jednom místě).

from typing import Final
import os

# Cesty a soubory (absolutní cesty pro Windows/Linux kompatibilitu)
PROJECT_ROOT: Final[str] = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH: Final[str] = os.path.join(PROJECT_ROOT, 'app.db')
STATIC_AUDIO_DIR: Final[str] = os.path.join(PROJECT_ROOT, 'static', 'audio')
TEMPLATES_DIR: Final[str] = os.path.join(PROJECT_ROOT, 'templates')

# Učení/Algoritmus (pro spaced repetition a zobrazení)
KNOWLEDGE_LEVELS: Final[dict[int, str]] = {
    0: 'Neučil se',
    1: 'Začátečník',
    2: 'Problematický',
    3: 'Střední',
    4: 'Dobře',
    5: 'Perfektní'
}
SPACED_REPETITION_DAYS: Final[list[int]] = [1, 3, 7, 14, 30]  # Intervaly opakování v dnech (Ebbinghaus-inspired)

# UI/Výpisy (zprávy pro flash nebo šablony)
FLASH_MESSAGES: Final[dict[str, str]] = {
    'success_add_word': 'Slovíčko přidáno!',
    'error_add_word': 'Chyba při přidávání slovíčka.',
    'success_add_lesson': 'Lekce vytvořena!',
    'no_words': 'Žádná slovíčka v databázi – přidej nějaká!'
}

# API/Limity (pro Dictionary API a validace)
DICTIONARY_API_URL: Final[str] = 'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
REQUEST_TIMEOUT: Final[int] = 5  # Sekundy pro requests.get()
MAX_WORDS_PER_LESSON: Final[int] = 20  # Limit slovíček v jedné lekci
AUDIO_LANG: Final[str] = 'en-US'  # Pro gTTS