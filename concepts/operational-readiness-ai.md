<!--meta
category: Organizational Readiness
short: Whether the organization can actually run an AI system — data, infrastructure, skills, process, governance — not whether the model works
aliases: [are we ready, deployment readiness, AI maturity, production readiness, can we actually run this]
tags: [Architecture, Data Governance]
established: established
-->
# Operational Readiness (AI)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The organizational capacity — data, infrastructure, skills, processes, and governance — required before an AI system can be safely deployed at scale.

---

## Technical definition

The assessment of whether an organization can actually *run* an AI system, as distinct from whether the system works. A model that performs well in evaluation is a necessary and badly insufficient condition for deployment: the surrounding capability determines whether it stays correct, whether failures are caught, and whether anyone can answer for it.

The foundational framing comes from the observation that only a small fraction of a real machine-learning system is the model itself. The mass of it is configuration, data collection, feature extraction, serving infrastructure, process management, and monitoring — and that surrounding system accrues distinctive maintenance debt: entangled components where changing anything changes everything, undeclared consumers depending on outputs nobody tracks, data dependencies that shift without notice, and configuration sprawl. Readiness is largely the question of whether an organization has capacity for that mass, not for the model.

In practice a readiness assessment spans five dimensions:

- **Data** — is the input data available, of known [quality](data-quality.md), lawfully usable for this purpose, and will it keep flowing?
- **Infrastructure** — can it be served, scaled, versioned, and rolled back? Is there a path to revert a bad change?
- **Skills** — is there someone who can diagnose it when it misbehaves, as opposed to someone who can only restart it?
- **Process** — is there a defined path for incidents, escalation, change, and decommissioning?
- **Governance** — is there a named [owner](ownership-ai-systems.md), a [permission model](permission-model-ai.md), an [audit trail](audit-trail-ai.md), and a monitoring commitment with someone resourced to act on it?

The distinguishing test is not "does it work today?" but **"what happens on a bad day?"** — when the model degrades, an input source changes, a vendor updates the model underneath, or an output causes harm. Readiness is the capacity to detect, respond, and answer.

Two asymmetries make this harder for AI than for conventional software. Deployment is unusually cheap relative to the ongoing obligation, so the commitment is systematically underestimated at the decision point. And a great deal of the capability sits with a vendor, which means part of your readiness is really a question about *their* practices and your contractual visibility into them.

---

## Plain-language version

Getting an AI system to work in a demo is the easy part. Running it is the commitment: keeping the data flowing, noticing when it starts going wrong, having someone who can diagnose it, and knowing who answers when it causes a problem. Readiness is asking those questions *before* you deploy, when the answer can still change the decision.

---

## AI literacy notes

1. **Working is not readiness.** A successful pilot demonstrates capability, not capacity to operate. The two are routinely conflated at exactly the moment a deployment decision gets made.
2. **The model is the small part.** Most of a production AI system — and most of its maintenance burden — is everything around the model. Budget and staffing that assume otherwise will be wrong by a wide margin.
3. **The right question is "what happens on a bad day?"** Not can it work, but: how would you notice it stopped, who responds, how fast, and who explains it afterwards.
4. **Deployment is cheap; the obligation is not.** The asymmetry between how easy it is to ship and how long you must run it is the single most common source of underestimation.
5. **Vendor dependencies are part of your readiness, and mostly outside your control.** If the model, data, or infrastructure is someone else's, your operational capacity includes their practices and whatever visibility your contract gives you.
6. **Readiness expires.** An assessment reflects one moment. Capability changes, staff leave, and dependencies shift — a readiness sign-off from a year ago describes an organization that may no longer exist.

---

## Governance notes

**Core question:** If this system failed quietly tomorrow, would anyone notice, would anyone be able to fix it, and could someone explain what happened?

