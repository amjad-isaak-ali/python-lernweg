"""Aufgabe: Kürzel fürs Preisschild

Beschreibung: Gibt von jedem Gebäcknamen die ersten 3 Buchstaben GROSS in einer neuen Liste zurück; leere Namen werden übersprungen.

Gelöst am: 2026-10-30
Hinweise: ohne Hinweise zum Code, aber Konzept-Hinweis zu continue bekommen
Quelle: VS Code Variante 13
"""

def kuerzel(namen):
    neu = []
    for b in namen:
        if len(b) == 0:
            continue
        b = b.upper()
        neu.append(b[0:3])
    return neu


if __name__ == "__main__":
    assert kuerzel(["Brezel", "Stollen", "Suisse"]) == ["BRE", "STO", "SUI"]
    assert kuerzel([]) == []
    assert kuerzel(["Croissant"]) == ["CRO"]
    assert kuerzel(["Ei", "", "Brot"]) == ["EI", "BRO"]
    assert kuerzel(["", ""]) == []
    assert kuerzel(["baguette", "TOAST", "mIlchbroetchen"]) == ["BAG", "TOA", "MIL"]
    assert kuerzel(["Tee", "o", "Ab", "Kuchen"]) == ["TEE", "O", "AB", "KUC"]
    print("Alle Tests bestanden.")
