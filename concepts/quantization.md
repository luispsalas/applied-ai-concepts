<!--meta
category: Foundations
short: Storing a model's weights at lower numerical precision to make it cheaper to run — which produces a different model, with its own evaluation status and its own safety behavior
aliases: [quantized model, quantisation, post-training quantization, PTQ, quantization-aware training, QAT, int8, 4-bit, 8-bit, low precision inference, model compression by precision, GGUF, bit width]
tags: [Architecture, Model Behavior, Evaluation]
established: established
-->
# Quantization

> **Term status — Established.** Standard terminology in numerical computing long before machine learning, and in continuous use across every model-serving stack, hardware vendor and open-weights community. Independent of any vendor.

## One-line essence
Storing and computing a model's weights at lower numerical precision so it runs faster and on smaller hardware — which is not a deployment setting but a change to the model itself.

---

## Technical definition

Quantization reduces the number of bits used to represent a model's parameters, and often its activations — typically from 16-bit floating point to 8-bit or 4-bit integers. Fewer bits means less memory, less memory bandwidth, and cheaper arithmetic, which is why it is the main lever for running a capable model on constrained hardware ([edge AI](edge-ai.md), [local LLMs](local-llms.md)).

**Two families, with different implications for who is responsible for the result:**

- **Post-training quantization (PTQ)** converts an already-trained model. Frantar et al.'s GPTQ made this practical at scale for generative models, quantizing weights in one pass without retraining. **Anyone can apply PTQ to a released model, which means the artifact people run is frequently not the artifact the provider evaluated.**
- **Quantization-aware training (QAT)** trains with the reduced precision in the loop, so the model adapts to it. Better results, far more expensive, and available only to whoever is doing the training.

**The engineering problem is that error is not uniform.** Dettmers et al. showed that a small number of **outlier features** carry disproportionate importance, and naive low-precision handling of those specific dimensions is what breaks large models — their LLM.int8() approach isolates the outliers at higher precision and quantizes the rest. **The loss from quantization is concentrated, not spread**, which is why aggregate benchmark scores can look nearly unchanged while specific behaviors move a lot.

**Which brings the governance point that none of the neighboring entries makes: a quantized model is a different model.** It has different weights, different outputs, and its own evaluation status. **Everything established about the full-precision version — benchmark results, red-team findings, safety evaluations, model card claims — was measured on an artifact you are not running** ([model card / system card](model-card-system-card.md), [evaluation](evaluation.md)).

**This is not a theoretical concern.** Kharinaev et al. evaluate 66 quantized variants across four post-training and two quantization-aware methods, against four safety benchmarks including human evaluation, and find **both PTQ and QAT can degrade safety** — with the trade-offs varying by method rather than following a simple precision-versus-quality curve. **The degradation does not announce itself**: a quantized model that has lost safety behavior still answers fluently.

**And the loss is not evenly distributed across users.** Because quantization error concentrates in the less-represented parts of a model's behavior, the capabilities that degrade first tend to be the ones that were weakest to begin with — lower-resource languages, minority dialects, specialist domains. **A quantized deployment can be near-identical for the median user and materially worse for a minority**, and an aggregate benchmark will not show it ([bias](bias-ai-systems.md)).

---

## Plain-language version

Models store their knowledge as very large piles of numbers. Quantization is the practice of storing those numbers less precisely — rounding them, roughly speaking — so the model takes less memory and runs faster and cheaper. It is how a model that needed a data-center GPU comes to run on a laptop or a phone.

It works remarkably well, which is why everyone does it. But it is worth being clear about what it is.

**It is not a setting. It is a different model.** The numbers are genuinely different, so the outputs are genuinely different. Everything anyone measured about the original — how accurate it is, what it refuses, what the safety testing found, what the documentation claims — was measured on a model you are not running.

**And the damage is lumpy, not smooth.** Rounding does not degrade everything a little; it degrades a few things a lot, and leaves most things almost untouched. That is precisely what makes it hard to catch: run a standard benchmark and the score barely moves, because the benchmark is dominated by the things that were fine. The problems are hiding in the parts nobody averaged.

Two consequences follow, and both are easy to miss.

**Safety behavior can be among the things that shifts.** Researchers evaluated dozens of quantized versions across several methods and found that safety behavior can degrade — and not in a tidy way where less precision always means worse. It depends on the method. **A model that has lost some of its safety training does not sound damaged. It sounds the same.**

**And the loss tends to fall on whoever was already least well served.** The things a model does *weakly* are the first to break under rounding — a smaller language, an unusual dialect, a specialist subject. So a quantized deployment can be indistinguishable from the original for most users and noticeably worse for a minority, with the overall score showing nothing.

None of this is an argument against quantization. It is an argument for treating the quantized thing as a model in its own right: test it, document which version it is, and do not inherit assurances from something else.

---

## AI literacy notes

1. **A quantized model is a different model**, not a configuration of the same one.
2. **Evaluations do not transfer** from the full-precision artifact to the quantized one.
3. **Two families**: post-training (anyone can do it) and quantization-aware training (only the trainer can).
4. **Error is concentrated, not uniform** — a few outlier dimensions carry the damage.
5. **Aggregate benchmarks hide it**, because they are dominated by what did not break.
6. **Safety behavior can degrade**, measured across 66 variants and six methods.
7. **Degradation is silent** — a weakened model still sounds fluent and confident.
8. **Weakest capabilities break first**, so minority languages and specialist domains suffer most.
9. **It is the main enabler of on-device and local deployment**, which is why it is everywhere.

---

## Governance notes

**Core question:** Which exact artifact is in production — precision, method, and who produced it — and what has been evaluated on *that*, rather than on the model it was derived from?

