<!--meta
category: System Architecture
short: Multiple AI agents with different roles working together on a task — coordination and division of labor instead of one model doing everything
aliases: [agent swarm, multiple agents, agent teams, agent collaboration, agent handoff]
tags: [Agents, Architecture]
established: established
-->
[Applied AI Concepts](../README.md) › [System Architecture](../glossary/categories.md#system-architecture) › Multi-Agent Systems

# Multi-Agent Systems

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Multiple AI agents, often with different roles or specializations, working together on a task — coordination and division of labor instead of one model doing everything.

---

## Technical definition

An architecture in which several LLM-based agents, each with its own profile, tools, and objective, collaborate to complete a task that is decomposed across them rather than handled by a single agent. Surveys of LLM-based multi-agent (LLM-MA) systems characterize them along four axes: the **environment** the agents operate or simulate in, **agent profiling** (the role each agent is given), **communication** (how agents exchange information — cooperative, debate, or competitive; structured as layered, decentralized, or centralized), and **capability acquisition** (how agents improve from feedback or memory).

The most common production pattern is **orchestrator–workers**: a central model dynamically decomposes a task, delegates sub-tasks to worker models, and synthesizes their results — as distinct from a fixed workflow, where the decomposition is written by a developer in advance rather than decided at runtime. Other vendors document the same shape under their own names: OpenAI's *manager pattern*, in which a central model orchestrates specialized agents through tool calls, and Google's *Coordinator* pattern.

Multi-agent is a design choice with a cost, not a default upgrade. The decision framework in practice: use multiple agents when a task has genuinely separable sub-problems, requires distinct tool sets or permissions per role, or benefits from an adversarial arrangement (one agent generating, another critiquing). Keep a single agent when the coordination overhead — extra latency, token cost, and failure surface — exceeds the benefit of specialization. Vendor guidance agrees on the default: OpenAI's is *"to maximize a single agent's capabilities first"*, and Microsoft's adds multiple agents only when a single agent cannot reliably handle a task because of prompt complexity, tool overload or security requirements.

**Which models go in the system is itself a design choice, and where it has been measured rather than assumed, more is not better.** A study of model-pool selection across 23 models (six architecture families, 2B to 1.6T parameters) on three science-reasoning benchmarks tested eight ways of choosing the pool — by size, by architectural family, by an LLM's recommendation, by measured accuracy, by correct-answer diversity, by error diversity, and by two accuracy-weighted combinations — across a routing system and two answer-combining systems (majority vote and an LLM judge). Its result: *"more models nearly always decreases performance"*, and most deliberate groupings scored below the best single model in the pool and often below a randomly chosen set. Grouping models from one family did best, though in most cases that meant *"the least detriment to performance rather than a large improvement"*. The same study found that domain-specialized models did not outperform the generalist they were fine-tuned from, even in their own specialty, so a pool cannot be assembled from model cards alone. Two caveats bound the result: the degradation is specific to **heterogeneous** pools — the study's baseline systems built from instances of one model still improved as they grew more complex — and tool use and retrieval were disabled so the models could be compared, which removes a capability most deployed systems have.

Note that "multi-agent system" is an established term in distributed AI that long predates LLMs; the LLM-based variety inherits the name but not the formal coordination guarantees of the classical literature.

---

## Plain-language version

Instead of asking one AI to do a whole complicated job, you split the job across several — one to plan, one to research, one to check the work. Each has a narrow role. It can handle bigger problems than one AI alone, but there are now several things that can go wrong, and the failures are harder to trace because no single agent saw the whole task.

---

## AI literacy notes

1. **More agents means more failure surface, not more reliability.** An empirical fault taxonomy of agentic AI found that failures concentrate in orchestration, state handling, and environment interaction — not in the model itself. Adding agents adds exactly those three things. Reliability also compounds downward: a chain of steps each individually reliable can still fail often overall, because the per-step success rates multiply.
2. **Specialization is a governance tool, not just a performance one.** Giving each agent the narrowest role and the smallest tool set it needs is the multi-agent form of least privilege — it bounds what any single compromised or malfunctioning agent can do.
3. **Accountability blurs exactly where it matters most.** When several agents contribute to an outcome, "which agent decided this?" becomes a real question — and it is the question an audit will ask. Red-team studies of autonomous agents in live environments have documented unauthorized compliance, identity spoofing, and partial system takeover; attributing those events requires per-agent logging designed in from the start.
4. **A bigger roster is not a better system.** The intuition that adding a model adds a perspective does not survive measurement: in the pool-selection study above, enlarging the candidate pool usually made the system worse than its own best member, and the gap between what a pool *could* achieve if it always picked the right answer and what it actually achieved was wide. Treat the choice of models as a decision to test, not to reason about.
5. **The word is doing a lot of work.** Vendors describe as "multi-agent" everything from a genuinely dynamic orchestrator to a hard-coded three-step script. Ask what decides the decomposition — a model at runtime, or a developer in advance. Only the first is meaningfully multi-agent.

---

## Governance notes

**Core question:** When several agents contribute to an outcome, can you reconstruct which one did what — and who is answerable for the result?

**Watch for:**
- Per-agent actions that are not individually logged, making post-hoc attribution impossible
- Agents inheriting a shared, over-broad set of credentials instead of role-scoped permissions
- Coordination complexity adopted for its own sake, where a single agent or a fixed workflow would do
- A roster of models chosen from model cards, vendor claims or an LLM's recommendation, with no measurement of what the combination actually does
- Failures that are silent because one agent's degraded output is accepted as input by the next

**Practice:**
- Log agent identity, inputs, tool calls, and outputs at each hop — the [audit trail](audit-trail-ai.md) must be per-agent, not per-system
- Scope tools and credentials per role; treat every agent as a separate principal
- Set explicit stop conditions and budgets — step limits, token limits, wall-clock limits — so a coordination loop cannot run indefinitely
- Measure the system against the best single model in it, and keep that comparison as a release gate — a multi-agent system that loses to one of its own members is a cost with no benefit
- Require a single named owner for the system as a whole, regardless of how many agents it contains

**Key accountability owner:** the system owner — accountability does not distribute across agents just because work does.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The architectural patterns and their trade-offs are documented in peer-reviewed surveys and primary engineering sources, and the failure evidence is empirical. Controlled comparison has now started to arrive — the pool-selection study above measures the single-versus-multi question rather than asserting it — but it covers science-reasoning benchmarks with tool use disabled, on three simple architectures, so it bounds a claim rather than settling one. The field is young and moving: coordination protocols are unsettled, production evidence is still mostly case studies, and claims about when multi-agent beats single-agent remain contested.

---

## Related concepts

- [AI Agent](ai-agent.md) — the unit being multiplied; every constraint that applies to one agent applies to each of these, plus coordination
- [Harness Paradigm](harness-paradigm.md) — coordination logic lives in the harness, not the models; multi-agent systems are a harness design problem
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — orchestration, state, and hand-off failures are specific to this architecture
- [Audit Trail (AI)](audit-trail-ai.md) — attribution across agents is only possible if it was logged per agent
- [Observability (AI Systems)](observability.md) — reconstructing a multi-agent run requires tracing across hops, not inspecting one output
- [Types of AI Systems](types-of-ai-systems.md) — the high-autonomy end of the taxonomy, where oversight requirements concentrate
- [Tool Use](tool-use.md) — agents coordinate by acting, and they act through tools
- [Orchestration (AI Systems)](orchestration-ai-systems.md) — the general coordination problem of which multi-agent is one instance

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-152 | Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N.V.; Wiest, O.; Zhang, X. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* (IJCAI 2024) · [link](https://www.ijcai.org/proceedings/2024/890) | Peer-reviewed anchor: the four-axis characterization (environment, profiling, communication, capability acquisition) and open challenges. |
| SRC-378 | Marjanović, S.V.; Xu, J.; Laptev, A.; Nalbandyan, G.; Arakelyan, E.; Bakhaturina, E. — *Mo' Models, Mo' Problems: How to best select model pools when designing Multi-Agent Systems* (preprint, 2026) · [link](https://arxiv.org/abs/2609.17306) | Controlled comparison of eight model-pool selection strategies across routing, majority-vote and LLM-judge architectures: enlarging a heterogeneous pool usually degrades performance below the best single model; same-family pools fare best; fine-tuned specialists did not beat their generalist base model. ⚠️ Five of six authors are at NVIDIA; the benchmarks are science-reasoning only and tool use was disabled. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Orchestrator–workers pattern; the workflow-vs-agent distinction that separates dynamic from pre-written decomposition. ⚠️ Vendor-authored. |
| SRC-372 | OpenAI — *A practical guide to building agents* (2025) · [link](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) | The manager pattern (a central model orchestrating specialized agents through tool calls) and the decentralized pattern (agents handing off to one another); the recommendation to maximize a single agent's capabilities first. ⚠️ Vendor-authored. |
| SRC-373 | Microsoft — *AI Agent Orchestration Patterns* (Azure Architecture Center, 2026) · [link](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | Multi-agent orchestration patterns and when the added complexity is justified: prompt complexity, tool overload or security requirements a single agent cannot handle. ⚠️ Vendor-authored. |
| SRC-374 | Blount, A.; Gulli, A.; Saboo, S.; Zimmermann, M.; Vuskovic, V. (Google) — *Introduction to Agents* (Kaggle whitepaper, updated May 2026) · [link](https://www.kaggle.com/whitepaper-introduction-to-agents) | The Coordinator pattern: a manager agent segments a request and routes sub-tasks to specialist agents, then aggregates their responses. ⚠️ Vendor-authored. |
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

*Last updated: v1.2 · September 2026*
