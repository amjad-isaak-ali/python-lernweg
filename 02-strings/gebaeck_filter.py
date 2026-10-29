"""Aufgabe: Gebäck-Filter

Beschreibung: Filtert aus einer Liste von Gebäcknamen die, die mit einem bestimmten Buchstaben anfangen (Groß-/Kleinschreibung egal).

Gelöst am: 2026-10-29
Hinweise: mit Konzept-Hinweisen (Index [0], Strings unveränderlich), Review-Punkte selbst umgesetzt
Quelle: VS Code (phase1)
"""

def gebaeck_filter(namen, buchstabe):
    neu = []
    buchstabe = buchstabe.lower()
    for gebaeck in namen:
        if buchstabe == gebaeck[0].lower():
            neu.append(gebaeck)
    return neu


if __name__ == "__main__":
    assert gebaeck_filter(["Croissant", "Suisse", "Brezel", "Ciabatta", "Seelen"], "s") == ["Suisse", "Seelen"]
    assert gebaeck_filter([], "b") == []
    assert gebaeck_filter(["Brezel"], "B") == ["Brezel"]
    assert gebaeck_filter(["Brezel", "Brioche", "Croissant"], "b") == ["Brezel", "Brioche"]
    assert gebaeck_filter(["croissant", "Croissant", "CIABATTA", "Brezel"], "C") == ["croissant", "Croissant", "CIABATTA"]
    assert gebaeck_filter(["Suisse", "Brezel"], "x") == []
    assert gebaeck_filter(["Brezel", "Suisse", "Seelen", "Stolle"], "S") == ["Suisse", "Seelen", "Stolle"]
    print("Alle Tests bestanden.")
