<!--meta
category: Foundations
short: Models where only a fraction of the parameters run for any given token — which quietly breaks parameter count as a way of comparing anything
aliases: [MoE, sparse model, sparsely-gated, conditional computation, active parameters, total parameters, expert routing, why is this model so big but so fast]
tags: [Architecture, Model Behavior, AI Literacy]
established: established
-->
# Mixture of Experts

> **Term status — Established.** A recognized architecture with a 1991 founding paper, in independent use across research groups and model providers.

## One-line essence
An architecture that activates only a fraction of its parameters for each input — decoupling a model's total size from the compute any single request actually uses.

---

## Technical definition

A mixture-of-experts model contains many parallel sub-networks — **experts** — and a **gating** or routing function that sends each input to a small subset of them. Jacobs, Jordan, Nowlan and Hinton introduced the idea in 1991 as a way of letting different sub-networks specialize on different regions of the problem.

**Its modern significance is economic rather than conceptual.** Shazeer et al. applied **conditional computation** at scale, on the observation that a network's capacity to absorb information is bounded by its parameter count, while the cost of using it need not be — so activating parts of the network per example increases capacity *without a proportional increase in computation*. Fedus, Zoph and Shazeer then simplified routing to a single expert per token, reaching trillion-parameter models at **constant computational cost per token**.

**The consequence that matters outside the research literature: parameter count stops meaning one thing.** A dense model's parameter count is both its size and, roughly, its per-token cost. **A sparse model has two numbers — total parameters and active parameters — and they can differ by an order of magnitude.** A "400-billion-parameter" MoE model may run perhaps 30 billion for any given token.

**So every comparison that uses parameter count as a proxy is now ambiguous**, and the ambiguity runs in both directions: comparing a sparse model's *total* against a dense model's overstates its cost and its capability-per-token; comparing its *active* count understates what had to be trained, stored and served. **Providers do not consistently say which number they are quoting**, and many do not disclose the architecture at all ([model card / system card](model-card-system-card.md)).

**Serving economics differ from training economics, which is a common confusion.** Sparsity reduces compute per token, not memory: **all** experts must generally be resident to serve any request, so a sparse model is cheap in FLOPs and expensive in memory. This is why MoE is common in hosted frontier models and rare in [local](local-llms.md) or [edge](edge-ai.md) deployment, where memory is the binding constraint.

**Two behavioral properties are worth knowing.** Routing is learned, so **which experts fire is not a designed or documented mapping** — "experts" are not interpretable specialists and should not be described as such ([mechanistic interpretability](mechanistic-interpretability.md)). And routing depends on the batch a token is processed in under common implementations, which is one of the ways an identical prompt can produce different output ([determinism vs probabilism](determinism-vs-probabilism.md)).

---

## Plain-language version

Most models run all of themselves for every word they process. A mixture-of-experts model does not: it holds a large number of sub-networks and, for each piece of input, a router picks a couple of them to actually run.

The point is economic. You get the benefits of a very large model without paying to run all of it every time.

**The practical consequence is that "how big is this model" stopped having one answer.** There are now two numbers — how many parameters it *has*, and how many actually *run* for any given word — and they can differ by ten times or more. A model advertised at 400 billion parameters might use 30 billion per word.

That matters because parameter count is how people compare models. **Both possible comparisons are wrong in different directions:** use the big number and you overstate what it costs to run; use the small one and you understate what it took to build, store and serve. Providers are not consistent about which they quote, and often do not say the architecture at all.

One more thing that catches people out: **this saves computation, not memory.** All those sub-networks still have to be loaded, even though only a few run. So these models are efficient to run on big hosted infrastructure and awkward on your own hardware, where memory is usually what runs out first.

Finally, a caution about the word *expert*. It suggests a panel of specialists — one for law, one for code. That is not what happens. The router is trained, not designed, and what each sub-network ends up handling is not a documented or human-meaningful division. **Nothing is consulting an expert on anything.**

---

## AI literacy notes

1. **Two parameter counts, not one** — total and active, often differing by an order of magnitude.
2. **Any comparison using parameter count is ambiguous** unless it says which number.
3. **Sparsity saves compute, not memory** — all experts must generally be resident to serve.
4. **That is why MoE suits hosted serving** and sits awkwardly on local or edge hardware.
5. **"Experts" are not interpretable specialists** — routing is learned, not designed.
6. **Architecture is frequently undisclosed**, so you may not know which kind of model you are using.
7. **Routing can introduce output variability** independent of temperature.
8. **Capacity and cost were coupled in dense models and are not here** — that decoupling is the whole idea.

---

## Governance notes

**Core question:** For the models we compare, procure or report on, do we know whether the parameter counts are total or active — and whether we are comparing like with like?

