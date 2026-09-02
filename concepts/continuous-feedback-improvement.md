<!--meta
category: Organizational Readiness
short: Treating an AI system as something that must be watched and corrected for as long as it runs — a standing capability with an owner, not a post-launch intention
aliases: [continuous improvement, feedback loop, closing the loop, iterate, post-deployment monitoring, corrective action, continual improvement, learning from production]
tags: [Evaluation, Data Governance]
established: established
-->
# Continuous Feedback & Improvement

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The standing capability to detect that a deployed AI system has degraded, decide what to do about it, and make the change — funded and owned for the life of the system, rather than assumed to happen once a project has closed.

---

## Technical definition

A closed loop with four parts, all of which must exist for the loop to be real: **signal** (production [observability](observability.md) and outcome data), **judgment** ([evaluation](evaluation.md) against a maintained baseline), **decision** (a named owner with authority to act), and **change** (a controlled path to modify prompt, retrieval corpus, [guardrails](guardrails-ai-systems.md), configuration or model).

Break any one and the loop is decorative. **The most common break is the third**, not the first: organizations instrument a system, generate dashboards, and have no one empowered to decide that the numbers warrant a change.

**Management-system standards treat this as a requirement rather than a maturity nicety.** ISO/IEC 42001:2023 carries the improvement obligations of the standard ISO management-system architecture — continual improvement, and nonconformity with corrective action — into AI specifically; the NIST AI RMF's **Manage** function likewise covers ongoing monitoring and response after deployment. In both, an AI system is a thing under management for its operating life, not a delivery.

**Why AI needs this more than conventional software does.** Deterministic software does not silently get worse when the world changes; a model does. The inputs shift, the [drift](model-data-drift.md) accumulates, and the code is untouched throughout. Sculley et al. (NIPS 2015) established the general form of the problem: *"it is common to incur massive ongoing maintenance costs in real-world ML systems,"* driven by risk factors including **boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, and changes in the external world.**

**The loop is itself a hazard, which is what distinguishes this from ordinary continuous improvement.** Two of Sculley's named risks are about the feedback path rather than the system: *hidden feedback loops*, where a system's own outputs shape the data it later learns from, and *undeclared consumers*, where downstream users depend on outputs nobody knows about. A model retrained on data its predecessor influenced will confirm itself and report improvement while doing so. **A feedback loop with no independent measurement is a machine for producing agreement**, and the same dynamic that makes a model agreeable to a user ([sycophancy](sycophancy-llms.md)) makes a retraining pipeline agreeable to itself.

---

## Plain-language version

Conventional software does not rot on its own. Leave it alone and it keeps doing exactly what it did, right up until someone changes it.

AI systems are not like that. The code can sit untouched while the system gets steadily worse, because the world it was built for moved — customers ask about new things, vocabulary changes, the documents behind it go stale. Nothing broke. It just quietly stopped fitting.

So an AI system needs someone watching it for as long as it runs. That means four things, and it is only real if all four are present: you can see how it is doing, you can judge whether that is good enough, **someone is allowed to decide it isn't**, and there is a safe way to change it.

The third one is where this usually fails. Plenty of organizations build the dashboards and then discover nobody actually owns the decision to act on them. Monitoring without authority is watching, not improving.

There is a trap worth naming too. If you improve the system using data the system itself produced, you can end up teaching it that it was right all along. It will look like it is getting better. It is getting more self-consistent, which is not the same thing — and from the inside they look identical.

---

## AI literacy notes

1. **A model degrades without being touched.** Nothing needs to break for performance to fall; the world moving is enough.
2. **Monitoring is not improvement.** Signal without a decision-maker who can act on it is a dashboard, not a loop.
3. **The decision step is the usual missing piece** — more often than instrumentation, which is the part that gets budgeted.
4. **A loop fed by its own output confirms itself.** Improvement measured only on system-influenced data is self-agreement wearing the costume of progress.
5. **User satisfaction is not accuracy.** Thumbs-up feedback rewards outputs that feel good, and a system optimized on it drifts toward agreeableness ([sycophancy](sycophancy-llms.md)).
6. **"Continuous" means funded.** An improvement capability with no standing budget or owner reverts to incident response.
7. **Every change resets the baseline.** Without a maintained evaluation set, you cannot tell whether a fix helped or moved the problem.
8. **Undeclared consumers make changes riskier than they look** — downstream users you don't know about are depending on current behavior.

---

## Governance notes

**Core question:** For this system, who is authorized to decide it has degraded enough to change — and what independent evidence would they be deciding on?

