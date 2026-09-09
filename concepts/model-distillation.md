<!--meta
category: Foundations
short: Training a small model to reproduce a large one's behavior — and the fact that the only thing separating this from model theft is permission
aliases: [knowledge distillation, distillation, distilled model, teacher-student, teacher model, student model, model compression, dark knowledge, distill a model]
tags: [Architecture, Model Behavior, Safety]
established: established
-->
# Model Distillation

> **Term status — Established.** In continuous use across machine learning research and practice since 2015, named in a paper that itself refines a technique published in 2006. Independent of any vendor: the term appears in the documentation and research of every major model provider and in the open-weights ecosystem alike.

## One-line essence
Training a smaller model to reproduce a larger model's behavior — transferring capability at a fraction of the cost, and transferring things nobody intended along with it.

---

## Technical definition

Model distillation trains a **student** model to match the outputs of a larger **teacher** model, rather than training it directly on the original labeled data.

The mechanism is that the teacher's full output distribution carries more information than the correct answer alone. Asked to classify an image of a dog, a teacher does not simply say *dog* — it assigns some small probability to *wolf* and a much smaller one to *car*, and those relative magnitudes encode a learned similarity structure. Hinton, Vinyals and Dean called this the **dark knowledge** that a one-hot label throws away, and showed a student learns faster and generalizes better from the soft distribution than from the hard label. The output distribution is softened by a temperature parameter to make the small probabilities legible ([temperature](temperature-llms.md)).

**The idea predates the name by nine years.** Buciluă, Caruana and Niculescu-Mizil compressed large ensembles into single small models in 2006, training the small model on the ensemble's outputs. Distillation refined and named a technique rather than inventing one — worth stating because the 2015 paper is routinely cited as the origin of the *idea* rather than of the *term*.

**The trade is real and is usually quoted from one result.** DistilBERT reports a **40% reduction in size, 97% of language-understanding capability retained, and 60% faster** inference. That figure is worth quoting accurately: **97% is measured on language-understanding benchmarks**, not on everything a model does ([AI benchmarking](ai-benchmarking.md)).

**Distillation and model extraction are the same technique under different permissions.** Querying a model you do not own and training on its responses is how a distillation dataset is built; it is also how a [model extraction attack](privacy-attacks-ai-models.md) works. Nothing in the method distinguishes them. **The distinction is entirely contractual** — which is why provider terms of service address it explicitly ([acceptable use policy](acceptable-use-policy.md)), and why "was this distilled from a model we are not licensed to distill from" is a supply-chain question and not a technical one ([supply chain risk](supply-chain-risk-ai.md)).

**Safety properties do not reliably survive the transfer, and vulnerabilities do.** Angell, Brinkmann and He, testing 20 open-weight models against 33 jailbreak attacks, find that jailbreak transferability tracks representational similarity between models — and demonstrate the causal direction by showing that **deliberately increasing similarity through distillation on benign data alone increases transfer**. A student trained only on harmless teacher outputs inherits the teacher's attack surface ([jailbreak](jailbreak.md)).

**And the finished model does not disclose its own provenance.** A set of weights carries no record of what it was distilled from. Whatever is known about the teacher's training data, evaluations and limitations does not travel with the student unless someone writes it down ([model card / system card](model-card-system-card.md), [data provenance and lineage](data-provenance-lineage.md)).

---

## Plain-language version

A big model is expensive to run. So you use it as a teacher: you ask it a great many questions, record its answers, and train a small model to give the same answers. The small model ends up doing much of what the big one did, for a fraction of the cost. That is distillation, and it is why capable models can run on a phone.

The trick that makes it work better than it should is subtle. **You don't just train the student on the right answer — you train it on how the teacher spread its uncertainty.** A teacher shown a photo of a dog doesn't just say "dog"; it says "mostly dog, slightly wolf, definitely not car." That ranking of wrong answers is information about how the world is shaped, and the student learns from it. The right answer alone would have thrown it away.

Three things follow, and they are the reasons this is a governance topic and not just an engineering one.

**First: the technique is identical to stealing a model.** If you query someone else's model and train your own on the answers, what you have done is distillation if you were permitted and extraction if you were not. There is no technical difference to detect. The line is drawn by a contract, which means the question "where did this model's capability come from" cannot be answered by inspecting the model.

