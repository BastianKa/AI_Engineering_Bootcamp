# AI Engineer Curriculum – Roadmap

Persönlicher Lernpfad vom kompletten Programmier-Anfänger zum AI Engineer. Diese Datei ist der Überblick über alle Phasen. Der aktuelle Stand steht in `progress.md` — die wird bei jeder Session aktualisiert, damit wir nicht jedes Mal neu erklären müssen, wo wir stehen.

## Struktur

Jede Phase hat einen eigenen Ordner: `phase<N>-<thema>/`. Darin liegen die Lernplan-Dateien (`lernplan_<Schrittnummer>_<thema>.md`), die wir Schritt für Schritt im Coding-Along durcharbeiten, sowie ein `notebooks/`-Unterordner für alles, was du selbst baust (Notebooks, Scratch-Code) — Lerninhalt und eigener Code bleiben so getrennt.

Arbeitsmodus siehe CLAUDE.md: kurz erklären → selbst probieren lassen → erst auf Nachfrage Code schreiben.

## Phase 0 – Programmier-Grundlagen (Python)
`phase0-programmierung/`
Startpunkt für komplette Anfänger. Ohne das hier ergibt der Rest keinen Sinn.
- 0.1 Variablen, Datentypen, print/input → `lernplan_01_variablen_datentypen.md`
- 0.2 Kontrollfluss (if/else, Schleifen) → `lernplan_02_kontrollfluss.md`
- 0.3 Funktionen → `lernplan_03_funktionen.md`
- 0.4 Datenstrukturen (Listen, Dicts, Tupel) → `lernplan_04_datenstrukturen.md`
- 0.5 Fehler & Debugging (try/except, Fehler lesen) — noch zu schreiben
- 0.6 Terminal, venv, pip, Git-Basics — noch zu schreiben
- 0.7 Miniprojekt zum Abschluss (kombiniert alles oben) — noch zu schreiben

## Phase 1 – LLM Fundamentals
`phase1-llm-fundamentals/`
- 1.1 Wie funktioniert ein LLM + erster Chatbot → `lernplan_01_llm_grundlagen_chatbot.md` (bestehend)
- 1.2 Embeddings & Cosine Similarity → `lernplan_02_embeddings_cosine_similarity.md` (bestehend)

## Phase 2 – Retrieval & Data
`phase2-retrieval-data/`
- 2.1 RAG über eine PDF (Chunking, Chroma) → `lernplan_01_rag_pdf_chunking.md` (bestehend)
- 2.2 RAG Advanced (mehrere Dokumente, besseres Chunking, Quellenangaben, Re-Ranking) — noch zu schreiben

## Phase 3 – Structured Outputs & Tools
`phase3-structured-outputs/`
- 3.1 Function Calling & strukturierte Outputs — noch zu schreiben (fehlte bisher komplett, ist aber die Brücke zu Agenten)

## Phase 4 – Agents
`phase4-agents/`
- 4.1 Agenten-Team mit CrewAI → `lernplan_01_agenten_team_crewai.md` (bestehend)
- 4.2 Agent-Frameworks jenseits CrewAI (z. B. LangGraph) — noch zu schreiben

## Phase 5 – Production & Evaluation
`phase5-production-evaluation/`
- 5.1 Evaluation & Testing von LLM-Systemen — noch zu schreiben
- 5.2 Observability & Kosten — noch zu schreiben
- 5.3 Deployment — noch zu schreiben

## Phase 6 – Spezialisierung
`phase6-specialization/`
Wird später konkretisiert, je nach Interesse (Kandidaten: Fine-Tuning, Security/Prompt-Injection, Multimodalität).
