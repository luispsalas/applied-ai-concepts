# Permission Model (AI)

## One-line essence
A clear rulebook defining what an AI is allowed to do on its own, what needs a human to approve first, and what is always off-limits.

---

## Technical definition

The explicit specification of an AI system's authority: which actions it may take autonomously, which require human authorization, and which are prohibited outright — enforced by the system rather than requested of the model.

The governing principle predates AI by half a century. Least privilege holds that every program and every user should operate with the minimum set of privileges needed to complete the job, so that misuse of privilege is less likely and, when it occurs, the number of components requiring audit is small. Its companion principles apply equally: fail-safe defaults (deny unless explicitly permitted), complete mediation (check every access, not just the first), and economy of mechanism (a control simple enough to be verified).

What AI changes is not the principle but the *unit* being authorized. Traditional access control asks "who can do what," binding permissions to an identity. An [agent](ai-agent.md) acts on a user's behalf, at machine speed, across many steps, with the specific sequence decided at runtime — so identity-bound permissions either over-grant (the agent inherits everything its operator can do) or block legitimate work. Emerging approaches shift the question toward *purpose* — classifying the intent behind a request and mapping it to policy enforced at runtime — to close the semantic gap that role- and attribute-based models leave open for agentic systems.

A workable permission model specifies, at minimum: the action inventory (what the system can do at all), a classification of each action by reversibility and blast radius, the authorization required per class, the identity under which each action executes, and the record written when it happens.

The enforcement point is the critical design decision. Permissions checked in the prompt are advisory; permissions checked at the execution boundary — where a [tool call](tool-use.md) becomes a real effect — are controls.

---

## Plain-language version

Before an AI system can act, someone has to decide what it may do by itself, what it must ask about first, and what it must never do at all. That decision needs to be written down and enforced in code — not left as an instruction in the prompt, because an instruction is something the model can be talked out of.

---

## AI literacy notes

1. **Permissions in the prompt are not permissions.** "Only use this tool for X" is a request to a probabilistic system. Enforcement belongs where the action executes, so it holds regardless of what the model was persuaded to attempt.
2. **This is not a new discipline.** Least privilege, fail-safe defaults, and complete mediation date to 1975 and apply unchanged. The pattern to avoid is treating AI permissions as a novel problem and reinventing a weaker version of settled security practice.
3. **Reversibility is the useful sorting axis.** Reading is recoverable; sending, paying, publishing, and deleting are not. Classifying actions by whether a mistake can be undone gives a defensible rule for where the human gate goes.
4. **Agents inherit too much by default.** Running an agent under its operator's credentials silently grants it everything that operator can do. Scope it as a separate principal with its own, narrower rights.
5. **Adding a tool changes the permission model.** Capability and authority are separate decisions that arrive together. Every new tool is an authorization question, not just an integration task.

---

## Governance notes

**Core question:** For every action this system can take — who decided it was allowed, under whose authority does it execute, and what would stop it if it were wrong?

**Watch for:**
- Authority expressed only in prompt text, with nothing enforced behind it
- An agent running under a human's credentials, inheriting that person's full access
- Irreversible actions — payment, deletion, external communication, publication — reachable without an approval step
- Permissions granted at build time and never reviewed as tools accumulate
- No record of which permission allowed a given action, making after-the-fact review impossible

**Practice:**
- Maintain an explicit action inventory; classify each by reversibility and blast radius
- Default to deny — a capability is unavailable until someone grants it deliberately
- Give each agent its own identity and credentials, scoped below the operator's
- Gate irreversible actions behind [human approval](human-in-the-loop.md), and make the gate structural rather than advisory
- Record the authorization basis alongside the action in the [audit trail](audit-trail-ai.md)
- Re-review the model whenever tools, autonomy, or user population change

**Key accountability owner:** the system owner, jointly with the owner of each system the AI is permitted to touch.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the underlying principles — least privilege and its companions are foundational, peer-reviewed, and unchanged by AI. **Medium** on AI-specific mechanisms: intent- and purpose-based access control for agentic systems is an active area with practitioner proposals and early implementations rather than settled standards.

---

## Related concepts

- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the enforcement machinery; the permission model is the policy it enforces
- [Tool Use](tool-use.md) — the action surface being authorized, and where enforcement must sit
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the approval step for actions that should not be autonomous
- [AI Agent](ai-agent.md) — autonomy is precisely what makes an explicit permission model necessary
- [Jailbreak](jailbreak.md) — why authority must be enforced outside the model's own judgment
- [Accountability (AI Systems)](accountability-ai-systems.md) — permissions record who authorized what, which is where answerability starts
- [Audit Trail (AI)](audit-trail-ai.md) — the record that makes a permission decision reviewable afterwards
- [Multi-Agent Systems](multi-agent-systems.md) — each agent is a separate principal needing its own scope
- Agency (AI Systems) — the broader question of how much autonomous action is appropriate at all

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-160 | Saltzer, J.H.; Schroeder, M.D. (MIT) — *The Protection of Information in Computer Systems*, Proc. IEEE 63(9) (1975) · [link](https://doi.org/10.1109/PROC.1975.9939) | The principle of least privilege and its companions — fail-safe defaults, complete mediation, economy of mechanism. Grounds the claim that this is inherited practice, not a new discipline. |
| SRC-055 | Huang, Ken (DistributedApps.ai) — *Intent-Based Access Control: A Technical Primer* (2026) · [link](https://kenhuangus.substack.com/p/intentbased-access-control-a-technical) | The semantic gap RBAC/ABAC leave for agentic systems, and intent-to-policy enforcement at runtime as a proposed response. ⚠️ Practitioner source, not peer-reviewed. |
| SRC-060 | He, Yifeng et al. (UC Davis) — *Security of AI Agents* (2026) · [link](https://arxiv.org/abs/2406.08689) | Agent vulnerability taxonomy across confidentiality, integrity and availability; why agent authority is a distinct security problem from model safety. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Human-approval checkpoints and sandboxing as concrete patterns in agent workflows. ⚠️ Vendor-authored. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places authority and control decisions inside a recognized risk-management lifecycle. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The enforcement point is the design decision: prompt-level constraints are advisory, execution-boundary checks are controls. |
| **Organizational** | The permission model is the document that answers "what is this system actually allowed to do?" — the prerequisite for approving any deployment. |
| **Client-facing** | Explains concretely what an AI system may and may not do on its own, and where a person remains in the decision. |
| **LLM-native** | Capability arrives with every new tool; authority does not follow automatically and must be granted deliberately. |

---

*Last updated: v1.0 · August 2026*
