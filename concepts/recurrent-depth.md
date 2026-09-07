<!--meta
category: Foundations
short: Spending more compute by looping a model's own layers rather than by writing more tokens — capability without extra parameters, and thinking that produces nothing to read
aliases: [looped transformer, depth-recurrent, latent reasoning, weight-tied layers, recurrent block, thinking without tokens, reasoning with no trace]
tags: [Model Behavior, Safety, Architecture]
established: emerging
-->
# Recurrent Depth

> **Term status — Emerging.** Real and in use, but definitions still vary between sources — see the confidence level for what is unsettled.

## One-line essence
An architecture that adds reasoning effort by looping information through the same layers instead of by generating more text — more depth without more parameters, and reasoning that leaves no readable trace.

---

## Technical definition

A conventional transformer passes input through a fixed stack of distinct layers once per token. A recurrent-depth model instead **iterates a single weight-tied block**, unrolling it to a chosen depth at inference. Geiping et al. (NeurIPS 2025) state the mechanism directly: the model works by *iterating a recurrent block, thereby unrolling to arbitrary depth at test-time* — and they position it explicitly against the mainstream approach, which scales compute by producing more tokens.

**Two properties follow, and both matter.** Effective depth is decoupled from parameter count, so more computation can be spent without a larger model. And the additional computation happens **in latent space**, not in emitted text.

**The second property is the one with consequences.** The authors note the approach *does not require any specialized training data, can work with small context windows, and can capture types of reasoning that are not easily represented in words.* Their proof of concept was a 3.5-billion-parameter model trained on 800 billion tokens, which improved with additional test-time compute on reasoning tasks.

**This is a different way of buying the same thing.** [Reasoning models](reasoning-models.md) scale test-time compute by generating more tokens — a visible chain of thought. Recurrent depth scales it by iterating internally. Both spend compute at inference to improve answers ([inference](inference.md)); they differ in whether the spending leaves an artifact.

**And that difference is where the governance weight sits.** The corpus already records that a chain-of-thought trace **can misrepresent** the computation that produced an answer — measured, not hypothetical. Recurrent depth poses the harder version: **there is no trace to misrepresent.** Every oversight approach that reads a model's reasoning — trace monitoring, chain-of-thought review, self-report auditing — has nothing to read. What remains is the output, and [mechanistic interpretability](mechanistic-interpretability.md), which is a research program rather than an audit tool.

**Naming is genuinely unsettled.** *Recurrent depth*, *looped transformer*, and *depth-recurrent* all name this mechanism; the popular press mostly uses the second. Independent adoption exists — Tur et al. (2026) apply *Recurrent-Depth VLA* to vision-language-action models — but the vocabulary has not converged.

---

## Plain-language version

When an AI "thinks harder" today, it usually does it by writing more. It talks itself through the problem, and that written-out reasoning is what you see in a chatbot's thinking box.

Recurrent depth does it differently. Instead of writing more, the model runs the same set of internal layers over and over on the same input, refining its internal state before producing anything. It thinks by looping rather than by talking.

There are real advantages. You get more thinking without a bigger model, so you are not paying for extra parameters. The model can spend more effort on hard questions and less on easy ones. And it does not need specially prepared training examples of reasoning.

Now the catch, and it is a significant one. The written-out reasoning was never a perfect record of what the model actually did — research has shown those explanations can be misleading. But it was *something*. It could be read, logged, spot-checked, and argued with.

Loop the layers instead, and there is nothing to read. The thinking happens as numbers moving inside the network. It is not that the explanation might be wrong; it is that there is no explanation. Every method for supervising an AI by watching it reason stops applying, and you are left with judging the answer.

That is not an argument against the technique — it is faster and cheaper, and those are real. It is an argument for knowing which trade you are making, because a model that reasons invisibly is a different oversight problem from one that reasons out loud.

---

## AI literacy notes

1. **Thinking without tokens.** Extra computation happens inside the network, not as text you can read.
2. **Depth is decoupled from size** — more effective computation without more parameters.
3. **It is an alternative to chain-of-thought scaling, not an addition to it** — same goal, different medium.
4. **A visible trace can be unfaithful; an absent trace cannot be checked at all.** These are different problems, and the second is worse for oversight.
5. **Trace-based monitoring stops applying**, which removes a control many AI safety approaches currently assume.
6. **What remains is output judgment and mechanism** — and mechanistic interpretability is not yet an audit tool.
7. **Three names compete** for one mechanism; expect the literature and the press to disagree.
8. **⚠️ Do not repeat as fact that any specific commercial model uses it** — see the confidence level.

---

## Governance notes

**Core question:** If this system reasons in a form nobody can read, what is our evidence that it reasoned acceptably — and is that evidence anything other than "the answer looked right"?

**Watch for:**
- Oversight processes that assume a readable reasoning trace will exist ([reasoning models](reasoning-models.md))
- Trace or chain-of-thought monitoring named as a safety control for a system where it does not apply
- Vendor architecture claims accepted from press reporting rather than from the vendor's own documentation
- Latent reasoning depth treated as a performance dial with no owner, when it changes both cost and behavior ([inference](inference.md))
- Audit and record-keeping obligations planned around storing reasoning traces that will not be produced ([audit trail](audit-trail-ai.md), [compliance](compliance-ai-systems.md))
- Claims that invisible reasoning is *safer* because it cannot be manipulated — untested, and it removes evidence either way
- Evaluation that scores only final answers, where the process is now unobservable ([evaluation](evaluation.md))

