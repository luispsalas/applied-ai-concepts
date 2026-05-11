# Context Engineering

## One-line essence
Designing what an AI model receives is as important as the model itself.

---

## Technical definition

Context engineering is the discipline of constructing, structuring, and managing the inputs provided to a language model to maximize the relevance, accuracy, and usefulness of its outputs. It encompasses system prompt authoring, retrieval strategy, memory architecture, information sequencing across multi-turn interactions, and the deliberate exclusion of irrelevant content.

Where prompt engineering focuses on the form of individual instructions, context engineering addresses the full information environment the model operates within — including what is present, what is absent, and in what order things appear.

---

## Plain-language version

An AI model can only work with what you give it. Context engineering is the skill of giving it the right information, in the right form, at the right time.

It shifts the question from *"what should I ask?"* to *"what does the model need to know to help me well?"* — and that shift changes everything about how you design AI workflows.

Think of it like briefing a consultant before a meeting. The more precisely you describe the situation, the constraints, and the decision at hand, the more useful their input will be. Context engineering is the practice of building that brief systematically.

---

## AI literacy notes

Context engineering shifts the primary leverage point from the model to the operator. A well-designed context can compensate for model limitations; a poorly designed one will degrade even the most capable model's outputs.

This has two practical implications:

1. **For individuals:** The skill gap between casual AI use and effective AI use is largely a context gap — not a prompt-writing gap.
2. **For organizations:** Deploying AI effectively requires defining what information the system should have access to, in what form, and with what constraints — before thinking about which model to use.

Context engineering is also where governance enters. Decisions about what context an AI system receives — and what it cannot access — are governance decisions with real consequences.

---

## Governance notes

**Core question:** Who controls what information the model receives — and is that control documented?

**Watch for:**
- Context treated as disposable: not logged, not versioned, and therefore not auditable. If you cannot reconstruct what context the model received, you cannot investigate or explain its outputs.
- Sensitive or restricted data entering the context window without access controls. Context construction decisions are data access decisions.
- Context decay: injected information (system prompts, knowledge base entries, policy documents) going stale without detection — presenting outdated content with the same authority as current information.

**Practice:**
- Log what context was injected per session or request. This is the minimum required for output auditability.
- Treat context construction as a governed data access decision: who or what can inject information into the context window should be defined and controlled, not assumed.

**Key accountability owner:** Context owner — the role responsible for defining what information the model is given access to, in what form, and under what access controls.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** Active practitioner consensus since 2023. The term has stabilized; the discipline continues to deepen as agentic and multi-step systems become more common.

---

## Related concepts

- [Prompt Engineering](prompt-engineering.md) — operates within context; context engineering sets the environment prompt engineering works in
- [Harness Paradigm](harness-paradigm.md) — the harness is the primary mechanism for managing context at the system level
- [Persistent Synthesis](persistent-synthesis.md) — a wiki is itself an exercise in context engineering: structured knowledge as reusable input
- Retrieval-Augmented Generation (RAG) — a technical pattern for dynamic context injection
- System Prompt — the baseline layer of engineered context in any deployed model
- Context Window — the physical constraint context engineering must work within

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-011 | Karpathy, Andrej — *"Context engineering is the delicate art and science..."* (X post, 2025) · [link](https://x.com/karpathy/status/1937902205765607626) | Canonical definition: "context engineering is the delicate art and science of filling the context window with just the right information for the next step." Draws the key distinction from prompt engineering — prompts are short task descriptions; context engineering is the full information environment designed for production systems. |
| SRC-012 | LangChain — *Context Engineering for Agents* (blog, 2025) · [link](https://blog.langchain.com/context-engineering-for-agents/) | Practitioner framework for context engineering in agentic systems; dynamic context construction at runtime; distinction from prompt engineering at the system design level. |
| SRC-007 | Karpathy, Andrej — *LLM Wiki* (gist, 2023) · [link](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Synthesis philosophy informing the wiki-as-context-architecture framing; context as a compounding artifact. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core design discipline for any AI system or workflow. Informs system prompt design, memory strategy, retrieval architecture, and harness configuration. |
| **Organizational** | The primary skill gap between "using AI tools" and "deploying AI effectively." Understanding context engineering reframes AI adoption from a tool problem to an information design problem. |
| **Client-facing** | Explains why two people using the same AI tool get very different results — and what can be done about it. |
| **LLM-native** | Foundation concept. Every other concept in this wiki is downstream of context quality. |

---

*Last updated: v1.1 · May 2026*
