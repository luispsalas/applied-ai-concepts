<!--meta
category: Knowledge & Memory
short: Model output used as data in a later analysis — where high accuracy is not enough, because the errors are not noise and the second stage cannot see them
aliases: [generated regressors, surrogate labels, model-generated labels, LLM annotation as data, imputed variables, estimated variables, extraction used as measurement, machine-labeled data for analysis]
tags: [Evaluation, Data Governance, Model Behavior]
established: emerging
-->
# Generated Variables

> **Term status — Emerging.** The LLM-era naming is unsettled — *surrogate labels*, *generated regressors*, *model-generated variables* all appear — which is why this is filed `emerging` rather than `established`. **The underlying concept is not new or contested**: it was named, analyzed and solved in econometrics in 1984 as *generated regressors*, with a survey literature by 1993. This entry uses the broader name because the problem is no longer confined to regression.

## One-line essence
A variable that was produced by a model rather than observed, then used as though it were observed — which quietly breaks the analysis built on top of it, at accuracies most people would call good.

---

## Technical definition

A generated variable is any quantity in an analysis that was *estimated* rather than measured. In current practice it is most often a label, score or extracted field produced by a model — sentiment, topic, whether a document mentions a risk, whether a call was resolved — which is then counted, averaged, compared across groups, tracked over time, or used as an input to a second model.

**The problem is not that the labels are wrong. It is that the second stage treats them as if they were right.** An analysis run on generated variables inherits two defects that ordinary error bars do not cover:

- **Understated uncertainty.** The first-stage estimation error is invisible to the second stage, which computes its confidence intervals as though the inputs were observed facts. Pagan established this for regression in 1984: standard errors computed without accounting for the generation step are wrong, and wrong in the optimistic direction.
- **Bias, not just noise.** Model errors are **systematic** — correlated with the very features the analysis is about. A classifier that under-detects a category in one dialect, register or subpopulation does not add symmetric noise; it moves the estimate ([bias](bias-ai-systems.md)).

**The number that makes this a governance topic rather than a statistics footnote:** Egami, Hinck, Stewart and Wei show that direct use of LLM-generated labels in downstream statistical analysis produces **substantial bias and invalid confidence intervals — even with surrogate accuracy of 80–90%.** That range is precisely where a practitioner inspects a validation sample and concludes the labels are good enough to proceed. **The accuracy that feels reassuring is inside the failure region.**

**The temptation is well documented and genuine.** Gilardi, Alizadeh and Kubli report ChatGPT outperforming crowd workers on text-annotation tasks — cheaper, faster, and competitive on accuracy. That finding is about *annotation accuracy*, and it is sound. **The error is the inference from it**: that a label good enough to read is a label good enough to compute on. Those are different questions, and the second has a different answer ([data labeling](data-labeling.md)).

**Corrections exist and are not free.** Design-based approaches recover valid inference by combining the cheap generated labels with a **human-labeled probability sample**, using the sample to characterize the error structure and correct the estimate. The practical consequence: **generated variables do not remove the need for human labels — they change what the human labels are for.** They stop being the dataset and become the instrument that makes the dataset usable.

**Three places this shows up outside social science:**

- **Product and operations metrics.** "72% of tickets were resolved on first contact," where *resolved* was decided by a model ([evaluation](evaluation.md)).
- **Model evaluation itself.** A score produced by [LLM-as-judge](llm-as-judge.md) is a generated variable, and comparing two systems on it inherits every property above ([inter-rater reliability](inter-rater-reliability.md)).
- **Training pipelines.** Model-labeled data used to train the next model, where the generation step is upstream of everything ([synthetic data](synthetic-data.md), [data quality](data-quality.md)).

---

## Plain-language version

Suppose you want to know what fraction of your support conversations ended badly. Reading them all is impossible, so you have a model read them and tag each one. Then you count the tags.

That count is now a **generated variable** — a number about the world that was produced by a model rather than observed. And the moment you start doing things with it, something goes wrong that is easy to miss.

**The trouble is not that the model is inaccurate. It is that whatever you do next assumes it wasn't.** When you report "18% ended badly," or compare this quarter to last, or break it down by region, all of that arithmetic treats the model's tags as facts. The uncertainty from the tagging step simply isn't in the calculation, so your confidence intervals are too narrow and your comparisons look sharper than they are.

