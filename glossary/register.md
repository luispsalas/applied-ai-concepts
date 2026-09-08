# Term register

Every term this wiki tracks, with its status — **including the ones that are not published, and the ones that will not be.**

The field names things faster than it settles them, and a glossary that repeats every new label without comment is a list of buzzwords. So each term is judged on whether it is a *real term*. That is a separate question from how good the evidence is for the claims inside an entry, which each entry states for itself in its own confidence level.

**174 terms tracked — 123 published, 51 not.** See [how terms are admitted](../CONTRIBUTING.md#term-status--the-admission-test).

| Status | Meaning | Count |
|---|---|---|
| `established` | Recognized term of art, in independent use. | 117 |
| `emerging` | Real and in use, but definitions still vary between sources. | 8 |
| `unassessed` | Candidate not yet put through the term-status checks. | 40 |
| `declined` | Considered and turned down — not a term this wiki will publish. | 1 |
| `covered` | A real term, already covered by another entry — findable there as an alias. | 8 |

---

| Term | Status | Published | Notes |
|---|---|---|---|
| A/B Testing | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Acceptable Use Policy | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Accountability (AI Systems)](../concepts/accountability-ai-systems.md) | `established` | yes |  |
| [Agency (AI Systems)](../concepts/agency-ai-systems.md) | `established` | yes |  |
| [Agent Hooks](../concepts/agent-hooks.md) | `established` | yes | RENAMED from "Hook" and published Sep 7 2026, resolving the vendor status. Every major agent runtime has independently converged on the pattern — Claude Code, OpenAI Codex CLI, LangChain/LangGraph, Google ADK, AutoGen, Semantic Kernel — so it is convergent, not proprietary. The entry's contribution is the distinction most documentation buries: can the hook BLOCK, or only observe? |
| [Agent Interoperability (A2A)](../concepts/agent-interoperability-a2a.md) | `established` | yes |  |
| Agent Memory | `covered` | **covered by [Memory (AI Systems)](../concepts/memory-ai-systems.md)** | COVERED by Memory (AI Systems) — decided Sep 7 2026 under admission check 4. A real established term, but that entry already is this one: it uses the in-trial / cross-trial distinction, covers externalized file-system state and agent memory-loss failure, and cites the agent-memory survey (SRC-137) as its source. A separate entry would be a near-duplicate. Resolved by alias rather than a split, so the term stays findable: agent memory, cross-session memory and what does the agent remember all resolve there. The register derives the pointer from that alias, so retargeting the alias moves the pointer. |
| [Agent Skills](../concepts/agent-skills.md) | `established` | yes | RENAMED from "Skill" and published Sep 7 2026, resolving the vendor status — the bare word collided with Alexa Skills and with ordinary English. Cleared the gate ON USAGE rather than on governance: originated at Anthropic, released as an open standard, now implemented by roughly 45 clients including direct competitors (OpenAI Codex, Gemini CLI, GitHub Copilot, VS Code, Mistral, Cursor, Databricks, Snowflake). A different establishment route from A2A, which cleared on foundation governance with thin usage. |
| [Agentic Design Patterns](../concepts/agentic-design-patterns.md) | `emerging` | yes | RENAMED from "Agentic Design" and published Sep 7 2026 as `emerging`. This row's caution was HALF right: "agentic design" is not a settled discipline, but "agentic design PATTERNS" is real vocabulary with two independent anchor catalogs — Ng's four (The Batch, Mar 2024) and Anthropic's workflow set. They do not match, and no canonical list exists, which is exactly why it ships emerging rather than established. Check 4: Orchestration holds the workflow-versus-agentic distinction but no pattern catalog, so this is a real gap. ⚠️ The oversight-profile table is the wiki's own framing, not a finding — no source organizes patterns by where refusal can occur. |
| Agentic Pattern | `covered` | **covered by [Agentic Design Patterns](../concepts/agentic-design-patterns.md)** | COVERED by Agentic Design Patterns — decided Sep 7 2026, confirming this row's own caution that the two were likely redundant. That entry's technical definition literally defines this term, and it already carried "agentic patterns" as an alias; the exact singular form was added so it resolves. No separate entry: the reasons for filing the parent `emerging` — Ng's four-pattern catalog and Anthropic's do not match, and no canonical list exists — apply to this row unchanged. Folded by alias, so the term stays findable. |
| [AI Agent](../concepts/ai-agent.md) | `established` | yes |  |
| [AI Benchmarking](../concepts/ai-benchmarking.md) | `established` | yes |  |
| [AI Disclosure (Attribution)](../concepts/ai-disclosure-attribution.md) | `established` | yes |  |
| [AI Gateway](../concepts/ai-gateway.md) | `established` | yes | RENAMED from "LLM Mesh" and published Sep 7 2026, resolving the vendor status exactly as this row's earlier note prescribed. The concept is implemented independently of any model vendor (LiteLLM, Kong, Envoy, APISIX, Portkey, Bifrost, Cloudflare, OpenRouter), so it publishes under the neutral name with Dataiku's LLM Mesh cited as one vendor's term for it. ⚠️ The old essence described multi-model collaboration — a different concept already held by Multi-Agent Systems — and has been rewritten, as the earlier note required. |
| [AI Governance](../concepts/ai-governance.md) | `established` | yes |  |
| [AI Incident (Reporting)](../concepts/ai-incident-reporting.md) | `established` | yes |  |
| [AI Literacy](../concepts/ai-literacy.md) | `established` | yes |  |
| [AI Management System (ISO 42001)](../concepts/ai-management-system-iso-42001.md) | `established` | yes |  |
| [AI Use Case](../concepts/ai-use-case.md) | `established` | yes |  |
| Algorithmic Impact Assessment | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Alignment (AI Systems)](../concepts/alignment-ai-systems.md) | `established` | yes |  |
| Anonymization | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Anthropomorphism (AI)](../concepts/anthropomorphism-ai.md) | `established` | yes |  |
| APIs (Application Programming Interfaces) | `covered` | **covered by [Tool Use](../concepts/tool-use.md)** | COVERED by Tool Use — decided Sep 7 2026. Also caught by CONTRIBUTING's scope exclusion: terms well-defined elsewhere that add no distinctive governance, literacy or design insight. APIs are general software vocabulary, exhaustively documented; the two AI-specific senses are already held — an AI calling out to an API is Tool Use (which already carried the alias "API calls from AI"), and calling a model provider's API is AI Gateway plus Inference. An entry would restate a textbook definition the corpus already covers in AI-specific form. Folded by alias. |
| [Audit Trail (AI)](../concepts/audit-trail-ai.md) | `established` | yes |  |
| Automated Decision-Making | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Automation Bias](../concepts/automation-bias.md) | `established` | yes |  |
| [Bias (AI Systems)](../concepts/bias-ai-systems.md) | `established` | yes |  |
| [Black Box](../concepts/black-box.md) | `established` | yes |  |
| [Bluewashing](../concepts/bluewashing.md) | `established` | yes |  |
| Canary Deployment | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Catastrophic Forgetting](../concepts/catastrophic-forgetting.md) | `established` | yes | ESTABLISHED — published Sep 8 2026. Named since McCloskey & Cohen 1989 (SRC-286); mechanism from French's stability-plasticity framing (SRC-287); mitigation and its cost from Kirkpatrick et al. (SRC-288). ⚠️ Term normalized to title case here so it matches the entry title — the export gate compares exact strings. Governance hook: a fine-tune is tested for what it was meant to add, never for what it may have removed, and refusals are learned behavior that can be forgotten. |
| Change Management | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Checkpointing | `established` | not yet |  |
| Class Imbalance | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Cognitive Offloading & Deskilling](../concepts/cognitive-offloading-deskilling.md) | `established` | yes |  |
| [Compliance (AI Systems)](../concepts/compliance-ai-systems.md) | `established` | yes |  |
| [Concealing Uncertainty](../concepts/concealing-uncertainty.md) | `established` | yes |  |
| [Confidence vs Accuracy](../concepts/confidence-vs-accuracy.md) | `established` | yes |  |
| Constitutional AI | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Content Provenance & Watermarking (C2PA)](../concepts/content-provenance-watermarking.md) | `established` | yes |  |
| [Context (AI Systems)](../concepts/context-ai-systems.md) | `established` | yes |  |
| [Context Compaction](../concepts/context-compaction.md) | `established` | yes | RENAMED from "Compact" and published Sep 7 2026, resolving the vendor status. Compaction is documented as a first-class concept by Microsoft's Agent Framework and studied in named 2026 research, so the term is in independent use — it was only Anthropic's product vocabulary as the bare word "Compact". Published under the neutral name, citing implementations rather than any one product. |
| [Context Engineering](../concepts/context-engineering.md) | `established` | yes |  |
| Context Framing | `covered` | **covered by [Context Engineering](../concepts/context-engineering.md)** | COVERED by Context Engineering — decided Sep 7 2026, confirming this row's own caution. FAILS CHECK 2: filtering for independent use leaves a single LinkedIn post using "context framing" as a term, with an idiosyncratic definition unlike this row's essence; the field consolidated on CONTEXT ENGINEERING (Karpathy, June 2025) and the literature uses that. The concept — how presentation and structure shape behavior — is held between Context Engineering (the information environment) and Prompt Engineering (the form of instructions), with position effects in Context Window. ⚠️ Prompt Engineering carried a Related-concepts promise to this term; removed, since that entry already links Context Engineering with the same distinction one line above. |
| [Context Window](../concepts/context-window.md) | `established` | yes |  |
| [Continuous Feedback & Improvement](../concepts/continuous-feedback-improvement.md) | `established` | yes |  |
| [Copyright & AI Output](../concepts/copyright-ai-output.md) | `established` | yes |  |
| Cross-Validation | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Curse of Knowledge (AI Context)](../concepts/curse-of-knowledge-ai-context.md) | `established` | yes |  |
| Dangerous Capability | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Data Labeling | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Data Leakage (AI Systems)](../concepts/data-leakage-ai-systems.md) | `established` | yes |  |
| [Data Leakage (Model Evaluation)](../concepts/data-leakage-model-evaluation.md) | `established` | yes |  |
| [Data Minimization](../concepts/data-minimization.md) | `established` | yes |  |
| Data Poisoning | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Data Provenance / Lineage](../concepts/data-provenance-lineage.md) | `established` | yes |  |
| [Data Quality](../concepts/data-quality.md) | `established` | yes |  |
| Data Retention | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Deception (AI Systems)](../concepts/deception-ai-systems.md) | `established` | yes |  |
| [Determinism vs Probabilism](../concepts/determinism-vs-probabilism.md) | `established` | yes |  |
| Differential Privacy | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Direct Preference Optimization | `covered` | **covered by [RLHF (Reinforcement Learning from Human Feedback)](../concepts/rlhf.md)** | COVERED by RLHF — decided Sep 8 2026. That entry's technical definition already explains DPO in mechanical terms (a similar result without a separate reward model) and states that the governance question — whose preferences — is identical across RLHF, DPO and RLAIF, which it treats as one family. It also revisits DPO in its confidence section. This clears the alias test: the target DEFINES the term rather than merely mentioning it. The full term was added to RLHF's aliases so it resolves. |
| Disaster Recovery | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Domain](../concepts/domain.md) | `established` | yes |  |
| Dual Use | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Edge AI](../concepts/edge-ai.md) | `established` | yes |  |
| [Embeddings](../concepts/embeddings.md) | `established` | yes |  |
| [Environmental Cost of AI](../concepts/environmental-cost-of-ai.md) | `established` | yes | ESTABLISHED — published Sep 7 2026. Clears all four checks on independent use across intergovernmental, academic and press sources. ⚠️ SOURCING CAUTION, which is this entry's main hazard: published figures vary by large factors depending on boundary choices (power generation included or not, embodied hardware counted or not, training amortized or not), so numbers from different sources are frequently not comparable. Electricity figures from the IEA (SRC-277); water from Li et al. (SRC-278), which are ESTIMATES and must be cited as such. The entry's most confident claim is the structural one — that providers do not publish per-request energy, so an organization cannot compute its own footprint while reporting expectations rise. |
| [Evaluation (AI Systems)](../concepts/evaluation.md) | `established` | yes |  |
| [Explainability (XAI)](../concepts/explainability-xai.md) | `established` | yes |  |
| [Failure Modes (AI Systems)](../concepts/failure-modes-ai-systems.md) | `established` | yes |  |
| False Negative | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| False Positive | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Federated Learning | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Fine-tuning](../concepts/fine-tuning.md) | `established` | yes |  |
| Flow Engineering | `covered` | **covered by [Orchestration (AI Systems)](../concepts/orchestration-ai-systems.md)** | COVERED by Orchestration (AI Systems) — decided Sep 7 2026. FAILS CHECK 2 as this row instructed: filtering the originator's domains leaves only the AlphaCodium paper itself, its repo, and blog write-ups of it; no independent group uses the term. The concept is thriving in 2026 under agentic workflows, and Orchestration already carries it — workflow, pipeline and chaining steps are its aliases, and it has the workflow-versus-agentic distinction. Folded by alias. |
| [Frontier AI (Frontier Model)](../concepts/frontier-ai.md) | `established` | yes |  |
| [Fundamental Rights Impact Assessment (FRIA)](../concepts/fundamental-rights-impact-assessment.md) | `established` | yes |  |
| [Grounding](../concepts/grounding.md) | `established` | yes |  |
| [Guardrails (AI Systems)](../concepts/guardrails-ai-systems.md) | `established` | yes |  |
| [Hallucination](../concepts/hallucination.md) | `established` | yes |  |
| [Harness Paradigm](../concepts/harness-paradigm.md) | `emerging` | yes | The term "agent harness" is established in practitioner literature (Böckeler; Osmani); the paradigm framing itself is not yet settled across independent sources. |
| [Human Responsibility in AI Use](../concepts/human-responsibility-in-ai-use.md) | `established` | yes |  |
| [Human-in-the-Loop (HITL)](../concepts/human-in-the-loop.md) | `established` | yes |  |
| [Human–AI Collaboration Model](../concepts/human-ai-collaboration-model.md) | `established` | yes |  |
| [Human–LLM Communication Skills](../concepts/human-llm-communication-skills.md) | `emerging` | yes | Component competencies are well grounded, but there is no established assessment for the competency as a whole. |
| [Inference](../concepts/inference.md) | `established` | yes |  |
| Instantiation (AI Systems) | `covered` | **covered by [Context (AI Systems)](../concepts/context-ai-systems.md)** | COVERED by Context (AI Systems) — decided Sep 7 2026, confirming the caution this row already carried. That entry states it directly: context is assembled fresh for every response, each generation starts from whatever was assembled for it, and apparent memory is context reconstructed and re-sent. That is this term's seed essence. A separate entry would restate it. Folded by alias, so the term stays findable. |
| Inter-Rater Reliability | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Jailbreak](../concepts/jailbreak.md) | `established` | yes |  |
| [Knowledge Base](../concepts/knowledge-base.md) | `established` | yes |  |
| [Knowledge Cutoff](../concepts/knowledge-cutoff.md) | `established` | yes |  |
| [Knowledge Graphs](../concepts/knowledge-graphs.md) | `established` | yes |  |
| LangChain | `declined` | **no — declined** | DECLINED Sep 6 2026 by the author. A named open-source product, not a concept — CONTRIBUTING already excludes product documentation. Unlike the vendor rows there is nothing to rename: chaining model calls, tools and memory is already covered by Orchestration (AI Systems). Row kept deliberately, so the rejection stays visible rather than silent. |
| [Large Language Models (LLMs)](../concepts/large-language-models.md) | `established` | yes |  |
| [Latency (AI Systems)](../concepts/latency-ai-systems.md) | `established` | yes | ESTABLISHED — published Sep 7 2026. A standard performance term across computing, with the AI-specific reading being that generation time scales with output length. The only DOUBLY-PROMISED term in the corpus: both Edge AI and Scalability (AI Systems) pointed at it before it existed. Human thresholds from Nielsen (SRC-279, attributing Miller 1968 and Card et al. 1991); the percentiles-over-means argument from Dean & Barroso, The Tail at Scale (SRC-280). Central governance hook: SPEED COMPETES WITH CHECKS — under latency pressure the first thing removed is always a check whose absence nobody sees. |
| [LLM-as-Judge](../concepts/llm-as-judge.md) | `established` | yes |  |
| [Local LLMs](../concepts/local-llms.md) | `established` | yes |  |
| [Mechanistic Interpretability](../concepts/mechanistic-interpretability.md) | `established` | yes |  |
| Membership Inference | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Memory (AI Systems)](../concepts/memory-ai-systems.md) | `established` | yes |  |
| [Metaprompting](../concepts/metaprompting.md) | `emerging` | yes | EMERGING, and the instability is in the term rather than the practice — published Sep 7 2026. Research found THREE competing senses in active use: (1) using a model to generate or refine a prompt, the practitioner-dominant sense behind vendor prompt-improver features; (2) structural scaffolding — supplying the shape of a solution rather than examples of one (Zhang, Yuan & Yao, arXiv 2311.11482, SRC-281), the only sense with a clear published definition; (3) self-critique loops, the weakest attachment to the name and better known as self-refinement. The entry names all three rather than picking one. ⚠️ This row's earlier essence described sense 3 only, as its own caution predicted; rewritten against the entry. Narrow this entry when the field consolidates, most likely on sense 1. |
| Mixture of Experts | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Model Card / System Card](../concepts/model-card-system-card.md) | `established` | yes |  |
| Model distillation | `established` | not yet |  |
| Model Extraction | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Model Inversion | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Model Version & Update](../concepts/model-version-update.md) | `established` | yes |  |
| [Model/Data Drift](../concepts/model-data-drift.md) | `established` | yes |  |
| [Moral Crumple Zone](../concepts/moral-crumple-zone.md) | `established` | yes |  |
| [Multi-Agent Systems](../concepts/multi-agent-systems.md) | `established` | yes |  |
| [Multimodal AI](../concepts/multimodal-ai.md) | `established` | yes |  |
| [NLP](../concepts/nlp.md) | `established` | yes |  |
| Notified Body | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Observability (AI Systems)](../concepts/observability.md) | `established` | yes |  |
| [Ontology](../concepts/ontology.md) | `established` | yes | Published Sep 7 2026. Clears check 1 on a formal standard rather than on usage: OWL 2 is a W3C Recommendation, and Gruber (1993) is the canonical definition. ⚠️ CHECK 4 ALMOST SAID "COVERED" AND WOULD HAVE BEEN WRONG: `ontology` was already an alias of Knowledge Graphs, but that entry mentions a schema only three times, always as a prerequisite or a cost — it never defines one. An alias to an entry that merely MENTIONS a term conceals the gap instead of filling it, and hides it from both the promise sweep and the gap report. Alias moved here; Knowledge Graphs now carries a Related-concepts pointer stating the schema/instance layer split. Score deliberately blank — author's call. |
| [Operational Readiness (AI)](../concepts/operational-readiness-ai.md) | `established` | yes |  |
| [Orchestration (AI Systems)](../concepts/orchestration-ai-systems.md) | `established` | yes |  |
| [Overfitting](../concepts/overfitting.md) | `established` | yes | ESTABLISHED — published Sep 8 2026, and the entry covers BOTH ends of the axis: UNDERFITTING is folded here as an alias, since Geman et al. (SRC-282) define the two as one bias/variance trade-off rather than separate faults. ⚠️ The entry deliberately gives no rule for when a large model will memorize, because double descent (SRC-283, SRC-284) breaks the size-implies-overfitting intuition in both directions. At LLM scale the live risk is memorization surfacing as privacy and copyright exposure (SRC-150), not a poor score. |
| Overrefusal | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Ownership (AI Systems)](../concepts/ownership-ai-systems.md) | `established` | yes |  |
| [Performativity (LLMs)](../concepts/performativity-llms.md) | `emerging` | yes | Performativity is established in philosophy (Austin) and in ML as 'performative prediction' (Perdomo et al.); its application to LLM effects on human language is recent and still settling. |
| [Permission Model (AI)](../concepts/permission-model-ai.md) | `established` | yes |  |
| [Persistent Synthesis](../concepts/persistent-synthesis.md) | `emerging` | yes | Rests on a widely validated practitioner insight; the extended framework carries known specification gaps. |
| [Power Seeking](../concepts/power-seeking.md) | `established` | yes |  |
| [Pre-training](../concepts/pre-training.md) | `established` | yes |  |
| [Privacy (AI Systems)](../concepts/privacy-ai-systems.md) | `established` | yes |  |
| [Prompt Chaining](../concepts/prompt-chaining.md) | `established` | yes | ESTABLISHED — published Sep 8 2026. Not covered by Orchestration, which defines the control layer but never the technique; Agentic Design Patterns only names it in a list. Founding definition and the transparency finding from Wu, Terry & Cai (SRC-290, CHI 2022): people edited intermediate results rather than accepting one opaque answer. ⚠️ Distinct from CHAIN-OF-THOUGHT — separate calls with real artifacts, not generated reasoning text. Governance hook: decomposition adds failure points and no checks. |
| [Prompt Engineering](../concepts/prompt-engineering.md) | `established` | yes |  |
| [Prompt Injection](../concepts/prompt-injection.md) | `established` | yes |  |
| Pseudonymization | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Quantization | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [RACI](../concepts/raci.md) | `established` | yes |  |
| [Reasoning Models / Test-Time Compute](../concepts/reasoning-models.md) | `established` | yes |  |
| [Recurrent Depth](../concepts/recurrent-depth.md) | `emerging` | yes | Spelling corrected from "Recurring Depth", which no source uses. Coined by Geiping et al. (NeurIPS 2025); independently used by a separate group (Recurrent-Depth VLA, 2026). Emerging rather than established on naming — recurrent depth / looped transformer / depth-recurrent compete for one mechanism. ⚠️ Do not state as fact that OpenAI's Astra uses it: press reporting, unconfirmed by OpenAI. Fills a real gap — reasoning moves into latent states with no trace to read. |
| [Recursive Self-Improvement](../concepts/recursive-self-improvement.md) | `established` | yes |  |
| [Red Teaming](../concepts/red-teaming.md) | `established` | yes |  |
| Redress | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Reinforcement Learning (RL)](../concepts/reinforcement-learning.md) | `established` | yes |  |
| [Retrieval-Augmented Generation (RAG)](../concepts/rag.md) | `established` | yes |  |
| [Reward Hacking (Specification Gaming)](../concepts/reward-hacking.md) | `established` | yes |  |
| [RLHF (Reinforcement Learning from Human Feedback)](../concepts/rlhf.md) | `established` | yes |  |
| Sampling Bias | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Sandboxing](../concepts/sandboxing.md) | `established` | yes |  |
| [Scalability (AI Systems)](../concepts/scalability-ai-systems.md) | `established` | yes |  |
| [Scalable Oversight](../concepts/scalable-oversight.md) | `established` | yes |  |
| Selection Bias | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Service Level Objective | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Shadow AI](../concepts/shadow-ai.md) | `established` | yes |  |
| [Small Language Models (SLMs)](../concepts/small-language-models.md) | `established` | yes |  |
| Statistical Significance | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| Supply Chain Risk | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Sycophancy (LLMs)](../concepts/sycophancy-llms.md) | `established` | yes |  |
| [Synthetic Data](../concepts/synthetic-data.md) | `established` | yes |  |
| [Synthetic Media (Deepfakes)](../concepts/synthetic-media-deepfakes.md) | `established` | yes |  |
| [System Prompt](../concepts/system-prompt.md) | `established` | yes |  |
| [Systemic Risk (AI)](../concepts/systemic-risk-ai.md) | `established` | yes |  |
| [Tacit Knowledge](../concepts/tacit-knowledge.md) | `established` | yes |  |
| [Temperature (LLMs)](../concepts/temperature-llms.md) | `established` | yes |  |
| Third-Party Audit | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Tokenization](../concepts/tokenization.md) | `established` | yes |  |
| [Tool Use](../concepts/tool-use.md) | `established` | yes |  |
| Total Cost of Ownership | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Training Data](../concepts/training-data.md) | `established` | yes |  |
| Transfer Learning | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Transformers](../concepts/transformers.md) | `established` | yes |  |
| [Types of AI Systems](../concepts/types-of-ai-systems.md) | `established` | yes |  |
| Underfitting | `covered` | **covered by [Overfitting](../concepts/overfitting.md)** | COVERED by Overfitting — decided Sep 8 2026. Not redundancy but structure: Geman, Bienenstock & Doursat (SRC-282) define overfitting and underfitting as the two ends of ONE bias/variance axis, and the Overfitting entry's technical definition names and explains underfitting in those terms. Splitting them would mean two entries describing one dial. Underfitting is also the easy case — it fails visibly everywhere — which is why the axis is named for the dangerous end. Folded by alias. |
| [Value Realization (AI)](../concepts/value-realization-ai.md) | `emerging` | yes | Standard business term; the AI-specific application rests on evidence from prior general-purpose technologies rather than from AI. |
| Vendor Lock-in | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Verification](../concepts/verification.md) | `established` | yes |  |
| Whistleblowing | `unassessed` | not yet | Added Sep 8 2026 by the semi-annual vocabulary check — on an outside reference list, absent from the whole corpus. Not yet triaged; `covered` or `declined` are live outcomes. Score blank pending author assessment. |
| [Zero-shot / Few-shot Learning](../concepts/zero-shot-few-shot-learning.md) | `established` | yes |  |

---

*Generated from the term tracker by `scripts/build.py write`. Do not edit by hand.*
