<!--meta
category: Observability & Governance
short: The same capability serving a legitimate and a harmful purpose — which means risk is not a property of the model, and no amount of inspecting it will settle the question
aliases: [dual use research, dual-use research of concern, DURC, misuse potential, same capability different purpose, beneficial and harmful use]
tags: [Safety, Regulatory, Ethics]
established: established
-->
# Dual Use

> **Term status — Established.** A term of art in export control, biosecurity and research-ethics policy for decades, adopted into AI governance without modification and used identically across regulators, academic literature and industry. Independent of any vendor.

## One-line essence
The same capability serves both a legitimate and a harmful purpose — so the risk cannot be located in the technology, and cannot be removed by improving it.

---

## Technical definition

A dual-use capability is one whose beneficial and harmful applications are the *same capability*, not two different ones. The property that makes a model good at the intended task is the property that makes it good at the unintended one.

**This is what separates dual use from a defect.** A [failure mode](failure-modes-ai-systems.md) is something the system does wrong and could in principle do better. A dual-use risk is the system working exactly as designed, for someone else's purpose. **You cannot fix it by making the model more capable, more accurate or more reliable — those changes make it more capable at both uses.**

**The clearest demonstration in AI is also the most cited.** Urbina, Lentzos, Invernizzi and Ekins took a drug-discovery model whose purpose is to design molecules that are therapeutically active and non-toxic, and inverted the toxicity objective. The generative machinery, the training data and the compute were unchanged. In their own words: *"In less than 6 hours after starting on our in-house server, our model generated forty thousand molecules that scored within our desired threshold"* — and the model designed **not only VX itself but other known chemical warfare agents**, identified by matching against public chemistry databases. **The paper's significance is not that it is possible but that it is trivial**: it ran on an in-house server, on software the authors describe as similar to readily available open-source tools, and the safeguard that had been holding was the researchers' intent. Intent is not a control ([alignment](alignment-ai-systems.md)).

**For general-purpose models the problem is structural rather than incidental.** A model useful for writing code is useful for writing exploits; a model that summarizes literature summarizes literature on any subject; a model that persuades is not selective about what it persuades of. Brundage et al., across 26 authors and multiple institutions, frame the resulting expansion in three directions — existing threats made cheaper, new threats made possible, and the character of threats changed by scale, anonymity and psychological distance ([systemic risk](systemic-risk-ai.md)).

**Where this leaves governance, and it is uncomfortable:**

- **Capability evaluation is necessary and not sufficient.** Knowing what a model can do does not tell you what it will be used for. Evaluations establish the *upper bound* on misuse, which is a real and useful thing to know ([dangerous capability](dangerous-capability.md), [red teaming](red-teaming.md)).
- **The controls that exist are mostly not technical.** Access tiering, know-your-customer, usage terms, staged release, and export control operate on *who and why* rather than on *what* ([acceptable use policy](acceptable-use-policy.md), [permission model](permission-model-ai.md)).
- **Refusal training addresses the retail case only.** Declining to answer a harmful prompt is a real control against opportunistic misuse and a weak one against a determined actor with weights, budget and time ([jailbreak](jailbreak.md), [overrefusal](overrefusal.md) for its cost).
- **Publication is itself a decision with consequences.** The dual-use literature's oldest question — whether to publish a method whose harm is as available as its benefit — arrives unchanged, and open weights make it irreversible ([frontier AI](frontier-ai.md)).

**The EU AI Act reaches this through systemic risk rather than through the phrase.** Its general-purpose-model obligations attach where a model's reach makes misuse consequential at scale — an approach that regulates the *conditions* under which dual-use capability becomes a public problem rather than trying to define the capability itself.

---

## Plain-language version

Some dangers come from a system being broken. Dual use is the opposite: it is the danger that comes from the system working properly.

A model that is genuinely good at designing helpful molecules is, by that same skill, good at designing harmful ones. A model that writes good software writes good malicious software. There is no version of "make it better at its job" that fixes this, because being better at the job is the thing that makes the misuse possible.

