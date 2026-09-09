<!--meta
category: Observability & Governance
short: A mathematical guarantee that one person's presence in the data barely changes what comes out — a property of the computation, not a label on the dataset, and meaningless without its parameters
aliases: [differentially private, DP, epsilon differential privacy, privacy budget, privacy loss parameter, DP-SGD, differentially private training, epsilon]
tags: [Privacy, Data Governance, Regulatory]
established: established
-->
# Differential Privacy

> **Term status — Established.** Defined in a 2006 cryptography paper, developed in a large peer-reviewed literature, deployed in national statistical systems, and — the decisive evidence for this entry — the subject of a dedicated NIST Special Publication on how to evaluate a claim of it. Cleared on the **governance route**: a national standards body treats it as a term with a checkable meaning.

## One-line essence
A formal guarantee that whatever the system publishes, it would have been almost exactly as likely to publish had any one individual never been in the data at all.

---

## Technical definition

Differential privacy is a property of an **algorithm**, not of a dataset or of an output.

The definition compares two worlds: one where a given individual's record is in the input, and one where it is not. An algorithm is differentially private if the probability of producing any particular output is nearly the same in both, with "nearly" bounded by a parameter **ε (epsilon)**. Dwork, McSherry, Nissim and Smith achieve this by adding noise calibrated to *sensitivity* — how much any single record could move the answer.

**That framing is the whole point, and it is what marketing usually loses.** A traditional anonymization approach asks whether a released table can be re-identified ([anonymization and pseudonymization](anonymization-and-pseudonymization.md)). Sweeney's k-anonymity is a property of the table, and properties of tables can be defeated by information the publisher never saw. **Differential privacy makes no claim about the data; it constrains the computation** — which is why the guarantee holds regardless of what an attacker knows already, including a complete copy of everyone else's records.

**Four properties determine whether a claim means anything:**

- **ε is a policy choice with no mathematically correct value.** It is a knob spanning orders of magnitude, and low and high settings buy very different protection. **A claim of "differential privacy" without a stated ε is not a claim** — it names a technique, not a guarantee.
- **Privacy loss composes.** Run several analyses and the losses add up. A per-query ε is not the budget that matters; the cumulative budget over the lifetime of the data is.
- **Post-processing cannot weaken it.** Anything computed from a differentially private output is still covered. This is what makes the guarantee robust to downstream cleverness.
- **The unit of privacy decides the strength.** A guarantee "per event" is much weaker than one "per user" when one user generates thousands of events. NIST's evaluation guidance treats the unit, alongside ε, as central to reading any claim — and it is the parameter most often unstated.

**Applied to model training, the mechanism is DP-SGD**: clip each example's gradient contribution to a bounded size, add calibrated noise to the sum, and account for the cumulative privacy loss across training steps. The trained model then carries a stated guarantee ([training data](training-data.md)). **It is bought with accuracy and compute**, and that trade — not the mathematics — is the decision a governance reader is actually making.

**What it buys is a bound on a family of real attacks.** Membership inference — determining whether a specific person's record was in the training set — is bounded by construction under differential privacy, and so are the extraction and inversion attacks that depend on a model having memorized an individual ([privacy attacks](privacy-attacks-ai-models.md), [data leakage](data-leakage-ai-systems.md)).

**What it does not buy:** it says nothing about whether collecting the data was lawful or necessary ([data minimization](data-minimization.md)), nothing about group-level inferences that are true of a population rather than a person, and nothing at all once ε is set high enough to be decorative.

---

## Plain-language version

Imagine a report is published using data that includes you. Differential privacy is a promise about that report: **whatever it says, it would have said almost exactly the same thing if your record had never been collected.** Your presence made almost no difference to the output, so the output can reveal almost nothing about you specifically.

The way this is achieved is by adding a carefully measured amount of randomness — enough to hide any single person's contribution, not so much that the overall picture is lost.

Two things make this different from the older idea of "anonymized data."

**Anonymization is a claim about a file. This is a claim about a procedure.** Stripping names from a table and hoping nobody can work out who is who has repeatedly failed, because someone always turns out to hold the other half of the puzzle. Differential privacy sidesteps that entirely: because the guarantee is about how much any one person could have changed the answer, it holds no matter what else an attacker already knows.

