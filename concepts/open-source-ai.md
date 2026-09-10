<!--meta
category: Observability & Governance
short: A model release granting the freedoms to use, study, modify and share it — a defined standard requiring data information, code and parameters, which a weights-only release does not meet however often the label is applied to it
aliases: [open source model, open weights, open-weight model, open weight, OSAID, Open Source AI Definition, open model, openly available model, open-washing, openness in AI, weights available]
tags: [Data Governance, Regulatory, AI Literacy]
established: established
-->
# Open Source AI

> **Term status — Established.** Defined by a neutral standards body — the Open Source Initiative, which has defined "open source" for software for decades — in a formal, versioned document, and in overwhelming independent use across labs, regulators, press and practitioners. What is contested is the **threshold**, not the existence of the term.

## One-line essence
A model release that grants the freedoms to use, study, modify and share it — a defined standard requiring data information, code and parameters, and one that publishing weights alone does not meet.

---

## Technical definition

The Open Source Initiative's **Open Source AI Definition (OSAID) 1.0** grants four freedoms: to **use** the system for any purpose without asking permission, to **study** how it works and inspect its components, to **modify** it including to change its output, and to **share** it with or without modifications. These mirror the software definition, and on their own they are unremarkable.

**The substance is the precondition attached to them: access to the "preferred form to make modifications,"** which OSAID specifies as three elements that must *all* be present.

- **Data information** — enough detail about the training data that a skilled person could build a substantially equivalent system.
- **Code** — the complete source used to train and run the system: data processing and filtering, training arguments and settings, validation, tokenizers, hyperparameter search, inference, architecture.
- **Parameters** — the weights and configuration, potentially including intermediate checkpoints.

**The most misread provision is the first, and the entry turns on it: data information is not the data.** OSAID does not require publishing the training set. It requires a complete *description* — provenance, scope, characteristics, how the data was obtained and selected, labeling procedures, filtering methodology — plus a listing of what is publicly available and what can be obtained from third parties, including for a fee. It explicitly contemplates **unshareable data being described rather than released.** That compromise is what made the definition shippable, and it is also why parts of the community reject it as too weak, while others reject it as unworkably strict.

**Which produces the distinction that matters in practice: "open weights" is not "open source."** A release that publishes parameters — even under a permissive license, even at frontier scale — has supplied one of the three elements. You can run it, and you can [fine-tune](fine-tuning.md) it. You cannot rebuild it, audit what went into it, or establish what it learned and from whom.

**And openness is not a yes/no property.** Liesenfeld and Dingemanse assess generative AI systems against an evidence-based framework of **14 dimensions** — training datasets, documentation, licensing, access methods — across a survey of **more than 45 systems**, and find that while the term *open source* is widely used, **many models are "open weight" at best**, with providers withholding information on training and fine-tuning data in a way the authors characterize as evading scientific, legal and regulatory scrutiny. Their conclusion is the load-bearing one: **openness is composite and gradient** — it consists of multiple elements and comes in degrees — so declaring a model open or closed on any *single* feature, whether license or access, is a category error.

**Three reasons this is a governance question rather than a labeling one.**

- **Regulatory status attaches to it.** Open source systems are regulated differently, which converts a definitional dispute into a question about which obligations apply — and creates a direct incentive to claim the label ([AI governance](ai-governance.md), [compliance](compliance-ai-systems.md)).
- **Assurance depends on it.** Every claim about a model that requires inspecting its components — bias analysis, [third-party audit](third-party-audit.md), reproducing an evaluation — is bounded by what the release actually grants ([black box](black-box.md), [evaluation](evaluation.md)).
- **The disclosure it demands is the disclosure the ecosystem is worst at.** Data information is precisely the element most often withheld, and even where provenance *is* attempted, the Data Provenance Initiative's audit of over 1,800 text datasets found **license omission above 70% and error rates above 50%** on widely used hosting platforms. The requirement runs into an ecosystem that frequently cannot supply it accurately ([data provenance and lineage](data-provenance-lineage.md), [training data](training-data.md)).

**The dispute does not resolve, and that is a finding rather than a gap.** A multi-sectoral participatory study reports four recurring tensions that surface whenever general agreement about openness is turned into concrete action: its **purpose** (an end in itself, or a means to something else), its **scope** (expanding access, versus making access *meaningful*), and its **operation** (mandatory or conditional; sufficient on its own, or dependent on governance and use). The authors conclude that responsible openness is **not a singular technical solution but a negotiated sociotechnical project.** This entry takes that as its posture: it reports the standard a neutral body publishes and the objections to it, and does not adjudicate between them.

---

## Plain-language version

For software, "open source" has a clear meaning: you get the source code, so you can read it, change it, and build your own copy. Everyone knows what the source is.

