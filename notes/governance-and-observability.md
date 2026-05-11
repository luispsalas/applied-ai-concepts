# Governance & Observability Notes

## What this covers

This document collects governance implications, watch items, and observability patterns drawn from the core concepts in this wiki. Where concept entries answer *what is X*, this note answers *what do I need to control, monitor, and be accountable for when X is in play*.

Organized into three themes that cut across the six current concepts:

1. [Verification & Output Quality](#1-verification--output-quality)
2. [Context & Knowledge Governance](#2-context--knowledge-governance)
3. [System Control & Accountability](#3-system-control--accountability)

A cross-cutting [accountability checklist](#accountability-checklist) follows.

---

## 1. Verification & Output Quality

*Concepts: [Hallucination](../concepts/hallucination.md) · [Human-in-the-Loop (HITL)](../concepts/human-in-the-loop.md)*

### Watch items

- **Verification is selective when it should be structural.** Teams that only check outputs that "seem wrong" will miss hallucinations — because hallucinated outputs do not seem wrong. Verification must happen by design, not by suspicion.
- **Confidence of tone is mistaken for reliability.** A fluent, assertive AI output carries no more factual accuracy than a hedged one. Organizations that treat fluency as a quality signal are measuring the wrong thing.
- **AI explanations are treated as transparent.** When a model explains its reasoning, that explanation is itself a generated output subject to hallucination risk. A convincing rationale is not a verified one.
- **HITL erodes under volume pressure.** As AI throughput increases, human review is the first thing to compress. Systems designed without explicit review gates tend to lose them gradually without a deliberate governance decision being made.
- **Review roles are unassigned.** "Humans remain responsible" is not a HITL policy. Accountability without role assignment disappears under operational pressure.

### Best practices

- Design verification as a structural step, not a reactive one. Decide in advance: which outputs, at which volume, reviewed by whom, using what criteria.
- Define the HITL spectrum for each use case: full review, selective review (triggered by confidence threshold or output type), human-on-the-loop (monitoring at system level), or human-initiated. Document which one you are using and why.
- Specify reviewers by role, not by name. If the review policy says "Sarah checks AI outputs," it will not survive organizational change.
- Grounding strategies (RAG, retrieval, tool use) reduce hallucination risk but do not eliminate it. Do not treat grounding as a substitute for verification on consequential outputs.

### Observability signals

| Signal | What it tells you |
|---|---|
| Ground truth comparison rate | How often AI outputs are checked against verified sources |
| Human review coverage | % of outputs that passed through a HITL step |
| Review reversal rate | % of reviewed outputs changed or rejected by human reviewers |
| Time-in-review | How long reviewers are spending — proxy for whether review is genuine or rubber-stamp |
| Hallucination incident log | Tracked instances of factual errors that reached downstream use |

---

## 2. Context & Knowledge Governance

*Concepts: [Context Engineering](../concepts/context-engineering.md) · [Persistent Synthesis](../concepts/persistent-synthesis.md)*

### Watch items

- **Context is treated as disposable.** Organizations that don't version or govern context inputs lose the ability to reproduce, audit, or explain AI outputs. If you can't reconstruct what context the model received, you can't investigate what went wrong.
- **Sensitive data enters context without access controls.** Context construction decisions are data access decisions. Who or what can inject information into a model's context window is a security and compliance question.
- **Knowledge bases accumulate without synthesis.** A knowledge base that grows by addition drifts from current reality — older entries carry the same apparent authority as newer ones. The system doesn't know what it doesn't know.
- **RAG retrieval quality is assumed, not monitored.** Retrieval-augmented systems inherit the quality of the underlying knowledge base. Stale, inconsistent, or low-quality source material produces stale, inconsistent outputs regardless of model capability.
- **Context decay is invisible.** Injected context goes stale. A system prompt written six months ago may reference outdated policies, deprecated products, or superseded procedures — and will present them with the same authority as current information.

### Best practices

- Treat context as a governed asset: version-controlled, access-managed, and with a defined owner. Apply the same governance discipline as you would to a policy document or a data product.
- Log what context was injected per session or request. This is the minimum required for auditability of AI outputs.
- Apply the persistent synthesis principle to any knowledge base feeding AI systems: resolve contradictions rather than accumulating them; assign confidence decay to entries; deprecate explicitly rather than leaving outdated content in place.
- Audit knowledge base freshness on a defined schedule. Different knowledge types decay at different rates — operational procedures faster than conceptual definitions.

### Observability signals

| Signal | What it tells you |
|---|---|
| Context version log | Which context was active for a given session or output |
| Knowledge base entry age distribution | How many entries haven't been reviewed or updated recently |
| Stale entry rate | % of entries past their expected review date |
| Retrieval coverage | Whether retrieved context is actually relevant to the query |
| Context access log | Who or what injected content into the model's context window |

---

## 3. System Control & Accountability

*Concepts: [Harness Paradigm](../concepts/harness-paradigm.md) · [Prompt Engineering](../concepts/prompt-engineering.md)*

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

---

## Related concepts

- [Hallucination](../concepts/hallucination.md)
- [Human-in-the-Loop (HITL)](../concepts/human-in-the-loop.md)
- [Context Engineering](../concepts/context-engineering.md)
- [Persistent Synthesis](../concepts/persistent-synthesis.md)
- [Harness Paradigm](../concepts/harness-paradigm.md)
- [Prompt Engineering](../concepts/prompt-engineering.md)

---

## Sources

| ID | Source | Contribution to this note |
|---|---|---|
| SRC-010 | Zhang et al. — *A Survey on Hallucination in Large Language Models* (arXiv:2311.05232, 2023) · [link](https://arxiv.org/abs/2311.05232) | Basis for verification as structural, not reactive; hallucination as a systematic property requiring systematic controls. |
| SRC-015 | Stanford HAI — *Humans in the Loop: The Design of Interactive AI Systems* (2019) · [link](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems) | HITL spectrum (full / selective / on-the-loop); framing review design as an HCI governance problem. |
| SRC-016 | Google Cloud — *What is Human-in-the-Loop (HITL) in AI & ML?* (2024) · [link](https://cloud.google.com/discover/human-in-the-loop) | Three HITL patterns and their governance implications; review gate design. |
| SRC-017 | Verma, Rahul (LangChain) — *Human judgment in the agent improvement loop* (2026) · [link](https://blog.langchain.com/human-judgment-in-the-agent-improvement-loop/) | Scale tension in human review; expert judgment encoded into evaluation pipelines. |
| SRC-018 | Fowler, Martin — *Harness engineering for coding agent users* (martinfowler.com, 2025) · [link](https://martinfowler.com/articles/harness-engineering.html) | Governance as an architecture decision; capability vs permission; harness as the accountability layer. |
| SRC-019 | Multiple authors — *Architectural Design Decisions in AI Agent Harnesses* (arXiv:2604.18071, 2026) · [link](https://arxiv.org/html/2604.18071v1) | Harness components and their governance implications; observability and audit as harness-layer concerns. |
| SRC-007 | Karpathy, Andrej — *LLM Wiki* (gist, 2023) · [link](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Persistent synthesis as a knowledge governance discipline; context as the primary leverage point. |
| SRC-008 | Ghumare, Rohit — *LLM Wiki v2* (gist, 2024) · [link](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) | Knowledge decay rates; confidence scoring; stale entry detection as a governance practice. |
| — | ⚠️ Source needed | Adversarial input patterns and prompt injection as a harness-layer governance concern. |

---

*Last updated: v1.0 · May 2026*
