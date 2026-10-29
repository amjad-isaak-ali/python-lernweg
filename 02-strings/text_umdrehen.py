"""Aufgabe: Text umdrehen

Beschreibung: Gibt den Text rückwärts zurück, ohne [::-1] und ohne reversed().

Gelöst am: 2026-10-29
Hinweise: allein (0 Tipps, erster Versuch)
Quelle: Übungsheft (Kapitel 2)
"""

def text_umdrehen(text):
    neu = ""
    for b in text:
        neu = b + neu
    return neu


if __name__ == "__main__":
    assert text_umdrehen("abc") == "cba"
    assert text_umdrehen("") == ""
    assert text_umdrehen("a") == "a"
    assert text_umdrehen("Anna") == "annA"
    print("Alle Tests bestanden.")