**And model mistakes are not random.** If the model is slightly worse at recognizing frustration in one language, or one accent, or one product line, then the differences you find between groups are partly the model's blind spots. Random errors would cancel out. These do not — they lean.

**The number worth remembering:** researchers found that using model-generated labels directly in an analysis produces substantial bias and invalid confidence intervals **even when the labels are 80–90% accurate**. That is exactly the accuracy where you check a sample, see it looks good, and decide to proceed. The reassuring number sits inside the danger zone.

None of this means don't use models to label things. It means the labels are not the finished data. **You still need some human-labeled examples — not to replace the model's work, but to measure how the model gets it wrong, so the final numbers can be corrected.** The human effort moves; it does not disappear.

Worth knowing, finally, that this is not a new AI problem with a new AI answer. Economists hit it forty years ago, working with variables that came out of a first statistical step and went into a second. They named it, worked out what it does to standard errors, and built corrections. The tooling is different now. The mistake is the same one.

---

## AI literacy notes

1. **A generated variable was estimated, not observed** — and the next step usually forgets that.
2. **Confidence intervals computed on generated variables are too narrow.**
3. **Model errors are systematic, not noise** — they correlate with what you are studying.
4. **80–90% accuracy is inside the failure region**, not safely outside it.
5. **"Accurate enough to read" and "accurate enough to compute on" are different standards.**
6. **Corrections need a human-labeled probability sample** — the human work moves rather than vanishing.
7. **An LLM-as-judge score is a generated variable** and inherits all of this.
8. **The problem was named and solved in econometrics in 1984** as generated regressors.
9. **It compounds when generated variables feed the next model's training.**

---

## Governance notes

**Core question:** For every number this organization reports, was any part of it produced by a model — and if so, what was done about the fact that the model's errors are not random?

**Watch for:**
- A reported metric whose underlying classification was done by a model, with no mention of that in the reporting
- Validation of a labeling model reported as accuracy alone, with no error structure by subgroup ([bias](bias-ai-systems.md))
- Comparisons across groups, regions or time using model-labeled data, where the model's error rate may differ across exactly those splits
- Confidence intervals or significance claims on generated variables computed as though the inputs were observed
- "The model is 90% accurate, so this is fine" — the specific inference this entry exists to block
- A human-labeled sample dropped once the model was deemed good enough, removing the only means of correction
- Model-labeled data used to train a successor with no independent validation ([synthetic data](synthetic-data.md))
- An [LLM-as-judge](llm-as-judge.md) leaderboard treated as measurement rather than as estimation
- Dashboards where the generated origin of a field is invisible downstream ([data provenance and lineage](data-provenance-lineage.md))

**Practice:**
- **Mark generated fields as generated, in the schema and on the dashboard** — provenance that survives to the point of use is the precondition for everything else
- **Keep a human-labeled probability sample and keep refreshing it.** It is what makes correction possible and what detects drift in the labeler ([model and data drift](model-data-drift.md))
- **Characterize error by subgroup, not just overall accuracy** — a single accuracy number cannot reveal the correlation that causes bias
- Apply a correction method that propagates first-stage uncertainty rather than reporting naive intervals
- **State the accuracy and the correction alongside any figure derived from generated variables**, the way an agreement figure belongs beside an accuracy claim ([inter-rater reliability](inter-rater-reliability.md))
- Re-validate whenever the labeling model changes — a model upgrade silently changes every historical comparison ([model version and update](model-version-update.md))
- Where no correction is feasible, **report the quantity as an estimate with its known limitations rather than as a measurement**
- Do not chain generated variables into further generated variables without re-validating at each step

**Key accountability owner:** whoever publishes the figure — because the generation step is invisible by the time a number reaches a slide, and the person presenting it is the last one able to say that a model, not a measurement, produced it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The statistical result is old, settled and peer-reviewed on the econometrics side, and the LLM-specific demonstration is a NeurIPS paper with a stated algorithm and guarantees. The 80–90% figure is quoted from that paper's own abstract. **Two scope limits.** The correction method is framed for computational social science and interpretable regression; **the bias mechanism generalizes to any downstream inference on model-generated variables, but the specific algorithm assumes a design — including a probability sample — that many teams do not have.** And the econometrics sources are about macroeconomic models, cited here for the structure of the problem and the maturity of the literature, not for any AI-specific claim. ⚠️ **A DOI for the 1993 survey written from memory during drafting was wrong by one digit and resolved to an unrelated paper on business cycles**; it was corrected against Crossref before entering this entry, which is the reason the verification rule exists.

