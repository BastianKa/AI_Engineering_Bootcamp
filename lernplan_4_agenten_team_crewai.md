# Lernplan 4: Dein erstes Agenten-Team mit CrewAI (Marketing-Team)

**Level:** Aufbauend auf Lernplan 1, 1B und 2
**Lernformat:** viele Videos, kurze Theorie, Coding-Along
**Endprodukt:** ein Team aus 2 CrewAI-Agenten (Rechercheur + Schreiber), das aus echten Produktdaten + aktuellen Web-Infos einen Marketing-Text erstellt
**Stand der Code-Beispiele:** Juli 2026 (CrewAI, crewai-tools, Tavily)

---

## ⚠️ Hinweis zu CrewAI-Versionen

CrewAI hat sich stark weiterentwickelt. Die aktuelle offizielle Doku empfiehlt inzwischen ein CLI-Setup mit YAML-Konfigurationsdateien und "Flows" für Produktionsprojekte. Für unser Lernziel – verstehen, was Agenten sind und wie ein Team funktioniert – bleiben wir bewusst bei der einfacheren, direkten Python-Variante (`Agent`/`Task`/`Crew` direkt im Code). Die ist nach wie vor voll unterstützt, nur eben nicht mehr der von CrewAI beworbene Standardweg für große Projekte.

---

## 🎯 Lernziele

Nach diesem Lernplan kannst du:
1. Erklären, was ein Agent zusätzlich zu einem einfachen Chatbot (Lernplan 1) kann
2. Erklären, was ein Tool für einen Agenten ist und warum der Agent selbst entscheidet, wann er es nutzt
3. Verstehen, wie ein Multi-Agenten-Team (Crew) zusammenarbeitet: Rollen, Tasks, Reihenfolge, Informationsfluss zwischen Agenten
4. Ein eigenes 2-Agenten-Marketing-Team bauen, das echte Produktdaten + aktuelle Web-Infos nutzt, um einen Marketing-Text zu erstellen

---

## 🧰 Setup

- Aus Lernplan 1/2 vorhanden: OpenAI API-Key in `.env`
- Neu: Tavily-Account (kostenloser Tier reicht) → API-Key unter app.tavily.com anlegen, in `.env` als `TAVILY_API_KEY` ergänzen
- Neue Pakete: `crewai`, `crewai-tools`, `tavily-python`, `requests`

---

## 📺 Teil A – Grundlagen: Was ist ein Agent, was ist ein Agenten-Team?

1. **"What are AI Agents?" – IBM Technology** (~6 Min)
   https://www.youtube.com/watch?v=F8NKVhkZZWI

2. **"5 Types of AI Agents: Autonomous Functions & Real-World Applications" – IBM Technology / Martin Keen** (~10 Min)
   https://www.youtube.com/watch?v=fXizBc03D7E

Optional, wenn du CrewAI selbst noch ausführlicher sehen willst (längeres Format):
**"CrewAI Tutorial: Complete Crash Course for Beginners" – Brandon Hancock**
https://www.youtube.com/watch?v=sPzc6hMg7So

### Kurz-Theorie

**Agent vs. Chatbot – der Unterschied zu Lernplan 1**
Dein Chatbot aus Lernplan 1 macht: Frage rein → Text raus. Ein Agent macht mehr: Er bekommt ein Ziel, entscheidet selbst, welche Tools er dafür braucht, ruft sie auf, wertet die Ergebnisse aus und wiederholt das bei Bedarf, bis das Ziel erreicht ist. Kurz gesagt: **Agent = LLM + Tools + die Fähigkeit, selbst zu entscheiden, wann und wie es die Tools einsetzt.**

**Warum Tools?**
Ein LLM kann von sich aus nichts "tun" – nur Text erzeugen. Ein Tool (z. B. eine Funktion, die eine API aufruft) gibt dem Agenten die Möglichkeit, tatsächlich etwas in der echten Welt nachzuschlagen. Das kennst du im Grunde schon aus Lernplan 2 (die Chroma-Suche im RAG-Prozess) – neu ist hier: **das LLM selbst entscheidet**, wann es ein Tool benutzt, statt dass wir es fest im Code vorschreiben.

