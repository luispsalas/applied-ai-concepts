<!--meta
category: Observability & Governance
short: Two words used interchangeably that mean opposite things in law — one takes data out of scope, the other does not
aliases: [anonymization, anonymisation, pseudonymization, pseudonymisation, de-identification, re-identification, k-anonymity, anonymized data, is this data still personal]
tags: [Privacy, Regulatory, Data Governance]
established: established
-->
# Anonymization and Pseudonymization

> **Term status — Established.** Both are defined terms in data-protection law, in independent use across regulators, standards bodies and the re-identification literature.

## One-line essence
Two different operations that are routinely confused: one removes data from the scope of data-protection law, the other does not — and almost everything called "anonymized" in practice is the second.

---

## Technical definition

**Pseudonymization** replaces identifying fields with a key, holding the mapping separately. GDPR defines it as processing such that the data can no longer be attributed to a person **without additional information**, kept separately and subject to safeguards. **Pseudonymized data remains personal data.** Recital 26 says so directly: data which has undergone pseudonymization, and which could be attributed to a person by the use of additional information, *"should be considered to be information on an identifiable natural person."* Every obligation still applies.

**Anonymization** means the person can no longer be identified at all — and only then does the regulation stop applying. Recital 26 sets the test: whether identification is possible using *"all the means reasonably likely to be used… either by the controller or by another person"*, accounting for cost, time and **"technological developments."** **So anonymity is not a property of the dataset alone.** It is a claim about the dataset in an environment, and the environment changes.

**The difference is the whole legal consequence, and the words are used interchangeably in ordinary speech.** Pseudonymization is a security measure that reduces risk; anonymization is a change of legal status. A team saying "it's anonymized" almost always means the first.

**Re-identification research is the reason the bar is high.** Sweeney's foundational work introduced **k-anonymity** — the requirement that each record be indistinguishable from at least k−1 others — precisely because removing names does not prevent identification: combinations of ordinary attributes act as a fingerprint. The Article 29 Working Party's opinion on anonymisation techniques assesses each technique against three risks that survive naive de-identification: **singling out, linkability, and inference.** Its conclusion is the practical one — anonymization is a risk-management exercise with residual risk, not a switch.

**In AI systems there is an additional path the classical framing does not cover: the model itself.** A model trained on personal data can leak it back ([privacy attacks](privacy-attacks-ai-models.md)), and verbatim training data including personal information has been recovered from production systems ([data leakage](data-leakage-ai-systems.md)). **Anonymizing the training corpus does not automatically anonymize the model**, and a model is not obviously "a dataset" for the purposes of a technique designed for tables.

---

## Plain-language version

These two words get used as if they meant the same thing. In law they nearly mean opposites.

**Pseudonymization** is swapping names for codes and keeping the key somewhere else. It is a genuine security improvement. But the data is still personal data, and every legal duty still applies — because someone, somewhere, holds the key. The regulation says this outright.

**Anonymization** means nobody can work out who the person is anymore. Only then does data-protection law stop applying. That is a much higher bar, and it is not a property of the file on its own: the test is whether identification is possible by *any* means reasonably likely to be used, by you or by anyone else, **taking future technology into account**. So a dataset that is anonymous today can stop being anonymous because the world changed around it.

Why the bar is so high: removing names does not do the job. Combinations of ordinary details — a birth date, a postcode, a job title — act as a fingerprint. Research on this is what produced the standards used today, and the European regulators' own guidance treats anonymization as **risk management with leftover risk**, not a box that gets ticked.

**When somebody tells you data is anonymized, the useful question is: who could still put a name to a row, and what would they need?** In most systems the honest answer is that it is pseudonymized, which is fine — as long as nobody is relying on it having left the regulation's scope.

And one thing specific to AI: **anonymizing the training data does not make the model anonymous.** Models can be made to give training data back.

---

## AI literacy notes

1. **Pseudonymized data is still personal data** — a security measure, not a change in legal status.
2. **Anonymized data leaves the regulation's scope**, which is why the standard is demanding.
3. **The test includes "another person" and future technology**, so anonymity is contextual and can lapse.
4. **Removing names is not anonymization** — attribute combinations identify people.
5. **Three risks survive naive de-identification**: singling out, linkability, inference.
6. **Anonymization is risk management with residual risk**, per the regulators' own guidance.
7. **Most things called "anonymized" in practice are pseudonymized.**
8. **Anonymizing a training corpus does not anonymize the model trained on it.**

---

## Governance notes

**Core question:** When someone here says data is anonymized, which of the two do they mean — and if it is the legal claim, who assessed it and against what?

**Watch for:**
- "Anonymized" used loosely in a document that then relies on the data being out of scope
- A key or mapping held by the same team, or the same vendor, that holds the pseudonymized data
- An anonymity assessment done once and never revisited as data or technology accumulates
- Datasets anonymous in isolation and identifying in combination with something else the organization holds
- Training-data anonymization treated as covering the model ([privacy attacks](privacy-attacks-ai-models.md))
- Free-text fields de-identified by pattern matching alone, where identifiers appear in prose
- A vendor claim of anonymization accepted without the technique, the threat model, or the residual risk ([procurement of AI](compliance-ai-systems.md))
- Re-identification treated as a breach only when demonstrated, rather than as a standing risk to monitor

