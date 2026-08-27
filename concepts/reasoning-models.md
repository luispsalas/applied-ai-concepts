# Reasoning Models / Test-Time Compute

## One-line essence
Models that spend extra computation "thinking" through a problem step by step before answering, rather than generating a response in one pass — trading speed for higher accuracy on hard tasks.

---

## Technical definition

A class of language model, and the technique behind it, in which additional computation is spent at **inference** time rather than only at training time. Instead of producing an answer in a single forward pass, the model generates intermediate reasoning — exploring, checking, and revising — before committing to a final output. The amount of computation spent per query becomes a variable the system can tune, rather than a fixed property of the model.

The technique's antecedent is **chain-of-thought prompting**, which showed that eliciting a series of intermediate reasoning steps substantially improves performance on arithmetic, commonsense, and symbolic tasks — reasoning surfaced through the prompt rather than trained into the model.

Test-time compute generalizes this. Analysis of how to allocate it — through searching against verifier reward models, or adaptively revising the model's own output distribution — found that the most effective strategy depends on problem difficulty, and that under a compute-optimal allocation, extra inference compute can outperform a substantially larger model on problems where the smaller model already has a non-trivial success rate. Capability, in other words, can be bought at inference time instead of parameter count.

Contemporary reasoning models train this behavior in rather than prompting for it. DeepSeek-R1 demonstrated that reasoning can be incentivized through reinforcement learning alone, using rule-based rewards for accuracy and format without human-annotated reasoning traces — with self-reflection, verification, and dynamic strategy adaptation emerging from the training process rather than being explicitly designed.

An important caution on interpretation: the reasoning trace a model emits is generated text, not a transcript of an internal process. It is evidence about the answer, not a verified account of how the answer was produced.

---

## Plain-language version

Most models answer immediately, like someone blurting out the first thing that comes to mind. Reasoning models work through the problem first — trying an approach, noticing a mistake, backing up — and only then answer. They are slower and cost more per question, and they are better at hard problems. On easy ones you are paying for thinking that wasn't needed.

---

## AI literacy notes

1. **"Thinking" is a metaphor, and a load-bearing one.** The model is generating more text before its final answer, and that extra generation empirically improves accuracy. It is not deliberating in any human sense — and treating the trace as a window into the model's actual process is the same mistake as trusting a confident answer because it sounds confident.
2. **The reasoning trace is not an explanation.** It reads like a justification and is often taken as one, but it is model output subject to all the same failure modes — including being plausible and wrong. Genuine [explainability](explainability-xai.md) is a different thing, and a visible chain of thought does not supply it.
3. **Compute became a dial, and the dial has a cost.** Accuracy can now be bought per query. That makes "how hard should the system think about this?" a real design and budget decision, and it means the same model can behave quite differently depending on how it was configured.
4. **Harder is not always better.** Extra reasoning helps most on difficult, verifiable problems — mathematics, code, multi-step logic. On simple or subjective tasks it adds latency and cost without a matching gain, and can introduce errors by overthinking a straightforward question.
5. **These models are still probabilistic.** Reasoning raises accuracy; it does not make output deterministic or guaranteed. The same question can still yield different reasoning paths and different answers.

---

## Governance notes

**Core question:** If a reasoning trace is shown to a user, an auditor, or a regulator — is it being presented as evidence of *what the model produced*, or misrepresented as evidence of *why*?

**Watch for:**
- Reasoning traces surfaced in a product as though they were explanations or audit evidence
- Reasoning depth changed as a cost-control measure, silently altering system behavior and accuracy without reassessment
- Traces logged verbatim without review — they may restate sensitive input data at length
- Assuming a reasoning model needs less oversight because its output "shows its work"

**Practice:**
- Treat reasoning depth as a versioned configuration parameter, on the record alongside the model version — a change to it is a change to the system
- Where traces are retained, apply the same [data minimization](data-minimization.md) and retention rules as any other model output
- Evaluate reasoning models on outcome correctness, not on whether the trace looks sound; a convincing trace with a wrong answer is the failure to catch
- State plainly, in any user-facing surface, that a visible trace is generated text and not a verified account of the system's internal process

**Key accountability owner:** the system owner, jointly with whoever controls model configuration and inference budget.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The core results are strong — chain-of-thought and compute-optimal scaling are well-cited, and DeepSeek-R1 is peer-reviewed in a major journal. Less settled: how far test-time scaling extends, how reliably traces correspond to the computation that produced an answer, and how to evaluate reasoning quality independently of final-answer accuracy. Terminology is also unstable — "reasoning model," "thinking model," and "test-time compute" are used loosely and sometimes interchangeably.

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — the base capability that reasoning training and inference-time compute build on
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — reasoning improves accuracy without making outputs deterministic
- [Explainability (XAI)](explainability-xai.md) — the crucial distinction: a reasoning trace is not an explanation
- [Prompt Engineering](prompt-engineering.md) — chain-of-thought began as a prompting technique before it was trained in
- [Context Window](context-window.md) — reasoning traces consume context, and long traces compete with the input for room
- [Hallucination](hallucination.md) — a fluent reasoning trace can make a wrong answer more persuasive, not less
- [Evaluation (AI Systems)](evaluation.md) — outcome correctness must be measured separately from whether the reasoning reads well
- RLHF (Reinforcement Learning from Human Feedback) — the adjacent training paradigm; reasoning models use RL with rule-based rather than human-preference rewards
- Inference — the phase where this additional compute is spent

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-047 | Wei, Jason et al. (Google Research, Brain Team) — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2023) · [link](https://arxiv.org/abs/2201.11903) | The antecedent technique: intermediate reasoning steps improve arithmetic, commonsense, and symbolic task performance. |
| SRC-155 | Snell, C.; Lee, J.; Xu, K.; Kumar, A. (UC Berkeley / Google DeepMind) — *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* (arXiv, 2024) · [link](https://arxiv.org/abs/2408.03314) | Compute-optimal allocation of test-time compute; the finding that it can outperform a substantially larger model under a FLOPs-matched comparison. |
| SRC-156 | Guo, D.; Yang, D.; Zhang, H.; Song, J.; Wang, P.; Zhu, Q. et al. (DeepSeek-AI) — *DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning*, Nature 645(8081), 633–638 (2025) · [link](https://doi.org/10.1038/s41586-025-09422-z) | Peer-reviewed evidence that reasoning can be incentivized by reinforcement learning alone, with self-reflection and verification emerging from training. |
| SRC-142 | Zhao, W.X. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Background on inference-time behavior and the training-vs-inference distinction this entry rests on. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Reasoning depth is a tunable parameter with a direct accuracy/latency/cost curve — and a configuration change that alters system behavior. |
| **Organizational** | Introduces a per-query cost decision and a governance trap: reasoning traces look like explanations and will be mistaken for them unless you say otherwise. |
| **Client-facing** | Explains why some AI answers take noticeably longer, and why "it showed its reasoning" is not the same as "it can be trusted." |
| **LLM-native** | Capability is increasingly bought at inference time rather than parameter count, changing how model choice and budget interact. |

---

*Last updated: v1.0 · August 2026*
