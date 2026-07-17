# AI Use Case

## One-line essence
A defined, bounded application of AI to a specific problem — the unit of design, risk assessment, and governance accountability.

---

## Technical definition

A use case — formally, "a complete task of a system that provides a measurable result of value for an actor" (ISO/IEC/IEEE 24765, 3.3241) — in which the system is an AI system: "an engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives" (ISO/IEC 22989:2022, 3.1.4).

ISO/IEC TR 24030:2024 standardizes how an AI use case is documented: application domain, deployment model, objective(s), narrative, stakeholders and their perspectives, data characteristics, KPIs, threats and vulnerabilities, and trustworthiness considerations. This documented unit is where governance attaches: NIST AI RMF frames risk as dependent on context of use, the EU AI Act binds obligations to a system's intended purpose, and the OECD Classification Framework characterizes systems in their deployment context.

Note: no single standard defines the compound term "AI use case"; this definition composes the ISO use-case and AI-system definitions with the TR 24030 documentation structure.

---

## Plain-language version

An AI use case is the specific job you're asking AI to do — "summarize customer complaints," not "use AI." Naming the job precisely is what makes the right questions possible: what data does it need, what could go wrong, who is affected, and who is responsible.

---

## AI literacy notes

1. **Risk lives in the use, not the model.** The same model can be low-risk in one use case and high-risk in another. Regulators classify by use, not by technology — which makes the use case the unit where governance actually attaches.
2. **Vague use cases cannot be governed.** "Improve productivity with AI" cannot be evaluated, risk-assessed, or audited. A well-formed use case names: the task, the users, the affected people, the data involved, success criteria, and failure consequences.
3. **The use case is the unit of evaluation.** Success criteria and KPIs only make sense against a defined task with a defined scope — which is why the standardized documentation template (ISO/IEC TR 24030) exists.

---

## Governance notes

**Core question:** Who owns the definition and boundaries of each AI use case?

**Watch for:**
- Scope creep — a system reused beyond its assessed purpose
- Vague use-case statements that block evaluation
- Risk assessed at model level instead of use level

**Practice:**
- Maintain a use-case register with intended purpose, affected users, and risk tier
- Re-assess whenever scope changes

**Key accountability owner:** the product/business owner, with AI governance sign-off.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The definition is fully composed from international standards (ISO/IEC/IEEE 24765 "use case" + ISO/IEC 22989 "AI system" + ISO/IEC TR 24030 documentation structure), each verified — held below High only because no single standard defines the compound term itself.

---

## Related concepts

- [AI Governance](ai-governance.md) — the use case is the unit governance obligations attach to
- [Evaluation (AI Systems)](evaluation.md) — success criteria are defined per use case, not per model
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — failure consequences are use-case-specific
- [Domain](domain.md) — every use case lives in a domain that sets its quality criteria and error severity
- [AI Literacy](ai-literacy.md) — precise use-case framing is a core organizational competency

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-139 | ISO/IEC/IEEE — *24765:2010 Systems and Software Engineering — Vocabulary* (2010) · [link](https://cse.msu.edu/~cse435/Handouts/Standards/IEEE24765.pdf) | Formal definition of "use case" (entry 3.3241), verified verbatim. |
| SRC-133 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 22989:2022 — AI Concepts and Terminology* (2022) · [link](https://www.iso.org/standard/74296.html) | Canonical "AI system" definition (3.1.4), verified verbatim. |
| SRC-140 | ISO/IEC JTC 1/SC 42 — *ISO/IEC TR 24030:2024 — AI Use Cases* (2024) · [link](https://www.iso.org/standard/84144.html) | Standardized AI use-case documentation template: application domain, deployment model, objectives, narrative, stakeholders, data characteristics, KPIs, threats, trustworthiness. |
| SRC-001 | NIST — *AI Risk Management Framework* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Risk as a function of context of use; use-case-level risk framing. |
| SRC-129 | European Parliament — *EU Artificial Intelligence Act* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Obligations attach to a system's intended purpose; use case as the unit of risk classification. |
| SRC-134 | OECD — *Framework for the Classification of AI Systems* (2022) · [link](https://www.oecd.org/en/publications/oecd-framework-for-the-classification-of-ai-systems_cb6d9eca-en.html) | Five-dimension characterization of AI systems in their deployment context. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The unit of scoping and evaluation: task, data, success criteria, and failure consequences are defined per use case, not per model. |
| **Organizational** | The unit of risk assessment and accountability — a use-case register is the practical foundation of AI governance. |
| **Client-facing** | Answers "what exactly is the AI doing here?" — the precondition for informed consent and trust. |
| **LLM-native** | Guards against "the model can do anything" thinking: capability breadth makes precise use-case boundaries more important, not less. |

---

*Last updated: v1.0 · July 2026*
