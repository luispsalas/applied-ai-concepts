<!--meta
category: System Architecture
short: The named arrangements for splitting what a system decides at runtime from what is fixed in code — and each one puts the power to refuse somewhere different
aliases: [agentic design, agent design patterns, agentic patterns, reflection pattern, orchestrator-worker, evaluator-optimizer, planning pattern, how should I structure my agent]
tags: [Agents, Architecture, AI Literacy]
established: emerging
-->
# Agentic Design Patterns

> **Term status — Emerging.** Real and in use, but definitions still vary between sources — see the confidence level for what is unsettled.

## One-line essence
Reusable structures for arranging what an AI system decides at runtime versus what is fixed in code — and each arrangement puts the power to refuse in a different place.

---

## Technical definition

An agentic design pattern is a reusable solution to a recurring coordination problem that arises when a model decides at runtime rather than following a fixed code path. The vocabulary is borrowed directly from software design patterns, and it serves the same purpose: naming an arrangement so it can be chosen deliberately and discussed.

**Two catalogs anchor the field, and they do not match.** Andrew Ng named four in *The Batch* (March 2024): *"Reflection, Tool use, Planning and Multi-agent collaboration."* Anthropic's *Building Effective Agents* sets out a different, more implementation-shaped set — prompt chaining, routing, parallelization, orchestrator–workers, evaluator–optimizer — under an explicit workflow-versus-agent distinction. Later trade catalogs extend both. **There is no canonical list, and that is precisely why this term is `emerging` rather than established.**

**It is not [orchestration](orchestration-ai-systems.md), though it is often used as though it were.** Orchestration is the control *layer* — the thing that actually decides what runs and in what order. A design pattern is the *shape* that layer is arranged in. One is a component; the other is vocabulary for describing arrangements of it.

**The property this entry exists to name: each pattern relocates the authority to refuse, and the catalogs describe them by capability instead.**

| Pattern | What it does | Where the power to say no sits |
|---|---|---|
| **Reflection** | The model critiques and revises its own output | **Nowhere outside the model.** Self-review with no external standard |
| **Tool use** | The model calls external functions for what its weights lack | At the tool boundary — if permissions are enforced there ([agent hooks](agent-hooks.md)) |
| **Planning** | A goal is decomposed into steps, adapting when one fails | Diffuse — the plan is composed at runtime, so the reachable surface is not known in advance |
| **Orchestrator–workers** | One component directs others | Concentrated in the orchestrator, which becomes a single point of authority |
| **Evaluator–optimizer** | One component grades another's output and drives revision | In an internal grader **whose standard nobody outside the system set** ([LLM-as-judge](llm-as-judge.md)) |
| **Multi-agent collaboration** | Several agents with distinct roles | Distributed, which in practice often means **nowhere identifiable** ([multi-agent systems](multi-agent-systems.md)) |

**The most useful guidance in the literature is the conservative kind, and it runs against commercial pressure.** Anthropic's own advice is to prefer the simplest arrangement that works and to reach for autonomous loops only when a defined workflow genuinely cannot serve — because a workflow's possible executions are enumerable, and an agentic path is composed during operation ([orchestration](orchestration-ai-systems.md)).

**The characteristic failure is adoption by name.** A pattern names a structure, not a fit. *"We use orchestrator–workers"* says how components are wired; it says nothing about whether that wiring suits the task, and empirical fault taxonomies find that agentic failures concentrate in the seams between components rather than inside them.

---

## Plain-language version

Once you let an AI system make its own decisions about what to do next, there turn out to be a handful of recurring ways to arrange it. People have given those arrangements names — reflection, planning, orchestrator and workers, and so on — the way builders name a truss or an arch.

The names are useful. They let a team say what they built in two words instead of a diagram. Two people published influential lists, they do not match, and later lists extend both. **There is no agreed catalog**, which is worth knowing before anyone cites one as though it were a standard.

Here is what the lists tend not to say. Each arrangement decides *who gets to stop the thing*.

If the system checks its own work, nobody outside it is checking — it can be confidently wrong twice. If one component grades another, there is now an internal examiner whose marking scheme nobody outside chose. If one component directs several others, that one component holds all the authority. If several agents share the work, responsibility gets spread until it is hard to say which one should have refused.

None of those are wrong. They are just different answers to a question the catalogs mostly do not ask, and it is the question that matters when something goes wrong.

One more thing worth hearing, because it cuts against what vendors say: the strongest advice in this area is to use the *simplest* arrangement that works. A fixed sequence you wrote down can be tested, because you know every path it can take. Once the system composes its own path at runtime, you find out what it can reach by watching it.

---

## AI literacy notes

1. **A pattern names a structure, not a fit.** Saying which one you use describes wiring, not suitability.
2. **The catalogs disagree** — two influential lists, neither canonical, later ones extending both.
3. **This is not orchestration.** Orchestration is the control layer; a pattern is the shape it is arranged in.
4. **Each pattern relocates the authority to refuse**, which is the property the catalogs consistently omit.
5. **Reflection is self-review**, so a confident error survives it — no external standard is involved.
6. **Evaluator–optimizer creates an internal grader** whose criteria nobody outside the system set.
7. **Simpler is the standing advice**, including from vendors who sell the complex option.
8. **Failures concentrate in the seams** between components, not inside them, which is where testing tends not to look.

---

## Governance notes

**Core question:** For each arrangement in this system, what can actually stop it — a person, a component, or nothing — and was that chosen or inherited from a pattern someone copied?

