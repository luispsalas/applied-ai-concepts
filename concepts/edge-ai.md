<!--meta
category: System Architecture
short: Inference running on the device where the data is, not in a datacenter — which stops data leaving and simultaneously stops you seeing what happened
aliases: [on-device AI, edge inference, edge computing, embedded AI, TinyML, offline AI, AI on the device, does the data leave the device]
tags: [Architecture, Privacy, Data Governance]
established: established
-->
# Edge AI

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
AI inference running on local devices rather than in the cloud — improving privacy and reducing latency, but shifting governance responsibility to the organization deploying the hardware.

---

## Technical definition

Edge AI runs inference on or near the device that produces the data — phones, cameras, vehicles, industrial controllers, sensors, handhelds — rather than sending that data to a datacenter.

It inherits its rationale from edge computing, which Satyanarayanan (IEEE *Computer*, 2017) defines as placing compute and storage at the network edge in close proximity to mobile devices and sensors. The motivations are the same and are worth separating, because they pull in different directions: **latency** (a round trip is unacceptable for control loops), **bandwidth** (sending raw video or sensor streams upstream is often infeasible), **privacy** (the data never leaves), and **resilience** (the system keeps working when the network does not).

**It is not the same as the two concepts nearest to it, and the distinction is operational.** [Local LLMs](local-llms.md) is about running models on *infrastructure you own* — typically servers you administer. [Small Language Models](small-language-models.md) is about model *size*. Edge AI is about **topology**: computation sited at the data source, usually across a **fleet of devices you do not physically control**. Small models are usually a prerequisite and local deployment is usually implied, but the governance profile comes from the fleet, not from the model.

**The governance trade is a genuine inversion, and most treatments state only its first half.** Keeping raw data on the device is a real advance in data minimization — it can satisfy the principle directly rather than by policy ([data minimization](data-minimization.md)). **But the same move removes the central chokepoint through which everything was observed.** There is no server-side log unless you build and ship one, no single place to see what the system decided, and no reliable way to answer *which model produced this output* once a fleet updates unevenly. **You stop the data leaving, and you stop being able to see what happened** ([observability](observability.md), [audit trail](audit-trail-ai.md)).

**Three consequences follow that cloud deployment does not have.** Model **version fragmentation** is normal rather than exceptional — devices update at different times, so the fleet is running several behaviors at once ([model version and update](model-version-update.md)). **Physical access becomes an attack surface**: weights and prompts on a device can be extracted or altered by whoever holds it. And **the update channel becomes safety-critical** — it is the only way a fix, a guardrail, or a withdrawal reaches the fleet, and it may not reach devices that are offline by design.

**Where the case is strongest it is very strong.** Walusimbi et al. document offline-first LLM architecture for low-connectivity environments, where cloud dependence is not a cost trade-off but a barrier to the system existing at all.

---

## Plain-language version

Edge AI means the model runs on the thing in front of you — the phone, the camera, the machine on the factory floor — instead of sending your data to a company's servers and waiting for an answer.

Four reasons people do it. It is faster, because there is no round trip. It is cheaper on bandwidth, because you are not streaming raw video somewhere. It is more private, because the data genuinely never leaves. And it keeps working when the network doesn't.

The privacy benefit is real, not marketing. If the recording never leaves the camera, there is no transfer to justify and no copy sitting somewhere else.

Here is the part that usually goes unsaid. The server you removed was also the place where everything was recorded. Take it away and, unless you deliberately build a replacement, nobody can see what the system did. Worse, once you have thousands of devices, they will not all be running the same version — some update late, some never — so "what did our AI decide, and which one decided it?" becomes genuinely hard to answer.

Two more things change. Anyone holding the device can potentially get at what's inside it, which is not true of a model on your servers. And the update channel becomes the only way to fix anything — if you need to pull a broken model back, that channel is your only route, and a device that is offline by design will not hear you.

So the honest summary: edge AI is often the right choice, and it trades one kind of risk for another rather than removing risk. You give up exposure and gain blindness.

---

## AI literacy notes

1. **Topology, not model size.** Edge AI is about *where* inference runs; small models are usually a prerequisite, not the definition.
2. **The privacy gain is structural**, not a policy promise — data that never leaves cannot be transferred, retained elsewhere, or subpoenaed from a third party.
3. **Removing the server removes the log.** Central observability disappears unless you deliberately rebuild it on-device.
4. **A fleet runs several versions at once.** "Which model produced this?" stops being answerable by default.
5. **Physical possession is access.** Weights, prompts and cached data on a device are exposed in a way server-side deployment is not.
6. **The update channel is safety-critical** — it is the only path for a fix or a withdrawal, and offline devices may never receive one.
7. **Disconnected operation cuts both ways**: resilience when the network fails, and no reach for a kill switch when you need one.
8. **In low-connectivity settings it is enabling, not optimizing** — the alternative is often no system at all.

---

## Governance notes

**Core question:** If a device in this fleet produced a harmful or disputed output last month, could we say which model version made it, on what input, and could we withdraw that version today?

**Watch for:**
- Privacy benefits claimed while no replacement was built for the logging the server used to provide ([observability](observability.md))
- No per-device record of model version, so fleet behavior is unattributable ([model version and update](model-version-update.md))
- An update channel with no rollback, no staged rollout, and no evidence of which devices actually applied a fix
- Devices intentionally offline, where guardrail updates and withdrawals cannot reach ([guardrails](guardrails-ai-systems.md))
- Model weights, system prompts or cached inputs stored unprotected on hardware in public or customer hands ([data leakage](data-leakage-ai-systems.md))
- "The data never leaves the device" asserted without confirming telemetry, crash reports and analytics do not carry content out ([shadow AI](shadow-ai.md))
- Edge deployment treated as exempt from record-keeping duties that attach to the system, not to its topology ([compliance](compliance-ai-systems.md))
- Decommissioned or lost devices still holding weights and data, with no revocation path