**For a model, it is not obvious what the source even is.** The weights — the giant pile of numbers that makes the model work — are not instructions someone wrote. They are the *output* of a training process, closer to a baked cake than a recipe. Handing them over lets you run the model and adjust it at the edges. It does not let you understand how it came to be, or make it again.

So the definition asks for the things that would let you make it again: enough information about the training data that a competent team could assemble something equivalent, the code that did the training, and the weights themselves.

**Here is the part almost everyone gets wrong.** The definition does **not** require publishing the training data. It requires *describing* it thoroughly — where it came from, how it was chosen, how it was filtered, what is publicly available and what you would have to buy. Data that cannot be shared can be described instead. That compromise is why the definition exists at all, and also why some people think it does not go far enough and others think it goes too far.

**In practice, most models called "open" have released only the weights.** That is a real and useful thing — you can run them yourself, keep your data in-house, adapt them. It is just not the same thing, and the difference shows up exactly when it matters: when someone asks what the model was trained on, or wants to check it independently, or needs to reproduce a result.

**Two things follow.** The label is worth something — rules treat open systems differently, so claiming it has consequences beyond marketing, which is why the claim gets stretched. And **openness is not a switch.** Researchers who scored more than 45 systems across fourteen separate dimensions found it varies continuously, and that judging a model by any one feature — usually its license — reliably gets the answer wrong.

The useful question is never "is it open source?" It is **"which of these specific things did they actually give me, and is that enough for what I need to do?"**

---

## AI literacy notes

1. **"Open weights" and "open source" are different claims** — weights are one of three required elements.
2. **Weights are an output, not a recipe** — you can run and adapt them, not rebuild the model.
3. **The definition does not require releasing the training data**, only a description sufficient to rebuild an equivalent system.
4. **Openness is composite and gradient**, not a switch — assessed across 14 dimensions in the cited survey.
5. **Judging by license alone gets it wrong**, which is the single most common shortcut.
6. **Many systems marketed as open are "open weight" at best.**
7. **The label carries regulatory consequences**, so the incentive to claim it is not merely reputational.
8. **Data information is the element most often missing** — and the hardest to supply accurately.
9. **The term is settled; the threshold is not** — a neutral body has published a definition, and it is genuinely contested.
10. **Ask what you were actually granted**, then ask whether it covers what you need to do.

---

## Governance notes

**Core question:** For each model this organization depends on, which of use, study, modification and redistribution were actually granted — and is that enough for the obligations we have taken on?

**Watch for:**
- "Open source" used in a procurement document, a model card or a compliance filing with no statement of which elements were released ([model card / system card](model-card-system-card.md))
- A permissive-sounding license treated as settling the question, with no data information and no training code
- Field-of-use restrictions, acceptable-use terms or user-count thresholds in a license described as open ([acceptable use policy](acceptable-use-policy.md))
- Regulatory relief claimed on the basis of open source status that the release would not support if tested
- A bias, safety or reproducibility commitment made about a model whose components cannot be inspected ([third-party audit](third-party-audit.md), [black box](black-box.md))
- Openness asserted at the level of the *model* while the deployment adds closed components, so the system as a whole is not what the label describes
- A model's status assumed to be stable, when a license or release terms can change at the next version ([model version and update](model-version-update.md))
- "Open" treated as a synonym for safe, free, or unencumbered — three separate questions ([dual use](dual-use.md), [supply chain risk](supply-chain-risk-ai.md))

**Practice:**
- **Record which elements you received, not the label**: parameters, training code, data information, and the license terms attached to each. That record is what every later assurance question resolves against
- **State the definition and version you are testing against** — OSAID 1.0 is a versioned document, and "open source" without a referent is not a claim that can be checked
- **Assess by dimension, not by verdict.** A gradient framework gives an answer you can act on; a binary gives one you will have to defend
- Where regulatory treatment depends on the status, **get the determination reviewed rather than asserted** — the label is the trigger, and the incentive to over-claim runs in one direction ([compliance](compliance-ai-systems.md))
- **Do not promise what the release cannot support.** If you cannot inspect training data, you cannot make first-hand claims about its composition, however confident the provider's summary is
- Re-check the terms at each version rather than inheriting a determination made about an earlier release
- Where an obligation genuinely requires inspection, **treat the missing element as a procurement requirement**, not as something to be worked around after the fact
- **Say "open weights" when that is what you mean.** Precision here costs nothing and is the single cheapest way to stop the confusion propagating

**Key accountability owner:** whoever signs the compliance or procurement determination — because the label is what triggers different treatment, the marketing claim arrives upstream of them, and they are the last person positioned to ask which elements were actually granted before an obligation is assumed or waived.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the definition and on the practice finding.** The four freedoms and the three preferred-form elements were read directly from the Open Source Initiative's published OSAID 1.0 page rather than reproduced from memory, and the composite-and-gradient finding is peer-reviewed at ACM FAccT with a stated framework and a survey of more than 45 systems.

