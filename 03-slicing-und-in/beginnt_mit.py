"""Aufgabe: Beginnt mit ...

Beschreibung: Gibt True zurück, wenn text mit anfang beginnt (Groß/klein zählt), ohne startswith().

Gelöst am: 2026-10-30
Hinweise: erste Fassung um die Tests herum gebaut (selbst zugegeben), nach Erklärung sauber neu
Quelle: Übungsheft Kapitel 3
"""

def beginnt_mit(text, anfang):
    if anfang == text[0:len(anfang)]:
        return True
    else:
        return False


if __name__ == "__main__":
    assert beginnt_mit("Hallo", "Ha") is True
    assert beginnt_mit("Hallo", "ha") is False
    assert beginnt_mit("Hi", "Hallo") is False
    assert beginnt_mit("abc", "") is True
    assert beginnt_mit("Python", "Python") is True
    print("Alle Tests bestanden.")
