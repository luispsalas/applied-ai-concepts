<!--meta
category: Reliability & Quality
short: How much independent raters actually agree — the ceiling on what any evaluation built on their judgments can demonstrate, and almost never published beside the score it caps
aliases: [interrater reliability, inter-annotator agreement, inter-annotator reliability, rater agreement, annotator agreement, agreement rate, Cohen's kappa, kappa statistic, Fleiss kappa, Krippendorff's alpha, how much do reviewers agree]
tags: [Evaluation, Data Governance, AI Literacy]
established: established
-->
# Inter-Rater Reliability

> **Term status — Established.** A standard measurement concept across statistics, medicine, social science and machine learning since 1960, with a mature literature including its own critiques. Independent of any vendor or field.

## One-line essence
The degree to which independent people applying the same instructions to the same items reach the same judgment — which sets a hard ceiling on what any evaluation scored against those judgments can prove.

---

## Technical definition

Inter-rater reliability measures agreement between independent raters judging the same items under the same guidelines. It is the property that determines whether a set of human judgments constitutes a measurement or merely a collection of opinions.

**Raw percentage agreement is not a reliability figure**, because some agreement happens by chance. Two raters labeling a stream that is 95% negative will agree about 90% of the time while pressing the same button at random. Cohen's kappa corrects for this: it compares observed agreement against the agreement expected if the raters were guessing at their own base rates, and reports how much of the *available* room for agreement was actually used.

**The adjectives everyone quotes are a convention, not a finding.** Landis and Koch proposed the familiar bands — *slight, fair, moderate, substantial, almost perfect* — and said in the same breath what they were: *"Although these divisions are clearly arbitrary, they do provide useful 'benchmarks' for the discussion of the specific example in Table 1."* They were offered for one example in one paper. **They are now cited as thresholds by a literature the authors explicitly did not scope them to** ([bluewashing](bluewashing.md) is the marketing analogue of the same move: a real technical object, borrowed loosely).

**A low kappa is not automatically evidence of unreliable rating.** Feinstein and Cicchetti documented the paradox: when one category dominates, raters can agree on nearly every item and still produce a kappa close to zero, because chance-expected agreement is already almost total and there is little room left to beat it. **This is exactly the regime most AI evaluation lives in** — the harmful output, the fraudulent transaction, the safety violation are all rare classes ([false positives and false negatives](false-positives-and-false-negatives.md)). Kappa must be read with the prevalence of the categories, never alone.

**The ceiling argument is why this belongs in a governance vocabulary.** An evaluation compares a model's outputs against a reference set produced by raters. **If those raters agree with each other on 70% of the chance-corrected room, the reference set does not resolve more finely than that**, and a model scored against it cannot be demonstrated to exceed it — the extra precision is measuring disagreement, not capability ([evaluation](evaluation.md), [AI benchmarking](ai-benchmarking.md)). Published accuracy figures overwhelmingly appear without the agreement figure that bounds them.

**The same question applies to model raters and is asked even less often.** [LLM-as-judge](llm-as-judge.md) replaces the human rater with a model, which does not remove the reliability question — it changes who is being measured. A judge model's agreement with itself across runs, and with human raters, are both measurable and both routinely unreported ([determinism vs probabilism](determinism-vs-probabilism.md)).

**Disagreement is diagnostic, not merely noise.** Persistent disagreement on a class of items usually means the guideline is underspecified for those items, and the fix is to write the guideline rather than to average the raters ([data labeling](data-labeling.md)). Where the disagreement tracks who the raters are rather than what the items are, it is a bias signal ([bias](bias-ai-systems.md)).

---

## Plain-language version

Give two trained people the same hundred examples and the same instructions, and ask each to decide independently. How often do they land on the same answer? That number is inter-rater reliability, and it tells you whether the instructions describe something real or whether people are each interpreting them their own way.

**You cannot just count how often they matched**, because two people pressing buttons at random will still match sometimes — and if one answer is much more common than the other, they will match very often indeed by pure luck. So the standard measures subtract the agreement you would expect from chance and report what is left.

Two things about this number are worth knowing, and both are routinely got wrong.

