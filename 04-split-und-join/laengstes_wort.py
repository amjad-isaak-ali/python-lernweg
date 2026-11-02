"""Aufgabe: Längstes Wort

Beschreibung: Gibt das längste Wort zurück (bei Gleichstand das erste), bei leerem Satz None. Ohne max().

Gelöst am: 2026-11-02
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 4
"""

def laengstes_wort(satz):
    if len(satz) == 0:
        return None
    satz = satz.split()
    neu = ""
    for wort in satz:
        if len(wort) > len(neu):
            neu = wort
    return neu


if __name__ == "__main__":
    assert laengstes_wort("Ich lerne Python") == "Python"
    assert laengstes_wort("ab cd") == "ab"
    assert laengstes_wort("") is None
    assert laengstes_wort("Hallo") == "Hallo"
    assert laengstes_wort("eins drei zwei") == "eins"
    print("Alle Tests bestanden.")
