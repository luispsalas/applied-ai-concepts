<!--meta
category: System Architecture
short: Running an untrusted system inside a bounded environment so that what it can reach is limited by construction — the control that does not depend on predicting what it will try
aliases: [sandbox, isolation, containment, confinement, safe execution environment, restricted environment, agent sandbox, running agents safely]
tags: [Security, Architecture]
established: established
-->
# Sandboxing

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Running a system inside a deliberately bounded environment so the damage it can do is limited by construction rather than by good behavior — the control that holds even when the thing inside it is fully compromised.

---

## Technical definition

A sandbox constrains what a running process can reach: which files, which network destinations, which system calls, which credentials, how much compute and for how long. The constraint is enforced by the environment, **not by the code inside it** — which is what distinguishes it from a rule the system is asked to follow.

Goldberg et al. (USENIX Security '96) set out the canonical form for untrusted software: run an **unmodified, untrusted program in a restricted environment** so that the damage it can do is bounded even if it is compromised. Their Janus prototype mediated a helper application's system calls. The paper won Best Paper and later a Test of Time award, and the idea it names is now infrastructure.

**The property that transfers to AI, and the reason this matters more for agents than for models:** you do not have to anticipate what the untrusted thing will attempt. A [guardrail](guardrails-ai-systems.md) or a system prompt tries to enumerate disallowed behavior, and every enumeration is incomplete — which is why [prompt injection](prompt-injection.md) and [jailbreaks](jailbreak.md) keep working. **A sandbox does not enumerate; it bounds.** The question shifts from *"can we stop it doing X?"* to *"what is the worst that reaching everything available here could do?"*

This puts it in the same family as the principles Saltzer & Schroeder set out in 1975 — **least privilege** (grant only what the task needs), **complete mediation** (check every access, not the first), and **fail-safe defaults** (deny unless permitted). A sandbox is where those become a property of the environment rather than an intention.

**Why agents changed the stakes.** A model that only emits text is bounded by construction already. An agent that executes code, calls tools, browses, and writes files is running untrusted output — *its own* — against real systems. **The untrusted party is not an attacker here; it is the system you deployed**, acting on inputs that may be adversarial ([prompt injection](prompt-injection.md)) or simply on a plan that is wrong.

**The limits are real and should be stated.** A sandbox bounds blast radius; it does not make behavior correct. It cannot protect data you deliberately put inside it. Escapes exist, and the boundary is only as good as its weakest mediated path — a network egress, a shared mount, an over-scoped credential. And a sandbox that has to be widened to make the task work has been traded away by degrees, usually without a decision being recorded.

---

## Plain-language version

There are two ways to stop a system doing something harmful. You can tell it not to, or you can put it somewhere it cannot.

Telling it not to means writing down everything it must not do. That list is never complete, which is why people keep finding new ways to talk models into misbehaving.

A sandbox takes the other route. You run the system in a walled-off space — limited files, limited network, limited time, limited permissions — so the worst it can do is bounded by where it is, not by whether it behaved. The idea comes from computer security in the 1990s: run untrusted software in a restricted environment, so that even if it is completely taken over, the damage stops at the wall.

This matters much more for AI agents than for chatbots. A chatbot writes text. An agent runs commands, edits files, calls services, spends money. It is acting on real systems based on plans it made itself, from inputs that might be hostile — so the useful question stops being "will it behave?" and becomes **"if this goes wrong in the worst way, what can it reach?"**

Two honest caveats. A sandbox limits damage; it does not make the system right — it can still do the wrong thing correctly within its walls. And sandboxes get widened, a little at a time, to make things work. That is how they stop being sandboxes, usually without anyone deciding.

---

## AI literacy notes

1. **Bounding beats enumerating.** Guardrails list what is forbidden and are always incomplete; a sandbox limits what is reachable regardless of what is attempted.
2. **The untrusted party is your own agent.** Not because it is malicious, but because it acts on plans it generated from inputs you do not control.
3. **It limits blast radius, not correctness.** A sandboxed agent can still do exactly the wrong thing within its permitted scope.
4. **Everything you put inside it is at risk.** Credentials, data and network reach granted for convenience are inside the wall, not outside it.
5. **The weakest mediated path defines the boundary** — an open egress, a shared volume, or one over-scoped token undoes the rest.
6. **Sandboxes erode by widening.** Each "just allow this so it works" is a security decision, and they are rarely recorded as such.
7. **Time and spend are boundaries too**, not just files and network — an unbounded loop is a real failure mode ([multi-agent systems](multi-agent-systems.md)).
8. **Testing in a sandbox is not the same as deploying in one**, and the two are routinely conflated.

---

## Governance notes

**Core question:** If this agent did the worst thing its permissions allow — not the worst thing we imagine it attempting — what would it reach, and who decided it should be able to?

**Watch for:**
- An agent with production credentials because that is what made the task work
- Sandbox scope widened incrementally during development, with no record of who approved each widening
- Network egress unrestricted, making exfiltration possible regardless of other controls ([data leakage](data-leakage-ai-systems.md))
- Prompt-level instructions relied on as the containment boundary rather than as guidance ([prompt injection](prompt-injection.md))
- No time, step or spend ceiling, so a failure mode is unbounded rather than merely wrong
- The same environment used for testing and production, so nothing was ever really isolated
- Credentials scoped to a person rather than to a task ([permission model](permission-model-ai.md))
- Sandbox treated as sufficient on its own, with no [human checkpoint](human-in-the-loop.md) at irreversibility

**Practice:**
- **Specify the boundary before the capability**: what the agent may reach, for how long, at what cost — then build the task inside it
- Grant least privilege per task rather than per user, and prefer short-lived, narrowly-scoped credentials
- **Treat every widening as a change requiring a named approver and a record** — this is the control that actually erodes
- Bound time, steps and spend as first-class limits alongside file and network scope
- Restrict egress explicitly; an agent that can reach the open internet can move data out of any sandbox
- Keep [human checkpoints](human-in-the-loop.md) at irreversible actions regardless of containment — a sandbox is not an oversight substitute
- Log what was actually reached, not only what was permitted ([audit trail](audit-trail-ai.md))

**Key accountability owner:** whoever owns the credentials and network scope the agent runs with — because the boundary is defined by what was granted, and grants are made by people who are frequently not the ones running the agent.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the principle, medium on AI-specific practice.** Sandboxing is thirty years of settled security engineering with a canonical peer-reviewed anchor and an established principle base (least privilege, complete mediation, fail-safe defaults). What is *not* settled is what a sandbox should look like for an LLM agent: there is no standard scope model, no agreed default boundary, and no benchmark for whether a given containment is adequate. **Vendor tooling is moving faster than any consensus**, so treat specific product claims about "safe execution" as configuration choices rather than assurances. The erosion problem — sandboxes widening in practice until they no longer contain — is well recognized by practitioners and, as far as this entry's sourcing goes, **not quantified anywhere**.

---

## Related concepts

- [Permission Model (AI)](permission-model-ai.md) — what the agent is allowed to do; the sandbox is where that is enforced
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — enumerating disallowed behavior, the complementary and incomplete approach
- [Prompt Injection](prompt-injection.md) — why instruction-level containment fails and environment-level containment does not
- [Jailbreak](jailbreak.md) — the same lesson: constraints inside the model are negotiable, constraints outside it are not
- [AI Agent](ai-agent.md) — the reason this became load-bearing rather than optional
- [Multi-Agent Systems](multi-agent-systems.md) — where unbounded loops and compounding spend appear
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — egress is the boundary that matters most for exfiltration
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — containment bounds damage; it does not supply oversight
- [Tool Use](tool-use.md) — every tool is a hole deliberately made in the wall
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the boundary exists before deployment, not after

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-245 | Goldberg, I.; Wagner, D.; Thomas, R.; Brewer, E. (UC Berkeley) — *A Secure Environment for Untrusted Helper Applications (Confining the Wily Hacker)* (6th USENIX Security Symposium, 1996) · [link](https://www.usenix.org/conference/6th-usenix-security-symposium/secure-environment-untrusted-helper-applications) | The canonical formulation: run an unmodified, untrusted program in a restricted environment so damage is bounded even under full compromise. Best Paper; USENIX Test of Time Award 2019. |
| SRC-160 | Saltzer, J.H.; Schroeder, M.D. (MIT) — *The Protection of Information in Computer Systems*, Proc. IEEE 63(9) (1975) · [link](https://doi.org/10.1109/PROC.1975.9939) | The principle base a sandbox operationalizes: least privilege, complete mediation, and fail-safe defaults as properties of the environment rather than intentions of the code. |
| SRC-148 | OWASP Foundation (GenAI Security Project) — *OWASP Top 10 for LLM Applications* (2025) · [link](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Industry-standard framing of excessive agency and insecure output handling — the agent-era risks containment is meant to bound. |
| SRC-034 | Chase, Harrison (LangChain) — *The Agent Development Lifecycle* (2026) · [link](https://www.langchain.com/blog/the-agent-development-lifecycle) | Practitioner treatment of sandboxed execution and tool access control as lifecycle concerns, with checkpoint design proportional to consequence. ⚠️ Vendor-authored. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Specify the boundary before the capability. Bound time, steps and spend alongside files and network, restrict egress explicitly, and scope credentials per task rather than per user. |
| **Organizational** | Every widening of a sandbox is a security decision needing a named approver and a record — that is the control that erodes in practice, quietly. |
| **Client-facing** | Explains what an autonomous system can and cannot reach, and why that boundary is stated as a limit rather than as a promise about behavior. |
| **LLM-native** | Guardrails enumerate and are always incomplete; sandboxes bound and do not need to predict. The untrusted party is your own agent, acting on plans it generated from inputs you do not control. |

---

*Last updated: v1.0 · September 2026*
