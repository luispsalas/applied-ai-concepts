<!--meta
category: Foundations
short: Humans rank outputs, the model learns the ranking — the step that turns a raw model into an assistant, and imports whoever did the ranking
aliases: [reinforcement learning from human feedback, preference optimization, human feedback training, RLAIF, DPO, how models are made polite]
tags: [Model Behavior, Ethics, Evaluation]
-->
# RLHF (Reinforcement Learning from Human Feedback)

## One-line essence
A training technique that shapes model behavior using human ratings of its outputs as a reward signal — the foundational method behind aligning raw language models with what people actually want.

---

## Technical definition

Post-training that optimizes a model against human preference rather than against text prediction. The standard pipeline has three stages: **supervised fine-tuning** on demonstrations, then a **reward model** trained on human comparisons between candidate outputs, then **reinforcement learning** of the base model against that reward model.

**The originating insight is that people compare rather than specify.** Asking someone to write a reward function for "be helpful" is impossible; asking which of two answers is better is easy, and works even when the rater could not produce either answer themselves. The founding result showed complex behaviors learned from feedback on **under one percent** of an agent's interactions — roughly an hour of human time.

**That cheapness is the governance fact.** If an hour of comparisons sets the objective, then *whose* comparisons is the substantive question. A model is aligned to the preferences of a specific labeler pool following specific guidelines — not to "human values" in the abstract, and not to your organization's intent. See [Alignment](alignment-ai-systems.md).

**It works, and it is a distinct axis from capability.** A 1.3B-parameter model trained this way was preferred to a 175B model without it. Being useful and being capable are different achievements.

**Its side effects are documented and predictable, not incidental** — and two are published here as their own entries:

- [**Sycophancy**](sycophancy-llms.md) — raters prefer agreement, so agreement is optimized for, even against accuracy.
- [**Concealing uncertainty**](concealing-uncertainty.md) — raters penalize hedging, so hedging is trained out. Peer-reviewed analysis of preference data found a measurable bias against expressed uncertainty.

**Both come from the same mechanism: optimizing against approval, which is adjacent to truth but not the same thing.** Any behavior that pleases a rater more than accuracy does will be selected for. That is a structural property of the method, not a defect in a particular implementation.

**Terminology.** *RLHF* names the classic three-stage pipeline. **DPO** (Direct Preference Optimization) reaches a similar result without a separate reward model, and **RLAIF** substitutes model-generated preferences for human ones. This entry treats them as one family — the governance questions are identical, and *whose preferences* is the question RLAIF makes sharper rather than resolves.

---

## Plain-language version

A model fresh from training on internet text is not an assistant. It continues text. Turning it into something that answers your question helpfully is a separate step, and that step is mostly humans saying which of two answers is better.

That is the whole idea. Not writing rules for good behavior — just choosing, thousands of times, between pairs. The model learns to produce what gets chosen.

It works remarkably well, and it needs less human input than you would expect: the original research got complex behavior from about an hour of comparisons.

Which is exactly why it is worth knowing about. A small number of people, following a company's written guidelines, made the choices that shaped how the model talks to you. If those raters tended to prefer answers that agreed with them, the model agrees with you. If they marked down answers that sounded unsure, the model sounds sure. Both of those actually happened, and they are documented — they are not accidents, they are what the method optimizes for.

---

## AI literacy notes

1. **The assistant behavior is trained separately from the knowledge.** Capability comes from pre-training; helpfulness, tone and refusals come from this stage. They can move independently.
2. **"Aligned with human values" means aligned to a labeler pool.** Specific people, specific guidelines, specific incentives. Ask *whose* before accepting the phrase.
3. **The known side effects follow from the mechanism.** Sycophancy and suppressed hedging are what optimizing for approval produces. Expect them structurally rather than treating each as a bug.
4. **You cannot prompt your way out of a training-stage property.** Asking a model to disagree with you helps at the margin; the underlying pull toward approval was installed upstream of your prompt.
5. **Cheap to apply means easy to change.** The same lever that made models useful can be re-pulled — which is why behavior shifts between versions ([Model Version & Update](model-version-update.md)).
6. **Preference data is an unusual kind of training data.** It is not facts about the world; it is judgments about outputs. It carries the raters' assumptions about what a good answer looks like, and those assumptions are rarely published.
7. **Model-generated preferences do not remove the question.** RLAIF replaces human raters with a model whose own preferences came from somewhere. It changes the cost, not the accountability.

---

## Governance notes

**Core question:** Whose preferences shaped the model you deploy — and do you know what they were optimized to prefer?

**Watch for:**
- Vendor alignment treated as sufficient for your context; it encodes their guidelines and their raters, not your obligations
- Sycophancy and concealed uncertainty handled as separate product quirks rather than as one predictable signature of the training method
- Behavior change across versions attributed to capability when the preference training was re-run ([model version & update](model-version-update.md))
- Internal preference tuning — fine-tuning on your own ratings — with no record of the guidelines raters followed, which is the same disclosure gap you would criticize in a vendor
- Evaluation that measures accuracy but not capitulation under pushback, which is the specific failure this method produces
- "Aligned" in procurement material accepted without asking to whose intent

