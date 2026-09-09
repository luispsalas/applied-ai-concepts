<!--meta
category: Observability & Governance
short: The energy, water and emissions behind model training and use — a rising reporting expectation that organizations cannot currently compute for themselves
aliases: [AI energy use, carbon footprint of AI, AI water usage, data center energy, sustainability of AI, is AI bad for the environment]
tags: [Data Governance, Regulatory, Ethics]
established: established
-->
# Environmental Cost of AI

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Training and running models consumes significant energy and water — a real and often-invisible cost of the convenience, and an increasing reporting expectation.

---

## Technical definition

The environmental cost of AI spans three linked quantities: **electricity** consumed by training and serving models, **greenhouse gas emissions** arising from that electricity, and **water** withdrawn or evaporated for cooling and, indirectly, for power generation.

**The electricity figures are the best-established.** The IEA reports data center electricity consumption at **485 TWh in 2025**, projected to roughly **double to 950 TWh by 2030** — around **3% of global electricity demand**. Growth is concentrated: overall data center demand grew **17% in 2025** while AI-focused facilities **surged 50%**.

**Water is measured less well and is more locally consequential.** Li et al. estimate that training GPT-3 in Microsoft's US data centers **directly evaporated 700,000 liters of clean freshwater**, and project global AI water withdrawal at **4.2–6.6 billion cubic meters in 2027** — which they compare to the total annual withdrawal of four to six Denmarks. Electricity is fungible across a grid; **water is not, and a data center in a water-stressed region imposes a local cost that a global average conceals.**

**The training/inference split matters and is widely misread.** Training is a large, bounded, one-time expense that attracts the headlines. Inference is small per request and repeated indefinitely, so for any system with real usage it accumulates into the larger share ([inference](inference.md)). **Public debate is anchored on the number that stops growing.**

**Location is a bigger lever than model choice.** The same workload run on a low-carbon grid emits a fraction of what it emits on a coal-heavy one, and a facility in a water-scarce basin carries a cost one in a wet region does not. **Where you run is more consequential than which model you pick**, and it is the variable most organizations never consider.

**And here is the governance crux: you almost certainly cannot compute your own footprint.** Providers do not publish per-request energy or water, so an organization consuming AI through an API has no defensible basis for its own figure. **The reporting expectation is rising faster than the disclosure that would let anyone meet it honestly**, which pushes organizations toward estimates whose uncertainty is rarely carried alongside the number.

---

## Plain-language version

Running AI uses electricity, and generating that electricity produces emissions. Cooling the buildings uses water. None of this is visible from the chat window.

The scale is genuinely large. Data centers used about 485 terawatt-hours of electricity in 2025 and are expected to use roughly double that by 2030 — around 3% of the world's electricity. The AI-specific part is the fast-growing bit: up about half in a single year.

Water gets less attention and matters more locally. One estimate puts the training of a single well-known model at seven hundred thousand liters of clean freshwater evaporated. Electricity can be moved around a grid; water cannot. A data center in a dry region is a local problem in a way that a national average never shows.

Two things are commonly misunderstood.

First, most coverage is about **training** — the one-off cost of building a model. But every use afterwards costs something too, and for a widely-used system those small repeated costs add up to more than the one-off. The number people argue about is the one that stopped growing.

Second, and more usefully: **where the computation happens matters more than which model you chose.** The same work on a wind-powered grid and on a coal-powered one are not comparable. That is a lever most organizations have and never pull.

Now the honest part. If you use AI through somebody else's service, **you almost certainly cannot work out your own share.** The providers do not publish it. Meanwhile the expectation that you report environmental impact is growing. That gap is filled with estimates, and the estimates are usually quoted without the uncertainty that should travel with them.

---

## AI literacy notes

1. **Three quantities, not one** — electricity, emissions and water behave differently and are measured to different standards.
2. **Inference accumulates past training** for any system with real usage; the headline number is the one that stops growing.
3. **Water is local in a way electricity is not** — a global average hides the cost of a facility in a water-stressed basin.
4. **Location beats model choice** as a lever, and is the variable least often examined.
5. **You cannot compute your own footprint from provider APIs** — the disclosure does not exist.
6. **Efficiency gains are real and are being outpaced by demand growth**, so per-query improvements do not imply falling totals.
7. **Published figures vary widely** between sources and methods; a single confident number should raise suspicion.
8. **The reporting expectation is arriving before the data**, which is the practical governance problem rather than the physics.

---

## Governance notes

**Core question:** If we were asked to report the environmental cost of our AI use, what could we actually evidence — and would the uncertainty travel with the number?

**Watch for:**
- A footprint figure quoted with no method, no boundary, and no uncertainty range ([bluewashing](bluewashing.md))
- Training-only accounting for a system whose usage makes inference the larger share ([inference](inference.md))
- Vendor sustainability claims accepted without asking what is inside the boundary and what is excluded
- Region of deployment never considered, so the largest available lever is unused
- Water omitted entirely because electricity is easier to obtain
- Efficiency-per-query improvements reported as absolute reductions while total consumption rises
- Environmental disclosure obligations assumed to be met by a provider's aggregate report, which is not your figure
- Estimates hardening into cited facts as they are repeated internally ([data provenance](data-provenance-lineage.md))

