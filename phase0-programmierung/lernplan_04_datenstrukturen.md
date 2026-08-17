# Lernplan 0.4: Datenstrukturen (Listen, Dicts, Tupel)

**Phase:** 0 – Programmier-Grundlagen (siehe `ROADMAP.md`)
**Level:** Programmier-Anfänger, aufbauend auf Lektion 0.1–0.3
**Lernformat:** kurze Theorie, dann direkt kleine Übungen
**Endprodukt:** keine eigene Datei — Übungen als `phase0-programmierung/notebooks/1X_<thema>.py`

---

## 🎯 Lernziele

Nach dieser Lektion kannst du:
1. Eine Liste erstellen, durchlaufen und Elemente hinzufügen/entfernen
2. Auf Listen-Elemente per Index zugreifen (inkl. negativer Indizes)
3. Ein Dictionary erstellen und Werte per Key lesen/schreiben
4. Den Unterschied zwischen Liste, Dict und Tupel erklären (veränderbar vs. unveränderbar, Reihenfolge vs. Key-Zugriff)

---

## 🧠 Kurz-Theorie

**Liste (`list`)** — eine geordnete, veränderbare Sammlung von Werten:
```python
zahlen = [1, 2, 3]
zahlen.append(4)        # [1, 2, 3, 4]
print(zahlen[0])         # 1 (erstes Element)
print(zahlen[-1])        # 4 (letztes Element, negativer Index)

for zahl in zahlen:
    print(zahl)
```

**Dictionary (`dict`)** — Werte werden nicht über einen Index, sondern über einen **Key** angesprochen:
```python
person = {"name": "Anna", "alter": 30}
print(person["name"])    # "Anna"
person["stadt"] = "Berlin"   # neuen Key hinzufügen

for key, wert in person.items():
    print(key, wert)
```

**Tupel (`tuple`)** — wie eine Liste, aber **unveränderbar** (kann nach Erstellung nicht mehr geändert werden). Wird oft für feste Wertepaare genutzt:
```python
punkt = (3, 4)
print(punkt[0])   # 3
# punkt[0] = 5    # Fehler! Tupel sind unveränderbar
```

**Wann was?**
- Liste: geordnete Sammlung, die sich ändern soll (z. B. Einkaufsliste)
- Dict: Zuordnung Key → Wert (z. B. Name → Alter)
- Tupel: feste, unveränderbare Gruppe von Werten (z. B. Koordinaten)

---

## 💻 Übungen (der Reihe nach)

**Übung 1 – Liste befüllen und durchlaufen**
Erstelle eine Liste `namen` mit 3 Namen. Durchlaufe sie mit einer `for`-Schleife und gib jeden Namen mit `print` aus.

**Übung 2 – Liste verändern**
Nimm die Liste aus Übung 1. Füge mit `.append()` einen weiteren Namen hinzu, entferne einen Namen mit `.remove()` und gib die Liste danach aus.

**Übung 3 – Dictionary**
Erstelle ein Dict `person` mit den Keys `"name"`, `"alter"`, `"stadt"`. Gib alle drei Werte einzeln über den Key aus. Ändere danach den Wert von `"alter"` und gib das ganze Dict aus.

**Übung 4 – Kombination: Liste aus Dicts**
Erstelle eine Liste mit 2–3 Dicts (z. B. mehrere Personen wie in Übung 3). Durchlaufe die Liste mit einer `for`-Schleife und gib für jede Person Name und Alter aus.

---

## ✅ Erfolgskriterien

- [ ] Erklären können, wann man eine Liste, ein Dict oder ein Tupel nutzt
- [ ] Erklären können, warum Tupel unveränderbar sind und wofür das nützlich ist
- [ ] Alle 4 Übungen selbst gelöst

---

## 🔭 Ausblick

Sobald das sitzt: Lektion 0.5 — Fehler & Debugging (try/except, Fehler lesen).
