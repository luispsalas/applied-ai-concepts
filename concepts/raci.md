<!--meta
category: Human Oversight
short: Who does the work, who answers for it, who is consulted, who is informed — the system can be Responsible, only a person can be Accountable
aliases: [responsibility matrix, RACI matrix, responsible accountable consulted informed, role assignment, who owns what]
-->
# RACI

## One-line essence
A simple table that answers four questions for any AI task: who does the work, who is on the hook if something goes wrong, who you consult for expertise, and who just needs to be kept informed.

---

## Technical definition

A responsibility assignment matrix. Tasks form the rows, people or roles form the columns, and each cell carries one of four designations:

- **R — Responsible.** Does the work.
- **A — Accountable.** Answers for the outcome. **Exactly one per task**, always a person, never a group.
- **C — Consulted.** Provides input before the decision; two-way.
- **I — Informed.** Told the outcome; one-way.

RACI is a practitioner convention rather than a standardized instrument — it has no authoritative defining document, and variants proliferate (RASCI, RACIO, DACI). Its value is not theoretical rigor but that it forces two questions organizations otherwise leave implicit: *is there exactly one accountable person*, and *is Responsible distinct from Accountable*.

Applied to AI systems, one distinction does real work and the rest is ordinary project management. **The Responsible party can be a system; the Accountable party never can.** An AI system can perform the task — draft the summary, triage the ticket, flag the transaction — and so occupy the R. It cannot explain itself to a forum, justify a decision, or bear consequences, so it cannot occupy the A. Accountability in the sense that matters is a relationship between an actor and a forum that can question, judge, and impose consequences; a model is not a participant in that relationship.

This is where RACI earns a place in AI governance rather than being generic management furniture. Automating a task moves the R and silently leaves the A unfilled unless someone deliberately assigns it. The result is the [responsibility gap](human-responsibility-in-ai-use.md) in its most mundane and most common form — not a philosophical puzzle, but a matrix cell nobody filled in.

A second AI-specific wrinkle: the accountable party **shifts across the lifecycle**. Whoever is accountable for selecting and approving a system is often not who is accountable for operating it, and neither is who is accountable for decommissioning it. A single static matrix drawn at project kickoff misrepresents this, and the handover points are where accountability is most often dropped.

---

## Plain-language version

Four letters against every task: who does it, who answers for it, who gets asked first, who gets told after. The one rule that matters is that exactly one named person is accountable — and when an AI system takes over the doing, that accountable person does not disappear. If nobody can name them, that is the finding.

---

## AI literacy notes

1. **The system can be Responsible; a person must be Accountable.** This single line prevents the most common governance failure in automated workflows — the task moves to the system and the answerability quietly evaporates.
2. **One A, and it is a name.** "The AI team" or "Governance" is not accountable; a person is. A committee in the A cell means nobody is accountable, which is usually the actual state being disguised.
3. **Automation changes the matrix and almost nobody redraws it.** When a step is automated, the R moves. If the matrix is not revisited, it now describes a workflow that no longer exists.
4. **Accountability moves across the lifecycle.** Selection, operation, and decommissioning frequently have different accountable owners. Draw the matrix per phase, and pay attention to the handovers — that is where it gets dropped.
5. **RACI records assignment; it does not create capability.** Naming someone accountable who has no visibility into the system, no authority to stop it, and no budget to fix it produces a name to blame rather than a functioning control.
6. **It is a convention, not a standard, and the AI-era version is actively contested.** There is no canonical RACI specification, and variants differ. More to the point here: **whether an AI system belongs in the matrix at all is unsettled.** Practitioner frameworks published within months of each other take opposite positions — some place agents in R/C/I with human review gates, others hold that AI systems are objects of governance and never participants, on the grounds that admitting them signals clarity while introducing ambiguity. No standard resolves it, and the established variants (RASCI, RACI-VS, DACI) all predate the question. Agree what each letter means locally before using it, or the matrix will encode a disagreement.

---

## Governance notes

**Core question:** For every AI-supported task, can you name the one person accountable — and do they have the visibility, authority, and budget to act on it?

**Watch for:**
- An A cell containing a team, a committee, or a function rather than a person
- Multiple A's on one task, which reliably means none in practice
- Tasks with an R (increasingly the system) and an empty A — the automation-created accountability gap
- A matrix drawn at kickoff and never revisited as the system's autonomy grew
- Accountable owners without access to monitoring, or without authority to suspend the system
- No handover of accountability defined between build, operate, and decommission

