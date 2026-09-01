<!--meta
category: Human Oversight
short: How much a system may do without asking — granted by an organization, not possessed by the model
aliases: [autonomy, how much can it do on its own, scope of action, levels of autonomy, autonomous action]
-->
# Agency (AI Systems)

## One-line essence
The scope of autonomous action an AI system is permitted to take — and the governance question of where human authorization is required before the system acts.

---

## Technical definition

The range of actions a system may take without asking. Agency is a **granted** property, not an emergent one: it is the boundary an organization draws around what a system does on its own authority, and it exists whether or not anyone has drawn it deliberately.

It is best read along a continuum rather than as a binary. At one end, a system that only produces text a person then acts on. At the other, a system that plans, calls [tools](tool-use.md), writes to systems of record, spends money, and spawns further processes without a checkpoint. Most real deployments sit somewhere between, usually without anyone having decided where.

**Three properties determine how much agency a deployment actually has**, and they are worth separating because they are governed differently:

- **Reach** — what the system can touch. Which systems, records, accounts, and external services are within its grasp, via credentials or tools.
- **Irreversibility** — whether its actions can be undone. Drafting an email and sending it differ enormously here while looking similar in a permissions table.
- **Checkpointing** — where a human decision is *required* rather than merely possible. An oversight path nobody is obliged to use is not a checkpoint.

**Agency and the [permission model](permission-model-ai.md) are the same subject from two directions.** Agency is the policy question — how much autonomy *should* this system have, given the stakes. The permission model is the enforcement — what the system technically *can* do. When these diverge, the permission model wins, because it is the one the system actually obeys.

**In EU law this is now prescriptive for high-risk systems.** Article 14 of the AI Act requires that such systems be designed so they "can be effectively overseen by natural persons during the period in which they are in use," and enumerates what the assigned person must be *enabled* to do — including to "decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output," and to "intervene ... or interrupt the system through a 'stop' button or a similar procedure that allows the system to come to a halt in a safe state." Notably, the same article requires that the person remain aware of the tendency toward [automation bias](automation-bias.md) — an unusual case of a human-factors finding written into a statute.

**Autonomy is not accountability.** Granting a system wide agency delegates the *action*, never the answerability for it. There is no level of autonomy at which responsibility transfers to the system — see [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) and [Accountability](accountability-ai-systems.md).

---

## Plain-language version

Agency is how much an AI system is allowed to do without asking.

A tool that drafts a reply for you to send has very little. A system that reads your inbox, decides what needs answering, and sends replies itself has a great deal. Same underlying model, entirely different exposure — and the difference has nothing to do with how capable the model is. It is a decision someone made, or failed to make.

That is the useful reframe: agency is not something a system *has*, it is something an organization *grants*. And it is granted by default whenever nobody specifies otherwise, which is how most systems end up with more of it than anyone intended. The questions worth asking are ordinary ones: what can this reach, what can it do that cannot be undone, and at which points does it have to stop and ask.

---

## AI literacy notes

1. **Agency is granted, not possessed.** "The agent decided to..." usually means someone authorized it to decide that, or authorized nothing and defaults applied. The interesting question is always who set the boundary.
2. **Capability and permission are different axes.** A very capable model with narrow permissions is a narrow system. A weak model with broad write access is a dangerous one. Conflating the two is the most common analytical error here.
3. **Reversibility matters more than reach.** A system that can read everything and change nothing is a different risk from one that can touch little but permanently. Permission lists rarely make this distinction, and they should.
4. **An oversight step nobody must use is not oversight.** If a human *can* review but is not required to, and volume makes reviewing impractical, the effective agency is full autonomy — regardless of the design diagram.
5. **Multi-step autonomy compounds quietly.** Each step may be individually reasonable while the sequence goes somewhere nobody would have approved up front. This is why checkpoints are placed by consequence, not by step count.
6. **The default is expansion, not stability.** Scope tends to widen — credentials retained past their purpose, sub-agents inheriting access, integrations added. See [Power Seeking](power-seeking.md) for why that pressure is structural rather than incidental.
7. **More autonomy is not a maturity milestone.** It is a risk position. Reducing agency after learning something is a normal outcome, not a retreat.

---

## Governance notes

**Core question:** What can this system do without asking anyone — and was that ever an explicit decision?

**Watch for:**
- Agency defined by what the system was *built* to do rather than by what its credentials *allow* — the second is the real boundary
- No named point of irreversibility: nobody able to say which actions cannot be undone
- Human oversight that is available but not required, at volumes where nobody exercises it
- Autonomy widened incrementally through integrations and convenience fixes, with no decision point that ever recorded the change
- Sub-agents and tool chains inheriting authority nobody scoped ([multi-agent systems](multi-agent-systems.md))
- A stop path that exists on paper and has never been exercised
- Autonomy discussed as a capability achievement rather than as a delegation of authority

