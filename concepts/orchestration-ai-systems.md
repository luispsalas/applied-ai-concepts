<!--meta
category: System Architecture
short: The control layer deciding what runs and in what order — where the failures hide in the seams and look like success
aliases: [workflow, pipeline, coordinating AI components, agent orchestration, chaining steps]
tags: [Agents, Architecture]
established: established
-->
# Orchestration (AI Systems)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Coordinating multiple AI components — models, tools, memory, agents — to complete a complex task as a unified, governable system.

---

## Technical definition

The control layer that decides what runs, in what order, with what inputs, and what happens when a step fails. It is the difference between a collection of capable components and a system: models, [tools](tool-use.md), retrieval, [memory](memory-ai-systems.md), and other [agents](ai-agent.md) each do something useful, and orchestration is what turns them into a sequence with a defined outcome.

**The governing distinction is where control lives:**

| | |
|---|---|
| **Workflow** | The path is defined in code. The model fills steps; it does not choose them. Predictable, testable, auditable — and limited to paths you anticipated. |
| **Agentic** | The model chooses the path at runtime — which tool, how many steps, when to stop. Handles unanticipated cases, and the execution trace is decided during operation rather than at design time. |

This is the most consequential architectural decision in the space, and the practitioner consensus is unusually clear: **prefer the simplest arrangement that works, and add autonomy only where the task genuinely cannot be decomposed in advance.** Multi-agent and dynamic routing are frequently reached for before a single well-scoped call has been tried.

**Why it matters for governance rather than only for engineering:** orchestration determines what is *knowable* about a run. In a defined workflow, the set of possible executions is enumerable, so testing covers it and an [audit trail](audit-trail-ai.md) can be designed against it. In an agentic arrangement the path is composed at runtime, so the reachable surface — which tools, which data, how many steps — is decided during execution. That is the same property that makes [agency](agency-ai-systems.md) hard to bound and permissions hard to scope in advance.

**The characteristic failure is not a bad output; it is a lost one.** Empirical taxonomies of agentic faults find that failures concentrate in the *seams*: a tool returning something unexpected, a step consuming a malformed result from the previous one, a loop that neither completes nor terminates, an error swallowed so that a partial result is presented as complete. Individually reasonable steps compose into an outcome nobody would have approved. **Orchestration failures therefore look like success far more often than model failures do** — which is why they need their own detection rather than inheriting output-quality checks.

---

## Plain-language version

One AI call answering one question needs no coordination. Real work usually needs several things in sequence: look something up, draft with it, check it against a rule, format the result, file it somewhere.

Orchestration is whatever decides that sequence — the order, what feeds into what, and what happens when a step goes wrong.

There are two ways to do it. You can write the steps out, so the system always follows the same path and the model just does the work at each stage. Or you can let the model decide as it goes, which handles situations you did not anticipate but means nobody knows in advance what will actually happen.

The second is more flexible and much harder to govern, and it is reached for far too early. The useful instinct is to use the simplest arrangement that does the job — partly because complexity costs, and partly because the failures here are the quiet kind. When a multi-step system goes wrong, it usually does not stop. It produces something that looks finished, built on a step that silently did the wrong thing.

---

## AI literacy notes

1. **Two designs, one decision.** Fixed path or model-chosen path. Almost every other property — testability, cost predictability, auditability, how you bound permissions — follows from it.
2. **Reach for the simplest thing that works.** The practitioner literature is consistent: multi-agent arrangements are adopted well before a single well-scoped call has been ruled out, and they cost more in every dimension including debuggability.
3. **Failures live in the seams.** Not usually a bad model output, but a handoff — malformed results consumed as valid, an error caught and swallowed, a loop that never terminates.
4. **Orchestration failures look like success.** The system returns something plausible built on a step that quietly went wrong. This is why they need detection separate from output-quality review.
5. **Each step is reasonable; the sequence may not be.** Reviewing individual steps does not tell you the composition was sound. The trace is the unit of review, not the step.
6. **A dynamic path means an unpredictable reachable surface.** If the model chooses tools at runtime, what the system can touch is decided during execution — a permissions problem, not just an architecture one.
7. **Autonomy is not a maturity level.** Moving from a fixed workflow to a dynamic one is a trade, and moving back after learning something is a normal outcome.

---

## Governance notes

**Core question:** For a completed run, can you reconstruct every step it took — and was the set of steps it *could* have taken ever bounded?

**Watch for:**
- Multi-agent or dynamic routing chosen by default, before a simpler arrangement was tried and found insufficient
- Traces logged only at the endpoints — the request and the final answer — leaving the intermediate steps, the part where failures live, unrecorded
- Errors handled by continuing: a failed step swallowed so the run completes with a partial result presented as whole
- No termination guarantee: nothing bounding step count, wall-clock time, or spend
- Tool selection unbounded at runtime, so the reachable data and systems are decided during execution ([agency](agency-ai-systems.md), [permission model](permission-model-ai.md))
- Sub-agents inheriting the parent's credentials with no separate scoping ([multi-agent systems](multi-agent-systems.md))
- Evaluation at the output only, when the failure that matters happened three steps earlier ([evaluation](evaluation.md))