**Second: the student does not automatically inherit the teacher's safety, but it does inherit the teacher's weaknesses.** Researchers showed that making a student more similar to a teacher — by distilling on entirely harmless material — made attacks that worked on the teacher start working on the student. Nobody transferred anything harmful; the vulnerability came along with the resemblance.

**Third: the small model forgets where it came from.** Nothing in a file of numbers records which model it learned from. Every caveat and known limitation the teacher was documented with is lost unless a person deliberately carries it forward.

---

## AI literacy notes

1. **The student learns from the teacher's uncertainty**, not just its answers — that is what makes distillation work.
2. **The technique is nine years older than the name** — compression of ensembles, 2006; "distillation," 2015.
3. **"Retains 97%" is a benchmark claim**, scoped to what was measured, not a statement about all capability.
4. **Distillation and model extraction are technically identical** — permission is the only difference.
5. **Jailbreaks transfer with similarity**, and distillation deliberately increases similarity.
6. **Safety training is not guaranteed to transfer** even though vulnerabilities demonstrably do.
7. **A distilled model carries no record of its teacher** — provenance must be written down or it is gone.
8. **Cheaper inference is the point**, and it is a real environmental and cost lever ([environmental cost](environmental-cost-of-ai.md)).
9. **Distilling someone's model and shipping it under your name makes you the provider** of the result, with the obligations that follow.

---

## Governance notes

**Core question:** For every model in use here, do we know what it was distilled from, were we permitted to do it, and what did we verify about the student that we cannot simply inherit from the teacher?

**Watch for:**
- A capability claim about a small model inherited from the teacher's evaluations rather than measured on the student ([evaluation](evaluation.md))
- "Retains 97% of performance" repeated without the benchmark it was measured on ([AI benchmarking](ai-benchmarking.md))
- Distillation from a third-party API where the provider's terms prohibit it ([acceptable use policy](acceptable-use-policy.md))
- An acquired or open-weight model whose teacher is unknown and undocumented ([supply chain risk](supply-chain-risk-ai.md))
- Safety evaluation skipped for the student on the grounds that the teacher was aligned ([alignment](alignment-ai-systems.md))
- Red-teaming results carried over from teacher to student without re-testing ([red teaming](red-teaming.md))
- A distilled model shipped under your own name with no assessment of what obligations that creates ([compliance](compliance-ai-systems.md))
- Cost savings reported without the accompanying capability loss on the tasks that actually matter

**Practice:**
- **Record the teacher in the student's documentation** — model, version, access date, and the terms under which its outputs were used ([model card / system card](model-card-system-card.md))
- **Evaluate the student independently**, on your own tasks; teacher results are not evidence about the student
- **Re-run safety and jailbreak testing on the student specifically** — the research finding is that attacks transfer with similarity, and distillation maximizes similarity ([red teaming](red-teaming.md))
- Check the teacher's terms of service before building a distillation set, and record the check
- **Ask a supplier what their model was distilled from, and treat a non-answer as a finding** ([supply chain risk](supply-chain-risk-ai.md))
- State the capability loss in the terms your organization cares about, not in benchmark points
- Where the student is deployed at the edge or on-device, account for the fact that it can no longer be patched centrally ([edge AI](edge-ai.md), [local LLMs](local-llms.md))

**Key accountability owner:** whoever puts the distilled model into use under the organization's name — because both the licensing exposure and the untested-student risk attach to the deploying party, not to whoever ran the training job.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, moderate on the transfer claims.** Distillation itself is uncontroversial, well replicated, and in production use everywhere; the 2006 antecedent and the 2015 naming are both documented in the literature's own citations. **The jailbreak-transfer finding is more recent and more scoped**: it is a controlled causal experiment across 20 open-weight models, but frontier closed models were not tested, and the result is about attacks transferring — **it is not a general claim that no safety property survives distillation**, and this entry does not make one. The DistilBERT figures are quoted from the paper's own abstract and are scoped to the benchmarks it used. **The licensing point is stated as a structural fact about the technique**, not as legal advice; whether any particular distillation is permitted depends on terms this entry cannot read.

---

## Related concepts

