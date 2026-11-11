"""Aufgabe: Was kostet der Einkauf?

Beschreibung: Rechnet aus, was der Einkauf kostet. einkauf ist eine Liste von Artikeln, preise ein Dictionary. Artikel ohne Preis werden übersprungen.

Gelöst am: 2026-11-10
Hinweise: 1 Heft-Tipp und Hinweise (not in statt == False)
Quelle: Übungsheft Kapitel 5
"""

def warenkorb_summe(einkauf, preise):
    summe = 0
    for artikel in einkauf:
        if artikel not in preise:
            continue
        summe = summe + preise[artikel]
    return summe


if __name__ == "__main__":
    assert warenkorb_summe(["Brot", "Milch"], {"Brot": 3, "Milch": 1}) == 4
    assert warenkorb_summe(["Brot", "Brot"], {"Brot": 2}) == 4
    assert warenkorb_summe(["Brot", "Kaffee", "Brot"], {"Brot": 3, "Milch": 1}) == 6
    assert warenkorb_summe([], {"Brot": 3}) == 0
    print("Alle Tests bestanden.")
