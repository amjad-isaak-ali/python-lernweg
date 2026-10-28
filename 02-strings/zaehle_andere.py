"""Aufgabe: Andere Zeichen zählen

Beschreibung: Zählt die Zeichen im Text, die weder der gesuchte Buchstabe noch ein Leerzeichen sind (Groß-/Kleinschreibung egal).

Gelöst am: 2026-10-28
Hinweise: allein
Quelle: VS Code (phase1)
"""

def zaehle_andere(text, buchstabe):
    zaeler = 0
    text = text.lower()
    buchstabe = buchstabe.lower()
    for z in text:
        if z != buchstabe and z != " ":
            zaeler = zaeler + 1
    return zaeler


if __name__ == "__main__":
    assert zaehle_andere("Anna Bob", "a") == 5
    assert zaehle_andere("Hallo Welt", "L") == 6
    assert zaehle_andere("aAa", "a") == 0
    assert zaehle_andere("", "x") == 0
    assert zaehle_andere("   ", "a") == 0
    assert zaehle_andere("Ja, ja! Ach ja.", "J") == 9
    print("Alle Tests bestanden.")