**Practice:**
- Write down the intended agency before deployment: what it may do alone, what needs approval, what is prohibited — and enforce it in the [permission model](permission-model-ai.md) rather than in guidance
- Place checkpoints at irreversibility and at cost, not at arbitrary step counts
- Make the stop real: test it, time it, and confirm it leaves the system in a safe state — Art. 14 requires the capability, and only exercise shows it works
- Scope credentials to the task and expire them with it; review the *reachable* surface periodically, not just the intended one
- Record agency changes as decisions with an owner and a date, so widening is visible rather than cumulative
- Where oversight is required, make it affordable — see [Verification](verification.md); an unaffordable check is an unperformed one

**Key accountability owner:** whoever authorizes the scope of action — typically the system owner, and for high-risk systems under the EU AI Act, a named natural person assigned oversight. Not the builder, and never the system.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The governance framing is well grounded: the EU AI Act makes oversight obligations binding for high-risk systems, the philosophical literature on meaningful human control is established, and international standards supply autonomy vocabulary. Less settled: there is **no agreed scale for levels of AI agency** comparable to the levels-of-automation scales in aviation and driving, so "high autonomy" means different things across documents and vendors. Also unresolved in practice: how to keep agency bounded across multi-step, tool-using, sub-agent-spawning systems, where the reachable surface is decided at runtime rather than at design time.

---

## Related concepts

- [Permission Model (AI)](permission-model-ai.md) — the enforcement side of the same subject; when policy and permissions diverge, permissions win
- [AI Agent](ai-agent.md) — the system class where this stops being theoretical
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the checkpoint pattern that gives agency its boundary
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — the documented division of work that agency limits express
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — delegating action never delegates answerability
- [Accountability (AI Systems)](accountability-ai-systems.md) — who is answerable for what the system did on its own authority
- [Power Seeking](power-seeking.md) — why granted scope tends to widen rather than hold
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the technical constraints that hold the boundary
- [Multi-Agent Systems](multi-agent-systems.md) — where inherited authority makes scope hardest to track
- [Tool Use](tool-use.md) — the mechanism by which an agent reaches beyond text
- [Audit Trail (AI)](audit-trail-ai.md) — the record of what was done under delegated authority
- [Automation Bias](automation-bias.md) — named in Art. 14 itself as a risk oversight personnel must be aware of
- [Verification](verification.md) — an oversight step is only real if performing it is affordable
- [Compliance (AI Systems)](compliance-ai-systems.md) — where Art. 14 obligations are demonstrated
- Types of AI Systems — autonomy is one of the axes that taxonomy turns on

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-192 | European Parliament and Council — *EU Artificial Intelligence Act, Article 14: Human oversight* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding requirements: effective oversight by natural persons, and the enumerated capabilities — interpret output, decline to use, disregard/override/reverse, and interrupt via a stop that halts safely. Also names automation-bias awareness as an oversight requirement. |
| SRC-107 | Santoni de Sio, F.; van den Hoven, J. — *Meaningful Human Control over Autonomous Systems: A Philosophical Account* (2018) · [link](https://doi.org/10.3389/frobt.2018.00015) | Why nominal oversight is not control, and what conditions make human control meaningful rather than formal — the argument behind "an oversight step nobody must use is not oversight." |
| SRC-133 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 22989:2022 — Artificial intelligence concepts and terminology* · [link](https://www.iso.org/standard/74296.html) | Standardized vocabulary for autonomy and system classification. ⚠️ Paywalled; metadata and definitions verified via secondary sources — do not quote clause text without the standard in hand. |
| SRC-134 | OECD — *Framework for the Classification of AI Systems* (2022) · [link](https://www.oecd.org/en/publications/oecd-framework-for-the-classification-of-ai-systems_cb6d9eca-en.html) | Autonomy as one dimension of a system's risk profile rather than a standalone property, in an intergovernmental classification scheme. ⚠️ `oecd.org` returns 4xx to automated clients; reachable in a browser. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places scope-of-action decisions inside a govern/map/measure/manage lifecycle rather than treating autonomy as a deployment detail. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Scope credentials to the task and expire them with it; place checkpoints at irreversibility rather than step count; test the stop path and time it. |
| **Organizational** | Agency is delegated authority. If nobody decided how much, defaults decided it — and answerability stayed with you regardless. For high-risk systems the oversight capabilities are legally required, not optional. |
| **Client-facing** | Explains why an AI system has a bounded scope and defined approval points, in terms of what it may do rather than what it can do. |
| **LLM-native** | Capability and permission are independent axes. Reach, irreversibility and enforced checkpoints describe a deployment's real autonomy better than any label like "agentic." |

---

*Last updated: v1.0 · August 2026*
