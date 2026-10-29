"""Aufgabe: Endet-mit-Filter

Beschreibung: Filtert aus einer Liste von Gebäcknamen die, die mit einem bestimmten Buchstaben enden (Groß-/Kleinschreibung egal).

Gelöst am: 2026-10-29
Hinweise: allein (Transfer, erster Versuch)
Quelle: VS Code (phase1)
"""

def endet_mit(namen, buchstabe):
    neu = []
    buchstabe = buchstabe.lower()
    for ende in namen:
        if buchstabe == ende[-1].lower():
            neu.append(ende)
    return neu


if __name__ == "__main__":
    assert endet_mit(["Brezel", "Stollen", "Suisse", "Croissant", "Baguette"], "e") == ["Suisse", "Baguette"]
    assert endet_mit([], "n") == []
    assert endet_mit(["Stollen"], "N") == ["Stollen"]
    assert endet_mit(["Brezel", "Stollen"], "x") == []
    assert endet_mit(["SuissE", "Brezel", "Stollen", "BAGUETTE"], "e") == ["SuissE", "BAGUETTE"]
    assert endet_mit(["Brot", "Toast", "Tee", "Eis"], "T") == ["Brot", "Toast"]
    assert endet_mit(["e", "E", "Ei", "Tee"], "e") == ["e", "E", "Tee"]
    print("Alle Tests bestanden.")
