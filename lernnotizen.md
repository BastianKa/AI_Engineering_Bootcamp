# Lernnotizen

Dokumentiert jede gelöste Übung mit Aufgabe, Lösung und kurzer Erklärung — nicht nur, wenn es einen idiomatischeren Weg gibt, sondern grundsätzlich, was die Lösung macht und warum. Neueste Einträge unten.

---

## Phase 0.1 – Übung 1: Variable & print

**Aufgabe:** Lege eine Variable `name` mit deinem Namen an und gib damit `"Hallo, <name>!"` aus.

**Lösung:**
```python
name = "Max Mustermann"
print("Hallo, " + name + "!")
```
Variable `name` speichert einen String, `print` gibt ihn per `+`-Verkettung mit fixem Text aus.

**Idiomatischer (f-string):**
```python
print(f"Hallo, {name}!")
```
**Warum besser:** Kürzer, kein manuelles `+`-Verketten mehrerer Werte, weniger fehleranfällig (z. B. vergisst man leicht ein Leerzeichen oder `str()` bei Nicht-Strings). f-strings sind seit Python 3.6 der Standard-Weg für String-Formatierung.

---

## Phase 0.1 – Übung 2: Datentypen erkennen

**Aufgabe:** Lege drei Variablen an — eine ganze Zahl, eine Kommazahl, einen Wahrheitswert — und gib mit `type(...)` für jede den Typ aus.

**Lösung:**
```python
zahl = 42
kommazahl = 1.5
wahrheitswer = True

print("Typ von zahl:", typ_zahl)          # <class 'int'>
print("Typ von kommazahl:", typ_kommazahl) # <class 'float'>
print("Typ von wahrheitswer:", typ_wahrheitswert) # <class 'bool'>
```
`type(...)` gibt für jeden Wert die Klasse zurück, die Python automatisch anhand der Schreibweise erkennt: ohne Komma → `int`, mit Komma → `float`, `True`/`False` → `bool`. Kein manuelles Typ-Deklarieren nötig.

---

## Phase 0.1 – Übung 3: input() und Typumwandlung

**Aufgabe:** Frag mit `input()` nach dem Geburtsjahr, wandle die Eingabe in eine Zahl um (`int()`), und berechne daraus näherungsweise das aktuelle Alter. Gib das Ergebnis aus.

**Lösung:**
```python
eingabe = input("In welchem Jahr hast du Geburtstag?")
geburtsjahr = int(eingabe)
alter = 2026 - geburtsjahr
print("Du bist ungefähr", alter, "Jahre alt.")
```
`input()` liefert **immer einen String** — deshalb erst `int(...)`, bevor man damit rechnen kann. `input("Text")` zeigt den Text direkt vor dem Eingabe-Cursor an (eine Zeile statt zwei), spart ein separates `print()`.

---

## Phase 0.1 – Übung 4 (Bonus): `"3"+"4"` vs. `3+4`

**Aufgabe:** Was gibt `"3" + "4"` zurück, was `3 + 4`? Probier beides aus und erklär in eigenen Worten den Unterschied.

**Lösung:**
```python
print("3"+"4")   # "34" – String-Verkettung
print(3+4)        # 7   – echte Addition
```
Mit Anführungszeichen sind es Strings → `+` verkettet Text statt zu addieren. Ohne Anführungszeichen sind es Zahlen → `+` rechnet.

**Stolperfalle dabei:** `f"3""4"` sieht aus wie ein f-string-Trick, ist aber keiner — das ist automatische Verkettung zweier direkt nebeneinanderstehender String-Literale (`"3""4"` → `"34"`), das `f` davor bewirkt hier nichts, weil kein `{...}`-Platzhalter drin ist. Echter f-string-Einsatz braucht Variablen/Ausdrücke in `{}`:
```python
a, b = "3", "4"
print(f"{a}{b}")   # → "34", diesmal wirklich über Interpolation
```

---

## Phase 0.2 – Übung 1: Gerade oder ungerade

**Aufgabe:** Frag mit `input()` nach einer Zahl, wandle sie in `int` um, und gib mit `if`/`else` aus, ob sie gerade oder ungerade ist.

