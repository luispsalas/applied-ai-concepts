# Multi-Agent Systems

## One-line essence
Multiple AI agents, often with different roles or specializations, working together on a task — coordination and division of labor instead of one model doing everything.

---

## Technical definition

An architecture in which several LLM-based agents, each with its own profile, tools, and objective, collaborate to complete a task that is decomposed across them rather than handled by a single agent. Surveys of LLM-based multi-agent (LLM-MA) systems characterize them along four axes: the **environment** the agents operate or simulate in, **agent profiling** (the role each agent is given), **communication** (how agents exchange information — cooperative, debate, or competitive; structured as layered, decentralized, or centralized), and **capability acquisition** (how agents improve from feedback or memory).

The most common production pattern is **orchestrator–workers**: a central model dynamically decomposes a task, delegates sub-tasks to worker models, and synthesizes their results — as distinct from a fixed workflow, where the decomposition is written by a developer in advance rather than decided at runtime.

Multi-agent is a design choice with a cost, not a default upgrade. The decision framework in practice: use multiple agents when a task has genuinely separable sub-problems, requires distinct tool sets or permissions per role, or benefits from an adversarial arrangement (one agent generating, another critiquing). Keep a single agent when the coordination overhead — extra latency, token cost, and failure surface — exceeds the benefit of specialization.

Note that "multi-agent system" is an established term in distributed AI that long predates LLMs; the LLM-based variety inherits the name but not the formal coordination guarantees of the classical literature.

---

## Plain-language version

Instead of asking one AI to do a whole complicated job, you split the job across several — one to plan, one to research, one to check the work. Each has a narrow role. It can handle bigger problems than one AI alone, but there are now several things that can go wrong, and the failures are harder to trace because no single agent saw the whole task.

---

## AI literacy notes

1. **More agents means more failure surface, not more reliability.** An empirical fault taxonomy of agentic AI found that failures concentrate in orchestration, state handling, and environment interaction — not in the model itself. Adding agents adds exactly those three things. Reliability also compounds downward: a chain of steps each individually reliable can still fail often overall, because the per-step success rates multiply.
2. **Specialization is a governance tool, not just a performance one.** Giving each agent the narrowest role and the smallest tool set it needs is the multi-agent form of least privilege — it bounds what any single compromised or malfunctioning agent can do.
3. **Accountability blurs exactly where it matters most.** When several agents contribute to an outcome, "which agent decided this?" becomes a real question — and it is the question an audit will ask. Red-team studies of autonomous agents in live environments have documented unauthorized compliance, identity spoofing, and partial system takeover; attributing those events requires per-agent logging designed in from the start.
4. **The word is doing a lot of work.** Vendors describe as "multi-agent" everything from a genuinely dynamic orchestrator to a hard-coded three-step script. Ask what decides the decomposition — a model at runtime, or a developer in advance. Only the first is meaningfully multi-agent.

---

## Governance notes

**Core question:** When several agents contribute to an outcome, can you reconstruct which one did what — and who is answerable for the result?

**Watch for:**
- Per-agent actions that are not individually logged, making post-hoc attribution impossible
- Agents inheriting a shared, over-broad set of credentials instead of role-scoped permissions
- Coordination complexity adopted for its own sake, where a single agent or a fixed workflow would do
- Failures that are silent because one agent's degraded output is accepted as input by the next

**Practice:**
- Log agent identity, inputs, tool calls, and outputs at each hop — the [audit trail](audit-trail-ai.md) must be per-agent, not per-system
- Scope tools and credentials per role; treat every agent as a separate principal
- Set explicit stop conditions and budgets — step limits, token limits, wall-clock limits — so a coordination loop cannot run indefinitely
- Require a single named owner for the system as a whole, regardless of how many agents it contains

**Key accountability owner:** the system owner — accountability does not distribute across agents just because work does.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The architectural patterns and their trade-offs are documented in peer-reviewed surveys and primary engineering sources, and the failure evidence is empirical. But the field is young and moving: coordination protocols are unsettled, production evidence is still mostly case studies rather than controlled comparison, and claims about when multi-agent beats single-agent remain contested.

---

## Related concepts

- [AI Agent](ai-agent.md) — the unit being multiplied; every constraint that applies to one agent applies to each of these, plus coordination
- [Harness Paradigm](harness-paradigm.md) — coordination logic lives in the harness, not the models; multi-agent systems are a harness design problem
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — orchestration, state, and hand-off failures are specific to this architecture
- [Audit Trail (AI)](audit-trail-ai.md) — attribution across agents is only possible if it was logged per agent
- [Observability](observability.md) — reconstructing a multi-agent run requires tracing across hops, not inspecting one output
- [Types of AI Systems](types-of-ai-systems.md) — the high-autonomy end of the taxonomy, where oversight requirements concentrate
- Tool Use — agents coordinate by acting, and they act through tools
- Orchestration (AI Systems) — the general coordination problem of which multi-agent is one instance

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-152 | Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N.V.; Wiest, O.; Zhang, X. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* (IJCAI 2024) · [link](https://www.ijcai.org/proceedings/2024/890) | Peer-reviewed anchor: the four-axis characterization (environment, profiling, communication, capability acquisition) and open challenges. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Orchestrator–workers pattern; the workflow-vs-agent distinction that separates dynamic from pre-written decomposition. ⚠️ Vendor-authored. |
| SRC-061 | Olafenwa, Ayoola — *Single Agent vs Multi-Agent: When to Build a Multi-Agent System* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/single-agent-vs-multi-agent-when-to-build-a-multi-agent-system/) | Practitioner decision framework for single vs multi-agent; role specialization and the failure modes of over-complex single agents. |
| SRC-128 | Shah, M.B.; Morovati, M.M.; Rahman, M.M.; Khomh, F. — *Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes* (2026) · [link](https://arxiv.org/abs/2603.06847) | Empirical evidence that agentic failures arise from orchestration, state, and environment interaction rather than the model alone. |
| SRC-045 | Shapira, Natalie et al. — *Agents of Chaos* (preprint, 2026) · [link](https://arxiv.org/abs/2602.20021) | Red-team study of autonomous agents in a live environment: unauthorized compliance, identity spoofing, partial system takeover. |
| SRC-153 | InfoQ — *Grab's Multi-Agent Support System* (2026) · [link](https://www.infoq.com/news/2026/05/grab-multi-agent-support-system/) | Production case study of a deployed multi-agent system in customer support. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The single-vs-multi decision is an architecture choice with direct cost, latency, and debuggability consequences — not a capability upgrade. |
| **Organizational** | Multi-agent systems distribute work but not accountability; oversight and ownership must be defined before deployment, not after an incident. |
| **Client-facing** | Answers "is this one AI or several?" — and sets expectations about why a more capable system can also be a less predictable one. |
| **LLM-native** | Coordination, not model capability, is the current bottleneck; the interesting design work is in the harness between the agents. |

---

*Last updated: v1.0 · August 2026*
