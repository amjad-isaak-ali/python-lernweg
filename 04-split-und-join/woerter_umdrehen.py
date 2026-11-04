"""Aufgabe: Wörter umdrehen

Beschreibung: Gibt den Satz mit den Wörtern in umgekehrter Reihenfolge zurück, getrennt durch je ein Leerzeichen.

Gelöst am: 2026-11-03
Hinweise: 1 Heft-Tipp und Hinweise (insert(0, ...) wiederentdeckt)
Quelle: Übungsheft Kapitel 4
"""

def woerter_umdrehen(satz):
    satz = satz.split()
    neu = []
    for wort in satz:
        neu.insert(0, wort)
    return " ".join(neu)


if __name__ == "__main__":
    assert woerter_umdrehen("eins zwei drei") == "drei zwei eins"
    assert woerter_umdrehen("") == ""
    assert woerter_umdrehen("Hallo") == "Hallo"
    assert woerter_umdrehen("a  b") == "b a"
    print("Alle Tests bestanden.")
