<!--meta
category: Observability & Governance
short: What a model could do if someone tried to make it — measured separately from whether it would, because the two need different evidence and different controls
aliases: [dangerous capabilities, dangerous capability evaluation, extreme risk, uplift, capability evaluation, CBRN uplift, what could this model be used for]
tags: [Safety, Regulatory, Evaluation]
established: emerging
-->
# Dangerous Capability

> **Term status — Emerging.** In real and independent use — including a 21-author paper spanning competing labs, academia and policy institutes — but what counts as a dangerous capability is still specified differently by each organization's own framework. See the confidence level.

## One-line essence
A model ability that could enable serious harm if used — assessed for what the model *can* do, separately from whether it is inclined to do it.

---

## Technical definition

A dangerous capability is a model ability whose exercise could cause serious harm — offensive cyber operations, uplift toward chemical, biological, radiological or nuclear weapons, large-scale manipulation, or autonomous replication and resource acquisition.

**The organizing distinction, and the reason the term exists as a separate thing, is capability versus propensity.** Shevlane et al. set it out directly: developers must be able to identify dangerous capabilities — *"through 'dangerous capability evaluations'"* — **and** the propensity of models to apply their capabilities for harm — *"through 'alignment evaluations'"*. **These are two different questions needing two different tests.** A model that will not do something today because it was trained to refuse still *has* the capability; refusals are a behavioral layer over it, and behavior can be changed by fine-tuning ([fine-tuning](fine-tuning.md), [catastrophic forgetting](catastrophic-forgetting.md)) or circumvented ([jailbreak](jailbreak.md)).

**"Uplift" is the measurement concept, and it is a comparative one.** The question is not whether a model can describe something harmful, but **how much easier it makes the harm than the alternatives already available** — a search engine, a textbook, an expert. This is what makes the measurement hard and contested: the counterfactual is doing the work, and it is rarely stated.

**The threshold is where the disagreement lives.** Frontier developers publish their own frameworks naming capability thresholds that trigger heightened safeguards, and **the thresholds differ between them.** The EU AI Act codifies an adjacent concept — general-purpose models with **systemic risk**, carrying obligations to assess and mitigate — without resolving the underlying question of what capability level counts ([systemic risk](systemic-risk-ai.md), [frontier AI](frontier-ai.md)).

**Two properties make this genuinely hard rather than merely unsettled.** Capability is **elicitation-dependent**: what a model demonstrates depends on how hard someone tried, so an evaluation reports a lower bound rather than a measurement ([evaluation](evaluation.md), [red teaming](red-teaming.md)). And capabilities are frequently **latent** — present but not exhibited until a prompt, tool or scaffold reveals them, which means "we tested and it could not" ages badly as tooling around the same model improves ([harness paradigm](harness-paradigm.md)).

---

## Plain-language version

There are two different questions you can ask about a model, and mixing them up is the mistake this term exists to prevent.

**Can it?** and **Would it?**

"Can it" is about capability — could this model meaningfully help someone build a weapon, run a cyberattack, or manipulate people at scale. "Would it" is about behavior — will it refuse if asked.

These are tested differently and they fail differently. A model that refuses today still **has** whatever ability it has; the refusal sits on top, and refusals can be removed by fine-tuning or talked around. So a system that behaves impeccably in normal use can still be a capability problem.

The measurement everyone actually cares about is called **uplift**, and the key word is *compared to what*. Not "can the model describe something dangerous" — most of that is in libraries — but **how much easier does it make it than what someone could already do without it?** That comparison is the whole ball game, and it is often left unstated.

Two things make this properly difficult, not just unsettled.

**What a model shows you depends on how hard you tried.** A test that fails to elicit a capability has shown you a floor, not a ceiling. Someone more determined, or with better tools, may get further.

**And capabilities can be there without showing up.** The same model, unchanged, can turn out to be more capable next year because someone built better scaffolding around it. "We evaluated it and it couldn't" has a shelf life.

Different labs publish different thresholds for what counts as dangerous enough to act on, and they do not agree. Regulation names the neighboring idea — models with "systemic risk" — without settling where the line is.

---

## AI literacy notes

1. **Capability and propensity are separate questions** needing separate evaluations.
2. **A refusal is a behavioral layer over a capability**, not the absence of one.
3. **Uplift is comparative** — the counterfactual is the measurement, and it is often unstated.
4. **Evaluations report a lower bound**, because results depend on elicitation effort.
5. **Capabilities can be latent** and surface later through better tooling, with the model unchanged.
6. **Thresholds differ between organizations**, which is why the term is `emerging` rather than established.
7. **The EU AI Act's "systemic risk" is adjacent, not identical**, and does not settle the threshold.
8. **Fine-tuning can strip the refusal without touching the capability** ([fine-tuning](fine-tuning.md)).

---

## Governance notes

**Core question:** For the models we deploy, do we know what was assessed, how hard the assessors tried, and whether our own configuration extends what they tested?

