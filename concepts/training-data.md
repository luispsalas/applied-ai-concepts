<!--meta
category: Knowledge & Memory
short: What the model learned from — where its knowledge, gaps, blind spots and biases all come from, and which is rarely disclosed
aliases: [what was it trained on, training corpus, pretraining data, the data behind the model, where its knowledge comes from]
tags: [Data Governance, Ethics, AI Literacy]
established: established
-->
# Training Data

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The text, images and code a model learned from — where its knowledge, its gaps, its blind spots and its biases all come from, and which is rarely fully disclosed.

---

## Technical definition

The corpus a model's parameters were fit to. For a large language model this is typically web-scraped text at enormous scale, plus books, code, and licensed collections, followed by much smaller curated sets used for instruction tuning and preference optimization. The pre-training corpus determines what the model *knows*; the later stages shape how it *behaves*.

**Training data is absorbed, not referenced.** This is the property everything else follows from. A retrieval system points at documents and can be made to stop pointing at one. Training distributes statistical influence across billions of parameters, and there is no established method for removing a specific record's contribution afterwards. Deletion, correction and licensing problems discovered after training are remedied by retraining or by accepting the exposure.

**What is actually in a web-scale corpus is not what people assume.** The most useful evidence here is a direct audit of C4, a widely used Common Crawl derivative, which found: **machine-generated text** (output of machine translation systems, now training the next model); **evaluation examples from other benchmark datasets**, i.e. benchmark contamination that inflates measured performance; substantial content from unexpected sources including patents and US military websites; and — the finding that should change how people think about data cleaning — **blocklist filtering disproportionately removed text from and about minority individuals.** The cleaning step is itself a source of bias, not a correction for it.

**Disclosure has gone backwards.** Early large models shipped with documented corpora. Current frontier models generally do not disclose composition, and where regulation requires it — the EU AI Act obliges general-purpose model providers to publish a sufficiently detailed summary of training content — the summary is not the corpus. For most models in production use today, **nobody outside the provider can answer what they were trained on.**

**Three things trace directly back here** and are usually discussed as if they were independent: what the model knows and when it stops knowing it ([knowledge cutoff](knowledge-cutoff.md)); which groups, languages and viewpoints it represents well or badly ([bias](bias-ai-systems.md)); and what it can inadvertently reproduce ([data leakage](data-leakage-ai-systems.md)).

---

## Plain-language version

A model does not consult its training data when answering you. It was shaped by it, once, and the data is gone — what remains is a set of numbers that encode patterns from it.

That has an uncomfortable consequence. Everything the model is good at, everything it is bad at, everything it is skewed about, and everything it might accidentally repeat all originate in material you almost certainly cannot inspect. Most frontier providers no longer disclose what they trained on.

When people *have* looked carefully at a large web corpus, the contents were not what anyone expected: text machine-translated by earlier software, test questions from the very benchmarks used to grade models, patent filings, military websites. And the filtering meant to clean it up removed disproportionately more writing by and about minority groups — so the tidying introduced its own skew.

None of this makes the models unusable. It means that when a model is unreliable about something, "what was it trained on?" is usually the right question, and usually unanswerable.

---

## AI literacy notes

1. **The model does not look anything up.** It has no copy of its training data at answer time. It has patterns learned from it — which is why it can be confidently wrong about something it "saw."
2. **Absorbed, not referenced.** You cannot remove a document from a trained model the way you remove one from a folder. That asymmetry drives most of the governance consequences.
3. **Cleaning is not neutral.** Blocklist filtering measurably removed more text from and about minority individuals. Every filtering decision is an editorial decision about whose language survives.
4. **Benchmark contamination is real and inflates scores.** Test examples turn up inside training corpora, so some measured performance is partly recall. Treat headline benchmark numbers accordingly.
5. **Models are increasingly trained on model output.** Machine-generated text was already present in 2021-era corpora, and far more of the web is synthetic now. What that does over successive generations is an open question, not a solved one.
6. **You usually cannot check.** Composition is undisclosed for most production models, and a regulatory summary is not an inventory. Design as if the answer is unavailable, because it generally is.
7. **"Trained on public data" is not a permission claim.** Reachable and licensed are different, and the licensing of large public corpora is frequently unclear or wrong — see [Data Provenance / Lineage](data-provenance-lineage.md).

---

## Governance notes

**Core question:** For each model you rely on, what do you actually know about its training data — and which of your risks depend on an answer you do not have?

**Watch for:**
- Model selection made on capability benchmarks alone, with no question asked about corpus composition or disclosure
- Bias controls designed as output filters, when the origin is upstream and the filter only catches what it was told to look for
- Benchmark performance treated as evidence of capability without accounting for contamination
- [Fine-tuning](fine-tuning.md) or adaptation performed with no record of what was used — the most common training-data gap inside an organization, and the one you actually control
- Subject-rights and deletion processes that stop at storage, with no position on data already absorbed into weights
- "Publicly available" used as a licensing answer

