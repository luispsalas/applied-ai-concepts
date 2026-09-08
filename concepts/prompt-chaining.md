<!--meta
category: Interaction & Design
short: Breaking one task into a sequence of prompts — which buys you inspectable intermediate steps, and costs you a path for errors to travel down
aliases: [chaining, LLM chaining, AI chains, multi-step prompting, task decomposition, breaking a task into steps, step-by-step prompts]
tags: [Prompting, Architecture, AI Literacy]
established: established
-->
# Prompt Chaining

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator — named in peer-reviewed HCI research and in multiple vendors' architecture guidance.

## One-line essence
Connecting multiple prompts in sequence so each output feeds the next — a technique for breaking complex tasks into manageable, auditable steps.

---

## Technical definition

Prompt chaining decomposes a task into a sequence of model calls, where the output of one step becomes the input to the next. Wu, Terry and Cai introduced the concept as **Chaining**, defining a set of primitive LLM operations from which chains are built, and showing in a user study that chaining improved task outcomes *and* gave people a place to intervene — they could inspect and edit intermediate results rather than accepting or rejecting a single opaque response.

**Two distinct benefits, and they are usually conflated.** The first is **quality**: each step is a narrower problem, and a narrow prompt outperforms one prompt asked to do everything at once. The second is **transparency**: the intermediate outputs exist as artifacts, so a wrong answer can be traced to the step that produced it. **The second is the one that matters for governance**, and it is available whether or not the first materializes.

**It is the simplest workflow arrangement, and it sits at the bottom of the autonomy ladder.** Anthropic's *Building Effective Agents* lists prompt chaining first among its workflow patterns, before routing, parallelization, orchestrator–workers and evaluator–optimizer — and the standing advice across that literature is to prefer the simplest arrangement that works ([agentic design patterns](agentic-design-patterns.md), [orchestration](orchestration-ai-systems.md)). **The path is fixed in code; the model fills the steps but does not choose them**, which is exactly what makes a chain enumerable, testable and auditable in a way an agentic arrangement is not.

**Chaining is not chain-of-thought, and the names invite the confusion.** Chain-of-thought is reasoning *inside* one model call, elicited by prompting; the intermediate steps are generated text and [need not reflect the process that produced the answer](reasoning-models.md). Prompt chaining is multiple *separate* calls, and its intermediate outputs are real artifacts that were actually consumed by the next step. **One is a description of reasoning; the other is a record of execution.**

**The characteristic failure is propagation.** A step consuming a subtly wrong input produces a confidently wrong output, and each subsequent step launders it further — the chain has no mechanism to notice that step two was working from a bad premise. Empirical work on multi-step systems finds failures concentrating in exactly these seams, and the outcome commonly looks like success rather than like an error ([orchestration](orchestration-ai-systems.md)). **Decomposition multiplies the number of places a mistake can enter while creating no automatic place where one is caught.** Validation between steps is what converts the transparency into an actual control.

---

## Plain-language version

Instead of asking a model to do a big job in one go, you break it into steps and run them in order. Summarize the document. Then pull the key claims out of the summary. Then check each claim against the source. Each step gets one thing to do, and hands its result to the next.

Two things come out of this, and only one of them is what people usually mean.

The obvious one is that it works better. A model asked to do one narrow thing does it more reliably than one asked to do five things at once.

The more valuable one is that **you can see the middle.** With a single prompt, you get an answer and no idea how it got there. With a chain, the intermediate results exist — you can read them, correct them, and when the final answer is wrong you can find out which step went wrong. The researchers who named this found people used exactly that: they edited the middle rather than rerunning the whole thing.

A name to keep straight: this is **not** "chain of thought." That is a model talking through its reasoning inside a single answer, and what it says about its reasoning is not necessarily what actually happened. Prompt chaining is genuinely separate steps, and the intermediate output really is what the next step received.

Now the catch, and it is a real one. **A chain does not check itself.** If step two misreads step one, step three works faithfully from the mistake, and step four polishes it. What comes out the end is fluent, confident, and wrong — and it looks exactly like a good result. Breaking a task into six steps creates six places for something to go wrong and zero places where anything gets caught. **The visibility only becomes a safeguard if someone or something actually looks.**

---

## AI literacy notes

1. **Chaining buys two different things** — better output and visible intermediate steps. The second is the durable one.
2. **It is not chain-of-thought.** Separate calls with real artifacts, versus generated reasoning text inside one call.
3. **The path is fixed in code**, which is what makes a chain enumerable and testable, unlike an agentic arrangement.
4. **Errors propagate and get laundered** — later steps work faithfully from an earlier mistake.
5. **Decomposition adds failure points without adding checks**; the checks have to be put in deliberately.
6. **Failures look like success**, because the output is fluent and every step ran without erroring.
7. **Prefer a chain to an agent** where the steps are known in advance — less autonomy, more auditability.
8. **Latency and cost scale with the number of steps**, since each is a separate call ([latency](latency-ai-systems.md)).

---

## Governance notes

**Core question:** When this chain produces a wrong answer, can we say which step produced it — and is anything checking between the steps, or only at the end?

**Watch for:**
- Intermediate outputs discarded after use, so the traceability the pattern offers is thrown away ([audit trail](audit-trail-ai.md))
- No validation between steps, so the chain's only check is a human reading the final output
- A long chain where a single wrong early step is unrecoverable and invisible
- Evaluation applied to the end-to-end result only, so a systematically weak step is never isolated ([evaluation](evaluation.md))
- Chain-of-thought text treated as if it were an execution record ([reasoning models](reasoning-models.md))
- Steps added over time until nobody can enumerate the full path — the chain has quietly become an architecture
- Failure handling unspecified: what a step does with a malformed input from the previous one
- An agentic arrangement chosen where a fixed chain would have done, giving up auditability for flexibility nobody needed ([orchestration](orchestration-ai-systems.md))

