"""Aufgabe: Preis nachschlagen

Beschreibung: Gibt den Preis von artikel aus dem Dictionary preise zurück. Gibt es den Artikel nicht: None.

Gelöst am: 2026-11-04
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 5
"""

def preis_von(preise, artikel):
    if artikel in preise:
        return preise[artikel]
    else:
        return None


if __name__ == "__main__":
    assert preis_von({"Brot": 3.5, "Milch": 1.2}, "Brot") == 3.5
    assert preis_von({"Brot": 3.5}, "Kuchen") is None
    assert preis_von({}, "Brot") is None
    assert preis_von({"Croissant": 1.8}, "Croissant") == 1.8
    print("Alle Tests bestanden.")
