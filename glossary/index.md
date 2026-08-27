# Glossary

Quick-reference index of all concepts. Follow links for full entries.

---

| Term | One-line essence |
|---|---|
| [AI Agent](../concepts/ai-agent.md) | A language model that doesn't just respond — it plans, acts, and iterates across multiple steps to complete a task |
| [AI Incident (Reporting)](../concepts/ai-incident-reporting.md) | A documented event where an AI system caused or nearly caused harm — now with legal deadlines to report it, not just fix it quietly |
| [AI Use Case](../concepts/ai-use-case.md) | A defined, bounded application of AI to a specific problem — the unit of design, risk assessment, and governance accountability |
| [AI Governance](../concepts/ai-governance.md) | The frameworks, policies, and accountability structures that determine who decides how AI systems behave — and who is answerable when they don't |
| [AI Literacy](../concepts/ai-literacy.md) | The competencies required to engage with, use, and govern AI systems responsibly — at an individual, team, and organizational level |
| [Accountability (AI Systems)](../concepts/accountability-ai-systems.md) | The principle that someone can be held answerable for an AI system's behavior and outcomes — and that answerable means they must explain, justify, and face consequences |
| [Audit Trail (AI)](../concepts/audit-trail-ai.md) | The structured record of what an AI system received, decided, and did — enabling accountability, compliance, and governance review after the fact |
| [Bias (AI Systems)](../concepts/bias-ai-systems.md) | Systematic errors that unfairly advantage or disadvantage certain groups — often inherited from training data, rarely visible in any single output |
| [Black Box](../concepts/black-box.md) | An AI system whose internal reasoning process cannot be observed or interpreted — even when its outputs can |
| [Compliance (AI Systems)](../concepts/compliance-ai-systems.md) | Meeting defined obligations for how AI systems are built, deployed, and operated — and being answerable for whether those obligations were actually met, not just documented |
| [Context Engineering](../concepts/context-engineering.md) | Designing what an AI model receives is as important as the model itself |
| [Context Window](../concepts/context-window.md) | The maximum amount of text an AI model can consider at once — a hard limit on what it can reason about when generating any given response |
| [Data Leakage (AI Systems)](../concepts/data-leakage-ai-systems.md) | When sensitive information from training data or context surfaces in model outputs — exposing what was never meant to be accessible |
| [Data Minimization](../concepts/data-minimization.md) | Collecting and keeping only the data a system actually needs — less data, less risk, lower cost |
| [Data Quality](../concepts/data-quality.md) | The fitness of data for its intended use — and the upstream constraint that determines the reliability of every AI system built on it |
| [Determinism vs Probabilism](../concepts/determinism-vs-probabilism.md) | Why AI models generate statistically likely outputs rather than fixed answers — the same input can produce different results |
| [Domain](../concepts/domain.md) | The specific field the AI is working in — what counts as a "good" or "wrong" answer depends entirely on the domain |
| [Evaluation (AI Systems)](../concepts/evaluation.md) | The structured practice of measuring whether an AI system does what it is supposed to do — before deployment and continuously in production |
| [Explainability (XAI)](../concepts/explainability-xai.md) | Describing, in terms a human can understand, why an AI system produced a specific output — a prerequisite for accountability |
| [Failure Modes (AI Systems)](../concepts/failure-modes-ai-systems.md) | The specific ways an AI system can go wrong — each requiring a different detection-and-response control |
| [Grounding](../concepts/grounding.md) | Anchoring model outputs to specific, verifiable sources — reducing hallucination by giving the model something real to reason from |
| [Guardrails (AI Systems)](../concepts/guardrails-ai-systems.md) | Technical and policy constraints that prevent an AI system from producing outputs or taking actions outside defined boundaries |
| [Hallucination](../concepts/hallucination.md) | AI models generate plausible-sounding content that is factually incorrect — confidently and without warning |
| [Harness Paradigm](../concepts/harness-paradigm.md) | Intelligence and control are separate layers — governance lives in the harness, not the model |
| [Human-in-the-Loop (HITL)](../concepts/human-in-the-loop.md) | A design pattern that keeps humans as decision authorities at critical points |
| [Human Responsibility in AI Use](../concepts/human-responsibility-in-ai-use.md) | The obligation to oversee AI decisions and be answerable for their outcomes does not transfer to the system — it remains with the humans who deploy, configure, and use it |
| [Jailbreak](../concepts/jailbreak.md) | Bypassing a model's safety training through crafted prompts rather than a technical flaw — getting it to do what it was trained to refuse |
| [Knowledge Base](../concepts/knowledge-base.md) | The collection of documents an AI can look up when answering — the quality of the library determines the quality of the answers |
| [Large Language Models (LLMs)](../concepts/large-language-models.md) | Neural networks trained on vast text corpora that generate language by predicting what comes next — the foundation of most modern AI assistants, tools, and agents |
| [Memory (AI Systems)](../concepts/memory-ai-systems.md) | How an AI remembers — what it keeps in a conversation, what carries over to future sessions, and what it reuses as learned skill |
| [Multi-Agent Systems](../concepts/multi-agent-systems.md) | Multiple AI agents with different roles working together on a task — coordination and division of labor instead of one model doing everything |
| [Observability](../concepts/observability.md) | The ability to understand what an AI system is doing — and reconstruct why — by examining what goes in, what comes out, and every action in between |
| [Ownership (AI Systems)](../concepts/ownership-ai-systems.md) | Explicit assignment of accountability for an AI system's outputs, data, and governance — defining who is responsible, not just who built it |
| [Permission Model (AI)](../concepts/permission-model-ai.md) | What an AI may do on its own, what needs human approval, and what is always off-limits — enforced, not requested |
| [Persistent Synthesis](../concepts/persistent-synthesis.md) | Knowledge compounds when contradictions are resolved — not when information is accumulated |
| [Privacy (AI Systems)](../concepts/privacy-ai-systems.md) | The rights and obligations that govern how personal data is used in AI training and deployment — and the organizational responsibility to uphold them |
| [Prompt Engineering](../concepts/prompt-engineering.md) | Structuring inputs to consistently elicit useful, accurate, and safe model outputs |
| [Prompt Injection](../concepts/prompt-injection.md) | A trick where someone hides malicious instructions in text the AI reads, hijacking its behavior — like a fake note slipped into a document that overrides the real instructions |
| [Reasoning Models / Test-Time Compute](../concepts/reasoning-models.md) | Models that spend extra computation "thinking" through a problem step by step before answering — trading speed for higher accuracy on hard tasks |
| [Red Teaming](../concepts/red-teaming.md) | Deliberately attacking your own AI system — probing for jailbreaks, data leaks, and harmful outputs before anyone else finds them |
| [Retrieval-Augmented Generation (RAG)](../concepts/rag.md) | A technique that grounds language model outputs in retrieved, verifiable information — reducing hallucination by giving the model current, specific content to work from |
| [Small Language Models (SLMs)](../concepts/small-language-models.md) | Language models small enough to run cheaply, locally, or at the edge — often the better fit for narrow, repetitive tasks |
| [System Prompt](../concepts/system-prompt.md) | The behind-the-scenes instructions that set how an AI behaves before you start talking to it — a soft control that steers, not a hard boundary |
| [Tool Use](../concepts/tool-use.md) | How an AI model acts on the world rather than just describing it — calling external functions, APIs, and data sources |
| [Types of AI Systems](../concepts/types-of-ai-systems.md) | A taxonomy of AI by capability and autonomy — from narrow task tools to general-purpose models — that determines governance, risk, and oversight |

---

*This index is maintained manually in Phase 1. Automation planned for Phase 2.*
