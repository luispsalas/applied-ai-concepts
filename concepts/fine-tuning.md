<!--meta
category: Foundations
short: Adapting a model on your own data — cheap enough to be routine, and it can silently strip the safety behavior you were relying on
aliases: [LoRA, PEFT, parameter-efficient fine-tuning, adapting a model, custom model, training on our own data, domain adaptation]
tags: [Architecture, Data Governance, Security]
-->
# Fine-tuning

## One-line essence
Adapting a pre-trained model to a specific domain or task by training it further on targeted data — between prompting and building from scratch in cost, control, and risk.

---

## Technical definition

Continued training of an existing model on a smaller, targeted dataset, to specialize behavior, tone, format, or domain knowledge. It sits between [prompting](prompt-engineering.md), which changes nothing about the model, and pre-training, which almost nobody does.

**It became routine because it became cheap.** Parameter-efficient methods freeze the original weights and train small added matrices instead — reducing trainable parameters by up to **10,000×** versus full fine-tuning of a 175B model, cutting GPU memory roughly threefold, matching full fine-tuning on quality, and adding **no inference latency**. Adaptation moved from a capital project to something a team does in an afternoon.

**The governance consequence of that is the entry's first point:** the number of modified models inside an organization went up sharply, and no corresponding governance step was invented. A fine-tuned model is a **new model** — with its own behavior, its own evaluation status, and its own [provenance](data-provenance-lineage.md) — but it inherits the base model's documentation, which no longer describes it.

**And it silently degrades safety.** This is the finding that should change practice:

- **Adversarially:** safety alignment was stripped from a production model with **10 malicious training examples, for under $0.20.**
- **Benignly, which matters far more:** *"simply fine-tuning with benign and commonly used datasets can also inadvertently degrade the safety alignment of LLMs."*

**A team fine-tuning on ordinary internal data has changed the model's refusal behavior and has no reason to suspect it.** Nothing announces it. The provider's safety evaluation describes a model you are no longer running.

**What fine-tuning is and is not good for.** It reliably teaches *form* — tone, format, structure, task pattern, domain vocabulary. It is a poor and expensive way to teach *facts*, which go stale and cannot be corrected without retraining; [retrieval](rag.md) handles those better and keeps them auditable. The common failure is reaching for fine-tuning to inject knowledge that belonged in a [knowledge base](knowledge-base.md).

---

## Plain-language version

Fine-tuning means taking a model someone else built and training it a bit more on your own examples, so it does your particular job better — your tone, your format, your kind of task.

It used to be expensive. New techniques made it cheap enough that a small team can do it in an afternoon, which is mostly good and has one consequence nobody planned for: organizations now have modified models scattered around, and none of the paperwork describing the original model still describes them.

There is a sharper problem. Researchers found that fine-tuning can remove a model's safety training — deliberately, with about ten bad examples for pennies, but also **accidentally, using perfectly ordinary business data.** Not as badly, but measurably.

That is the part worth remembering. You are not warned. The model still looks like the one you approved, the vendor's safety documentation still exists, and the thing you are actually running has quietly become more willing to do things it used to refuse.

---

## AI literacy notes

1. **A fine-tuned model is a new model.** New behavior, new evaluation status, new provenance. It should not inherit the base model's approval by default.
2. **Safety degrades from benign data, not just malicious data.** This is the finding most people miss. Ordinary internal training data measurably weakens refusal behavior.
3. **Nothing tells you it happened.** No error, no warning, no metric. The only way to know is to test the fine-tuned model, not the base one.
4. **Good for form, poor for facts.** Tone, format and task pattern stick well. Knowledge goes stale and cannot be edited — [retrieval](rag.md) is the better tool and leaves an auditable trail.
5. **Cheap changed the governance problem, not just the cost.** When adaptation took a quarter and a budget line, it got reviewed. At an afternoon and a credit card, it does not.
6. **The training set is now yours.** Its licensing, personal data and provenance are your responsibility — this is the one training corpus you actually control, and the one most often undocumented.
7. **The vendor's model card no longer applies.** You created something they have not documented, evaluated, or made claims about ([model card](model-card-system-card.md)).

---

## Governance notes

**Core question:** Which models in your organization have been modified — and has anyone re-run the safety evaluation on the result rather than the base?

**Watch for:**
- Fine-tuned models inheriting the base model's approval, documentation and risk classification
- **Safety evaluation performed on the base model only**, which is the specific gap this entry exists to close
- No inventory of adapted models; cheap adaptation plus no procurement event is [Shadow AI](shadow-ai.md) with an internal face
- Adaptation datasets undocumented — the one corpus you control, and typically the one with no provenance record ([data provenance](data-provenance-lineage.md))
- Fine-tuning used to inject facts that change, producing a model that is confidently out of date with no way to correct it
- Personal data in a training set, absorbed rather than stored, with no path for a deletion request ([privacy](privacy-ai-systems.md))
- Adapter weights treated as a build artifact rather than as a governed model version

