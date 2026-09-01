<!--meta
category: Observability & Governance
short: The transparency artifact — a scoping document whose job is to say where *not* to use a model
aliases: [model card, system card, model documentation, what does this model do, transparency artifact]
-->
# Model Card / System Card

## One-line essence
A standardized document describing a model's capabilities, limitations, training data, and evaluation results — the transparency artifact regulators and users increasingly expect before trusting a system.

---

## Technical definition

A structured disclosure accompanying a released model. The originating proposal frames the purpose precisely, and the framing is more useful than any template: model cards exist to *"clarify the intended use cases of machine learning models and minimize their usage in contexts for which they are not well suited."* **It is a scoping instrument, not a spec sheet** — its job is to tell you where *not* to use something.

**The requirement that makes it do governance work is disaggregated evaluation.** Not a single headline accuracy figure, but performance reported across *"different cultural, demographic, or phenotypic groups"* and intersectional groups. An aggregate number conceals exactly the failures a card exists to surface: a model at 94% overall can be at 71% for one group, and only the disaggregated report shows it. **A card without disaggregation is a marketing document with sections.**

**Model card versus system card.** A *model card* documents the model — capabilities, evaluations, limitations, training data. A *system card* documents the deployed system: the model plus its [guardrails](guardrails-ai-systems.md), retrieval layer, [tools](tool-use.md), [system prompt](system-prompt.md), and human oversight. The distinction matters because **you deploy systems, not models** — the model card describes a component, and most of what determines behavior in production sits outside it.

**Where it sits in the documentation family.** Datasheets — covered under [Data Provenance / Lineage](data-provenance-lineage.md) — document the *dataset*; model cards document the *model*; system cards document the *deployment*. Same lineage — the same authors are on both foundational papers — and the same underlying argument: a component released without documented operating characteristics puts the burden of discovering them on whoever uses it.

**Increasingly a duty rather than a courtesy.** The EU AI Act requires technical documentation for high-risk systems and a sufficiently detailed summary of training content from general-purpose model providers. The card is the recognized shape that documentation has converged on — but note what regulation obliges is *documentation*, not specifically a model card, and the two are not automatically the same artifact.

---

## Plain-language version

When a company releases an AI model, a model card is the document that says what it does, how well, on what, and where it should not be used.

The idea came from electronics: a component ships with a datasheet giving its operating range and test results, so an engineer can tell whether it suits the job. A model card is that, for a model — and the most valuable part is the same part. It is the limits section, not the capabilities section.

The single feature that separates a real card from a brochure is whether performance is broken down by group. "94% accurate" can hide being much worse for one set of people, and only a card that reports the breakdown will show you.

There is also a distinction worth holding onto. A model card describes the model. A *system card* describes what you actually deploy — the model plus the filters, the retrieval, the instructions, the human review. You never deploy a bare model, so the model card is only ever part of the picture.

---

## AI literacy notes

1. **It is a scoping document.** Its stated purpose is to *reduce* use in contexts a model is not suited to. If it reads as promotional, it is not doing its job.
2. **Read the limitations first.** They are the section with information you cannot get anywhere else. Capabilities are discoverable by testing; limits usually are not.
3. **Disaggregation is the test of seriousness.** Aggregate metrics only, and the card is hiding the thing it exists to reveal — whether or not anyone intended that.
4. **A card is a claim, not a certification.** Self-published, self-evaluated, with no conformance test. It tells you what the provider chose to disclose and measure.
5. **Model card ≠ system card.** You deploy the system. Guardrails, retrieval, prompts and oversight determine most production behavior and appear in neither the model's card nor its benchmarks.
6. **Absence is information.** A missing section — training data composition, evaluation on your population, known failure modes — tells you something, and "not disclosed" should be recorded as a finding rather than skipped over.
7. **You may need to write one.** If you fine-tune, adapt, or assemble a system, you have created something whose operating characteristics nobody has documented, and the burden has moved to you.

---

## Governance notes

**Core question:** For each model in use, does a card exist, does it report disaggregated results, and does anything document the *system* you actually deployed?

**Watch for:**
- A card's existence accepted as evidence of diligence, without anyone reading the limitations
- Aggregate-only metrics, which conceal precisely the disparities the format was designed to expose
- Provider evaluation populations that do not resemble your users, treated as transferable
- No system card for internally assembled systems — the model is documented and the deployment is not
- Fine-tuned and adapted models inheriting the base model's card, which no longer describes them
- Cards treated as launch artifacts and never revised, while the model behind an API changes (see Model Version & Update, and [model/data drift](model-data-drift.md))
- Regulatory technical documentation and a model card treated as the same deliverable when the obligation may require more

