<!--meta
category: System Architecture
short: One control point in front of every model provider — the only place organizational AI policy can actually be enforced, and the place every prompt now collects
aliases: [LLM gateway, model gateway, LLM proxy, model router, LLM routing, provider abstraction, AI proxy, LLM Mesh, one place to control AI usage]
tags: [Architecture, Data Governance, Privacy]
established: established
-->
# AI Gateway

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
A layer sitting between an organization's applications and its model providers, through which every request passes — making it the one place where cost, policy, credentials and provider switching are actually enforced.

---

## Technical definition

An AI gateway (also **LLM gateway** or **model gateway**) is a proxy between applications and one or more model providers. Applications call the gateway using a single interface; the gateway decides which provider and model serves each request and handles what sits around that decision: authentication, rate limiting, spend tracking and budgets, retries and failover, caching, logging, and policy enforcement.

**Routing is the visible feature; centralization is the actual one.** Requests can be routed by cost, latency, task complexity or business rule — but the reason this pattern became infrastructure rather than an optimization is that **it is the only architectural point where every AI request in an organization passes through one place.** By 2026 gateways are widely treated as critical AI infrastructure rather than an optional add-on, precisely because that is where cost, reliability and governance can be controlled at all.

**It is not orchestration.** [Orchestration](orchestration-ai-systems.md) decides *what runs and in what order* — the steps of a task. A gateway decides *which provider serves a call* and enforces what happens around it. One sequences work; the other abstracts suppliers. A system commonly has both, at different layers.

**The provider-abstraction consequence is strategic rather than technical.** When applications address a gateway rather than a vendor SDK, changing model or provider becomes a configuration change instead of a rewrite. That is the practical substance behind most claims of avoiding lock-in, and it is also what makes multi-provider redundancy achievable ([systemic risk](systemic-risk-ai.md)).

**Implementations are numerous and largely open source**, which is what establishes the term beyond any one vendor: LiteLLM, Kong AI Gateway, Envoy AI Gateway, Apache APISIX, Portkey, Bifrost, Cloudflare AI Gateway and OpenRouter among them. Some vendors market the same pattern under their own name — **Dataiku's "LLM Mesh" is one such term**, and this entry publishes the concept under the neutral one.

**The cost of centralizing control is centralizing exposure, and it is rarely stated alongside the benefit.** Every prompt and every response now flows through one system, so the gateway becomes simultaneously the organization's best policy enforcement point, its most complete record of AI usage, its largest concentration of sensitive content, and a single point of failure for all AI capability at once.

---

## Plain-language version

Most organizations end up using several AI providers — one for this, another for that, a cheaper one for bulk work. Left alone, every application talks to each provider directly, with its own keys, its own bill, and its own idea of the rules.

A gateway puts one door in front of all of it. Applications talk to the door; the door decides which provider actually answers, and applies whatever rules you have set: who is allowed to use what, how much they may spend, what gets logged, what happens when a provider goes down.

The routing is the part people demo. The part that matters is simpler: **it is the only place where every AI request in the organization goes past the same checkpoint.** You cannot enforce a policy you have no chokepoint for, and without a gateway there isn't one.

It also makes switching providers realistic. If your applications are written against the door rather than against one vendor's software, changing model becomes a settings change rather than a rebuild. That is what "avoiding lock-in" concretely means here.

There is a cost, and it deserves saying plainly. Once everything goes through one place, that place holds everything. Every prompt anyone sent, including the ones they should not have. It becomes the richest record of what your organization is actually doing with AI — useful for governance, and a serious concentration of sensitive material. And if it goes down, all your AI goes down at once, not just one product's.

---

## AI literacy notes

1. **Centralization is the point; routing is the feature** — the value is having a chokepoint, not having clever model selection.
2. **You cannot enforce a policy without a place to enforce it.** A gateway is that place, and most organizations lack one.
3. **It is not orchestration** — one abstracts providers, the other sequences steps, and a system usually needs both.
4. **Provider abstraction is what makes switching feasible**, which is the concrete content of most lock-in claims.
5. **It is the natural answer to unsanctioned use** — the sanctioned path becomes the easy path ([shadow AI](shadow-ai.md)).
6. **Every prompt now passes through one system**, which is a governance benefit and a data concentration at the same time.
7. **It is a single point of failure for all AI capability**, not for one application.
8. **Model attribution depends on it** — without gateway records, "which model actually answered this?" is often unanswerable.

---

## Governance notes

**Core question:** Is there a single point through which our AI requests pass — and if not, on what basis do we believe any AI policy we have written is being applied?

**Watch for:**
- AI policy written with no enforcement point, so compliance is voluntary per application ([compliance](compliance-ai-systems.md))
- Provider credentials distributed across teams and applications rather than held at the gateway
- A gateway logging full prompt and response content with no retention rule, quietly building the organization's most sensitive corpus ([privacy](privacy-ai-systems.md), [data minimization](data-minimization.md))
- No record of which provider and **model version** served each request, making behavior changes unattributable ([model version and update](model-version-update.md))
- Routing rules that silently move traffic between providers with different data-handling terms or jurisdictions
- Fallback to a second provider on failure, where that provider was never assessed for the same data class
- Gateway treated as infrastructure with no owner for its *policy* configuration, only for its uptime
- Single point of failure unexamined, with no degraded mode defined for when the gateway is down ([operational readiness](operational-readiness-ai.md))
- Cost controls present but usage attribution absent, so spend is bounded while accountability is not

