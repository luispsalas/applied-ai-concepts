<!--meta
category: Foundations
short: Text, images, audio and video in one system — every text risk carried across, with weaker tooling to detect it
aliases: [vision language model, image and text AI, VLM, AI that sees, cross-modal]
tags: [Architecture, Security]
established: established
-->
# Multimodal AI

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
AI systems that process and generate across multiple types of input and output — text, images, audio, video — rather than being limited to one modality.

---

## Technical definition

Systems that take in and produce more than one kind of data. A model that reads a chart and answers a question about it, transcribes and reasons over speech, describes an image, or generates video from a text description.

**The enabling idea is a shared representation space.** The result that made this practical showed that *"the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn"* visual representations — trained on 400 million internet image-text pairs with **no labeled dataset.** Once images and text are embedded in a comparable space, operations that cross modalities become possible. Every later multimodal system builds on that principle.

**The governance consequence follows directly, and it is what earns this entry a place in a governance corpus:** every property this wiki documents for text — [hallucination](hallucination.md), [bias](bias-ai-systems.md), [prompt injection](prompt-injection.md), [training-data](training-data.md) opacity, [confidence uncoupled from accuracy](confidence-vs-accuracy.md) — **applies to each additional modality, with less mature tooling for detecting it.** Adding a modality does not add one risk; it multiplies an existing set across a surface with weaker instrumentation.

Three specifics worth stating:

- **Prompt injection now arrives through images, audio and documents.** Instructions embedded in a picture, a slide, or a scanned PDF enter the same undifferentiated [context](context-ai-systems.md) stream as text. The attack surface widens with each input type accepted, and image-borne injection is far less commonly filtered than text-borne.
- **Evaluation is markedly weaker.** Text benchmarks are contested but numerous; cross-modal evaluation is thinner, and "the model described the image well" is much harder to measure than answer accuracy.
- **Modality-specific bias compounds.** Vision systems carry documented demographic performance disparities, and speech recognition carries documented accent and dialect disparities. A multimodal pipeline inherits both, and an aggregate metric conceals both.

**A note on vocabulary.** *Multimodal* describes the input/output surface, not the architecture, and covers systems built very differently — a unified model, or a text model orchestrating separate vision and speech components. That matters for governance because **the components may have separate providers, separate training data and separate limitations, none of which a single model card describes.**

---

## Plain-language version

Early AI assistants only handled text. Now most handle images, audio and video too — you can show one a photograph, a chart or a scanned document and ask about it, or ask it to make a picture.

The trick that made this work is simpler than it sounds: train a system on hundreds of millions of images paired with their captions, and it learns to place pictures and words in the same conceptual space. After that, going between them becomes possible.

The important thing for anyone governing this is what it *doesn't* change. Every existing problem — making things up, inheriting bias, sounding equally confident whether right or wrong — applies just as much to images and audio. And the tools for spotting those problems in text, imperfect as they are, are considerably better developed than the equivalents for other formats.

One risk deserves specific mention. Hidden instructions can be embedded in an image or a document, and a system that reads them may follow them. Most organizations filter text for this and do not filter images.

---

## AI literacy notes

1. **Every text limitation carries over.** Hallucination, bias, misplaced confidence, opacity about training data. A confident description of an image is exactly as unreliable as a confident paragraph.
2. **Detection tooling is weaker outside text.** Not because the problems are smaller, but because the instruments are less mature. Assume you can see less, not that there is less to see.
3. **Images and documents are an injection channel.** Instructions hidden in a picture or a scanned file enter the same stream as your instructions, and image-borne injection is much less commonly filtered.
4. **Bias arrives per modality and compounds.** Vision systems have documented demographic disparities; speech systems have documented accent and dialect disparities. A pipeline using both inherits both.
5. **"Multimodal" describes the surface, not the build.** It may be one model or several stitched together, with different providers, training data and limitations — and one model card will not tell you which.
6. **Evaluation is genuinely harder.** There is no clean equivalent of answer accuracy for "did it describe this image well?", so quality claims outside text deserve more scrutiny.
7. **The training data problem is worse, not better.** Web-scraped image-text pairs carry the same licensing and composition opacity as text corpora, plus likeness and consent questions that text does not raise.

---

## Governance notes

**Core question:** For every input type this system accepts, does the control you built for text also exist — and how would you know it was working?

**Watch for:**
- Content filtering, injection defenses and logging built for text and never extended to images, audio or uploaded documents
- Document and image upload enabled as a convenience feature, without recognizing it as a new untrusted input channel ([prompt injection](prompt-injection.md))
- Bias assessed on text output only, when vision and speech components carry their own documented disparities
- One model card treated as covering a pipeline assembled from several providers' components ([model card](model-card-system-card.md))
- Evaluation carried over from text benchmarks, which do not measure cross-modal quality
- Image, audio and video inputs not captured in the [audit trail](audit-trail-ai.md), so a run cannot be reconstructed
- Personal data entering through images and voice — faces, documents, recordings — outside the data inventory built for text ([privacy](privacy-ai-systems.md))