**Practice:**
- **Re-run the safety evaluation on the fine-tuned model, always, including when the training data was benign** — the evidence says benign data is enough to degrade it
- Register each adapted model as a distinct system with its own owner, version and evaluation record
- Write a [system card](model-card-system-card.md) for it — the base model's card describes something else now
- Document the adaptation set at intake: origin, licensing, personal data, consent. Do the provenance check *before* training, since it cannot be undone afterwards
- Prefer retrieval for knowledge and fine-tuning for behavior; state which problem you are solving before choosing
- Keep base-model version and adapter version together, since a base update invalidates the adapter's evaluation
- Give the capability an approval path cheap enough that people use it, or it will happen unrecorded

**Key accountability owner:** whoever fine-tunes becomes the model owner — not the provider, and not the person who approved the base model. That transfer is the thing to make explicit, because it happens by default and is almost never stated.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the safety finding, medium on the practice.** The safety-degradation result is peer-reviewed (ICLR 2024), widely replicated, and the benign-data half is the load-bearing part. Parameter-efficiency claims are peer-reviewed and uncontested. **Limits:** the ease-of-attack figures describe 2023-era models and providers have since added fine-tuning-time moderation, so *how easily* should not be quoted as current — the direction is what transfers. Method choice (LoRA, QLoRA, full fine-tuning, adapters) moves fast and this entry deliberately does not recommend one. And the fine-tuning-versus-retrieval guidance is convergent practitioner experience rather than comparative study.

---

## Related concepts

- [Training Data](training-data.md) — the pre-training corpus this sits on top of, and the provenance duties that carry over
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — the other post-training stage, and the safety behavior fine-tuning can undo
- [Retrieval-Augmented Generation (RAG)](rag.md) — the better tool for knowledge, and auditable in a way weights are not
- [Model Card / System Card](model-card-system-card.md) — what a fine-tuned model needs and does not inherit
- [Data Provenance / Lineage](data-provenance-lineage.md) — the adaptation set is a governed dataset
- [Evaluation (AI Systems)](evaluation.md) — must be re-run on the adapted model, not the base
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the external layer that still holds when trained-in safety weakens
- [Shadow AI](shadow-ai.md) — cheap adaptation with no procurement event
- [Small Language Models (SLMs)](small-language-models.md) — where fine-tuning most often pays off
- [Local LLMs](local-llms.md) — adaptation is usually why organizations self-host
- [Privacy (AI Systems)](privacy-ai-systems.md) — personal data absorbed into weights cannot be selectively deleted
- [Model Version & Update](model-version-update.md) — a base update invalidates the adapter's evaluation
- [Ownership (AI Systems)](ownership-ai-systems.md) — fine-tuning transfers model ownership, usually silently

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-216 | Qi, X.; Zeng, Y.; Xie, T.; Chen, P.-Y.; Jia, R.; Mittal, P.; Henderson, P. — *Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.03693) | The core finding: safety stripped with 10 adversarial examples for under $0.20, **and** degraded by benign, commonly used datasets — the reason evaluation must be re-run on the adapted model. |
| SRC-215 | Hu, E.J.; Shen, Y.; Wallis, P.; Allen-Zhu, Z.; Li, Y.; Wang, S.; Wang, L.; Chen, W. (Microsoft) — *LoRA: Low-Rank Adaptation of Large Language Models* (ICLR, 2022) · [link](https://arxiv.org/abs/2106.09685) | Why adaptation became routine: up to 10,000× fewer trainable parameters, 3× less memory, quality on par with full fine-tuning, no added inference latency. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Where fine-tuning sits between pre-training and prompting in the model lifecycle. |
| SRC-197 | European Parliament / Council of the EU — *EU AI Act, Article 10: Data and data governance* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding duties that attach to a training set — origin, preparation, bias examination — which apply to your adaptation data. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | Why the licensing of an assembled fine-tuning set is rarely as clear as assumed. |
| SRC-150 | Carlini, N.; Tramer, F.; Wallace, E.; Jagielski, M. et al. — *Extracting Training Data from Large Language Models* (2021) · [link](https://arxiv.org/abs/2012.07805) | That absorbed data can resurface — the reason personal data in an adaptation set is a disclosure risk, not just a compliance one. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Re-run safety evaluation on the fine-tuned model every time, including after benign training data. Use fine-tuning for form and retrieval for facts. |
| **Organizational** | A fine-tuned model is a new model with a new owner — the team that adapted it, not the provider. Cheap adaptation without an approval path produces unrecorded models. |
| **Client-facing** | Explains why a customized model needs its own review rather than inheriting the base model's assurances. |
| **LLM-native** | Benign data degrades safety alignment measurably and silently. The vendor's evaluation describes a model you are no longer running. |

---

*Last updated: v1.0 · September 2026*
