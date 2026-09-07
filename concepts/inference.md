<!--meta
category: Foundations
short: Running a trained model to produce an output — the phase that carries almost all of a system's lifetime cost, latency and governance surface, and the one most often left out of AI budgets
aliases: [model inference, serving, running the model, prediction, inference time, test-time, deployment cost, why is the API bill so high]
tags: [AI Literacy, Architecture]
established: established
-->
# Inference

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The process of running a trained AI model to generate outputs — as distinct from training. Most production AI use is inference.

---

## Technical definition

Inference is the execution phase: a trained model's parameters are held fixed and used to compute an output for a given input. It is the counterpart to training, where the parameters themselves change. **Everything a deployed model does for a user is inference.**

**The economics are the reverse of the intuition most people carry.** Training is a large, bounded, one-time expense. Inference is a small per-request expense repeated indefinitely, and for any system with real usage it dominates the total. Hoffmann et al. (2022) made the direction of this trade explicit at the design stage: because a model is trained once and served many times, it can be rational to train a smaller model on far more data than compute-optimality alone suggests, specifically to lower the inference cost that follows ([small language models](small-language-models.md)).

**For generative models, inference is sequential and that shapes everything downstream.** Output is produced one token at a time, each conditioned on all preceding ones. Latency therefore scales with output length rather than being fixed per request, and the intermediate state (the KV cache) grows with the conversation. Kwon et al. (SOSP 2023) showed that memory management of that cache was the binding constraint on serving throughput — their PagedAttention scheme, borrowing virtual-memory paging from operating systems, improved throughput 2–4× at equal latency. **The relevant point for a non-specialist is that "how many users can we serve" was answered by memory layout, not by model quality.**

**Inference is not deterministic by default, and often not deterministic even when asked to be.** Sampling introduces variation by design ([temperature](temperature-llms.md)), but He (2025) shows that identical requests can produce different outputs even at temperature zero, because batching and kernel non-determinism make a result depend on what *other* requests happened to be processed alongside it. **Reproducibility is a property of the serving stack, not only of the model or its settings** ([determinism vs probabilism](determinism-vs-probabilism.md)).

**Compute spent at inference now buys capability, which changes the trade.** Snell et al. (2024) found that allocating additional test-time compute can outperform scaling model parameters for some problems — the basis of [reasoning models](reasoning-models.md). Cost per request stops being a fixed property of the model and becomes a dial someone chooses, usually without a policy governing it.

---

## Plain-language version

There are two very different things people mean by "running AI." Training is building the model — enormously expensive, done rarely. Inference is *using* it: you send a question, it computes an answer. Every time anyone uses the system, that is inference.

Most of the public conversation is about training costs. Most of the actual bill is inference, because it happens every time, forever. A model is trained once and used millions of times, so a design that is slightly cheaper to run beats one that was slightly cheaper to build, almost always.

Text models produce their answers one piece at a time, each piece depending on everything written before it. That is why a long answer takes longer than a short one, and why speed is about output length rather than question difficulty. It also means the system is holding a growing pile of working memory for every conversation in progress — and managing that memory well, rather than having a better model, is often what determines how many people you can serve at once.

Two things surprise people. First, the same question can produce different answers even with the randomness setting turned off — because the answer can depend on what other requests were being processed at the same moment. Reproducibility is a property of the plumbing, not just the settings. Second, you can now spend more computing time per question to get a better answer. That makes cost per answer a choice somebody makes, which means it is a decision that ought to have an owner.

---

## AI literacy notes

1. **Training is the one-time cost; inference is the forever cost.** For any system with real usage, inference dominates the total.
2. **This inverts model selection.** A smaller model that is cheaper to serve often beats a larger one that scored better, once lifetime cost is counted.
3. **Latency scales with output length**, not with question difficulty — which is why streaming exists and why verbose prompting is expensive twice over.
4. **Throughput is a memory-management problem** as much as a model problem; serving capacity is an infrastructure decision.
5. **Temperature zero does not guarantee identical outputs.** Batching effects in the serving stack can change results between otherwise identical requests.
6. **Reproducibility must be established at the stack level** if anything depends on it — audit, regression testing, regulated decisions.
7. **Spending more compute per request can raise quality**, so cost per answer is now a dial rather than a constant, and dials need owners.
8. **Every inference call is where the governance surface actually is** — the logging, the [prompt injection](prompt-injection.md) exposure, the data leaving the boundary. Training-time controls do not cover it.

---

## Governance notes

**Core question:** Who owns the per-request cost and latency of this system, and where is the decision recorded that set them at their current level?