**Watch for:**
- A pattern adopted by name, with no statement of why it suits this task ([AI use case](ai-use-case.md))
- Reflection or self-critique described in assurance material as a quality control, when nothing external is checking ([evaluation](evaluation.md))
- An evaluator component whose grading criteria were never reviewed by anyone accountable for the outcome ([LLM-as-judge](llm-as-judge.md))
- An autonomous loop chosen where a defined workflow would serve, so the reachable surface stops being enumerable ([orchestration](orchestration-ai-systems.md))
- Multi-agent arrangements where no single component is accountable for a refusal that should have happened ([accountability](accountability-ai-systems.md))
- Enforcement assumed at the tool boundary without checking whether the hook can actually block ([agent hooks](agent-hooks.md))
- Planning patterns given unbounded steps, retries or spend, so failure is expensive rather than merely wrong ([sandboxing](sandboxing.md))
- Testing that exercises components but not the seams between them, where faults concentrate ([failure modes](failure-modes-ai-systems.md))

**Practice:**
- **Write down, per pattern, what can refuse and who owns that refusal.** This is one line per component and it is almost never recorded
- **Justify the pattern against the task**, not against a catalog — and record the reason, since it is the thing that will be questioned later
- Prefer the simplest arrangement whose paths you can enumerate; escalate to runtime autonomy only when a defined workflow demonstrably cannot serve
- Where a component grades another, treat its criteria as a governed artifact with a named owner
- Bound steps, retries and spend on any planning or looping pattern before deployment
- Test the seams explicitly — malformed hand-offs, swallowed errors, loops that neither complete nor terminate
- Keep a [human checkpoint](human-in-the-loop.md) at irreversibility regardless of pattern; no arrangement supplies oversight by itself

**Key accountability owner:** whoever chose the architecture — because the pattern decides where refusal can happen, and it is normally selected on engineering grounds by someone who was never asked where accountability should sit.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium — and the reason is the catalogs, not the patterns.** The individual arrangements are real, widely implemented and documented by named sources: Ng's four are quoted verbatim from *The Batch*, and Anthropic's set comes with an explicit workflow-versus-agent distinction. **What is unsettled is the catalog itself** — there is no canonical list, the two influential ones do not match, and most later enumerations are trade publications extending them without adding evidence. That is why this is filed `emerging`, and why the entry names patterns rather than claiming a taxonomy.

**The oversight-profile table is this wiki's own framing, not a finding.** No source consulted organizes patterns by where refusal can occur; the column is reasoned from what each arrangement does, and it is offered as a question to ask rather than as an established classification. **Sourcing here is also weaker than the corpus average**: two of the anchors are vendor- or practitioner-authored, and the trade catalogs that dominate search results are largely uncited. Treat specific pattern names as vocabulary that will shift, and the governance question as the durable part.

---

## Related concepts

- [Orchestration (AI Systems)](orchestration-ai-systems.md) — the control layer these are arrangements of; the distinction most often collapsed
- [AI Agent](ai-agent.md) — the thing being arranged
- [Multi-Agent Systems](multi-agent-systems.md) — one pattern, and the one where accountability disperses fastest
- [Tool Use](tool-use.md) — a pattern in its own right, and the boundary where enforcement is possible
- [Agent Hooks](agent-hooks.md) — where a refusal is actually implemented, or only observed
- [LLM-as-Judge](llm-as-judge.md) — the evaluator half of evaluator–optimizer, with its known biases
- [Agency (AI Systems)](agency-ai-systems.md) — how much latitude the arrangement grants
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the seams where agentic faults concentrate
- [Sandboxing](sandboxing.md) — bounding a looping pattern regardless of its shape
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the refusal no pattern supplies on its own

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-276 | Ng, Andrew (DeepLearning.AI) — *The Batch*, issue 242 (March 27, 2024) · [link](https://www.deeplearning.ai/the-batch/issue-242/) | The first influential enumeration, quoted verbatim: *"Last week, I described four design patterns for AI agentic workflows that I believe will drive significant progress this year: Reflection, Tool use, Planning and Multi-agent collaboration."* ⚠️ A newsletter letter, not a paper — cite for the naming and its influence, not as evidence the patterns work. |
| SRC-104 | Anthropic — *Building Effective Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | The second anchor catalog and the workflow-versus-agent distinction, plus the conservative guidance this entry highlights: prefer the simplest arrangement that works. ⚠️ Vendor-authored — noted because the advice runs *against* the author's commercial interest, which is why it is worth quoting. |
| SRC-128 | Shah, M.B.; Morovati, M.M.; Rahman, M.M.; Khomh, F. — *Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes* (2026) · [link](https://arxiv.org/abs/2603.06847) | Empirical support for the seams claim: agentic faults concentrate between components rather than inside them, which is what makes pattern choice a reliability decision. |
| SRC-152 | Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N.V.; Wiest, O.; Zhang, X. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* (IJCAI, 2024) · [link](https://www.ijcai.org/proceedings/2024/890) | Peer-reviewed treatment of the multi-agent pattern and its coordination failure modes — the strongest-sourced entry in the catalog. |
| SRC-034 | Chase, Harrison (LangChain) — *The Agent Development Lifecycle* (2026) · [link](https://www.langchain.com/blog/the-agent-development-lifecycle) | Practitioner framing of pattern choice as a lifecycle decision with checkpoints proportional to consequence. ⚠️ Vendor-authored. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Write down, per pattern, what can refuse and who owns that refusal. Prefer arrangements whose paths you can enumerate, and test the seams rather than the components. |
| **Organizational** | The architecture choice decides where a refusal can happen, and it is normally made on engineering grounds by someone never asked where accountability should sit. |
| **Client-facing** | Explains why two systems described the same way can behave very differently under failure, without requiring the architecture to be explained. |
| **LLM-native** | The catalogs describe patterns by capability and omit the thing that matters: each one relocates the authority to refuse. Reflection puts it nowhere outside the model. |

---

*Last updated: v1.0 · September 2026*