**Watch for:**
- Pilot success treated as a deployment decision, with no separate readiness assessment
- No named owner, or an owner without the budget or authority to act on what monitoring shows
- Monitoring committed to in a plan but not staffed, so alerts arrive with nobody assigned
- Single-person dependency — one individual who understands the system and no documented handover
- No decommissioning path, so the system persists past its usefulness because nobody owns turning it off
- Vendor dependencies with no contractual visibility into model changes or incident notification

**Practice:**
- Run a readiness assessment against the five dimensions as a **gate before deployment**, not as a retrospective document
- Require named owners for the system, its data, and each dependency it touches
- Confirm monitoring is *staffed*, not merely configured — an unread alert is not a control
- Define the decommissioning path at deployment, while it is cheap to agree
- Re-assess on a schedule and on any material change, treating readiness as perishable
- For vendor components, record what you can and cannot see, and what you would do if the vendor changed the model

**Key accountability owner:** the system owner, with the accountable executive who authorizes deployment.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The underlying claim — that the surrounding system dominates the model, and that its maintenance burden is systematically underestimated — is peer-reviewed and has held up for a decade. The five-dimension framing is a practitioner synthesis rather than a standardized model: it is consistent with NIST AI RMF's GOVERN and MAP functions and with ISO/IEC 42001's management-system structure, but no authoritative readiness rubric exists, and organizations should expect to adapt it rather than adopt it.

---

## Related concepts

- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — the certifiable framework that formalizes much of this capacity
- [Ownership (AI Systems)](ownership-ai-systems.md) — a named owner is a readiness precondition, not a formality
- [Observability (AI Systems)](observability.md) — the detection capability readiness is largely assessing
- [Model/Data Drift](model-data-drift.md) — the reason monitoring must exist before deployment rather than after the first surprise
- [Data Quality](data-quality.md) — the upstream constraint on everything downstream
- [Evaluation (AI Systems)](evaluation.md) — measures whether it works; readiness measures whether you can run it
- [AI Incident (Reporting)](ai-incident-reporting.md) — the response path readiness has to establish in advance
- [AI Governance](ai-governance.md) — readiness is the operational face of the governance commitment
- [AI Literacy](ai-literacy.md) — the skills dimension, at organizational scale
- [Audit Trail (AI)](audit-trail-ai.md) — without it, the "explain what happened" requirement cannot be met
- [Value Realization (AI)](value-realization-ai.md) — the other half of the deployment question: capable of running it, and getting something from it

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-166 | Sculley, D. et al. (Google) — *Hidden Technical Debt in Machine Learning Systems* (NIPS, 2015) · [link](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | The foundational claim: the model is a small fraction of a real system, and the surrounding infrastructure carries distinctive, underestimated maintenance debt. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The GOVERN and MAP functions: organizational capacity, roles, and context established before deployment rather than after. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The management-system view of the same capacity — resources, competence, operational planning — as auditable requirements. ⚠️ Paywalled; cited for scope and structure only. |
| SRC-105 | Kausar, Rehan (CDO Magazine) — *AI Governance Roles: Who Owns What as AI Scales in the Enterprise* (2026) · [link](https://www.cdomagazine.tech/ai-governance/ai-governance-roles-who-owns-what-as-ai-scales-in-the-enterprise) | The organizational reality: five cross-functional areas converge on each system, and accountability must land on one named individual. |
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* · [link](https://www.dama.org/cpages/body-of-knowledge) | The data-readiness dimension, drawing on established data management practice rather than treating it as an AI-specific invention. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Most of the work and most of the debt is outside the model — plan capacity for the surrounding system, and build the rollback path before you need it. |
| **Organizational** | Readiness is a deployment gate distinct from evaluation, and it is where the ongoing cost of an AI decision actually becomes visible. |
| **Client-facing** | Answers "are we ready to run this?" — including who responds when it misbehaves and how it gets turned off. |
| **LLM-native** | When the model is a vendor's, a large share of your operational readiness is really a question about their practices and your contractual visibility. |

---

*Last updated: v1.0 · August 2026*
