"""Aufgabe: Quadratzahlen

Beschreibung: Gib eine neue Liste zurück, in der jede Zahl mit sich selbst malgenommen ist.

Gelöst am: 2026-10-23
Quelle: Python-Übungsheft (Kapitel 1)
"""

def quadrate(zahlen):
    malzwei = []
    for zahl in zahlen:
        zahl = zahl * zahl 
        malzwei.append(zahl)
    return malzwei


if __name__ == "__main__":
    assert quadrate([1, 2, 3]) == [1, 4, 9]
    assert quadrate([]) == []
    assert quadrate([-2, 0]) == [4, 0]
    assert quadrate([10]) == [100]
    print("Alle Tests bestanden.")