**Lösung:**
```python
eingabe = input("Gib eine zahl ein: ")
zahl = int(eingabe)
if zahl % 2 == 0:
    print(f"{zahl} ist eine GERADE Zahl.")
else:
    print(f"{zahl} ist eine UNGERADE Zahl.")
```
`%` (Modulo) liefert den Rest einer Division. Rest `0` bei Division durch 2 → gerade Zahl, sonst ungerade. `if`/`else` deckt beide Fälle vollständig ab.

---

## Phase 0.2 – Übung 2: Notenstufen

**Aufgabe:** Frag nach einer Punktzahl (0–100) und gib mit `if`/`elif`/`else` eine Note aus: ≥90 → "Sehr gut", ≥75 → "Gut", ≥50 → "Bestanden", sonst → "Nicht bestanden".

**Lösung (nach Bugfix):**
```python
if zahl < 0 or zahl > 100:
    print("Die Zahl liegt nicht zwischen 0 und 100!")
elif zahl >= 90:
    print("Sehr gut")
elif zahl >= 75:
    print("Gut")
elif zahl >= 50:
    print("Bestanden")
else:
    print("Nicht bestanden")
```
`elif`-Kette prüft Bedingungen der Reihe nach von oben nach unten, der erste Treffer gewinnt. **Wichtiger Fehler in der ersten Version:** das abschließende `else` fehlte — Werte wie `30` oder `0`, die keine der `elif`-Bedingungen erfüllten, erzeugten dadurch gar keine Ausgabe. Ohne `else` deckt eine `elif`-Kette nur die explizit genannten Fälle ab, nicht automatisch "alles andere".

**Zusätzlich idiomatischer:** `zahl < 0` und `zahl > 100` zu einer Bedingung mit `or` zusammengefasst, statt sie getrennt (und mit doppelter Fehlermeldung) an zwei Stellen der Kette zu prüfen — erst validieren, dann bewerten, statt eine Validierung mitten in der Noten-Logik zu verstecken.

---

## Phase 0.2 – Übung 3: while-Countdown

**Aufgabe:** Schreib eine `while`-Schleife, die von 10 runterzählt bis 1 (jede Zahl in einer eigenen Zeile), und am Ende `"Start!"` ausgibt.

**Finale Lösung:**
```python
zahl = 10
while zahl > 0:
    print(zahl)
    zahl = zahl - 1
else:
    print("Start!")
```
`print` läuft **vor** dem Dekrement, deshalb wird der Startwert `10` korrekt mit ausgegeben; Schleife läuft, solange `zahl > 0`.

**Zwei Bugs auf dem Weg dorthin (zur Erinnerung):**
1. `print({zahl})` (ohne `f`) erzeugt ein **Set**, keine Zahl-Ausgabe — `{...}` ohne `f`-Präfix ist Set-Syntax, kein Platzhalter. Fix: einfach `print(zahl)`.
2. Erster Versuch hatte `zahl = zahl - 1` **vor** `print(zahl)` — dadurch fehlte die `10` in der Ausgabe. Zwischenlösung war, bei `11` statt `10` zu starten (funktioniert, aber Workaround); die sauberere Lösung ist, `print` vor das Dekrement zu setzen (siehe oben).

---

## Phase 0.2 – Übung 4: for-Schleife, Summe berechnen

**Aufgabe:** Berechne mit einer `for`-Schleife und `range(...)` die Summe aller Zahlen von 1 bis 100 (ohne `sum()`) und gib das Ergebnis aus.

**Lösung:**
```python
summe = 0
for i in range(101):
    summe += i
print(summe)   # 5050
```
`summe` startet bei `0`, in jedem Durchlauf wird `i` addiert (`+=` ist Kurzform für `summe = summe + i`). `range(101)` erzeugt `0` bis `100`; die `0` verfälscht die Summe nicht (addiert nichts), daher stimmt `5050`.

