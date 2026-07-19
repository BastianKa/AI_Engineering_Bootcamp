# Lernplan 2: Simples RAG mit einer PDF-Datei (Chunking + Retrieval)

**Level:** Aufbauend auf Lernplan 1 (LLM-Grundlagen + Chatbot)
**Lernformat:** viele Videos, kurze Theorie-Häppchen
**Endprodukt:** ein Jupyter Notebook, das Fragen zu genau einer PDF-Datei beantwortet
**Stand der Code-Beispiele:** Juli 2026 (OpenAI Python SDK, ChromaDB, pypdf)

⚠️ **Bevor es losgeht:** Ich habe in deinem Projektordner noch keine PDF gefunden. Lade sie hoch (einfach ins Chat-Fenster ziehen), damit wir – bzw. Claude Code im Coding-Along – konkret damit arbeiten können.

---

## 🎯 Lernziele

Nach diesem Lernplan kannst du:
1. Erklären, was RAG ist und warum ein Chatbot es braucht, um über eigene/aktuelle Dokumente Bescheid zu wissen
2. Erklären, was Chunking ist, warum man Text in Stücke teilt und was Überlappung bringt
3. Erklären, wie Embeddings + Vektor-Ähnlichkeit beim Retrieval (Finden der passenden Textstücke) funktionieren
4. Ein simples RAG-System für **eine** PDF selbst bauen: PDF → Text → Chunks → Embeddings in einer Vektor-Datenbank → Retrieval → Antwort mit Kontext

---

## 🧰 Setup, bevor es losgeht

- Alles aus Lernplan 1 (Python, venv, `.env` mit `OPENAI_API_KEY`)
- Deine PDF-Datei im Projektordner (siehe Hinweis oben)
- Neue Pakete: `pypdf` (PDF-Text auslesen), `chromadb` (Vektor-Datenbank)

---

## 📺 Teil A – Grundlagen: Was ist RAG, was ist Chunking?

Schau dir vor dem Coding-Along an:

1. **"What is Retrieval-Augmented Generation (RAG)?" – IBM Technology** (ca. 7 Min, sehr verständlich)
   https://www.youtube.com/watch?v=T-D1OfcDW1M
   Kernidee: Statt dem Modell alles Wissen "einzutrainieren", gibt man ihm bei jeder Frage passende Textausschnitte aus echten Dokumenten mit – wie eine Prüfung, bei der man ein Buch aufschlagen darf.

Optional, wenn du beim Chunking tiefer einsteigen willst:
2. **"How to find the best chunking method for your RAG app" – Timescale**
   https://www.youtube.com/watch?v=5T3037ITATo

### Kurz-Theorie zum Nachlesen

**Warum reicht ein normaler Chatbot (aus Lernplan 1) nicht?**
Ein LLM kennt nur das, was in seinen Trainingsdaten stand – und was du ihm im Prompt mitschickst. Es weiß nichts von deiner PDF, außer du gibst ihm den Inhalt mit. Das Problem: Ein ganzes Dokument passt oft nicht ins Kontextfenster, und selbst wenn, wird die Antwort ungenauer, je mehr irrelevanter Text dabei ist.

**Die Lösung – drei Phasen:**

| Phase | Wann? | Was passiert? |
|---|---|---|
| **1. Chunking & Indexierung** | Einmalig, beim Start | Die PDF wird in kleine Textstücke ("Chunks") zerlegt, jedes Chunk wird in einen Embedding-Vektor umgewandelt und in einer Vektor-Datenbank gespeichert |
| **2. Retrieval** | Bei jeder Frage | Die Frage wird ebenfalls in einen Vektor umgewandelt, die Datenbank sucht die Chunks, deren Vektoren der Frage am ähnlichsten sind |
| **3. Generation** | Bei jeder Frage | Die gefundenen Chunks + die Frage werden gemeinsam ans LLM geschickt: "Beantworte die Frage anhand dieses Kontexts" |

**Warum Chunking überhaupt?**
- Embedding-Modelle sind für kurze bis mittlere Textstücke gedacht, nicht für 50 Seiten auf einmal
- Kleinere, thematisch fokussierte Chunks führen zu präziseren Treffern beim Retrieval – ein 50-Seiten-Chunk "trifft" auf fast jede Frage ein bisschen, aber nie genau

**Fixed-Size Chunking mit Überlappung (unsere Methode für diesen Lernplan):**
Der Text wird in gleich große Stücke geschnitten (z. B. 800 Zeichen), wobei sich aufeinanderfolgende Chunks am Rand leicht überlappen (z. B. 100 Zeichen). So geht ein Satz, der genau auf der Schnittstelle zwischen zwei Chunks liegt, nicht komplett verloren.

```
Text:     [....................................................]
Chunk 1:  [══════════════]
Chunk 2:          [══════════════]   ← überlappt mit Chunk 1
Chunk 3:                  [══════════════]
```

Das ist die einfachste Chunking-Methode und in der Praxis ein solider Startpunkt (typische Werte: 500–1000 Zeichen Chunk-Größe, 10–20 % Überlappung). Es gibt ausgefeiltere Methoden (satzbasiert, semantisch, nach Überschriften) – die heben wir uns für einen späteren Lernplan auf.

---

## 💻 Teil B – Praxis: RAG für deine PDF (Coding-Along mit Claude Code)

