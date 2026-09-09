<!--meta
category: Knowledge & Memory
short: The human work that produces every label a model learns from and every benchmark it is judged against — undervalued in exactly the systems that depend on it most
aliases: [data labelling, annotation, data annotation, labeling, labelers, annotators, ground truth, data work, who labels the data]
tags: [Data Governance, Ethics, Evaluation]
established: established
-->
# Data Labeling

> **Term status — Established.** A recognized term of art across machine learning practice and research, in independent use well beyond any single originator.

## One-line essence
The human work of attaching labels to data — the process that produces the ground truth every model is trained toward and every evaluation is scored against.

---

## Technical definition

Data labeling is the assignment of the target values a supervised model learns to predict, and of the reference answers an evaluation compares against. It covers classification labels, bounding boxes, transcriptions, relevance judgments, and — in the current era — the preference comparisons behind [RLHF](rlhf.md) and the reference sets behind benchmarks ([evaluation](evaluation.md), [AI benchmarking](ai-benchmarking.md)).

**Labeling is a judgment process, not a transcription process, and that is what makes it governance-relevant.** Someone writes guidelines deciding what counts as toxic, relevant, or correct; someone else applies them to ambiguous cases. **Those two decisions determine what the model treats as true**, and neither is visible in the finished dataset ([bias](bias-ai-systems.md)).

**The empirical finding this entry is built on is that the work is systematically undervalued in exactly the applications where it matters most.** Sambasivan et al. document **data cascades** — compounding downstream problems originating in data quality — affecting **92% of the AI practitioners they interviewed**, and trace them to a culture in which model work is prestigious and data work is not. Their title states the mechanism: *"Everyone wants to do the model work, not the data work."* The cascades are described as **opaque in diagnosis, with no clear indicators**, surfacing late and far from their cause.

**Agreement between labelers is the ceiling on measurement.** If two qualified annotators disagree on a fifth of cases, no model can be shown to exceed that on the same task — the evaluation cannot resolve finer than its reference. **Inter-annotator agreement is rarely reported**, which means most published accuracy figures have an unstated ceiling.

**Two structural facts about who does the work.** It is frequently outsourced to contractors in lower-wage regions, under conditions the buying organization does not see; and for content-moderation and safety data it involves sustained exposure to distressing material. **Neither appears in a model card, and neither is a technical matter** ([model card / system card](model-card-system-card.md)).

**Synthetic and model-generated labels change the economics and relocate the problem rather than removing it** — the judgment is now the labeling model's, and its biases are inherited wholesale ([synthetic data](synthetic-data.md), [LLM-as-judge](llm-as-judge.md)).

---

## Plain-language version

Before a model can learn, somebody has to say what the right answer is. Is this email spam. Is this reply better than that one. Is this comment abusive. That is data labeling, and it is where a model's idea of "correct" comes from.

Two things are worth understanding.

**It is judgment, not clerical work.** Someone writes the rules for what counts as abusive; someone else applies those rules to cases the rules did not anticipate. Those choices become the model's definition of the thing. They are made early, by people whose names nobody records, and they are invisible in the finished dataset.

**And the work is undervalued precisely where it matters most.** Researchers interviewing AI practitioners working on high-stakes systems found that **92% had experienced compounding problems traceable to data quality** — and they trace the cause to a professional culture where building models is prestigious and preparing data is not. Their title says it: *"Everyone wants to do the model work, not the data work."* The problems are hard to diagnose because they show up late, far from where they started.

There's a measurement consequence that follows directly. **If two trained people disagree about a fifth of the cases, then no model can be proven better than that on the same task** — the answer key itself isn't that precise. That figure is almost never published alongside the accuracy score it caps.

Finally, the part that is not technical at all: this work is often contracted out to people in lower-wage countries, under conditions the company buying it does not see, and for safety and moderation data it means looking at genuinely distressing material all day. **None of that appears in any documentation of the model it produced.**

---

## AI literacy notes

1. **Labeling is judgment, not transcription** — guidelines and edge-case calls become the model's definition of correct.
2. **Data cascades affected 92% of practitioners studied**, and are diagnosed late because their indicators are opaque.
3. **Inter-annotator agreement caps what any evaluation can show** — and is rarely reported.
4. **The guidelines are the artifact to ask for**, not the label counts.
5. **Labor conditions are part of the supply chain** and appear in no model documentation.
6. **Safety and moderation labeling carries psychological cost** to the people doing it.
7. **Model-generated labels relocate the judgment**, they do not remove it.
8. **Prestige asymmetry is the root cause identified by the research** — a cultural fact with technical consequences.

---

## Governance notes

**Core question:** For the datasets and benchmarks this system depends on, who wrote the labeling guidelines, who applied them, and under what conditions?

