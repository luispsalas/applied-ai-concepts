<!--meta
category: Foundations
short: The wait between asking and being answered — and the constraint that quietly decides whether a human review step survives contact with the product
aliases: [latency, response time, time to first token, TTFT, tokens per second, speed, how fast is it, why is it slow]
tags: [AI Literacy, Architecture]
established: established
-->
# Latency (AI Systems)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The time between sending a request to an AI system and receiving a response — a performance constraint that shapes what real-time and user-facing applications can rely on.

---

## Technical definition

Latency is elapsed time from request to response. For generative systems it is not one number, and treating it as one is the most common mistake:

- **Time to first token (TTFT)** — how long before anything appears.
- **Inter-token latency** — how fast output continues, usually quoted as tokens per second.
- **Total completion time** — TTFT plus generation, and therefore **a function of output length rather than of question difficulty** ([inference](inference.md)).

**Human thresholds are old, stable, and rarely consulted.** Nielsen's three limits, drawn from Miller (1968) and Card et al. (1991), are **0.1 second** for a system to feel instantaneous, **1 second** for a user's flow of thought to continue uninterrupted, and **10 seconds** as the limit of attention on a task — beyond which people need to be told when it will finish.

**Streaming changes which threshold applies, and that is why every chat interface streams.** With output appearing progressively, TTFT governs the *perception* of responsiveness while total completion time can exceed ten seconds without losing the user, because feedback is continuous. **Latency budgets written against total time, for a streaming product, are measuring the wrong thing.**

**The operational problem is the tail, not the mean.** Dean and Barroso (*Communications of the ACM*, 2013) set out why: in systems where one request fans out to many components, the slowest component determines the response, so rare slow events dominate the experience rather than averaging away. **Agentic systems make this sharply worse** — a run that issues many model and tool calls in sequence inherits the tail of each, and a p99 that looks acceptable per call is not acceptable twenty calls deep ([multi-agent systems](multi-agent-systems.md)).

**Latency is bought and sold against other things.** Batching more requests raises throughput and can raise per-request latency; spending more compute at inference raises answer quality and raises latency with it ([reasoning models](reasoning-models.md)). Neither trade is visible to the person experiencing the result.

---

## Plain-language version

Latency is the wait. You ask; you wait; you get an answer.

For text-generating systems the wait has two parts that people confuse. There is how long before *anything* appears, and there is how fast the words keep coming once they start. Total time depends mostly on how long the answer is — not on how hard the question was. A short answer to a hard question comes back quickly; a long answer to an easy one does not.

There are three numbers worth knowing, and they come from research older than the web. Under a tenth of a second feels instant. Under a second, your train of thought survives. Past about ten seconds, people stop waiting unless you tell them how much longer it will be.

This is why chat interfaces show words as they arrive rather than waiting for the whole answer. Once something is visibly happening, people will wait much longer than ten seconds. The thing being measured has quietly changed from "how long did it take" to "how long until something happened."

Averages also mislead here. What ruins the experience is not the typical wait but the occasional very long one — and systems that make many internal calls collect the worst case from each. A system that is usually fast can be reliably annoying.

The part worth carrying into a decision: **speed competes with checks.** A review step, a safety filter, a second opinion — each adds time. When something has to give, it is usually the check, because the delay is visible to users and the missing check is not.

---

## AI literacy notes

1. **It is not one number** — time to first token, tokens per second, and total time behave differently and answer different questions.
2. **Total time tracks output length**, not question difficulty, which is why verbose prompting costs twice.
3. **Three human thresholds**: 0.1s instantaneous, 1s uninterrupted thought, 10s the limit of attention.
4. **Streaming moves the relevant threshold to TTFT** and lets total time exceed ten seconds without losing the user.
5. **The tail dominates, not the mean** — and measuring p50 will tell you the system is fine while users disagree.
6. **Agent runs compound the tail** across every call in the chain.
7. **Throughput and latency trade against each other**; serving more users can slow each one.
8. **More thinking costs more waiting** — inference-time reasoning buys quality with time.

---

## Governance notes

**Core question:** Which checks in this system were removed, shortened, or made optional because they were too slow — and was that a recorded decision or an engineering default?

**Watch for:**
- A latency budget expressed as total response time for a product that streams — measuring what the user does not experience
- Performance reported as an average or p50, where the tail is what users actually meet
- **Human review, verification or filtering steps dropped or made asynchronous for responsiveness**, with no record of the trade ([human-in-the-loop](human-in-the-loop.md), [verification](verification.md))
- Guardrails moved from blocking to observe-only to save time, converting a control into a monitor ([agent hooks](agent-hooks.md))
- Agent runs with no per-call or total time ceiling, so a slow path becomes an unbounded one ([sandboxing](sandboxing.md))
- Latency assumptions carried across a model version change without re-measurement ([model version and update](model-version-update.md))
- Cost controls that raise batching, quietly degrading per-request latency for everyone
- Timeouts set without deciding what a timeout *means* — retry, degrade, or fail closed