**Practice:**
- **Say which one you mean, every time it appears in a document** — this single discipline prevents most of the failures above
- Where the claim is anonymization, **record the technique, the threat model, and who could re-identify with what** — the assessment is the artifact, not the label
- Assess against singling out, linkability and inference, rather than against the presence of names
- Keep pseudonymization keys under separate control, and treat their holder as in scope
- **Re-assess when the environment changes** — new linked datasets, new public data, new technique — since the legal test is explicitly forward-looking
- Treat models trained on personal data as potentially disclosive regardless of corpus treatment ([data leakage](data-leakage-ai-systems.md))
- Apply data minimization first: the strongest de-identification is not collecting the field ([data minimization](data-minimization.md))

**Key accountability owner:** whoever signs the lawful-basis or scope determination — because an "anonymized" label decides whether the whole of data-protection law applies, and it is routinely applied by people describing a technique rather than making that determination.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the legal distinction, medium on any specific technique's sufficiency.** The definitions, the "still personal data" status of pseudonymized data, and the "means reasonably likely to be used" test are settled regulatory text quoted here from the source. **What is genuinely uncertain, and openly so in the regulators' own guidance, is whether a given anonymization technique is adequate for a given dataset** — that assessment is contextual, and the guidance frames it as residual-risk management rather than a threshold. The re-identification literature is strong but adversarial: it demonstrates that specific claimed-anonymous datasets were not, which supports the general caution without licensing a rate. **The AI-specific claim — that anonymizing a corpus does not anonymize the model — follows from the memorization evidence and is not yet settled in regulatory guidance.**

---

## Related concepts

- [Privacy (AI Systems)](privacy-ai-systems.md) — the broader set of obligations these techniques serve
- [Data Minimization](data-minimization.md) — not collecting the field is stronger than de-identifying it
- [Privacy Attacks (AI Models)](privacy-attacks-ai-models.md) — how a model discloses what its corpus was cleaned of
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — memorized personal data surfacing at inference
- [Training Data](training-data.md) — where corpus-level treatment applies, and stops
- [Synthetic Data](synthetic-data.md) — generated data as an alternative, with its own disclosure risk
- [Compliance (AI Systems)](compliance-ai-systems.md) — where the scope determination has consequences
- [Data Provenance / Lineage](data-provenance-lineage.md) — knowing which treatment was applied where
- [Data Quality](data-quality.md) — de-identification degrades data, and the trade should be explicit
- Federated learning — keeping data in place as a different answer to the same problem

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-299 | European Union — *GDPR Recital 26 and Article 4(5): anonymous information and pseudonymisation* (Reg. (EU) 2016/679) · [link](https://gdpr-info.eu/recitals/no-26/) | The two definitions and the decisive consequence, verified against the text: pseudonymized data *"should be considered to be information on an identifiable natural person"*, and identifiability is tested against *"all the means reasonably likely to be used… either by the controller or by another person"*, accounting for cost, time and *"technological developments."* |
| SRC-296 | Article 29 Data Protection Working Party — *Opinion 05/2014 on Anonymisation Techniques* (WP216, 2014) · [link](https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf) | The three residual risks this entry uses as the assessment frame — **singling out, linkability, inference** — and the framing of anonymization as risk management with residual risk rather than a binary. ⚠️ The Working Party was superseded by the EDPB in 2018; the opinion remains the standard reference but check for newer EDPB guidance before relying on it operationally. |
| SRC-295 | Sweeney, Latanya (Carnegie Mellon University) — *k-Anonymity: A Model for Protecting Privacy* (International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems 10(5), pp. 557–570, 2002) · [link](https://doi.org/10.1142/S0218488502001648) | The foundational re-identification result and the k-anonymity criterion — each record indistinguishable from at least k−1 others — establishing that removing direct identifiers does not prevent identification, because attribute combinations fingerprint individuals. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The regulation these definitions sit inside, and the source of the obligations that continue to apply to pseudonymized data. |
| SRC-161 | Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M. et al. — *Scalable Extraction of Training Data from (Production) Language Models* (2023) · [link](https://arxiv.org/abs/2311.17035) | Evidence for the AI-specific claim that corpus treatment does not settle model disclosure: training data recovered from production, alignment-trained models. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Assess against singling out, linkability and inference — not against the presence of names. Keep keys under separate control. |
| **Organizational** | The label decides whether data-protection law applies at all, and it is usually applied by someone describing a technique rather than making that determination. |
| **Client-facing** | Lets you answer "is our data anonymized?" honestly, including the common and acceptable answer that it is pseudonymized. |
| **LLM-native** | Cleaning the training corpus does not anonymize the model. Models can be made to return what was in them. |

---

*Last updated: v1.0 · September 2026*