**And it comes with a dial.** There is a number, epsilon, that sets how much difference a person is allowed to make. Small means strong protection and a blurrier answer; large means a sharper answer and weaker protection. There is no scientifically correct setting — it is a policy decision. So **"we use differential privacy" on its own tells you nothing.** It is like being told a door is locked without being told whether it is a bank vault or a suitcase latch. The right question is always: at what epsilon, and privacy for what unit — each event, or each person?

One more thing worth knowing, because it is the most common way a real guarantee gets quietly weakened. **The protection gets used up.** Every additional analysis run on the same data spends more of the budget. A system that publishes one report with strong protection and then publishes forty more has not published forty strongly protected reports.

---

## AI literacy notes

1. **It is a property of the algorithm**, not of the dataset or the output file.
2. **The guarantee holds against attackers with outside information** — that is its main advance over anonymization.
3. **ε is a policy dial with no correct value**, spanning orders of magnitude.
4. **"Differentially private" with no stated ε is not a claim.**
5. **Privacy loss composes** — the lifetime budget matters, not the per-query one.
6. **Post-processing cannot break it**, which is why the guarantee is durable downstream.
7. **The unit of privacy — event or user — changes the strength enormously** and is often unstated.
8. **DP-SGD applies it to model training**, at a cost in accuracy and compute.
9. **It bounds membership inference and memorization attacks** by construction.
10. **It does not make collection lawful or necessary**, and says nothing about group-level inference.

---

## Governance notes

**Core question:** For any system here described as differentially private — what is ε, what is the unit of privacy, and who is tracking the cumulative budget?

**Watch for:**
- "Differential privacy" claimed with no ε published ([bluewashing](bluewashing.md))
- An ε disclosed per query while the data is queried repeatedly, with no cumulative accounting
- A per-event guarantee presented as a per-user one
- ε set high enough that the guarantee is nominal, chosen for utility and reported as protection
- Differential privacy cited as satisfying a data-protection obligation that is actually about lawfulness or necessity ([compliance](compliance-ai-systems.md), [data minimization](data-minimization.md))
- A vendor claim of differential privacy with no description of the mechanism or threat model ([supply chain risk](supply-chain-risk-ai.md))
- DP-SGD adopted and then the accuracy cost quietly recovered by weakening ε
- Synthetic data described as private because it was generated by a model, with no formal guarantee behind it ([synthetic data](synthetic-data.md))
- The guarantee assumed to cover inferences about groups, which it does not

**Practice:**
- **Require ε, the unit of privacy, and the composition accounting as a disclosure** — a differential-privacy claim without all three should be treated as unsubstantiated
- **Set and record ε as a governance decision with a named owner**, not as a tuning parameter chosen by whoever ran the job
- **Track the cumulative privacy budget across the data's lifetime**, including analyses run by other teams
- Use NIST SP 800-226 as the checklist for evaluating a third party's claim rather than accepting the label ([AI governance](ai-governance.md))
- **State the utility cost openly** alongside the guarantee, so the trade is visible to whoever owns the outcome
- Do not let a formal guarantee substitute for collection discipline — minimize first, then protect what remains ([data minimization](data-minimization.md))
- Where a claim cannot be substantiated, say the data is *noised* rather than *differentially private*; the terms are not interchangeable
- Re-verify the standards edition before citing clause detail — this area is actively revised ([model version and update](model-version-update.md) has the same discipline for models)

**Key accountability owner:** whoever owns the data being protected — because ε is a decision about acceptable risk to the people in that data, and it is the one parameter in this entire mechanism that no mathematician can choose for you.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The definition, the composition and post-processing properties, and the DP-SGD construction are all peer-reviewed, mature and uncontested; the governance framing is taken from a final NIST Special Publication rather than from commentary. **Two limits.** The DP-SGD utility figures are from 2016 on small models — **the accuracy cost at modern model scale is different and remains an open research question**, so this entry states that a cost exists without quantifying it. And the claim that DP bounds membership inference is a statement about what the guarantee implies, which is exact; whether any *particular* deployment achieves it depends on implementation details that a published ε does not reveal. **A stated ε is necessary for a claim to be assessable, not sufficient for it to be true.**

---

## Related concepts