**Three scope limits, stated deliberately.** First, **this entry does not cite any statutory provision.** The regulatory-consequence point rests on the peer-reviewed premise that open source systems are regulated differently under the EU AI Act — **the specific articles were not verifiable at drafting time**, because every EUR-Lex endpoint tried, including the archived copy, returned an empty response, so no article number is stated here and none should be added without reading the text. Second, the survey evidence is a **snapshot of a fast-moving landscape**: the framework and the open-weight-at-best finding are cited, no individual model is named, and the counts should not be treated as current. Third, **OSAID is contested and this entry does not adjudicate the dispute** — it reports the standard a neutral body publishes alongside the objections to it, which is the posture the participatory study's own conclusion supports.

---

## Related concepts

- [Local LLMs](local-llms.md) — what an open-weights release actually enables
- [Frontier AI](frontier-ai.md) — where release decisions carry the most weight
- [Training Data](training-data.md) — the element the definition asks you to describe
- [Data Provenance / Lineage](data-provenance-lineage.md) — the record that makes data information possible, and is often broken
- [Model Card / System Card](model-card-system-card.md) — where the released elements should be stated
- [Third-Party Audit](third-party-audit.md) — the assurance that depends on what was granted
- [Black Box](black-box.md) — what a weights-only release leaves you with
- [Fine-Tuning](fine-tuning.md) — the modification an open-weights release does permit
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — third-party artifacts of uncertain provenance
- [Copyright & AI Output](copyright-ai-output.md) — the rights questions upstream of any release
- [Dual Use](dual-use.md) — the argument that release decisions are safety decisions
- [Bluewashing](bluewashing.md) — the general pattern of which open-washing is one instance
- [AI Governance](ai-governance.md) — where the determination is made and owned

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-359 | Open Source Initiative — *The Open Source AI Definition — 1.0* · [link](https://opensource.org/ai/open-source-ai-definition) | The definitional anchor: four freedoms plus the **preferred form to make modifications** — data information, code, parameters — and the provision this entry turns on, that **data information is not the data**, explicitly allowing unshareable data to be described rather than released. ⚠️ Definitional, not empirical: it says what the term means, never who complies. ⚠️ A versioned living document at an unversioned URL, and genuinely contested — cited as the definition a neutral body publishes, not as consensus. |
| SRC-360 | Liesenfeld, Andreas; Dingemanse, Mark (Radboud University) — *Rethinking open source generative AI: open washing and the EU AI Act* (ACM FAccT, 2024) · [link](https://doi.org/10.1145/3630106.3659005) | The evidence that **openness is composite and gradient**: 14 dimensions across a survey of more than 45 generative AI systems, finding the term widely used while **many models are "open weight" at best**, and that relying on any single feature to declare a model open is a mistake. Also the premise that open source systems are regulated differently, which makes the label consequential. ⚠️ A snapshot of a fast-moving landscape — the framework and the finding are cited, no individual model is. ⚠️ Predates OSAID 1.0 and is not a commentary on it. |
| SRC-361 | Smith, Genevieve; Patel, Hiral; Okolo, Chinasa T.; Osborne, Cailean; Widder, David Gray; et al. (23 authors) — *Reimagining Open Source and Openness in AI: Co-Creating Responsible Technological Futures* (ACM FAccT, 2026) · [link](https://doi.org/10.1145/3805689.3806719) | Why the dispute does not resolve, documented rather than asserted: four tensions surfacing when agreement about openness meets concrete action — **purpose** (end or means), **scope** (expansion versus meaningful access), and **operation** (mandatory versus conditional, sufficient versus governance-dependent) — and the conclusion this entry adopts as its posture, that responsible openness is a **negotiated sociotechnical project** rather than a singular technical solution. ⚠️ A participatory workshop study: the tensions are a structure for the disagreement, not a measured distribution of opinion. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | Why the data-information requirement is the hard one: an audit of **1,800+ text datasets** found **license omission above 70% and error rates above 50%** on widely used hosting platforms — so the element the definition demands is the one the surrounding ecosystem is least able to supply accurately. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Record which elements you received — parameters, training code, data information — and the license on each. Assess by dimension rather than by verdict, and say "open weights" when that is what you have. |
| **Organizational** | The label triggers different regulatory treatment, so it is a determination someone signs, not a marketing word. Ask which of the four freedoms the release actually grants before assuming or waiving an obligation. |
| **Client-facing** | Explains why "it's open source" is not one claim but several, and why the honest answer to "can you check what it was trained on?" usually depends on something the provider chose not to publish. |
| **LLM-native** | Weights are the output of training, not its source. Data information means a description sufficient to rebuild an equivalent system — not the dataset. Openness is composite and gradient; single-feature tests fail. |

---

*Last updated: v1.0 · September 2026*
