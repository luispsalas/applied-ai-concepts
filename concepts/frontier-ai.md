<!--meta
category: Observability & Governance
short: The leading edge — a category defined by capabilities being discovered after training, not by size
aliases: [frontier model, state of the art model, most capable models, cutting edge AI, leading models]
tags: [Regulatory, Safety]
-->
# Frontier AI (Frontier Model)

## One-line essence
The most capable AI models at any given time — the class regulators and AI labs single out for extra safety scrutiny because their capabilities are advancing faster than tools to evaluate them.

---

## Technical definition

The leading edge of model capability at a given moment. The working definition in the policy literature is *"highly capable foundation models that could possess dangerous capabilities sufficient to pose severe risks to public safety."*

**The category is defined by three properties, not by size** — and this is what makes it a coherent regulatory object rather than a superlative:

- **Capabilities emerge unpredictably.** What a model can do is discovered after training, not specified before it. You cannot write a pre-deployment safety case against a capability nobody knew the model would have.
- **Misuse is hard to prevent after deployment.** A general-purpose model's uses are not enumerable by its provider, so post-hoc restriction is partial by construction.
- **Capabilities proliferate once released.** Weights, techniques and distillations spread, so a decision made once by one lab does not stay contained.

**"Frontier" is inherently relative and therefore decays.** Today's frontier model is next year's mid-tier one, so any list of frontier models is a snapshot. **Do not attach durable policy to a named model** — attach it to the properties above, or to a threshold that is explicitly maintained.

**The relationship to the regulatory category.** [Systemic Risk (AI)](systemic-risk-ai.md) is what happened when this informal category met binding law: the EU AI Act does not use "frontier," and instead classifies general-purpose models with systemic risk, presuming high-impact capability above 10^25 training FLOP. **Frontier is the concept; systemic-risk designation is the legal instrument.** They overlap heavily and are not the same set, and using the words interchangeably in a compliance context is a real error.

**Three of the proposed governance building blocks are now law.** The policy literature proposed standard-setting, registration and reporting, and compliance enforcement, plus pre-deployment risk assessment, external scrutiny, and post-deployment capability monitoring. EU AI Act Art. 55 obligations map onto that closely enough that the lineage is visible — which is a useful reminder that this vocabulary was constructed by an identifiable community with identifiable interests, several of them working at the labs being regulated.

---

## Plain-language version

"Frontier" means the most capable models around right now — the ones at the leading edge.

The reason they are treated as a separate category is not that they are big. It is that nobody, including the people who built them, knows in advance what a new model will be able to do. Capabilities turn up during testing after training is finished. That makes the usual approach to safety — decide what a product does, then assess whether that is safe — structurally difficult, because the first half is not available.

Two further things compound it. Once a general-purpose model is released, its uses cannot be listed, so restricting misuse is always partial. And capability spreads, through open weights and through smaller models trained to imitate larger ones, so a single lab's decision does not stay that lab's decision.

The word itself is a moving target. Whatever counts as frontier today will be ordinary in a few years. That is why regulation avoids the word and uses measurable thresholds instead — and why anything you write that depends on a list of frontier models will be wrong quite soon.

---

## AI literacy notes

1. **Frontier is relative and always dating.** It names a position, not a capability level. Anything written against a list of models has a short shelf life.
2. **The defining problem is unpredictable capability, not scale.** Big is a proxy. What makes the category coherent is that you cannot enumerate what the model will be able to do before you have it.
3. **"Frontier" and the EU's "systemic risk" are not synonyms.** One is an informal category, the other a legal designation with a compute presumption and specific obligations. Do not swap them in a compliance context.
4. **Frontier capability does not imply frontier suitability.** For most organizational tasks, a smaller or older model is a better fit — see [Small Language Models](small-language-models.md). Frontier is a safety category, not a procurement recommendation.
5. **The vocabulary has authors with interests.** The framing was developed substantially by researchers affiliated with the labs it governs. That does not make it wrong; it does mean the category's boundaries are not neutral, and where the line falls is contested for good reason.
6. **Proliferation makes the category leaky.** Open weights and distillation move capability downward continuously, so the gap between frontier and non-frontier is narrower than a top-of-the-leaderboard framing suggests.
7. **Extra scrutiny is not a safety guarantee.** Designation means more evaluation and reporting duties, not that a model has been shown to be safe. The reason for the scrutiny is that evaluation is inadequate.

---

## Governance notes

**Core question:** Does anything you have written depend on which models are currently "frontier" — and what happens to it when that changes?

**Watch for:**
- Policies and contracts written against named models or vendors rather than against properties or thresholds
- "Frontier" and "systemic risk" used interchangeably in documents with compliance consequences
- Frontier capability selected by default when the task does not need it, importing cost, latency and vendor concentration for no benefit
- Provider safety documentation treated as a substitute for evaluation in your own context
- The category treated as someone else's problem: most of its obligations fall on providers, but **capability proliferation means the risks reach deployers without the designation reaching them**
- Model updates changing the capability of a system you already assessed ([model/data drift](model-data-drift.md))

