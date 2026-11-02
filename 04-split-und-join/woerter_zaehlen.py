"""Aufgabe: Wörter zählen

Beschreibung: Gibt zurück, wie viele Wörter im Satz stehen.

Gelöst am: 2026-10-31
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 4
"""

def woerter_zaehlen(satz):
    satz = satz.split()
    return len(satz)


if __name__ == "__main__":
    assert woerter_zaehlen("Ich lerne Python") == 3
    assert woerter_zaehlen("") == 0
    assert woerter_zaehlen("  viele   Leerzeichen  ") == 2
    assert woerter_zaehlen("Hallo") == 1
    print("Alle Tests bestanden.")
