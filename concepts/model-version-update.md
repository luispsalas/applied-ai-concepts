<!--meta
category: Reliability & Quality
short: The system you use today may not be the one you tested — providers change models underneath you, and reliable behavior can shift without notice
aliases: [model updates, version pinning, deprecation, it changed without telling us, model changed, provider update, snapshot models]
tags: [Model Behavior, Evaluation, Regulatory]
established: established
-->
# Model Version & Update

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The system you use today may not be the system you tested — providers change models underneath you, and behavior that was reliable can shift without notice.

---

## Technical definition

A hosted model behind a stable name is not a stable artifact. The provider retrains, re-runs preference optimization, adjusts system-level safety layers, and deprecates versions on their schedule — and a deployment pinned to a friendly alias inherits every one of those changes without acting.

**This is measured, not feared.** A study comparing March and June 2023 releases of two widely used models found substantial behavioral change across math, sensitive questions, code generation and visual reasoning. The most cited figure: accuracy on prime-versus-composite identification **fell from 84% to 51%** in three months.

**Read that carefully, because the correct reading is the useful one.** The same study found the *other* model **improved** on the same task, and the drop was attributed substantially to reduced amenability to chain-of-thought prompting — **a behavior change, not demonstrated capability loss.** "The model got worse" is the wrong lesson and the one usually taken. The right one is the authors' own framing: *"when and how these models are updated over time is opaque"* — which is precisely the deployer's problem.

**Three distinct things move, and they need separating:**

| | |
|---|---|
| **The weights** | Retraining or continued training. Capability and behavior both shift. |
| **The post-training layer** | Re-run preference optimization. Tone, refusals and hedging change — see [RLHF](rlhf.md). |
| **The surrounding system** | Provider-side system prompts, safety filters, routing. The model is untouched and the output changes anyway. |

Only the first is what most people mean by "a new model," and all three reach you identically.

**Pinning helps and does not solve it.** Most providers offer dated snapshots, which is the single most effective control here — but snapshots are **deprecated on a schedule**, so pinning converts an unannounced behavior change into a scheduled migration. That is a much better problem, and it is still a problem you have to staff.

**Why this is a governance entry and not an ops note:** every assurance you hold — the [evaluation](evaluation.md) you ran, the [model card](model-card-system-card.md) you read, the [FRIA](fundamental-rights-impact-assessment.md) or impact assessment you filed, the [red team](red-teaming.md) exercise you commissioned — was performed against a specific model state. **A provider update silently invalidates all of them**, and nothing in the change notification is addressed to your compliance file.

---

## Plain-language version

You test an AI system, it works, you approve it, you ship it. Some weeks later it behaves differently. Nobody at your organization changed anything.

The model behind the name got updated. That is normal and usually improves things — but it means the thing you approved and the thing running now are not necessarily the same, and you were not asked.

The evidence here is worth stating precisely, because it gets exaggerated. When researchers compared two versions of the same product three months apart, one task's accuracy dropped from 84% to 51%. That sounds like the model got much worse. But another model *improved* on that same task, and the drop came largely from the model no longer responding to a particular prompting style — it changed how it worked, more than what it could do.

The practical point is not that updates are bad. It is that **your testing has an expiry date you do not control.** Most providers let you pin to a dated version, which is the sensible move — as long as you know that pinned versions get retired, so you are trading a surprise for a deadline.

---

## AI literacy notes

1. **A model name is not a version.** "The latest model" is a moving target. If you cannot state which dated snapshot you are on, you do not know what you are running.
2. **Read the prime-number result correctly.** It shows behavior changing in both directions, not decline. Anyone citing it as "AI is getting worse" has skipped the part where the other model improved.
3. **Three things move independently** — weights, post-training, and the provider's surrounding system. The third changes output with the model untouched, and is the least visible.
4. **Improvements break things too.** A model that becomes more cautious breaks a workflow that depended on it answering. Change is the risk, not degradation.
5. **Your evaluation has an expiry date.** Every test result is scoped to a model state. This is the single most under-appreciated consequence.
6. **Pinning trades a surprise for a deadline.** Snapshots are deprecated. Pin anyway — a scheduled migration is a far better problem than a silent change.
7. **Prompts are version-coupled.** Prompt engineering tuned against one version is an undocumented dependency on it, and it degrades quietly rather than failing loudly.

---

## Governance notes

**Core question:** Which exact model version is each system running — and what happens to your evaluations, assessments and approvals when it changes?

