<!--meta
category: Reliability & Quality
short: When information from the test set reaches the model during training, so measured performance describes a exam the model had already seen — the most common cause of results that do not survive deployment
aliases: [train/test contamination, benchmark contamination, test set leakage, data contamination, why did accuracy drop in production, too good to be true results, leakage]
tags: [Evaluation, Data Governance]
established: established
-->
# Data Leakage (Model Evaluation)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
When information the model should not have had reaches it before evaluation, so the score measures memory rather than capability — the single most common reason a system that tested well fails in production.

---

## Technical definition

**A different concept from [Data Leakage (AI Systems)](data-leakage-ai-systems.md), sharing a name.** That entry is about *sensitive information escaping* a system — a confidentiality failure. This one is about *evaluation information entering* the model — a measurement failure. The two are unrelated, and the collision is a genuine hazard when reading the literature.

The mechanism: a model's score is only meaningful if the data it is scored on was genuinely unseen. When any information about the test set reaches training — the rows themselves, a proxy for the answer, or statistics computed over the whole dataset before splitting — the score stops measuring generalization and starts measuring recall. **The result is systematically optimistic and fails in exactly one direction**, which is what makes it dangerous: the error always flatters.

**Kapoor & Narayanan (Patterns, 2023) established that this is systemic rather than occasional.** They document a **taxonomy of eight leakage types** *"that range from textbook errors to open research problems"* — from the naive (test rows in the training set) to the subtle (temporal leakage, where a model is trained on data from after the period it predicts) to the genuinely unresolved. Their survey found leakage across many scientific fields and hundreds of affected papers, and their case study is the pattern in miniature: in civil-war prediction, complex models reported as beating logistic regression **failed to reproduce, and did not actually beat it.**

Their proposed remedy is procedural rather than technical — **model info sheets** documenting how the split was made and what the model saw — on the argument that leakage is invisible to peer review of the paper alone.

**The LLM-era form is benchmark contamination**, and it is harder to police. When a model is pre-trained on a large scrape of the internet, public benchmarks are *in* that scrape. A high score may reflect the benchmark's presence in [training data](training-data.md) rather than capability. Because [pre-training](pre-training.md) corpora are increasingly undisclosed, **the deployer usually cannot check** — which converts a methodological problem into a procurement one.

---

## Plain-language version

Testing a model means giving it questions it has not seen, then checking the answers. The score is only worth anything if that condition holds.

Leakage is when it does not. Maybe the test questions were accidentally left in the study material. Maybe something in the training data quietly gives the answer away. Either way the model is not solving the problem — it is remembering, and the exam result says nothing about whether it can do the job.

The important part: **this kind of error only ever makes results look better.** Nobody investigates a number that came out surprisingly good, so leakage tends to survive review and get discovered in production, when the system meets genuinely new cases and the performance is not there.

Researchers who went looking found it across many fields and hundreds of papers, with eight distinct ways it happens — some obvious mistakes, some still unsolved research problems. In one case, sophisticated models reported as beating a decades-old simple method turned out, once the leak was fixed, not to beat it at all.

With today's large models there is a newer version: they were trained on huge amounts of internet text, and the standard tests are *on* the internet. So a great benchmark score may mean the model saw the test. And because companies increasingly do not say what their models were trained on, you often cannot find out.

---

## AI literacy notes

1. **Leakage errors only flatter.** They inflate, never deflate — so a surprisingly good result deserves more scrutiny than a disappointing one, not less.
2. **A benchmark score is a claim about unseen data.** If you cannot establish the data was unseen, the number is uninterpretable rather than merely uncertain.
3. **Eight distinct types, not one mistake.** Some are textbook errors; some are open research problems. "We checked for leakage" is not a single action.
4. **Temporal leakage is the subtle one** — training on data from after the period being predicted looks fine in a random split and is meaningless in production.
5. **Preprocessing before splitting leaks.** Normalizing or imputing over the whole dataset lets test-set statistics into training.
6. **Public benchmarks are in the training scrape.** For any model trained on a web crawl, assume contamination unless the provider states otherwise ([knowledge cutoff](knowledge-cutoff.md) tells you when, not what).
7. **A private held-out set built from your own data is the only score you fully control**, and it is usually the only one that predicts your deployment.
8. **Reproduction failure is the diagnostic.** Results that will not reproduce on a clean split were often never real.

---

## Governance notes

**Core question:** For every performance figure we rely on — vendor benchmark or internal evaluation — can we state what the model was scored on and establish it had not seen it?

