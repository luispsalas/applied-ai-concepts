<!--meta
category: Knowledge & Memory
short: Where the data came from and what has happened to it since — the record that answers "can we actually use this?"
aliases: [data lineage, provenance, dataset provenance, data origin, where did this data come from]
tags: [Data Governance, Regulatory]
-->
# Data Provenance / Lineage

## One-line essence
The traceable history of where data came from, how it was transformed, and what it has touched — the record that makes it possible to answer "can we actually use this?" for training or retrieval data.

---

## Technical definition

Two related records, often used interchangeably and worth separating:

- **Provenance** — where a dataset *originated*: who produced it, under what license or lawful basis, collected for what original purpose, with what consent.
- **Lineage** — what has *happened to it since*: which transformations, joins, filters and enrichments produced the version in front of you, and which downstream systems consume it.

Provenance answers *may we use this*. Lineage answers *what is this, and what breaks if it changes*. An AI system needs both, at two distinct points: the data a model or index was **built from**, and the data a running system **retrieves** at inference time.

**Why one entry, given they answer different questions.** Because they are *governed* as one practice, even though they are *understood* as two. EU AI Act Art. 10 places origin and transformation history inside a single obligation, discharged by a single record and audited together — and in practice both are captured or lost at the same moment, when data enters the pipeline. Splitting them would let a reader satisfy half a duty with no signal that the other half belonged to it. **Keep the distinction when reasoning; keep the record whole.**

**In the EU this is now a legal duty rather than a maturity practice.** Article 10 of the AI Act requires training, validation and testing data sets for high-risk systems to be subject to governance practices covering, in the regulation's own words, *"data collection processes and the origin of data, and in the case of personal data, the original purpose of the data collection"* — origin named explicitly — along with annotation, labelling, cleaning, updating, enrichment and aggregation, examination for biases likely to affect health, safety or fundamental rights, measures to mitigate those biases, and identification of data gaps. Art. 10(3) requires the data to be *"relevant, sufficiently representative, and to the best extent possible, free of errors and complete."*

**The state of practice is worse than most teams assume.** A systematic audit of over 1,800 widely used text datasets traced their lineage and licensing and found **license omission above 70% and error rates above 50%** on major hosting platforms — the authors describe it as a crisis in misattribution and informed use. The pattern is structural: datasets get aggregated, re-packaged and re-hosted, and provenance is lost at each hop, not maliciously but because nothing carries it forward.

**The documentation pattern predates the regulation.** *Datasheets for Datasets* proposed, by analogy with electronic components shipping operating characteristics and test results, that every dataset carry a record of its motivation, composition, collection process and recommended uses. [Model cards](model-card-system-card.md) and the AI Act's Art. 10 duties both descend from it.

**Where AI changes the classic data-governance problem.** Lineage is a mature discipline in data management, but AI adds three things it was not designed for: **training data is absorbed rather than referenced**, so a model cannot be un-trained on a record that must be deleted; **retrieval at inference time** means the data reaching a user is selected per request, so scope is decided at runtime; and **model weights are themselves a derived data asset** whose lineage almost nobody tracks.

---

## Plain-language version

Two questions, and most organizations can answer neither for the data behind their AI systems.

*Where did this come from?* Who made it, were we allowed to use it, and was it collected for something else entirely. *What has happened to it since?* Which cleaning, merging and filtering steps produced the version being used, and what else depends on it.

These sound like bookkeeping and they are not. They are what lets you answer whether you may legally use a dataset, whether a discovered problem affects one system or nine, and what actually needs redoing when a source turns out to be wrong. Without them, every question of that kind becomes an investigation.

The uncomfortable part is that provenance degrades by default. Data gets copied, combined and re-published, and the origin drops off at each step — an audit of the most widely used public datasets found license information missing or wrong more often than not. And AI makes it harder: once a model has trained on something, you cannot simply remove that record the way you would delete a row.

---

## AI literacy notes

1. **Provenance and lineage answer different questions.** *May we use it* versus *what is it and what depends on it*. Teams often build lineage tooling and still cannot answer the licensing question.
2. **The default is decay.** Nothing carries origin forward automatically through copying, aggregation and re-hosting. Provenance has to be actively preserved or it is simply lost.
3. **Public and popular is not the same as cleared.** The most-used datasets are among the worst documented; a majority of license fields on major platforms are missing or wrong.
4. **Training absorbs; retrieval references.** You can remove a document from an index. You cannot remove it from weights — which is why the provenance check belongs *before* training, not after.
5. **Two checkpoints, not one.** What the system was built from, and what it retrieves at runtime. A clean training set says nothing about what a retrieval layer can reach today.
6. **Model weights are a derived asset.** They have their own lineage — base model, fine-tuning data, adaptation steps — and it is almost never recorded.
7. **"Publicly available" is not a lawful basis.** Accessibility and permission are different questions, and personal data collected for one purpose does not become usable for another because it was reachable.

---

## Governance notes

**Core question:** For each dataset behind an AI system, can you state its origin, your basis for using it, and what would need redoing if it turned out to be wrong?

