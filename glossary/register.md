# Term register

Every term this wiki tracks, with its status — **including the ones that are not published, and the ones that will not be.**

The field names things faster than it settles them, and a glossary that repeats every new label without comment is a list of buzzwords. So each term is judged on whether it is a *real term*. That is a separate question from how good the evidence is for the claims inside an entry, which each entry states for itself in its own confidence level.

**134 terms tracked — 116 published, 18 not.** See [how terms are admitted](../CONTRIBUTING.md#term-status--the-admission-test).

| Status | Meaning | Count |
|---|---|---|
| `established` | Recognized term of art, in independent use. | 120 |
| `emerging` | Real and in use, but definitions still vary between sources. | 10 |
| `declined` | Considered and turned down — not a term this wiki will publish. | 1 |
| `covered` | A real term, already covered by another entry — findable there as an alias. | 3 |

---

| Term | Status | Published | Notes |
|---|---|---|---|
| [Accountability (AI Systems)](../concepts/accountability-ai-systems.md) | `established` | yes |  |
| [Agency (AI Systems)](../concepts/agency-ai-systems.md) | `established` | yes |  |
| [Agent Hooks](../concepts/agent-hooks.md) | `established` | yes | RENAMED from "Hook" and published Sep 7 2026, resolving the vendor status. Every major agent runtime has independently converged on the pattern — Claude Code, OpenAI Codex CLI, LangChain/LangGraph, Google ADK, AutoGen, Semantic Kernel — so it is convergent, not proprietary. The entry's contribution is the distinction most documentation buries: can the hook BLOCK, or only observe? |
| [Agent Interoperability (A2A)](../concepts/agent-interoperability-a2a.md) | `established` | yes |  |
| Agent Memory | `covered` | **covered by [Memory (AI Systems)](../concepts/memory-ai-systems.md)** | COVERED by Memory (AI Systems) — decided Sep 7 2026 under admission check 4. A real established term, but that entry already is this one: it uses the in-trial / cross-trial distinction, covers externalized file-system state and agent memory-loss failure, and cites the agent-memory survey (SRC-137) as its source. A separate entry would be a near-duplicate. Resolved by alias rather than a split, so the term stays findable: agent memory, cross-session memory and what does the agent remember all resolve there. The register derives the pointer from that alias, so retargeting the alias moves the pointer. |
| [Agent Skills](../concepts/agent-skills.md) | `established` | yes | RENAMED from "Skill" and published Sep 7 2026, resolving the vendor status — the bare word collided with Alexa Skills and with ordinary English. Cleared the gate ON USAGE rather than on governance: originated at Anthropic, released as an open standard, now implemented by roughly 45 clients including direct competitors (OpenAI Codex, Gemini CLI, GitHub Copilot, VS Code, Mistral, Cursor, Databricks, Snowflake). A different establishment route from A2A, which cleared on foundation governance with thin usage. |
| Agentic Design | `emerging` | not yet | "Agentic" is now widespread, but "agentic design" as a named discipline is not settled — usage varies between practitioners and no standard formulation exists. |
| Agentic Pattern | `emerging` | not yet | "Agentic pattern" is used loosely as a synonym for agent design templates; no canonical catalogue exists. Likely redundant with Agentic Design — decide whether both are needed. |
| [AI Agent](../concepts/ai-agent.md) | `established` | yes |  |
| [AI Benchmarking](../concepts/ai-benchmarking.md) | `established` | yes |  |
| [AI Disclosure (Attribution)](../concepts/ai-disclosure-attribution.md) | `established` | yes |  |
| [AI Gateway](../concepts/ai-gateway.md) | `established` | yes | RENAMED from "LLM Mesh" and published Sep 7 2026, resolving the vendor status exactly as this row's earlier note prescribed. The concept is implemented independently of any model vendor (LiteLLM, Kong, Envoy, APISIX, Portkey, Bifrost, Cloudflare, OpenRouter), so it publishes under the neutral name with Dataiku's LLM Mesh cited as one vendor's term for it. ⚠️ The old essence described multi-model collaboration — a different concept already held by Multi-Agent Systems — and has been rewritten, as the earlier note required. |
| [AI Governance](../concepts/ai-governance.md) | `established` | yes |  |
| [AI Incident (Reporting)](../concepts/ai-incident-reporting.md) | `established` | yes |  |
| [AI Literacy](../concepts/ai-literacy.md) | `established` | yes |  |
| [AI Management System (ISO 42001)](../concepts/ai-management-system-iso-42001.md) | `established` | yes |  |
| [AI Use Case](../concepts/ai-use-case.md) | `established` | yes |  |
| [Alignment (AI Systems)](../concepts/alignment-ai-systems.md) | `established` | yes |  |
| [Anthropomorphism (AI)](../concepts/anthropomorphism-ai.md) | `established` | yes |  |
| APIs (Application Programming Interfaces) | `established` | not yet |  |
| [Audit Trail (AI)](../concepts/audit-trail-ai.md) | `established` | yes |  |
| [Automation Bias](../concepts/automation-bias.md) | `established` | yes |  |
| [Bias (AI Systems)](../concepts/bias-ai-systems.md) | `established` | yes |  |
| [Black Box](../concepts/black-box.md) | `established` | yes |  |
| [Bluewashing](../concepts/bluewashing.md) | `established` | yes |  |
| Catastrophic forgetting | `established` | not yet |  |
| Checkpointing | `established` | not yet |  |
| [Cognitive Offloading & Deskilling](../concepts/cognitive-offloading-deskilling.md) | `established` | yes |  |
| [Compliance (AI Systems)](../concepts/compliance-ai-systems.md) | `established` | yes |  |
| [Concealing Uncertainty](../concepts/concealing-uncertainty.md) | `established` | yes |  |
| [Confidence vs Accuracy](../concepts/confidence-vs-accuracy.md) | `established` | yes |  |
| [Content Provenance & Watermarking (C2PA)](../concepts/content-provenance-watermarking.md) | `established` | yes |  |
| [Context (AI Systems)](../concepts/context-ai-systems.md) | `established` | yes |  |
| [Context Compaction](../concepts/context-compaction.md) | `established` | yes | RENAMED from "Compact" and published Sep 7 2026, resolving the vendor status. Compaction is documented as a first-class concept by Microsoft's Agent Framework and studied in named 2026 research, so the term is in independent use — it was only Anthropic's product vocabulary as the bare word "Compact". Published under the neutral name, citing implementations rather than any one product. |
| [Context Engineering](../concepts/context-engineering.md) | `established` | yes |  |
| Context Framing | `emerging` | not yet | Framing effects are established in psychology; "context framing" as a prompting sub-skill is practitioner vocabulary and overlaps Context Engineering — check for redundancy before drafting. |
| [Context Window](../concepts/context-window.md) | `established` | yes |  |
| [Continuous Feedback & Improvement](../concepts/continuous-feedback-improvement.md) | `established` | yes |  |
| [Copyright & AI Output](../concepts/copyright-ai-output.md) | `established` | yes |  |
| [Curse of Knowledge (AI Context)](../concepts/curse-of-knowledge-ai-context.md) | `established` | yes |  |
| [Data Leakage (AI Systems)](../concepts/data-leakage-ai-systems.md) | `established` | yes |  |
| [Data Leakage (Model Evaluation)](../concepts/data-leakage-model-evaluation.md) | `established` | yes |  |
| [Data Minimization](../concepts/data-minimization.md) | `established` | yes |  |
| [Data Provenance / Lineage](../concepts/data-provenance-lineage.md) | `established` | yes |  |
| [Data Quality](../concepts/data-quality.md) | `established` | yes |  |
| [Deception (AI Systems)](../concepts/deception-ai-systems.md) | `established` | yes |  |
| [Determinism vs Probabilism](../concepts/determinism-vs-probabilism.md) | `established` | yes |  |
| Direct Preference Optimization | `established` | not yet |  |
| [Domain](../concepts/domain.md) | `established` | yes |  |
| [Edge AI](../concepts/edge-ai.md) | `established` | yes |  |
| [Embeddings](../concepts/embeddings.md) | `established` | yes |  |
| Environmental Cost of AI | `established` | not yet |  |
| [Evaluation (AI Systems)](../concepts/evaluation.md) | `established` | yes |  |
| [Explainability (XAI)](../concepts/explainability-xai.md) | `established` | yes |  |
| [Failure Modes (AI Systems)](../concepts/failure-modes-ai-systems.md) | `established` | yes |  |
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
| [Jailbreak](../concepts/jailbreak.md) | `established` | yes |  |
| [Knowledge Base](../concepts/knowledge-base.md) | `established` | yes |  |
| [Knowledge Cutoff](../concepts/knowledge-cutoff.md) | `established` | yes |  |
| [Knowledge Graphs](../concepts/knowledge-graphs.md) | `established` | yes |  |
| LangChain | `declined` | **no — declined** | DECLINED Sep 6 2026 by the author. A named open-source product, not a concept — CONTRIBUTING already excludes product documentation. Unlike the vendor rows there is nothing to rename: chaining model calls, tools and memory is already covered by Orchestration (AI Systems). Row kept deliberately, so the rejection stays visible rather than silent. |
| [Large Language Models (LLMs)](../concepts/large-language-models.md) | `established` | yes |  |
| Latency (AI Systems) | `established` | not yet |  |
| [LLM-as-Judge](../concepts/llm-as-judge.md) | `established` | yes |  |
| [Local LLMs](../concepts/local-llms.md) | `established` | yes |  |
| [Mechanistic Interpretability](../concepts/mechanistic-interpretability.md) | `established` | yes |  |
| [Memory (AI Systems)](../concepts/memory-ai-systems.md) | `established` | yes |  |
| Metaprompting | `emerging` | not yet | Meta-prompting appears in the literature but definitions vary; the tracker essence describes a narrower self-critique technique than most usage. |
| [Model Card / System Card](../concepts/model-card-system-card.md) | `established` | yes |  |
| Model distillation | `established` | not yet |  |
| [Model Version & Update](../concepts/model-version-update.md) | `established` | yes |  |
| [Model/Data Drift](../concepts/model-data-drift.md) | `established` | yes |  |
| [Moral Crumple Zone](../concepts/moral-crumple-zone.md) | `established` | yes |  |
| [Multi-Agent Systems](../concepts/multi-agent-systems.md) | `established` | yes |  |
| [Multimodal AI](../concepts/multimodal-ai.md) | `established` | yes |  |
| [NLP](../concepts/nlp.md) | `established` | yes |  |
| [Observability (AI Systems)](../concepts/observability.md) | `established` | yes |  |
| [Ontology](../concepts/ontology.md) | `established` | yes | Published Sep 7 2026. Clears check 1 on a formal standard rather than on usage: OWL 2 is a W3C Recommendation, and Gruber (1993) is the canonical definition. ⚠️ CHECK 4 ALMOST SAID "COVERED" AND WOULD HAVE BEEN WRONG: `ontology` was already an alias of Knowledge Graphs, but that entry mentions a schema only three times, always as a prerequisite or a cost — it never defines one. An alias to an entry that merely MENTIONS a term conceals the gap instead of filling it, and hides it from both the promise sweep and the gap report. Alias moved here; Knowledge Graphs now carries a Related-concepts pointer stating the schema/instance layer split. Score deliberately blank — author's call. |
| [Operational Readiness (AI)](../concepts/operational-readiness-ai.md) | `established` | yes |  |
| [Orchestration (AI Systems)](../concepts/orchestration-ai-systems.md) | `established` | yes |  |
| Overfitting | `established` | not yet |  |
| [Ownership (AI Systems)](../concepts/ownership-ai-systems.md) | `established` | yes |  |
| [Performativity (LLMs)](../concepts/performativity-llms.md) | `emerging` | yes | Performativity is established in philosophy (Austin) and in ML as 'performative prediction' (Perdomo et al.); its application to LLM effects on human language is recent and still settling. |
| [Permission Model (AI)](../concepts/permission-model-ai.md) | `established` | yes |  |
| [Persistent Synthesis](../concepts/persistent-synthesis.md) | `emerging` | yes | Rests on a widely validated practitioner insight; the extended framework carries known specification gaps. |
| [Power Seeking](../concepts/power-seeking.md) | `established` | yes |  |
| [Pre-training](../concepts/pre-training.md) | `established` | yes |  |
| [Privacy (AI Systems)](../concepts/privacy-ai-systems.md) | `established` | yes |  |
| Prompt Chaining | `established` | not yet |  |
| [Prompt Engineering](../concepts/prompt-engineering.md) | `established` | yes |  |
| [Prompt Injection](../concepts/prompt-injection.md) | `established` | yes |  |
| [RACI](../concepts/raci.md) | `established` | yes |  |
| [Reasoning Models / Test-Time Compute](../concepts/reasoning-models.md) | `established` | yes |  |
| [Recurrent Depth](../concepts/recurrent-depth.md) | `emerging` | yes | Spelling corrected from "Recurring Depth", which no source uses. Coined by Geiping et al. (NeurIPS 2025); independently used by a separate group (Recurrent-Depth VLA, 2026). Emerging rather than established on naming — recurrent depth / looped transformer / depth-recurrent compete for one mechanism. ⚠️ Do not state as fact that OpenAI's Astra uses it: press reporting, unconfirmed by OpenAI. Fills a real gap — reasoning moves into latent states with no trace to read. |
| [Recursive Self-Improvement](../concepts/recursive-self-improvement.md) | `established` | yes |  |
| [Red Teaming](../concepts/red-teaming.md) | `established` | yes |  |
| [Reinforcement Learning (RL)](../concepts/reinforcement-learning.md) | `established` | yes |  |
| [Retrieval-Augmented Generation (RAG)](../concepts/rag.md) | `established` | yes |  |
| [Reward Hacking (Specification Gaming)](../concepts/reward-hacking.md) | `established` | yes |  |
| [RLHF (Reinforcement Learning from Human Feedback)](../concepts/rlhf.md) | `established` | yes |  |
| [Sandboxing](../concepts/sandboxing.md) | `established` | yes |  |
| [Scalability (AI Systems)](../concepts/scalability-ai-systems.md) | `established` | yes |  |
| [Scalable Oversight](../concepts/scalable-oversight.md) | `established` | yes |  |
| [Shadow AI](../concepts/shadow-ai.md) | `established` | yes |  |
| [Small Language Models (SLMs)](../concepts/small-language-models.md) | `established` | yes |  |
| [Sycophancy (LLMs)](../concepts/sycophancy-llms.md) | `established` | yes |  |
| [Synthetic Data](../concepts/synthetic-data.md) | `established` | yes |  |
| [Synthetic Media (Deepfakes)](../concepts/synthetic-media-deepfakes.md) | `established` | yes |  |
| [System Prompt](../concepts/system-prompt.md) | `established` | yes |  |
| [Systemic Risk (AI)](../concepts/systemic-risk-ai.md) | `established` | yes |  |
| [Tacit Knowledge](../concepts/tacit-knowledge.md) | `established` | yes |  |
| [Temperature (LLMs)](../concepts/temperature-llms.md) | `established` | yes |  |
| [Tokenization](../concepts/tokenization.md) | `established` | yes |  |
| [Tool Use](../concepts/tool-use.md) | `established` | yes |  |
| [Training Data](../concepts/training-data.md) | `established` | yes |  |
| [Transformers](../concepts/transformers.md) | `established` | yes |  |
| [Types of AI Systems](../concepts/types-of-ai-systems.md) | `established` | yes |  |
| Underfitting | `established` | not yet |  |
| [Value Realization (AI)](../concepts/value-realization-ai.md) | `emerging` | yes | Standard business term; the AI-specific application rests on evidence from prior general-purpose technologies rather than from AI. |
| [Verification](../concepts/verification.md) | `established` | yes |  |
| [Zero-shot / Few-shot Learning](../concepts/zero-shot-few-shot-learning.md) | `established` | yes |  |

---

*Generated from the term tracker by `scripts/build.py write`. Do not edit by hand.*