**Practice:**
- **Ship the audit trail with the model.** Decide before deployment what is recorded on-device, what is summarized upstream, and what is deliberately not kept ([audit trail](audit-trail-ai.md))
- Record model version per inference and make it recoverable from the device, not just from a deployment dashboard
- Treat the update channel as a controlled, safety-critical system: staged rollout, rollback, and evidence of uptake
- Verify the privacy claim empirically — inspect what telemetry and diagnostics actually transmit, rather than trusting the architecture diagram
- Protect weights and prompts at rest on the device, and plan for loss, theft and decommissioning
- Define behavior for devices that never reconnect: expiry, degradation, or refusal, chosen deliberately rather than by default
- Keep a [human checkpoint](human-in-the-loop.md) for consequential on-device decisions, since remote intervention may be unavailable

**Key accountability owner:** whoever owns the device fleet and its update channel — because on the edge, the ability to fix, withdraw, or even observe the system is a property of fleet management, and it usually sits with a team that was never told it now owns an AI control.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the architecture and its trade-offs, medium on practice.** Edge computing has a peer-reviewed definitional anchor and two decades of literature, and the motivations — latency, bandwidth, privacy, resilience — are uncontested. The data-minimization benefit follows directly from regulation rather than from vendor claims. **The weaker ground is operational:** there is no standard for on-device audit logging, no agreed approach to version attribution across a fleet, and little published evidence on how organizations actually handle withdrawal and rollback for deployed edge models. **The observability-loss argument central to this entry is reasoned from the architecture rather than measured** — it follows necessarily from removing the central chokepoint, but this entry cites no study quantifying how often edge deployments ship without replacement logging, because none was found. Treat it as a structural prediction to check in your own deployment, not as a documented failure rate.

---

## Related concepts

- [Local LLMs](local-llms.md) — models on infrastructure you own; the sibling concept, distinguished by fleet control
- [Small Language Models (SLMs)](small-language-models.md) — the model sizes that make edge deployment feasible
- [Inference](inference.md) — the phase being relocated, and the cost profile that motivates it
- Latency (AI Systems) — the constraint that most often forces the architecture
- [Privacy (AI Systems)](privacy-ai-systems.md) — the benefit most often claimed for it
- [Data Minimization](data-minimization.md) — the principle edge deployment can satisfy structurally
- [Observability](observability.md) — what is lost when the central chokepoint disappears
- [Model Version & Update](model-version-update.md) — fleet fragmentation, and why attribution gets hard
- [Audit Trail (AI)](audit-trail-ai.md) — the record that must now be designed rather than inherited
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — physical possession as an extraction path

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-257 | Satyanarayanan, Mahadev (Carnegie Mellon University) — *The Emergence of Edge Computing* (IEEE *Computer* 50(1), pp. 30–39, January 2017) · [link](https://doi.org/10.1109/MC.2017.9) | The definitional anchor: compute and storage placed at the network edge in proximity to mobile devices and sensors, and the four motivations — latency, bandwidth, privacy and resilience — this entry separates. ⚠️ Metadata verified via Crossref; a same-author, same-journal, same-year piece (*Edge Computing*, 50(10), 36–38) is a **different paper** and is frequently conflated with this one. |
| SRC-087 | Belcak, P. et al. (NVIDIA) — *Small Language Models Are the Future of Agentic AI* (2025) · [link](https://arxiv.org/abs/2506.02153) | The argument that capable small models make on-device deployment practical for real workloads. ⚠️ Vendor-authored. |
| SRC-057 | Walusimbi, Joseph et al. (Soroti University, Uganda) — *Offline-First LLM Architecture for Adaptive Learning in Low-Connectivity Environments* (2026) · [link](https://arxiv.org/abs/2603.03339) | The enabling rather than optimizing case: contexts where cloud dependence prevents the system existing at all. |
| SRC-102 | Sandrini, Peter — *Beyond the Cloud: Assessing the Benefits and Drawbacks of Local LLM Deployment for Translators* (2025) · [link](https://arxiv.org/abs/2507.23399) | Practitioner assessment of the trade-offs when inference moves off provider infrastructure, including the operational burden that transfers with it. |
| SRC-126 | European Union — *GDPR Article 5(1)(c) — Data Minimisation* (2016) · [link](https://gdpr-info.eu/art-5-gdpr/) | The principle edge deployment can satisfy structurally rather than by policy — data that is never collected centrally needs no minimization argument. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Ship the audit trail with the model, record version per inference, and treat the update channel as safety-critical with staged rollout and rollback. Verify the privacy claim against actual telemetry. |
| **Organizational** | The ability to observe, fix or withdraw an edge model is a property of fleet management — usually owned by a team that was never told it now owns an AI control. |
| **Client-facing** | Supports an honest version of "your data stays on your device," including what the organization can and cannot see or correct afterwards. |
| **LLM-native** | Edge AI is topology, not model size. It trades data exposure for blindness: removing the server removes the log, and a fleet runs several model versions at once by default. |

---

*Last updated: v1.0 · September 2026*
