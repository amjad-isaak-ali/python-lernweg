"""Aufgabe: Erster und letzter Buchstabe

Beschreibung: Gibt den ersten und den letzten Buchstaben zusammen als Text zurück, bei leerem Text "".

Gelöst am: 2026-10-30
Hinweise: allein, 0 Tipps
Quelle: Übungsheft Kapitel 3
"""

def erster_und_letzter(text):
    if len(text) == 0:
        return ""
    neu = text[0] + text[-1]
    return neu


if __name__ == "__main__":
    assert erster_und_letzter("Hallo") == "Ho"
    assert erster_und_letzter("a") == "aa"
    assert erster_und_letzter("") == ""
    assert erster_und_letzter("Python") == "Pn"
    print("Alle Tests bestanden.")
