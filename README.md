# Plauderfy

Mein persönlicher, selbstgesteuerter Lernpfad vom Programmier-Anfänger zum AI Engineer — begleitet als strukturiertes Coding-Along mit [Claude Code](https://claude.com/claude-code).

Kein fertiges Kursmaterial zum Durchlesen, sondern Lernpläne, die Schritt für Schritt in echten Coding-Sessions umgesetzt werden: kurze Theorie, dann selbst schreiben, dann Feedback.

## Struktur

```
phase0-programmierung/        Python-Grundlagen (Variablen, Kontrollfluss, Funktionen, ...)
phase1-llm-fundamentals/      Wie LLMs funktionieren, erster Chatbot, Embeddings
phase2-retrieval-data/        RAG: Chunking, Vektor-Suche, Retrieval über eigene Dokumente
phase3-structured-outputs/    Function Calling, strukturierte Outputs
phase4-agents/                Multi-Agenten-Systeme (CrewAI)
phase5-production-evaluation/ Evaluation, Observability, Deployment
phase6-specialization/        Vertiefung nach Interesse
```

Jede Phase enthält:
- `lernplan_<schritt>_<thema>.md` — die eigentlichen Lernpläne (Theorie + Übungen)
- `notebooks/` — selbst gebaute Jupyter Notebooks / Code aus den Coding-Alongs

Der Gesamtüberblick steht in [`ROADMAP.md`](./ROADMAP.md), der aktuelle Lernstand in [`progress.md`](./progress.md).

## Voraussetzungen

- Python 3.11+
- Ein Editor mit Jupyter-Unterstützung (z. B. VS Code)
- Eigene API-Keys (z. B. OpenAI, ab Phase 4 zusätzlich Tavily) — werden lokal in einer **eigenen, nicht committeten** `.env`-Datei hinterlegt (siehe `.gitignore`). Im Repo selbst befinden sich keine Keys.

## Arbeitsweise

Die Lernpläne sind so geschrieben, dass sie direkt als Prompt für Claude Code dienen: Theorie kurz erklären lassen, Aufgaben selbst lösen, Code erst auf Nachfrage schreiben lassen. Details dazu in [`CLAUDE.md`](./CLAUDE.md).

---

*Lernprojekt, kein Produktivcode. Manche Beispiele referenzieren einen fiktiven Stand ("Juli 2026") für API-/Modellnamen — vor dem Nacharbeiten lohnt ein Blick auf die jeweils aktuelle Anbieter-Doku.*