**Practice:**
- Enumerate accepted input types explicitly and check each against the controls you built for text; the gap list is usually longer than expected
- **Treat every non-text input as untrusted and potentially instruction-bearing**, since it enters the same context stream
- Evaluate per modality rather than in aggregate, and disaggregate by group for vision and speech specifically
- Document the pipeline's components and their providers, since no single card covers an assembled system
- Extend logging to non-text inputs at sufficient fidelity to reconstruct a run
- Bring images, audio and documents into the data inventory and retention policy on the same footing as text
- Re-run [FRIA](fundamental-rights-impact-assessment.md) or impact assessment when a modality is added — it is a change of exposure, not a feature toggle

**Key accountability owner:** the system owner, with the specific duty of confirming that **each accepted modality is covered by the controls designed for text** — because the failure mode here is not a missing control, it is a control that exists and silently covers only one input type.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, medium on the governance specifics.** The shared-representation paradigm is peer-reviewed, foundational and uncontested. **The transfer-of-risk argument is reasoning by extension rather than a body of measurement** — that text failure modes recur across modalities is well supported in principle and consistent with practitioner reports, but there is no equivalent to the text literature quantifying it. Cross-modal evaluation is an acknowledged open problem. And **the underlying result is 2021**: current multimodal systems are architecturally different and far more capable, so this entry is deliberately written about the paradigm and its consequences rather than about any current model's capabilities.

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — the text-only starting point this extends
- [Context (AI Systems)](context-ai-systems.md) — where all modalities arrive as one undifferentiated stream
- [Prompt Injection](prompt-injection.md) — the attack surface that widens with every accepted input type
- [Training Data](training-data.md) — image-text corpora carrying the same opacity plus likeness and consent questions
- [Bias (AI Systems)](bias-ai-systems.md) — modality-specific disparities that compound in a pipeline
- [Evaluation (AI Systems)](evaluation.md) — markedly less mature outside text
- [Synthetic Media (Deepfakes)](synthetic-media-deepfakes.md) — what cross-modal generation makes cheap
- [Content Provenance & Watermarking (C2PA)](content-provenance-watermarking.md) — marking obligations that apply across audio, image, video and text
- [Model Card / System Card](model-card-system-card.md) — why an assembled pipeline needs a system card
- [Privacy (AI Systems)](privacy-ai-systems.md) — faces, voices and documents as personal data entering by a new door
- [Data Provenance / Lineage](data-provenance-lineage.md) — provenance for non-text corpora
- [Types of AI Systems](types-of-ai-systems.md) — where modality sits as a classification axis
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the controls that need extending per modality

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-213 | Radford, A.; Kim, J.W.; Hallacy, C.; Ramesh, A.; Goh, G.; Agarwal, S. et al. (OpenAI) — *Learning Transferable Visual Models From Natural Language Supervision (CLIP)* (ICML, 2021) · [link](https://arxiv.org/abs/2103.00020) | The enabling paradigm: caption-matching over 400M web image-text pairs producing a shared representation space, with strong zero-shot transfer and no labeled dataset. ⚠️ Vendor-authored, peer-reviewed; cited for the paradigm, not as a description of current models. |
| SRC-143 | Bommasani, R. et al. (Stanford CRFM / HAI) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | Multimodality within the foundation-model frame, and the homogenization argument for why one model's properties propagate across every downstream modality. |
| SRC-146 | Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. — *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023) · [link](https://arxiv.org/abs/2302.12173) | That content entering as data can act as instruction — the mechanism that makes every additional input type an attack surface. |
| SRC-202 | Dodge, J.; Sap, M.; Marasović, A. et al. — *Documenting Large Webtext Corpora* (EMNLP, 2021) · [link](https://arxiv.org/abs/2104.08758) | The corpus-composition and filtering-bias problems that carry over to web-scraped image-text data. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Why per-modality, disaggregated assessment is required rather than an aggregate figure across a pipeline. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Where multimodal extension sits in the model lifecycle and the vocabulary used consistently across this wiki. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Enumerate accepted input types and check each against the controls built for text. Image-borne injection is the most commonly missed — most filtering stops at text. |
| **Organizational** | Adding a modality is a change of exposure, not a feature toggle. It multiplies existing risks across a surface with weaker instrumentation, and warrants re-running the impact assessment. |
| **Client-facing** | Explains why a system that accepts documents and images needs its controls reviewed again, even though the underlying model is the same one already approved. |
| **LLM-native** | "Multimodal" describes the surface, not the architecture — an assembled pipeline may span several providers with separate training data and limitations that no single model card covers. |

---

*Last updated: v1.0 · August 2026*