**Practice:**
- **Persist the intermediate outputs**, not just the final one — this is the whole governance value of the pattern and it is free at design time, expensive to retrofit
- **Validate between steps**, at least for shape and plausibility; the chain will not notice a bad premise on its own
- Evaluate steps individually as well as end-to-end, so a weak link is attributable ([evaluation](evaluation.md))
- Define explicitly what each step does with a malformed or empty input, rather than letting it improvise
- Put the human checkpoint where the intermediate result is still correctable, not after the last step ([human-in-the-loop](human-in-the-loop.md))
- Keep the chain short enough to enumerate, and re-read it as a whole when steps are added
- **Prefer a fixed chain over an agentic arrangement whenever the steps are known in advance** — same work, enumerable paths

**Key accountability owner:** whoever owns the workflow's output — because decomposition distributes the work across steps while leaving responsibility for the result undivided, and only retained intermediates make that responsibility discharge-able.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The technique is simple, uncontroversial and independently documented in peer-reviewed HCI research and in multiple vendors' architecture guidance, and its mechanics are not in dispute. **The quality claim is the part to state carefully**: the founding study demonstrated improvements on specific tasks with a specific interface, and chaining is not universally better than a single well-written prompt — a chain adds calls, latency and failure surface, and short tasks are frequently better served by one call. **The transparency claim is stronger and holds structurally**, since intermediate artifacts either exist or do not, independent of task. The error-propagation characterization draws on empirical work about multi-step systems generally rather than about chains specifically, and is stated here as a mechanism rather than a measured rate.

---

## Related concepts

- [Orchestration (AI Systems)](orchestration-ai-systems.md) — the control layer a chain is the simplest form of
- [Agentic Design Patterns](agentic-design-patterns.md) — the catalog prompt chaining sits at the bottom of
- [Prompt Engineering](prompt-engineering.md) — the craft applied to each individual step
- [Reasoning Models / Test-Time Compute](reasoning-models.md) — chain-of-thought, and why it is a different thing
- [Human-in-the-Loop](human-in-the-loop.md) — the checkpoint a chain makes it possible to place mid-process
- [Audit Trail (AI)](audit-trail-ai.md) — what retained intermediate outputs become
- [Evaluation (AI Systems)](evaluation.md) — per-step measurement, not only end-to-end
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — propagation as a named class
- [AI Agent](ai-agent.md) — what you get when the model chooses the steps instead
- [Latency (AI Systems)](latency-ai-systems.md) — the cost of every additional step

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-290 | Wu, Tongshuang; Terry, Michael; Cai, Carrie Jun (Carnegie Mellon / Google Research) — *AI Chains: Transparent and Controllable Human-AI Interaction by Chaining Large Language Model Prompts* (CHI, 2022) · [link](https://doi.org/10.1145/3491102.3517582) | The founding definition — chaining LLM steps so the output of one becomes the input of the next, built from a defined set of primitive operations — and the user-study finding this entry's transparency argument rests on: people inspected and **edited intermediate results** rather than accepting or rejecting one opaque answer. ⚠️ Improvements were measured on specific tasks with a purpose-built interface; do not restate as a general claim that chaining beats single prompts. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Places prompt chaining first among workflow patterns (before routing, parallelization, orchestrator–workers and evaluator–optimizer) under an explicit workflow-versus-agent distinction, and supplies the standing advice to prefer the simplest arrangement that works. ⚠️ Vendor engineering guidance; cited for the pattern's place in the ladder, not as evidence of efficacy. |
| SRC-045 | Shapira, Natalie et al. — *Agents of Chaos* (arXiv:2602.20021, 2026) · [link](https://arxiv.org/abs/2602.20021) | Empirical grounding for the propagation failure: errors cascading across a multi-step action sequence, with the outcome presented as complete. ⚠️ A preprint, and about agentic systems rather than fixed chains — cited here for the mechanism, which is why this entry states propagation as a mechanism rather than a rate. |
| SRC-047 | Wei, Jason et al. (Google Research, Brain Team) — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2023) · [link](https://arxiv.org/abs/2201.11903) | The other "chain" — needed to state the distinction accurately rather than from paraphrase: reasoning elicited **within** a single call, as against separate calls with real intermediate artifacts. |
| SRC-238 | Turpin, M.; Michael, J.; Perez, E.; Bowman, S.R. — *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting* (NeurIPS, 2023) · [link](https://arxiv.org/abs/2305.04388) | Why the distinction is load-bearing rather than pedantic: generated reasoning text need not reflect the process that produced the answer, whereas a chain's intermediate output demonstrably was consumed by the next step. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Persist the intermediates and validate between steps. Decomposition adds failure points and no checks — the checks are yours to add. |
| **Organizational** | A chain is the auditable option: fixed path, enumerable steps, inspectable middle. Prefer it to an agent whenever the steps are known in advance. |
| **Client-facing** | Explains how a multi-step system can be examined and corrected part-way, rather than trusted or rejected whole. |
| **LLM-native** | Not chain-of-thought. The middle is real and reviewable — but a bad step two is laundered by every step after it. |

---

*Last updated: v1.0 · September 2026*
