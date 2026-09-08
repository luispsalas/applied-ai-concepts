<!--meta
category: Reliability & Quality
short: Learning the training set instead of the pattern — and the reason a model's reported score is not a promise about your data
aliases: [underfitting, generalization, generalization gap, bias-variance trade-off, bias variance, double descent, why does it do well on tests but badly in practice]
tags: [Evaluation, Model Behavior, AI Literacy]
established: established
-->
# Overfitting

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
When a model learns its training material so well that it memorizes rather than generalizes — and fails on anything slightly different.

---

## Technical definition

Overfitting is when a model achieves low error on its training data and high error on data it has not seen, because it has captured detail specific to that sample rather than the structure the sample was drawn from. The distance between the two is the **generalization gap**, and it is the only number that says anything about future behavior.

**The classical framing is a trade-off with a named opposite.** Geman, Bienenstock and Doursat set it out as the **bias/variance dilemma**: a model too simple to represent the pattern has high *bias* and misses it — **underfitting** — while a model flexible enough to chase noise has high *variance* and reproduces accidents of the sample. Classically these pull against each other, and the good model is the one balanced between them.

**Underfitting is the same axis, and rarely the problem you have.** It produces consistently poor results everywhere, which makes it easy to see; overfitting produces *excellent* results in the place you are looking and poor ones everywhere else, which is why it is the failure worth naming.

**The classical picture does not straightforwardly hold for large models, and pretending otherwise is the literacy error.** Belkin, Hsu, Ma and Mandal showed a **double descent** curve: past the point where a model can fit the training data exactly, test error falls *again*, so heavily over-parameterized models can generalize well precisely where the textbook predicts disaster. Nakkiran et al. demonstrated the same in deep networks — and, more usefully, identified regimes where **bigger models and more data make performance worse**. **So "the model is huge, therefore it overfits" is not a valid inference about a modern model, and neither is its opposite.**

**What replaces the classical worry at LLM scale is memorization.** Carlini et al. extracted verbatim training examples — including personally identifiable information — from a production language model by querying it. Nasr et al. later extended this to **production, alignment-trained models**, recovering gigabytes of training data — and reported that **alignment training does not eliminate memorization**, which closes off the most common reassurance. This is overfitting's mechanism (reproducing specific training instances rather than the pattern) surfacing as a **privacy and copyright** problem rather than an accuracy one ([data leakage](data-leakage-ai-systems.md), [copyright and AI output](copyright-ai-output.md)).

**The governance consequence is about what a reported score licenses you to claim.** A model's benchmark number is a measurement on a particular held-out set; it becomes a claim about *your* data only if your data resembles that set. When the split is contaminated, the gap is invisible ([data leakage in model evaluation](data-leakage-model-evaluation.md)) — **and a hidden generalization gap does not look like a failure, it looks like a good model.**

---

## Plain-language version

Think of a student who memorizes the answers to last year's exam. On last year's exam, they are perfect. On this year's, they are lost — because they learned the answers, not the subject.

That is overfitting: the model has learned its practice material rather than the pattern behind it. It scores brilliantly on what it has seen and badly on anything new. The gap between those two scores is the only thing that tells you how it will behave in the real world.

The opposite exists too, and has a name — **underfitting**, where the model is too simple to catch the pattern at all. It does poorly everywhere. That version is easy to spot, which is exactly why it causes less trouble. Overfitting is dangerous because it looks like success.

Two things are worth knowing beyond the textbook version.

First, **"the model is enormous, so it must be overfitting" is not true of modern systems.** Researchers found that past a certain size, performance starts improving again — a pattern called double descent. The old intuition that bigger means more memorization does not reliably transfer, in either direction.

Second, **overfitting has changed shape.** For large language models, the practical worry is not that they score badly on new data — it is that they can reproduce chunks of their training material word for word. Researchers pulled real personal information out of a production model just by asking it the right way. Same underlying mechanism, but it shows up as a privacy problem rather than an accuracy one.