**Watch for:**
- Datasets adopted from aggregators with no origin record, on the assumption that popularity implies clearance
- Provenance tracked for training data but not for the retrieval corpus, where scope is decided at request time and grows quietly
- No lineage from a source to its downstream consumers, so the blast radius of a bad source is unknown when one is found
- Fine-tuned or adapted models with no record of what they were adapted on — the most common lineage gap in practice
- Deletion and subject-rights requests handled at the storage layer only, with no path for data already absorbed into weights or an index
- License and lawful basis recorded once at intake and never re-checked as terms change

**Practice:**
- Record origin at intake, before the data enters any pipeline — retrofitting provenance is far more expensive than capturing it, and often impossible
- Keep a dataset record covering motivation, composition, collection process, license and recommended uses; the datasheet pattern is a usable template and predates the regulation
- Maintain lineage in both directions: source → systems, and system → sources. The second is what you need during an incident
- Treat the retrieval corpus as a governed dataset with the same intake discipline as training data
- Version the model as a derived asset: base, adaptation data, date, and the evaluation it passed
- Check provenance *before* training or indexing, since that is the last point at which it is cheap to act on

**Key accountability owner:** the data owner for each source, with the AI system owner accountable for the *composite* — the assembled training set or retrieval corpus is itself an asset that needs an owner, and it usually has none.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** Unusually well anchored: the obligation is binding law with quotable clause text, the documentation pattern is peer-reviewed and long-established, and the state-of-practice finding is a large systematic audit rather than an impression. Two caveats. The audit's specific rates describe 2023-era platforms and should be re-checked before being quoted as current, though the structural finding — aggregation loses provenance — is not in question. And **the hard case has no settled answer**: there is no reliable method for removing a specific record's influence from trained weights, so provenance failures found after training are currently remedied by retraining or by accepting the exposure.

---

## Related concepts

- [Data Quality](data-quality.md) — provenance is what lets you judge fitness rather than assume it
- [Training Data](training-data.md) — what the model absorbed, and where its gaps and biases originate
- [Knowledge Base](knowledge-base.md) — the retrieval corpus is a governed dataset, with the same intake duties
- [Retrieval-Augmented Generation (RAG)](rag.md) — where runtime data scope is decided per request
- [Privacy (AI Systems)](privacy-ai-systems.md) — original collection purpose and lawful basis are provenance fields
- [Data Minimization](data-minimization.md) — the decision provenance makes possible: knowing what you have, you can justify keeping less
- [Bias (AI Systems)](bias-ai-systems.md) — Art. 10 requires examination for bias as part of data governance, not as a separate exercise
- [Compliance (AI Systems)](compliance-ai-systems.md) — where Art. 10 obligations are demonstrated
- [Audit Trail (AI)](audit-trail-ai.md) — the runtime counterpart: what the system did, alongside what it was built from
- [Ownership (AI Systems)](ownership-ai-systems.md) — the assembled corpus needs an owner, and usually lacks one
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — why absorbed data is not recoverable, and can resurface
- [Model/Data Drift](model-data-drift.md) — lineage is what tells you which systems a changed source affects
- [Model Card / System Card](model-card-system-card.md) — the model-level counterpart of a datasheet
- [Copyright & AI Output](copyright-ai-output.md) — the licensing question provenance exists to answer

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-197 | European Parliament / Council of the EU — *EU Artificial Intelligence Act, Article 10: Data and data governance* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding obligation, with origin of data and original collection purpose named explicitly, plus the bias-examination and data-gap duties and the representativeness standard in Art. 10(3). |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative: A Large Scale Audit of Dataset Licensing & Attribution in AI* (2023) · [link](https://arxiv.org/abs/2310.16787) | The measured state of practice across 1,800+ datasets: license omission above 70%, error rates above 50%, and the concentration of closed data in lower-resource categories. |
| SRC-199 | Gebru, T.; Morgenstern, J.; Vecchione, B.; Wortman Vaughan, J.; Wallach, H.; Daumé III, H.; Crawford, K. — *Datasheets for Datasets* (Communications of the ACM 64(12), 2021) · [link](https://doi.org/10.1145/3458723) | The documentation pattern the practice descends from — motivation, composition, collection process, recommended uses — and the component-datasheet analogy that makes it legible. |
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | Lineage as an established data-management discipline, and the vocabulary AI governance inherits rather than invents. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Purpose limitation and lawful basis — why "collected for something else" is a provenance field with legal consequences. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places data documentation inside the map function of a risk lifecycle rather than treating it as pipeline hygiene. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Capture origin at intake — retrofitting is expensive and often impossible. Maintain lineage in both directions, and treat the retrieval corpus with the same discipline as training data. |
| **Organizational** | This is what makes "can we use this?" answerable in minutes rather than as an investigation, and under the EU AI Act it is a documented obligation for high-risk systems, not a maturity goal. |
| **Client-facing** | Explains why data intake carries questions about origin and permission before anything is built, and why that step cannot be done afterwards. |
| **LLM-native** | Training absorbs and retrieval references — the asymmetry that makes the pre-training provenance check the one that counts, since weights cannot be selectively unlearned. |

---

*Last updated: v1.1 · August 2026*