**Practice:**
- **State the boundary before the number** — training or inference, direct or including power generation, your usage or the provider's total
- **Carry the uncertainty with the figure everywhere it travels**, since the estimate will outlive the caveat otherwise
- Ask providers for per-request or per-token energy and regional carbon intensity, and **record the refusal when it comes** — an unanswered question is evidence of the gap
- Treat region selection as a governed decision where the provider offers it
- Account separately for water where operating in or procuring from a water-stressed region
- Prefer smaller models and shorter outputs where they suffice — the same lever that reduces cost and latency ([small language models](small-language-models.md), [latency](latency-ai-systems.md))
- Disclose method alongside result in any published claim ([model card / system card](model-card-system-card.md), [AI management system](ai-management-system-iso-42001.md))

**Key accountability owner:** whoever signs the organization's sustainability disclosure — because they are accountable for a figure the AI supply chain does not currently give them the data to produce, and the honest response to that is a stated limitation rather than a confident estimate.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on direction and scale, low-medium on any specific number — and the gap between those is this entry's main caution.** The IEA figures are from an intergovernmental body and are the most defensible available; the water estimates are peer-reviewed but are *estimates* built on disclosed and inferred parameters, and the authors present them as such. **Published figures across the field vary by large factors** depending on boundary choices — whether power generation is included, whether embodied hardware emissions count, whether training is amortized over usage — and comparisons between sources are frequently invalid for that reason. **Projections to 2030 are scenarios, not forecasts.** This entry deliberately gives magnitudes with their sources attached rather than a single headline figure, and the claim it states most confidently is the structural one: **that organizations cannot currently compute their own share**, which follows from what providers do and do not publish.

---

## Related concepts

- [Inference](inference.md) — the recurring cost that accumulates past the one-time training figure
- [Small Language Models (SLMs)](small-language-models.md) — the capability-for-resources trade with a direct environmental reading
- [Latency (AI Systems)](latency-ai-systems.md) — shorter outputs reduce time, cost and energy together
- [Edge AI](edge-ai.md) — relocating computation, with its own energy profile
- [Compliance (AI Systems)](compliance-ai-systems.md) — where disclosure obligations attach
- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — the management framework such reporting sits inside
- [Model Card / System Card](model-card-system-card.md) — the disclosure surface where method belongs beside result
- [Bluewashing](bluewashing.md) — the failure mode of an unevidenced sustainability claim
- [Value Realization (AI)](value-realization-ai.md) — cost against benefit, with resources counted
- [Frontier AI](frontier-ai.md) — where training-scale consumption is concentrated

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-277 | International Energy Agency (IEA) — *Key Questions on Energy and AI* (2026) · [link](https://www.iea.org/reports/key-questions-on-energy-and-ai/executive-summary) | The electricity figures used here: data center consumption **485 TWh in 2025**, projected to **950 TWh by 2030** and around **3% of global electricity demand**; overall demand **+17% in 2025** with AI-focused facilities **+50%**. Intergovernmental and the most defensible available. ⚠️ Contains no water figures — that gap is why SRC-278 is cited separately. Projections are scenarios, not forecasts. |
| SRC-278 | Li, Pengfei; Yang, Jianyi; Islam, Mohammad A.; Ren, Shaolei — *Making AI Less "Thirsty": Uncovering and Addressing the Secret Water Footprint of AI Models* (2023, revised 2025) · [link](https://arxiv.org/abs/2304.03271) | The water estimates: training GPT-3 in Microsoft's US data centers **directly evaporating 700,000 liters** of clean freshwater, and global AI water withdrawal projected at **4.2–6.6 billion cubic meters in 2027**. ⚠️ Estimates built on disclosed and inferred parameters, presented as such by the authors — cite with that framing, never as measurement. |
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | The disclosure pattern this entry's practice section follows: method and boundary reported alongside result, rather than a bare figure. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The management-system frame in which environmental reporting for AI sits as a governed, auditable process rather than an ad-hoc calculation. ⚠️ Paywalled standard. |
| SRC-247 | Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu, C.H.; Gonzalez, J.E.; Zhang, H.; Stoica, I. (UC Berkeley et al.) — *Efficient Memory Management for Large Language Model Serving with PagedAttention* (SOSP, 2023) · [link](https://arxiv.org/abs/2309.06180) | Evidence that serving efficiency is a real and improving engineering variable — the basis for distinguishing per-query efficiency gains from absolute consumption. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Region of deployment is a larger lever than model choice. Shorter outputs and smaller models reduce time, cost and energy together. |
| **Organizational** | You are accountable for a figure your supply chain does not give you the data to produce. Ask providers for per-request energy and regional intensity, and record the refusal — an unanswered question is evidence of the gap. |
| **Client-facing** | Supports an honest answer about environmental impact, including the parts that genuinely cannot be quantified yet. |
| **LLM-native** | Inference accumulates past training for anything widely used. Water is local in a way electricity is not, and the reporting expectation is arriving ahead of the disclosure needed to meet it. |

---

*Last updated: v1.0 · September 2026*