**Practice:**
- Write policy against capability properties and named thresholds, not model names; review whenever the threshold or the market shifts
- Keep the distinction explicit in any document a regulator or auditor might read
- Where you deploy a frontier model, read its system card and evaluations as a *starting point* and re-evaluate for your use ([model card](model-card-system-card.md), [evaluation](evaluation.md))
- Right-size deliberately: state why the task requires frontier capability, if it does
- Track designation and safety-framework status of providers you depend on — it signals both maturity and a regulatory surface that may reach your contracts ([systemic risk](systemic-risk-ai.md))
- Re-assess on provider model updates; a capability change is a change to your system whether or not you initiated it

**Key accountability owner:** for providers, the party carrying the regulatory duties. **For deployers — which is almost everyone — whoever owns model selection**, since the practical decisions here are choosing a class of model, writing policy that survives it changing, and re-assessing when it does.

---

## Confidence level

**Medium.** The defining properties are well argued and widely adopted, and the influence on subsequent regulation is traceable. **Three caveats worth stating.** The foundational source is a preprint and explicitly advocacy — it argues for a regulatory approach, and several authors are affiliated with frontier labs, which is a genuine interest in where the boundary is drawn. **The category has no agreed measurement**; compute thresholds are administrative proxies, and capability benchmarks are the very instruments the category exists because we do not trust. And the term is definitionally unstable — this entry is written to be about the properties precisely because anything written about the membership will date fast.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Related concepts

- [Systemic Risk (AI)](systemic-risk-ai.md) — the binding legal category this informal one shades into; not synonyms
- [Small Language Models (SLMs)](small-language-models.md) — the other end, and usually the better organizational fit
- [Red Teaming](red-teaming.md) — the pre-deployment scrutiny frontier governance leans on
- [Evaluation (AI Systems)](evaluation.md) — inadequate to the task, which is the reason the category exists
- [Model Card / System Card](model-card-system-card.md) — where frontier providers document capabilities and limits
- [Alignment (AI Systems)](alignment-ai-systems.md) — much of the underlying capability concern
- [Power Seeking](power-seeking.md) — a specific capability concern in the same register
- Scalable Oversight — the proposed answer to evaluation not keeping pace
- [AI Governance](ai-governance.md) — where the deployer-side decisions actually get made
- [Compliance (AI Systems)](compliance-ai-systems.md) — the obligations designation triggers
- [Model/Data Drift](model-data-drift.md) — provider capability changes as a change to your system
- [AI Incident (Reporting)](ai-incident-reporting.md) — the reporting duties attached to designated models
- Reasoning Models / Test-Time Compute — a capability axis that moves the frontier without moving parameter counts

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-203 | Anderljung, M.; Barnhart, J.; Korinek, A.; Leung, J.; O'Keefe, C.; Whittlestone, J.; et al. — *Frontier AI Regulation: Managing Emerging Risks to Public Safety* (2023) · [link](https://arxiv.org/abs/2307.03718) | The definition and the three properties that make the category coherent — unpredictable emergence, unpreventable misuse, proliferation — plus the governance building blocks later visible in EU law. ⚠️ Preprint, explicitly advocacy, several authors lab-affiliated. |
| SRC-200 | European Parliament / Council of the EU — *EU AI Act, Articles 51 and 55* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The legal instrument this informal category shades into, and the compute-threshold presumption that replaces the word "frontier" in binding text. |
| SRC-143 | Bommasani, R. et al. (Stanford CRFM / HAI) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | The foundation-model framing the category is built on, and the homogenization argument behind proliferation concerns. |
| SRC-159 | Ganguli, D.; Lovitt, L.; Kernion, J.; Askell, A.; Bai, Y. et al. (Anthropic) — *Red Teaming Language Models to Reduce Harms* (2022) · [link](https://arxiv.org/abs/2209.07858) | What pre-deployment scrutiny of a highly capable model actually involves at scale. ⚠️ Vendor-authored. |
| SRC-115 | Stanford HAI — *AI Index Report* (2026) · [link](https://hai.stanford.edu/ai-index) | Independent tracking of capability and concentration trends. ⚠️ Annual — verify the edition permalink and re-check any figure before citing. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | A non-EU lifecycle framing for capability risk, and the govern function where model-class decisions belong. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Frontier is a safety category, not a procurement recommendation. State why the task needs it, and re-evaluate on provider model updates. |
| **Organizational** | Write policy against properties and thresholds, never model names — the membership changes. And keep "frontier" separate from "systemic risk" in anything an auditor reads. |
| **Client-facing** | Explains why the most capable models get extra scrutiny: not because they are known to be dangerous, but because their capabilities are discovered after they are built. |
| **LLM-native** | The defining problem is that capability is discovered post-training, so a pre-deployment safety case cannot be written against a full capability list. Proliferation then moves that capability downward continuously. |

---

*Last updated: v1.0 · August 2026*
