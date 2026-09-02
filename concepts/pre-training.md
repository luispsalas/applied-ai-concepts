<!--meta
category: Foundations
short: The first and largest training stage, where a model learns language and world knowledge from a huge corpus — the stage that fixes what it knows and that nobody can undo afterwards
aliases: [pretraining, pre-trained model, base model, foundation model training, how models are trained, where knowledge comes from, scaling laws, Chinchilla]
tags: [AI Literacy, Data Governance]
established: established
-->
# Pre-training

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The first and by far the largest training stage, in which a model learns language, facts and reasoning patterns by predicting text across a vast corpus — establishing everything it knows before any adaptation, and doing so irreversibly.

---

## Technical definition

Pre-training is **self-supervised learning at scale**: the model is repeatedly shown text and asked to predict the next [token](tokenization.md), with the correct answer being the text itself. No labels are required, which is what allows the corpus to be enormous.

The output is a **base model** — one with broad capability and no particular manners. It can continue text; it is not yet an assistant. Instruction-following, tone, refusals and helpfulness come from later, far smaller stages ([fine-tuning](fine-tuning.md), [RLHF](rlhf.md)). The proportions matter: **capability is overwhelmingly a product of this stage; behavior is largely a product of the ones after it.**

Bommasani et al. (2021) named the resulting artifact a **foundation model** — trained on broad data at scale and adaptable to many downstream tasks — and identified the governance property that follows. Because a great many systems are built by adapting the same few base models, **defects, biases and blind spots are inherited rather than isolated**. The authors call this homogenization: a single flaw at this stage propagates into everything downstream.

**The scaling result that reset industry practice.** Hoffmann et al. (2022) trained *"over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens"* and concluded that *"current large language models are significantly undertrained"* — the field had been buying parameters when it should have been buying data. Their rule: *"for every doubling of model size the number of training tokens should also be doubled."* The demonstration was Chinchilla — **70B parameters and 4× more data** at the same compute budget as the much larger Gopher — reaching *"a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher."*

The governance consequence is not usually drawn, and should be: **compute-optimal training makes data the binding constraint.** A finding that better models need proportionally more text is what turns corpus acquisition — its provenance, licensing and consent — into a competitive pressure rather than a compliance afterthought. See [Training Data](training-data.md) and [Copyright & AI Output](copyright-ai-output.md).

**This stage is effectively irreversible.** It costs enormous compute, happens once, and cannot be selectively undone: there is no operation that removes one document's influence from a finished model. Later stages can suppress a behavior; they do not delete what was learned. Everything about a model's [knowledge cutoff](knowledge-cutoff.md), its factual coverage, and the associations it carries is fixed here.

---

## Plain-language version

Before an AI model can be helpful, it spends months reading. It is shown staggering quantities of text and given one repetitive exercise: guess what comes next. Correct itself. Repeat, trillions of times.

Nobody labels any of it, which is exactly why the amount can be so large. And from that one exercise, done at enough scale, the model picks up grammar, facts, styles, and a good deal of reasoning.

What comes out is a **base model** — knowledgeable and rather useless. It continues text; it does not answer questions or decline harmful requests. That behavior gets added afterwards, in much smaller training stages. Worth separating: nearly all of what a model *knows* comes from this first stage, while most of how it *behaves* comes from the later ones.

Two consequences do most of the work in practice.

**It cannot be undone.** There is no way to reach into a finished model and remove the influence of one document. Later training can teach it not to say something. It cannot make it not have learned it. That is why the cutoff date is fixed, and why "just remove that from the model" is not a thing anyone can do.

**Everyone inherits the same starting point.** Most AI products are adaptations of a handful of base models, so a flaw in one is not one product's problem — it is quietly present in everything built on top.

---

## AI literacy notes

1. **Capability comes from here; behavior mostly does not.** A model's knowledge is a pre-training property. Its helpfulness, tone and refusals are later, thinner layers.
2. **A base model is not an assistant.** Without the later stages it continues text rather than answering.
3. **It cannot be selectively undone.** No operation removes one document's contribution. Suppression is not deletion — the distinction matters for any deletion or takedown request.
4. **The [knowledge cutoff](knowledge-cutoff.md) is a consequence of this stage**, not a policy choice about what to serve.
5. **More data, not just more parameters.** Compute-optimal training scales tokens with model size — which is why corpus acquisition became a strategic and legal issue.
6. **Parameter count is a poor proxy for capability.** A well-trained smaller model can beat a larger undertrained one, which is the entire Chinchilla result.
7. **Homogenization concentrates risk.** Many products, few base models: a defect at this stage is systemic rather than local ([systemic risk](systemic-risk-ai.md)).
8. **Fine-tuning cannot add a missing foundation.** If the base model never learned a domain, later stages adapt style far more readily than they add knowledge.

---

## Governance notes

**Core question:** For the base model underneath our system, what was it trained on, under what rights, and what can we actually do if something in there turns out to be a problem?