**Watch for:**
- A budget built around a training or licensing figure with no lifetime inference projection
- Cost per request drifting upward as prompts, [context](context-ai-systems.md) and reasoning depth grow, with no ceiling and no review
- Reproducibility assumed from a temperature setting rather than verified against the serving stack
- Regression tests or audits that rely on identical outputs from identical inputs without that having been established
- Model choice made on benchmark scores alone, with serving cost treated as an afterthought ([AI benchmarking](ai-benchmarking.md))
- No per-request logging, so the only record of what the system did is the user's own screen ([audit trail](audit-trail-ai.md))
- Unbounded retries or agent loops, where a failure mode is expensive rather than merely wrong ([multi-agent systems](multi-agent-systems.md))
- Sensitive data crossing a boundary at inference time that training-time governance never examined ([privacy](privacy-ai-systems.md))

**Practice:**
- **Project lifetime inference cost before selecting a model**, not after — and re-project when prompt or reasoning depth changes
- Set and monitor ceilings on tokens, retries and reasoning depth per request; treat raising one as a change with an approver
- **Verify reproducibility empirically** if anything downstream depends on it, rather than inferring it from settings
- Log inputs, outputs and configuration per call, including model version ([model version and update](model-version-update.md))
- Measure latency at the percentile users experience, not the mean, and against output length
- Evaluate candidate models on cost-at-quality rather than quality alone ([evaluation](evaluation.md))
- Treat the inference boundary as the primary data-governance perimeter — it is where content actually leaves

**Key accountability owner:** whoever owns the serving budget — because per-request cost, latency and retry policy are all set there, and each is a quality and governance decision arriving disguised as an infrastructure one.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The training/inference distinction is textbook, and the specific claims here — the serving-throughput result, the non-determinism finding, the test-time compute trade, the inference-aware training argument — each come from a named peer-reviewed or lab-published source. **Where confidence drops is on numbers rather than mechanisms:** the ratio of lifetime inference cost to training cost is highly system-specific, providers publish little, and this entry deliberately states the direction of the trade rather than a multiple. Serving-stack behavior also moves quickly — the specific memory-management result is from 2023 and the field has not stood still, so treat particular throughput figures as dated while the underlying constraint remains. **The non-determinism point is the one most often disputed in practice** and is the most worth verifying in your own stack rather than accepting from any source, including this one.

---

## Related concepts

- [Pre-training](pre-training.md) — the phase this one is defined against
- [Fine-tuning](fine-tuning.md) — the other way parameters change, also not inference
- [Reasoning Models](reasoning-models.md) — where additional inference compute is spent deliberately
- [Temperature (LLMs)](temperature-llms.md) — the sampling control applied at this phase
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — why identical inputs need not give identical outputs
- [Small Language Models (SLMs)](small-language-models.md) — the argument that serving cost should drive model choice
- [Local LLMs](local-llms.md) — moving this phase inside your own boundary
- [Scalability (AI Systems)](scalability-ai-systems.md) — what happens to all of this under load
- [Context Window](context-window.md) — the working state whose size drives cost and latency
- [Tokenization](tokenization.md) — the unit both cost and latency are counted in

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-247 | Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu, C.H.; Gonzalez, J.E.; Zhang, H.; Stoica, I. (UC Berkeley et al.) — *Efficient Memory Management for Large Language Model Serving with PagedAttention* (SOSP, 2023) · [link](https://arxiv.org/abs/2309.06180) | Establishes KV-cache memory management as the binding constraint on serving throughput; 2–4× throughput improvement at equal latency, showing capacity as an infrastructure rather than a model property. |
| SRC-145 | He, Horace (Thinking Machines Lab) — *Defeating Nondeterminism in LLM Inference* (2025) · [link](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) | Identifies batch-dependent kernel non-determinism as a cause of varying output at temperature zero — the basis for treating reproducibility as a serving-stack property. |
| SRC-155 | Snell, C.; Lee, J.; Xu, K.; Kumar, A. (UC Berkeley / Google DeepMind) — *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* (2024) · [link](https://arxiv.org/abs/2408.03314) | Evidence that inference-time compute can substitute for parameter scale, making cost per request a deliberate quality dial. |
| SRC-228 | Hoffmann, J.; Borgeaud, S.; Mensch, A.; Buchatskaya, E.; Cai, T.; Rutherford, E.; Sifre, L. et al. (DeepMind) — *Training Compute-Optimal Large Language Models* (2022) · [link](https://arxiv.org/abs/2203.15556) | The compute-allocation frame behind the inference-aware design argument: a model trained once and served many times justifies trading training cost for lower serving cost. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. (Renmin University of China + multi-institution) — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Survey treatment of the training/inference division and autoregressive decoding as the source of sequential latency. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Project lifetime serving cost before choosing a model, cap tokens and retries per request, and verify reproducibility against your stack rather than assuming it from a temperature setting. |
| **Organizational** | The recurring bill and the governance perimeter both live here, not in training. A per-request cost with no owner is a budget line that grows on its own. |
| **Client-facing** | Explains why response time tracks answer length, why costs scale with use rather than with purchase, and why "the same question twice" can differ. |
| **LLM-native** | Training is bounded and one-time; inference is unbounded and forever. Compute spent at this phase now buys capability, which makes cost per answer a decision rather than a constant. |

---

*Last updated: v1.0 · September 2026*
