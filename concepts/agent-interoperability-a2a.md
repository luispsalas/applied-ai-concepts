<!--meta
category: System Architecture
short: Letting agents built by different parties discover and delegate to each other — the layer where accountability crosses an organizational boundary, usually before anyone has decided who holds it
aliases: [A2A, agent2agent, agent-to-agent, agent interop, agent communication protocol, cross-platform agents, agent discovery]
tags: [Agents, Architecture, Security]
established: established
-->
# Agent Interoperability (A2A)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Standards that let AI agents built on different platforms discover each other's capabilities and communicate directly — the connective layer between agents, as MCP is between an agent and its tools.

---

## Technical definition

Agent interoperability is the ability of agents built on different frameworks, by different vendors, and inside different organizations to discover one another's capabilities and exchange work without prior bespoke integration. The A2A (Agent2Agent) protocol is the leading open specification for it: agents advertise capabilities, then **delegate sub-tasks, exchange information and coordinate actions** without exposing internal logic, prompts or memory.

**Two protocol layers, one distinction worth keeping straight.** [MCP](tool-use.md) governs agent-to-tool communication — how an agent reaches a resource. A2A governs agent-to-agent communication — how an agent reaches another autonomous party. They are complementary rather than competing, and conflating them obscures the difference that matters: **a tool does what it is told and an agent decides**.

**Governance of the standard itself is the reason this is a concept and not a product.** A2A originated at Google (announced April 2025) and was donated to the Linux Foundation in June 2025, with a Technical Steering Committee drawn from AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP and ServiceNow. **Multi-vendor stewardship is what distinguishes an interoperability standard from a platform's integration surface**, and it is the appropriate thing to check before adopting any protocol claiming this role.

**Deliberate opacity is the design feature with the largest governance consequence.** A2A lets an agent expose what it can do without revealing how — reasonable commercially, and it means the calling organization cannot inspect the reasoning, [training data](training-data.md), [system prompt](system-prompt.md) or model version behind a capability it depends on. **Accountability crosses an organizational boundary at exactly the point where observability stops** ([accountability](accountability-ai-systems.md), [observability](observability.md)).

**The failure modes are those of multi-agent systems, with the blast radius extended past your perimeter.** Surveys of LLM multi-agent systems and taxonomies of agentic faults document error propagation across agents, coordination failure and compounding cost; He et al. add the security dimension. Interoperability does not create these problems, but it **removes the boundary that used to contain them** — a compromised or merely wrong external agent now propagates into your workflow, and [prompt injection](prompt-injection.md) gains a path through a trusted channel rather than through user input.

**Adoption is real but early.** The specification exists and is multi-vendor governed; production deployment of cross-organizational agent delegation, and the contractual and liability practice that would have to accompany it, are not yet settled.

---

## Plain-language version

Most AI agents today are islands. An agent your company built can use its own tools, but it cannot hand a job to an agent built by a supplier, because the two have no shared way to talk. Interoperability is the effort to fix that: a common language for one agent to find out what another can do, hand it a task, and get a result.

There are two different plumbing problems here and they get muddled. One is connecting an agent to *tools* — a database, a search index, a calendar. The other is connecting an agent to *another agent*. The difference sounds technical but it is not: a tool does what it is told, and an agent makes decisions. Handing work to something that decides is a different act from calling a function.

The leading standard for the second one is A2A. It started at Google and was handed to the Linux Foundation in 2025, with a committee spanning most of the large cloud and software vendors. That handover matters more than it sounds — a standard controlled by one company is that company's integration surface with a friendly name on it.

Now the part to be careful about. The design deliberately lets an agent show what it can do without showing how it works. That is commercially sensible and it means you cannot see inside something you are relying on. You will not know which model it used, what it was told to do, or why it answered as it did. If it is wrong, the consequence still lands on you, and the customer will still hold you responsible — but the evidence sits inside someone else's system.

That is the real question here, and it is not a technical one. It is: when an agent you do not control does something wrong on your behalf, who answers for it, and what did you agree in advance?

---

## AI literacy notes

1. **Agent-to-tool and agent-to-agent are different problems.** A tool executes; an agent decides. Delegating to something that decides is a different act.
2. **Who governs the standard is a due-diligence question.** Multi-vendor stewardship is what separates an interoperability standard from one company's integration surface.
3. **Opacity is designed in, not accidental** — capabilities are advertised without internals, which is reasonable commercially and costly for oversight.
4. **Accountability crosses the boundary; observability does not.** That asymmetry is the defining governance problem of this layer.
5. **Existing multi-agent failure modes extend past your perimeter** — error propagation, coordination failure and compounding cost now involve parties you do not control.
6. **A trusted agent channel is an injection path**, and it carries more implicit trust than user input does.
7. **You cannot see the other agent's model version**, so its behavior can change under you without notice.
8. **The specification is ahead of the practice.** Contracts, liability allocation and audit expectations for cross-organizational delegation are not settled.

---

## Governance notes

**Core question:** When an agent we do not control acts on our behalf and gets it wrong, who is accountable to the affected person, and what evidence will we actually be able to produce?

**Watch for:**
- External agent capabilities consumed with no contract covering error, liability or notification of change
- No record of which external agent handled which request, or which version of it ([audit trail](audit-trail-ai.md))
- Trust granted to an agent channel that would not be granted to equivalent user input ([prompt injection](prompt-injection.md))
- Data crossing an organizational boundary in a delegation with no lawful basis assessed ([privacy](privacy-ai-systems.md), [data leakage](data-leakage-ai-systems.md))
- Chains of delegation where no participant can see the full path, so no one can reconstruct what happened ([multi-agent systems](multi-agent-systems.md))
- No cost, time or step ceiling on work delegated outward, making a failure unbounded and billed
- Silent behavior change when the external party updates their model ([model version and update](model-version-update.md))
- Agent capability advertisements accepted as accurate without verification ([verification](verification.md))
- An interoperability standard adopted on a vendor's description of it rather than on its actual governance

