"""Aufgabe: Kommt das Wort vor?

Beschreibung: Gibt True zurück, wenn wort im satz vorkommt, Groß- und Kleinschreibung egal.

Gelöst am: 2026-10-30
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 3
"""

def enthaelt_wort(satz, wort):
    satz = satz.lower()
    wort = wort.lower()
    return wort in satz


if __name__ == "__main__":
    assert enthaelt_wort("Ich lerne Python", "python") is True
    assert enthaelt_wort("Hallo", "Welt") is False
    assert enthaelt_wort("", "a") is False
    assert enthaelt_wort("Abendschule", "SCHULE") is True
    print("Alle Tests bestanden.")
