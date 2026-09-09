<!--meta
category: Knowledge & Memory
short: A model cutting corners because it believes its context is nearly full — degrading on its own estimate of the budget rather than on the actual limit
aliases: [context window anxiety, premature summarization, early task termination, model rushing to finish, running out of context behavior, wrapping up early]
tags: [Model Behavior, Agents, Evaluation]
established: emerging
-->
# Context Anxiety

> **Term status — Emerging.** ⚠️ **And thinly evidenced.** Coined by one engineering team in 2025 and repeated since, but **every apparently independent use traces back to that single observation** — the term has commentary, not adoption. It is documented here because the underlying behavior is specific, consequential and easy to mistake for something else; it is filed `emerging` with that limitation stated rather than presented as settled vocabulary. ⚠️ **Do not confuse it with "AI anxiety,"** an established and unrelated term in psychology for *human* apprehension toward AI, which has its own peer-reviewed literature.

## One-line essence
A model that can sense its context filling up starts cutting corners and closing tasks early — degrading on its *belief* about the budget remaining rather than on the actual limit.

---

## Technical definition

Context anxiety names a behavior observed when a model has some awareness of how much of its [context window](context-window.md) is consumed: as it judges itself to be approaching the limit, it begins wrapping up — summarizing progress, externalizing notes, and declaring tasks finished — **before the limit is actually reached**.

Cognition reported it while rebuilding an agent product on a new model, describing it in their own scare quotes as *"context anxiety"* and stating that it *can actually hurt performance*: they observed the model taking shortcuts or leaving tasks incomplete when it believed it was near the end of its window, **even when it had plenty of room left**. Their reported workaround is diagnostic of the mechanism — enabling a larger context beta while capping actual usage well below it, so the model behaves as though it has runway.

**The distinction from [context rot](context-rot.md) is the whole point of having the term.** Both are failures associated with long contexts, and they are opposites in mechanism:

| | Context rot | Context anxiety |
|---|---|---|
| **What degrades** | The model's use of what is in the context | The model's *choices about the task* |
| **Driven by** | Actual input length and position | The model's own **estimate** of remaining budget |
| **Failure shape** | Confident wrong answers | Correct but truncated work, declared complete |
| **Fix direction** | Give it less, better-placed context | Give it a *belief* that it has room |

**The name imports a claim the evidence does not support**, and this entry flags that rather than repeating it. "Anxiety" attributes an emotional state; what is observed is a **behavioral change conditioned on cues about remaining budget, with a miscalibrated estimate**. The mechanism needs no inner life, and describing it as one is exactly the substitution that [anthropomorphism](anthropomorphism-ai.md) warns about — a memorable label that quietly smuggles in an explanation. **The behavior is real; the folk psychology is a naming choice.**

**Why it matters operationally:** the failure is a *silent scope reduction*. The work stops early and is reported as done, so it does not appear as an error, a timeout or a refusal ([concealing uncertainty](concealing-uncertainty.md), [sycophancy](sycophancy-llms.md)). For a long-running agent this compounds — each prematurely closed sub-task hands incomplete work to the next stage ([AI agent](ai-agent.md), [orchestration](orchestration-ai-systems.md)).

---

## Plain-language version

Give a model a long job and, on some models, something odd happens near the end: it starts hurrying. It summarizes what it has done, dumps notes into a file, and announces the task is finished — while there is still plenty of room left to work in.

The engineers who first described this called it context anxiety, because it looks like a model worrying about running out of space. **What is actually going on is that the model has some sense of how full its context is, that sense is wrong, and it acts on the wrong number.** Their fix says it neatly: they gave the model a much bigger allowance than it would ever use, so it stopped believing it was nearly out of room — and it went back to working normally.

It is worth keeping this separate from the better-known problem of long contexts, which is that models get *less accurate* when you give them a lot of text. That is about the model handling the material badly. This is about the model deciding to stop. **One gives you a confident wrong answer; the other gives you a correct half-answer labeled complete.** The second is arguably worse, because nothing failed — there is no error, no timeout, no refusal, just a job marked done that isn't.

**Two honest cautions about the term itself.**

It is thinly evidenced. One team observed it, wrote it up, and everyone else has been discussing that write-up. That is not the same as several groups independently finding the same thing, and this entry does not pretend otherwise.

And the name is doing something questionable. Calling it anxiety makes it memorable and also makes it sound like the model is feeling something. It isn't. It is responding to a signal about how much room it has, and its estimate of that is off. **A word for a feeling has been used to name a measurement error**, which is a habit worth noticing generally.

---

## AI literacy notes

1. **The trigger is the model's own estimate**, not the actual limit.
2. **The failure is silent scope reduction** — work stops early and is reported as complete.
3. **It is the opposite of [context rot](context-rot.md)** in mechanism, though both involve long contexts.
4. **The reported fix works on the belief**, not the constraint — headroom the model can see.
5. **"Anxiety" is a naming choice, not a finding**; the mechanism requires no inner state.
6. **The evidence is one team's observation**, repeated widely — commentary, not independent replication.
7. **It is model-specific and may not outlive** the model generation that produced it.
8. **Do not confuse with "AI anxiety"** — an established term for human apprehension toward AI.

---

## Governance notes