- [Small Language Models](small-language-models.md) — frequently what distillation produces
- [Inference](inference.md) — the cost distillation exists to reduce
- [Fine-Tuning](fine-tuning.md) — adapting a model, as distinct from compressing one
- [Pre-Training](pre-training.md) — where the teacher's capability came from
- [Edge AI](edge-ai.md) — deployment made possible by a smaller model
- [Local LLMs](local-llms.md) — running the result yourself
- [Environmental Cost of AI](environmental-cost-of-ai.md) — the resource case for a smaller model
- [Privacy Attacks on AI Models](privacy-attacks-ai-models.md) — model extraction, the same technique without permission
- [Jailbreak](jailbreak.md) — what transfers along with representational similarity
- [Acceptable Use Policy](acceptable-use-policy.md) — where provider terms address distillation
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — an acquired model with an unknown teacher
- [Model Card / System Card](model-card-system-card.md) — where the teacher should be recorded
- [Frontier AI](frontier-ai.md) — the models most worth distilling from
- [Mixture of Experts](mixture-of-experts.md) — a different route to cheaper inference

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-315 | Hinton, Geoffrey; Vinyals, Oriol; Dean, Jeff (Google) — *Distilling the Knowledge in a Neural Network* (NIPS 2014 Deep Learning Workshop, 2015) · [link](https://arxiv.org/abs/1503.02531) | The originating paper for the term and the method: training the student on the teacher's full softened output distribution rather than on hard labels, so it learns the relative confidences a one-hot label discards. ⚠️ A workshop paper; its results are on 2014-era vision and speech models, so the method transfers to language models but the numbers do not. |
| SRC-316 | Buciluǎ, Cristian; Caruana, Rich; Niculescu-Mizil, Alexandru (Cornell University) — *Model compression* (KDD, 2006) · [link](https://doi.org/10.1145/1150402.1150464) | The antecedent, cited so this entry credits the idea to the right decade: compressing an ensemble into a small model trained on the ensemble's outputs, nine years before the technique was named. ⚠️ Pre-deep-learning — cite for priority of the idea, never for a result about current models. |
| SRC-317 | Sanh, Victor; Debut, Lysandre; Chaumond, Julien; Wolf, Thomas (Hugging Face) — *DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter* (NeurIPS EMC² Workshop, 2019) · [link](https://arxiv.org/abs/1910.01108) | The concrete trade, quoted from the abstract: **40% smaller, 97% of language-understanding capability retained, 60% faster.** ⚠️ Vendor-adjacent, and the 97% is measured on language-understanding benchmarks — it is not a claim about generative or reasoning capability. |
| SRC-318 | Angell, Rico; Brinkmann, Jannik; He, He — *Jailbreak Transferability Emerges from Shared Representations* (arXiv, June 2025) · [link](https://arxiv.org/abs/2506.12913) | The safety-inheritance evidence, across 20 open-weight models and 33 attacks: transferability tracks representational similarity, and **increasing similarity through benign-only distillation causally increases transfer.** ⚠️ Open-weight models only; the claim is about attacks transferring, not about all safety properties. |
| SRC-301 | European Parliament / Council of the EU — *EU AI Act, Article 25: Responsibilities along the AI value chain* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The provision that makes distillation a compliance event and not only an engineering one: putting a model on the market under your own name places the provider's obligations on you, regardless of who trained the teacher. |
| SRC-294 | Tramèr, Florian; Zhang, Fan; Juels, Ari; Reiter, Michael K.; Ristenpart, Thomas — *Stealing Machine Learning Models via Prediction APIs* (USENIX Security, 2016) · [link](https://arxiv.org/abs/1609.02943) | Establishes model extraction through query access as a practical attack — the same procedure as distillation, which is what makes permission rather than technique the distinguishing feature. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Evaluate the student on your own tasks and re-run safety testing on it; teacher results are not evidence about the student. |
| **Organizational** | Distillation is how capability is acquired cheaply, and how it is acquired without permission. The difference is a contract, not a technical control. |
| **Client-facing** | Explains how a small, cheap model can behave like an expensive one — and why "it's based on a big model" is not a quality guarantee. |
| **LLM-native** | The student inherits the teacher's attack surface along with its behavior. Increasing similarity is the point of distillation and the mechanism of jailbreak transfer. |

---

*Last updated: v1.0 · September 2026*