The thing to carry away: **a published accuracy figure is a measurement on one particular set of examples.** It becomes a promise about your situation only if your situation resembles theirs — and nobody checks that for you.

---

## AI literacy notes

1. **Overfitting looks like success**, which is what makes it dangerous; underfitting looks like failure and gets fixed.
2. **The generalization gap — training score minus held-out score — is the informative number**, not either score alone.
3. **A benchmark result is a measurement on a specific set**, and transfers to your data only insofar as your data resembles it.
4. **"Too big, therefore overfitting" is not a valid inference for modern models** — double descent breaks the classical intuition in both directions.
5. **At LLM scale the practical form is memorization**, surfacing as privacy and copyright exposure rather than as a bad score.
6. **A contaminated evaluation split hides the gap entirely**, and produces a model that appears excellent right up to deployment.
7. **Underfitting is the same axis, not a separate topic** — the classical trade-off has two ends and one dial.
8. **More training is not automatically better**: past a point, additional epochs fit noise rather than pattern.

---

## Governance notes

**Core question:** Do we know the gap between how this model performs on the data it was fitted to and the data it will actually meet — and does anyone own that number?

**Watch for:**
- A single headline accuracy figure quoted with no held-out comparison ([evaluation](evaluation.md))
- Evaluation data that overlaps the training data, so the gap cannot appear ([data leakage in model evaluation](data-leakage-model-evaluation.md))
- A model selected by repeatedly tuning against the same test set — which overfits the *selection*, not just the model
- Vendor benchmark claims accepted without asking what the held-out set contained ([AI benchmarking](ai-benchmarking.md))
- Verbatim reproduction of training material treated as a quality quirk rather than a disclosure incident ([data leakage](data-leakage-ai-systems.md))
- "The model is huge, so it can't be memorizing" — or "it's huge, so it must be" — used as reasoning instead of measurement
- Excellent pilot results on curated examples taken as evidence about production traffic
- Performance degrading after deployment attributed to drift when it was a generalization gap all along ([model/data drift](model-data-drift.md))

**Practice:**
- **Report the held-out score and the gap together**, never the training score alone
- Hold out a genuinely untouched set — one not used for tuning, selection, or prompt iteration — and touch it once
- **Test on data that resembles production, not on data that resembles the training set**; a curated pilot set is the friendliest possible case
- Check for training-data reproduction explicitly where the corpus contained personal or licensed material ([privacy](privacy-ai-systems.md), [training data](training-data.md))
- Treat repeated evaluation against one set as a form of fitting, and rotate or reserve accordingly
- Record which set produced any number that leaves the team, so a claim can be traced to its measurement ([model card / system card](model-card-system-card.md))
- Re-measure after any change to the model or its data, since the gap is a property of the pair ([model version and update](model-version-update.md))

