"""Aufgabe: Ohne Rand

Beschreibung: Gibt den Text ohne das erste und das letzte Zeichen zurück, bei zu kurzem Text "".

Gelöst am: 2026-10-30
Hinweise: erst Schleife mit Bug (Buchstabe statt Position), nach Erklärung mit Slicing gelöst
Quelle: Übungsheft Kapitel 3
"""

def ohne_rand(text):
    if len(text) <= 1:
        return ""
    return (text[1:-1])


if __name__ == "__main__":
    assert ohne_rand("Hallo") == "all"
    assert ohne_rand("ab") == ""
    assert ohne_rand("a") == ""
    assert ohne_rand("") == ""
    assert ohne_rand("[42]") == "42"
    print("Alle Tests bestanden.")
