"""Aufgabe: Summe über einer Grenze

Beschreibung: Gib die Summe aller Zahlen zurück, die größer als grenze sind.

Gelöst am: 2026-10-20
Quelle: Python-Übungsheft (Kapitel 1)
"""

def summe_ueber(zahlen, grenze):
    alles_ueber = 0
    for zahl in zahlen:
        if zahl > grenze:
            alles_ueber = alles_ueber + zahl
    return alles_ueber


if __name__ == "__main__":
    assert summe_ueber([1, 5, 10], 4) == 15
    assert summe_ueber([], 3) == 0
    assert summe_ueber([2, 2], 2) == 0
    assert summe_ueber([-1, 0, 1], -1) == 1
    print("Alle Tests bestanden.")
