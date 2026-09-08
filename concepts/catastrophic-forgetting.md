<!--meta
category: Reliability & Quality
short: Teaching a model something new can silently remove something it already knew — including behavior nobody re-tests
aliases: [catastrophic interference, forgetting, continual learning, stability-plasticity dilemma, why did fine-tuning break something else, capability regression]
tags: [Model Behavior, Evaluation, Safety]
established: established
-->
# Catastrophic Forgetting

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator, named in the peer-reviewed literature since 1989.

## One-line essence
The tendency of neural networks to lose previously learned knowledge when trained on new data — a key constraint in continual learning and fine-tuning.

---

## Technical definition

Catastrophic forgetting is the abrupt loss of previously learned capability when a neural network is trained on new data. McCloskey and Cohen named it *catastrophic interference* in 1989, showing that sequential training on one task then another did not accumulate both — the second overwrote the first.

**The mechanism is that the same weights encode everything.** French frames it as the **stability–plasticity dilemma**: a network's knowledge is distributed across shared parameters rather than filed in separate places, so the plasticity that lets it learn something new is the same property that lets new learning overwrite old. **It is a structural consequence of distributed representation, not a bug in a particular training run** — which is why it recurs across architectures and decades rather than being fixed once.

**Mitigations constrain change rather than prevent it.** Kirkpatrick et al.'s *elastic weight consolidation* slows learning on weights identified as important to previously learned tasks — a principled and effective approach, and still a trade rather than a solution: protecting old capability costs capacity for new.

**It happens in current language models, and scale does not save you.** Luo et al. evaluated continual instruction tuning across models from 1B to 7B parameters and found forgetting **generally observed** in domain knowledge, reasoning and reading comprehension — and, contrary to the comfortable assumption, **severity intensified as model scale increased across that range**. They attribute this to the larger model having more initial performance to lose. They also report two findings worth carrying: the decoder-only model retained more than the encoder-decoder one, and **general instruction tuning beforehand helped alleviate later forgetting**.

**The governance problem is asymmetry of attention.** Fine-tuning is undertaken to add a capability, so the new capability is what gets tested. The capabilities that might have degraded are the ones nobody thought to re-measure — and among them are the model's refusals, tone, and safety behaviors, which were themselves trained in ([RLHF](rlhf.md), [alignment](alignment-ai-systems.md)). **A model can pass its acceptance test for the thing it was changed to do while having quietly lost something it was never re-tested on.**

**Not to be confused with [drift](model-data-drift.md).** Drift is the world changing underneath a fixed model. Forgetting is the model changing while the world stays put — same symptom, opposite cause, and different fix.

---

## Plain-language version

Teach a network something new and it can lose something it already knew. Not gradually — abruptly, and without any warning that it happened.

The reason is that a model does not file its knowledge in separate drawers. Everything is spread across the same set of numbers. The flexibility that lets it learn a new thing is exactly what lets the new thing write over the old one. This was named in 1989 and has never been fully solved, because it is a consequence of how these systems represent anything at all, not a mistake someone made.

There are ways to soften it — techniques that slow down changes to the parts of the model that matter most for what it already knows. They work, and they cost something: protecting the old makes room for less of the new.

Two things are counterintuitive and worth knowing.

**Bigger did not mean safer.** A study across models from one billion to seven billion parameters found that forgetting got *worse* as models got larger, not better — plausibly because a larger model had more to lose in the first place.

**And here is the practical trap.** You fine-tune a model to do a new thing. You test the new thing. It works, so you ship. But nobody re-tested everything else — and "everything else" includes the model's manners: what it refuses to do, how it handles a hostile request, how careful it is. Those behaviors were trained in, and training can take them out. **The test you ran was the test for the thing you changed, not the test for what you might have broken.**

---

## AI literacy notes

1. **It is abrupt, not gradual** — capability can disappear rather than fade.
2. **It is structural**, a consequence of distributed representation, not a defect in one training run.
3. **Mitigations trade capacity, not eliminate the problem** — protecting old learning costs room for new.
4. **Larger was worse, not better**, in the one systematic LLM study across a 1B–7B range.
5. **Safety behavior is learned behavior and can be forgotten** like any other capability.
6. **The new capability gets tested; the old ones do not** — that asymmetry is the actual failure path.
7. **Forgetting is not drift**: the model changed, the world did not.
8. **Prior general instruction tuning reduced later forgetting** in the same study — an ordering effect, not a fix.

---

## Governance notes

**Core question:** After we changed this model, what did we re-test *besides* the thing we changed it to do — and does that list include its refusals?

**Watch for:**
- A fine-tune accepted on a task-specific evaluation alone, with no regression suite ([fine-tuning](fine-tuning.md))
- Safety and refusal behavior never re-measured after training, because it was not the point of the change ([guardrails](guardrails-ai-systems.md), [red teaming](red-teaming.md))
- Sequential fine-tunes stacked over months, each tested only against its own objective
- Post-change degradation diagnosed as drift, sending the investigation in the wrong direction ([model/data drift](model-data-drift.md))
- "It's a bigger model, so it's more robust to this" — the opposite of what the evidence shows in the studied range
- No preserved copy of the pre-change model, so a regression cannot be demonstrated or reversed ([model version and update](model-version-update.md))
- Vendor model updates assumed to be strictly additive, with no re-run of your own acceptance tests
- Evaluation sets built only from the new use case, so the old ones are structurally unrepresented ([evaluation](evaluation.md))