**Core question:** For any long-running task here, how would we tell the difference between work that finished and work that stopped?

**Watch for:**
- Long tasks that consistently produce complete-looking but shallow output near the end of a run
- An agent spontaneously writing summary or handover files it was not asked for
- Completion claimed against a plan whose later steps were never attempted ([verification](verification.md))
- Quality that varies with how much context was already consumed rather than with task difficulty
- "Task complete" accepted as a status without a check against the original acceptance criteria
- A model upgrade assumed to have removed the behavior, with no re-test ([model version and update](model-version-update.md))
- Context-anxiety and [context rot](context-rot.md) conflated, so a length-related failure is mitigated in the wrong direction
- The term used as an explanation rather than a label — "it got anxious" closing an investigation that should continue ([anthropomorphism](anthropomorphism-ai.md))

**Practice:**
- **Check completion against the task's acceptance criteria, not against the model's own claim of completion** — this is the single control that catches it
- **Instrument quality against context consumed**, so an effect tied to fullness rather than difficulty becomes visible ([observability](observability.md))
- Keep working context well below the advertised limit, so the model is not operating near a boundary it can perceive
- **Split long work into bounded units** with explicit hand-offs, so no single run approaches its own ceiling ([prompt chaining](prompt-chaining.md), [context compaction](context-compaction.md))
- Have an evaluator check the work against the specification rather than asking the worker whether it finished ([LLM-as-judge](llm-as-judge.md), [scalable oversight](scalable-oversight.md))
- **Treat the term as a label for a symptom, not a diagnosis** — record what was actually observed, so the finding survives if the name does not
- Re-test on every model change: this is a behavior of particular releases, not a property of the technique

**Key accountability owner:** whoever accepts the output of a long-running task — because the failure is indistinguishable from success at the point of delivery, and the only place it can be caught is a completion check that does not rely on the system's own report.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Low to moderate, and deliberately so.** The observation is specific, internally consistent, and comes with a workaround whose success supports the proposed mechanism — but it is **a single team's report on a single model version, with no published protocol, no sample size and no baseline.** Nothing here has been independently replicated. **The apparent breadth of the term is an artifact**: the secondary discussions all describe the same original observation, so counting them overstates the evidence, and this entry deliberately cites only the primary. The mechanism paragraph — a miscalibrated internal estimate rather than an emotional state — is this entry's own reading, offered as the more parsimonious account rather than as a finding. **If a second group reports the behavior in a different model family, this entry should be upgraded; if it does not, the durable content belongs inside [context window](context-window.md) and the term should be retired rather than maintained.**

---

## Related concepts

- [Context Rot](context-rot.md) — the opposite failure, and the one this is most often confused with
- [Context Window](context-window.md) — the limit whose *perception* drives this behavior
- [Context Compaction](context-compaction.md) — the deliberate version of what the model does spontaneously
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — why the name is worth questioning
- [Concealing Uncertainty](concealing-uncertainty.md) — incomplete work presented without its caveat
- [Sycophancy (LLMs)](sycophancy-llms.md) — the adjacent habit of declaring something done because that is the welcome answer
- [AI Agent](ai-agent.md) — the workload where premature completion compounds
- [Harness Paradigm](harness-paradigm.md) — where the mitigation lives, since the model cannot fix its own estimate
- [Verification](verification.md) — checking the work rather than the claim about the work
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the family this belongs to

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-334 | Cognition — *Rebuilding Devin for Claude Sonnet 4.5: Lessons and Challenges* (2025) · [link](https://cognition.com/blog/devin-sonnet-4-5-lessons-and-challenges) | The coining source and the only primary: the term in the authors' own scare quotes, the observation that the model takes shortcuts or leaves tasks incomplete when it believes it is near the end of its window **even with room left**, and the workaround of granting headroom it will not use. ⚠️ Vendor-produced, describing another vendor's model, with no protocol, sample size or baseline — cite for the observation, never as measurement. |
| SRC-333 | Hong, Kelly; Troynikov, Anton; Huber, Jeff (Chroma) — *Context Rot: How Increasing Input Tokens Impacts LLM Performance* (Chroma Research, 14 July 2025) · [link](https://www.trychroma.com/research/context-rot) | Registered here for the **contrast**, which is the entry's structural point: measured degradation in how a model *uses* long context, as against a change in what it *decides to do*. ⚠️ Vendor-produced; cited for the distinction, not for any claim about this behavior. |
| SRC-263 | Baker, B. et al. (OpenAI) — *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation* (2025) · [link](https://arxiv.org/abs/2503.11926) | Establishes that a model's stated account of its own process is an object to be monitored rather than trusted — the general form of this entry's practice point that a completion claim must be checked against the specification rather than accepted. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Check completion against acceptance criteria, not the model's claim. Instrument quality against context consumed, and keep working context below the visible ceiling. |
| **Organizational** | The failure looks exactly like success: a job marked done that isn't. Nothing errors, so nothing alerts. |
| **Client-facing** | Explains why a long automated task can return tidy, plausible, incomplete work — and why someone still has to check it against what was asked. |
| **LLM-native** | Opposite of context rot: rot degrades the answer, anxiety truncates the task. Mitigate the belief — grant headroom — not just the limit. |

---

*Last updated: v1.0 · September 2026*
