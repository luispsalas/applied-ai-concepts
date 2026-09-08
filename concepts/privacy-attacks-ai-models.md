<!--meta
category: Observability & Governance
short: Querying a deployed model to get back what went into it — the training data, its members, or the model itself
aliases: [privacy attacks, membership inference, model inversion, data reconstruction, model extraction, model stealing, attacks on models, can someone steal our model]
tags: [Security, Privacy, Evaluation]
established: established
-->
# Privacy Attacks (AI Models)

> **Term status — Established.** NIST's adversarial-machine-learning taxonomy uses *privacy attacks* as a top-level category alongside evasion and poisoning, and each specific attack named here has its own peer-reviewed founding paper.

## One-line essence
Attacks that use ordinary query access to a deployed model to recover what it was built from — whether a record was in the training data, what that data contained, or the model itself.

---

## Technical definition

NIST defines privacy attacks as attacks *"to infer sensitive information about the training data or the ML model"* — a category distinct from evasion (fooling the model at inference) and poisoning (corrupting it during training). **What unites them is the access they need: a working deployment and the ability to send it queries.** No breach, no insider, no exfiltrated file.

Three named attacks, in increasing scope:

**Membership inference** — determining whether a specific record was in the training set. Shokri et al. established it against commercial machine-learning-as-a-service platforms using only query access. **The harm does not require the record's contents**: knowing that someone's data was in a clinical-trial dataset discloses the diagnosis by itself.

**Model inversion / data reconstruction** — recovering the training data rather than merely detecting it. Fredrikson et al. showed that confidence scores returned alongside a prediction are the leak: the extra precision that makes an API useful is what makes reconstruction feasible.

**Model extraction** — reconstructing a functional copy of the model itself through its prediction interface. Tramèr et al. demonstrated this against production ML APIs. **Here the victim is the model owner rather than the data subject**, which is why it is sometimes filed as an intellectual-property problem — but NIST places it in the same category, since its definition covers information about *the model* as well as the training data.

**The unifying governance fact: the interface is the attack surface, and it is the part you deliberately exposed.** Access controls, encryption at rest, and network segmentation do not address any of this, because nothing here is unauthorized access. **The queries are legitimate; only their pattern and purpose are not.**

**Precision in the response is the currency.** Confidence scores, logits and fine-grained outputs all raise utility and attack feasibility together, so mitigation is a deliberate degradation of the product ([differential privacy](anonymization-and-pseudonymization.md) is the formal instrument here, at a measurable accuracy cost).

**For language models the boundary blurs into ordinary use.** Extraction of verbatim training data from production, alignment-trained models has been demonstrated at scale, and **alignment training does not eliminate memorization** — so what is an attack in the classical framing can be a sufficiently unusual prompt here ([data leakage](data-leakage-ai-systems.md), [overfitting](overfitting.md)).

---

## Plain-language version

You do not have to break into a system to get data out of it. You can sometimes just ask the model — a lot, and cleverly.

Three versions, in order of ambition.

**Was this person in the training data?** Researchers showed you can often work this out from outside, using nothing but the model's normal responses. That alone can be the harm: if the training set was a study of a particular illness, then knowing someone was in it tells you they have it.

**What was in the training data?** Stronger, and it works because of a feature rather than a flaw: models usually return a confidence score along with the answer, and that extra precision is enough to reconstruct what they learned from.

**Can I have the model itself?** Given enough queries, someone can build a working copy of a model through its own public interface — the thing that cost a great deal to train, rebuilt from its answers.

Here is what makes this different from most security topics. **None of it is unauthorized access.** There is no break-in to detect, no stolen credential, no file leaving the building. Every request is one your system was built to answer. So the usual protections — encryption, access control, network rules — do not touch it, because nothing about it is against the rules.

The awkward trade: the thing that makes these attacks work is the thing that makes the product good. Detailed, confident, precise answers are useful *and* leaky. Defending means giving back less than you could.

And for language models the line is genuinely blurry. Getting training data out of a production chatbot has been demonstrated, and the safety training does not stop it. **The same behavior is called an attack in a research paper and an unusual prompt in a product.**

---

## AI literacy notes

1. **Query access is the attack surface** — no breach is required, and none will be detected.
2. **Membership alone can be the harm**, independent of the record's contents.
3. **Confidence scores are the leak** in reconstruction attacks — the precision is the vulnerability.
4. **Extraction's victim is the model owner**, which is why it is often missed by privacy reviews.
5. **Conventional security controls do not apply**, because the access is authorized.
6. **Mitigation degrades the product**, so it is a business decision as much as a technical one.
7. **Alignment training does not prevent memorization** in language models.
8. **The same act is an attack or a prompt** depending on framing, which is a real detection problem.

---

## Governance notes

**Core question:** What could someone learn about our training data, or rebuild of our model, using only the interface we published — and would we see it happening?

**Watch for:**
- Privacy review scoped to data at rest and in transit, with the inference interface excluded
- Confidence scores, logits or probabilities returned by default because they were easy to include
- No rate limiting or query-pattern monitoring on a model endpoint ([observability](observability.md))
- "The training data was anonymized, so the model is safe" ([anonymization and pseudonymization](anonymization-and-pseudonymization.md))
- Models trained on personal data exposed to broader query access than the data ever was
- Extraction treated purely as an IP matter and therefore never reaching the privacy assessment
- Fine-tuning on sensitive internal data followed by wide internal deployment ([fine-tuning](fine-tuning.md))
- An incident definition that cannot classify "the model answered too well" as an incident ([AI incident reporting](ai-incident-reporting.md))