**Watch for:**
- Deletion, takedown or erasure obligations answered with output filtering, on the assumption the model can be made to un-learn ([data minimization](data-minimization.md))
- Base-model provenance unexamined because the vendor relationship is with an API, not a corpus ([data provenance](data-provenance-lineage.md))
- Training-corpus rights treated as the vendor's problem alone, without checking where deployer liability actually sits ([copyright](copyright-ai-output.md))
- Multiple internal systems assumed to be independently sourced when they adapt the same base model — correlated failure presented as diversity ([systemic risk](systemic-risk-ai.md))
- Bias remediation planned entirely at the [guardrail](guardrails-ai-systems.md) layer, with no acknowledgment that the origin is upstream and permanent
- Knowledge-cutoff limitations described as a temporary gap rather than a fixed property of the artifact
- Model selection made on parameter count as if it indexed capability
- No [model card](model-card-system-card.md) or equivalent disclosure of training data composition, and no request for one

**Practice:**
- **Ask for training-data composition and rights basis at procurement**, and record the answer — including when the answer is that the vendor will not say, which is itself a finding
- Design erasure and takedown paths on the assumption that **the model cannot forget**: hold the controllable copies (retrieval corpora, logs, [vector stores](embeddings.md)) where deletion genuinely works
- Map which of your systems share a base model, and treat that overlap as correlated risk rather than as redundancy
- Locate bias and safety controls with honest expectations: upstream origin, downstream mitigation, no pretense that the latter reaches the former
- Track the base model's identity and version as a system dependency ([model version & update](model-version-update.md))
- Evaluate candidate models on your own tasks rather than on size or benchmark headline

**Key accountability owner:** whoever owns vendor and third-party risk for the system — because pre-training decisions are made entirely outside the deploying organization, and the only available control point is the procurement and disclosure relationship.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the mechanism, the lifecycle position, and the irreversibility, all of which are uncontested and well documented. **High but time-bound on the scaling guidance:** the Chinchilla result is a rigorous, large-scale empirical study, and its qualitative lesson — that data scales with model size and that undertraining was widespread — has held. The specific ratios have not: subsequent practice routinely trains far past the compute-optimal point because inference cost, not training cost, dominates in deployment. **Treat the token-doubling rule as the finding that corrected the field, not as current practice**, and note that the frontier-scale numbers are no longer publicly verifiable — leading labs have stopped disclosing corpus size and composition, so claims about what current models were trained on are increasingly unauditable.

---

## Related concepts

- [Training Data](training-data.md) — the corpus consumed at this stage, and the provenance duties attached to it
- [Large Language Models (LLMs)](large-language-models.md) — the artifact this stage produces
- [Fine-tuning](fine-tuning.md) — the adaptation stage that sits on top of this one
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — where assistant behavior is added, separately from knowledge
- [Knowledge Cutoff](knowledge-cutoff.md) — a direct consequence of when this stage ended
- [Tokenization](tokenization.md) — the units predicted here, and the vocabulary learned from this corpus
- [Embeddings](embeddings.md) — the representations formed during this stage, carrying its associations
- [Copyright & AI Output](copyright-ai-output.md) — the rights question that compute-optimal scaling made unavoidable
- [Data Provenance & Lineage](data-provenance-lineage.md) — the asymmetry: training absorbs, retrieval references
- [Systemic Risk (AI)](systemic-risk-ai.md) — homogenization, and why a single base-model defect is not a local one
- [Small Language Models (SLMs)](small-language-models.md) — the case that well-trained small beats undertrained large
- [Frontier AI (Frontier Model)](frontier-ai.md) — where the scale, cost and disclosure questions concentrate
- [Model Card / System Card](model-card-system-card.md) — the disclosure artifact where corpus composition should appear

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-228 | Hoffmann, J.; Borgeaud, S.; Mensch, A.; Buchatskaya, E.; Cai, T.; Rutherford, E. et al. (DeepMind) — *Training Compute-Optimal Large Language Models* (2022) · [link](https://arxiv.org/abs/2203.15556) | The compute-optimal scaling result from 400+ models: token count should double with model size; current LLMs are "significantly undertrained"; Chinchilla (70B, 4× data) beat Gopher at equal compute, 67.5% MMLU, >7% improvement. |
| SRC-143 | Bommasani, R. et al. (Stanford CRFM / HAI) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | Names the artifact and its governance property: broad-data training adaptable to many tasks, with homogenization meaning defects are inherited by everything built downstream. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | The standard lifecycle framing — pre-training then adaptation — and the self-supervised next-token objective as the prevailing pre-training method. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (2017) · [link](https://arxiv.org/abs/1706.03762) | The architecture that made pre-training at this scale tractable, and on which the scaling studies were run. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Fine-tuning adapts style far more readily than it adds knowledge. Evaluate candidate base models on your own tasks; parameter count does not index capability. |
| **Organizational** | Ask for training-data composition and rights basis at procurement and record the answer. Build erasure paths on the assumption the model cannot forget, and map which systems share a base model. |
| **Client-facing** | Explains why a model's knowledge stops at a date, why it cannot be made to un-learn something, and why capability and good manners come from different places. |
| **LLM-native** | Capability is pre-training; behavior is the thin layers after it. The stage is irreversible, increasingly undisclosed, and shared across the industry — which is what makes one defect systemic. |

---

*Last updated: v1.0 · September 2026*
