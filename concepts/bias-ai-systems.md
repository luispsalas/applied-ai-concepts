# Bias (AI Systems)

## One-line essence
Systematic errors in AI outputs that unfairly advantage or disadvantage certain groups — often inherited from training data or embedded in design choices, rarely visible in the output itself.

---

## Technical definition

Bias in AI systems is systematic, repeatable error that produces outcomes which unfairly advantage or disadvantage particular groups. It is not random noise and not an occasional mistake — it is structured deviation that recurs across a population. NIST SP 1270 identifies three interacting categories:

1. **Systemic bias** — present in the institutions, historical data, and social structures the system learns from; the training data faithfully records a biased world and the model reproduces it.
2. **Statistical / computational bias** — introduced by the data and modeling pipeline: unrepresentative samples, label noise, proxy variables, optimization choices, and evaluation on non-representative benchmarks.
3. **Human / cognitive bias** — introduced by the people who frame the problem, choose features, and interpret outputs.

Bias is rarely visible in any single output; a loan denial or screening rejection looks individually reasonable, and the bias is a property of the distribution of decisions across groups, detectable only in aggregate. Fairness is not a single metric — demographic parity, equalized odds, and calibration can be mutually incompatible — so "unbiased" is always a choice about which fairness criterion the system is held to (Mehrabi et al. 2021).

---

## Plain-language version

An AI system is biased when it is systematically wrong in a way that consistently helps some groups and hurts others. The key word is systematically — not "it made a mistake," but "it makes the same kind of mistake, in the same direction, again and again."

Most bias is inherited, not invented. If a model learns from historical hiring decisions that favored one group, it learns to favor that group — even if no one intended it and even if the protected attribute was never in the data. The model finds proxies (a postal code, a school name, an employment gap) and reconstructs the pattern.

You usually can't see bias by looking at one decision. It hides in the pattern across thousands of decisions. That's what makes it dangerous: each individual output looks defensible.

---

## AI literacy notes

1. **Bias is not the same as inaccuracy.** A model can be highly accurate overall and still be badly biased against a minority subgroup — because aggregate accuracy is dominated by the majority. "95% accurate" tells you nothing about who the 5% are.
2. **Removing the protected attribute does not remove the bias.** Models reconstruct sensitive attributes from correlated features (proxies). Fairness must be measured on outcomes, not assumed from input blindness.
3. **"Fair" is a contested, multi-valued choice.** Several reasonable fairness definitions are mathematically incompatible. Choosing one is a governance decision with winners and losers, and should be made explicitly and documented — not left to a library default.

---

## Governance notes

**Core question:** Has someone measured how this system's outcomes differ across groups — and decided, explicitly, which fairness definition it is held to?

**Watch for:**
- Aggregate accuracy reported with no subgroup breakdown
- "We removed the protected attribute" treated as proof of fairness
- Fairness metric chosen implicitly by a library default rather than a documented decision
- No monitoring for bias drift after deployment

**Practice:**
- Require disaggregated evaluation (performance by subgroup) before deploying any consequential system
- Document the chosen fairness criterion and its rationale
- Assign a named owner for bias measurement on a defined cadence
- Treat proxy variables as in-scope for audit

**Key accountability owner:** the model/decision owner is accountable for bias measurement and the fairness-definition choice — it cannot be delegated to the tool or the vendor.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** The existence, categories, and mechanisms of AI bias are well-documented and standardized (NIST SP 1270), and the fairness-metrics literature is mature and peer-reviewed (Mehrabi et al. 2021). What remains active is operational: which fairness definition applies in a given regulatory or business context, how to mitigate bias without introducing new harms, and how bias manifests in large generative models where training data is vast and opaque.

---

## Related concepts

- [Data Quality](data-quality.md) — bias is frequently a data-quality failure: unrepresentative or skewed training data is the most common upstream source
- [Hallucination](hallucination.md) — a different failure mode; bias is systematic skew across groups, hallucination is fabricated content
- [Explainability (XAI)](explainability-xai.md) — detecting and diagnosing bias often depends on being able to see which features drove a decision
- [Black Box](black-box.md) — opacity makes bias harder to locate; bias must be measured on outputs when internals can't be inspected
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — responsibility for discriminatory outcomes stays with the humans who deployed the system
- [AI Governance](ai-governance.md) — fairness-criterion selection and bias monitoring are governance decisions, not purely technical ones
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — bias is one named failure family, requiring its own detection-and-response control

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-121 | NIST — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (SP 1270, 2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Primary taxonomy: systemic, statistical/computational, and human-cognitive bias across the AI lifecycle; socio-technical framing. |
| SRC-122 | Mehrabi, N. et al. — *A Survey on Bias and Fairness in Machine Learning* (ACM Computing Surveys 54(6), 2021) · [link](https://doi.org/10.1145/3457607) | Peer-reviewed survey of bias sources and formal fairness definitions; establishes that fairness metrics can be mutually incompatible. |
| SRC-001 | NIST — *Artificial Intelligence Risk Management Framework (AI RMF 1.0)* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | MEASURE/MANAGE functions: bias as a managed risk requiring measurement across the lifecycle. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs dataset auditing, fairness-metric selection, subgroup evaluation, and proxy detection. Aggregate accuracy is not a fairness signal — disaggregated evaluation is mandatory. |
| **Organizational** | The risk that turns an AI deployment into a discrimination liability. Bias is measurable and therefore auditable — and increasingly, legally required to be. |
| **Client-facing** | Answers "could your AI discriminate?" honestly: bias is inherited by default and must be actively measured and mitigated, not assumed absent. |
| **LLM-native** | Bias in foundation models is harder to locate (vast, opaque training data) and surfaces in generation, ranking, and refusal behavior — making output-level evaluation and red-teaming essential. |

---

*Last updated: v1.0 · June 2026*
