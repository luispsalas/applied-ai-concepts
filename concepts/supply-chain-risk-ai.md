<!--meta
category: Observability & Governance
short: Everything in your AI system that you did not build and cannot inspect — and the point at which the law stops treating you as a user and starts treating you as the maker
aliases: [supply chain risk, AI supply chain, model provenance, third-party model risk, upstream risk, AI BOM, where did this model come from]
tags: [Security, Regulatory, Data Governance]
established: established
-->
# Supply Chain Risk (AI)

> **Term status — Established.** Supply-chain risk management is a defined discipline with its own NIST standard; the AI-specific form is in independent use across regulators, standards bodies and security research.

## One-line essence
The risk an organization inherits from the models, weights, datasets, and packages it did not build and usually cannot inspect.

---

## Technical definition

An AI system is assembled far more than it is built. A typical deployment inherits a **base model** trained by someone else on data nobody outside the provider can enumerate, **weights** downloaded from a hub, **datasets** of uncertain provenance, an **orchestration framework**, and a long tail of packages — plus, increasingly, **agent-facing artifacts** like tool definitions and skill files that carry instructions rather than only code.

**Conventional supply-chain practice applies, and stops short.** NIST's C-SCRM standard covers supplier assessment, provenance and integrity for systems generally, and the discipline transfers. What it was not designed for is an artifact whose behavior is not readable from its contents: **you can verify a model file's hash and still have no idea what the model will do**, because the properties that matter were determined by training data and process you cannot see ([training data](training-data.md), [black box](black-box.md)).

**Two AI-specific attack surfaces have no traditional analogue.** [Data poisoning](training-data.md) corrupts behavior through the training corpus rather than the code path. And **artifacts that are instructions rather than executables** — skill files, tool descriptions, system prompts shipped with a component — are read by a model and can carry directives, which makes them a [prompt-injection](prompt-injection.md) surface that no code review or dependency scanner is looking at.

**The governance fact that changes the calculus is legal rather than technical.** Under EU AI Act Article 25, a distributor, importer, deployer or other third party **becomes the provider** of a high-risk system — assuming the provider's full obligations — if they put their name or trademark on it, make a **substantial modification** to it, or **modify its intended purpose**. Fine-tuning a base model and deploying it under your own brand is not obviously "using someone else's model" in the eyes of that provision.

**So the inheritance runs in both directions.** You inherit risk you cannot inspect, and you can inherit liability you did not intend to assume — by doing things that feel routine: rebranding, adapting, repurposing ([fine-tuning](fine-tuning.md)).

**Disclosure is the binding constraint on all of it.** Frontier model providers generally do not publish corpus composition, so the deepest supplier in the chain is the one you can assess least ([training data](training-data.md)). Supplier assessment questionnaires return statements, not evidence, and **a supply chain you cannot see is managed by contract rather than by verification.**

---

## Plain-language version

Almost nobody builds an AI system from nothing. You take a model someone else trained, on data you cannot see, downloaded from a place you did not audit, wired together with frameworks and packages written by strangers. Then you put your product name on it.

Ordinary supply-chain security helps — check your suppliers, check what you downloaded is what they published — and then runs out. **You can confirm a model file is exactly the one the provider released and still have no idea how it behaves**, because what it does was decided by training data and choices nobody outside that company can look at.

Two problems here have no equivalent in normal software. Someone can corrupt a model by poisoning the **data** it learned from, leaving the code untouched. And some of what ships alongside a model is **instructions rather than programs** — tool descriptions, skill files, prompts — which the model reads and follows. A dependency scanner is not looking for that, because it isn't code.

Now the part that catches organizations out, and it is legal rather than technical. Under the EU AI Act, if you **put your name on** a high-risk system, **substantially modify** it, or **change what it is for**, you stop being a user of someone else's product and become its **provider** — with the maker's full obligations. Fine-tuning a model and shipping it as your own feature can be exactly that.

So you are inheriting two things at once: risk you cannot inspect, and possibly responsibility you did not plan to take on.

**The practical bind: the supplier you most need to assess is the one who tells you least.** Model providers do not publish what they trained on. What you get back from a supplier questionnaire is a statement, not evidence — which means most of this chain is managed by contract, not by checking.

---

## AI literacy notes

1. **AI systems are assembled, not built** — most of the stack came from elsewhere.
2. **Hash verification proves origin, not behavior**; the risky properties are not in the file's contents.
3. **Poisoning attacks the data path**, leaving code review and dependency scanning blind.
4. **Some shipped artifacts are instructions, not code**, and are read by the model.
5. **Rebranding, substantially modifying, or repurposing can make you the *provider*** under the EU AI Act.
6. **The deepest supplier discloses the least** — training-data composition is generally unpublished.
7. **Questionnaires return statements, not evidence.**
8. **Depth matters:** your model's provider had suppliers too, and you have no relationship with them.

---

## Governance notes

**Core question:** For each externally-sourced component in this system, do we know where it came from, what we changed about it, and whether that change made us its provider?

