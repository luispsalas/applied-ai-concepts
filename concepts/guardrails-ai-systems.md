<!--meta
category: System Architecture
short: Technical and policy constraints that prevent an AI system from producing outputs or taking actions outside defined boundaries
aliases: [safety filters, content filtering, constraints, boundaries, policy enforcement]
tags: [Security, Architecture, Safety]
established: established
-->
# Guardrails (AI Systems)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Technical and policy constraints that prevent an AI system from producing outputs or taking actions outside defined boundaries.

---

## Technical definition

Guardrails are control mechanisms — input/output filters, content classifiers, policy checks, action constraints, and permission boundaries — placed around an AI model to keep system behavior within defined limits, independent of the model's own training. The programmable-rails formulation established the defining properties in the research literature: guardrails are user-defined, independent of the underlying LLM, and interpretable (Rebedea et al., EMNLP 2023).

In the harness paradigm, guardrails live in the system layer around the model, not inside it. Regulation increasingly expects documented controls of this kind for high-risk systems (EU AI Act), mapped to risk-management functions such as the NIST AI RMF "Manage" function.

---

## Plain-language version

Guardrails are the fences around an AI system: rules that check what goes in and what comes out, and block or flag anything outside the lines — like a reviewer that inspects the AI's work before it reaches you, or a lock that stops it from taking actions it shouldn't.

---

## AI literacy notes

1. **Guardrails are not alignment.** They constrain the system externally rather than changing what the model has learned. A guardrailed model is still the same model — the boundaries live around it.
2. **Guardrails are layered.** Input guardrails (prompt-injection screening, PII detection), output guardrails (toxicity, hallucination and format checks), and action guardrails (tool permissions, human-approval gates) address different failure surfaces.
3. **Guardrails are themselves probabilistic.** Classifiers miss things — guardrails are defense in depth, not guarantees. And over-tight guardrails degrade usefulness: calibration is an ongoing trade-off, not a one-time setting.

---

## Governance notes

**Core question:** Who defines the boundaries, and who is notified when a guardrail fires?

**Watch for:**
- Guardrails treated as guarantees (they are probabilistic)
- Silent blocking with no logging — invisible failure
- Guardrail configuration drift as models are swapped underneath

**Practice:**
- Log every guardrail trigger to the audit trail
- Test guardrails adversarially, not just functionally

**Key accountability owner:** platform/security engineering, with governance sign-off.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** Established engineering practice with a peer-reviewed reference formulation (NeMo Guardrails, EMNLP 2023) and an active tooling ecosystem; no standardized taxonomy yet, and terminology still varies across vendors.

---

## Related concepts

- [Harness Paradigm](harness-paradigm.md) — guardrails are a harness-layer control: they live around the model, not in it
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — approval gates are action guardrails with a human as the checkpoint
- [Compliance (AI Systems)](compliance-ai-systems.md) — documented controls are what regulation increasingly expects for high-risk systems
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — each guardrail layer targets specific failure modes; guardrails failing silently is itself a failure mode
- [Audit Trail (AI)](audit-trail-ai.md) — guardrail triggers belong in the audit record, not just in blocked outputs

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-135 | Rebedea, T. et al. — *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails* (EMNLP 2023) · [link](https://arxiv.org/abs/2310.10501) | Peer-reviewed reference: programmable rails that are user-defined, LLM-independent, and interpretable. |
| SRC-032 | McKinsey & Company — *What are AI Guardrails?* (2024) · [link](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-are-ai-guardrails) | Definitional framing and guardrail types (vendor-produced; background only). |
| SRC-085 | Palomares Carrascosa, I. — *Guardrails for LLMs: Measuring AI Hallucination and Verbosity* (KDnuggets, 2026) · [link](https://www.kdnuggets.com/guardrails-for-llms-measuring-ai-hallucination-and-verbosity) | Practical output-guardrail implementation and metrics. |
| SRC-129 | European Parliament — *EU Artificial Intelligence Act* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Regulatory expectation of documented controls for high-risk systems. |
| SRC-001 | NIST — *AI Risk Management Framework* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Controls mapped to the Manage function. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Implementation surface: input/output/action rails, adversarial testing, and trigger logging are engineering deliverables. |
| **Organizational** | The practical answer to "how do we keep the AI within policy?" — but only when guardrail firing is visible and owned. |
| **Client-facing** | Explains what protections exist between the model and the user — and their probabilistic limits. |
| **LLM-native** | Core pattern for agentic deployments: tool permissions and approval gates are what make autonomy governable. |

---

*Last updated: v1.0 · July 2026*
