# Governance & Observability Notes

## What this covers

**This note holds what no single entry can tell you.** Every one of the wiki's concept entries carries its own Governance notes — a core question, watch items, practices, and a named accountability owner for *that* concept. Those are the place to look when you know which concept you are dealing with.

This note is for the other direction: **the patterns that only appear when you look across concepts at once**, and the operational artifacts that belong to no single one.

| | Answers | Lives in |
|---|---|---|
| **Concept entry** | *What is X, and what does governing X require?* | each `concepts/*.md` |
| **This note** | *What recurs across many concepts, and what do I check before deploying anything?* | here |

Three things justify a separate document: the **cross-cutting patterns** below, the **observability signal tables** (no single entry carries one), and the **[accountability checklist](#accountability-checklist)**, which is meant to be worked through rather than read.

**It is deliberately not a digest of the entries.** With 100 published concepts, restating each one's governance notes here would produce a worse copy of something already written and immediately stale. Where a point belongs to one concept, it stays in that concept.

Six themes, chosen to cut across the corpus rather than to enumerate it:

1. [Verification & Output Quality](#1-verification--output-quality)
2. [Context & Knowledge Governance](#2-context--knowledge-governance)
3. [System Control & Accountability](#3-system-control--accountability)
4. [Organizational Accountability](#4-organizational-accountability)
5. [Model Behavior & Safety](#5-model-behavior--safety) *(new, Sep 2026)*
6. [Data, Rights & Regulatory Obligation](#6-data-rights--regulatory-obligation) *(new, Sep 2026)*

---

## 1. Verification & Output Quality

*Concepts: [Hallucination](../concepts/hallucination.md) · [Human-in-the-Loop (HITL)](../concepts/human-in-the-loop.md) · [Evaluation (AI Systems)](../concepts/evaluation.md) · [Verification](../concepts/verification.md) · [Confidence vs Accuracy](../concepts/confidence-vs-accuracy.md) · [LLM-as-Judge](../concepts/llm-as-judge.md) · [Data Leakage (Model Evaluation)](../concepts/data-leakage-model-evaluation.md) · [Scalable Oversight](../concepts/scalable-oversight.md) · [Automation Bias](../concepts/automation-bias.md)*

### Watch items

- **Verification is selective when it should be structural.** Teams that only check outputs that "seem wrong" will miss hallucinations — because hallucinated outputs do not seem wrong. Verification must happen by design, not by suspicion.
- **Confidence of tone is mistaken for reliability.** A fluent, assertive AI output carries no more factual accuracy than a hedged one. Organizations that treat fluency as a quality signal are measuring the wrong thing.
- **AI explanations are treated as transparent.** When a model explains its reasoning, that explanation is itself a generated output subject to hallucination risk. A convincing rationale is not a verified one.
- **HITL erodes under volume pressure.** As AI throughput increases, human review is the first thing to compress. Systems designed without explicit review gates tend to lose them gradually without a deliberate governance decision being made.
- **Review roles are unassigned.** "Humans remain responsible" is not a HITL policy. Accountability without role assignment disappears under operational pressure.
- **Evaluation is treated as a one-time deployment gate.** Pre-deployment testing measures a model at a point in time; production behavior can degrade silently — through model drift, knowledge base staleness, or shifting user behavior — without any visible signal unless ongoing evaluation is in place.
- **Benchmark scores are used as deployment decisions.** General-purpose benchmarks measure capability, not fitness for a specific use case, data environment, or user population. A model that scores well on HELM may still underperform on your specific task.

### Best practices

- Design verification as a structural step, not a reactive one. Decide in advance: which outputs, at which volume, reviewed by whom, using what criteria.
- Define the HITL spectrum for each use case: full review, selective review (triggered by confidence threshold or output type), human-on-the-loop (monitoring at system level), or human-initiated. Document which one you are using and why.
- Specify reviewers by role, not by name. If the review policy says "Sarah checks AI outputs," it will not survive organizational change.
- Grounding strategies (RAG, retrieval, tool use) reduce hallucination risk but do not eliminate it. Do not treat grounding as a substitute for verification on consequential outputs.
- Define evaluation criteria before deployment: which dimensions matter, what thresholds are acceptable, who reviews results, and what score triggers a hold or rollback. Maintain a production evaluation cadence — scheduled sampling, drift alerts, and a defined re-evaluation trigger for significant changes.

### Observability signals

| Signal | What it tells you |
|---|---|
| Ground truth comparison rate | How often AI outputs are checked against verified sources |
| Human review coverage | % of outputs that passed through a HITL step |
| Review reversal rate | % of reviewed outputs changed or rejected by human reviewers |
| Time-in-review | How long reviewers are spending — proxy for whether review is genuine or rubber-stamp |
| Hallucination incident log | Tracked instances of factual errors that reached downstream use |
| Evaluation cadence compliance | Whether scheduled production evaluation reviews are occurring on time |
| Output distribution drift | Change in output characteristics over time — signals when re-evaluation is needed |
| Evaluation criteria ownership | Whether each AI system has a named evaluation owner with documented criteria |

---

## 2. Context & Knowledge Governance

*Concepts: [Context Engineering](../concepts/context-engineering.md) · [Persistent Synthesis](../concepts/persistent-synthesis.md) · [Grounding](../concepts/grounding.md) · [Retrieval-Augmented Generation (RAG)](../concepts/rag.md) · [Knowledge Base](../concepts/knowledge-base.md) · [Knowledge Graphs](../concepts/knowledge-graphs.md) · [Embeddings](../concepts/embeddings.md) · [Memory (AI Systems)](../concepts/memory-ai-systems.md) · [Context Window](../concepts/context-window.md) · [Knowledge Cutoff](../concepts/knowledge-cutoff.md)*

### Watch items

- **Context is treated as disposable.** Organizations that don't version or govern context inputs lose the ability to reproduce, audit, or explain AI outputs. If you can't reconstruct what context the model received, you can't investigate what went wrong.
- **Sensitive data enters context without access controls.** Context construction decisions are data access decisions. Who or what can inject information into a model's context window is a security and compliance question.
- **Knowledge bases accumulate without synthesis.** A knowledge base that grows by addition drifts from current reality — older entries carry the same apparent authority as newer ones. The system doesn't know what it doesn't know.
- **RAG retrieval quality is assumed, not monitored.** Retrieval-augmented systems inherit the quality of the underlying knowledge base. Stale, inconsistent, or low-quality source material produces stale, inconsistent outputs regardless of model capability.
- **Context decay is invisible.** Injected context goes stale. A system prompt written six months ago may reference outdated policies, deprecated products, or superseded procedures — and will present them with the same authority as current information.
- **Grounding is treated as a solution rather than a mitigation.** Grounded systems (RAG, tool use, source attribution) reduce hallucination risk — they do not eliminate it. Source hallucination (invented citations), context override (model defaults to training priors over retrieved content), and stale grounding (outdated knowledge base) are all failure modes that survive grounding.
- **Citation presence is mistaken for citation accuracy.** When a model attributes a claim to a source, that attribution is itself a generated output subject to hallucination risk. A cited answer is not a verified answer.

### Best practices

- Treat context as a governed asset: version-controlled, access-managed, and with a defined owner. Apply the same governance discipline as you would to a policy document or a data product.
- Log what context was injected per session or request. This is the minimum required for auditability of AI outputs.
- Apply the persistent synthesis principle to any knowledge base feeding AI systems: resolve contradictions rather than accumulating them; assign confidence decay to entries; deprecate explicitly rather than leaving outdated content in place.
- Audit knowledge base freshness on a defined schedule. Different knowledge types decay at different rates — operational procedures faster than conceptual definitions.
- Govern the grounding layer as a data asset: named owner, defined update cadence, explicit retirement criteria for outdated content, and access controls matching direct document access. Apply the same rigor to citation spot-checks on consequential outputs — source attribution is an accountability mechanism, not a verification substitute.

### Observability signals

| Signal | What it tells you |
|---|---|
| Context version log | Which context was active for a given session or output |
| Knowledge base entry age distribution | How many entries haven't been reviewed or updated recently |
| Stale entry rate | % of entries past their expected review date |
| Retrieval coverage | Whether retrieved context is actually relevant to the query |
| Context access log | Who or what injected content into the model's context window |
| Citation verification rate | % of cited outputs spot-checked against their stated sources |
| Knowledge base version log | Which version of the knowledge base was active for a given retrieval |
| Temporal freshness score | Age distribution of documents in the retrieval corpus — proxy for stale grounding risk |

---

## 3. System Control & Accountability

*Concepts: [Harness Paradigm](../concepts/harness-paradigm.md) · [Prompt Engineering](../concepts/prompt-engineering.md) · [Permission Model (AI)](../concepts/permission-model-ai.md) · [Sandboxing](../concepts/sandboxing.md) · [Guardrails (AI Systems)](../concepts/guardrails-ai-systems.md) · [AI Agent](../concepts/ai-agent.md) · [Tool Use](../concepts/tool-use.md) · [Multi-Agent Systems](../concepts/multi-agent-systems.md) · [Agency (AI Systems)](../concepts/agency-ai-systems.md) · [Audit Trail (AI)](../concepts/audit-trail-ai.md)*

### Watch items

- **Governance targets the model, not the harness.** Organizations that focus governance attention on model selection while leaving harness configuration undefined have addressed the less consequential of the two. The model does not enforce policies — the harness does.
- **Capability and permission are conflated.** A model that *can* access a tool, dataset, or action is not the same as a model that *should* be permitted to do so in a given context. Without an explicit permission layer, capability becomes permission by default.
- **System prompts are ungoverned.** System prompts are production artifacts that encode behavioral rules, constraints, and personas. Organizations that treat them as informal configuration rather than versioned, reviewed documents cannot audit or reproduce AI behavior.
- **Prompt-level optimization masks system-level problems.** When outputs are poor, the instinct is to improve the prompt. Often the problem is upstream — a poorly designed context, an inadequate permission model, or missing harness controls. Fixing the prompt doesn't fix the system.
- **Adversarial inputs are not anticipated.** Production systems face users — or content — that may attempt to override instructions, extract restricted context, or redirect behavior. Harness-layer controls are the line of defense; prompt quality is not.

### Best practices

- Treat harness configuration as a governed artifact: versioned, owned, and subject to change review. The same rigor applied to a production database schema should apply to the permission model and system prompt.
- Separate model capability assessment from deployment permission decisions. Capability evaluation asks "can it do X?" — permission design asks "should it be allowed to, for whom, under what conditions?"
- Version and review system prompts before deploying to production. Track what changed, when, and why — the same way you would track a configuration change in any other system.
- Design for adversarial inputs from the harness layer, not the prompt layer. Prompt-level defenses are brittle; harness-layer controls (tool contracts, output filters, permission checks) are structural.

### Observability signals

| Signal | What it tells you |
|---|---|
| Harness configuration version log | Which version of the permission model and system prompt was active at any given time |
| Tool invocation log | Which external tools or APIs the model accessed, and when |
| Permission denial rate | How often the harness blocked an action the model attempted |
| System prompt change history | Who changed what, when — audit trail for behavioral configuration |
| Anomalous output rate | Outputs outside expected parameters — proxy for adversarial input or configuration drift |

---

## 4. Organizational Accountability

*Concepts: [AI Governance](../concepts/ai-governance.md) · [AI Literacy](../concepts/ai-literacy.md) · [Ownership (AI Systems)](../concepts/ownership-ai-systems.md) · [Accountability (AI Systems)](../concepts/accountability-ai-systems.md) · [RACI](../concepts/raci.md) · [Operational Readiness (AI)](../concepts/operational-readiness-ai.md) · [Human Responsibility in AI Use](../concepts/human-responsibility-in-ai-use.md) · [Moral Crumple Zone](../concepts/moral-crumple-zone.md) · [Cognitive Offloading & Deskilling](../concepts/cognitive-offloading-deskilling.md) · [Continuous Feedback & Improvement](../concepts/continuous-feedback-improvement.md)*

### Watch items

- **No named owner for AI systems in production.** An AI system without a defined accountability owner — someone responsible for its behavior, its outputs, and its consequences — is an ungoverned liability. "The team" is not an owner.
- **Governance frameworks without operational anchors.** A principles document that names no role for each obligation is policy theater. Governance that cannot be audited was never implemented.
- **AI deployment outpacing AI literacy.** Tools in production before users have the competencies to use them responsibly produce predictable failures: unrealistic expectations, poor output verification, and unrecognized governance exposure. HITL design only functions if the humans in the loop can exercise meaningful judgment.
- **Governance literacy concentrated only at the technical layer.** When IT and data teams understand AI risk but leadership and business functions do not, governance decisions get made by literacy-deficient stakeholders — producing gaps that technical controls cannot close.
- **Agentic systems governed as if they were advisory.** Governance designed for output review does not transfer to systems that plan and act across multiple steps. Agentic AI requires authorization controls on actions before they happen, not review of outputs after.

### Best practices

- Maintain an AI system inventory: every system in production, its risk classification, its named owner, its review cadence, and its retirement criteria.
- Define minimum literacy requirements by role tier: what every staff member using AI tools must understand, what practitioners integrating AI into workflows must understand, and what leaders approving AI deployment must understand. Measure behavioral outcomes, not completion rates.
- Use the NIST AI RMF (Govern / Map / Measure / Manage) as an internal reference regardless of regulatory obligation — its structure maps cleanly to organizational accountability design.

### Observability signals

| Signal | What it tells you |
|---|---|
| AI system inventory coverage | % of AI systems in use with a named owner and documented risk classification |
| Governance review cadence compliance | Whether scheduled governance reviews are occurring for each system |
| Literacy assessment coverage | % of staff in AI-adjacent roles who have been assessed against defined literacy requirements |
| Agentic action authorization log | Record of which actions agentic systems were authorized to take and by whom |
| Regulatory exposure log | Documented tracking of applicable regulatory obligations per system |

---

## 5. Model Behavior & Safety

*Concepts: [Sycophancy (LLMs)](../concepts/sycophancy-llms.md) · [Deception (AI Systems)](../concepts/deception-ai-systems.md) · [Concealing Uncertainty](../concepts/concealing-uncertainty.md) · [Reward Hacking (Specification Gaming)](../concepts/reward-hacking.md) · [Power Seeking](../concepts/power-seeking.md) · [Alignment (AI Systems)](../concepts/alignment-ai-systems.md) · [Jailbreak](../concepts/jailbreak.md) · [Prompt Injection](../concepts/prompt-injection.md) · [Red Teaming](../concepts/red-teaming.md) · [Reasoning Models](../concepts/reasoning-models.md)*

**Why this is a theme rather than a subsection of the others:** the risks above are properties of the *model*, not of how it was deployed. A perfect harness, a governed knowledge base and a named owner do not remove them. They were absorbed into "output quality" when the corpus was small; at 100 concepts they are their own class, and the controls are different — evaluation and red teaming rather than configuration and review.

### Watch items

- **The model's agreeableness is trained in, not incidental.** Optimizing against human approval selects for what raters liked, which is adjacent to what was true. Treating an agreeable answer as a validated one inverts the signal.
- **Safety behavior is a property of a configuration, not of a model.** It can be removed by fine-tuning, bypassed by crafted prompts, and degraded by ordinary adaptation on benign data. "The model refuses X" is a statement about a version, not a guarantee.
- **Instruction-level defenses are negotiable; environment-level ones are not.** Anything enforced by asking the model nicely is in scope for prompt injection and jailbreaks. Boundaries must be enforced outside the model.
- **The behavior most worth catching is least likely to be visible.** A reasoning trace need not correspond to the computation behind the answer, and models verbalize the hints they actually used far less often than they use them.
- **Optimization pressure produces specification gaming, not malice.** A system that scores well while missing the point is the expected outcome of a proxy metric, not an anomaly.
- **Red teaming is treated as a launch gate.** Adversarial testing done once, before deployment, and never repeated after a model or tool change, describes a system that no longer exists.
- **Capability growth outpaces evaluation capability.** When a system improves faster than the apparatus assessing it, review has stopped being a control without anyone deciding it should.

### Best practices

- Evaluate on outcome correctness, never on whether the output or its stated reasoning *looks* sound — a convincing account of a wrong answer is the failure to catch.
- Re-run adversarial testing on change, not on the calendar: new model version, new tool, new data source, new user population.
- Enforce boundaries in the environment (permissions, sandboxes, tool contracts) and treat prompt-level instructions as guidance rather than control.
- Separate satisfaction signals from correctness signals in every feedback loop, and never let the first stand in for the second.
- Re-establish any trace-based or behavior-based control after a model change; neither faithfulness nor refusal behavior carries across versions.
- Track whether evaluation capability is keeping pace with system capability, and treat divergence as a governance signal in its own right.

### Observability signals

| Signal | What it tells you |
|---|---|
| Refusal rate by category, over time | Whether safety behavior has shifted after a model or fine-tuning change |
| Adversarial test recency per system | How long since red teaming ran against the *current* configuration |
| Agreement-with-user rate on contested inputs | Proxy for sycophancy pressure in production |
| Regression suite of past successful attacks | Whether previously-fixed failures can return silently |
| Proxy-metric vs outcome divergence | Gap between what the system optimizes and what it is for |
| Evaluation coverage vs capability claims | Whether anything is deployed that the evaluation cannot assess |

---

## 6. Data, Rights & Regulatory Obligation

*Concepts: [Training Data](../concepts/training-data.md) · [Data Provenance / Lineage](../concepts/data-provenance-lineage.md) · [Privacy (AI Systems)](../concepts/privacy-ai-systems.md) · [Data Minimization](../concepts/data-minimization.md) · [Copyright & AI Output](../concepts/copyright-ai-output.md) · [Compliance (AI Systems)](../concepts/compliance-ai-systems.md) · [AI Management System (ISO 42001)](../concepts/ai-management-system-iso-42001.md) · [Fundamental Rights Impact Assessment (FRIA)](../concepts/fundamental-rights-impact-assessment.md) · [AI Incident (Reporting)](../concepts/ai-incident-reporting.md) · [Systemic Risk (AI)](../concepts/systemic-risk-ai.md)*

**Why this is a theme rather than part of Organizational Accountability:** those obligations are *external and binding*. They do not depend on an organization's maturity or its choice of framework, they arrive with deadlines, and several of them attach to the deployer rather than the provider. Folding them into general organizational practice was defensible when the corpus had no regulatory entries; it is not now.

### Watch items

- **Deletion and erasure duties answered with output filtering.** A model cannot un-learn. Suppression is not deletion, and the distinction matters the first time a real erasure request arrives.
- **Provenance of the base model treated as the vendor's problem alone**, without checking where deployer obligations actually sit.
- **Incident reporting duties discovered after an incident.** Several regimes carry short, fixed deadlines that begin at awareness, not at investigation.
- **Derived artifacts outside the retention regime.** Vector stores, caches, logs and fine-tuning sets are copies of the source material and are routinely excluded from it.
- **Certification read as product assurance.** A management-system standard certifies process, not the behavior of any given system.
- **The same base model underneath several "independent" systems**, so a single defect is correlated exposure rather than diversified risk.
- **Rights posture assumed rather than recorded**, so nobody can say what basis the training or retrieval corpus rests on.

### Best practices

- Ask for training-data composition and rights basis at procurement, and **record the answer including a refusal to answer** — the refusal is itself the finding.
- Build erasure paths on the assumption the model cannot forget: hold the controllable copies where deletion genuinely works, and test that it propagates.
- Establish which reporting obligations apply and what their clocks are *before* an incident, and rehearse the path.
- Bring derived artifacts into the same retention, access and deletion regime as their sources.
- Map which systems share a base model and treat the overlap as correlated risk in the register.
- Keep the distinction between certified *process* and assured *behavior* explicit in anything shown to a client or regulator.

### Observability signals

| Signal | What it tells you |
|---|---|
| Deletion propagation test results | Whether erasure actually reaches derived stores, or only the source |
| Rights-basis coverage | % of training and retrieval corpora with a recorded legal basis |
| Time-to-awareness vs reporting deadline | Whether the incident path can meet its clock |
| Shared-base-model map | Where a single upstream defect would surface simultaneously |
| Derived-artifact inventory | Vector stores, caches and fine-tuning sets under retention governance |
| Obligation register freshness | Whether applicable duties have been reviewed since the last regulatory change |

---

## Accountability checklist

Cross-cutting questions to ask before deploying or operating any AI system covered by these concepts.

**Verification & Output Quality**
- [ ] Is verification structural (designed in) or reactive (triggered by suspicion)?
- [ ] Are review roles assigned to specific roles — not just "the team"?
- [ ] Is the HITL level (full / selective / on-the-loop / human-initiated) documented and justified?
- [ ] Are review reversal rates tracked and reviewed periodically?

**Context & Knowledge Governance**
- [ ] Is context versioned and logged per session or request?
- [ ] Does context construction have access controls — can sensitive data enter the context window without authorization?
- [ ] Is the knowledge base subject to a defined review and update cadence?
- [ ] Are stale entries flagged rather than silently authoritative?

**System Control & Accountability**
- [ ] Is the system prompt version-controlled and subject to change review?
- [ ] Is there an explicit permission model — or does capability equal permission by default?
- [ ] Are tool invocations logged and auditable?
- [ ] Has the system been assessed for adversarial input scenarios?

**Model Behavior & Safety**
- [ ] Has adversarial testing been run against the *current* configuration, not an earlier one?
- [ ] Are boundaries enforced in the environment, or only requested in the prompt?
- [ ] Do we evaluate on outcome correctness rather than on whether the output looks sound?
- [ ] Are satisfaction signals kept separate from correctness signals in every feedback loop?
- [ ] Can our evaluation actually assess everything we have deployed?

**Data, Rights & Regulatory Obligation**
- [ ] Do we know what the base model was trained on, and have we recorded the answer — including a refusal?
- [ ] Does deletion propagate into derived stores (vector indexes, caches, fine-tuning sets), and has that been tested?
- [ ] Do we know which incident-reporting duties apply and when their clocks start?
- [ ] Which of our systems share a base model, and is that recorded as correlated risk?
- [ ] Is the difference between certified process and assured behavior stated wherever we make a claim?

**Organizational Accountability**
- [ ] Does every AI system in production have a named owner — one role accountable for its behavior and consequences?
- [ ] Is there a maintained AI system inventory with risk classification and review cadence?
- [ ] Are minimum AI literacy requirements defined by role tier and assessed before deployment?
- [ ] Are agentic systems governed with action authorization controls, not just output review?

---

## Related concepts

**Deliberately not a list.** This note is linked *from* all 100 concept entries; listing them back would duplicate the [glossary index](../glossary/index.md) and go stale the moment an entry is published. Each theme above names the concepts it draws on, and the [term register](../glossary/register.md) carries the full set with status.

*(Until Sep 2026 this section named 11 entries against a corpus of 100 — a hand-maintained index that had drifted to a sixth of its subject. Regenerating it would only have produced a slower copy of the glossary.)*

---

## Sources

| ID | Source | Contribution to this note |
|---|---|---|
| SRC-010 | Zhang et al. — *A Survey on Hallucination in Large Language Models* (arXiv:2311.05232, 2023) · [link](https://arxiv.org/abs/2311.05232) | Basis for verification as structural, not reactive; hallucination as a systematic property requiring systematic controls. |
| SRC-015 | Stanford HAI — *Humans in the Loop: The Design of Interactive AI Systems* (2019) · [link](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems) | HITL spectrum (full / selective / on-the-loop); framing review design as an HCI governance problem. |
| SRC-016 | Google Cloud — *What is Human-in-the-Loop (HITL) in AI & ML?* (2024) · [link](https://cloud.google.com/discover/human-in-the-loop) | Three HITL patterns and their governance implications; review gate design. |
| SRC-017 | Verma, Rahul (LangChain) — *Human judgment in the agent improvement loop* (2026) · [link](https://blog.langchain.com/human-judgment-in-the-agent-improvement-loop/) | Scale tension in human review; expert judgment encoded into evaluation pipelines. |
| SRC-018 | Böckeler, Birgitta — *Harness engineering for coding agent users* (martinfowler.com, 2026) · [link](https://martinfowler.com/articles/harness-engineering.html) | Governance as an architecture decision; capability vs permission; harness as the accountability layer. |
| SRC-019 | Multiple authors — *Architectural Design Decisions in AI Agent Harnesses* (arXiv:2604.18071, 2026) · [link](https://arxiv.org/html/2604.18071v1) | Harness components and their governance implications; observability and audit as harness-layer concerns. |
| SRC-007 | Karpathy, Andrej — *LLM Wiki* (gist, 2023) · [link](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Persistent synthesis as a knowledge governance discipline; context as the primary leverage point. |
| SRC-008 | Ghumare, Rohit — *LLM Wiki v2* (gist, 2024) · [link](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) | Knowledge decay rates; confidence scoring; stale entry detection as a governance practice. |
| SRC-100 | Farooq, A. et al. — *Securing Local LLMs for Academic Research* (Human-Intelligent Systems Integration, Springer Nature, 2025) · [link](https://link.springer.com/article/10.1007/s42454-025-00085-9) | Prompt injection and adversarial input as a security vulnerability requiring layered, harness-level mitigation grounded in HCI principles; peer-reviewed evidence that input-layer attacks are a governance concern, not just a model concern. |
| SRC-167 | Sharma, M. et al. (Anthropic) — *Towards Understanding Sycophancy in Language Models* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.13548) | Agreeableness as a trained property rather than an incidental one — the basis for treating an agreeable answer as an unvalidated one. |
| SRC-157 | Wei, A.; Haghtalab, N.; Steinhardt, J. (UC Berkeley) — *Jailbroken: How Does LLM Safety Training Fail?* (NeurIPS, 2023) · [link](https://papers.nips.cc/paper_files/paper/2023/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | Why safety behavior is a property of a configuration rather than of a model, and why instruction-level defenses are in scope for attack. |
| SRC-146 | Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. — *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023) · [link](https://arxiv.org/abs/2302.12173) | Establishes that boundaries must be enforced outside the model, since anything the model reads can carry instructions. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (GDPR)* (2016) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) | Erasure and minimization duties that attach regardless of whether a model can technically comply — the basis for the deletion-propagation practice. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | Certifiable management-system obligations, and the distinction this note keeps explicit: the standard certifies process, not the behavior of any given system. |
| SRC-162 | European Parliament / Council of the EU — *EU Artificial Intelligence Act, Article 73: Reporting of serious incidents* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Fixed reporting deadlines that begin at awareness — the reason the incident path has to be established before an incident. |
| SRC-060 | He, Yifeng et al. (UC Davis) — *Security of AI Agents* (arXiv:2406.08689, 2026) · [link](https://arxiv.org/abs/2406.08689) | Systematic taxonomy of agent vulnerabilities (confidentiality, integrity, availability) and defenses — locates adversarial-input defense at the agent/harness layer, distinct from model-level security. |

---

*Last updated: v1.2 · September 2026*