**Watch for:**
- No inventory of models, weights, datasets and agent artifacts in use — you cannot govern an unlisted dependency ([shadow AI](shadow-ai.md))
- A fine-tuned, rebranded model still described internally as "the vendor's model" ([fine-tuning](fine-tuning.md))
- Intended purpose changed from the one the provider documented, with no reassessment ([model card / system card](model-card-system-card.md))
- Weights pulled from a hub with no provenance check and no record of which revision is running ([model version and update](model-version-update.md))
- Skill files, tool definitions or prompts treated as configuration rather than as an injection surface ([prompt injection](prompt-injection.md))
- Supplier assurance consisting of a completed questionnaire with nothing verifiable behind it
- No plan for a supplier disappearing, deprecating, or materially changing a model you depend on ([systemic risk](systemic-risk-ai.md))
- Open-weight components treated as lower-risk because they are inspectable — the weights are visible, the training data still is not

**Practice:**
- **Maintain an inventory of every externally-sourced model, dataset and agent artifact**, with source, revision and who approved it — everything else here depends on this existing
- **Assess your own status under Article 25 explicitly**: name, modification, purpose. Record the determination before someone else makes it for you
- Pin revisions rather than tracking a moving tag, and record which one is in production ([model version and update](model-version-update.md))
- Verify integrity where you can (hashes, signatures) **and write down what that does not tell you**, so the check is not mistaken for behavioral assurance
- Review agent artifacts as instructions — read what a skill file or tool description actually says to the model
- Ask suppliers for training-data provenance and **record the refusal**, which is evidence of the gap rather than a dead end ([data provenance and lineage](data-provenance-lineage.md))
- Test inherited components yourself for the properties you rely on; a provider's evaluation describes their configuration, not yours ([evaluation](evaluation.md))

**Key accountability owner:** whoever signs the deployment into production — because Article 25 attaches to acts (branding, modifying, repurposing) that are usually taken as engineering or product decisions, and the obligation arrives whether or not anyone noticed the threshold.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the structure, medium on the AI-specific threat picture.** That AI systems are assembled from externally-sourced components, that supply-chain risk management is a defined discipline, and that Article 25 reassigns provider status on the three named triggers are all established and quoted here from primary sources. **The AI-specific attack surfaces are demonstrated but not quantified**: poisoning and instruction-bearing artifacts have published proof-of-concept research, and there is no reliable base rate for how often either occurs in practice — treat them as reasons to look, not as a risk score. **The claim stated most confidently is the disclosure asymmetry**, which follows from what providers do and do not publish rather than from any threat assessment. Article 25's thresholds — particularly what counts as a *substantial* modification — are subject to guidance that continues to develop; verify before relying on a determination.

---

## Related concepts

- [Training Data](training-data.md) — the supplier input nobody downstream can inspect
- [Fine-tuning](fine-tuning.md) — the routine act that can make you the provider
- [Model Version & Update](model-version-update.md) — a supplier changing the thing you depend on
- [Prompt Injection](prompt-injection.md) — why instruction-bearing artifacts are a distinct surface
- [Data Provenance / Lineage](data-provenance-lineage.md) — the record that makes a chain assessable
- [Compliance (AI Systems)](compliance-ai-systems.md) — where provider obligations land
- [Shadow AI](shadow-ai.md) — components in use that no inventory knows about
- [Systemic Risk (AI)](systemic-risk-ai.md) — concentration, when everyone depends on the same few suppliers
- [Frontier AI](frontier-ai.md) — the upstream suppliers with the least disclosure
- [Model Card / System Card](model-card-system-card.md) — the documentation that stops describing your model once you change it

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-301 | European Parliament / Council of the EU — *EU AI Act, Article 25: Responsibilities along the AI value chain* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The provision this entry's central point rests on, verified verbatim from EUR-Lex: a distributor, importer, deployer or other third party **is considered a provider** — assuming Article 16 obligations — where they put their name or trademark on a high-risk system, make a **substantial modification** to it, or **modify its intended purpose**. Turns inherited risk into potentially inherited liability. ⚠️ What counts as *substantial* is subject to developing guidance; quote the triggers, do not predict determinations. |
| SRC-302 | National Institute of Standards and Technology (NIST) — *Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations* (SP 800-161 Rev. 1) · [link](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) | The established discipline the AI case extends: supplier assessment, provenance and integrity as a governed practice. Used here to mark where conventional practice applies **and where it stops** — it assumes an artifact whose behavior can be reasoned about from its contents. |
| SRC-269 | Saha, Shoumik; Faghih, Kazem; Feizi, Soheil — *Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry* (2026) · [link](https://arxiv.org/abs/2605.11418) | The AI-specific surface with no traditional analogue: agent artifacts that are **instructions rather than executables**, read by a model and capable of carrying directives past code review and dependency scanning. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The governance frame third-party AI risk is managed within — mapping and measuring risks arising from components the organization did not build. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Inventory every external model, dataset and agent artifact with source and revision. Verify integrity, and write down what integrity does not tell you. |
| **Organizational** | Branding, substantially modifying or repurposing a high-risk system can make you its **provider** under Article 25. Make that determination deliberately, before someone else makes it for you. |
| **Client-facing** | Supports an honest answer about what is in the system and what can be assured about it — including the parts nobody downstream can verify. |
| **LLM-native** | The supplier you most need to assess discloses the least. Read skill files and tool descriptions as instructions, because the model does. |

---

*Last updated: v1.0 · September 2026*