**Watch for:**
- Vendor benchmark scores accepted as capability evidence with no statement about contamination ([evaluation](evaluation.md))
- Selection between models made on public benchmark leaderboards alone
- An internal evaluation set built from data that also fed retrieval, fine-tuning or few-shot examples
- Preprocessing, feature selection or imputation performed before the train/test split
- Time-series or forecasting work split randomly rather than chronologically
- An evaluation set reused so often it has effectively become training data through iteration
- A result markedly better than prior work, accepted without a reproduction attempt
- No record of how a split was made, so leakage cannot be ruled in or out afterwards

**Practice:**
- **Hold out a private evaluation set built from your own data, and never let it touch any other stage** — it is the only score you control end to end
- Split before you preprocess, and split chronologically wherever time matters
- **Document how the split was made** alongside the result; the model-info-sheet argument is that this is the only thing that makes leakage reviewable
- Treat a surprisingly strong result as a reproduction task, not a finding
- Ask vendors directly whether benchmarks were excluded from training, and **record the answer including a refusal to answer** ([model card](model-card-system-card.md))
- Rotate or refresh internal evaluation sets that have been iterated against many times
- Re-baseline against a simple model; leakage is often what makes a complex one look superior ([data quality](data-quality.md))

**Key accountability owner:** whoever signs off that a system is fit to deploy — because leakage is invisible in the metric they are being shown, and the only defense is demanding to know how the number was produced.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanism is elementary statistics, the taxonomy and the cross-field survey are peer-reviewed in a Cell Press journal, and the finding has been widely replicated in commentary and follow-up work. **One caution on citing it:** the headline count grows — the paper reports one figure and the authors maintain a *living* table that has since listed considerably more, so attribute the published number to the paper and the larger number to the table. **Lower on the LLM-specific half:** benchmark contamination is well documented in principle and hard to quantify in practice, precisely because the corpora are undisclosed, so treat claims about *how much* a given model was contaminated as estimates rather than measurements.

---

## Related concepts

- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — **the unrelated sense of the same name**: information escaping, not entering
- [Evaluation (AI Systems)](evaluation.md) — the practice this failure mode silently corrupts
- [Training Data](training-data.md) — where benchmark contamination originates
- [Pre-training](pre-training.md) — undisclosed corpora are why deployers cannot check
- [Knowledge Cutoff](knowledge-cutoff.md) — tells you when the corpus ends, not what is in it
- [Data Quality](data-quality.md) — the upstream discipline that catches split and preprocessing errors
- [Model Card / System Card](model-card-system-card.md) — where a contamination statement belongs
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — a strong number and a reliable system are different claims
- [Verification](verification.md) — reproduction as the check on a result that looks too good

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-243 | Kapoor, S.; Narayanan, A. (Princeton) — *Leakage and the reproducibility crisis in machine-learning-based science* (Patterns 4, 100804, 2023) · [link](https://doi.org/10.1016/j.patter.2023.100804) | The taxonomy of eight leakage types "that range from textbook errors to open research problems", the cross-field survey establishing it as systemic, the model-info-sheet remedy, and the civil-war case where complex models failed to reproduce and did not beat logistic regression. |
| SRC-065 | Liang, P. et al. (Stanford CRFM) — *Holistic Evaluation of Language Models (HELM)* (TMLR, 2023) · [link](https://arxiv.org/abs/2211.09110) | The benchmarking frame this failure mode undermines: standardized evaluation is only interpretable when the evaluation data is genuinely held out. |
| SRC-228 | Hoffmann, J.; Borgeaud, S.; Mensch, A. et al. (DeepMind) — *Training Compute-Optimal Large Language Models* (2022) · [link](https://arxiv.org/abs/2203.15556) | Why contamination is structural at LLM scale: compute-optimal training scales token count aggressively, and public benchmarks sit inside the corpora being consumed. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Split before preprocessing, split chronologically where time matters, and document how the split was made. Treat a surprisingly strong result as a reproduction task. |
| **Organizational** | Every performance figure is a claim about unseen data. Ask vendors whether benchmarks were excluded from training and record the answer — including a refusal. |
| **Client-facing** | Explains why we evaluate on our own held-out data rather than quoting published benchmark scores. |
| **LLM-native** | Public benchmarks are inside the training scrape, and undisclosed corpora mean the deployer usually cannot check — which turns a methodology problem into a procurement one. |

---

*Last updated: v1.0 · September 2026*