**Ziel:** Ein Notebook `rag_pdf.ipynb`, das deine PDF liest, in Chunks zerlegt, embedded und Fragen dazu beantwortet.

Aufgabenliste für das Coding-Along:

1. **Setup**
   - `pypdf` und `chromadb` installieren (aktuelle Versionen)
   - Bestehenden `.env`/OpenAI-Client aus Lernplan 1 wiederverwenden

2. **PDF-Text extrahieren**
   - Mit `pypdf.PdfReader` alle Seiten der PDF einlesen und zu einem langen String zusammenfügen
   - Zur Kontrolle: Gesamtlänge des Texts und die ersten paar hundert Zeichen ausgeben

3. **Chunking-Funktion schreiben**
   - Eine Funktion, die den Text in überlappende Stücke fester Größe zerlegt (siehe Skizze oben)
   - Ausprobieren: Wie viele Chunks entstehen bei 500 vs. 1000 Zeichen Chunk-Größe?

4. **Chroma-Collection anlegen und befüllen**
   - Einen `PersistentClient` erstellen (Daten bleiben zwischen Notebook-Neustarts erhalten)
   - Eine Collection mit OpenAI-Embedding-Funktion (`text-embedding-3-small`) anlegen
   - Alle Chunks mit eindeutigen IDs hinzufügen (Chroma berechnet die Embeddings dabei automatisch im Hintergrund)

5. **Retrieval isoliert testen**
   - Eine Beispielfrage stellen und dir **nur** die zurückgegebenen Chunks anschauen (noch ohne LLM-Antwort)
   - Prüfen: Ergeben die gefundenen Textstücke inhaltlich Sinn für die Frage?

6. **RAG zusammenbauen**
   - Gefundene Chunks + Frage in einen Prompt packen
   - Über die Responses API (aus Lernplan 1) eine Antwort generieren lassen, die sich nur auf den Kontext stützt

7. **Grenzfälle testen**
   - Eine Frage stellen, die eindeutig **nicht** in der PDF beantwortet wird
   - Beobachten, wie der Bot reagiert – und den System-Prompt so anpassen, dass er ehrlich sagt "steht nicht im Dokument", statt zu raten

### Technischer Hinweis zur Umsetzung (Stand Juli 2026)

**Chunking (reines Python, keine zusätzliche Bibliothek nötig):**
```python
def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks
```

**Chroma-Collection mit OpenAI-Embeddings:**
```python
import chromadb
from chromadb.utils import embedding_functions
import os

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-small",
)

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="pdf_chunks",
    embedding_function=openai_ef,
)

collection.add(
    documents=chunks,
    ids=[f"chunk-{i}" for i in range(len(chunks))],
)
```

**Retrieval:**
```python
ergebnisse = collection.query(query_texts=[frage], n_results=3)
gefundene_chunks = ergebnisse["documents"][0]
```

**Generation mit Kontext (Responses API, wie in Lernplan 1):**
```python
kontext = "\n\n---\n\n".join(gefundene_chunks)

antwort = client.responses.create(
    model="gpt-5.6",
    instructions=(
        "Beantworte die Frage ausschließlich anhand des gegebenen Kontexts. "
        "Wenn die Antwort nicht im Kontext steht, sag ehrlich, dass du es "
        "aus dem Dokument nicht beantworten kannst."
    ),
    input=f"Kontext:\n{kontext}\n\nFrage: {frage}",
)
print(antwort.output_text)
```

Hinweis zum Embedding-Modell: `text-embedding-3-small` ist (Stand Juli 2026) weiterhin OpenAIs empfohlenes Standardmodell für die meisten Retrieval-Anwendungsfälle – günstig und gut genug für dieses Projekt. Für höchste Genauigkeit gäbe es `text-embedding-3-large`, das brauchen wir hier aber nicht.

---

## ✅ Erfolgskriterien – das solltest du danach können

- [ ] Erklären, was RAG von einem normalen Chatbot (Lernplan 1) unterscheidet
- [ ] Erklären, warum Chunking nötig ist und was die Überlappung bringt
- [ ] Ein Notebook vorzeigen, das eine echte Frage zu deiner PDF korrekt beantwortet
- [ ] Erklären, was passiert (und was passieren sollte), wenn die Antwort nicht im Dokument steht

---

## 🤖 So startest du das Coding-Along mit Claude Code

> Hier ist mein Lernplan (`lernplan_2_rag_pdf_chunking.md`), er baut auf Lernplan 1 auf. Ich bin weiterhin Python-Anfänger. Geh mit mir Schritt für Schritt durch Teil B. Erkläre kurz, bevor wir jeden Schritt umsetzen, lass mich aber selbst tippen und frag nach, bevor du Code für mich schreibst. Die PDF, mit der wir arbeiten, liegt unter [Pfad einfügen].

---

## 🔭 Ausblick auf Lernplan 3

Mögliche Richtungen – sag Bescheid, was dich reizt:
- Mehrere Dokumente / einen ganzen Ordner statt nur einer PDF
- Bessere Chunking-Strategien (satzbasiert oder semantisch statt fester Größe)
- Quellenangaben (aus welcher Seite/welchem Abschnitt stammt die Antwort?)
- Re-Ranking der gefundenen Chunks für noch bessere Treffer
