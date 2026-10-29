"""Aufgabe: Palindrom erkennen

Beschreibung: Gibt True zurück, wenn der Text vorwärts und rückwärts gleich ist (Groß-/Kleinschreibung egal), sonst False.

Gelöst am: 2026-10-29
Hinweise: allein (0 Tipps)
Quelle: Übungsheft (Kapitel 2)
"""

def ist_palindrom(text):
    text = text.lower()
    neu = ""
    merker = False
    for b in text.lower():
        neu = b + neu
    if neu == text:
        return True
    else:
        return False


if __name__ == "__main__":
    assert ist_palindrom("Anna") is True
    assert ist_palindrom("Hallo") is False
    assert ist_palindrom("") is True
    assert ist_palindrom("Otto") is True
    assert ist_palindrom("ab") is False
    print("Alle Tests bestanden.")
