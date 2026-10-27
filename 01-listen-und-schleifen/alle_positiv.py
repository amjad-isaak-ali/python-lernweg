"""Aufgabe: Sind alle positiv?

Beschreibung: True, wenn alle Zahlen größer als 0 sind, sonst False. Leere Liste: True.

Gelöst am: 2026-10-27
Quelle: Python-Übungsheft (Kapitel 1)
"""

def alle_positiv(zahlen):
    if len(zahlen) == 0:
        return True
    merker = False 
    for zahl in zahlen:
        if zahl > 0:
            merker = True
        else:
            return False
    return merker


if __name__ == "__main__":
    assert alle_positiv([1, 2, 3]) is True
    assert alle_positiv([1, -2, 3]) is False
    assert alle_positiv([]) is True
    assert alle_positiv([0]) is False
    assert alle_positiv([5, 6, -1]) is False
    print("Alle Tests bestanden.")