**Practice:**
- **Measure and state the tail** — p95 and p99, not the mean — and measure at the point the user experiences, not at the model call
- Budget TTFT separately from completion time, and match the metric to whether the product streams
- **Record every check traded away for speed as a decision with an owner.** This is the trade that happens silently and is the one worth writing down
- Set explicit per-call and total ceilings on agent runs, and define the behavior on breach rather than inheriting a default
- Re-measure after any model, prompt, or serving change; latency is not a stable property of a system
- Prefer degrading gracefully — a partial answer, a progress signal, a queued result — to a silent long wait
- Where a review step is genuinely too slow to be synchronous, make it asynchronous **and** make the record show it happened after the fact ([audit trail](audit-trail-ai.md))

**Key accountability owner:** whoever owns the user experience — because latency pressure is felt there first, and the fastest thing to remove is always a check whose absence nobody sees.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The decomposition into TTFT, inter-token latency and completion time is standard engineering practice; the human thresholds come from a stable HCI literature with named 1968 and 1991 antecedents; and the tail-latency argument is a peer-reviewed *CACM* paper that has held up for over a decade across exactly the fan-out architectures agentic systems now build. **The weaker claim is the governance one** — that latency pressure is where oversight gets traded away. That follows from the mechanics and matches practitioner experience, but **this entry cites no measurement of how often a check is removed for speed**, because none was found. It is offered as the question to ask, not as a documented rate. Specific numbers also date fast: serving performance changes with every model and infrastructure generation, so treat any figure as a measurement of a moment.

---

## Related concepts

- [Inference](inference.md) — the phase where latency is actually incurred, and where its cost is paid
- [Scalability (AI Systems)](scalability-ai-systems.md) — what happens to all of this under load
- [Edge AI](edge-ai.md) — relocating computation specifically to remove the round trip
- [Reasoning Models / Test-Time Compute](reasoning-models.md) — buying answer quality with time
- [Context Window](context-window.md) — longer inputs and outputs cost time as well as money
- [Multi-Agent Systems](multi-agent-systems.md) — where per-call tails compound into a run
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the check most often traded for responsiveness
- [Agent Hooks](agent-hooks.md) — where a blocking control becomes an observing one under time pressure
- [Observability](observability.md) — measuring the tail rather than the average
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the degraded path was designed or discovered

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-279 | Nielsen, Jakob (Nielsen Norman Group) — *Response Times: The 3 Important Limits* (January 1, 1993) · [link](https://www.nngroup.com/articles/response-times-3-important-limits/) | The three human thresholds this entry uses — 0.1s instantaneous, 1s uninterrupted thought, 10s the limit of attention — which Nielsen attributes to Miller (1968) and Card, Robertson & Mackinlay (1991). ⚠️ A practitioner article summarizing older research; cite it for the thresholds and follow the attribution for the underlying studies. |
| SRC-280 | Dean, Jeffrey; Barroso, Luiz André (Google) — *The Tail at Scale* (Communications of the ACM 56(2), pp. 74–80, February 2013) · [link](https://doi.org/10.1145/2408776.2408794) | The tail-latency argument: where one request fans out across many components, the slowest determines the response, so rare slow events dominate rather than averaging away. The basis for this entry's claim that agent runs compound tails. Metadata verified via Crossref. |
| SRC-247 | Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu, C.H.; Gonzalez, J.E.; Zhang, H.; Stoica, I. (UC Berkeley et al.) — *Efficient Memory Management for Large Language Model Serving with PagedAttention* (SOSP, 2023) · [link](https://arxiv.org/abs/2309.06180) | The throughput-versus-latency trade at the serving layer, and evidence that per-request latency is an infrastructure property rather than a model one. |
| SRC-155 | Snell, C.; Lee, J.; Xu, K.; Kumar, A. (UC Berkeley / Google DeepMind) — *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters* (2024) · [link](https://arxiv.org/abs/2408.03314) | Establishes that answer quality can be bought with inference-time compute — which is bought, in turn, with waiting. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Background on autoregressive decoding, the mechanism that makes completion time scale with output length. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Measure p95 and p99 at the user's vantage point, budget TTFT separately from completion time, and set explicit ceilings on agent runs with a defined behavior on breach. |
| **Organizational** | Latency pressure is where oversight quietly gets traded away — the delay is visible and the missing check is not. Record every check shortened for speed as a decision with an owner. |
| **Client-facing** | Explains why answer length drives wait time, why a usually-fast system is sometimes slow, and why progress feedback is a design choice rather than a nicety. |
| **LLM-native** | Latency is not one number. Streaming moves the threshold that matters to time-to-first-token, and the tail — not the mean — is what users actually meet. |

---

*Last updated: v1.0 · September 2026*
