# AI Agent

## One-line essence
A language model that doesn't just respond — it plans, acts, and iterates across multiple steps to complete a task.

---

## Technical definition

An AI agent is a language model configured to pursue a goal through a sequence of actions — perceiving inputs, planning steps, invoking tools, observing results, and adjusting behavior based on feedback — rather than producing a single output in response to a single input.

What distinguishes an agent from a standard model call:

- **Tool use** — agents invoke external capabilities (web search, code execution, APIs, file systems, databases, email) as part of their reasoning process
- **Multi-step execution** — agents decompose goals into action sequences, executing them in order or in parallel across multiple model calls
- **State and memory** — agents track what has been done, what has been observed, and what remains; state persists across steps
- **Feedback loops** — agents observe the results of their actions and revise their plan accordingly (canonical pattern: Reason → Act → Observe, repeated until goal is reached or a stopping condition is met)

Agent architectures vary in autonomy: from simple tool-augmented models executing linear pipelines, to fully autonomous agents that self-direct across long horizons with minimal human intervention. The appropriate level of autonomy is a governance decision, not a technical default.

---

## Plain-language version

A regular AI model responds to what you ask. An AI agent is given a goal and figures out the steps to get there — using tools, taking actions, checking the results, and adjusting as it goes.

You might ask a model to summarize a document. You'd ask an agent to research a topic, cross-reference sources, draft a report, and flag anything it couldn't verify — without you specifying each step.

The capability gain is real. So is the governance challenge: an agent that can act in the world — sending emails, writing files, calling APIs, executing code — needs controls that a model answering questions does not.

---

## AI literacy notes

Agents represent a qualitative shift in what AI systems do — from generating text to taking actions. Three implications practitioners need to carry:

1. **Capability and permission diverge.** An agent that can access a tool is not automatically authorized to use it in every context. The harness defines what the agent is allowed to do; the model's capabilities are a separate question. A capable agent with no permission model is a liability, not an asset.
2. **Failure modes compound.** A single-step model failure affects one output. An agent failure propagates — each step builds on the last, so an early error amplifies rather than isolates. Long-horizon agents require checkpointing, not just output review.
3. **Human oversight must be designed in.** Agents acting autonomously across long chains of action are the strongest argument for explicit HITL design. "Someone will check" is not a control when the agent has already acted.

---

## Governance notes

**Core question:** Is the agent's permission boundary explicitly defined — and does the harness enforce it structurally, or is it assumed?

**Watch for:**
- Capability assumed as permission: if the agent can call a tool, it does — because no one specified otherwise. Tool access should be explicitly granted, not implicitly inherited from model capability.
- Failure propagation unaddressed: agents that continue executing after producing an anomalous intermediate result, compounding an early error across subsequent steps without a human gate.
- Long-horizon autonomy without HITL checkpoints: the longer the execution chain, the more consequential an unchecked error becomes. Checkpoint design should scale with execution length and action reversibility.

**Practice:**
- Define the permission model before deployment: which tools can the agent invoke, under what conditions, with what constraints. This is a harness-layer decision, not a prompt-level one.
- Design HITL checkpoints proportional to action consequence: irreversible or high-impact actions (send, delete, publish, execute payment) warrant a human gate; reversible or low-impact actions may not. Explicit checkpoints are not a performance tax — they are a design decision.

**Key accountability owner:** Agent owner — the role responsible for the agent's permission model, HITL checkpoint design, and the harness configuration that mediates between the agent and the world.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** AI agents are a recognized and widely deployed architecture (2023–present). Core patterns — tool use, ReAct reasoning loop, memory management — are stable. Orchestration frameworks, multi-agent coordination, and long-horizon reliability are active development areas.

---

## Related concepts