**Watch for:**
- Model comparisons resting on parameter count with no statement of which count ([AI benchmarking](ai-benchmarking.md))
- Cost or capability projections built from total parameters on a sparse model
- Local or on-premise plans that budget by active parameters and are then defeated by memory ([local LLMs](local-llms.md), [edge AI](edge-ai.md))
- "Expert" described to non-technical audiences as a specialist consulted for a topic ([anthropomorphism](anthropomorphism-ai.md))
- Architecture undisclosed, and the gap unrecorded in the assessment ([model card / system card](model-card-system-card.md))
- Reproducibility expectations that do not account for routing variability ([determinism vs probabilism](determinism-vs-probabilism.md))
- Environmental or cost estimates that assume dense compute for a sparse model ([environmental cost of AI](environmental-cost-of-ai.md))
- A provider changing architecture between versions with no notice, altering cost and latency behavior ([model version and update](model-version-update.md))

**Practice:**
- **State total and active parameters separately, or state that you do not know** — an unqualified parameter count is not a usable figure
- Size infrastructure by memory for total parameters and throughput by active ones; the two budgets are different
- Ask providers for the architecture and record a refusal as a known gap rather than assuming dense
- **Compare models by measured behavior — cost per token, latency, evaluation results — rather than by size**, which is the durable fix for all of this ([evaluation](evaluation.md))
- Avoid "expert" in explanations for non-technical audiences, or say plainly that the term is architectural
- Re-measure cost and latency after a model version change, since architecture may have changed underneath ([model version and update](model-version-update.md))

**Key accountability owner:** whoever signs off model selection or capacity planning — because both decisions usually rest on a size figure, and for a sparse model that figure means two different things depending on which one was quoted.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the architecture and its consequences, medium on what any specific deployed model does.** The mechanism, the founding work and the scaling results are peer-reviewed and uncontroversial, and the compute/memory asymmetry follows directly from how the architecture works. **What is uncertain is application to particular models**, because frontier providers often do not disclose whether a model is sparse, how many experts it has, or how many are active — so the reader's own systems may be affected in ways they cannot confirm. Widely circulated parameter counts for closed models are frequently unattributed, and this entry deliberately cites none. **The routing-variability point is implementation-dependent** — it follows from batch-dependent routing in common implementations rather than from the architecture as such, and is stated here as a known mechanism rather than a universal property.

---

## Related concepts

- [Transformers](transformers.md) — the architecture MoE layers are usually inserted into
- [Small Language Models (SLMs)](small-language-models.md) — the other answer to the capability-for-resources trade
- [Inference](inference.md) — where the compute saving is actually realized
- [Latency (AI Systems)](latency-ai-systems.md) — what active parameter count affects per request
- [Local LLMs](local-llms.md) — where memory rather than compute is the binding constraint
- [Edge AI](edge-ai.md) — the deployment context sparsity does not help
- [Model Card / System Card](model-card-system-card.md) — where architecture should be disclosed and often is not
- [AI Benchmarking](ai-benchmarking.md) — comparisons that quietly assume parameter counts are comparable
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — routing as a source of output variability
- [Environmental Cost of AI](environmental-cost-of-ai.md) — why compute estimates need the active count

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-305 | Jacobs, Robert A.; Jordan, Michael I.; Nowlan, Steven J.; Hinton, Geoffrey E. — *Adaptive Mixtures of Local Experts* (Neural Computation 3(1), pp. 79–87, 1991) · [link](https://doi.org/10.1162/neco.1991.3.1.79) | The founding paper and the origin of the term: parallel sub-networks with a gating function allocating inputs among them. Establishes the concept's age and that it long predates its use in language models. |
| SRC-306 | Shazeer, Noam; Mirhoseini, Azalia; Maziarz, Krzysztof; Davis, Andy; Le, Quoc; Hinton, Geoffrey; Dean, Jeff (Google Brain) — *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer* (2017) · [link](https://arxiv.org/abs/1701.06538) | The result this entry's economics rest on: a network's capacity is bounded by parameter count while the cost of using it need not be, so **conditional computation raises capacity without a proportional increase in computation**. The basis for separating total from active parameters. |
| SRC-307 | Fedus, William; Zoph, Barret; Shazeer, Noam (Google) — *Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity* (2021) · [link](https://arxiv.org/abs/2101.03961) | Routing simplified to a single expert per token, reaching trillion-parameter scale at **constant computational cost per token** — the clearest demonstration that total size and per-request cost have come apart. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (2017) · [link](https://arxiv.org/abs/1706.03762) | The architecture MoE layers are inserted into, needed to state where the substitution happens rather than describing MoE as a separate kind of model. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Size memory by total parameters and throughput by active ones. They are different budgets and conflating them defeats capacity plans. |
| **Organizational** | Any model comparison resting on parameter count is ambiguous unless it says which count. Compare measured behavior instead. |
| **Client-facing** | Explains how a model can be enormous and still fast, without implying it is cheap to host. |
| **LLM-native** | "Experts" are not specialists — routing is learned and not human-meaningful. And sparsity buys compute, never memory. |

---

*Last updated: v1.0 · September 2026*