**Key accountability owner:** whoever signs off that a model is fit for its intended use — because that judgment is a claim about *unseen* data, and the only evidence for it is a gap measured on data the model genuinely never saw.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the concept, medium on how it applies to large models — and the split is the point.** The classical definition, the bias/variance framing and the generalization gap are settled textbook material with decades of peer-reviewed support. **What is genuinely unsettled is the behavior of heavily over-parameterized models**: double descent is a robust empirical finding, replicated across architectures and reported by its own authors as a phenomenon they can characterize but not fully explain, and the theory reconciling it with classical statistics is active research. This entry therefore states the classical relationship as established, states double descent as observed, and **explicitly declines to give a rule for when a large model will or will not memorize** — because there is no reliable one. The memorization findings are strong and specific but come from particular models and attack methods; treat them as existence proofs rather than as a rate.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — where the generalization gap is supposed to be measured
- [Data Leakage (Model Evaluation)](data-leakage-model-evaluation.md) — the contamination that hides the gap
- [AI Benchmarking](ai-benchmarking.md) — published scores and what they do not license you to claim
- [Fine-tuning](fine-tuning.md) — the operation most likely to overfit, on the smallest data
- [Training Data](training-data.md) — the sample whose accidents get learned
- [Catastrophic Forgetting](catastrophic-forgetting.md) — the other way training on new data degrades a model
- [Model/Data Drift](model-data-drift.md) — degradation from the world changing, not from the fit
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — memorization surfacing as disclosure
- [Synthetic Data](synthetic-data.md) — where generated training material can narrow the distribution
- [Model Version & Update](model-version-update.md) — why the gap must be re-measured per version

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-282 | Geman, Stuart; Bienenstock, Elie; Doursat, René — *Neural Networks and the Bias/Variance Dilemma* (Neural Computation 4(1), pp. 1–58, 1992) · [link](https://doi.org/10.1162/neco.1992.4.1.1) | The classical framing this entry opens with: overfitting and underfitting as two ends of one variance/bias axis rather than separate faults, which is why underfitting is treated here as the same topic rather than its own entry. |
| SRC-283 | Belkin, Mikhail; Hsu, Daniel; Ma, Siyuan; Mandal, Soumik — *Reconciling modern machine-learning practice and the classical bias–variance trade-off* (PNAS 116(32), pp. 15849–15854, 2019) · [link](https://doi.org/10.1073/pnas.1903070116) | The **double descent** result: past the interpolation threshold, test error falls again, so over-parameterized models can generalize well exactly where the classical curve predicts failure. The basis for this entry's refusal to treat model size as evidence about memorization. |
| SRC-284 | Nakkiran, Preetum; Kaplun, Gal; Bansal, Yamini; Yang, Tristan; Barak, Boaz; Sutskever, Ilya — *Deep Double Descent: Where Bigger Models and More Data Hurt* (2019) · [link](https://arxiv.org/abs/1912.02292) | Demonstrates double descent in modern deep networks as a function of both model size and training epochs, and identifies regimes where more data and more parameters **hurt**. Cited for the "more training is not automatically better" point. |
| SRC-150 | Carlini, N. et al. — *Extracting Training Data from Large Language Models* (USENIX Security, 2021) · [link](https://arxiv.org/abs/2012.07805) | The LLM-era form of the failure: verbatim training examples, including personally identifiable information, recovered from a production model by querying it. The evidence for treating memorization as a disclosure problem rather than an accuracy one. ⚠️ An existence proof on specific models and methods, not a rate — do not restate as a general frequency. |
| SRC-161 | Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M. et al. — *Scalable Extraction of Training Data from (Production) Language Models* (2023) · [link](https://arxiv.org/abs/2311.17035) | Extends SRC-150 to production, alignment-trained models: gigabytes of training data recovered, and the finding this entry leans on — **alignment training does not eliminate memorization**. Cited to keep the memorization claim current rather than resting on a 2021 result. |
| SRC-285 | Zhang, Chiyuan; Bengio, Samy; Hardt, Moritz; Recht, Benjamin; Vinyals, Oriol — *Understanding deep learning requires rethinking generalization* (2016) · [link](https://arxiv.org/abs/1611.03530) | Establishes that deep networks can fit random labels perfectly, so capacity alone cannot explain why they generalize — the result that made the classical account insufficient before double descent characterized what replaces it. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Report the gap, not the score. Hold out a set that nothing has touched — including your prompt iteration — and touch it once. |
| **Organizational** | A model's published accuracy is a measurement on someone else's data. Signing that it is fit for your use is a separate claim, and needs its own evidence. |
| **Client-facing** | Explains why a system that demoed perfectly can disappoint in production, without implying anyone was misleading. |
| **LLM-native** | At this scale the risk is memorization, not a bad score — and it surfaces as privacy and copyright exposure. Model size tells you nothing either way. |

---

*Last updated: v1.0 · September 2026*