**Practice:**
- Record what is knowable per model — disclosed composition, published summary, cutoff date, provider terms — and record explicitly where the answer is *unavailable*, since that is a risk register entry rather than a blank
- Own the part you control absolutely: every fine-tuning and adaptation set documented at intake, with license and origin ([data provenance](data-provenance-lineage.md))
- Do the provenance check *before* training, since it is the last point at which it is cheap to act on
- Evaluate on your own data rather than trusting published benchmarks, which may be contaminated ([evaluation](evaluation.md))
- Treat corpus-derived bias as requiring measurement in your context, not as something the provider handled
- Where a deletion obligation could reach absorbed data, get a legal position in advance rather than at the point of a request

**Key accountability owner:** for third-party models, whoever owns model selection — because "we do not know what it was trained on" is a decision to accept a risk, and it should be made by someone with authority to accept it. For internal fine-tuning, the data owner, with the same duties as any training set.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, low on the specifics of any current model.** That models are shaped by their corpora, that influence cannot be selectively removed, and that filtering introduces its own bias are all well established — the last from a direct peer-reviewed audit. **The unavoidable limitation is that the audit evidence is about corpora that are now dated**, principally C4, because those are the ones that could be examined. Frontier training data is undisclosed, so claims about what current models were trained on are inference. Treat the structural findings as transferable and any specific composition claim as unverifiable unless the provider published it.

---

## Related concepts

- [Data Provenance / Lineage](data-provenance-lineage.md) — origin and licensing of the corpus; the check that has to happen before training
- [Knowledge Cutoff](knowledge-cutoff.md) — the temporal boundary the corpus imposes
- [Bias (AI Systems)](bias-ai-systems.md) — where it originates, and why output filtering addresses the symptom
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — absorbed content resurfacing in output
- [Large Language Models (LLMs)](large-language-models.md) — how a corpus becomes a model
- [Hallucination](hallucination.md) — what happens in the gaps the corpus left
- [Evaluation (AI Systems)](evaluation.md) — contamination is why published benchmarks need your own data alongside them
- [Data Quality](data-quality.md) — fitness for purpose, applied at corpus scale
- [Model Card / System Card](model-card-system-card.md) — the artifact where composition is meant to be disclosed
- [Privacy (AI Systems)](privacy-ai-systems.md) — personal data absorbed rather than stored
- [Local LLMs](local-llms.md) — open weights do not imply open or licensed training data
- Synthetic Data — increasingly part of the corpus, with its own quality and feedback questions
- [Copyright & AI Output](copyright-ai-output.md) — the licensing question the corpus raises and does not answer
- [Pre-training](pre-training.md) — the stage at which the corpus does its work

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-202 | Dodge, J.; Sap, M.; Marasović, A.; Agnew, W.; Ilharco, G.; Groeneveld, D.; Mitchell, M.; Gardner, M. — *Documenting Large Webtext Corpora: A Case Study on the Colossal Clean Crawled Corpus* (EMNLP, 2021) · [link](https://arxiv.org/abs/2104.08758) | The direct audit: machine-generated text, benchmark contamination, unexpected sources, and blocklist filtering disproportionately removing text from and about minority individuals. |
| SRC-143 | Bommasani, R. et al. (Stanford CRFM / HAI) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | Why corpus properties propagate to every downstream application built on the model — the homogenization argument. |
| SRC-150 | Carlini, N.; Tramer, F.; Wallace, E.; Jagielski, M.; Herbert-Voss, A.; Lee, K.; Roberts, A.; Brown, T.; Song, D.; Erlingsson, U.; Oprea, A.; Raffel, C. — *Extracting Training Data from Large Language Models* (2021) · [link](https://arxiv.org/abs/2012.07805) | That absorbed content can be recovered from a trained model — the evidence behind treating the corpus as a live disclosure surface. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | The licensing reality behind "publicly available": omission above 70% and error rates above 50% across widely used datasets. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | The pre-training/fine-tuning/preference-optimization pipeline and where each stage's data does its work. |
| SRC-197 | European Parliament / Council of the EU — *EU AI Act, Article 10: Data and data governance* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding duties on training data for high-risk systems — origin, preparation, bias examination, representativeness. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Evaluate on your own data — published benchmarks may be contaminated. Document every fine-tuning set at intake; that is the training data you actually control. |
| **Organizational** | "We do not know what it was trained on" is true for most production models and is a risk acceptance, not a blank. It belongs on the register with a named owner. |
| **Client-facing** | Explains why a model's strengths, gaps and biases are inherited rather than designed, and why they cannot simply be configured away. |
| **LLM-native** | Absorbed, not referenced — there is no reliable unlearning, so the provenance check before training is the one that counts. And cleaning is editorial: filtering removed more minority-authored text, not less. |

---

*Last updated: v1.0 · August 2026*