**Practice:**
- **Settle accountability contractually before technically** — error handling, liability, incident notification and change notice, agreed with the counterparty rather than assumed
- Log every outbound delegation with the counterparty, the declared capability, the request, the response and the timestamp
- **Treat inbound agent traffic as untrusted input**, with the same validation applied to user content, and never as privileged because it arrived over a trusted channel
- Scope what may be delegated and what may not, by data class and by consequence, and enforce it at the boundary ([permission model](permission-model-ai.md))
- Bound cost, steps and time on delegated work; contain the run regardless of where it executes ([sandboxing](sandboxing.md))
- Require change notification for the counterparty's model or agent version, and re-verify on notice
- Keep a [human checkpoint](human-in-the-loop.md) at irreversible actions that cross an organizational boundary
- Verify the standard's governance — who stewards it, who sits on its committee — as part of adoption
- Record the delegation chain in a form that survives an incident review, since your own logs are the only evidence you will control

**Key accountability owner:** whoever holds the relationship with the counterparty organization — because this is a contractual and liability question wearing a protocol's clothing, and the party that can actually fix it is the one who signed the agreement, not the one who wrote the integration.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-high on the concept, medium on practice.** Agent interoperability as a problem is well established and the A2A specification is public, versioned, and stewarded by a Linux Foundation Technical Steering Committee spanning eight major vendors — which is the evidence that this is a standard rather than a single vendor's vocabulary, and the reason it clears this wiki's term-status gate. **Confidence drops sharply on deployment.** Public evidence of production cross-organizational agent delegation at scale is thin, competing and overlapping proposals exist, and the specification is moving. **The governance analysis here is largely reasoned rather than observed:** the accountability-crosses-the-boundary-while-observability-stops argument follows from the protocol's stated opacity design and from documented multi-agent failure modes, but there is no body of incident evidence yet to calibrate against, and no settled contractual or audit practice to point to. Expect this entry to need revision as that practice forms — and treat any vendor claim about interoperability maturity as a claim about a specification, not about operational experience.

---

## Related concepts

- [Multi-Agent Systems](multi-agent-systems.md) — the failure modes this extends beyond your organizational perimeter
- [Tool Use](tool-use.md) — the agent-to-tool layer, and where MCP sits relative to this
- [AI Agent](ai-agent.md) — the autonomous party being delegated to, as distinct from a tool
- [Orchestration (AI Systems)](orchestration-ai-systems.md) — coordinating work you control, as against work you do not
- [Accountability (AI Systems)](accountability-ai-systems.md) — the question this layer forces and does not answer
- [Observability](observability.md) — what you lose at the boundary you gain reach across
- [Permission Model (AI)](permission-model-ai.md) — what may be delegated outward, and what may not
- [Prompt Injection](prompt-injection.md) — why a trusted agent channel is an attack path
- [Sandboxing](sandboxing.md) — bounding delegated work regardless of where it runs
- [Audit Trail (AI)](audit-trail-ai.md) — the only evidence of a cross-boundary action you will control

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-252 | A2A Project (Linux Foundation; originated at Google Cloud, donated June 2025) — *A2A Protocol Specification and Documentation* · [link](https://a2a-protocol.org/latest/) | The specification's own statement of purpose — capability discovery, sub-task delegation and coordination without exposing internal logic or memory — its MCP/A2A layer distinction, and its Technical Steering Committee composition (AWS, Cisco, Google, IBM Research, Microsoft, Salesforce, SAP, ServiceNow). ⚠️ Primary source maintained by the standard's own project; treat adoption claims accordingly. |
| SRC-103 | Model Context Protocol project (Anthropic) — *What is the Model Context Protocol (MCP)?* (2024) · [link](https://modelcontextprotocol.io/docs/getting-started/intro) | The agent-to-tool layer against which agent-to-agent interoperability is defined. ⚠️ Vendor-originated specification. |
| SRC-152 | Guo, T.; Chen, X.; Wang, Y.; Chang, R.; Pei, S.; Chawla, N.V.; Wiest, O.; Zhang, X. — *Large Language Model based Multi-Agents: A Survey of Progress and Challenges* (IJCAI, 2024) · [link](https://www.ijcai.org/proceedings/2024/890) | Documented coordination and error-propagation failure modes in multi-agent systems, which interoperability extends across organizational boundaries. |
| SRC-128 | Shah, M.B.; Morovati, M.M.; Rahman, M.M.; Khomh, F. — *Characterizing Faults in Agentic AI: A Taxonomy of Types, Symptoms, and Root Causes* (2026) · [link](https://arxiv.org/abs/2603.06847) | Fault taxonomy underlying the watch-for list, including coordination faults and the difficulty of attributing a failure across agents. |
| SRC-060 | He, Yifeng et al. (UC Davis) — *Security of AI Agents* (2026) · [link](https://arxiv.org/abs/2406.08689) | The security dimension of agent-to-agent channels, supporting treatment of inbound agent traffic as untrusted regardless of channel. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Treat inbound agent traffic as untrusted input, log every outbound delegation with counterparty and version, and bound cost, steps and time on work that executes outside your control. |
| **Organizational** | This is a contract and liability question wearing a protocol's clothing. Settle accountability, incident notification and change notice with the counterparty before the integration is built. |
| **Client-facing** | Explains what it means for work to be handed to a system another organization operates, and why that changes what can be shown if something goes wrong. |
| **LLM-native** | A tool executes; an agent decides. Interoperability moves accountability across an organizational boundary at exactly the point where observability stops. |

---

*Last updated: v1.0 · September 2026*