**The example that made this concrete is worth knowing.** Researchers had a system for designing drug molecules — one of its goals was to avoid toxicity. They flipped that one goal to seek toxicity instead. Nothing else changed: same model, same data, same in-house server. In **under six hours it produced forty thousand** candidate compounds meeting their toxicity threshold — including the nerve agent VX and other known chemical weapons it rediscovered on its own. **The published point was not that this was clever. It was that it was easy** — ordinary hardware, software they describe as similar to what is freely available, and the only thing that had been stopping it was that nobody had asked.

This is why some AI risk questions do not have engineering answers. You can measure what a model is capable of, and you should. But capability tells you the worst case; it does not tell you what will actually happen, because that depends on who has access and what they want.

So the real controls sit somewhere less satisfying: who is allowed to use it, under what agreement, with what checks on who they are, and what happens if they break the terms. Those are decisions about people and contracts, not about the model.

**And there is a genuinely hard version of the question** that the field inherited from biology and nuclear physics: should you publish at all? If a technique's harmful use is as available as its beneficial one, describing it clearly helps both. Once model weights are released publicly, that decision cannot be revisited.

---

## AI literacy notes

1. **Dual use is the system working, not failing** — which is why capability improvements do not help.
2. **The same property enables both uses.** They are not separable features.
3. **The drug-discovery inversion was trivial** — one objective flipped, and forty thousand candidates in under six hours on an in-house server.
4. **General-purpose models are structurally dual-use**, not incidentally so.
5. **Capability evaluation gives the upper bound**, not the expected outcome.
6. **The effective controls are about access and intent**, not about the model.
7. **Refusal training works against opportunists**, not against determined actors with weights.
8. **Publication and open weights are irreversible decisions** in a way deployment is not.
9. **Misuse changes character with scale**, not only in volume.

---

## Governance notes

**Core question:** For each capability this system has, who else would want it, and what stands between them and it that is not the model's own reluctance?

**Watch for:**
- Risk assessments that evaluate the model's behavior but never ask who has access ([permission model](permission-model-ai.md))
- Refusal rates reported as a misuse control, with no distinction between opportunistic and determined misuse
- Capability evaluations read as predictions of harm rather than as upper bounds ([dangerous capability](dangerous-capability.md))
- A release decision made on benefit alone, with the misuse case never written down ([frontier AI](frontier-ai.md))
- Open-weight release treated as reversible
- Usage terms that prohibit misuse with no mechanism to detect or attribute it ([acceptable use policy](acceptable-use-policy.md))
- Fine-tuning access granted on a safety-trained model, which can remove the safety training ([fine-tuning](fine-tuning.md))
- A domain-specific model assumed safe because its purpose is benign — the drug-discovery case is exactly this
- Export-control or sanctions exposure unassessed for a capability with military or surveillance application ([compliance](compliance-ai-systems.md))

**Practice:**
- **Write the misuse case down before release, not after an incident** — name who would want this capability and what it would take them to get it
- **Evaluate for the inverted objective**, not only for the intended one; the drug-discovery result was found by someone deliberately asking the question
- **Tier access by who the user is and what they have agreed to**, and treat that as the primary control rather than the model's refusal behavior
- Assess release form separately from release decision: API, gated weights and open weights are different and only one is reversible
- **Measure refusal against its cost** so a safety control is not adopted blind to the legitimate use it blocks ([overrefusal](overrefusal.md))
- Treat downstream fine-tuning as a capability change requiring its own assessment ([model version and update](model-version-update.md))
- Keep the publication question explicit and minuted — it is a governance decision, not an academic default
- **Record what you decided not to build or not to release.** A dual-use program with no record of restraint has not made a decision

