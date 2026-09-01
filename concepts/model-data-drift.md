<!--meta
category: Reliability & Quality
short: The quiet decay of a deployed system as the world moves away from its training data — nothing breaks, accuracy just slides
aliases: [concept drift, model decay, it used to work, performance degradation, data drift]
tags: [Model Behavior, Data Governance, Evaluation]
-->
# Model/Data Drift

## One-line essence
The gradual degradation in an AI system's reliability as the real world changes and its training data or assumptions become outdated.

---

## Technical definition

The decay of a deployed model's performance caused by divergence between the conditions it was trained on and the conditions it now operates in. The literature separates two mechanisms that are routinely conflated:

- **Data drift** (also *covariate shift*, *virtual drift*) — the distribution of the inputs changes while the underlying input-to-output relationship holds. New user populations, new phrasing, a new product line.
- **Concept drift** (*real drift*) — the relationship between input and output itself changes, so the correct answer for a given input is now different. Fraud patterns adapt; a regulation changes what "compliant" means; a term acquires a new meaning.

The distinction matters because the remedies differ: data drift may be addressed by broadening or rebalancing training data, while concept drift means the previously learned mapping is now *wrong* and retraining on fresh labels is the only fix.

Drift is further characterized by its shape over time — **sudden** (a discrete change), **gradual** (old and new regimes overlap for a period), **incremental** (a slow slide through intermediate states), and **recurring** (seasonal or cyclical return of an earlier regime). Recurring drift is the one most often misdiagnosed as model failure.

Critically, drift is a property of a **changing world**, not a defect introduced by the model. A model that was correct at deployment and is wrong a year later has not broken; the ground beneath it moved. This is why detection depends on monitoring rather than testing: it cannot be found before release.

For LLM-based systems the classical framing needs two extensions. The model is often frozen behind a vendor API, so the organization cannot retrain — and the vendor may itself change the model underneath, producing behavior change with no corresponding change in the deployment. And in retrieval systems, drift can live in the **corpus** rather than the model: the knowledge base ages while the model stays constant.

---

## Plain-language version

A model learns from the world as it was when it was trained. The world keeps moving. Slowly, the answers that were right become less right — not because anything broke, but because the ground shifted. You will not catch this by testing before launch. The only way to see it is to keep measuring after.

---

## AI literacy notes

1. **Nothing breaks, and that is what makes it dangerous.** There is no error, no exception, no alert. Accuracy slides quietly while the system keeps returning confident answers. Drift is found by measurement or not at all.
2. **Data drift and concept drift need different responses.** Inputs changing is not the same as the right answer changing. Diagnose which one you have before deciding to retrain — retraining on stale labels fixes neither.
3. **A frozen vendor model does not mean frozen behavior.** When the model sits behind an API, the provider can change it under you. Version-pin where you can, and monitor for behavior change even when *you* changed nothing.
4. **In retrieval systems the corpus drifts too.** A perfectly stable model over an aging knowledge base produces confidently outdated answers. [RAG](rag.md) moves part of the drift problem from the model to the content.
5. **Recurring drift is regularly misread as failure.** Seasonal patterns return. Before retraining on an anomaly, check whether you have seen this regime before.

---

## Governance notes

**Core question:** How would you know this system had become less reliable — and how long would it take you to find out?

**Watch for:**
- Performance measured at deployment and never again, with launch metrics cited long after they stopped being true
- Monitoring on system health (latency, errors, uptime) but not on output quality — a system can be perfectly available and increasingly wrong
- Detection dependent on user complaints, which means detection is late and biased toward the loudest cases
- No owner for the question "is this still accurate?", so nobody asks it
- Vendor model updates absorbed silently, with no re-evaluation triggered

**Practice:**
- Define drift metrics and thresholds *before* deployment, alongside the go-live criteria — retrofitting a baseline after the fact is guesswork
- Monitor inputs and outputs separately: input distribution shift is an early warning, output quality decay is the harm
- Set a scheduled re-evaluation cadence rather than relying on incident-driven review
- Treat a vendor model version change as a change requiring re-evaluation, exactly like a change of your own
- For retrieval systems, track corpus freshness as a first-class metric alongside model performance

**Key accountability owner:** the system owner, with the data owner for input-side monitoring.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the taxonomy and mechanisms — concept drift has a mature, peer-reviewed literature predating the current AI wave, and the categories have held up. **Medium** on application to LLM-based systems, where detection methods designed for supervised learning with ground-truth labels do not transfer cleanly to open-ended generation, and where the vendor-controlled-model case has no settled practice.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — the measurement that makes drift visible; drift is why evaluation cannot be a one-time gate
- [Observability (AI Systems)](observability.md) — drift detection is an observability capability, not a modeling one
- [Data Quality](data-quality.md) — the input side of the problem; degrading data produces degrading outputs
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the slow, silent member of the family
- [RAG](rag.md) — moves part of the drift surface from the model to the retrieved corpus
- [Knowledge Base](knowledge-base.md) — corpus freshness is a drift control
- [Operational Readiness (AI)](operational-readiness-ai.md) — the monitoring capability must exist before deployment, not after the first incident
- Continuous Feedback & Improvement — the loop that turns drift detection into correction
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — a drifting model stays confident while becoming less accurate

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-165 | Gama, J.; Žliobaitė, I.; Bifet, A.; Pechenizkiy, M.; Bouchachia, A. — *A survey on concept drift adaptation* (ACM Computing Surveys 46(4), 2014) · [link](https://doi.org/10.1145/2523813) | The canonical taxonomy: data vs concept drift, the sudden/gradual/incremental/recurring shapes, and detection-and-adaptation strategies. |
| SRC-166 | Sculley, D. et al. (Google) — *Hidden Technical Debt in Machine Learning Systems* (NIPS, 2015) · [link](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | Why monitoring is structurally necessary: the world changes underneath a deployed model, and the surrounding system — not the model — is where that has to be caught. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places post-deployment monitoring inside a recognized risk-management lifecycle rather than treating it as optional maintenance. |
| SRC-028 | Alexander, Emmimal P. — *RAG Is Blind to Time* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/rag-is-blind-to-time-i-built-a-temporal-layer-to-fix-it-in-production/) | The retrieval-side case: a stable model over an aging corpus produces confidently outdated answers. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Drift metrics and thresholds are part of the deployment definition of done, not a later addition — and input drift is the leading indicator of output decay. |
| **Organizational** | An AI system's accuracy is a claim with an expiry date. Someone must own the question "is this still true?" and be resourced to answer it. |
| **Client-facing** | Explains why an AI system needs ongoing measurement rather than a one-time acceptance test, and why launch metrics are not a permanent guarantee. |
| **LLM-native** | The model may change under you without notice, and in retrieval systems the corpus drifts independently of the model — both need watching. |

---

*Last updated: v1.0 · August 2026*
