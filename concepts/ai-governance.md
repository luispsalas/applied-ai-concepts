# AI Governance

## One-line essence
The frameworks, policies, and accountability structures that determine who decides how AI systems behave — and who is answerable when they don't.

---

## Technical definition

AI governance refers to the ensemble of rules, processes, roles, and controls applied to the design, deployment, monitoring, and retirement of AI systems. It operates at three distinct levels:

1. **Regulatory governance** — external frameworks imposed by law or regulation. The EU AI Act establishes a risk-tiered compliance model; the NIST AI Risk Management Framework (AI RMF 1.0) provides a voluntary but widely adopted structured approach to managing AI risk across four core functions: Govern, Map, Measure, Manage.
2. **Organisational governance** — internal policies, roles, and decision rights: model registries, AI review boards, acceptable use policies, procurement standards, accountability assignments.
3. **Technical governance** — controls embedded in AI systems and their harnesses: access controls, logging, guardrails, version management, and auditability mechanisms.

The governance landscape is fragmented. A 2023 synthesis found more than 84 AI ethics and governance guidelines in circulation globally; by some estimates that figure has since exceeded 200. Convergence is occurring around a small set of principles — fairness, transparency, accountability, human oversight — but implementation standards remain inconsistent across jurisdictions and sectors.

Two structural challenges are reshaping what governance must address:
- **The agentic shift**: AI systems that act, not just respond — planning across steps, invoking tools, and operating with reduced human oversight per action cycle. Governance designed for advisory AI does not transfer cleanly to agentic AI.
- **Local and on-device AI**: Models running outside organizational perimeters remove the data-residency and access-control guarantees that centralized deployment provides. Governance must extend to the edge.

---

## Plain-language version

AI governance is the answer to the question: who is in charge of what AI does, and what happens when something goes wrong?

Without it, AI systems accumulate in organizations without anyone being clearly responsible for their behavior, their accuracy, or their consequences. Individual teams adopt tools; no one owns the risk.

With it, there are defined rules for which AI systems are approved, who can use them, what they can do with organizational data, how outputs are verified, and who is accountable for failures. Governance is what makes AI adoption manageable — not just technically, but organizationally and legally.

---

## AI literacy notes

Governance is not a compliance layer bolted on after deployment. It is a design decision made at the start — and the teams who treat it that way end up with AI systems that are easier to operate, easier to audit, and easier to fix.

Three things practitioners need to understand:

1. **Governance without accountability is policy theater.** A framework that names no owner for each obligation is a document, not a control. Every governance decision needs a named role attached to it.
2. **The NIST AI RMF is the most actionable starting point for most organizations.** It is voluntary, sector-agnostic, and structured around practical functions rather than abstract principles. The EU AI Act applies if your organization deploys AI into the EU market — ignore it at legal risk.
3. **Agentic AI requires a different governance posture.** When AI systems take actions rather than producing outputs for human review, the intervention point moves. Governance must shift from output review to action authorization — defining what the system is permitted to do before it does it, not after.

---

## Governance notes

**Core question:** Does your organization have a named owner for each AI system in production — someone accountable for its behavior, its outputs, and its consequences?

**Watch for:**
- AI systems deployed without a defined accountability owner: no one responsible for monitoring, updating, or retiring the system. Common in shadow AI adoption where business units deploy tools outside central oversight.
- Governance frameworks that address data and models but not agents: agentic systems that plan and act require authorization controls on actions, not just outputs. Existing frameworks frequently have no answer for this.
- Regulatory exposure that goes unrecognized: the EU AI Act applies to systems deployed into the EU market regardless of where the deploying organization is headquartered. Organizations operating internationally cannot treat it as out of scope.

**Practice:**
- Maintain an AI system inventory: every system in use, its risk classification, its owner, its review cadence, and its retirement criteria. An ungoverned AI system is a liability that compounds.
- Adopt the NIST AI RMF as an internal reference even if not legally required — its Govern / Map / Measure / Manage structure maps cleanly to organizational accountability design.

**Key accountability owner:** AI governance owner — the role (individual or function) responsible for maintaining the organization's AI governance framework, system inventory, and compliance posture.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established, active.** Core governance principles (accountability, transparency, human oversight) are stable and widely endorsed. Regulatory frameworks (NIST AI RMF, EU AI Act) are published and in force. Implementation standards and agentic governance norms are active development areas — this entry will require revision as the regulatory landscape consolidates.

---

## Related concepts

- [Observability](observability.md) — the technical precondition for governance: you cannot govern what you cannot see
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the design pattern that preserves human decision authority; a core governance requirement for high-stakes systems
- [Harness Paradigm](harness-paradigm.md) — governance controls are implemented at the harness layer; the harness is where policy becomes enforceable
- [AI Agent](ai-agent.md) — agentic systems introduce governance requirements (action authorization, multi-step accountability) that advisory AI does not
- [Black Box](black-box.md) — opacity is a governance risk; systems that cannot be interpreted cannot be audited
- [AI Literacy](ai-literacy.md) — governance frameworks require the people responsible for them to understand what they are governing

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-001 | NIST — *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (2023) · [link](https://airc.nist.gov/RMF) | Primary framework reference: four-function structure (Govern, Map, Measure, Manage), risk management posture, organizational accountability design. Authoritative US government publication. |
| SRC-024 | Jobin, A. et al. — *The Global Landscape of AI Ethics Guidelines* (Nature Machine Intelligence, 2019) · [link](https://www.nature.com/articles/s42256-019-0088-2) | Synthesis of 84+ AI ethics/governance guidelines globally; convergence around fairness, transparency, accountability, human oversight; fragmentation in implementation standards. Peer-reviewed. |
| SRC-036 | European Parliament — *EU Artificial Intelligence Act* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Risk-tiered compliance model; extraterritorial scope for EU market deployment; prohibited AI practices; high-risk system requirements. Primary legal source. |
| SRC-037 | Anthropic — *Model Specification* (2024) · [link](https://anthropic.com/model-spec) | Agentic governance framing: principal hierarchy, action authorization, reduced-oversight deployment patterns, corrigibility as a governance property. Vendor-produced — used as background reference for agentic governance framing; not cited as an independent authority. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs what controls must be built into AI systems and their harnesses to satisfy governance requirements: logging, access controls, guardrails, version management. |
| **Organizational** | The primary audience. AI governance is fundamentally an organizational accountability problem — not a technical one. Leaders who treat it as IT's problem will discover it is theirs when something fails. |
| **Client-facing** | Answers the question: "what governance do you have around your AI systems?" A prerequisite for any client that is itself subject to AI regulation. |
| **LLM-native** | Foundation context for understanding why harness design, observability, and HITL exist — they are the technical implementation of governance requirements. |

---

*Last updated: v1.0 · May 2026*
