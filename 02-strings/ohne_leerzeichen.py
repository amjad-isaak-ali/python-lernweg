"""Aufgabe: Ohne Leerzeichen

Beschreibung: Gibt den Text ohne Leerzeichen zurück.

Gelöst am: 2026-10-28
Hinweise: allein (Transfer, erster Versuch)
Quelle: Übungsheft (Kapitel 2)
"""

def ohne_leerzeichen(text):
    neu = ""
    for o in text:
        if o != " ":
            neu = neu + o
    return neu


if __name__ == "__main__":
    assert ohne_leerzeichen("a b c") == "abc"
    assert ohne_leerzeichen("Hallo Welt") == "HalloWelt"
    assert ohne_leerzeichen("") == ""
    assert ohne_leerzeichen("   ") == ""
    print("Alle Tests bestanden.")