**Key accountability owner:** whoever authorizes release — because dual use cannot be delegated to the people building the capability, whose job is to make it work, and the only point where the misuse case can still be acted on is before it is available.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The concept is decades old and stable, imported into AI governance without redefinition, and the central AI demonstration is published in a peer-reviewed Nature journal by authors who deliberately withheld the operational detail. **Two scope notes.** The drug-discovery result is a *feasibility demonstration in silico* — the paper does not claim the generated compounds were synthesized or tested, and treating it as evidence of realized harm overstates it; its force is in how little effort the inversion required. The quoted figures were read from the full text rather than the abstract, which does not contain them. And the Brundage et al. report is a **2018 forecasting document**, so its threat taxonomy is durable while its specific examples predate current models — cite the structure, not the instances. This entry states no probability of misuse, deliberately: there is no defensible base rate, and the dual-use literature's own position is that the question is about conditions and access rather than likelihood.

---

## Related concepts

- [Dangerous Capability](dangerous-capability.md) — the evaluation that establishes the upper bound
- [Frontier AI](frontier-ai.md) — where the release decision is hardest
- [Systemic Risk (AI)](systemic-risk-ai.md) — misuse consequential at scale
- [Acceptable Use Policy](acceptable-use-policy.md) — the contractual control that does the real work
- [Permission Model (AI)](permission-model-ai.md) — access as the lever the model cannot provide
- [Red Teaming](red-teaming.md) — deliberately asking the inverted question
- [Jailbreak](jailbreak.md) — how refusal training is defeated at retail
- [Overrefusal](overrefusal.md) — the cost side of refusal as a control
- [Fine-Tuning](fine-tuning.md) — the step that can remove safety training
- [Alignment (AI Systems)](alignment-ai-systems.md) — why intent is not a technical property
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the category dual use is explicitly not in
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — where the decision actually sits

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-344 | Urbina, Fabio; Lentzos, Filippa; Invernizzi, Cédric; Ekins, Sean — *Dual use of artificial-intelligence-powered drug discovery* (Nature Machine Intelligence 4, pp. 189–191, 2022) · [link](https://doi.org/10.1038/s42256-022-00465-9) | The demonstration this entry is built on: inverting a single toxicity objective on an unchanged drug-discovery model, with the point being how **trivial** the change was rather than how sophisticated. Verified from the full text: **forty thousand molecules in under six hours**, including VX and other known agents. ⚠️ An in-silico result — nothing was synthesized or tested — and the authors state that details of the approach are withheld, though they were available to reviewers. |
| SRC-343 | Brundage, Miles; Avin, Shahar; Clark, Jack; Toner, Helen; Eckersley, Peter; Garfinkel, Ben; Dafoe, Allan; et al. (26 authors) — *The Malicious Use of Artificial Intelligence: Forecasting, Prevention, and Mitigation* (2018) · [link](https://arxiv.org/abs/1802.07228) | The structural framing: misuse expands existing threats, enables new ones, and changes their character through scale, anonymity and distance — from 26 authors across multiple institutions, which is what makes it a field position rather than one lab's view. ⚠️ A 2018 forecasting document; cite the taxonomy, not its examples. |
| SRC-303 | Shevlane, Toby; Farquhar, Sebastian; Garfinkel, Ben; Phuong, Mary; Whittlestone, Jess; Leung, Jade; Kokotajlo, Daniel; Marchal, Nahema; et al. (21 authors) — *Model evaluation for extreme risks* (2023) · [link](https://arxiv.org/abs/2305.15324) | The evaluation half of the answer, and its limit: capability evaluation identifies what a model *could* enable, which bounds misuse without predicting it. Twenty-one authors across competing organizations. |
| SRC-200 | European Parliament / Council of the EU — *EU AI Act, Articles 51 and 55* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | How the regulation reaches dual use without naming it: obligations attach to general-purpose models whose reach makes misuse consequential at scale, regulating the conditions rather than defining the capability. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Evaluate for the inverted objective, not only the intended one. Treat downstream fine-tuning as a capability change needing its own assessment. |
| **Organizational** | This risk has no engineering fix. The controls are access, contracts and release decisions — and only some of those can be revisited later. |
| **Client-facing** | Explains why a system built for a benign purpose still needs a misuse assessment, and why "it's a medical tool" is not an answer. |
| **LLM-native** | Refusal training is a retail control. It is weak against a determined actor with weights, and it has a measurable cost in wrongly refused legitimate use. |

---

*Last updated: v1.0 · September 2026*