**Watch for:**
- Systems pointed at a floating alias with no pinned version, so updates arrive unannounced and untested
- **Evaluation, red-team and impact-assessment results with no model version recorded**, making them unfalsifiable after the fact and worthless as evidence
- Deprecation notices routed to engineering only, when the affected artifacts are compliance ones
- Behavior change diagnosed as [drift](model-data-drift.md) — the world moving — when the model moved instead. Different cause, different fix, and they are routinely confused
- Prompts tuned against a version that is going away, with the coupling undocumented
- Fine-tuned adapters built on a base that gets updated, invalidating their evaluation ([fine-tuning](fine-tuning.md))
- No canary or regression set that would detect a behavior shift before users do

**Practice:**
- **Pin to dated snapshots wherever the provider offers them**, and track deprecation dates as scheduled work with an owner
- **Record the model version on every evaluation, assessment and approval** — a result without a version is not evidence
- Maintain a small regression set per system and re-run it on every version change and periodically regardless; this is the cheapest detection available
- Treat a version change as a change requiring re-assessment, not a configuration edit — and say explicitly which assurances it invalidates
- Distinguish model change from data drift when diagnosing: check the version first, since it is a one-line check and the other is an investigation
- Subscribe compliance and risk owners to provider deprecation channels, not just engineering
- Where a system is high-risk, make version change an approval gate rather than a notification

**Key accountability owner:** the system owner for the pin and the regression set; **jointly with whoever holds the compliance artifacts**, because the failure mode is a technically-managed update silently invalidating a governance record nobody re-checked.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the phenomenon, deliberately cautious on the measurements.** That hosted model behavior changes across versions is directly measured and uncontested, and the opacity of update schedules is a matter of record. **The specific figures should not be carried forward:** they describe two 2023 snapshots of one vendor, the study is a preprint that drew substantial methodological discussion, and the behavior-versus-capability distinction is doing real work in interpreting it — this entry cites the result for *that behavior changes unannounced*, never as a claim about any current model's quality. Provider practice on snapshots and deprecation windows also varies and changes; verify against current documentation rather than assuming.

---

## Related concepts

- [Model/Data Drift](model-data-drift.md) — the world moving versus the model moving; same symptom, different cause, routinely confused
- [Evaluation (AI Systems)](evaluation.md) — results are scoped to a model version and expire with it
- [Model Card / System Card](model-card-system-card.md) — documentation that describes a version, not a name
- [RLHF (Reinforcement Learning from Human Feedback)](rlhf.md) — the layer whose re-running changes tone, refusals and hedging
- [Fine-tuning](fine-tuning.md) — adapters are coupled to a base version
- [Prompt Engineering](prompt-engineering.md) — prompts are an undocumented dependency on a version
- [Operational Readiness (AI)](operational-readiness-ai.md) — version management is part of being able to run this
- [Compliance (AI Systems)](compliance-ai-systems.md) — the assurances an update invalidates
- [Frontier AI (Frontier Model)](frontier-ai.md) — capability changes arriving as a provider update
- [Observability (AI Systems)](observability.md) — a regression set is the detection mechanism
- [Local LLMs](local-llms.md) — self-hosting removes the surprise and hands you the update decision, including never
- [AI Incident (Reporting)](ai-incident-reporting.md) — where a behavior change that caused harm gets recorded

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-217 | Chen, L.; Zaharia, M.; Zou, J. — *How is ChatGPT's behavior changing over time?* (2023) · [link](https://arxiv.org/abs/2307.09009) | Direct measurement of behavior change between March and June 2023 releases, and the authors' framing that update timing and method are opaque. ⚠️ Preprint; the prime-number drop is substantially a behavior change, not demonstrated capability loss — do not cite as "the model got worse." |
| SRC-165 | Gama, J.; Žliobaitė, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. — *A survey on concept drift adaptation* (ACM Computing Surveys, 2014) · [link](https://doi.org/10.1145/2523813) | The established vocabulary for the other cause of the same symptom, and why distinguishing them determines the fix. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | The post-training layer whose re-running changes behavior without any change to underlying capability. ⚠️ Vendor-authored, peer-reviewed. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Why a version change matters to the compliance file: obligations attach to a system as assessed, not to a product name. |
| SRC-166 | Sculley, D.; Holt, G.; Golovin, D. et al. (Google) — *Hidden Technical Debt in Machine Learning Systems* (NeurIPS, 2015) · [link](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | Undeclared dependencies as an ML-specific debt — a prompt tuned to a version is exactly that. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Treats a material change in the system as triggering re-assessment rather than as maintenance. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Pin to dated snapshots, track deprecation as scheduled work, and keep a regression set you re-run on every version change. |
| **Organizational** | Every evaluation, red-team result and impact assessment is scoped to a model version. Record it, or the artifact cannot be defended later. |
| **Client-facing** | Explains why AI systems are re-tested on a cadence rather than approved once, and why the vendor's release schedule is now part of your risk. |
| **LLM-native** | Weights, post-training and the provider's surrounding system move independently and reach you identically. A model name is not a version. |

---

*Last updated: v1.0 · September 2026*