**Practice:**
- Draw the matrix per **use case and per lifecycle phase**, not once per project
- Where a system holds the R, record that explicitly — the fact that a step is automated should be visible in the matrix, not hidden behind a team name
- Verify each accountable owner has three things: visibility into behavior, authority to stop it, and budget to remediate
- Re-run the matrix whenever autonomy, tools, or scope change — treat it as a versioned artifact
- Connect it to the [permission model](permission-model-ai.md): the A on a task should be the party authorizing what the system may do within it

**Key accountability owner:** whoever owns the governance framework — and, recursively, someone must be accountable for the matrix itself being current.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium — and lower for the AI-specific application.** The mechanics are stable, widely used, and uncontroversial, but RACI is practitioner convention with **no authoritative defining source** — this entry describes established usage rather than a specification, and variants disagree at the edges.

The one claim this entry rests on is well grounded: that accountability requires an actor who can explain, justify, and face consequences is supported by the peer-reviewed accountability literature, and it is what rules a model out of the A cell.

**Everything past that is in active development, and the entry deliberately stops there.** How an automated executor should be *represented* in a responsibility matrix has no authoritative answer: no standard admits AI systems as role-holders, practitioner frameworks openly disagree, and there is no peer-reviewed treatment of RACI-with-agents at all. A further complication sits underneath: recent formal work argues that above a threshold of system autonomy, naming an accountable human satisfies completeness at the cost of foreseeability — producing a designated blame-holder rather than a genuinely accountable person. **Treat the R/A split as durable and any notation for machine execution as unsettled.**

---

## Related concepts

- [Accountability (AI Systems)](accountability-ai-systems.md) — the relationship RACI's "A" is trying to assign; the theory behind the letter
- [Ownership (AI Systems)](ownership-ai-systems.md) — the closest concept: a named owner is an A that persists across the whole system rather than per task
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — why the A cannot transfer to the system, however much of the R does
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — the fine-grained division of labor; RACI is its coarse organizational counterpart
- [Permission Model (AI)](permission-model-ai.md) — what the system may do, authorized by the party holding the A
- [AI Governance](ai-governance.md) — role assignment is one of its basic mechanics
- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — assigning roles and responsibilities is a clause requirement; RACI is a common way to satisfy it
- [AI Use Case](ai-use-case.md) — the unit the matrix should be drawn against
- [AI Incident (Reporting)](ai-incident-reporting.md) — when something goes wrong, the A is who must respond and report

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-110 | Bovens, Mark — *Analysing and Assessing Accountability: A Conceptual Framework* (2007) · [link](https://doi.org/10.1111/j.1468-0386.2007.00378.x) | Accountability as a relationship between an actor and a forum that can question, judge, and impose consequences — the theoretical basis for why a model cannot hold the "A". |
| SRC-105 | Kausar, Rehan (CDO Magazine) — *AI Governance Roles: Who Owns What as AI Scales in the Enterprise* (2026) · [link](https://www.cdomagazine.tech/ai-governance/ai-governance-roles-who-owns-what-as-ai-scales-in-the-enterprise) | "One person, one name" rather than a committee; the five cross-functional areas converging on each system; and that RACI accountability shifts across lifecycle stages. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The GOVERN function's requirement that roles, responsibilities, and lines of authority be documented and understood. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | Assigned roles and responsibilities as an auditable management-system requirement. ⚠️ Paywalled; cited for scope and structure only. |
| SRC-106 | Matthias, Andreas — *The Responsibility Gap: Ascribing Responsibility for the Actions of Learning Automata* (2004) · [link](https://doi.org/10.1007/s10676-004-3422-1) | The gap that opens when a system acts and no human is positioned to answer for it — what an unfilled "A" cell produces in practice. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | When a step is automated the matrix changes; record the system in the R explicitly rather than leaving the automation invisible. |
| **Organizational** | The fastest governance diagnostic available: for each AI-supported task, name the one accountable person. Inability to answer *is* the finding. |
| **Client-facing** | Answers "who is responsible for this?" with a name and a scope rather than a department. |
| **LLM-native** | Agentic systems absorb the R across many steps at once; the A has to be assigned deliberately or it is simply left empty. |

---

*Last updated: v1.1 · August 2026*
