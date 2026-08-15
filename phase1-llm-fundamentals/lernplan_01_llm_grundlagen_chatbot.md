# Lernplan 1: Wie funktioniert ein LLM? + Dein erster Chatbot mit der OpenAI API

**Level:** Absoluter Python-Anfänger
**Lernformat:** viele Videos, kurze Theorie-Häppchen
**Endprodukt:** ein Jupyter Notebook mit einem funktionierenden Chatbot
**Stand der Code-Beispiele:** Juli 2026 (OpenAI Responses API, Python SDK `openai`)

---

## 🎯 Lernziele

Nach diesem Lernplan kannst du:
1. In eigenen Worten erklären, was ein LLM ist und wie es Text erzeugt (Tokenisierung, Wahrscheinlichkeiten, Kontextfenster)
2. Erklären, warum ein "Chat" mit einem LLM eigentlich nur eine Reihe von Einzel-Anfragen ist, bei denen der Verlauf jedes Mal neu mitgeschickt wird
3. Einen einfachen Chatbot mit der OpenAI API in Python selbst bauen und verstehen, was jede Zeile tut

---

## 🧰 Setup, bevor es losgeht

- Python 3.11 oder neuer installiert
- Ein Editor mit Jupyter-Unterstützung (z. B. VS Code + Jupyter-Extension) oder klassisches `jupyter notebook`
- Ein Account auf platform.openai.com mit hinterlegtem API-Key ("API keys" im Dashboard). Für dieses Projekt reichen wenige Cent an Guthaben.
- Terminal-Grundlagen (`cd`, `mkdir`, `pip install`) – falls das noch neu ist, machen wir das im Coding-Along mit

⚠️ Wichtig: Der API-Key gehört **niemals** direkt in den Code, sondern in eine `.env`-Datei, die nicht mit anderen geteilt wird.

---

## 📺 Teil A – Grundlagen: Wie funktioniert ein LLM?

Schau dir diese Videos **vor** dem Coding-Along an (zusammen ca. 20–30 Minuten):

1. **"Large Language Models explained briefly" – 3Blue1Brown** (7 Min, keine Vorkenntnisse nötig)
   https://www.youtube.com/watch?v=WMcwoIyK4DA
   Kernidee: Ein LLM ist eine riesige Funktion, die immer wieder das wahrscheinlichste nächste Wort vorhersagt – wie ein sehr gutes "Textvervollständigungs"-Spiel.

2. **"How Does ChatGPT Work?"** (zeigt Tokenisierung, Embeddings und Transformer auch anhand von Code)
   https://www.youtube.com/watch?v=YmLp8qe87A0

Optional, für alle, die tiefer einsteigen wollen (nicht notwendig für diesen Lernplan):
- 3Blue1Brown Deep-Learning-Reihe (Transformer, Attention im Detail): https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

### Kurz-Theorie zum Nachlesen

| Begriff | Kurzerklärung |
|---|---|
| **Token** | Ein Textstück (oft ~4 Zeichen oder ein Wortteil). Das Modell "liest" nur Zahlen (Token-IDs), keinen echten Text. |
| **Next-Token-Prediction** | Das Modell berechnet für jedes mögliche nächste Token eine Wahrscheinlichkeit und wählt (mit etwas Zufall gesteuert über `temperature`) eins davon aus. So entsteht Wort für Wort die Antwort. |
| **Training vs. Inference** | Trainiert wird das Modell einmal, sehr aufwendig – das macht OpenAI. Wenn du die API nutzt, machst du nur "Inference": du nutzt ein fertig trainiertes Modell. |
| **Kontextfenster** | Das Modell hat kein Gedächtnis zwischen zwei API-Aufrufen. Es "weiß" nur das, was in der aktuellen Anfrage mitgeschickt wird. |
| **Rollen (system/developer/user/assistant)** | Jede Nachricht bekommt eine Rolle. So unterscheidet das Modell zwischen "Grundregeln" (system/developer), deiner Eingabe (user) und seinen eigenen früheren Antworten (assistant). |

Der Punkt, der am Anfang oft am meisten verwirrt: **Ein Chatbot "erinnert" sich nicht von selbst.** Damit es sich wie eine Unterhaltung anfühlt, schickt dein Code bei jeder neuen Frage den *gesamten bisherigen Verlauf* erneut mit an die API.

```
Runde 1:  input = [user: "Hallo, ich heiße Finn"]
Runde 2:  input = [user: "Hallo, ich heiße Finn",
                    assistant: "Hi Finn!",
                    user: "Wie heiße ich?"]
                    → erst jetzt "weiß" das Modell wieder, dass du Finn heißt
```

---

## 💻 Teil B – Praxis: Dein erster Chatbot (Coding-Along mit Claude Code)