**The famous labels are made up.** You will see "0.61 to 0.80 means substantial agreement" quoted as though it were a standard. It comes from a 1977 paper whose authors wrote, in the same passage, that the divisions were clearly arbitrary and were there to help discuss one example in one table. Fifty years and tens of thousands of citations later they are treated as thresholds. They are not.

**And a bad-looking score is not always bad.** If almost every item belongs to one category — which is the normal situation when you are looking for something rare, like fraud or harmful content — two raters can agree on ninety-nine items in a hundred and still score close to zero. The number is not lying; it is answering a narrow question about how much better than luck they did, and when luck already gets you most of the way, there is very little room left.

**Here is why any of it matters outside a statistics class.** When you say a model is 94% accurate, you mean it matched an answer key. Somebody wrote that answer key. **If the people who wrote it only agreed with each other seven times out of ten, then "94% accurate" cannot mean what it sounds like** — the model is being scored against something that is not that precise. The agreement figure is the ceiling on the claim, and it is almost never printed next to it.

---

## AI literacy notes

1. **Percent agreement is not reliability** — chance agreement must be subtracted.
2. **Rater agreement caps evaluation precision.** A model cannot be shown to beat its own answer key.
3. **The "substantial / almost perfect" bands are an arbitrary convention**, described as such by the authors who proposed them.
4. **A low kappa with a dominant category is a known paradox**, not proof of bad rating — report prevalence alongside it.
5. **Rare-event evaluation is the paradox's home ground**, which is most safety and risk work.
6. **Model judges have reliability too** — against themselves across runs, and against humans.
7. **Disagreement locates the underspecified guideline** and is worth reading rather than averaging away.
8. **Disagreement patterned by rater identity is a bias finding**, not a reliability one.
9. **Kappas are not comparable across studies** with different numbers of raters, categories, or class balance.

---

## Governance notes

**Core question:** For every accuracy or quality figure this organization relies on, who produced the reference judgments, how much did they agree, and was that figure reported?

**Watch for:**
- An accuracy or quality metric published with no agreement figure for its reference set ([evaluation](evaluation.md))
- Kappa quoted against the Landis and Koch adjectives as though they were validated thresholds
- A low agreement score dismissed, or a whole rating exercise abandoned, without checking class prevalence first
- Agreement measured on a convenient balanced sample and reported as if it applied to production traffic
- A single rater used throughout, so agreement is not measurable at all and the guideline is never tested
- Adjudication of disagreements done silently, with the reconciled label stored and the disagreement discarded
- Model-as-judge substituted for human raters with no measurement of its agreement with anyone ([LLM-as-judge](llm-as-judge.md))
- Kappas compared between studies whose rater counts, category counts or class balance differ
- Preference data for tuning collected from a labeler pool whose agreement is never published ([RLHF](rlhf.md))
- Red-team findings triaged by one person, so severity ratings have no reliability at all ([red teaming](red-teaming.md))

**Practice:**
- **Double-rate a sample of every reference set and publish the agreement figure next to the score it bounds** — this is the single practice the entry exists for
- **Report class prevalence with any kappa**, so a paradoxical low score can be recognized as one
- **Retain the disagreements, not just the adjudicated label.** The disagreement set is the most informative part of the exercise
- Treat clusters of disagreement as guideline defects and fix the guideline, then re-rate ([data labeling](data-labeling.md))
- Check whether disagreement tracks rater identity or background before treating it as noise ([bias](bias-ai-systems.md))
- **Measure a judge model's self-agreement across runs and its agreement with human raters**, and treat both as required disclosures ([LLM-as-judge](llm-as-judge.md))
- State the agreement ceiling in any external claim about system accuracy, rather than reporting the point estimate alone ([confidence vs accuracy](confidence-vs-accuracy.md))
- Where agreement is genuinely low and the guideline cannot be improved, say the task is not reliably measurable rather than shipping a number that implies it is

