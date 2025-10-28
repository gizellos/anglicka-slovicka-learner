# app/utils.py
# Pomocné funkce pro appku – utility pro audio generování atd.
# Proč oddělený soubor? Aby routes.py zůstal čistý (jen routy), utils pro "pomocníky".

from gtts import gTTS  # gTTS pro generování MP3 z textu
from pathlib import Path  # Pro cesty k souborům (standardní Python)
from flask import url_for, request  # url_for pro static URL, request pro host
from app.models import Word, db  # Import modelu a DB pro přístup k datům

def generate_audio_url(word_english):
    """Generuje US audio MP3 pro slovíčko a vrátí URL.

    Args:
        word_english (str): Anglické slovo (např. 'hello').

    Returns:
        str: Plná URL k MP3 v static/audio/ nebo None, pokud chyba.

    Notes:
        Uloží MP3 do static/audio/{word}.mp3 – první volání generuje, další vrátí existující.
        Lang='en' = US English.
        Použij request.host_url pro absolutní URL (řeší relativní problémy na Windowsu).
    """
    audio_dir = Path('static/audio')
    audio_dir.mkdir(parents=True, exist_ok=True)  # Vytvoř složku (včetně rodičovské 'static')
    audio_file = audio_dir / f"{word_english}.mp3"

    if not audio_file.exists():  # Generuj jen pokud neexistuje (ušetří čas)
        try:
            tts = gTTS(text=word_english, lang='en', slow=False)  # US English, normální rychlost
            tts.save(str(audio_file))  # Ulož MP3
            print(f"Audio pro '{word_english}' vygenerováno: {audio_file}")
        except Exception as e:
            print(f"Chyba generování audio: {e}")
            return None

    # Absolutní URL pro player (host + path)
    static_path = url_for('static', filename=f"audio/{word_english}.mp3")
    full_url = request.host_url.rstrip('/') + static_path
    return full_url