**Watch for:**
- Accuracy claimed against a reference set whose inter-annotator agreement is unknown ([evaluation](evaluation.md))
- Labeling guidelines undocumented or unavailable, so the definition of "correct" cannot be examined
- Ambiguous cases resolved silently by individual labelers rather than escalated and recorded
- Labeling outsourced with no visibility into pay, conditions, or reviewer wellbeing ([supply chain risk](supply-chain-risk-ai.md))
- Benchmark reference sets treated as ground truth rather than as one group's judgment ([AI benchmarking](ai-benchmarking.md))
- Model-generated labels adopted for cost without accounting for inherited bias ([LLM-as-judge](llm-as-judge.md))
- Persistent quality problems attributed to the model when they originate upstream — the cascade pattern
- No feedback route from a labeler who thinks the guideline is wrong

**Practice:**
- **Treat labeling guidelines as a governed artifact** — versioned, reviewed, and retained with the dataset ([data provenance and lineage](data-provenance-lineage.md))
- **Measure and publish inter-annotator agreement** alongside any accuracy figure; without it the figure has an unstated ceiling
- Route ambiguous cases to adjudication and record the decision, so precedent accumulates instead of dispersing
- **Ask suppliers about pay, conditions and wellbeing support, and record the answer** — including a refusal ([supply chain risk](supply-chain-risk-ai.md))
- Sample and re-label a portion independently, to detect drift in how guidelines are applied
- Where labels are model-generated, state which model and validate against human labels on a sample ([synthetic data](synthetic-data.md))
- **Investigate quality problems upstream before tuning the model** — the research finding is that cascades originate in data and are diagnosed late

**Key accountability owner:** whoever owns the dataset or benchmark — because the labeling guideline is where the organization's definition of "correct" is actually written, and it is usually authored by whoever had the task rather than by whoever owns the consequence.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanics of labeling are uncontroversial, and the central empirical claim comes from peer-reviewed CHI research with a stated method — interviews with AI practitioners working on high-stakes applications. **Two limits on that number.** The 92% figure describes the *studied population*, which was selected for high-stakes AI work across specific regions, and it should be cited as what those practitioners reported rather than as an industry rate. And the study predates the current preference-labeling and model-generated-label era, so its cultural finding transfers more confidently than its specifics. **The labor-conditions claims are reported widely and credibly but unevenly evidenced**, which is why this entry states them as structural facts about how the work is organized rather than quantifying them.

---

## Related concepts

- [Training Data](training-data.md) — the corpus labeling produces the targets for
- [Data Quality](data-quality.md) — the property cascades degrade
- [Evaluation (AI Systems)](evaluation.md) — where labeled reference sets set the ceiling
- [AI Benchmarking](ai-benchmarking.md) — published scores resting on someone's judgment calls
- [Bias (AI Systems)](bias-ai-systems.md) — guidelines and labeler pools as a bias source
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — preference comparison as the modern labeling task
- [LLM-as-Judge](llm-as-judge.md) — relocating the judgment to a model
- [Synthetic Data](synthetic-data.md) — generated labels and inherited bias
- [Data Provenance / Lineage](data-provenance-lineage.md) — the record that makes guidelines traceable
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — labeling as outsourced work you do not see

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-308 | Sambasivan, Nithya; Kapania, Shivani; Highfill, Hannah; Akrong, Diana; Paritosh, Praveen; Aroyo, Lora M. (Google Research) — *"Everyone wants to do the model work, not the data work": Data Cascades in High-Stakes AI* (CHI, 2021) · [link](https://doi.org/10.1145/3411764.3445518) | The empirical core: **data cascades affecting 92% of the AI practitioners interviewed**, described as opaque in diagnosis with no clear indicators, and traced to a culture that rewards model work over data work. The title itself is the mechanism this entry names. ⚠️ 92% describes the studied population — practitioners working on high-stakes AI in specific regions — not an industry rate. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | Establishes preference comparison by a specific labeler pool following specific guidelines as the modern form of the labeling task — which is what connects this entry to how current models are shaped. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Standards grounding for label noise and unrepresentative annotation as named sources of statistical bias, rather than as incidental data problems. |
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | The disclosure surface where labeling provenance would belong — and, by its absence in practice, evidence for this entry's point that labor conditions appear in no model documentation. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Publish inter-annotator agreement with every accuracy figure. Investigate quality problems upstream before tuning the model. |
| **Organizational** | The labeling guideline is where your definition of "correct" is written, usually by whoever had the task rather than whoever owns the consequence. |
| **Client-facing** | Explains why data preparation dominates timelines, and why "we'll just label it" is rarely a small ask. |
| **LLM-native** | Preference comparison is labeling. Model-generated labels move the judgment to a model and inherit its biases wholesale. |

---

*Last updated: v1.0 · September 2026*
