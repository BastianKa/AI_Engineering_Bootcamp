# Lernplan 0.3: Funktionen (def, Parameter, Rückgabewerte)

**Phase:** 0 – Programmier-Grundlagen (siehe `ROADMAP.md`)
**Level:** Programmier-Anfänger, aufbauend auf Lektion 0.1 und 0.2
**Lernformat:** kurze Theorie, dann direkt kleine Übungen
**Endprodukt:** keine eigene Datei — Übungen als `phase0-programmierung/notebooks/0X_<thema>.py`

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
1. Eine eigene Funktion mit `def` definieren und aufrufen
2. Parameter an eine Funktion übergeben
3. Den Unterschied zwischen `return` (Wert zurückgeben) und `print` (nur anzeigen) erklären
4. Einen Default-Wert für einen Parameter festlegen

---

## 🧠 Kurz-Theorie

**Warum Funktionen?** Code, den man mehrfach braucht, schreibt man einmal als Funktion und ruft sie dann beliebig oft auf — statt denselben Code immer wieder zu kopieren.

```python
def begruessen(name):
    print(f"Hallo, {name}!")

begruessen("Anna")   # Aufruf mit Parameter "Anna"
begruessen("Ben")    # derselbe Code, andere Eingabe
```

**`return` vs. `print`** — der wichtigste Stolperstein am Anfang:
- `print(...)` zeigt nur etwas auf dem Bildschirm — der Wert geht danach verloren, du kannst ihn nicht weiterverwenden.
- `return ...` gibt einen Wert an die Stelle zurück, wo die Funktion aufgerufen wurde — du kannst ihn in einer Variable speichern und weiterverarbeiten.

```python
def addiere(a, b):
    return a + b

ergebnis = addiere(3, 4)   # ergebnis = 7, kann weiterverwendet werden
print(ergebnis * 2)        # 14
```

Würde `addiere` stattdessen nur `print(a + b)` machen, wäre `ergebnis` danach `None` — die Funktion hätte zwar etwas angezeigt, aber nichts zum Weiterrechnen zurückgegeben.

**Default-Werte** — ein Parameter kann einen Standardwert bekommen, der gilt, wenn beim Aufruf nichts übergeben wird:
```python
def begruessen(name, sprache="de"):
    if sprache == "de":
        print(f"Hallo, {name}!")
    else:
        print(f"Hello, {name}!")

begruessen("Anna")            # nutzt sprache="de" automatisch
begruessen("Ben", "en")       # überschreibt den Default
```

---

## 💻 Übungen (der Reihe nach)

**Übung 1 – Einfache Funktion**
Schreib eine Funktion `begruessen(name)`, die `"Hallo, <name>!"` ausgibt (mit `print`, kein `return` nötig). Ruf sie danach mit zwei verschiedenen Namen auf.

**Übung 2 – Funktion mit Rückgabewert**
Schreib eine Funktion `addiere(a, b)`, die die Summe **zurückgibt** (mit `return`, nicht `print`). Speichere das Ergebnis in einer Variable und gib die Variable danach mit `print` aus.

**Übung 3 – Default-Parameter**
Schreib eine Funktion `potenz(basis, exponent=2)`, die `basis` hoch `exponent` zurückgibt (Tipp: `**` ist der Potenz-Operator in Python). Ruf sie einmal nur mit `basis` auf (nutzt den Default `2`) und einmal mit beiden Parametern.

**Übung 4 – Kombination mit if**
Schreib eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt, wenn `zahl` gerade ist, sonst `False` (nutze `%` wie in Lektion 0.2). Ruf sie mit ein paar Zahlen auf und gib das Ergebnis jeweils aus.

---

## ✅ Erfolgskriterien

- [ ] Erklären können, was der Unterschied zwischen `return` und `print` in einer Funktion ist
- [ ] Erklären können, wozu Default-Parameter gut sind
- [ ] Alle 4 Übungen selbst gelöst

---

## Weiter mit Lektion 0.4

Sobald das sitzt: Datenstrukturen (Listen, Dicts, Tupel) — Datei folgt danach.
