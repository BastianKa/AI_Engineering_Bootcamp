# Lernplan 0.1: Variablen, Datentypen, print & input

**Phase:** 0 – Programmier-Grundlagen (siehe `ROADMAP.md`)
**Level:** kompletter Programmier-Anfänger
**Lernformat:** kurze Theorie, dann direkt kleine Übungen (kein Video nötig)
**Endprodukt:** keine eigene Datei — wir üben in einer Python-Konsole oder einem Scratch-Notebook `uebungen_p0.ipynb`

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
1. Erklären, was eine Variable ist
2. Die wichtigsten Datentypen unterscheiden: `str`, `int`, `float`, `bool`
3. Werte mit `print()` ausgeben und mit `input()` einlesen
4. Typumwandlungen durchführen (`int()`, `str()`, `float()`)

---

## 🧠 Kurz-Theorie

- **Variable** = ein benannter Speicherplatz für einen Wert, z. B. `alter = 28`
- Python braucht (anders als z. B. Java) keinen Typ vorab — der Typ ergibt sich automatisch aus dem Wert.
- `print(...)` gibt etwas auf dem Bildschirm aus.
- `input(...)` liest eine Eingabe des Nutzers ein — **immer als Text (`str`)**, auch wenn eine Zahl eingegeben wird.

---

## 💻 Übungen (der Reihe nach)

**Übung 1 – Variable & print**
Lege eine Variable `name` mit deinem Namen an und gib damit `"Hallo, <name>!"` aus.

**Übung 2 – Datentypen erkennen**
Lege drei Variablen an: eine ganze Zahl, eine Kommazahl, einen Wahrheitswert. Gib mit `type(...)` für jede den Typ aus.

**Übung 3 – input() und Typumwandlung**
Frage mit `input()` nach dem Geburtsjahr, wandle die Eingabe in eine Zahl um (`int()`) und berechne daraus näherungsweise das aktuelle Alter. Gib das Ergebnis aus.

**Übung 4 (Bonus)**
Was gibt `"3" + "4"` zurück, was `3 + 4`? Probier beides aus und erklär in eigenen Worten den Unterschied.

---

## ✅ Erfolgskriterien

- [ ] Erklären können, warum `input()` immer einen String zurückgibt
- [ ] Erklären können, was bei `"3" + 4` passiert und warum
- [ ] Alle 4 Übungen selbst gelöst (nicht nur gelesen)

---

## Weiter mit Lektion 0.2

Sobald das sitzt: Kontrollfluss (`if`/`else`, Schleifen) — Datei folgt, sobald wir hier fertig sind.