**Was ist ein Multi-Agenten-Team (Crew)?**
Statt einem Agenten, der alles allein macht, teilt man die Arbeit auf mehrere spezialisierte Agenten auf – wie in einem echten Team. In CrewAI:
- Ein **Agent** hat eine Rolle (`role`), ein Ziel (`goal`), eine kurze "Persönlichkeit" (`backstory`) und optional Tools
- Ein **Task** ist eine konkrete Aufgabe mit Beschreibung (`description`) und erwartetem Ergebnis (`expected_output`), zugewiesen an einen Agenten
- Eine **Crew** verbindet Agenten + Tasks und führt sie in einer bestimmten Reihenfolge aus (bei uns: sequenziell – Agent 1 ist fertig, dann übernimmt Agent 2 dessen Ergebnis)

Unser Team für diesen Lernplan:

| Agent | Rolle | Tools |
|---|---|---|
| Rechercheur | sammelt echte Produktdaten + aktuelle Web-Infos | Open Food Facts (öffentliche API), Tavily (Websuche) |
| Schreiber | verfasst daraus einen kurzen Marketing-Text | keine (nutzt nur die Recherche-Ergebnisse) |

---

## 💻 Teil B – Praxis: Das Marketing-Team bauen (Coding-Along mit Claude Code)

**Ziel:** Ein Skript/Notebook, das für ein Produkt (per Barcode) einen fertigen Social-Media-Post erzeugt.

Aufgabenliste:

1. **Setup**
   - `crewai`, `crewai-tools`, `tavily-python`, `requests` installieren
   - Tavily-Account anlegen, API-Key in `.env` ergänzen

2. **Eigenes Tool bauen: Produkt-Lookup**
   - Ein CrewAI-Tool schreiben, das die Open Food Facts API aufruft und Name, Marke, Zutaten zurückgibt
   - Mit ein paar echten Barcodes testen – isoliert, noch ohne Agenten

3. **Tavily-Tool einbinden**
   - `TavilySearchTool` aus `crewai_tools` importieren, kurz isoliert testen (z. B. "aktuelle Trends Schokoaufstrich")

4. **Rechercheur-Agent bauen**
   - `Agent` mit Rolle, Ziel, Backstory und beiden Tools
   - Dazu einen `Task`, der beschreibt, was recherchiert werden soll

5. **Schreiber-Agent bauen**
   - `Agent` ohne Tools, nur mit Rolle/Ziel/Backstory
   - Dazu einen `Task` mit `context=[recherche_task]`, der auf Basis der Recherche einen Post schreibt

6. **Crew zusammensetzen und starten**
   - `Crew(agents=[...], tasks=[...], process=Process.sequential, verbose=True)`
   - `crew.kickoff(inputs={"barcode": "..."})` aufrufen
   - Ergebnis anschauen – und im `verbose`-Log mitlesen, wie die Agenten nacheinander arbeiten

7. **Experimentieren**
   - Einen anderen Barcode ausprobieren (z. B. von einem Produkt bei dir zuhause)
   - Beobachten: Nutzt der Rechercheur wirklich beide Tools? Was passiert, wenn Open Food Facts das Produkt nicht kennt?

### Technischer Hinweis zur Umsetzung (Stand Juli 2026)

**Eigenes Tool für Open Food Facts (öffentliche API, kein Key nötig):**
```python
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests

class ProduktLookupInput(BaseModel):
    barcode: str = Field(..., description="Der Barcode (EAN) des Produkts")

class ProduktLookupTool(BaseTool):
    name: str = "produkt_lookup"
    description: str = (
        "Ruft echte Produktdaten (Name, Marke, Zutaten) anhand eines "
        "Barcodes von Open Food Facts ab."
    )
    args_schema: Type[BaseModel] = ProduktLookupInput

    def _run(self, barcode: str) -> str:
        url = f"https://world.openfoodfacts.org/api/v2/product/{barcode}.json"
        headers = {"User-Agent": "LernplanMarketingCrew/1.0 (Lernprojekt)"}
        response = requests.get(url, headers=headers, timeout=10)
        daten = response.json()

        if daten.get("status") != 1:
            return f"Kein Produkt mit Barcode {barcode} gefunden."

        produkt = daten["product"]
        name = produkt.get("product_name", "Unbekannt")
        marke = produkt.get("brands", "Unbekannt")
        zutaten = produkt.get("ingredients_text", "keine Angabe")
        return f"Produkt: {name}\nMarke: {marke}\nZutaten: {zutaten}"
```

