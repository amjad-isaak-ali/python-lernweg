"""Aufgabe: An welcher Stelle?

Beschreibung: Gibt die Position zurück, an der ziel zum ersten Mal vorkommt (ab 0), sonst -1.

Gelöst am: 2026-10-28
Hinweise: Heft ohne Tipps, danach im Review aufgeräumt
Quelle: Übungsheft (Kapitel 1)
"""

def index_von(zahlen, ziel):
    if len(zahlen) == 0:
        return -1
    for pos in range(len(zahlen)):
        if ziel == zahlen[pos]:
            return pos
    return -1


if __name__ == "__main__":
    assert index_von([4, 7, 9], 7) == 1
    assert index_von([4, 7], 5) == -1
    assert index_von([], 3) == -1
    assert index_von([2, 2, 2], 2) == 0
    assert index_von([1, 2, 3], 3) == 2
    print("Alle Tests bestanden.")
