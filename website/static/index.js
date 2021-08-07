function settingSlider(numDecks, deckPen, numPlayers, modeSelect, countMethod) {
    fetch('/setting-slider', {
        method: 'POST',
        body: JSON.stringify(numDecks, deckPen, numPlayers, modeSelect, countMethod), // this line might be an error, vid does {{ noteId: noteId }}
    }).then((_res) => {
        window.location.href = "/";
    });
}
