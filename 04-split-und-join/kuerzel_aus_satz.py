"""Aufgabe: Kürzel aus einem Satz

Beschreibung: Bildet ein Kürzel aus den Anfangsbuchstaben aller Wörter, immer groß geschrieben. Die Funktion heißt kuerzel(satz) und ist eine andere Aufgabe als kuerzel.py in 03-slicing-und-in.

Gelöst am: 2026-11-02
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 4
"""

def kuerzel(satz):
    satz = satz.split()
    neu = ""
    for wort in satz:
        neu = neu + wort[0].upper()
    return neu


if __name__ == "__main__":
    assert kuerzel("Abend real schule") == "ARS"
    assert kuerzel("fachinformatiker für systemintegration") == "FFS"
    assert kuerzel("") == ""
    assert kuerzel("Köln") == "K"
    print("Alle Tests bestanden.")
