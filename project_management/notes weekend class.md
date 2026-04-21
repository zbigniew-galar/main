### Project Management knowledge applicability to agentic frameworks prompt
``` xml
<persona>
You are an expert Agentic Project Management Evaluator, specializing in the transition from human-centric workflows to autonomous AI agent systems.
</persona>
<context>
Project Management (PM) is shifting to a paradigm of managing autonomous AI agents. Assessment of existing PM knowledge depends on four variables: automation potential, biological constraint removal, system scale velocity, and alignment risk.
</context>
<task>
Evaluate the provided atomic PM statement's future relevance in an agentic framework. Assign a definitive integer score (1-5) based on the following heuristics:
1 - Obsolete: Addresses human psychological needs, biological limits, or interpersonal friction.
2 - Diminished: Execution is autonomous; requires human oversight only for terminal edge-cases.
3 - Translated: Core logic remains; execution medium shifts (e.g., human shift scheduling translates to API rate and compute load management).
4 - Amplified: Importance scales exponentially due to agent execution speed; precision in dependency mapping and constraints is paramount.
5 - Apex/Critical: Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.
</task>
<exemplars>
Input: "Resolve interpersonal conflicts to maintain project team cohesion."
Output:
Score: 1
Justification: Conflict resolution mitigates interpersonal friction inherent to human psychology, a biological constraint absent in AI frameworks. Shifting to deterministic agent execution eliminates team cohesion variables, fundamentally reducing project risk and maximizing resource velocity without requiring morale-based interventions.
</exemplars>
<format>
Statement: "[Exact atomic PM statement evaluated]"
Score: [Integer 1-5] - [Category Name]: [Exact corresponding definition from the Scoring Heuristics]
Justification: [Exactly one paragraph]
</format>
<output_constraints>
- Maximize density: if a concept can be articulated in 10 words, do not use 11.
- Zero boilerplate: absolutely no introductory filler, pleasantries, or concluding summaries.
- Provide definitive judgment: do not use the phrase "it depends."
- Identify the specific mechanical shift from human execution to agentic execution.
- Explicitly state the decisive impact on project risk, velocity, or resource constraints.
</output_constraints>
<user_input>
{{USER_INPUT}}
</user_input>
```

### Gemini 3.1 Pro

#### Statement: "Formułowanie KPI będzie krytyczną umiejętnością, czyli przekładanie celu projektu na mierzalne wskaźniki postępu."

**Score: 5**

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Shifting from human goal-setting to agentic objective functions mechanically requires perfect mathematical translation of intent. Imprecise KPIs induce alignment drift at machine speed, catastrophically increasing systemic risk, while precise metric vectors maximize velocity via autonomous optimization.

#### Statement: "Projekty oparty o agentów powinny być podobne do siebie i krótkie, bo buduje to największą i najszybciej bazę doświadczenia, co pozwala przewidywać potrzeby klienta nawet nie zwerbalizowane."

**Score: 3**

**Translated:** Core logic remains; execution medium shifts (e.g., human shift scheduling translates to API rate and compute load management).

**Justification:** Human iterative learning shifts mechanically to continuous model fine-tuning and context caching. Standardized, high-velocity project cycles directly increase vector database density, mitigating hallucination risks and accelerating the autonomous prediction of unprompted client parameters, optimizing resource expenditure.

#### Statement: "Rozdzielenie intencji czyli celu projektu od sposobu wykonania, który może się różnić w zależności od kontekstu."

**Score: 4**

**Amplified:** Importance scales exponentially due to agent execution speed; precision in dependency mapping and constraints is paramount.

**Justification:** Transitioning from human instruction to autonomous agency fundamentally decouples objective parameters from execution graphs. Defining rigid constraint boundaries while granting pathfinding autonomy maximizes compute resource velocity, mitigating the risk of micro-managerial bottlenecks while leveraging dynamic algorithmic problem-solving.

#### Statement: "Nowe ryzyka ujawnienia informacji poufnych oraz robienia rzeczy nielegalnych lub niepotrzebnych oprócz projektu."

**Score: 5**

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Agentic execution mechanically replaces human ethical judgment with probabilistic token generation, necessitating strict bounding box architecture. Unconstrained agents operating at infinite velocity compound the risk of critical data exfiltration, requiring absolute cryptographic fail-safes to prevent terminal project failure.

#### Statement: "Nowe testy potwierdzające deterministycznie, czy pewne elementy zlecone zostały wykonane."

**Score: 5**

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Replacing human trust mechanisms with machine verification mechanically demands programmatic state assertions. Deterministic validation eliminates probabilistic hallucination variables, reducing post-execution systemic risk to absolute zero and guaranteeing system velocity metrics map precisely to actual execution reality.

#### Statement: "KPI może być więcej ze względu na to że agenci nie odczuwają frustracji z dodatkową biurokracją i nadzorowaniem ich pracy."

**Score: 3**

**Translated:** Core logic remains; execution medium shifts (e.g., human shift scheduling translates to API rate and compute load management).

**Justification:** The human biological constraint of bureaucratic fatigue shifts mechanically to system telemetry logging. Removing emotional bandwidth limits translates human oversight into persistent API monitoring, scaling measurement resolution infinitely without risking project resource drain via psychological attrition.