**Practice:**
- **Include the inference interface in the privacy assessment**, and name it explicitly — this is the omission the whole entry exists to prevent
- **Return the least precision the use case needs.** Withholding confidence scores and coarsening outputs is the cheapest mitigation, and it is a product decision
- Rate-limit and monitor query patterns per principal; extraction and inference attacks need volume, which is detectable even though the individual queries are not
- Treat a model trained on personal data as carrying that data for access-control purposes ([permission model](permission-model-ai.md))
- Where a formal guarantee is needed, use differential privacy and **record the accuracy cost** rather than adopting it silently
- Test for memorization before release on any model fine-tuned on sensitive data ([evaluation](evaluation.md))
- Write an incident path that covers disclosure through normal operation, not only through breach ([AI incident reporting](ai-incident-reporting.md))

**Key accountability owner:** whoever approves the model's exposure — because the decision that creates this risk is the decision to publish an interface, and it is usually taken as a product or integration call rather than a privacy one.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High that the attacks work; low on how likely any given deployment is to be attacked.** Each attack has a peer-reviewed founding demonstration and a standards-body taxonomy placing it, so the mechanisms are not in dispute. **What this entry deliberately does not give is a probability or a rate.** The founding results were obtained under specified conditions — particular model families, particular query budgets, often unlimited access to confidence scores — and the literature is adversarial by design: it establishes that something is possible, not how often it happens in the field. Real-world incidence is essentially unmeasured, partly because **these attacks leave the same trace as ordinary use**, which is itself the entry's point rather than a gap in it. Treat the findings as existence proofs that justify assessing the interface, not as a basis for a risk score.

---

## Related concepts

- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — the same disclosure through ordinary use
- [Privacy (AI Systems)](privacy-ai-systems.md) — the obligations these attacks put at risk
- [Anonymization and Pseudonymization](anonymization-and-pseudonymization.md) — why corpus treatment does not settle model disclosure
- [Overfitting](overfitting.md) — memorization as the mechanism these attacks exploit
- [Training Data](training-data.md) — what is being inferred, reconstructed or recovered
- [Fine-tuning](fine-tuning.md) — how sensitive internal data gets into a widely queried model
- [Permission Model (AI)](permission-model-ai.md) — treating a model as carrying its training data
- [Observability (AI Systems)](observability.md) — query-pattern monitoring as the only detection available
- [Red Teaming](red-teaming.md) — testing for these before someone else does
- [AI Incident (Reporting)](ai-incident-reporting.md) — classifying disclosure that involved no breach

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-291 | NIST — *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* (AI 100-2 E2025) · [link](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) | The standards-backed category this entry is named for: **privacy attacks**, defined as attacks *"to infer sensitive information about the training data or the ML model"*, placed alongside evasion and poisoning, and noting that membership inference and data reconstruction *"can also be mounted by attackers with query access to a deployed ML model."* The "or the ML model" clause is what brings extraction under the same heading. |
| SRC-292 | Shokri, Reza; Stronati, Marco; Song, Congzheng; Shmatikov, Vitaly — *Membership Inference Attacks Against Machine Learning Models* (IEEE Symposium on Security and Privacy, 2017) · [link](https://doi.org/10.1109/SP.2017.41) | The founding membership-inference result, demonstrated against commercial ML-as-a-service platforms using query access alone. ⚠️ An existence proof under stated conditions, not a base rate — do not restate as a likelihood. |
| SRC-293 | Fredrikson, Matt; Jha, Somesh; Ristenpart, Thomas — *Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures* (ACM CCS, pp. 1322–1333, 2015) · [link](https://doi.org/10.1145/2810103.2813677) | Establishes that **confidence scores are the leak** in reconstruction attacks — the basis for this entry's central mitigation, which is to return less precision than you could. |
| SRC-294 | Tramèr, Florian; Zhang, Fan; Juels, Ari; Reiter, Michael K.; Ristenpart, Thomas — *Stealing Machine Learning Models via Prediction APIs* (USENIX Security, 2016) · [link](https://arxiv.org/abs/1609.02943) | The founding model-extraction demonstration against production prediction APIs, and the source for this entry's point that the victim here is the model owner rather than the data subject. |
| SRC-161 | Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M. et al. — *Scalable Extraction of Training Data from (Production) Language Models* (2023) · [link](https://arxiv.org/abs/2311.17035) | The LLM-era case: training data recovered from production, alignment-trained models, with **alignment training not eliminating memorization** — the evidence for the claim that the attack/ordinary-use boundary has blurred. |
| SRC-150 | Carlini, N. et al. — *Extracting Training Data from Large Language Models* (USENIX Security, 2021) · [link](https://arxiv.org/abs/2012.07805) | The earlier extraction result establishing that verbatim training data, including personally identifiable information, is recoverable by querying. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Return the least precision the use case needs, rate-limit per principal, and monitor query patterns — volume is detectable even when individual queries are not. |
| **Organizational** | The decision creating this risk is the decision to publish an interface, usually taken as a product call. Privacy review scoped to data at rest misses all of it. |
| **Client-facing** | Explains how data can be disclosed with no breach, no stolen credential and nothing leaving the building. |
| **LLM-native** | Alignment training does not stop memorization, and the same act is an attack in a paper and an unusual prompt in a product. |

---

*Last updated: v1.0 · September 2026*
