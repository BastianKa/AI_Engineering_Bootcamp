# Lernplan 1B: Embeddings & Vektor-Ähnlichkeit (Brücke zwischen Lernplan 1 und 2)

**Format:** kurzer Zwischenschritt, kein eigenständiges Coding-Along-Projekt wie 1 und 2
**Ziel:** verstehen (nicht selbst bauen), was Chroma in Lernplan 2 automatisch für dich erledigt
**Stand der Code-Beispiele:** Juli 2026 (OpenAI Python SDK)

---

## Warum dieser Zwischenschritt?

Lernplan 1 hat Tokenisierung und Next-Token-Prediction erklärt. Lernplan 2 nutzt Embeddings + eine Vektor-Datenbank (Chroma), um passende Textstellen zu finden – aber Chroma erledigt das Berechnen und Vergleichen der Vektoren automatisch im Hintergrund. Ohne diesen Zwischenschritt würdest du RAG "benutzen", aber nicht verstehen, **warum** die richtigen Textstellen gefunden werden. Das holen wir hier kurz nach.

---

## 🎯 Lernziele

Danach kannst du:
1. Erklären, was ein Embedding ist (Text → Liste von Zahlen, die Bedeutung einfängt)
2. Erklären, was Cosine Similarity misst und wie sie berechnet wird
3. An einem konkreten Beispiel sehen: ähnliche Sätze haben eine hohe Similarity, unähnliche eine niedrige
4. Einordnen: Genau das übernimmt Chroma in Lernplan 2 automatisch für dich

---

## 📺 Video

**"Python + AI: Vector embeddings" – Pamela Fox (Microsoft, Cloud Advocate für Python)**
https://www.youtube.com/watch?v=ABLeB7JMWk0

Die Session ist ca. 45–60 Minuten und geht am Ende auch auf fortgeschrittenere Themen ein (Quantisierung, Dimensionsreduktion), die wir hier nicht brauchen. Für diesen Lernplan reicht der erste Teil: "Was sind Embeddings?", "Vector similarity space" und "Vector distance metrics" – danach kannst du stoppen.

---

## 🧠 Kurz-Theorie

**Was ist ein Embedding, noch mal konkret?**
Ein Embedding-Modell (z. B. `text-embedding-3-small` von OpenAI) wandelt einen Text in eine feste Liste von Zahlen um – bei diesem Modell 1536 Stück. Diese Zahlenliste ("Vektor") ist so gelernt, dass Texte mit ähnlicher Bedeutung auch ähnliche Vektoren bekommen.

**Wie misst man "ähnlich"? – Cosine Similarity**
Man kann sich jeden Vektor als Pfeil in einem (sehr hochdimensionalen) Raum vorstellen. Cosine Similarity misst den **Winkel** zwischen zwei solchen Pfeilen, nicht ihre Länge:

- Zeigen zwei Pfeile in exakt dieselbe Richtung → Cosine Similarity = 1 (maximal ähnlich)
- Stehen sie im rechten Winkel zueinander → Cosine Similarity ≈ 0 (kein Zusammenhang)
- Zeigen sie in entgegengesetzte Richtungen → Cosine Similarity = -1 (bei Text-Embeddings in der Praxis selten)

Die Formel dahinter:

```
cosine_similarity(a, b) = (a · b) / (‖a‖ × ‖b‖)
```

– das Skalarprodukt (`dot product`) der beiden Vektoren, geteilt durch das Produkt ihrer Längen (`norm`). Das klingt abstrakter, als es ist – im Beispiel unten siehst du die komplette Berechnung in drei Zeilen Code.

---

## 🔬 Vorgegebenes Beispiel (zum Ausführen & Verstehen)

Kopiere diese Zelle in ein Notebook (z. B. direkt in `chatbot.ipynb` aus Lernplan 1 als neue Zelle, oder in ein neues Notebook `embeddings_test.ipynb`) und führe sie aus:

```python
import numpy as np
from openai import OpenAI

client = OpenAI()  # nutzt denselben API-Key wie in Lernplan 1

saetze = [
    "Der Hund rannte über die Wiese.",
    "Ein Hund lief durchs Feld.",
    "Die Steuererklärung ist kompliziert.",
    "Ich mag Katzen und Hunde.",
]

# Embeddings für alle Sätze in einem API-Call holen
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=saetze,
)

# Nach Index sortieren, damit die Reihenfolge sicher zu "saetze" passt
daten_sortiert = sorted(response.data, key=lambda item: item.index)
vektoren = [np.array(item.embedding) for item in daten_sortiert]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Vergleiche Satz 0 ("Der Hund rannte über die Wiese.") mit allen anderen
print(f"Vergleichssatz: {saetze[0]}\n")
for i, satz in enumerate(saetze):
    sim = cosine_similarity(vektoren[0], vektoren[i])
    print(f"{sim:.3f}  ↔  {satz}")
```

**Was du beobachten solltest:**
- Satz 0 mit sich selbst → Similarity genau `1.000`
- Satz 0 vs. Satz 1 (auch ein Hund draußen) → hohe Similarity, meist über `0.6`
- Satz 0 vs. Satz 2 (Steuererklärung, völlig anderes Thema) → deutlich niedrigere Similarity
- Satz 0 vs. Satz 3 (Hunde werden erwähnt, aber anderer Satzbau/Kontext) → irgendwo dazwischen

Die genauen Zahlen können leicht variieren, das Muster (Thema "Hund draußen" liegt nah beieinander, "Steuererklärung" liegt weit weg) sollte aber immer sichtbar sein.

**Die Brücke zu Lernplan 2:**
Genau das, was du hier von Hand gemacht hast – Text in Vektoren umwandeln, dann per Cosine Similarity vergleichen – übernimmt Chroma automatisch, wenn du dort `collection.add(...)` und `collection.query(...)` aufrufst. Es ist keine Magie, sondern exakt diese Rechnung, nur für viele Chunks gleichzeitig und mit einer effizienten Suche statt einem manuellen Vergleich mit jedem einzelnen Vektor.

---

## ✅ Erfolgskriterien

- [ ] Erklären, was ein Embedding ist
- [ ] Erklären, was Cosine Similarity misst (Winkel zwischen Vektoren) und was der Wertebereich bedeutet
- [ ] Das Beispiel ausführen und begründen können, warum bestimmte Sätze näher beieinander liegen als andere
- [ ] Erklären können, was Chroma in Lernplan 2 automatisch übernimmt

---

## Weiter mit Lernplan 2

Sobald das sitzt, kannst du direkt mit Lernplan 2 (RAG mit Chunking + Chroma) weitermachen – dort wird aus diesem Prinzip ein vollständiges Retrieval-System für deine PDF.