**Practice:**
- **Make the sanctioned path the easy path.** A gateway suppresses unsanctioned use by being more convenient than working around it, not by prohibition
- Hold provider credentials at the gateway and issue scoped virtual keys per team or application, with budgets attached
- **Decide log content deliberately** — metadata, or full content, with a stated retention period — rather than defaulting to capture-everything
- Record provider, model and version per request; that record is the only basis for attributing a behavior change later ([audit trail](audit-trail-ai.md))
- Assess every routing destination and fallback target against the data class permitted to reach it, and pin routing where jurisdiction matters
- Define and test the degraded mode for gateway failure before it is needed
- Name an owner for gateway *policy* distinct from the owner of gateway *uptime* — they are different jobs and only one is usually staffed
- Use the aggregate view for what only it can do: real cost per team, real model mix, real usage patterns ([value realization](value-realization-ai.md))

**Key accountability owner:** whoever is answerable for AI policy across the organization — because the gateway is the only place their policy can actually take effect, and it is almost always owned by a platform team scoped to keep it running rather than to decide what it permits.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the pattern, medium on practice.** The architecture is uncontroversial and implemented in numerous independent, largely open-source projects, which is what establishes the term beyond any single vendor. **The weaker ground is evidential:** most published material on gateways is written by companies selling them, and this entry deliberately cites the pattern rather than any product's claims about it. **No independent measurement is cited here for the central governance argument** — that a chokepoint is the precondition for enforceable AI policy — because it follows structurally rather than being demonstrated, and because no study of how organizations actually govern gateways was found. **The concentration risk is stated symmetrically on purpose:** vendor material describes the control benefit and rarely the data-aggregation and single-point-of-failure costs, and a reader deciding on this pattern needs both. Product names and capabilities will date quickly; the trade will not.

---

## Related concepts

- [Orchestration (AI Systems)](orchestration-ai-systems.md) — sequencing steps, as against abstracting providers; different layers, commonly both present
- [Shadow AI](shadow-ai.md) — the problem a gateway addresses by making the sanctioned route the convenient one
- [Inference](inference.md) — the per-request cost a gateway exists to see and bound
- [Model Version & Update](model-version-update.md) — attribution that depends entirely on gateway records
- [Observability](observability.md) — the aggregate view only a chokepoint can produce
- [Privacy (AI Systems)](privacy-ai-systems.md) — the concentration created by routing every prompt through one system
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — why routing and fallback destinations need assessing individually
- [Systemic Risk (AI)](systemic-risk-ai.md) — provider redundancy, and the single point of failure it introduces
- [Local LLMs](local-llms.md) — a destination a gateway can route to like any other
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether a degraded mode exists for the day the door is shut

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-273 | LiteLLM (BerriAI) — *LiteLLM Proxy Server (LLM Gateway)* documentation · [link](https://docs.litellm.ai/docs/simple_proxy) | A concrete, open-source instance of the pattern and its standard capability set: a unified interface across many providers, spend tracking and budgets per virtual key or user, rate limiting, logging, and load balancing with routing and failover. Cited as evidence that the pattern is implemented independently of any model vendor. ⚠️ Project documentation — cite for what the pattern comprises, not for comparative claims. |
| SRC-063 | Covin, Chad Kwiwon (Dataiku Blog) — *Unified AI Ops: How to Scale AgentOps, MLOps, DataOps, & LLMOps* (2025) · [link](https://www.dataiku.com/stories/blog/unified-ai-ops) | Vendor treatment of centralized control across AI operations; Dataiku markets this pattern under its own name, *LLM Mesh*, which is why this entry publishes the concept under the neutral term. ⚠️ Vendor-authored. |
| SRC-105 | Kausar, Rehan (CDO Magazine) — *AI Governance Roles: Who Owns What as AI Scales in the Enterprise* (2026) · [link](https://www.cdomagazine.tech/ai-governance/ai-governance-roles-who-owns-what-as-ai-scales-in-the-enterprise) | The ownership split this entry's accountability line rests on — policy ownership and platform ownership being separate, and only one of them usually staffed. |
| SRC-126 | European Union — *GDPR Article 5(1)(c) — Data Minimisation* (2016) · [link](https://gdpr-info.eu/art-5-gdpr/) | The obligation a capture-everything gateway log quietly runs against, and the reason log content is a decision rather than a default. |
| SRC-001 | NIST — *AI Risk Management Framework* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Governance functions that require an enforcement and measurement point to be operable at all rather than aspirational. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Hold credentials at the gateway with scoped keys and budgets, record provider and model version per request, assess every fallback destination, and define the degraded mode before you need it. |
| **Organizational** | This is the only place written AI policy can actually take effect — and it is usually owned by a team scoped to keep it running, not to decide what it permits. Name both owners. |
| **Client-facing** | Explains how an organization can say which models handled their data, switch providers without rebuilding, and enforce a rule rather than merely publish one. |
| **LLM-native** | Centralization is the point; routing is the feature. The same chokepoint that makes policy enforceable also concentrates every prompt in one system and fails all AI at once. |

---

*Last updated: v1.0 · September 2026*
