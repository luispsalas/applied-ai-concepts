<!--meta
category: System Architecture
short: The points where custom code runs during an agent's execution — and the question that decides whether a guardrail is a control or just a camera
aliases: [hook, hooks, middleware, callbacks, lifecycle hooks, interceptors, event hooks, PreToolUse, where do guardrails attach]
tags: [Agents, Architecture, Safety]
established: established
-->
# Agent Hooks

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Event-triggered extension points in an agent runtime where custom code runs — before a model call, around a tool call, at session start — and the layer where a guardrail either stops an action or merely watches it.

---

## Technical definition

An agent runtime emits events as it executes: a run begins, a model is about to be called, a tool is about to be invoked, a result returns, the run ends. A hook is registered code that fires at one of those points. The pattern is borrowed wholesale from web framework middleware, and by 2026 **every major agent runtime had independently converged on some version of it** — Claude Code, OpenAI's Codex CLI, LangChain and LangGraph, Google's ADK, AutoGen and Semantic Kernel among them.

**The distinction that decides everything is whether a hook can intervene or only observe**, and frameworks differ on this in ways their documentation does not make obvious:

| Framework surface | Can it stop an action? |
|---|---|
| LangChain **callbacks** | **No.** The dispatcher discards handler return values, so a callback cannot block or rewrite anything |
| CrewAI **event bus** | **No.** Observe-only |
| Semantic Kernel **filters** | **Yes** — though execution order between filters is undefined |
| LangChain **middleware** | **Yes** — `wrapModelCall` and `wrapToolCall` intercept rather than notify |

**So "we have guardrails" is, mechanically, a claim about hooks — and a large share of hook surfaces cannot enforce anything.** A control implemented as an observe-only callback is monitoring wearing a control's name. Microsoft's Responsible AI team, proposing a framework-neutral hook contract, characterizes the current state bluntly: existing controls are **framework-specific, mostly observe-only, and fail open when they crash.**

**Fail-open is the second half of the problem.** A guardrail that stops enforcing when it throws is not a guardrail; it is a component whose failure mode is silent permission. Whether a hook fails open or closed is rarely stated and rarely tested.

**Coverage is not comparable across frameworks either.** Event counts range from **2 to 78** — LlamaIndex exposes two coexisting observability surfaces, Semantic Kernel three, the OpenAI Agents SDK seven lifecycle hooks, LangChain twenty callback events, CrewAI seventy-eight typed event kinds. **A control that attaches cleanly in one runtime may have no equivalent attachment point in another**, so a policy expressed as hooks does not port with the agent.

---

## Plain-language version

An AI agent runs through a sequence: think, call a tool, get a result, think again. A hook is a place where you can insert your own code into that sequence — "before it calls a tool, run this check."

This is how nearly every guardrail is actually built. When a vendor says a system has safety controls, what usually exists underneath is code attached at one of these points.

**Here is the thing almost nobody checks: in many frameworks, that code cannot actually stop anything.** It gets told an action is happening. It can log it, count it, raise an alert. But whatever it returns is thrown away, and the action proceeds. Some frameworks work this way, others genuinely allow a block, and the documentation rarely leads with the difference.

So there are two very different things wearing the same word. One is a **control** — it can refuse. The other is a **camera** — it can only record. Both get described as guardrails.

There is a second issue. If the checking code crashes, most systems carry on as though the check had passed. A safety check whose failure mode is "allow everything" is worse than no check, because someone is relying on it.

And the attachment points vary enormously between frameworks — one offers two, another seventy-eight. So a rule you implemented in one tool may have nowhere to attach in the next one. **Your controls do not necessarily travel with your agent.**

---

## AI literacy notes

1. **Hooks are where guardrails actually live** — a guardrail claim is a claim about this layer.
2. **Observing and blocking are different capabilities**, and many hook surfaces only observe.
3. **A control that cannot refuse is monitoring**, however it is labeled in a datasheet.
4. **Fail-open is the common default** — a crashed check usually means the action proceeds.
5. **Event coverage varies from 2 to 78** across major frameworks, so control surfaces are not comparable.
6. **Execution order between hooks is often undefined**, so two rules can conflict with an unspecified winner.
7. **Controls do not port with the agent** — changing runtime can silently drop an enforcement point.
8. **The pattern is convergent, not proprietary** — every major runtime has one, which is what makes it a term of art rather than a product feature.

---

## Governance notes

**Core question:** For each control we claim to have, can the code behind it actually refuse the action — and what happens to that control when it throws an exception?

**Watch for:**
- "Guardrails" cited in an assurance document with no statement of whether they can block ([guardrails](guardrails-ai-systems.md))
- Controls implemented on observe-only surfaces — callbacks or event buses — and reported as enforcement
- No test that the control actually prevents the action, only that it fires ([evaluation](evaluation.md))
- Undefined or untested behavior when a hook raises: fail-open by default, and nobody has checked
- Undefined execution order between multiple hooks, so conflicting rules resolve arbitrarily
- A framework migration that silently drops an enforcement point with no equivalent in the new runtime
- Hooks used for [audit logging](audit-trail-ai.md) whose own failure is unlogged, producing gaps that look like inactivity
- Sensitive content passing through hook handlers into third-party observability tooling ([data leakage](data-leakage-ai-systems.md))

