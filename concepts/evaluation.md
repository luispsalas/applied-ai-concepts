# Evaluation (AI Systems)

## One-line essence
The structured practice of measuring whether an AI system does what it is supposed to do — before deployment and continuously in production.

---

## Technical definition

Evaluation is the systematic measurement of AI system performance against defined criteria. It operates across two distinct phases with different methods and different accountability implications:

**Pre-deployment evaluation**
- **Benchmarking** — standardized test sets that measure capability across defined tasks. HELM (Holistic Evaluation of Language Models) evaluates 30+ metrics including accuracy, calibration, robustness, fairness, and efficiency across multiple scenarios. Benchmarks establish a capability profile, not a deployment readiness verdict.
- **Red-teaming** — adversarial testing: deliberate attempts to elicit failures, unsafe outputs, or policy violations. Identifies failure modes that benchmarks miss because benchmarks test expected inputs.
- **Human evaluation** — human raters assess output quality on dimensions that resist automated measurement: coherence, usefulness, appropriateness. Expensive and slow; used selectively on high-stakes output dimensions.

**Production evaluation**
- **LLM-as-judge** — a second language model evaluates the outputs of the deployed model against defined criteria. Scalable but introduces a second model's biases and failure modes into the evaluation signal.
- **Sampling and spot-check pipelines** — a proportion of production outputs reviewed by humans or automated classifiers. Maintains a quality signal without full-coverage review.
- **Drift detection** — continuous monitoring of output distributions to detect when production behavior diverges from evaluated behavior. Triggers re-evaluation when thresholds are crossed.

**Evaluation is not observability.** Observability tells you what a system is doing; evaluation tells you how well it is doing it. Both are necessary; neither substitutes for the other.

---

## Plain-language version

Evaluation is how you find out whether an AI system actually works — not in theory, but for your specific use case, with your data, for your users.

Before deployment, this means running it through structured tests and deliberate attempts to break it. In production, it means continuously checking whether the system that was approved is still performing the way it did when it was approved.

Without evaluation, AI adoption is based on assumption. With it, you have evidence — and a basis for intervention when performance changes.

---

## AI literacy notes

Evaluation is the gap between "the demo worked" and "we know this works." Most AI failures in organizations trace back to the same root cause: deployment happened before evidence of performance was collected.

Three things practitioners need to understand:

1. **Benchmark scores do not transfer directly to your use case.** A model that performs well on HELM's general capability tests may underperform on your domain-specific documents, your users' actual queries, or your organization's risk profile. Published benchmarks inform model selection; they do not replace task-specific evaluation.
2. **Evaluation must be designed before deployment, not retrofitted after.** This requires knowing in advance what "good" looks like: what dimensions matter, who judges them, and what thresholds trigger action. Teams that skip this step cannot tell whether their system is working.
3. **Production drift is the most common and least monitored failure mode.** Models that pass pre-deployment evaluation can degrade silently as the world changes, as user behavior evolves, or as retrieval sources go stale. Evaluation doesn't end at launch.

---

## Governance notes

**Core question:** Who is responsible for defining what "good performance" means for each AI system — and for maintaining evidence that the system continues to meet that standard in production?

**Watch for:**
- Evaluation treated as a one-time gate at deployment rather than a continuous practice. Pre-deployment evaluation measures a model at a point in time; production behavior can diverge without any visible signal unless monitoring is in place.
- Benchmark scores used as deployment decisions without task-specific validation. General-purpose benchmarks measure capability; they do not measure fit for your use case, your data, or your users.
- Evaluation criteria defined by the team building the system rather than by the function accountable for consequences. The team optimizing a system has an incentive to set thresholds it can clear; the accountability owner should set the criteria.

**Practice:**
- Define evaluation criteria before deployment: what dimensions matter, what thresholds are acceptable, who reviews results, and what score triggers a hold or rollback.
- Maintain a production evaluation cadence: scheduled sampling reviews, automated drift alerts, and a defined re-evaluation trigger for significant model or environment changes.

**Key accountability owner:** Evaluation owner — the role responsible for defining performance criteria, commissioning pre-deployment testing, and maintaining the production monitoring signal for each AI system.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established, evolving.** Pre-deployment benchmarking and human evaluation are stable practices. Production evaluation methods — LLM-as-judge, drift detection, automated pipelines — are active development areas with known limitations. Evaluation methodology is a fast-moving field; specific techniques and benchmarks should be treated as current best practice, not fixed standards.

---

## Related concepts

- [Observability](observability.md) — evaluation measures performance quality; observability provides the signal stream that makes production evaluation possible
- [Hallucination](hallucination.md) — factual accuracy is a core evaluation dimension; hallucination rate is a key metric in most evaluation frameworks
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — human evaluation is the most reliable method for dimensions that resist automated measurement; HITL design decisions affect what can be evaluated
- [Retrieval-Augmented Generation (RAG)](rag.md) — RAG systems require evaluation of both retrieval quality and generation quality as distinct dimensions
- [Persistent Synthesis](persistent-synthesis.md) — evaluation findings should be synthesized into the knowledge base; accumulated evaluation results without synthesis produce noise, not signal
- Benchmarking — the standardized test set methodology; HELM is the most comprehensive current framework
- Red-teaming — adversarial evaluation practice; identifies failure modes that benchmarks miss

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-065 | Liang, P. et al. — *Holistic Evaluation of Language Models (HELM)* (TMLR, 2023) · [link](https://arxiv.org/abs/2211.09110) | Comprehensive benchmarking framework: 30+ metrics across accuracy, calibration, robustness, fairness, efficiency; multi-scenario evaluation methodology; distinction between capability and deployment readiness. Peer-reviewed. |
| SRC-132 | DoorDash Engineering — *How DoorDash Efficiently Scales LLM-based Order Item Recommendations* (2024) · [link](https://doordash.engineering/2024/09/17/how-doordash-efficiently-scales-llm-based-order-item-recommendations/) | Production evaluation at scale: LLM-as-judge implementation, offline/online evaluation split, sampling pipeline, performance drift monitoring in a live recommendation system. Industry case study. |
| SRC-131 | LangChain — *LangSmith Documentation: Evaluation* (2024) · [link](https://docs.smith.langchain.com/evaluation) | Practical evaluation tooling patterns: automated evaluators, human review workflows, production monitoring integration, evaluation dataset management. Vendor-produced — use as background reference for tooling patterns; not cited as methodological authority. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core practice for AI system deployment: benchmark selection, evaluation dataset design, LLM-as-judge implementation, drift detection pipelines. |
| **Organizational** | The evidence base for deployment decisions. Leaders who approve AI systems without evaluation evidence are accepting unknown risk. Evaluation is how "we tested it" becomes a defensible claim. |
| **Client-facing** | Answers the question: "how do you know it works?" — and establishes what ongoing quality assurance looks like for AI-powered products or services. |
| **LLM-native** | Prerequisite for responsible deployment. Understanding evaluation is required to interpret benchmark results, design production monitoring, and define what success looks like for a specific use case. |

---

*Last updated: v1.0 · May 2026*
