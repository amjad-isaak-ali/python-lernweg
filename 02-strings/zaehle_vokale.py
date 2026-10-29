"""Aufgabe: Vokale zählen

Beschreibung: Zählt, wie viele Vokale (a, e, i, o, u) im Text stehen, egal ob groß oder klein.

Gelöst am: 2026-10-29
Hinweise: allein (0 Tipps)
Quelle: Übungsheft (Kapitel 2)
"""

def zaehle_vokale(text):
   text = text.lower()
   zaehler = 0
   for b in text:
       if b == "a" or b == "e" or b == "i" or b == "o" or b == "u":
           zaehler = zaehler + 1
   return zaehler


if __name__ == "__main__":
    assert zaehle_vokale("Hallo") == 2
    assert zaehle_vokale("") == 0
    assert zaehle_vokale("xyz") == 0
    assert zaehle_vokale("AEIOU") == 5
    assert zaehle_vokale("Banane") == 3
    print("Alle Tests bestanden.")
