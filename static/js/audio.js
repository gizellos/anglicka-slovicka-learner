// static/js/audio.js – JS pro přehrávání audio na klik (US výslovnost)
function playAudio(wordEnglish) {
    // Vygeneruj URL k MP3 (dynamicky, jako v Jinja2)
    const audioUrl = `/static/audio/${wordEnglish}.mp3`;

    // Vytvoř Audio objekt a pusť
    const audio = new Audio(audioUrl);
    audio.play().catch(e => {
        console.error('Chyba přehrávání:', e);  // Debug v konzoli prohlížeče (F12)
        alert('Audio se nenačetlo – zkus refresh.');  // Fallback pro uživatele
    });

    // Volitelně: Přidej event listener pro stop na konci
    audio.addEventListener('ended', () => {
        console.log(`Dokončeno: ${wordEnglish}`);
    });
}