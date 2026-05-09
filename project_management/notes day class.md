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

### Gemini 3.1 Pro Result
#### Statement: **"Rola człowieka będzie związana ze scope projektu (komunikacja z klientem)"**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Defining scope dictates the mechanical shift from abstract goals to rigid alignment constraints. Extracting accurate client intent establishes immutable boundaries for autonomous execution, neutralizing drift risk and guaranteeing computational velocity targets validated outcomes.

#### Statement: **"Techniki przełożenia scope na wewnętrzną wiedzę agenta (zrozumienie intencji)."**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Embedding scope directly into agent memory shifts human directives into deterministic operational parameters. Perfect semantic translation eliminates execution divergence, serving as the primary fail-safe against systemic hallucinations and exponential resource waste.

#### Statement: **"Komunikacja z zewnętrznymi interesariuszami (kontakt z człowiekiem jest istotny)."**

**Score: 1** 

**Obsolete:** Addresses human psychological needs, biological limits, or interpersonal friction.

**Justification:** Stakeholder contact serves purely biological needs for trust and reassurance, variables entirely divorced from agent logic. Isolating the system from this interpersonal friction removes emotional drag, maximizing execution velocity without degrading output accuracy.

#### Statement: **"Planowanie harmonogramu staje się drugorzędne dla agentów, bo nie frustrują się zmianami w planie na ostatnią chwilę. Planowanie harmonogramu staje się pierwszorzędne dla kierownika projektu, aby przewidywać wąskie gardła wykonania oraz ilość iteracji do osiągnięcia celu."**

**Score: 4** 

**Amplified:** Importance scales exponentially due to agent execution speed; precision in dependency mapping and constraints is paramount.

**Justification:** Scheduling transitions from mitigating human fatigue to managing deterministic compute loads and iteration limits. Precision in mapping execution bottlenecks amplifies in importance to prevent cascading resource failures as autonomous agents process tasks at maximum velocity.

#### Statement: **"Klient będzie próbował bezpośrednio tłumaczyć zespołowi agentów wymagania z pominięciem kierownika projektu."**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Unmediated client prompting bypasses alignment protocols, risking catastrophic output drift. The PM acts as a necessary architectural fail-safe, sanitizing volatile human ambiguity into deterministic constraints to secure system alignment and prevent unchecked resource depletion.

**Statement: "Formułowanie KPI będzie krytyczną umiejętnością, czyli przekładanie celu projektu na mierzalne wskaźniki postępu."**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Translating goals into quantifiable metrics shifts from guiding human intent to programming rigid reward functions. This deterministic alignment directly mitigates unbounded execution risk, guaranteeing maximum system velocity toward verified operational outcomes.

**Statement: "Projekty oparty o agentów powinny być podobne do siebie i krótkie, bo buduje to największą i najszybciej bazę doświadczenia, co pozwala przewidywać potrzeby klienta nawet nie zwerbalizowane."**

**Score: 4** 

**Amplified:** Importance scales exponentially due to agent execution speed; precision in dependency mapping and constraints is paramount.

**Justification:** High-frequency project execution shifts from gradual human retrospective learning to rapid algorithmic context caching. Enforcing short, standardized execution loops exponentially accelerates system scale velocity, reducing long-term project failure risk through immediate, compounded predictive accuracy.

**Statement: "Rozdzielenie intencji czyli celu projektu od sposobu wykonania, który może się różnić w zależności od kontekstu."**

**Score: 4** 

**Amplified:** Importance scales exponentially due to agent execution speed; precision in dependency mapping and constraints is paramount.

**Justification:** Decoupling rigid objectives from fluid execution paths shifts planning from human sequential drafting to autonomous algorithmic routing. Removing human cognitive bottlenecks in procedural planning exponentially accelerates execution velocity, demanding extreme precision in initial objective constraints to prevent failure.

**Statement: "Nowe ryzyka ujawnienia informacji poufnych oraz robienia rzeczy nielegalnych lub niepotrzebnych oprócz projektu."**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Mitigating data breaches and illegal operations shifts from human policy compliance to hardcoded boundary enforcement. Implementing deterministic fail-safes is strictly mandatory to eliminate catastrophic alignment risk, preventing high-velocity autonomous agents from executing destructive actions beyond project scope.

**Statement: "Nowe testy potwierdzające deterministycznie, czy pewne elementy zlecone zostały wykonane."**

**Score: 5** 

**Apex/Critical:** Fundamental to agentic control, including alignment, deterministic output validation, and fail-safes against systemic hallucinations.

**Justification:** Validating deliverables shifts from subjective human status updates to continuous, automated programmatic state checks. Deterministic output validation eliminates trust-based risk entirely, guaranteeing accurate dependency resolution and enabling uninterrupted high-velocity resource scaling.

**Statement: "KPI może być więcej ze względu na to że agenci nie odczuwają frustracji z dodatkową biurokracją i nadzorowaniem ich pracy."**

**Score: 3** 

**Translated:** Core logic remains; execution medium shifts (e.g., human shift scheduling translates to API rate and compute load management).

**Justification:** Expanding KPI tracking shifts from a friction-inducing human psychological burden to computationally bounded telemetry processing. Eliminating biological constraints allows infinite telemetry ingestion, transforming traditional bureaucracy into continuous, frictionless system optimization that maximizes resource velocity.