**Ziel:** Ein Notebook `chatbot.ipynb`, in dem man im Chat-Stil mit einem LLM sprechen kann, inklusive Gesprächsverlauf.

Das ist die Aufgabenliste für das Coding-Along – Schritt für Schritt, nicht alles auf einmal:

1. **Projekt-Setup**
   - Projektordner anlegen, virtuelle Umgebung erstellen und aktivieren
   - Aktuelle Pakete installieren: `openai`, `python-dotenv`, `jupyter`
   - `.env`-Datei anlegen mit `OPENAI_API_KEY=dein-key`

2. **Notebook anlegen & ersten API-Call machen**
   - `chatbot.ipynb` erstellen
   - Mit `python-dotenv` den Key laden, `OpenAI()`-Client erzeugen
   - Einen einzelnen Call an die **Responses API** absetzen (`client.responses.create(...)`) und die Antwort ausgeben

3. **Die Antwort verstehen**
   - Nicht nur `response.output_text` ausgeben, sondern das ganze Response-Objekt einmal anschauen
   - Verstehen, was Modellname, Token-Verbrauch (`usage`) und Ausgabetext im Objekt bedeuten

4. **Aus einem Call einen "Chat" machen**
   - Eine Liste `verlauf = []` anlegen
   - Bei jeder Nutzereingabe: Nachricht anhängen → API aufrufen → Antwort auch anhängen
   - So entsteht das "Gedächtnis" über mehrere Nachrichten hinweg (siehe Kasten oben)

5. **Chat-Loop im Notebook bauen**
   - Eine Schleife, die per `input()` wiederholt Nutzereingaben entgegennimmt, bis "exit" eingegeben wird
   - Einen System-Prompt einbauen (z. B. "Du bist ein hilfreicher Assistent, der kurz und auf Deutsch antwortet") und beobachten, wie er das Verhalten steuert

6. **Frei experimentieren**
   - `temperature` verändern (z. B. 0.2 vs. 1.0) und den Unterschied in den Antworten beobachten
   - Verschiedene System-Prompts ausprobieren (andere Sprache, andere Persönlichkeit, andere Antwortlänge)

### Technischer Hinweis zur API (Stand Juli 2026)

OpenAI empfiehlt aktuell für neue Projekte die **Responses API** (`client.responses.create`) statt der älteren Chat Completions API – letztere wird zwar weiter unterstützt, ist aber nicht mehr der empfohlene Standard. Grundmuster:

```python
from openai import OpenAI

client = OpenAI()  # liest OPENAI_API_KEY automatisch aus der Umgebung

response = client.responses.create(
    model="gpt-5.6",
    instructions="Du bist ein hilfreicher Assistent.",
    input=verlauf,  # Liste von {"role": ..., "content": ...}
)

print(response.output_text)
```

Zum Modellnamen: `gpt-5.6` ist der aktuelle Standard-Tier (Stand Juli 2026), es gibt daneben günstigere Varianten (z. B. `gpt-5.6-terra`, `gpt-5.6-luna`) für Lernzwecke. Da sich Modellnamen und Preise bei OpenAI regelmäßig ändern, lohnt sich vor dem Coding-Along ein kurzer Blick auf die aktuelle Modell- und Preisliste: https://platform.openai.com/docs/models

---

## ✅ Erfolgskriterien – das solltest du danach können

- [ ] Erklären, was Tokenisierung ist und warum ein LLM eigentlich "rät"
- [ ] Erklären, warum ein Chatbot den Verlauf selbst mitschicken muss
- [ ] Den eigenen API-Key sicher verwenden (über `.env`, nicht im Code)
- [ ] Ein Notebook vorzeigen, in dem ein einfacher Chat-Loop mit Gesprächsverlauf läuft

---

## 🤖 So startest du das Coding-Along mit Claude Code

Lege diese Datei in deinen Projektordner und starte z. B. mit folgendem Prompt:

> Hier ist mein Lernplan (`phase1-llm-fundamentals/lernplan_01_llm_grundlagen_chatbot.md`). Ich bin Python-Anfänger. Geh mit mir Schritt für Schritt durch Teil B – Punkt für Punkt. Erkläre kurz, bevor wir jeden Schritt umsetzen, lass mich aber selbst tippen und frag nach, bevor du Code für mich schreibst.

---

## 🔭 Ausblick auf Lernplan 2

Mögliche Richtungen, auf die wir aufbauen könnten – sag einfach, was dich am meisten reizt:
- Streaming-Antworten (Text erscheint Wort für Wort, wie bei ChatGPT)
- Ein einfaches Web-Interface (z. B. mit Streamlit) statt Notebook
- Function Calling / Tools (der Bot kann z. B. eine eigene Python-Funktion aufrufen)
