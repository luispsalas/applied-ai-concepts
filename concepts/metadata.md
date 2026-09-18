<!--meta
category: Knowledge & Memory
short: Data that describes other data — and which AI systems act on without checking, although it strips in transit, is often wrong at source, can stay unchanged while the data changes, and can be written by an attacker
aliases: [data about data, descriptive metadata, structural metadata, metadata schema, file metadata, EXIF, dataset metadata, model metadata, metadata stripping, dataset documentation]
tags: [Data Governance, Security, AI Literacy]
established: established
-->
[Applied AI Concepts](../README.md) › [Knowledge & Memory](../glossary/categories.md#knowledge--memory) › Metadata

# Metadata

> **Term status — Established.** Defined by NIST across several publications and in universal use throughout computing, archives and data management, independent of any vendor.

## One-line essence
Data that describes other data — its origin, format, meaning and permitted use — which AI systems read and act on as though it were reliable, although nothing guarantees that it is.

---

## Technical definition

NIST defines metadata as *"information describing the characteristics of data including, for example, structural metadata describing data structures (e.g., data format, syntax, and semantics) and descriptive metadata describing data contents (e.g., information security labels)"*, and more briefly as *"data about data."* The two kinds matter separately: **structural** metadata tells a system how to read something, **descriptive** metadata tells it what that something is.

**The property that makes metadata a governance topic is simple and routinely forgotten: metadata is a claim about data, stored apart from the data, and nothing forces the two to agree.** Every system that acts on metadata — filters by it, routes by it, trusts it — is acting on the claim, not on the thing. There are four documented ways the claim and the thing come apart.

- **Lost in transit.** Metadata attached to a file does not survive most of what happens to files. The C2PA provenance standard carries a second, content-embedded binding for exactly this reason: an asset *"can become separated from its C2PA Manifest due to removal or corruption of asset metadata."* A screenshot, a re-encode or an upload pipeline removes it silently ([content provenance and watermarking](content-provenance-watermarking.md)).
- **Wrong at source.** An audit of more than 1,800 text datasets on widely used hosting platforms found **license information omitted in over 70% of cases and wrong in over 50%**. The metadata existed, looked authoritative, and was frequently false — and downstream decisions about what a model may be trained on were being made from it ([data provenance and lineage](data-provenance-lineage.md), [training data](training-data.md)).
- **Stale while the data moves.** A descriptor can stay constant across a real change in what it describes. In a medical-imaging study, scans differing only in reconstruction kernel carried identical values in the metadata field naming that kernel, while features computed from the pixels recovered the difference. **A monitor reading the field saw a stable stream that was not stable** ([model and data drift](model-data-drift.md)).
- **Written by an attacker.** When a system *selects* on a description, the description becomes attack surface. In agent skill registries, where discovery runs on a natural-language description, adversarial skills reached up to an **86% pairwise win rate** in retrieval, and description-only framing biased agents toward malicious variants in **77.6% of paired trials** ([agent skills](agent-skills.md), [prompt injection](prompt-injection.md)).

**Signing metadata proves who wrote it — never that it is true.** Cryptographic provenance binds a signed claim to an asset so that tampering is detectable, and the C2PA specification states the limit itself: it should not judge whether a set of provenance data is "good" or "bad," only whether its assertions validate against the asset. **Integrity and attribution are real guarantees; accuracy is not one of them.**

**For AI systems in particular, metadata is where the missing dimensions live.** An embedding space represents meaning and nothing else — recency, authority and reliability have to be added as separate metadata and filters. So a retrieval system's sense of what is *current*, *authoritative* or *permitted* is exactly as good as its metadata, and no better ([embeddings](embeddings.md), [RAG](rag.md)).

**And the documentation that governs AI is itself metadata.** Datasheets for datasets record *"motivation, composition, collection process, recommended uses"*; model cards record intended use and disaggregated evaluation ([model card / system card](model-card-system-card.md)). Both are descriptions of an artifact, and they inherit the same property as every other kind: **they describe the version they were written for, and nothing makes them follow when the artifact changes.**

---

## Plain-language version

Metadata is the label on the box, not what is in the box. It tells you when a photo was taken, what license a dataset carries, what a file contains, what a software tool claims to do.

Computers — and especially AI systems — read labels constantly and open boxes rarely, because labels are small and fast and boxes are big and slow. That is the whole point of metadata, and it works well. But it means the system is trusting the label.

**Labels go wrong in four ordinary ways.** They fall off: screenshot a photo and its credentials are gone. They were written wrong in the first place: when researchers checked the license labels on more than 1,800 public datasets, most were missing and more than half of the ones present were incorrect. They stop matching: the box's contents change and nobody updates the label. And someone writes a misleading label on purpose, because the system chooses what to use by reading labels — so whoever writes the most persuasive label wins.

**A seal on the label doesn't fix this.** A tamper-proof seal tells you nobody changed the label since it was written, and tells you who wrote it. It tells you nothing about whether the label was true.

None of this makes metadata bad. It makes it a claim, and the useful habit is to treat it like one: check the box sometimes, especially when a decision depends on what the label says.

---

## AI literacy notes

1. **Metadata is a claim about data, not the data** — and it is stored separately, so the two can disagree.
2. **It strips easily** — screenshots, re-encoding and upload pipelines remove it without warning.
3. **It is often wrong at source** — license metadata on public datasets was missing or incorrect far more often than not.
4. **It can go stale** — a field can stay constant while the thing it describes changes.
5. **When a system selects by description, the description is an attack surface.**
6. **Signing proves authorship and integrity, never truth.**
7. **Retrieval systems know recency, authority and permission only through metadata.**
8. **Model cards and datasheets are metadata too**, and they drift from the artifact the same way.
9. **Absence of metadata is not evidence** — a stripped label and a label that never existed look identical.

---

## Governance notes

**Core question:** Which decisions in this system are made by reading metadata rather than the data itself — and what happens when that metadata is missing, wrong, stale, or written by someone with an interest in the outcome?

**Watch for:**
- Training, licensing or permission decisions made from dataset metadata that was never checked against the data ([data provenance and lineage](data-provenance-lineage.md))
- Monitoring or drift detection implemented against metadata fields with no check that the fields vary when the data does ([model and data drift](model-data-drift.md))
- Provenance metadata assumed to survive a publication or ingestion pipeline that was never tested for stripping ([content provenance and watermarking](content-provenance-watermarking.md))
- Tool, skill or plugin descriptions treated as documentation when they are what drives selection ([agent skills](agent-skills.md))
- A valid signature read as evidence that the signed content is accurate
- Retrieval filters on recency or authority built on metadata nobody maintains ([RAG](rag.md))
- Model cards and datasheets that describe a previous version of the artifact they ship with ([model card / system card](model-card-system-card.md))
- Metadata that carries more than it should — identifying details in provenance or file records passed downstream unexamined ([privacy](privacy-ai-systems.md))

**Practice:**
- **Inventory where metadata drives a decision**, and for each one name what would happen if it were missing, wrong, stale or adversarial
- **Sample the data behind the metadata** at a cadence proportionate to the decision, rather than treating the descriptor as ground truth ([data quality](data-quality.md))
- **Treat any description that influences selection as untrusted input** and review it as such, not as documentation ([supply chain risk](supply-chain-risk-ai.md))
- Test your own pipelines for stripping — ingestion, conversion and delivery — before relying on metadata surviving them
- **Record what a signature establishes and what it does not**, so integrity is never reported as accuracy
- Version documentation metadata with the artifact, and treat a change to the artifact as a trigger to re-check it
- Treat the absence of expected metadata as a distinct state to handle, never as a default value

**Key accountability owner:** whoever owns the decision that reads the metadata — because metadata is usually produced by someone else, often upstream and out of reach, and the only party positioned to decide how far to trust it is the one about to act on it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the definition and the mechanisms.** The definition is taken directly from NIST's glossary, read live and matched against an archived copy; the stripping limit and the signature limit are both stated in the C2PA specification itself; the datasheet and model-card framing is peer-reviewed; and the license-metadata finding comes from a systematic audit of more than 1,800 datasets. **Three limits.** The drift and attack-surface demonstrations come from **preprints** in specific settings — one clinical imaging pipeline, one skill-registry retrieval setup — so the figures are properties of those studies, cited here for the mechanism rather than as rates that transfer. The dataset-license audit reflects hosting platforms as surveyed in **2023**, and those rates may have moved since. And the privacy point — that metadata can carry identifying detail — is stated structurally, not measured by any source cited here.

---

## Related concepts

- [Data Provenance / Lineage](data-provenance-lineage.md) — the record of where data came from, which is itself metadata
- [Data Quality](data-quality.md) — metadata accuracy as one of its dimensions
- [Content Provenance & Watermarking](content-provenance-watermarking.md) — signed provenance metadata and why it strips
- [Model Card / System Card](model-card-system-card.md) — documentation metadata for models
- [Agent Skills](agent-skills.md) — descriptions as the selection surface and the attack surface
- [Model & Data Drift](model-data-drift.md) — descriptors that stay constant while data changes
- [Embeddings](embeddings.md) — what the vector cannot represent, and metadata must
- [RAG](rag.md) — filtering and ranking on metadata at retrieval time
- [Ontology](ontology.md) — the schema that structural metadata follows
- [Training Data](training-data.md) — where license metadata decides what may be used
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — untrusted third-party descriptions
- [Privacy (AI Systems)](privacy-ai-systems.md) — identifying detail carried in metadata

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-362 | National Institute of Standards and Technology (NIST) — *CSRC Glossary: metadata* · [link](https://csrc.nist.gov/glossary/term/metadata) | The definitional anchor: *"information describing the characteristics of data"*, distinguishing **structural** metadata (format, syntax, semantics) from **descriptive** metadata (contents), sourced there to NIST SP 800-150, with *"data about data"* from SP 800-86. ⚠️ A glossary aggregating definitions from several NIST publications — cited for the definition, not for any practice claim. |
| SRC-205 | Coalition for Content Provenance and Authenticity (C2PA) — *C2PA Technical Specification (Content Credentials) v2.4* (2026) · [link](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) | Two limits stated by the standard itself: soft bindings exist because an asset can become separated from its manifest through removal or corruption of asset metadata, and validation establishes integrity and attribution, never whether the provenance data is "good." ⚠️ A rapidly versioned consortium standard — version cited explicitly. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | The evidence that metadata is often wrong at source: across 1,800+ text datasets on widely used hosting platforms, **license omission above 70% and error rates above 50%**. ⚠️ Platform conditions as surveyed in 2023. |
| SRC-357 | Soliman, Daniel — *Acquisition state behaves as a structured, measurable variable governing lung-nodule AI* (arXiv:2606.12824v2, 2026) · [link](https://arxiv.org/abs/2606.12824) | The stale-descriptor case: a metadata field naming the reconstruction kernel held identical values across genuinely different reconstructions, while pixel features recovered them. ⚠️ Single-author preprint in one clinical setting — cited for the mechanism, not a transferable rate. |
| SRC-269 | Saha, Shoumik; Faghih, Kazem; Feizi, Soheil — *Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry* (2026) · [link](https://arxiv.org/abs/2605.11418) | The adversarial case: where selection runs on a natural-language description, adversarial skills reached up to an 86% pairwise win rate and description-only framing biased agents toward malicious variants in 77.6% of paired trials. ⚠️ Preprint; figures are properties of that retrieval setup. |
| SRC-199 | Gebru, T.; Morgenstern, J.; Vecchione, B.; Wortman Vaughan, J.; Wallach, H.; Daumé III, H.; Crawford, K. — *Datasheets for Datasets* (Communications of the ACM, 2021) · [link](https://doi.org/10.1145/3458723) | Documentation metadata for datasets — motivation, composition, collection process, recommended uses — as the origin of the practice that governs what AI is trained on. |
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | Documentation metadata for models — intended use and disaggregated evaluation — and therefore an instance of metadata that describes the version it was written for. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Inventory the decisions driven by metadata, sample the data behind them, test your pipelines for stripping, and treat selection-driving descriptions as untrusted input. |
| **Organizational** | A signature proves who wrote a label, not that it is true — and dataset license labels were wrong more often than they were right. Decisions resting on metadata need an owner who checks. |
| **Client-facing** | Explains why "the file says it was made by a camera" or "the dataset is labeled as licensed" is a claim to verify, not a fact. |
| **LLM-native** | Metadata is a separately stored claim about data. It strips, it is wrong at source, it goes stale, and when it drives selection it is attack surface. Signing guarantees integrity, not accuracy. |

---

*Last updated: v1.0 · September 2026*
