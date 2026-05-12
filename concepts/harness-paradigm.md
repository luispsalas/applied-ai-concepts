# Harness Paradigm

## One-line essence
Intelligence and control are separate layers — governance lives in the harness, not the model.

---

## Technical definition

The harness paradigm describes the architectural separation between a language model (the intelligence layer) and the surrounding infrastructure that makes it operational and governable (the control layer). The harness encompasses everything that mediates between the model and the world: tool access, permission systems, memory management, context injection, output routing, logging, and human-in-the-loop checkpoints.

In this paradigm, the model is not the system — it is a component of the system. Its capabilities are defined by what the harness permits it to access and do. A model with no harness is a raw capability; a model with a well-designed harness is a governed system.

Key harness components:

- **System prompt** — baseline context and behavioral constraints defined before any user interaction
- **Tool contracts** — explicit definitions of what external actions the model can invoke, with what parameters, and under what conditions
- **Permission model** — role- and context-based rules governing what the system can access or modify
- **Memory layer** — management of what the model retains, for how long, and across which sessions
- **Routing layer** — logic that determines which model, which prompt variant, or which workflow handles a given input
- **Logging and audit** — structured records of model inputs, outputs, and tool calls for review and accountability

---

## Plain-language version

Think of the model as an engine and the harness as everything else in the vehicle: the steering, the brakes, the instruments, the rules about who can drive and where.

A powerful engine with no controls is not a safe vehicle. The engine's power doesn't determine whether the vehicle is safe — the design of the controls does.

The same logic applies to AI systems. A capable model deployed without a well-designed harness is not a governed system. The harness is where you answer the questions that actually matter for responsible deployment: What can this system do? Who authorized it? What can it not touch? What happens when it fails? Who reviews the outputs?

---

## AI literacy notes

The harness paradigm resolves a common confusion in AI governance: treating the model as the governance object. Model selection (which AI to use) and model governance (how it is controlled and accountable) are separate concerns. Organizations that focus governance attention on model choice while leaving the harness undefined have addressed the less consequential of the two.

Four implications:

1. **Governance is an architecture decision.** Policies that are not implemented in the harness are not enforced — they are aspirations. If a rule about data access isn't encoded in the permission layer, it doesn't exist operationally.
2. **Capability ≠ permission.** A model that *can* do something is not the same as a model that *should* be allowed to do it in a given context. The harness is where that distinction is made real.
3. **Harness design requires domain knowledge.** Effective harness configuration requires understanding the use case, the risk profile, and the data landscape — not just the model's technical specifications. This is a human governance task.
4. **The harness is where accountability lives.** Logging, audit trails, and HITL checkpoints are harness-layer decisions. A system without a harness cannot be audited.

---

## Governance notes

**Core question:** Who owns the harness configuration — and is it governed like a production artifact?

**Watch for:**
- Governance attention focused on model selection while harness configuration remains informal or undefined. The model doesn't enforce policies — the harness does.
- Capability treated as permission by default: if the model can access a tool or data source, it does, because no one specified otherwise.
- System prompts and permission models that are not versioned, not owned, and not subject to change review.

**Practice:**
- Treat harness configuration (permission model, tool contracts, system prompt, logging setup) as a governed artifact: versioned, owned, and change-reviewed the same way as any production configuration.
- Separate capability assessment ("can it do X?") from permission design ("should it be allowed to, for whom, under what conditions?"). These are different questions answered by different people.

**Key accountability owner:** Harness owner — the role or team responsible for configuring, versioning, and reviewing the control layer that sits between the model and the world.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Emerging — practitioner consensus.** The paradigm is well-established in production AI engineering (2023–present). The term "harness" is gaining adoption as a conceptual frame. Its application to governance and organizational design is newer and still developing.

---

## Related concepts

- [Context Engineering](context-engineering.md) — context engineering shapes the inputs the harness delivers to the model
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — HITL checkpoints are a harness-layer design decision
- [Hallucination](hallucination.md) — grounding and verification controls are implemented at the harness layer
- Permission Model — the access control component of the harness
- System Prompt — the baseline context layer; the most visible harness component for end users
- AI Agent — autonomous agents require especially deliberate harness design, as they act across multiple steps with real-world consequences

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-018 | Böckeler, Birgitta — *Harness engineering for coding agent users* (martinfowler.com, 2026) · [link](https://martinfowler.com/articles/harness-engineering.html) | Authoritative definition of the harness as the infrastructure surrounding the model. Introduces guides (feedforward controls that steer before the agent acts) vs sensors (feedback controls that observe after). Direct grounding for the core claim that intelligence and control are separate architectural layers. |
| SRC-019 | Multiple authors — *Architectural Design Decisions in AI Agent Harnesses* (arXiv:2604.18071, 2026) · [link](https://arxiv.org/html/2604.18071v1) | Systematic academic treatment of harness components: state/persistence, security/governance, orchestration/tool use, memory, observability, and evals. Provides peer-reviewed grounding for the harness component list in the technical definition. |
| — | ⚠️ Source needed | Tool contracts, MCP as standardization layer for tool interfaces — drawn from practitioner analysis of production agent systems; no single primary source identified. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core architectural frame for any AI system deployment. Defines the design space for governance implementation — logging, permissions, tool contracts, routing. |
| **Organizational** | Reframes the governance question: not "which model is safe?" but "how is this system controlled?" Shifts accountability from the vendor to the deployer. |
| **Client-facing** | Explains why two organizations using the same AI model can produce very different outcomes — and why implementation decisions matter as much as model choice. |
| **LLM-native** | The paradigm that clarifies the relationship between model capability and system governance. Every other governance concept in this wiki is implemented at the harness layer. |

---

*Last updated: v1.1 · May 2026*
