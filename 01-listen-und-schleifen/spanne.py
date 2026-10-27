"""Aufgabe: Spanne einer Liste

Beschreibung: Größte minus kleinste Zahl, ohne max() und min(). Leere Liste: None.

Gelöst am: 2026-10-23
Quelle: Python-Übungsheft (Kapitel 1)
"""

def spanne(zahlen):
    if len(zahlen) == 0:
        return None
    diespanne = 0
    merkerklein = zahlen[0]
    merkergross = zahlen[0]
    for zahl in zahlen:
        if zahl > merkergross:
            merkergross = zahl
    for zahl in zahlen:
        if zahl < merkerklein:
            merkerklein = zahl
    diespanne = merkergross - merkerklein
    return diespanne


if __name__ == "__main__":
    assert spanne([3, 9, 2]) == 7
    assert spanne([5]) == 0
    assert spanne([]) is None
    assert spanne([-4, 4]) == 8
    print("Alle Tests bestanden.")