**Practice:**
- **Keep a standing regression suite covering what the model could already do**, and run it on every change — this is the single control that addresses the asymmetry
- **Include safety, refusal and tone cases in that suite explicitly**, since they are learned behaviors and will not re-test themselves
- Retain the previous model version so a regression can be shown, attributed and rolled back ([model version and update](model-version-update.md))
- Prefer approaches that leave weights untouched — retrieval or prompting — when the goal is new *knowledge* rather than new *behavior* ([RAG](rag.md))
- Record what each fine-tune was tested against, so a later failure can be traced to the change that caused it ([audit trail](audit-trail-ai.md))
- Re-run acceptance tests after a provider's model update, not only after your own changes
- Treat a sequence of fine-tunes as cumulative risk, and re-baseline periodically rather than per-step

**Key accountability owner:** whoever approves a model change into production — because the evidence they are shown is almost always about the intended improvement, and the question that goes unasked is what else moved.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the phenomenon, medium on the LLM-scale specifics.** Catastrophic forgetting has been documented since 1989, has a well-understood mechanism, and is uncontroversial across architectures — the concept is as settled as anything in this corpus. **The numbers about current language models rest on a narrower base.** The scale finding cited here (severity increasing from 1B to 7B) comes from a single empirical study over a specific model range and set of tasks; the authors offer an explanation for it, and it should be treated as **one well-conducted observation, not an established scaling law** — in particular it should not be extrapolated above the range tested. The claim this entry makes most confidently is neither of those: it is the governance asymmetry — that a change is tested for its intent and not for its side effects — which follows from ordinary practice rather than from any measurement.

---

## Related concepts

- [Fine-tuning](fine-tuning.md) — the operation that most often causes it
- [Model Version & Update](model-version-update.md) — where a regression becomes attributable and reversible
- [Evaluation (AI Systems)](evaluation.md) — the regression suite is the control that catches this
- [Model/Data Drift](model-data-drift.md) — the same symptom from the opposite cause
- [Overfitting](overfitting.md) — the other way training on new data degrades a model
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — how the behaviors most at risk were trained in
- [Alignment (AI Systems)](alignment-ai-systems.md) — what is being lost when safety behavior degrades
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the external controls that do not forget
- [Retrieval-Augmented Generation (RAG)](rag.md) — adding knowledge without touching weights
- [Training Data](training-data.md) — the sequence in which material is presented matters

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-286 | McCloskey, Michael; Cohen, Neal J. — *Catastrophic Interference in Connectionist Networks: The Sequential Learning Problem* (Psychology of Learning and Motivation, pp. 109–165, 1989) · [link](https://doi.org/10.1016/S0079-7421(08)60536-8) | The originating result and the original name: sequential training on two tasks did not accumulate both, the second overwriting the first. Establishes the term's age and its origin in cognitive science rather than in current ML practice. |
| SRC-287 | French, Robert M. — *Catastrophic forgetting in connectionist networks* (Trends in Cognitive Sciences 3(4), pp. 128–135, 1999) · [link](https://doi.org/10.1016/S1364-6613(99)01294-2) | The **stability–plasticity dilemma** framing this entry's mechanism section rests on: forgetting as a structural consequence of distributed representation over shared weights, rather than a defect to be engineered away. |
| SRC-288 | Kirkpatrick, James; Pascanu, Razvan; Rabinowitz, Neil; Veness, Joel; Desjardins, Guillaume; Rusu, Andrei A. et al. (DeepMind) — *Overcoming catastrophic forgetting in neural networks* (PNAS 114(13), pp. 3521–3526, 2017) · [link](https://doi.org/10.1073/pnas.1611835114) | Elastic weight consolidation — slowing learning on weights important to earlier tasks — as the canonical mitigation, and the basis for this entry's characterization of mitigations as trades rather than solutions. |
| SRC-289 | Luo, Yun; Yang, Zhen; Meng, Fandong; Li, Yafu; Zhou, Jie; Zhang, Yue — *An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning* (2023) · [link](https://arxiv.org/abs/2308.08747) | The current-model evidence: forgetting **generally observed** from 1B to 7B parameters across domain knowledge, reasoning and reading comprehension, with **severity intensifying as scale increased** in that range; decoder-only retaining more than encoder–decoder; and prior general instruction tuning alleviating later forgetting. ⚠️ A single study over a specific model range — do not extrapolate the scale finding beyond 7B or restate it as a scaling law. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | Establishes that refusal, tone and instruction-following are **trained** behaviors rather than intrinsic ones — which is what makes them forgettable, and is the premise of this entry's central governance point. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Keep a regression suite covering prior capability, including safety cases, and run it on every model change. Retain the previous version so a regression can be shown. |
| **Organizational** | Approval evidence is almost always about the intended improvement. The unasked question — what else moved — is the one that costs you. |
| **Client-facing** | Explains why an improvement in one area can coincide with a decline in another, without implying carelessness. |
| **LLM-native** | Fine-tuning can remove refusals. Bigger was worse, not better, in the range studied. If you only need new knowledge, retrieval leaves the weights alone. |

---

*Last updated: v1.0 · September 2026*