- [Privacy (AI Systems)](privacy-ai-systems.md) — the broader obligation this is one technique within
- [Anonymization and Pseudonymization](anonymization-and-pseudonymization.md) — the dataset-property approach this replaces
- [Privacy Attacks on AI Models](privacy-attacks-ai-models.md) — the attacks the guarantee bounds
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — memorization as the leak DP constrains
- [Data Minimization](data-minimization.md) — the obligation DP does not discharge
- [Federated Learning](federated-learning.md) — decentralized training that needs DP to be private
- [Training Data](training-data.md) — what DP-SGD protects
- [Synthetic Data](synthetic-data.md) — generation without a formal guarantee is not privacy
- [Compliance (AI Systems)](compliance-ai-systems.md) — what a technical guarantee does and does not satisfy
- [Bluewashing](bluewashing.md) — a real technical object borrowed as a label
- [AI Governance](ai-governance.md) — where the ε decision belongs

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-324 | Dwork, Cynthia; McSherry, Frank; Nissim, Kobbi; Smith, Adam — *Calibrating Noise to Sensitivity in Private Data Analysis* (Theory of Cryptography Conference, 2006) · [link](https://doi.org/10.1007/11681878_14) | The originating definition and the entry's central pin: a guarantee about the **algorithm**, bounding how much one individual's presence can change the output distribution — with sensitivity-calibrated noise as the mechanism. |
| SRC-325 | Dwork, Cynthia; Roth, Aaron — *The Algorithmic Foundations of Differential Privacy* (Foundations and Trends in Theoretical Computer Science 9(3–4), pp. 211–407, 2014) · [link](https://doi.org/10.1561/0400000042) | The properties that decide whether a claim is meaningful: **composition** (loss accumulates across queries), post-processing immunity, and ε as a policy choice with no correct value. ⚠️ Predates DP-SGD's use in deep learning — cite for foundations, not for current practice. |
| SRC-326 | Near, Joseph; Darais, David; Lefkovitz, Naomi; Howarth, Gary (NIST) — *NIST SP 800-226: Guidelines for Evaluating Differential Privacy Guarantees* (final, March 2025) · [link](https://csrc.nist.gov/pubs/sp/800/226/final) | The governance anchor, and the establishment evidence for this term: a national standards body publishing how to **evaluate** a differential-privacy claim, with the unit of privacy and the deployment model treated as central to reading one. ⚠️ Confirm this is still the current edition before citing clause detail. |
| SRC-327 | Abadi, Martin; Chu, Andy; Goodfellow, Ian; McMahan, H. Brendan; Mironov, Ilya; Talwar, Kunal; Zhang, Li (Google) — *Deep Learning with Differential Privacy* (ACM CCS, 2016) · [link](https://doi.org/10.1145/2976749.2978318) | DP-SGD: per-example gradient clipping plus calibrated noise, with privacy accounting across training steps — the bridge from the definition to a trained model. ⚠️ Vendor-authored; 2016 results on small models, so the utility cost at current scale is not what this paper measured. |
| SRC-295 | Sweeney, Latanya (Carnegie Mellon University) — *k-Anonymity: A Model for Protecting Privacy* (International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 10(5), pp. 557–570, 2002) · [link](https://doi.org/10.1142/S0218488502001648) | The contrast that makes the definition legible: a property of a released **table**, which is precisely what differential privacy stopped trying to guarantee. ⚠️ Cite for the founding insight, never as a current sufficiency standard. |
| SRC-292 | Shokri, Reza; Stronati, Marco; Song, Congzheng; Shmatikov, Vitaly — *Membership Inference Attacks Against Machine Learning Models* (IEEE Symposium on Security and Privacy, 2017) · [link](https://doi.org/10.1109/SP.2017.41) | The concrete attack that differential privacy bounds by construction, which is what turns the guarantee from an abstraction into a control with a named threat. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Publish ε, the unit of privacy, and the composition accounting. Track the cumulative budget across teams, not per query. |
| **Organizational** | ε is a risk decision about the people in your data, and it is the one parameter no expert can choose for you. Demand it before accepting the label. |
| **Client-facing** | Explains why "we use differential privacy" is an incomplete answer, and what the follow-up question is. |
| **LLM-native** | DP-SGD gives a trained model a stated guarantee against memorization attacks, paid for in accuracy and compute. |

---

*Last updated: v1.0 · September 2026*