**Practice:**
- **Establish which oversight controls depend on a readable trace, and mark them as inapplicable** rather than letting them sit in a policy that no longer bites
- Ask suppliers directly whether reasoning is emitted or latent, and treat an unanswered question as a material gap
- Strengthen output-side evidence where process evidence is unavailable — held-out testing, [verification](verification.md) of consequential outputs, [human checkpoints](human-in-the-loop.md) at irreversibility
- Record reasoning depth or compute budget per request as a governed configuration value with an approver
- Do not accept "no trace" as either a safety benefit or a safety failure without evidence; state it as a **change in what can be observed**
- Track [mechanistic interpretability](mechanistic-interpretability.md) as the only non-behavioral evidence route, while treating it as research rather than assurance

**Key accountability owner:** whoever owns the model-selection decision — because whether reasoning is emitted or latent is fixed by the architecture chosen, is rarely stated in procurement, and silently determines which oversight controls remain available for the system's lifetime.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-high on the mechanism, low-medium on adoption — and the naming is the reason this is filed as emerging rather than established.** The architecture, its stated properties and the proof-of-concept scale come from peer-reviewed work at a top venue, and independent use by an unrelated group is verifiable. **What is unsettled is vocabulary and uptake:** three names compete for one mechanism, the term is under two years old, and its public salience comes from a news cycle rather than from documented deployment. It is admitted as a real term on evidence, and labeled `emerging` because the label has not converged.

**⚠️ One widely-repeated claim is explicitly not endorsed here.** Numerous secondary sources report that a specific frontier commercial model uses recurrent depth. **The developer has not confirmed it.** The claim traces to press reporting; the model's own launch material and system card do not name the architecture, and a September 2026 publication from that developer discussing the model at length — its compute allocation, its safety restrictions — **contains no mention of recurrent depth, looping, or latent reasoning at all.** That is a checked absence, not an inference from silence. Treat the attribution as journalism until the developer states otherwise.

---

## Related concepts

- [Reasoning Models / Test-Time Compute](reasoning-models.md) — the token-emitting way of buying the same thing, and where trace unfaithfulness was measured
- [Inference](inference.md) — the phase where this compute is spent, and the cost dial it creates
- [Mechanistic Interpretability](mechanistic-interpretability.md) — the only remaining non-behavioral evidence route when there is no trace
- [Black Box](black-box.md) — the general problem this architecture deepens
- [Explainability (XAI)](explainability-xai.md) — post-hoc explanation, which now has less to work from
- [Scalable Oversight](scalable-oversight.md) — supervising what you cannot fully inspect
- [Large Language Models (LLMs)](large-language-models.md) — the model family this architecture modifies
- [Evaluation](evaluation.md) — output-side evidence, which carries more weight when process evidence is gone
- [Audit Trail (AI)](audit-trail-ai.md) — what can and cannot be recorded about a decision
- [Frontier AI](frontier-ai.md) — where the reported deployments sit, and where the attribution is unconfirmed

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-254 | Geiping, J.; McLeish, S.; Jain, N.; Kirchenbauer, J.; Singh, S.; Bartoldson, B.R.; Kailkhura, B.; Bhatele, A.; Goldstein, T. — *Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach* (NeurIPS, 2025) · [link](https://arxiv.org/abs/2502.05171) | The originating formulation and this entry's mechanism: iterating a recurrent block to unroll to arbitrary depth at test time, contrasted explicitly with scaling by producing more tokens. Proof of concept at 3.5B parameters / 800B tokens; no specialized training data required. |
| SRC-258 | Tur, Y.; Naghiyev, J.; Fang, H.; Tsai, W.-C.; Duan, J.; Fox, D.; Krishna, R. — *Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning* (2026) · [link](https://arxiv.org/abs/2602.07845) | Independent use of the term by an unrelated group in a different modality — the evidence that this is a term of art rather than one lab's vocabulary. |
| SRC-155 | Snell, C.; Lee, J.; Xu, K.; Kumar, A. (UC Berkeley / Google DeepMind) — *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* (2024) · [link](https://arxiv.org/abs/2408.03314) | The general finding this architecture is one implementation of: inference-time compute can substitute for parameter scale. |
| SRC-240 | Chen, Y.; Benton, J.; Radhakrishnan, A.; Uesato, J.; Denison, C.; Schulman, J. et al. (Anthropic) — *Reasoning Models Don't Always Say What They Think* (2025) · [link](https://arxiv.org/abs/2505.05410) | The measured unfaithfulness of visible reasoning traces — the baseline against which "no trace at all" is the harder case rather than an equivalent one. |
| SRC-253 | OpenAI — *Research acceleration: The view inside OpenAI* (September 6, 2026) · [link](https://openai.com/index/research-acceleration-view-inside-openai/) | Cited for a **checked absence**: this publication discusses the model in question at length, including compute allocation and safety restrictions, and never names recurrent depth, looping or latent reasoning — supporting the entry's refusal to repeat the press attribution. ⚠️ Vendor-authored and self-reported; live URL is behind a bot challenge, archived copy used. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Establish which oversight controls assume a readable trace and mark them inapplicable. Ask suppliers whether reasoning is emitted or latent; treat no answer as a material gap. |
| **Organizational** | Whether a model reasons visibly or invisibly is fixed at procurement, rarely stated, and silently determines which controls remain available for the system's lifetime. |
| **Client-facing** | Explains why some systems can show their working and others structurally cannot, without overclaiming that either is safer. |
| **LLM-native** | It thinks by looping, not by talking. A visible trace can be unfaithful; an absent trace cannot be checked at all — and those are different problems. |

---

*Last updated: v1.0 · September 2026*