**Zwei Bugs auf dem Weg dorthin:**
1. Erster Versuch: `range(100)` (also `0`–`99`) → Ergebnis `4950` statt `5050`, weil die `100` fehlte.
2. Erster Versuch: `print(summe)` **innerhalb** der Schleife → gab die Zwischensumme 100-mal aus statt nur einmal am Ende. Fix: `print` auf die Einrückungsebene der Schleife selbst (also eine Ebene raus).

**Noch etwas präziser:** `range(1, 101)` statt `range(101)` — trifft exakt "Zahlen von 1 bis 100", auch wenn `range(101)` wegen der neutralen `0` zum selben Ergebnis kommt.

---

## Phase 0.3 – Übung 1: Einfache Funktion

**Aufgabe:** Schreib eine Funktion `begruessen(name)`, die `"Hallo, <name>!"` ausgibt (mit `print`, kein `return` nötig). Ruf sie danach mit zwei verschiedenen Namen auf.

**Lösung:**
```python
def begruessung(name):
    print(f"Hallo, {name}!")

begruessung("Max")
begruessung("Fritz")
```
`def` definiert die Funktion (Code läuft noch nicht), erst der Aufruf `begruessung("Max")` führt den Funktionskörper mit `name="Max"` aus. Kein `return`, weil hier nichts weiterverarbeitet werden muss — reines Anzeigen reicht.

---

## Phase 0.3 – Übung 2: Funktion mit Rückgabewert

**Aufgabe:** Schreib eine Funktion `addiere(a, b)`, die die Summe **zurückgibt** (mit `return`, nicht `print`). Speichere das Ergebnis in einer Variable und gib die Variable danach mit `print` aus.

**Lösung:**
```python
def addiere(a, b):
    summe = a + b
    return summe

meine_summe = addiere(2, 5)
print(meine_summe)   # 7
```
`return summe` gibt den Wert an die Aufrufstelle zurück, `addiere(2, 5)` liefert dadurch `7`, das in `meine_summe` gespeichert und danach ausgegeben wird. Anders als bei reinem `print` in der Funktion kann der Wert hier weiterverwendet werden (z. B. für weitere Berechnungen).

---

## Phase 0.3 – Übung 3: Default-Parameter

**Aufgabe:** Schreib eine Funktion `potenz(basis, exponent=2)`, die `basis` hoch `exponent` zurückgibt. Ruf sie einmal nur mit `basis` auf (nutzt den Default `2`) und einmal mit beiden Parametern.

**Lösung:**
```python
def potenz(basis, exponent=2):
    ergebnis = basis**exponent
    return ergebnis

mein_ergebnis = potenz(4)      # 16  – nutzt Default exponent=2
print(mein_ergebnis)

mein_ergebnis = potenz(4, 4)   # 256 – überschreibt den Default
print(mein_ergebnis)
```
`exponent=2` in der Funktionssignatur ist der Default — wird beim Aufruf kein zweiter Wert übergeben, gilt automatisch `2`. Wird ein zweiter Wert übergeben (`potenz(4, 4)`), überschreibt der den Default für diesen Aufruf.

---

## Phase 0.3 – Übung 4: Kombination mit if

**Aufgabe:** Schreib eine Funktion `ist_gerade(zahl)`, die `True` zurückgibt, wenn `zahl` gerade ist, sonst `False`. Ruf sie mit ein paar Zahlen auf und gib das Ergebnis jeweils aus.

**Lösung:**
```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

test_werte = [3, 4, 5, 6]
for t in test_werte:
    abfrage = ist_gerade(t)
    print(f"Ist {t} gerade? {abfrage}")
```
`if`/`else` gibt direkt `True` oder `False` zurück (Rückgabewert einer Funktion muss kein Text sein — auch Wahrheitswerte gehen). Statt die Funktion einzeln mehrfach aufzurufen, wurden die Testwerte in einer Liste `test_werte` gesammelt und per `for`-Schleife automatisch durchprobiert — Vorgriff auf Listen (Lektion 0.4).

**Kürzer ginge außerdem:** `return zahl % 2 == 0` allein reicht — der Vergleich `zahl % 2 == 0` ist bereits `True` oder `False`, das `if`/`else` drumherum ist nicht nötig.