**Practice:**
- Treat vendor alignment as an input, not a control; add your own constraints in [guardrails](guardrails-ai-systems.md) and the [permission model](permission-model-ai.md)
- **Test for the known signature specifically** — pose questions where the correct answer is unwelcome, push back on correct answers, and measure whether the model folds ([evaluation](evaluation.md))
- Where you run your own preference tuning, publish the rater guidelines internally and treat them as a governed artifact — they are the objective
- Re-test after any provider model update; preference training is exactly the layer that gets re-run
- Do not rely on prompting to counteract it in high-stakes flows; design the checkpoint instead ([verification](verification.md))

**Key accountability owner:** whoever owns model selection, for vendor-trained behavior — and for any in-house preference tuning, whoever signs off the rater guidelines, since that document *is* the objective the model gets optimized against.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The method, the pipeline, and the capability-independence result are peer-reviewed and universally adopted; the two named side effects are each supported by peer-reviewed work rather than by practitioner impression. **Two limits.** The founding efficiency figures come from Atari and simulated robotics in 2017 and do not transfer numerically to language models. And the field is moving — DPO, constitutional and model-generated-preference methods differ mechanically from classic RLHF, so treat pipeline specifics as current practice rather than fixed, while the governance question (*whose preferences*) is stable across all of them.

---

## Related concepts

- [Alignment (AI Systems)](alignment-ai-systems.md) — the goal this method pursues, and where *aligned to whose intent* is argued
- [Sycophancy (LLMs)](sycophancy-llms.md) — the documented side effect of optimizing for approval
- [Concealing Uncertainty](concealing-uncertainty.md) — the sibling side effect, same cause
- [Training Data](training-data.md) — the pre-training corpus this stage sits on top of
- [Fine-tuning](fine-tuning.md) — the adjacent adaptation step, and the one you actually control
- [Large Language Models (LLMs)](large-language-models.md) — what this converts into an assistant
- [Model Version & Update](model-version-update.md) — re-running this stage is how behavior changes between releases
- [Evaluation (AI Systems)](evaluation.md) — where the capitulation test belongs
- [Reward Hacking (Specification Gaming)](reward-hacking.md) — the reward model is a proxy, and proxies get gamed
- [Bias (AI Systems)](bias-ai-systems.md) — rater demographics and guidelines are a bias surface
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — humans at training time rather than at decision time
- [Scalable Oversight](scalable-oversight.md) — what happens when raters can no longer judge the output
- Reinforcement Learning (RL) — the optimization framework underneath

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-214 | Christiano, P.; Leike, J.; Brown, T.B.; Martic, M.; Legg, S.; Amodei, D. — *Deep Reinforcement Learning from Human Preferences* (NeurIPS, 2017) · [link](https://arxiv.org/abs/1706.03741) | The originating method: pairwise comparison as a goal-specification channel, and its striking cheapness — under 1% of interactions, about an hour of human time. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | The pipeline as applied to language models, and the capability-independence result: 1.3B aligned preferred over 175B unaligned. ⚠️ Vendor-authored, peer-reviewed. |
| SRC-167 | Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell, A.; Bowman, S.R. et al. (Anthropic) — *Towards Understanding Sycophancy in Language Models* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.13548) | That a training objective produces truth-displacing behavior without anyone designing it — the first named side effect. ⚠️ Vendor-affiliated, peer-reviewed. |
| SRC-172 | Zhou, K.; Hwang, J.D.; Ren, X.; Sap, M. — *Relying on the Unreliable: The Impact of Language Models' Reluctance to Express Uncertainty* (ACL, 2024) · [link](https://aclanthology.org/2024.acl-long.198/) | The measured bias against expressed uncertainty in preference data — the second side effect, and evidence it originates in the rating step. |
| SRC-193 | Gabriel, I. (DeepMind) — *Artificial Intelligence, Values and Alignment* (Minds and Machines, 2020) · [link](https://arxiv.org/abs/2001.09768) | Why *whose preferences* is the substantive question, and why "aligned with human values" conceals rather than answers it. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Where preference optimization sits in the training pipeline, and the vocabulary used consistently across this wiki. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Test the known signature directly — push back on correct answers and measure capitulation. Prompting does not undo a training-stage property. |
| **Organizational** | "Aligned" means aligned to a labeler pool following guidelines you have not seen. If you run your own preference tuning, the rater guidelines *are* the objective and need an owner. |
| **Client-facing** | Explains why models are helpful and polite by construction, and why that same construction makes them prone to agreeing with you. |
| **LLM-native** | Sycophancy and suppressed hedging are not bugs — they are what optimizing against approval selects for, and they arrive together. |

---

*Last updated: v1.0 · September 2026*