**Watch for:**
- Safety, accuracy or red-team results inherited from the full-precision model ([evaluation](evaluation.md), [red teaming](red-teaming.md))
- A model card describing a model that is not the one deployed ([model card / system card](model-card-system-card.md))
- Quantization applied by an infrastructure team as an optimization, with no re-evaluation triggered
- Only aggregate benchmarks used to confirm "no meaningful loss," with no per-domain or per-language breakdown
- A quantized build downloaded from a public hub with unknown method and unverified provenance ([supply chain risk](supply-chain-risk-ai.md), [checkpointing](checkpointing.md))
- Deployment to a multilingual or specialist user base with testing only in the majority language ([bias](bias-ai-systems.md))
- Precision changed silently between releases, so a behavioral regression has no obvious cause ([model version and update](model-version-update.md))
- Cost savings reported without the corresponding capability and safety assessment
- Edge deployment where the quantized model cannot be patched centrally once shipped ([edge AI](edge-ai.md))

**Practice:**
- **Record the exact artifact**: base model, version, precision, quantization method, and who produced the build — this belongs with the deployment, not in someone's memory
- **Re-run safety evaluation on the quantized build specifically.** The published finding is that degradation is method-dependent, so it cannot be predicted from the bit width alone
- **Evaluate per-domain and per-language, not only in aggregate** — the aggregate is where this failure hides by construction
- Treat a precision change as a model change requiring the same approval as any other ([model version and update](model-version-update.md))
- Verify the provenance and format of third-party quantized builds before loading them ([supply chain risk](supply-chain-risk-ai.md))
- **State the deployed precision in user-facing documentation** where output quality materially depends on it
- For on-device deployment, decide the update path before shipping, since the artifact leaves your control ([edge AI](edge-ai.md))
- Where quantization is what makes a deployment affordable, **record that trade explicitly** rather than presenting the result as equivalent to the full model

**Key accountability owner:** whoever approved the deployment — because quantization is usually performed downstream as an infrastructure optimization, by people whose remit is cost and latency, while the assurance being invalidated belongs to whoever signed off the model.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, moderate on the magnitude of any specific loss.** The technique is mature, the outlier-concentration finding and the practical PTQ method are both peer-reviewed at major venues, and the safety evaluation covers 66 variants across six methods with human-annotated benchmarks. **Two limits.** The safety result establishes **that** degradation occurs and that it is method-dependent — it does not license a general claim that any given quantization will degrade safety, and this entry does not make one. And the distributional claim, that weakly-represented capabilities degrade first, follows from the concentration of quantization error and is consistent with the multilingual literature, but this entry states it as a **structural expectation to test for rather than a measured universal**; the practice section accordingly says to measure it rather than assume it.

---

## Related concepts

- [Model Distillation](model-distillation.md) — the other main route to a smaller, cheaper model
- [Small Language Models](small-language-models.md) — what quantization often makes deployable
- [Edge AI](edge-ai.md) — the deployment quantization enables
- [Local LLMs](local-llms.md) — running a model on your own hardware
- [Inference](inference.md) — the cost quantization reduces
- [Environmental Cost of AI](environmental-cost-of-ai.md) — the resource case for lower precision
- [Model Card / System Card](model-card-system-card.md) — documentation that describes the wrong artifact
- [Model Version & Update](model-version-update.md) — precision as a version-defining property
- [Evaluation (AI Systems)](evaluation.md) — what does not transfer
- [Bias (AI Systems)](bias-ai-systems.md) — uneven degradation across languages and domains
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — third-party builds of unknown provenance
- [Checkpointing](checkpointing.md) — the model file itself as an untrusted artifact

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-346 | Frantar, Elias; Ashkboos, Saleh; Hoefler, Torsten; Alistarh, Dan — *GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers* (ICLR, 2023) · [link](https://arxiv.org/abs/2210.17323) | The method that made post-training quantization practical at generative-model scale without retraining — which is why the artifact in production is so often one the provider never evaluated. |
| SRC-347 | Dettmers, Tim; Lewis, Mike; Belkada, Younes; Zettlemoyer, Luke — *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2208.07339) | The concentration result this entry's central argument rests on: a small set of **outlier features** carries disproportionate importance, so quantization error is concentrated rather than spread — which is why aggregate scores can hold while specific behaviors move. |
| SRC-348 | Kharinaev, Artyom; Moskvoretskii, Viktor; Shvetsov, Egor; Studenikina, Kseniia; Bykov, Mikhail; Burnaev, Evgeny — *Investigating the Impact of Quantization Methods on the Safety and Reliability of Large Language Models* (2025) · [link](https://arxiv.org/abs/2502.15799) | The safety evidence: **66 quantized variants**, four post-training and two quantization-aware methods, across four safety benchmarks including human evaluation — finding that both families **can** degrade safety, with trade-offs that depend on method rather than on precision alone. ⚠️ Establishes that degradation occurs and is method-dependent; it does not license a general claim about any particular build. |
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | The disclosure surface that quantization silently invalidates: a model card describes the artifact it was written for, and nothing in the format flags that the deployed build is a different one. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Record base model, precision, method and builder with the deployment. Re-run safety evaluation on the quantized build, and break results down by language and domain. |
| **Organizational** | The cheap version is a different model. Every assurance you hold was measured on something else, and the aggregate benchmark is where that fact hides. |
| **Client-facing** | Explains how the same system can run on a phone, and why "same model, smaller" is not quite what happened. |
| **LLM-native** | Error concentrates in outlier dimensions, so weakly-represented capabilities break first. A model that lost safety training still sounds fluent. |

---

*Last updated: v1.0 · September 2026*
