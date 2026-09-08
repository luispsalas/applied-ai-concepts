<!--meta
category: Human Oversight
short: When a decision about a person is made without a human in it — the one place law already grants an individual the right to object, and the threshold most systems are quietly designed to sit under
aliases: [redress, automated decision, solely automated processing, profiling, right to contest, right to explanation, human intervention, GDPR Article 22, can I appeal an AI decision]
tags: [Regulatory, Ethics, Data Governance]
established: established
-->
# Automated Decision-Making

> **Term status — Established.** A defined legal concept under GDPR Article 22 and addressed directly by EU AI Act Article 86, in independent use across regulators, courts and practice.

## One-line essence
A decision about a person produced without meaningful human involvement — the case where law grants specific rights to human intervention, explanation and contest.

---

## Technical definition

GDPR Article 22 gives a person the right *"not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."* Where such a decision is permitted — by contract, by law, or by explicit consent — the controller must implement safeguards including, at minimum, **"the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision."** Those three together are what **redress** concretely means here: not a general sense of fairness, but a specific person's ability to be heard by a human and to challenge an outcome.

**Two thresholds do all the work, and both are gameable.** The right attaches only to decisions that are **solely** automated and that have **legal or similarly significant** effects. A system with a human somewhere in it, or whose outputs are characterized as recommendations, is frequently designed — deliberately or not — to fall outside.

**"Solely" is the contested one, and rubber-stamping does not clear it.** A human who approves outputs without the authority, information or time to reach a different conclusion does not make a decision non-automated in substance ([human-in-the-loop](human-in-the-loop.md), [moral crumple zone](moral-crumple-zone.md)). **The safeguard the law names — human intervention — is precisely the thing that a nominal reviewer does not supply.**

**EU AI Act Article 86 adds a second, differently-shaped right**, and its shape matters. Any affected person subject to a decision taken by a **deployer** on the basis of output from an Annex III high-risk system, producing legal effects or similarly significantly affecting them *"in a way that they consider to have an adverse impact on their health, safety or fundamental rights"*, has the right to obtain from the deployer **"clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken."**

**Note what Article 86 does and does not require.** It is owed by the **deployer**, not the provider. It covers the system's *role* in the procedure and the decision's *main elements* — **not the model's internals**, which is why it is satisfiable without [explainability](explainability-xai.md) techniques and equally why it is not a right to understand the model. It also applies only where the right is not already provided elsewhere in Union law, so it sits alongside Article 22 rather than replacing it.

**The practical gap this entry exists to name: the obligation is to a person who must first know a system was involved.** Neither right self-executes. An individual who is not told an automated system contributed cannot request intervention, explanation or contest — which makes [disclosure](ai-disclosure-attribution.md) the precondition for every remedy described here.

---

## Plain-language version

Most of this wiki is about good practice. This is one of the few places where a person has an actual legal right, and it is worth knowing exactly what it says.

Under GDPR, if a decision about you is made **entirely** by a machine, and it has legal effects or something close to that — a loan, a job, a benefit — you have the right not to be subject to it. Where it is allowed anyway, you must be able to **get a human involved, say your piece, and challenge the result**. Those three things are what "redress" actually means. Not a feeling of fairness: a human, a hearing, a challenge.

Two words carry all the weight. **"Solely"** automated, and effects that are **legal or similarly significant**. Put a person somewhere in the process, or call the output a recommendation, and a system can be arranged to fall outside the rule. That arrangement is common, and it is not always deliberate.

But a person who clicks approve is not automatically a person who decided. **If a reviewer has no real authority, no useful information, or no time, the decision was made by the machine and a human absorbed the responsibility for it.** The thing the law asks for — genuine human involvement — is exactly what a rubber stamp fails to provide.

The EU AI Act adds a second right, with a different shape. For certain high-risk systems, if a decision affects you badly, you can ask the **organization using the system** — not the company that built it — for a clear and meaningful explanation of **what part the system played and what the decision mainly rested on**. Notice that this is not a right to be told how the model works. It is a right to be told how the decision was made.

And here is the catch that undoes all of it in practice: **you cannot ask for any of this if nobody told you a system was involved.** Every right on this page depends on someone knowing there was something to object to.

---

## AI literacy notes

1. **This is a legal right, not a best practice** — one of few in the field.
2. **Redress has three concrete parts**: human intervention, expressing a view, contesting the decision.
3. **"Solely" and "significant effect" are the thresholds**, and systems are commonly arranged to sit under them.
4. **A rubber stamp does not make a decision non-automated** in substance, whatever it does formally.
5. **AI Act Article 86 binds the deployer**, not the provider — the organization using the system owes the explanation.
6. **It covers the system's role and the decision's main elements**, not the model's internals.
7. **The two rights coexist**; Article 86 applies where the right is not otherwise provided in Union law.
8. **Neither right self-executes** — without disclosure, nobody knows to invoke them.

---

## Governance notes

