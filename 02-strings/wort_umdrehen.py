"""Aufgabe: Wort umdrehen

Beschreibung: Gibt den Text rückwärts zurück, nur mit for-Schleife und +.

Gelöst am: 2026-10-28
Hinweise: mit Hinweis (Reihenfolge beim +)
Quelle: VS Code (phase1)
"""

def wort_umdrehen(text):
    neu = ""
    for u in text:
        neu = u + neu
    return neu


if __name__ == "__main__":
    assert wort_umdrehen("Teig") == "gieT"
    assert wort_umdrehen("") == ""
    assert wort_umdrehen("a") == "a"
    assert wort_umdrehen("Anna") == "annA"
    assert wort_umdrehen("Hefe Teig") == "gieT efeH"
    assert wort_umdrehen("123") == "321"
    print("Alle Tests bestanden.")
