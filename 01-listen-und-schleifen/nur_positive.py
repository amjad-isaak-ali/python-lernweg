"""Aufgabe: Nur positive Zahlen

Beschreibung: Gib eine neue Liste mit allen Zahlen größer als 0 zurück.

Gelöst am: 2026-10-23
Quelle: Python-Übungsheft (Kapitel 1)
"""

def nur_positive(zahlen):
    positivezahlen = []
    for zahl in zahlen:
        if zahl > 0:
            positivezahlen.append(zahl)
    return positivezahlen


if __name__ == "__main__":
    assert nur_positive([-1, 0, 3, 5]) == [3, 5]
    assert nur_positive([]) == []
    assert nur_positive([-2, -7]) == []
    assert nur_positive([1]) == [1]
    print("Alle Tests bestanden.")