**Practice:**
- Make card review a gate in model selection, with the limitations section read and its gaps recorded — including "not disclosed," which is a finding
- **Write a system card for anything you assemble**, covering the components the model card cannot: guardrails, retrieval scope, prompts, tools, oversight, and known failure modes in *your* context
- Re-evaluate on your own population rather than accepting the provider's disaggregation as covering your users
- Version the card with the system, and set a re-issue trigger on material change — a card that describes an earlier version is worse than none, because it is trusted
- Where you fine-tune, document the adaptation set and re-run the evaluations that the base card reports
- Check the card against your regulatory documentation duty rather than assuming it satisfies it

**Key accountability owner:** whoever owns the deployed system — because the artifact that matters for governance is the *system* card, and no provider will write it for you.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The format, its purpose and the disaggregation requirement are peer-reviewed and the pattern is now embedded in regulation and platform norms. **The weakness is enforcement, and it is structural:** cards are self-published, self-evaluated and voluntary in most jurisdictions, with no conformance test and no independent verification — so quality varies enormously and a card's presence says little on its own. **System card practice is markedly less mature than model card practice**; there is no established template for documenting an assembled deployment, and the guidance above is a reasoned extension of the model-card argument rather than a settled standard.

---

## Related concepts

- [Data Provenance / Lineage](data-provenance-lineage.md) — datasheets are the dataset-level ancestor, from the same authorship lineage
- [Training Data](training-data.md) — the section most often thin or absent
- [Evaluation (AI Systems)](evaluation.md) — the results a card reports, and why yours still need running
- [Bias (AI Systems)](bias-ai-systems.md) — what disaggregated reporting exists to surface
- [Explainability (XAI)](explainability-xai.md) — documentation transparency, distinct from output-level interpretability
- [Compliance (AI Systems)](compliance-ai-systems.md) — where technical documentation duties are demonstrated
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — part of the system, absent from the model card
- [AI Use Case](ai-use-case.md) — the scoping question a card is meant to inform
- [Operational Readiness (AI)](operational-readiness-ai.md) — a system card is part of what "documented" means at go-live
- [Model/Data Drift](model-data-drift.md) — why a card needs a re-issue trigger
- [Accountability (AI Systems)](accountability-ai-systems.md) — a card names what was claimed, and by whom
- [Frontier AI (Frontier Model)](frontier-ai.md) — where system cards are most developed in practice, and most scrutinized
- [AI Disclosure (Attribution)](ai-disclosure-attribution.md) — the adjacent question of disclosing AI use in output rather than model properties

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | The format, its stated purpose as a scoping instrument, and the disaggregated-evaluation requirement that separates a working card from a brochure. ⚠️ `dl.acm.org` blocks automated clients; the DOI is live. |
| SRC-199 | Gebru, T.; Morgenstern, J.; Vecchione, B.; Wortman Vaughan, J.; Wallach, H.; Daumé III, H.; Crawford, K. — *Datasheets for Datasets* (CACM 64(12), 2021) · [link](https://doi.org/10.1145/3458723) | The dataset-level ancestor and the component-datasheet analogy the whole documentation family rests on. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Technical documentation duties for high-risk systems and the training-content summary required of general-purpose model providers. |
| SRC-065 | Liang, P. et al. (Stanford CRFM) — *Holistic Evaluation of Language Models (HELM)* (TMLR, 2023) · [link](https://arxiv.org/abs/2211.09110) | Multi-metric, multi-scenario reporting as the evaluation practice a card should be summarizing. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Why aggregate metrics conceal group-level disparity, and what documenting it properly requires. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places documentation inside the map and govern functions rather than treating it as a release formality. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Read limitations first; check for disaggregation; write a system card for anything you assemble, since no provider documents your guardrails, retrieval and prompts. |
| **Organizational** | A card is a self-published claim, not a certification. Its presence is not diligence — reading it and recording its gaps, including "not disclosed," is. |
| **Client-facing** | Explains what documentation to ask a vendor for and what a good answer looks like: the limits section and per-group results, not the headline number. |
| **LLM-native** | Model card describes a component; you deploy a system. Most production behavior comes from the layer neither the card nor the benchmarks cover. |

---

*Last updated: v1.0 · August 2026*