**Key accountability owner:** whoever signs off the evaluation — because the agreement figure is what makes an evaluation result a measurement rather than an assertion, and the decision to publish a score without it is made at sign-off, not by the people doing the rating.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The statistics are settled and sixty-five years old, and the two limitations this entry emphasizes — the arbitrariness of the benchmark bands and the prevalence paradox — are documented in the primary literature rather than being this entry's own critique. **One sourcing caveat, stated because it matters for a quotation.** The Landis and Koch paper is paywalled and was not fetched directly; the quoted sentence and the band table are reproduced identically by two independent secondary sources, which is good corroboration but is not the same as reading the original. **Anyone relying on the exact wording should verify it against the Biometrics text.** The ceiling argument is a straightforward consequence of what an evaluation compares against, not an empirical finding, and is stated that way.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — what rater agreement puts a ceiling on
- [Data Labeling](data-labeling.md) — the process whose quality this measures
- [AI Benchmarking](ai-benchmarking.md) — published scores resting on someone's answer key
- [LLM-as-Judge](llm-as-judge.md) — the model rater, with the same reliability question
- [False Positives and False Negatives](false-positives-and-false-negatives.md) — the rare-class setting where the paradox bites
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — a precise-looking number resting on an imprecise reference
- [Bias (AI Systems)](bias-ai-systems.md) — disagreement patterned by who is rating
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — preference rating as the modern rating task
- [Red Teaming](red-teaming.md) — findings whose severity is a rated judgment
- [Verification](verification.md) — checking a claim rather than accepting it
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — why a model judge disagrees with itself
- [Human-in-the-Loop](human-in-the-loop.md) — human review whose consistency is itself measurable

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-321 | Cohen, Jacob — *A Coefficient of Agreement for Nominal Scales* (Educational and Psychological Measurement 20(1), pp. 37–46, 1960) · [link](https://doi.org/10.1177/001316446002000104) | The primary for chance-corrected agreement, and for this entry's central point that raw percentage agreement is not a reliability figure. ⚠️ Two raters, nominal unordered categories, equal weighting — kappa in this form does not cover more raters or ordered categories. |
| SRC-322 | Landis, J. Richard; Koch, Gary G. — *The Measurement of Observer Agreement for Categorical Data* (Biometrics 33(1), pp. 159–174, 1977) · [link](https://doi.org/10.2307/2529310) | The source of the *slight / fair / moderate / substantial / almost perfect* bands, cited here as a caution: the authors describe the divisions as clearly arbitrary and useful for discussing their own Table 1. ⚠️ Do not cite the bands as an empirical threshold. ⚠️ Paywalled; the quoted sentence is corroborated by two independent secondary reproductions, not read from the original. |
| SRC-323 | Feinstein, Alvan R.; Cicchetti, Domenic V. — *High agreement but low Kappa: I. The problems of two paradoxes* (Journal of Clinical Epidemiology 43(6), pp. 543–549, 1990) · [link](https://doi.org/10.1016/0895-4356(90)90158-L) | The prevalence paradox: with one category dominant, raters can agree on nearly everything and still score near zero, so kappa must be read with class prevalence. ⚠️ Clinical epidemiology — the mathematics transfers exactly, the examples do not. ⚠️ No archive snapshot exists; four URL forms were checked. |
| SRC-308 | Sambasivan, Nithya; Kapania, Shivani; Highfill, Hannah; Akrong, Diana; Paritosh, Praveen; Aroyo, Lora M. (Google Research) — *"Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI* (CHI, 2021) · [link](https://doi.org/10.1145/3411764.3445518) | Evidence that reference-set quality problems are systematic and diagnosed late, which is why the agreement figure is worth demanding before a score is trusted rather than after it fails. ⚠️ Its 92% figure describes the studied population, not an industry rate. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | Establishes preference comparison by a specific labeler pool as the rating task that shapes current models — the highest-stakes place where rater agreement is measurable and rarely surfaced. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Double-rate a sample of every reference set, publish the agreement figure beside the score, and report class prevalence with any kappa. |
| **Organizational** | An accuracy figure is a comparison against someone's judgment. Ask how much those people agreed before treating the figure as a fact. |
| **Client-facing** | Explains why "94% accurate" needs a second question, and why some tasks cannot honestly be given a single quality number. |
| **LLM-native** | A judge model has reliability too — with itself across runs and with humans. Neither is usually measured, and both can be. |

---

*Last updated: v1.0 · September 2026*