**Watch for:**
- Safety evidence that is entirely about refusals, with no capability assessment behind it
- "It refused when we asked" treated as evidence a capability is absent ([jailbreak](jailbreak.md))
- Uplift claims with no stated counterfactual — easier *than what?*
- A provider's evaluation assumed to cover your deployment, when you have added tools, retrieval or scaffolding that extend reach ([tool use](tool-use.md), [harness paradigm](harness-paradigm.md))
- Fine-tuning on internal data with no re-check of safety behavior ([catastrophic forgetting](catastrophic-forgetting.md))
- Evaluation results treated as durable, when elicitation technique improves continuously
- A vendor's threshold framework cited as if it were an external standard ([frontier AI](frontier-ai.md))
- No route to report a capability discovered in production ([AI incident reporting](ai-incident-reporting.md))

**Practice:**
- **Read a provider's evaluation for what it tested and how hard**, not only for its conclusion — a negative result is a floor
- **Assess your own configuration separately**, since tools, retrieval and scaffolding extend what the same model can do
- Re-check safety behavior after any fine-tune, and treat the provider's card as no longer describing your model ([model card / system card](model-card-system-card.md))
- Where uplift matters, **state the counterfactual explicitly** and evaluate against it rather than against nothing
- Track which framework and which threshold a claim comes from; they are not interchangeable
- Keep capability findings reportable — a route for "we discovered it can do X" that does not depend on an incident occurring ([AI incident reporting](ai-incident-reporting.md))
- Treat evaluation results as dated evidence and schedule re-assessment against current elicitation practice ([red teaming](red-teaming.md))

**Key accountability owner:** whoever accepts a model into a deployment that adds tools or reach — because the provider assessed a model, and what you are fielding is a system, and no upstream evaluation covers the difference.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium, and the entry is filed `emerging` for a specific reason worth stating.** The capability/propensity distinction is clearly drawn in a paper with 21 authors spanning competing labs, academia and policy institutes — which is strong independent use and is what clears the establishment gate's first check on **usage** rather than on governance. **What is not established is the threshold.** Each frontier developer publishes its own framework with its own trigger levels, no independent standard adjudicates between them, and the EU AI Act's adjacent "systemic risk" concept does not resolve it. **This entry therefore documents the distinction and the measurement problems, and deliberately declines to state what level of capability is dangerous** — there is no defensible cross-organization answer. The elicitation-dependence and latency points are widely accepted in the evaluation literature and are stated here as properties rather than as quantified findings. **Revisit if an independent standards body sets thresholds**, at which point this may become `established`.

---

## Related concepts

- [Frontier AI (Frontier Model)](frontier-ai.md) — where these assessments are concentrated
- [Systemic Risk (AI)](systemic-risk-ai.md) — the adjacent regulatory concept, deliberately not identical
- [Evaluation (AI Systems)](evaluation.md) — why a negative result is a lower bound
- [Red Teaming](red-teaming.md) — elicitation effort as the variable that decides the result
- [Jailbreak](jailbreak.md) — removing the behavioral layer without touching the capability
- [Fine-tuning](fine-tuning.md) — the routine operation that degrades refusals
- [Catastrophic Forgetting](catastrophic-forgetting.md) — safety behavior as learned behavior that can be lost
- [Harness Paradigm](harness-paradigm.md) — why the same model becomes more capable over time
- [Tool Use](tool-use.md) — what extends reach beyond anything the provider evaluated
- [AI Incident (Reporting)](ai-incident-reporting.md) — the route for a capability found in production

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-303 | Shevlane, Toby; Farquhar, Sebastian; Garfinkel, Ben; Phuong, Mary; Whittlestone, Jess; Leung, Jade; Kokotajlo, Daniel; Marchal, Nahema; et al. (21 authors) — *Model evaluation for extreme risks* (2023) · [link](https://arxiv.org/abs/2305.15324) | The central distinction, in the authors' own terms: developers must identify dangerous capabilities *"through 'dangerous capability evaluations'"* and the propensity to apply them for harm *"through 'alignment evaluations'"*. **Also the establishment evidence** — 21 authors across competing labs, academia and policy institutes is independent use, which is what clears check 1 on usage. |
| SRC-200 | European Parliament / Council of the EU — *EU AI Act, Articles 51 and 55* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The adjacent regulatory concept — general-purpose models with **systemic risk** and the obligations attaching to them — cited to show that regulation names the neighboring idea **without** settling what capability level counts. |
| SRC-203 | Anderljung, M.; Barnhart, J.; Korinek, A.; Leung, J.; O'Keefe, C.; Whittlestone, J.; et al. — *Frontier AI Regulation: Managing Emerging Risks to Public Safety* (2023) · [link](https://arxiv.org/abs/2307.03718) | The policy framing in which capability thresholds trigger heightened obligations, and evidence that the threshold question is treated as open rather than settled. ⚠️ Shares authors with SRC-303 — these are **not two independent confirmations**. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The general risk-management frame such assessments sit inside, and the basis for treating capability findings as something to map, measure and manage rather than to disclose ad hoc. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | A negative evaluation is a floor, not a ceiling. Assess your own configuration — tools and scaffolding extend what the provider tested. |
| **Organizational** | Safety evidence built entirely on refusals says nothing about capability. Ask what was tested, how hard, and by whose threshold. |
| **Client-facing** | Explains why "the model refuses" is a reasonable answer about behavior and not an answer about what the system can do. |
| **LLM-native** | Capability and propensity are different tests. Fine-tuning can strip the refusal and leave the capability entirely intact. |

---

*Last updated: v1.0 · September 2026*
