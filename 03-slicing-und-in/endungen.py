"""Aufgabe: Endungen für die Lieferliste

Beschreibung: Gibt von jedem Gebäcknamen die letzten n Buchstaben klein in einer neuen Liste zurück; leere Namen und Namen mit "#" am Anfang werden übersprungen.

Gelöst am: 2026-10-30
Hinweise: allein, ohne Hinweise, 8/8 im ersten Versuch
Quelle: VS Code Variante 14 (Transfer zu Variante 13)
"""

def endungen(namen, n):
    neu = []
    for name in namen:
        name = name.lower()
        if len(name) == 0:
            continue
        if name[0] == "#":
            continue
        neu.append(name[-n:])
    return neu


if __name__ == "__main__":
    assert endungen(["Brezel", "Stollen", "Suisse"], 3) == ["zel", "len", "sse"]
    assert endungen([], 2) == []
    assert endungen(["Croissant"], 4) == ["sant"]
    assert endungen(["Ei", "#Torte", "", "BROT"], 2) == ["ei", "ot"]
    assert endungen(["", "#Brot", "#"], 1) == []
    assert endungen(["Ei", "Tee", "Kuchen"], 5) == ["ei", "tee", "uchen"]
    assert endungen(["BAGUETTE", "tOAST", "Mohnschnecke"], 1) == ["e", "t", "e"]
    print("Alle Tests bestanden.")
