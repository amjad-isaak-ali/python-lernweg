"""Aufgabe: Liste umdrehen

Beschreibung: Gibt eine neue Liste in umgekehrter Reihenfolge zurück, ohne reverse(), reversed() und [::-1].

Gelöst am: 2026-10-29
Hinweise: allein (0 Tipps, erster Versuch)
Quelle: Übungsheft (Kapitel 1)
"""

def umdrehen(zahlen):
    umgedreht = []
    for z in zahlen:
        umgedreht.insert(0, z)
    return umgedreht


if __name__ == "__main__":
    assert umdrehen([1, 2, 3]) == [3, 2, 1]
    assert umdrehen([]) == []
    assert umdrehen([5]) == [5]
    assert umdrehen([1, 1, 2]) == [2, 1, 1]
    print("Alle Tests bestanden.")
