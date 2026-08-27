# Tool Use

## One-line essence
How an AI model acts on the world rather than just describing it — calling external functions, APIs, and data sources, and folding the results back into its reasoning.

---

## Technical definition

The mechanism by which a language model invokes external capabilities it does not itself possess. The model is given a set of **tool definitions** — each a name, a description, and a typed parameter schema — and, rather than emitting prose, emits a structured request naming a tool and its arguments. That request is executed outside the model; the result is returned into the context, and generation continues with the result available. This request-emission step is what is meant by **function calling**: the model selects the function and binds its parameters, but does not execute anything.

Execution is always external, and where it happens matters for governance: a tool may run **client-side** (the application receives the request, executes it, and returns the result) or **server-side** (the provider executes it on the model's behalf). The distinction determines who holds the credentials and where the audit boundary falls.

Tool use is the action half of the reason–act loop introduced by ReAct, in which a model interleaves reasoning traces with actions and observations rather than reasoning in one pass — the pattern underneath most agent architectures.

The **Model Context Protocol (MCP)** is an open standard for exposing tools, data sources, and workflows to AI applications through a common interface — described by its authors as "a USB-C port for AI applications" — so that an integration is built once and reusable across clients, instead of re-implemented per model or per vendor.

At scale, tool selection becomes its own engineering problem: as a tool catalog grows, models degrade at choosing correctly and begin invoking tools that do not fit the task or do not exist. Practical mitigations include gating (exposing only relevant tools), retrieval over the tool catalog, routing, explicit planning, and fallback logic.

---

## Plain-language version

On its own, a model can only produce text. Tools are how it does things — look up a live price, query a database, send a request, run a calculation. You give it a list of what it's allowed to call and what each one needs; it decides which to use and with what inputs. It never runs anything itself: your system does the running, which is exactly where you get to decide what is permitted.

---

## AI literacy notes

1. **The model chooses; your system acts.** A model emitting a tool call has not done anything yet — it has made a request. Every real-world effect happens in code you control. This is the single most useful thing to understand about tool use, because it locates the control point precisely: permission checks belong at execution, not in the prompt.
2. **Tools convert a text risk into a real-world risk.** A hallucinating chatbot produces a wrong sentence. A hallucinating chatbot with tools produces a wrong action against a live system. The severity of every other failure mode rises the moment tools are attached.
3. **Tool descriptions are prompt surface.** The model chooses tools by reading their descriptions, so those descriptions shape behavior as much as the [system prompt](system-prompt.md) does — and, like any text entering the context, they are a place where injected instructions can hide.
4. **More tools is not better.** Selection accuracy degrades as catalogs grow, and models begin calling tools that don't fit or don't exist. A curated, task-scoped tool set outperforms an exhaustive one.
5. **A standard interface is not a permission model.** MCP makes tools easier to connect; it does not decide which tools an agent should have, under whose credentials, with what approval. That remains a governance decision.

---

## Governance notes

**Core question:** For every tool an AI system can call — who authorized it, under whose credentials does it execute, and is the call recorded?

**Watch for:**
- Tools attached to an agent because they were available, not because the use case required them
- A single broad credential shared across all tools instead of per-tool, least-privilege scoping
- Write, delete, payment, or send actions exposed with no human approval gate
- Tool calls absent from the audit trail — logging the model's text output but not the actions it triggered
- Tool descriptions treated as inert configuration rather than as untrusted, model-visible text

**Practice:**
- Maintain an explicit inventory of tools per system, each with a named owner and a stated reason for being there
- Separate read-only tools from state-changing ones, and gate the second category behind [human approval](human-in-the-loop.md)
- Log every call — tool name, arguments, result, and outcome — as a first-class [audit trail](audit-trail-ai.md) record
- Scope credentials per tool and per agent role; never let tool access default to the operator's own permissions
- Re-review the tool set whenever it grows; treat catalog expansion as a capability change requiring reassessment

**Key accountability owner:** the system owner, jointly with whoever owns the underlying system each tool touches.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The mechanics (structured call emission, external execution, the reason–act loop) are stable and documented in primary sources, and MCP is a published open standard. Less settled: tool-selection techniques at scale are practitioner-reported rather than systematically evaluated, and interoperability standards beyond MCP are still consolidating.

---

## Related concepts

- [AI Agent](ai-agent.md) — an agent is largely a model plus tools plus a loop; tool use is what makes agency more than text generation
- [Harness Paradigm](harness-paradigm.md) — tool definitions, permissions, and execution live in the harness, which is where control over them belongs
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the constraints that decide which calls are permitted to execute
- [Prompt Injection](prompt-injection.md) — tools are what turn an injection from a bad answer into an unauthorized action
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the approval gate for consequential, state-changing calls
- [Audit Trail (AI)](audit-trail-ai.md) — actions must be recorded, not just outputs
- [Grounding](grounding.md) — retrieval tools are one way a model gets something real to reason from
- [Multi-Agent Systems](multi-agent-systems.md) — agents coordinate by acting, and they act through tools
- [Permission Model (AI)](permission-model-ai.md) — the rulebook determining which calls need authorization
- Agent Interoperability (A2A) — the connective standard between agents, as MCP is between an agent and its tools

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-022 | Anthropic — *How tool use works* (2026) · [link](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/how-tool-use-works) | Tool-call mechanics; client-side vs server-side execution and where the audit boundary falls. ⚠️ Vendor-authored. |
| SRC-021 | Yao, S. et al. — *ReAct: Synergizing Reasoning and Acting in Language Models* (2022) · [link](https://arxiv.org/abs/2210.03629) | The reason–act–observe loop: interleaving reasoning traces with actions, and the evidence that it improves multi-step reliability. |
| SRC-103 | Model Context Protocol project (Anthropic) — *What is the Model Context Protocol (MCP)?* (2024) · [link](https://modelcontextprotocol.io/docs/getting-started/intro) | MCP as an open standard for tool interfaces; build-once / integrate-everywhere framing. ⚠️ Vendor-originated standard. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Tool use within agent workflow patterns; guardrails and sandboxed testing. ⚠️ Vendor-authored. |
| SRC-154 | Olumide, Shittu — *The Complete Guide to Tool Selection in AI Agents* (Machine Learning Mastery, 2026) · [link](https://machinelearningmastery.com/the-complete-guide-to-tool-selection-in-ai-agents/) | Tool-selection degradation at catalog scale; gating, retrieval, routing, planning, fallback, and benchmarking as mitigations. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Tool definitions and their execution boundary are where model behavior becomes system behavior — and where permission logic must live. |
| **Organizational** | Every tool is an authorization decision. The tool inventory, not the model choice, determines what an AI deployment can actually do to your systems. |
| **Client-facing** | Explains the jump from "it can tell you about your order" to "it can change your order" — and why the second needs approval controls. |
| **LLM-native** | Capability increasingly comes from the tool layer and its standards (MCP), not from the model; designing the tool set is the design work. |

---

*Last updated: v1.0 · August 2026*
