"""Aufgabe: Buchstaben zählen

Beschreibung: Zählt, wie oft jeder Buchstabe im Text vorkommt, und gibt ein Dictionary zurück. Groß/klein zählt gleich, Leerzeichen werden nicht gezählt.

Gelöst am: 2026-11-18
Hinweise: mit Konzept-Hinweisen (Dict anlegen, zwei Fälle, not in), 0 Heft-Tipps
Quelle: Übungsheft Kapitel 5 (Boss)
"""

def buchstaben_zaehlen(text):
    text = text.lower()
    anzahl = {}
    for buchstabe in text:
        if buchstabe == " ":
                    continue
        if buchstabe not in anzahl:
            anzahl[buchstabe] = 0
        anzahl[buchstabe] = anzahl[buchstabe] + 1
    return anzahl


if __name__ == "__main__":
    assert buchstaben_zaehlen("Anna") == {"a": 2, "n": 2}
    assert buchstaben_zaehlen("a b A") == {"a": 2, "b": 1}
    assert buchstaben_zaehlen("") == {}
    print("Alle Tests bestanden.")
