"""Aufgabe: Negative Zahlen zählen

Beschreibung: Gib zurück, wie viele Zahlen in der Liste kleiner als 0 sind.

Gelöst am: 2026-10-20
Quelle: Python-Übungsheft (Kapitel 1)
"""

def zaehle_negative(zahlen):
    negative_zahlen = 0
    for zahl in zahlen:
        if zahl < 0:
            negative_zahlen = negative_zahlen + 1
    return negative_zahlen


if __name__ == "__main__":
    assert zaehle_negative([-1, 2, -3]) == 2
    assert zaehle_negative([]) == 0
    assert zaehle_negative([0, 1, 2]) == 0
    assert zaehle_negative([-5]) == 1
    print("Alle Tests bestanden.")
