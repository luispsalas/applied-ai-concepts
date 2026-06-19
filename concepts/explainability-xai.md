# Explainability (XAI)

## One-line essence
The ability to describe, in terms a human can understand, why an AI system produced a specific output — a prerequisite for accountability in high-stakes decisions.

---

## Technical definition

Explainability (Explainable AI, XAI) is the capacity to render an AI system's behavior — a specific output or its general logic — understandable to a relevant human audience. It is often distinguished from interpretability: interpretability concerns how intrinsically transparent a model's mechanism is; explainability concerns whether a usable account of a decision can be produced, including post-hoc. Doshi-Velez & Kim (2017) note there is no single agreed definition or metric, and propose evaluating explanations by whether they serve their purpose for their audience rather than by an abstract standard.

Approaches span intrinsically interpretable models (linear models, decision trees), post-hoc attribution methods (feature importance, SHAP, LIME, saliency), and example/counterfactual-based explanations. The DARPA XAI program (Gunning & Aha 2019) framed the goal as systems whose decisions can be understood and appropriately trusted by end users, requiring advances in explainable models, explanation interfaces, and the psychology of explanation. For large language models the terrain shifts again: LLMs can generate fluent natural-language self-explanations at scale, but these can be plausible and wrong — explanation and faithfulness are not the same thing (Singh et al. 2024).

---

## Plain-language version

Explainability is being able to answer "why did the AI decide that?" in a way a person can actually understand and check.

This matters most when the stakes are high. If an AI denies someone a loan, flags a medical scan, or rejects a job application, "the model said so" is not an acceptable answer — to the person affected, to a regulator, or to a court. Someone needs to be able to give a real reason.

The catch with modern AI: a system can produce a confident, fluent explanation that sounds great and is simply not the actual reason it decided what it did. An explanation that sounds good is not the same as an explanation that's true. That gap — between a plausible story and the faithful reason — is the hard part of explainability.

---

## AI literacy notes

1. **Explainability is audience-relative.** An explanation good enough for an ML engineer (a SHAP plot) is useless to a loan applicant; one good enough for a regulator differs again. "Is it explainable?" is incomplete without "to whom, for what decision?"
2. **A model's self-explanation is not necessarily its real reason.** Post-hoc explanations — including an LLM's own narration — can be unfaithful: persuasive, coherent, and disconnected from the actual computation. Faithfulness must be tested, not trusted (Singh et al. 2024).
3. **Explainability is a prerequisite for accountability, not a substitute for it.** Being able to explain a decision is necessary for someone to answer for it — but the explanation doesn't carry the responsibility. A human still does.

---

## Governance notes

**Core question:** For each high-stakes decision this system informs, can you produce an explanation that is (a) understandable to the affected person and (b) faithful to how the decision was actually made?

**Watch for:**
- Model-generated explanations accepted as faithful without testing
- Explanations pitched at the wrong audience (engineer-grade output handed to end users)
- Explainability treated as satisfied by a dashboard nobody can interpret
- "The model is too complex to explain" used to avoid accountability rather than trigger a simpler-model or stronger-oversight decision

**Practice:**
- Define the explanation audience and standard per decision class
- Test explanation faithfulness, don't assume it
- Prefer interpretable models where stakes and regulation demand it
- Log the inputs and factors behind consequential decisions at the harness layer so a real account can be reconstructed

**Key accountability owner:** the decision owner is accountable for producing faithful, audience-appropriate explanations; explainability tooling supports this duty but does not discharge it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established (field), active (LLM frontier).** XAI is a mature research field with standardized methods (attribution, counterfactuals) and a foundational literature (Doshi-Velez & Kim 2017; Gunning & Aha 2019). Explainability for large generative models is an active, fast-moving area: self-explanation, mechanistic interpretability, and faithfulness evaluation are open problems (Singh et al. 2024). Regulatory demand (EU AI Act, GDPR) is pushing explainability from research aspiration to compliance requirement.

---

## Related concepts

- [Black Box](black-box.md) — explainability is the set of techniques for working around opacity; the black box is the problem it responds to
- [Hallucination](hallucination.md) — a model's self-explanation can itself be hallucinated, which is why faithfulness must be tested
- Confidence vs Accuracy — a fluent, confident explanation is not evidence that it is the true reason
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — explanation enables accountability but does not transfer it away from humans
- [Accountability (AI Systems)](accountability-ai-systems.md) — being answerable for a decision depends on being able to give a faithful account of it
- [AI Governance](ai-governance.md) — explainability is moving from research aspiration to regulatory requirement
- [Observability](observability.md) — observability instruments the system boundary; explainability interprets the decision — complementary, not the same

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-123 | Doshi-Velez, F. & Kim, B. — *Towards a Rigorous Science of Interpretable Machine Learning* (arXiv:1702.08608, 2017) · [link](https://arxiv.org/abs/1702.08608) | Foundational: no single definition/metric of interpretability; evaluate explanations by fitness for audience and purpose. |
| SRC-124 | Gunning, D. & Aha, D. — *DARPA's Explainable Artificial Intelligence (XAI) Program* (AI Magazine 40(2), 2019) · [link](https://doi.org/10.1609/aimag.v40i2.2850) | Program-level framing: explainable models, explanation interfaces, and the psychology of trust. |
| SRC-125 | Singh, C. et al. — *Rethinking Interpretability in the Era of Large Language Models* (arXiv:2402.01761, 2024) · [link](https://arxiv.org/abs/2402.01761) | LLM-era shift: natural-language self-explanation at scale, plus new risks (hallucinated, unfaithful explanations). |
| SRC-024 | European Parliament — *EU Artificial Intelligence Act, Article 13: Transparency* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Transparency/explainability obligations for high-risk systems. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs the choice between intrinsically interpretable models and post-hoc methods, and the requirement to test explanation faithfulness rather than assume it. |
| **Organizational** | The capability that makes high-stakes AI decisions defensible to regulators, courts, and affected people. Without it, accountability has nothing to stand on. |
| **Client-facing** | Answers "can you tell me why the AI did that?" — and sets honest expectations about what current methods can and cannot faithfully reveal. |
| **LLM-native** | Central to auditing LLM behavior. Self-explanations are a tool, not ground truth; faithfulness evaluation and mechanistic interpretability are the frontier. |

---

*Last updated: v1.0 · June 2026*