**Practice:**
- **For every claimed control, record which hook it attaches to and whether that hook can block** — this is a one-line fact that is almost never written down
- **Test enforcement by attempting the forbidden action**, not by confirming the handler ran
- Decide fail-open or fail-closed deliberately per control, and **test the crash path**, since the default is usually permissive
- Where order matters, pin it explicitly rather than relying on registration sequence
- Re-verify every control after a framework or version change; enforcement points are not portable ([model version and update](model-version-update.md))
- Keep enforcement separate from observation, so a logging failure cannot disable a block
- Prefer [sandboxing](sandboxing.md) for anything that must hold regardless — a bounded environment does not depend on a handler running correctly

**Key accountability owner:** whoever signs the statement that the system has controls — because that statement is, underneath, a claim that specific code can refuse specific actions, and it is routinely made about handlers that are structurally incapable of refusing anything.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The convergence across runtimes is directly observable in the frameworks' own documentation, and the blocking-versus-observing differences, the event counts, and the fail-open characterization come from a named comparison that its authors report testing across eight frameworks from six vendors. **The weaker element is that the leading comparison is authored by a vendor proposing its own contract** — an interest worth noting, though the specific claims about other frameworks are checkable against those frameworks' documentation and the entry states them as such rather than adopting the proposal. **Framework details will date quickly**: event counts and capabilities change release to release, so verify against the version you run rather than against this entry. **What will not date is the question** — can this control refuse, and what happens when it crashes — which is the entry's actual contribution.

---

## Related concepts

- [Guardrails (AI Systems)](guardrails-ai-systems.md) — what is usually built on hooks, and the claim this entry says to check
- [Harness Paradigm](harness-paradigm.md) — the control layer these are the extension points of
- [Permission Model (AI)](permission-model-ai.md) — what a blocking hook enforces
- [Sandboxing](sandboxing.md) — containment that does not depend on a handler running correctly
- [Tool Use](tool-use.md) — the action most commonly wrapped by a hook
- [Agent Skills](agent-skills.md) — loadable instructions whose actions these are the enforcement points for
- [AI Agent](ai-agent.md) — the execution loop emitting the events
- [Observability](observability.md) — the other, legitimate use of the same surfaces
- [Audit Trail (AI)](audit-trail-ai.md) — commonly implemented here, with the same failure risk
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the checkpoint a blocking hook can actually enforce

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-272 | Abuomar, Mohammad; McCaffrey, Caitie; Bird, Sarah; and Responsible AI at Microsoft — *Agent Hooks: An Open, Framework-Neutral AI Governance Contract* (Command Line, Microsoft, August 27 2026) · [link](https://commandline.microsoft.com/agent-hooks-framework-neutral-ai-governance-contract/) | The blocking-versus-observing comparison this entry is built on: LangChain callbacks discard return values and cannot block, CrewAI's event bus is observe-only, Semantic Kernel filters genuinely block with undefined ordering. Also the event-count spread (2 to 78) and the characterization that existing controls are framework-specific, mostly observe-only, and **fail open when they crash**. Reported as tested across eight frameworks from six vendors. ⚠️ Vendor-authored while proposing its own contract — the comparative claims are checkable against each framework's own documentation; the proposal is not adopted here. ⚠️ The page also carries the headline *"Your agent's guardrails have a bypass"*; same document. |
| SRC-071 | Osmani, Addy (O'Reilly Radar) — *Agent Harness Engineering* (2026) · [link](https://www.oreilly.com/radar/agent-harness-engineering/) | Positions the control layer as an engineered, versioned surface — the layer hooks are the extension points of. |
| SRC-018 | Böckeler, Birgitta — *Harness engineering for coding agent users* (2026) · [link](https://martinfowler.com/articles/harness-engineering.html) | The guides-versus-sensors distinction: what the harness suggests to the model as against what it actually enforces. |
| SRC-135 | Rebedea, T.; Dinu, R.; Sreedhar, M.; Parisien, C.; Cohen, J. (NVIDIA) — *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails* (EMNLP, 2023) · [link](https://arxiv.org/abs/2310.10501) | Peer-reviewed treatment of programmable rails as interposed, enforcing components rather than prompt-level instruction. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | The workflow-versus-agent distinction that determines where enforcement points can be placed at all. ⚠️ Vendor-authored. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | For each control, record the hook it attaches to and whether that hook can block. Test enforcement by attempting the forbidden action, and test the crash path — the default is usually fail-open. |
| **Organizational** | "We have guardrails" is a claim that specific code can refuse specific actions. It is routinely made about handlers that are structurally incapable of refusing anything. |
| **Client-facing** | Explains the difference between a system that watches for a problem and one that prevents it, without requiring the framework to be explained. |
| **LLM-native** | Observing and blocking are different capabilities sharing one word. Coverage ranges from 2 to 78 events across frameworks, so controls do not port with the agent. |

---

*Last updated: v1.0 · September 2026*