**Watch for:**
- Monitoring in place with no named person holding authority to act on it
- Improvement measured on data the system itself generated or influenced — the self-confirming loop
- Thumbs-up/thumbs-down user feedback used as the primary quality signal
- No maintained evaluation baseline, so no change can be shown to be an improvement ([evaluation](evaluation.md))
- Improvement work funded as a project rather than as an operating cost, and quietly ending at handover ([operational readiness](operational-readiness-ai.md))
- Changes to prompts, retrieval corpora or configuration made outside version control and absent from the [audit trail](audit-trail-ai.md)
- Drift detection specified for the model while the [retrieval corpus](knowledge-base.md) silently goes stale
- Corrective action closed on the immediate symptom, with no cause analysis ([AI incident reporting](ai-incident-reporting.md))
- Retraining cadence set by calendar rather than by measured degradation

**Practice:**
- **Name the decision owner explicitly**, with the authority to require a change and to escalate — this is the step that most often has no name ([RACI](raci.md), [ownership](ownership-ai-systems.md))
- Maintain a versioned evaluation set that is **not** drawn from system-influenced production data, and re-run it on every change
- Keep at least one measurement channel independent of the system's own outputs — sampled human review, external outcome data, or a held-out benchmark
- Separate *satisfaction* signals from *correctness* signals and never let the first stand in for the second
- Version and log every change to prompt, corpus, configuration and model together, so a regression can be attributed
- Set review triggers on measured degradation as well as on schedule, and define in advance what result forces a rollback
- Fund the capability as an operating cost with a stated horizon, and inventory downstream consumers before changing behavior

**Key accountability owner:** the system owner as an operating asset — deliberately *not* the delivery team, whose mandate ends at launch and whose disappearance is precisely how the loop goes quiet.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the requirement and the mechanism. Continual improvement and corrective action are explicit obligations in ISO/IEC 42001 and the NIST AI RMF's Manage function, and the maintenance-cost and feedback-loop findings are peer-reviewed and long established. **Lower on implementation:** there is no settled standard for how often to re-evaluate, what degradation threshold should force action, or how to size the capability — these remain organizational judgments, and published guidance is mostly vendor-authored. **The self-confirming-loop hazard is well described in the ML systems literature but poorly reflected in AI governance practice**, which tends to treat feedback as unambiguously good.

---

## Related concepts

- [Model & Data Drift](model-data-drift.md) — the degradation this capability exists to catch
- [Observability (AI Systems)](observability.md) — the signal layer the loop depends on
- [Evaluation (AI Systems)](evaluation.md) — the judgment step, and the baseline every change is measured against
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the capability exists before launch, not after
- [AI Management System (ISO/IEC 42001)](ai-management-system-iso-42001.md) — where continual improvement is a certifiable requirement
- [Model Version & Update](model-version-update.md) — the controlled change path the loop terminates in
- [Ownership (AI Systems)](ownership-ai-systems.md) — the decision authority whose absence is the usual failure
- [RACI (AI Context)](raci.md) — making the decision owner explicit rather than assumed
- [Sycophancy (LLMs)](sycophancy-llms.md) — the same self-agreement dynamic, at the level of a single response
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — a feedback loop with exactly this hazard, at training scale
- [AI Incident (Reporting)](ai-incident-reporting.md) — the escalation path when degradation is not gradual
- [Audit Trail (AI Systems)](audit-trail-ai.md) — the record that lets a regression be attributed to a change
- [Value Realization (AI)](value-realization-ai.md) — the benefit that erodes when the loop is absent

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | Continual improvement and nonconformity/corrective action as certifiable obligations, carrying the management-system architecture into AI. ⚠️ Paywalled standard; clause-level detail should be verified against the text before being quoted. |
| SRC-166 | Sculley, D.; Holt, G.; Golovin, D.; Davydov, E.; Phillips, T.; Ebner, D.; Chaudhary, V.; Young, M.; Crespo, J.; Dennison, D. (Google) — *Hidden Technical Debt in Machine Learning Systems* (NIPS, 2015) · [link](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | The maintenance-cost finding — "massive ongoing maintenance costs in real-world ML systems" — and the named risk factors this entry builds on: boundary erosion, entanglement, hidden feedback loops, undeclared consumers, data dependencies, configuration issues, and changes in the external world. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The **Manage** function: ongoing post-deployment monitoring and response, and the requirement that controls be measured rather than assumed. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Maintain a versioned evaluation set not drawn from system-influenced production data; version prompt, corpus, config and model together so regressions can be attributed. |
| **Organizational** | Name the person authorized to decide the system has degraded, and fund the capability as an operating cost. Monitoring without that authority is watching, not improving. |
| **Client-facing** | Explains why an AI service needs ongoing attention even when nothing has broken, and what the provider is committing to after go-live. |
| **LLM-native** | Degradation is silent and requires no change to the code. And a loop fed by its own output produces self-agreement that is indistinguishable from improvement unless one measurement channel stays independent. |

---

*Last updated: v1.0 · September 2026*
