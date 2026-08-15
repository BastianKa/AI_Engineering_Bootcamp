# Lernplan 0.2: Kontrollfluss (if/else, Schleifen)

**Phase:** 0 – Programmier-Grundlagen (siehe `ROADMAP.md`)
**Level:** Programmier-Anfänger, aufbauend auf Lektion 0.1
**Lernformat:** kurze Theorie, dann direkt kleine Übungen
**Endprodukt:** keine eigene Datei — Übungen als `phase0-programmierung/notebooks/0X_<thema>.py`

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
1. Mit `if` / `elif` / `else` Entscheidungen im Code treffen
2. Vergleichsoperatoren (`==`, `!=`, `<`, `>`, `<=`, `>=`) und logische Verknüpfungen (`and`, `or`, `not`) benutzen
3. Eine `while`-Schleife schreiben (wiederholen, solange eine Bedingung gilt)
4. Eine `for`-Schleife mit `range(...)` schreiben (eine bekannte Anzahl von Wiederholungen)

---

## 🧠 Kurz-Theorie

**if / elif / else** — Code wird nur ausgeführt, wenn eine Bedingung `True` ergibt:
```python
if bedingung:
    ...      # läuft, wenn bedingung True ist
elif andere_bedingung:
    ...      # läuft, wenn die erste False war, diese aber True ist
else:
    ...      # läuft, wenn keine der Bedingungen True war
```
Wichtig: Die Einrückung (4 Leerzeichen) ist in Python **Pflicht**, nicht nur Stil — sie legt fest, was zum Block gehört.

**Vergleiche & Verknüpfungen:**
`==` (gleich), `!=` (ungleich), `<`, `>`, `<=`, `>=` liefern immer `True` oder `False`. Mit `and`, `or`, `not` lassen sich mehrere Bedingungen kombinieren, z. B. `alter >= 18 and hat_ticket`.

**while-Schleife** — wiederholt, solange die Bedingung `True` ist:
```python
zaehler = 0
while zaehler < 5:
    print(zaehler)
    zaehler += 1   # Kurzform für zaehler = zaehler + 1
```
Achtung: Wenn sich die Bedingung nie ändert, läuft die Schleife endlos — die Zeile `zaehler += 1` ist hier entscheidend.

**for-Schleife mit range()** — für eine bekannte Anzahl an Durchläufen:
```python
for i in range(5):   # i läuft durch 0, 1, 2, 3, 4
    print(i)
```

---

## 💻 Übungen (der Reihe nach)

**Übung 1 – Gerade oder ungerade**
Frag mit `input()` nach einer Zahl, wandle sie in `int` um, und gib mit `if`/`else` aus, ob sie gerade oder ungerade ist. (Tipp: `zahl % 2` — der Rest bei Division durch 2 — ist `0` bei geraden Zahlen.)

**Übung 2 – Notenstufen**
Frag nach einer Punktzahl (0–100) und gib mit `if`/`elif`/`else` eine Note aus, z. B.: ≥90 → "Sehr gut", ≥75 → "Gut", ≥50 → "Bestanden", sonst → "Nicht bestanden".

**Übung 3 – while-Countdown**
Schreib eine `while`-Schleife, die von 10 runterzählt bis 1 (jede Zahl in einer eigenen Zeile ausgeben), und am Ende `"Start!"` ausgibt.

**Übung 4 – for-Schleife: Summe berechnen**
Berechne mit einer `for`-Schleife und `range(...)` die Summe aller Zahlen von 1 bis 100 (ohne die eingebaute Funktion `sum()` zu benutzen) und gib das Ergebnis aus.

---

## ✅ Erfolgskriterien

- [ ] Erklären können, warum Einrückung in Python Pflicht ist
- [ ] Den Unterschied zwischen `while` und `for` in eigenen Worten erklären können
- [ ] Alle 4 Übungen selbst gelöst

---

## Weiter mit Lektion 0.3

Sobald das sitzt: Funktionen (`def`, Parameter, Rückgabewerte) — Datei folgt danach.