**Tavily-Tool (fertig aus crewai-tools, kein eigener Code nötig):**
```python
from crewai_tools import TavilySearchTool

tavily_tool = TavilySearchTool()  # liest TAVILY_API_KEY automatisch aus der Umgebung
```

**Agenten, Tasks und Crew:**
```python
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(model="openai/gpt-5.6")  # nutzt denselben OPENAI_API_KEY wie in Lernplan 1/2

produkt_tool = ProduktLookupTool()
tavily_tool = TavilySearchTool()

rechercheur = Agent(
    role="Produkt-Rechercheur",
    goal="Sammle verlässliche, echte Informationen über ein Produkt aus offiziellen Daten und aktuellen Web-Quellen.",
    backstory="Du bist gründlich und stützt dich immer auf Fakten, bevor du bewertest.",
    tools=[produkt_tool, tavily_tool],
    llm=llm,
    verbose=True,
)

schreiber = Agent(
    role="Marketing-Texter",
    goal="Verfasse aus vorhandenen Recherche-Ergebnissen einen kurzen, überzeugenden Marketing-Text.",
    backstory="Du hast ein Gespür für knappe, einprägsame Sprache in sozialen Medien.",
    llm=llm,
    verbose=True,
)

recherche_task = Task(
    description=(
        "Recherchiere das Produkt mit Barcode {barcode}. Nutze zuerst 'produkt_lookup' "
        "für echte Produktdaten (Name, Marke, Zutaten). Nutze danach Tavily, um "
        "herauszufinden, was aktuell im Web über dieses Produkt oder diese Marke "
        "gesagt wird (Trends, Bekanntheit, Meinungen)."
    ),
    expected_output=(
        "Eine strukturierte Zusammenfassung: Produktname, Marke, wichtigste "
        "Zutaten/Eigenschaften, plus 2-3 aktuelle Erkenntnisse aus der Websuche."
    ),
    agent=rechercheur,
)

schreib_task = Task(
    description="Schreibe auf Basis der Recherche einen kurzen Social-Media-Post (max. 5 Sätze) auf Deutsch.",
    expected_output="Ein fertiger Social-Media-Post-Text.",
    agent=schreiber,
    context=[recherche_task],
)

crew = Crew(
    agents=[rechercheur, schreiber],
    tasks=[recherche_task, schreib_task],
    process=Process.sequential,
    verbose=True,
)

ergebnis = crew.kickoff(inputs={"barcode": "3017624010701"})  # Beispiel: Nutella
print(ergebnis.raw)
```

Hinweis: Der Barcode `3017624010701` ist ein echter, öffentlicher Barcode (Nutella) zum Testen. Für dein eigenes Produkt: Barcode von einer Verpackung bei dir zuhause ablesen oder auf openfoodfacts.org nach einem Produkt suchen.

---

## ✅ Erfolgskriterien

- [ ] Erklären, was ein Agent zusätzlich zu einem einfachen Chatbot kann
- [ ] Erklären, was ein Tool ist und warum der Agent selbst auswählt, ob und wann er es nutzt
- [ ] Erklären, wie Informationen zwischen zwei Agenten in einer Crew weitergegeben werden (`context`)
- [ ] Ein laufendes Marketing-Team vorzeigen, das für ein selbst gewähltes Produkt einen Text erzeugt

---

## 🤖 So startest du das Coding-Along mit Claude Code

> Hier ist mein Lernplan (`lernplan_4_agenten_team_crewai.md`), er baut auf Lernplan 1, 1B und 2 auf. Geh mit mir Schritt für Schritt durch Teil B. Erkläre kurz, bevor wir jeden Schritt umsetzen, lass mich aber selbst tippen und frag nach, bevor du Code für mich schreibst.

---

## 🔭 Ausblick auf Lernplan 5 (Ideen)

- Eine dritte Rolle, z. B. Reviewer/Editor, der den Text vor Veröffentlichung noch mal gegenprüft (hierarchisches statt sequenzielles Team)
- Mehrere Produkte automatisch nacheinander verarbeiten (`kickoff_for_each`)
- Ein eigenes Tool, das den fertigen Text direkt irgendwo speichert oder verschickt
