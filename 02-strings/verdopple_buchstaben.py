"""Aufgabe: Buchstaben verdoppeln

Beschreibung: Gibt jeden Buchstaben des Textes doppelt zurück.

Gelöst am: 2026-10-28
Hinweise: allein
Quelle: Übungsheft (Kapitel 2)
"""

def verdopple_buchstaben(text):
    neu = ""
    for d in text:
        neu = neu + d + d
    return neu


if __name__ == "__main__":
    assert verdopple_buchstaben("abc") == "aabbcc"
    assert verdopple_buchstaben("Hi!") == "HHii!!"
    assert verdopple_buchstaben("") == ""
    print("Alle Tests bestanden.")
