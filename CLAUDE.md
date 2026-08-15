# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is not a software project — it's a self-paced, multi-phase AI/LLM learning curriculum written in German ("Lernpläne" = lesson plans), starting from zero programming knowledge and building toward AI Engineer skills. Each lesson plan's "Endprodukt" (end product) is typically a Jupyter notebook that gets built *during* a coding-along session with Claude Code.

## Curriculum structure — always check these first

- **`ROADMAP.md`** — the full phase overview (Phase 0 Programming Fundamentals → Phase 1 LLM Fundamentals → Phase 2 Retrieval & Data → Phase 3 Structured Outputs & Tools → Phase 4 Agents → Phase 5 Production & Evaluation → Phase 6 Specialization). This is the source of truth for what exists and what comes next — don't re-derive the curriculum shape from scratch.
- **`progress.md`** — current phase/lesson and session notes. Read this at the start of a session instead of reconstructing context from chat history (saves tokens across sessions).

Each phase has its own folder `phase<N>-<topic>/` containing lesson files `lernplan_<step>_<topic>.md` plus a `notebooks/` subfolder for the learner's own notebooks/scratch code — lesson content and the learner's code stay separate. When adding a new lesson, follow this naming pattern and update `ROADMAP.md`.

Each plan's own "🔭 Ausblick" (outlook) section at the end lists candidate directions for the *next* plan — check there too, but `ROADMAP.md` is authoritative for the overall sequence.

## Conventions used across all plans (keep consistent if extending)

- **API/model choices** (stated as "Stand Juli 2026" in each file — treat as the pinned convention for this repo, not necessarily current reality): OpenAI Responses API over Chat Completions; model name `gpt-5.6` (with cheaper variants like `gpt-5.6-terra`/`gpt-5.6-luna`); embeddings via `text-embedding-3-small`.
- **Secrets**: API keys always via a `.env` file (`OPENAI_API_KEY`, later `TAVILY_API_KEY`), loaded with `python-dotenv` — never hardcoded in notebook cells.
- **Deliverable format**: each coding-along produces one Jupyter notebook per plan, built incrementally cell-by-cell rather than all at once.

## How to run a coding-along session in this repo

Every lesson plan ends with a suggested kickoff prompt (under "🤖 So startest du das Coding-Along mit Claude Code"). The consistent pattern across all of them, and the expected mode of operation when a user references one of these files:

- Go through the plan's "Teil B – Praxis" task list **step by step**, not all at once.
- Briefly explain a step before implementing it.
- Let the learner type code themselves where reasonable — this is an explicit learning exercise, not a "build it for me" task.
- **Ask before writing code for the user**, rather than generating full solutions unprompted.

Treat this pedagogical style (explain → let them attempt → confirm before writing code) as the default working mode whenever a session references one of these `lernplan_*.md` files, even if not restated explicitly in the user's prompt.
