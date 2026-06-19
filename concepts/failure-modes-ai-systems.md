# Failure Modes (AI Systems)

## One-line essence
The specific ways an AI system can go wrong — from hallucination to scope creep to misuse — each requiring different governance responses.

---

## Technical definition

A failure mode is a specific, characterizable way an AI system produces a wrong, harmful, or unintended result. Treating "the AI failed" as a single event obscures the engineering reality: failures have distinct types, symptoms, and root causes, and each calls for a different control. Major families include:

- **Generation failures** — hallucination (confident fabrication), factual drift, unfaithful explanation.
- **Input / robustness failures** — distribution shift, adversarial inputs, prompt injection.
- **Specification failures** — the system optimizes the stated objective in unintended ways (reward hacking, scope creep, goal misgeneralization).
- **Agentic / execution failures** — in systems that act: tool-call errors, faulty structured-output parsing, runtime/exception mishandling, and error propagation where an early mistake compounds across steps (Shah et al. 2026; Agents of Chaos 2026).
- **Sociotechnical failures** — misuse, over-reliance, automation bias, and deployment outside the validated context.

Recent taxonomies of agentic systems catalog dozens of fault types across architectural dimensions (e.g., 34 fault types in four dimensions; Shah et al. 2026), reflecting that agentic failures arise not only from the model but from orchestration, state, and environment interaction. The NIST AI RMF MEASURE function frames failure identification and measurement as a lifecycle obligation, not a one-time test.

---

## Plain-language version

"The AI made a mistake" is too vague to act on. Failure modes are the specific, named ways AI systems go wrong — and naming them matters, because each one needs a different fix.

A model that confidently invents a fact (hallucination) needs grounding and verification. A model fed a weird input it never saw in training (distribution shift) needs input checks. An agent that takes a wrong early step and then builds five more on top of it (error propagation) needs checkpoints. A tool misused by people for something it wasn't built for (misuse) needs scoping and access control. Same headline — "it failed" — completely different responses.

The most dangerous failures are the quiet ones: the system keeps running and looks fine while being wrong. That's why you design for failure on purpose, instead of waiting to discover the modes in production.

---

## AI literacy notes

1. **"It failed" is not a diagnosis.** Effective governance requires naming the failure mode, because the control that prevents hallucination is not the control that prevents prompt injection or error propagation. Lumping them together guarantees the wrong fix.
2. **Agentic failures compound; single-shot failures don't.** A one-output model error is contained. An agent's early error becomes the input to its next step — so long-horizon systems need checkpoints and circuit-breakers, not just output review (Agents of Chaos 2026; Shah et al. 2026).
3. **Failure analysis is a design activity, not an incident-response one.** Anticipating failure modes before deployment — through red-teaming and a structured devil's-advocate pass — is cheaper and safer than cataloging them after they cause harm.

---

## Governance notes

**Core question:** Have this system's likely failure modes been enumerated before deployment — and does each one have a specific detection-and-response control?

**Watch for:**
- "The AI failed" treated as a single undifferentiated risk
- No pre-deployment failure analysis
- Agents allowed to run long chains with no checkpoint or circuit-breaker
- Silent failures (system wrong but confident) with no detection
- Failure controls assumed rather than tested

**Practice:**
- Enumerate failure modes per system at design time (a red-team / devil's-advocate pass)
- Map each mode to a named control
- Scale checkpoint density to execution length and action reversibility
- Monitor for the quiet failures, not just the loud ones
- Record incidents against the taxonomy to improve it

**Key accountability owner:** the system/agent owner is accountable for failure-mode enumeration and the control mapping; per-mode detection cannot be left implicit.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established (concept), active (agentic taxonomies).** That AI systems fail in distinct, categorizable ways is well-established and standardized in risk frameworks (NIST AI RMF). Specific failure taxonomies for LLM agents are an active, fast-developing area — recent peer-reviewed and preprint work is still converging on shared categories (Shah et al. 2026; Agents of Chaos 2026). Expect this entry to evolve as agentic-failure taxonomies mature.

---

## Related concepts

- [Hallucination](hallucination.md) — the most familiar generation failure mode; one family within the broader taxonomy
- [AI Agent](ai-agent.md) — agentic systems introduce execution and error-propagation failures that single model calls do not have
- [Black Box](black-box.md) — opacity makes some failures silent and hard to detect from the output alone
- [Bias (AI Systems)](bias-ai-systems.md) — systematic skew across groups is a distinct failure family with its own control
- [Evaluation (AI Systems)](evaluation.md) — evaluation is how failure modes are surfaced and measured before and during deployment
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — checkpoints and human gates are the primary control for compounding agentic failures
- [Grounding](grounding.md) — grounding and verification are the control for generation failures
- [AI Governance](ai-governance.md) — failure-mode enumeration and control mapping are governance obligations, not optional engineering polish

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-128 | Shah, M. et al. — *Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes* (arXiv:2603.06847, 2026) · [link](https://arxiv.org/abs/2603.06847) | Empirical taxonomy (34 fault types across four architectural dimensions) from 385 analyzed faults; failures arise from orchestration, state, and environment, not the model alone. |
| SRC-045 | Shapira, N. et al. — *Agents of Chaos* (arXiv:2602.20021, 2026) · [link](https://arxiv.org/abs/2602.20021) | Red-team study of error cascades across an agent's action sequence; failure propagation in multi-step systems. |
| SRC-001 | NIST — *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | MEASURE function: failure identification and measurement as a lifecycle obligation. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | A design checklist. Each failure family maps to a control — grounding, input validation, checkpointing, access scoping. Failure analysis belongs in design, not just incident response. |
| **Organizational** | Reframes "is the AI reliable?" into "which failure modes is it exposed to, and what catches each one?" — a far more answerable and auditable question. |
| **Client-facing** | Answers "what happens when it goes wrong?" with specifics and mitigations rather than reassurance. |
| **LLM-native** | Especially critical for agents, where failures compound across steps. Long-horizon autonomy demands checkpoints, circuit-breakers, and pre-deployment red-teaming. |

---

*Last updated: v1.0 · June 2026*