---

## Related concepts

- [Data Labeling](data-labeling.md) — where the labels come from, human or otherwise
- [Inter-Rater Reliability](inter-rater-reliability.md) — the human-agreement ceiling that bounds the reference sample
- [LLM-as-Judge](llm-as-judge.md) — evaluation scores that are themselves generated variables
- [Synthetic Data](synthetic-data.md) — generated data used for training rather than for measurement
- [Evaluation (AI Systems)](evaluation.md) — where generated scores masquerade as measurements
- [Data Quality](data-quality.md) — the property a generated field silently changes
- [Bias (AI Systems)](bias-ai-systems.md) — why the errors lean instead of cancelling
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — a precise number resting on an estimated input
- [Data Provenance / Lineage](data-provenance-lineage.md) — the record that keeps "generated" visible downstream
- [Model & Data Drift](model-data-drift.md) — the labeler changing under a historical series
- [Automated Decision-Making](automated-decision-making.md) — where a generated variable becomes a decision about a person

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-337 | Egami, Naoki; Hinck, Musashi; Stewart, Brandon M.; Wei, Hanying — *Using Imperfect Surrogates for Downstream Inference: Design-based Supervised Learning for Social Science Applications of Large Language Models* (NeurIPS, 2023) · [link](https://arxiv.org/abs/2306.04746) | The result this entry is built on: direct use of model-generated labels in downstream analysis yields **substantial bias and invalid confidence intervals even at 80–90% surrogate accuracy**, plus the design-based correction that recovers valid inference. ⚠️ Framed for computational social science; the correction requires a human-labeled probability sample. |
| SRC-335 | Pagan, Adrian — *Econometric Issues in the Analysis of Regressions with Generated Regressors* (International Economic Review 25(1), p. 221, 1984) · [link](https://doi.org/10.2307/2648877) | The established anchor, and the reason this is not a new problem: using an estimated quantity as an input to a second analysis understates uncertainty, worked out four decades before anyone fed model output into a regression. ⚠️ Econometrics — the structure transfers, the estimators do not. |
| SRC-336 | Oxley, Les; McAleer, Michael — *Econometric Issues in Macroeconomic Models with Generated Regressors* (Journal of Economic Surveys 7(1), pp. 1–40, 1993) · [link](https://doi.org/10.1111/j.1467-6419.1993.tb00158.x) | The survey establishing generated regressors as a settled literature rather than a single result — registered as the evidence that the concept clears on an established anchor. ⚠️ Macroeconomics; cite for maturity of the literature, not for an AI claim. ⚠️ No archive snapshot after four URL forms. |
| SRC-338 | Gilardi, Fabrizio; Alizadeh, Meysam; Kubli, Maël (University of Zurich) — *ChatGPT outperforms crowd workers for text-annotation tasks* (PNAS 120(30), 2023) · [link](https://doi.org/10.1073/pnas.2305016120) | The source of the temptation, cited so the entry names what makes the practice attractive before explaining its cost. ⚠️ A claim about **annotation accuracy** — never evidence that generated labels are safe to compute on. SRC-337 shows that inference fails at exactly this accuracy range. |
| SRC-308 | Sambasivan, Nithya; Kapania, Shivani; Highfill, Hannah; Akrong, Diana; Paritosh, Praveen; Aroyo, Lora M. (Google Research) — *"Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI* (CHI, 2021) · [link](https://doi.org/10.1145/3411764.3445518) | The cascade pattern that describes how this defect propagates: data-origin problems surface late, far from their cause, with opaque diagnosis — which is exactly how a generated variable's bias behaves downstream. ⚠️ Its 92% figure describes the studied population, not an industry rate. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Mark generated fields in the schema, keep a refreshed human-labeled probability sample, and characterize error by subgroup rather than reporting accuracy alone. |
| **Organizational** | If a model produced any part of a number you publish, the confidence around it is narrower than it should be and its group comparisons may be the model's blind spots. |
| **Client-facing** | Explains why "the model is 90% accurate" does not make a report built on its output 90% right. |
| **LLM-native** | An LLM-as-judge score is a generated variable. Annotation accuracy and inferential validity are different standards, and the second is stricter. |

---

*Last updated: v1.0 · September 2026*