**Core question:** For each decision this system touches, is there a person who could ask a human to look again — and would anything actually change if they did?

**Watch for:**
- A "human in the loop" with no authority to overturn, no dissenting information, and no time ([human-in-the-loop](human-in-the-loop.md))
- Outputs relabeled as recommendations while decision practice is unchanged
- No route for an affected person to contest, or one that returns to the same system
- Individuals never told an automated system was involved ([AI disclosure](ai-disclosure-attribution.md))
- Reviewer override rates near zero or near one hundred percent — both indicate the review is not functioning
- The Article 86 explanation obligation assumed to sit with the vendor, because the model is theirs
- Explanations produced about the model instead of about the decision
- No record of what the system output and what the human then did, making contest unanswerable ([audit trail](audit-trail-ai.md))

**Practice:**
- **Determine and record whether each decision path is solely automated**, before the question is asked by someone affected
- **Give reviewers authority, dissenting information and time** — the three things that distinguish intervention from ratification
- **Measure override rates and investigate both extremes**; this is the cheapest available evidence that human involvement is real
- Provide the contest route to a different human or process, not back into the same pipeline
- Disclose system involvement at the point of decision, since every right here depends on it ([AI disclosure](ai-disclosure-attribution.md))
- Prepare the Article 86 explanation as a **deployer** obligation: the system's role in the procedure and the main elements of the decision, not the model's mechanics
- Log the output, the human action and the reasons together, so a contest can be answered with evidence ([audit trail](audit-trail-ai.md))

**Key accountability owner:** the **deployer** — the organization using the system to decide about people. Both rights described here attach there rather than to the model's builder, and this is the most commonly misassigned obligation in the area.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on what the texts say, medium on how they apply to any particular system.** Article 22's wording, its three named safeguards and Article 86's scope are quoted here from the regulatory sources and are not in dispute. **What is genuinely unsettled is the boundary**: what counts as *solely* automated, what reaches *similarly significant* effect, and how much human involvement converts one category into the other. These are matters of guidance, supervisory practice and case law that continue to develop, and this entry deliberately states the tests rather than predicting outcomes. The claim made on this wiki's own judgment — that a nominal reviewer does not satisfy the intervention safeguard in substance — is an interpretation consistent with the provision's purpose, not a settled ruling. **Verify current guidance before relying on any threshold determination.**

---

## Related concepts

- [Human-in-the-Loop](human-in-the-loop.md) — the safeguard the law names, and how it fails in practice
- [Moral Crumple Zone](moral-crumple-zone.md) — the reviewer who absorbs responsibility without holding control
- [AI Disclosure (Attribution)](ai-disclosure-attribution.md) — the precondition without which no right here can be invoked
- [Explainability (XAI)](explainability-xai.md) — a different thing from the explanation Article 86 requires
- [Accountability (AI Systems)](accountability-ai-systems.md) — who answers when the decision is challenged
- [Compliance (AI Systems)](compliance-ai-systems.md) — where these obligations sit among the others
- [Fundamental Rights Impact Assessment (FRIA)](fundamental-rights-impact-assessment.md) — the deployer-side assessment for the same class of systems
- [Audit Trail (AI)](audit-trail-ai.md) — the record that makes a contest answerable
- [Bias (AI Systems)](bias-ai-systems.md) — what a contested decision often turns out to be about
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the wider duty this codifies in one narrow case

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-297 | European Union — *GDPR Article 22: Automated individual decision-making, including profiling* (Reg. (EU) 2016/679) · [link](https://gdpr-info.eu/art-22-gdpr/) | The right and its three named safeguards, verified against the text: the right *"not to be subject to a decision based solely on automated processing… which produces legal effects… or similarly significantly affects him or her"*, and where permitted, *"the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision."* This is what the entry means by redress. |
| SRC-298 | European Parliament / Council of the EU — *EU AI Act, Article 86: Right to explanation of individual decision-making* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The second right, verified verbatim from EUR-Lex: owed by the **deployer**, for Annex III high-risk systems, covering *"clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken."* ⚠️ Note the exclusion of Annex III point 2, and that it applies only where the right is not otherwise provided under Union law. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The regulation Article 22 sits within, and the source of the surrounding obligations — lawful basis, transparency, data-subject rights — that a contest engages alongside it. |
| SRC-024 | European Parliament — *EU AI Act, Article 13* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The transparency obligation on providers, distinguished here from Article 86's deployer-side duty — the distinction this entry flags as the most commonly misassigned. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Log the output, the human action and the reasons together. Without that record a contest cannot be answered, whatever the process says. |
| **Organizational** | Both rights attach to the **deployer**, not the model's builder. Measure reviewer override rates — both extremes mean the human step is not working. |
| **Client-facing** | Lets you state precisely what an affected person can ask for: a human, a hearing, a challenge, and an explanation of the decision. |
| **LLM-native** | Calling an output a recommendation does not settle whether the decision was solely automated; what the reviewer could actually have changed does. |

---

*Last updated: v1.0 · September 2026*