**Practice:**
- Justify autonomy rather than assuming it: state what the task requires that a defined path cannot supply
- Trace every step — inputs, tool calls, results, errors — at a fidelity that lets a run be replayed, not just summarized
- Make failures loud: a step that fails should halt or escalate, never be absorbed into a plausible-looking completion
- Bound every run: maximum steps, timeout, spend ceiling, and a defined stop that has been exercised
- Scope tools and credentials per step rather than per system, and do not let sub-agents inherit by default
- Evaluate the trace, not only the answer, and include the seams in what you test
- Place [human checkpoints](human-in-the-loop.md) at irreversibility and cost, not at arbitrary step counts

**Key accountability owner:** the system owner, who owns the *composition* — because every individual component can be sound while the assembled behavior is not, and no component owner is accountable for the sequence.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The workflow/agentic distinction is stable and the fault taxonomy is peer-reviewed and matches practitioner experience. **Less settled:** when autonomy actually pays. The "simplest thing that works" guidance is convergent industry advice from vendors and practitioners rather than comparative study, and the field lacks independent evidence on where dynamic orchestration outperforms a defined workflow. Evaluation of multi-step systems is also immature — most available tooling scores final outputs, which is precisely the wrong place to catch the failures this entry describes. Treat specific architectural patterns as current practice, not settled method.

---

## Related concepts

- [AI Agent](ai-agent.md) — the component whose runtime path-choosing creates the harder orchestration case
- [Multi-Agent Systems](multi-agent-systems.md) — the arrangement most often adopted before it is needed
- [Tool Use](tool-use.md) — the calls being sequenced, and where the seams are
- [Agency (AI Systems)](agency-ai-systems.md) — a dynamic path is what makes the reachable surface hard to bound
- [Permission Model (AI)](permission-model-ai.md) — where per-step scoping is actually enforced
- [Harness Paradigm](harness-paradigm.md) — orchestration is the control layer that paradigm names
- [Observability (AI Systems)](observability.md) — traces are the only way an assembled run becomes reviewable
- [Audit Trail (AI)](audit-trail-ai.md) — the record that makes a completed run reconstructable
- [Evaluation (AI Systems)](evaluation.md) — must reach the trace, not just the endpoint
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the family the seam failures belong to
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — checkpoints placed by consequence within a sequence
- [Context (AI Systems)](context-ai-systems.md) — what each step receives, assembled by the orchestrator
- [Scalability (AI Systems)](scalability-ai-systems.md) — step count multiplies cost and latency non-obviously
- Orchestration drift — the slow divergence of a running arrangement from its designed one

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-128 | Shah, M.B.; Morovati, M.M.; Rahman, M.M.; Khomh, F. — *Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes* (2026) · [link](https://arxiv.org/abs/2603.06847) | The empirical fault taxonomy behind this entry's central claim: failures concentrate in handoffs and integration seams rather than in model output, and frequently present as completion. |
| SRC-104 | Anthropic — *Building Effective Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | The workflow-versus-agentic distinction and the "simplest arrangement that works" guidance. ⚠️ Vendor-produced — widely adopted framing, cited as convergent practice rather than authority. |
| SRC-152 | Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N.V.; Wiest, O.; Zhang, X. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* (IJCAI, 2024) · [link](https://www.ijcai.org/proceedings/2024/890) | Coordination architectures and their open problems, from a peer-reviewed survey rather than vendor guidance. |
| SRC-061 | Olafenwa, A. (Towards Data Science) — *Single Agent vs Multi-Agent: When to Build a Multi-Agent System* (2026) · [link](https://towardsdatascience.com/single-agent-vs-multi-agent-when-to-build-a-multi-agent-system/) | The practitioner case for restraint, and the failure patterns that follow premature multi-agent adoption. ⚠️ Practitioner article — background reference. |
| SRC-103 | Model Context Protocol project (Anthropic) — *What is the Model Context Protocol (MCP)?* (2024) · [link](https://modelcontextprotocol.io/docs/getting-started/intro) | The standardized integration layer between an orchestrator and its tools — where the seams are made explicit rather than bespoke. ⚠️ Vendor-originated standard. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places composed-system behavior inside a risk lifecycle, where the assembled system is the unit of assessment rather than each component. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Trace every step at replay fidelity, make failures halt rather than absorb, bound steps/time/spend, and scope tools per step rather than per system. |
| **Organizational** | Nobody owns a sequence by default — every component can be sound while the composition is not. Autonomy should be justified against a defined path, not adopted as a default. |
| **Client-facing** | Explains why multi-step AI systems need step-level logging and defined stopping points, and why "it returned an answer" is not evidence the process worked. |
| **LLM-native** | Fixed path versus model-chosen path determines testability, auditability and how permissions can be bounded. A runtime-composed path means a runtime-decided reachable surface. |

---

*Last updated: v1.0 · August 2026*
