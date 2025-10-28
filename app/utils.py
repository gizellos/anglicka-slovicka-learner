# app/utils.py
# Pomocné funkce pro aplikaci.
# Proč oddělený soubor? Aby routes.py zůstal přehledný – tam jsou jen routy, tady "nástroje".

from gtts import gTTS
from pathlib import Path
from flask import url_for, request
from app.models import Word, db

def generate_audio_url(word_english):
    """Vygeneruje MP3 soubor s výslovností slova a vrátí URL k němu.

    Jak to funguje:
    1. Zkontroluje, jestli MP3 už existuje ve static/audio/
    2. Pokud ne, použije gTTS (Google Text-to-Speech) pro vytvoření MP3
    3. Vrátí URL, kterou můžeš použít v <audio> tagu

    Args:
        word_english: Anglické slovo (např. 'hello')

    Returns:
        str: Plná URL k MP3 (např. 'http://127.0.0.1:5000/static/audio/hello.mp3')
        None: Pokud se vytvoření nepovedlo
    """
    # Vytvoř složku static/audio/, pokud neexistuje
    # Path = moderní způsob práce se soubory v Pythonu (lepší než string cesty)
    audio_dir = Path('static/audio')
    audio_dir.mkdir(parents=True, exist_ok=True)  # parents=True vytvoří i 'static', exist_ok=True ignoruje chybu "už existuje"

    # Cesta k MP3 souboru pro toto slovo
    audio_file = audio_dir / f"{word_english}.mp3"  # / spojí cestu: static/audio + hello.mp3

    # Pokud MP3 neexistuje, vygeneruj ho
    if not audio_file.exists():
        try:
            # gTTS vytvoří MP3 z textu
            # lang='en' = angličtina, slow=False = normální rychlost
            tts = gTTS(text=word_english, lang='en', slow=False)
            tts.save(str(audio_file))  # Ulož jako hello.mp3
            print(f"Audio pro '{word_english}' vytvořeno: {audio_file}")
        except Exception as e:
            # Pokud se něco pokazí (např. žádné internet), vypíše chybu a vrátí None
            print(f"Chyba při vytváření audio: {e}")
            return None

    # Vytvoř URL k MP3
    # url_for('static', filename='...') = Flask funkce pro cestu ke static souborům
    static_path = url_for('static', filename=f"audio/{word_english}.mp3")

    # request.host_url = základ URL (např. 'http://127.0.0.1:5000/')
    # rstrip('/') odstraní lomítko na konci, pak přidáme static_path
    full_url = request.host_url.rstrip('/') + static_path

    return full_url  # Vrátí celou URL (např. http://127.0.0.1:5000/static/audio/hello.mp3)