- [Harness Paradigm](harness-paradigm.md) — agents require especially deliberate harness design; the permission model, tool contracts, and HITL checkpoints are all harness-layer decisions
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — agents acting across multiple steps are the primary driver for explicit, checkpoint-based HITL design; autonomy without oversight is a governance gap
- [Context Engineering](context-engineering.md) — agent execution depends on well-constructed context at each step; context engineering at the system level determines agent reliability across the full chain
- [Retrieval-Augmented Generation (RAG)](rag.md) — agents frequently incorporate RAG as a tool-use step, retrieving context dynamically during execution
- Multi-Agent Systems — architectures in which multiple agents coordinate, delegate, and check each other's outputs; extends the single-agent permission and oversight challenges
- Tool Use — the mechanism by which agents interact with external systems; requires explicit contract definition and permission scoping

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-021 | Yao, S. et al. — *ReAct: Synergizing Reasoning and Acting in Language Models* (arXiv:2210.03629, 2022) · [link](https://arxiv.org/abs/2210.03629) | Canonical paper introducing the ReAct pattern: interleaved reasoning and acting; Reason → Act → Observe loop; empirical evidence that reasoning traces improve agent reliability on multi-step tasks. Foundational architecture reference. |
| SRC-022 | Anthropic — *How tool use works* (documentation, 2026) · [link](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/how-tool-use-works) | Agentic loop mechanics (Reason → Act → Observe), client vs. server tool execution, and when to use tools vs. prose. (The original *Build effective agents* page was reorganized into the agents-and-tools section May 2026; the agent design-pattern content moved to Anthropic's engineering blog — see SRC-104.) |
| SRC-104 | Anthropic — *Building Effective AI Agents* (engineering blog, 2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Orchestrator-subagent patterns: defines the orchestrator-workers workflow (a central LLM decomposes tasks, delegates to worker LLMs, and synthesizes results) alongside prompt chaining, routing, parallelization, and evaluator-optimizer. Also covers pausing for human feedback at checkpoints, guardrails, and sandboxed testing — the primary source for the multi-agent coordination and HITL-integration claims in this entry. |
| SRC-055 | Huang, Ken (DistributedApps.ai) — *Intent‑Based Access Control: A Technical Primer* (Substack, March 2026) · [link](https://kenhuangus.substack.com/p/intentbased-access-control-a-technical) | Capability vs. permission distinction: IBAC shifts authorization from "who can do what" to "for what purpose, under what conditions" — separates what an agent *can* do from what it is *permitted* to do at runtime. |
| SRC-045 | Shapira, Natalie et al. — *Agents of Chaos* (arXiv:2602.20021, 2026) · [link](https://arxiv.org/abs/2602.20021) | Failure propagation in multi-step systems: red-team study documenting 11 empirical failure cases (unauthorized compliance, identity spoofing, partial system takeover) where errors cascade across an agent's action sequence. |
| SRC-034 | Chase, Harrison (LangChain) — *The Agent Development Lifecycle* (2026) · [link](https://www.langchain.com/blog/the-agent-development-lifecycle) | Checkpoint design proportional to consequence: documents tool access controls, sandboxed execution, durable execution, and HITL gates as lifecycle controls scaled to the risk of the action. |
| SRC-118 | Sutter, Michal — *Claude Code Guide 2026: 25 Features with Examples + Demo* (MarkTechPost, 2026) · [link](https://www.marktechpost.com/2026/06/14/claude-code-guide-2026-25-features-with-examples-demo/) | Third-party analysis of a deployed multi-step agentic system's extensibility primitives: subagent delegation, hooks (event-triggered controls), MCP server integrations, and permission-scoped skills. Grounds the governance notes on harness-layer permission design and the literacy note that capability and permission are distinct concerns. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core architectural concept for building AI systems that do more than respond. Informs tool contract design, state management, orchestration framework selection, and HITL checkpoint placement. |
| **Organizational** | The concept that explains why AI systems can now take actions, not just generate content — and why that shift requires governance thinking that passive AI use does not. |
| **Client-facing** | Answers "what's the difference between using AI and having AI do things?" — and surfaces the control questions that autonomous action raises for organizational accountability. |
| **LLM-native** | The deployment pattern that makes harness design, HITL, and permission modeling urgent rather than theoretical. Agent architecture is where AI governance becomes a real engineering constraint. |

---

*Last updated: v1.2 · June 2026*
