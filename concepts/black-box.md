# Black Box

## One-line essence
An AI system whose internal reasoning process cannot be observed or interpreted — even when its outputs can be.

---

## Technical definition

"Black box" describes any computational system whose internal workings are not visible or interpretable to those using or overseeing it. In the context of large language models, black box characteristics arise from three sources:

1. **Model opacity** — the billions of parameters that determine a model's outputs do not correspond to human-interpretable rules, weights, or logic paths. There is no decision tree to inspect, no rule list to audit.
2. **Emergent behavior** — capabilities and failure modes that were not explicitly programmed, and which appear (or disappear) in ways that resist prediction from architecture or training data alone. A model may perform a task reliably at one capability level and fail unpredictably at another.
3. **Non-transparent self-explanation** — model-generated explanations of its own outputs are themselves generated text, not readouts of the internal process that produced the answer. A model that explains its reasoning is not describing what happened computationally — it is generating a plausible account. (See: Hallucination — reasoning hallucination.)

Black box is often contrasted with *white box* (fully interpretable, e.g., a decision tree or rule-based system) and *grey box* (partially interpretable via post-hoc methods such as attention visualization or feature attribution). Current large language models are black boxes; interpretability research provides partial and approximate visibility, not operational transparency.

---

## Plain-language version

With most software, you can trace why it produced a result — follow the logic, inspect the rules, find where something went wrong. With large language models, you can't. The model produces an output, and the billions of calculations that led to it are not accessible in any meaningful way.

This matters for accountability: if you can't explain why the model said what it said, you can't audit it, defend it in a dispute, or reliably fix it when it goes wrong.

And the model's own explanation doesn't help. When an AI tells you why it answered a certain way, that explanation is itself a generated output — subject to the same errors as any other answer. A convincing rationale from a black-box model is not evidence that the rationale is correct.

---

## AI literacy notes

Black box is not a flaw to be fixed in a future update — it is a structural property of how current large language models work. Understanding it changes what governance looks like in practice.

Three implications:

1. **Explainability and accuracy are separate.** A model can produce a correct output with an incorrect or fabricated explanation. Evaluating AI outputs by whether the explanation sounds reasonable is evaluating the wrong signal. The explanation is itself a black-box output.
2. **Black box shifts accountability upstream.** If you cannot audit what happened inside the model, accountability must live in the observable layer: what was the input, what context was provided, what tools were available, what was the output. The harness is auditable; the model is not.
3. **Interpretability research exists but is not production-ready as an accountability mechanism.** Techniques like attention visualization, LIME, and SHAP attribution provide approximate insight useful for research — not operational audit trails sufficient for organizational accountability in most contexts.

---

## Governance notes

**Core question:** If the model's internal reasoning is not observable, what observable artifacts are being captured — and are they sufficient to reconstruct accountability after the fact?

**Watch for:**
- Explainability proxies mistaken for transparency: model-generated rationales, attention weights, or saliency maps treated as windows into actual computational process. They are approximations and generated outputs — not ground truth. Auditing the explanation rather than the harness inputs and outputs creates a false sense of accountability.
- Accountability gaps where no harness-layer logging was implemented: the model is a black box, but the inputs, context injections, tool calls, and outputs are observable. If these are not logged, there is nothing to audit.
- Risk classification that ignores opacity: treating a black-box model as lower-risk because it performs well in testing, without accounting for failure modes that test coverage does not surface. Opacity is a risk multiplier — it doesn't generate errors, but it makes them harder to detect, diagnose, and explain.

**Practice:**
- Accept the black box and govern the observable layer: log inputs, outputs, tool calls, and injected context at the harness layer. This is what can be audited; ensure it is captured systematically before deployment.
- Apply stricter HITL and verification requirements where model opacity intersects with high-consequence decisions. Where you cannot see inside the process, you need stronger controls at the boundary.

**Key accountability owner:** System auditor — the role responsible for defining what observable evidence is captured at the harness layer to enable accountability in the absence of model-internal transparency.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** The opacity of large language models is a well-documented property with an active research community (interpretability, explainability, mechanistic analysis). The practical governance implications — that accountability must live in the harness, not in model-generated explanations — are settled in the responsible AI literature.

---

## Related concepts

- [Hallucination](hallucination.md) — reasoning hallucination (confabulation) is a direct consequence of model opacity: the model's self-explanations do not reflect its actual computational process
- [Harness Paradigm](harness-paradigm.md) — since the model's interior is not observable, accountability migrates entirely to the harness layer; the harness is the auditable artifact
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — black box opacity strengthens the case for structural human review; when you cannot inspect the process, you must inspect the output
- Explainability (AI) — the research and practice of making model behavior more interpretable; addresses but does not resolve the black box problem for production accountability
- Confidence vs. Accuracy — the decoupling of how certain a model sounds from how correct it is; a direct consequence of opacity
- [Grounding](grounding.md) — anchoring outputs to verifiable external sources as a partial organizational response to model opacity

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-023 | Lipton, Z. — *The Mythos of Model Interpretability* (arXiv:1606.03490, 2016) · [link](https://arxiv.org/abs/1606.03490) | Foundational critique of interpretability claims: distinguishes simulatability, decomposability, and algorithmic transparency; establishes that model-generated explanations do not constitute transparency; widely cited framing of why black-box opacity is not simply an engineering problem to be solved. |
| SRC-024 | European Parliament — *EU Artificial Intelligence Act, Article 13: Transparency and provision of information to deployers* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Regulatory framing: high-risk AI systems must be designed to enable deployers to interpret outputs; transparency requirements as a governance response to black-box opacity. Establishes the regulatory expectation that accountability lives in the observable system layer. |
| — | ⚠️ Source needed | Governance framing: accountability migrating to the harness layer; logging inputs and outputs as the minimum observable artifact; opacity as a risk multiplier rather than error source. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs logging architecture, explainability tooling selection, and audit trail design. The technical response to opacity is harness-layer observability — knowing this shapes system design decisions. |
| **Organizational** | The concept that explains why "the AI said so" is not an accountable explanation — and what a defensible audit trail actually requires. Essential for any governance framework built around human accountability for AI outputs. |
| **Client-facing** | Directly addresses the question: "how do we know why the AI made that recommendation?" — with an honest answer and a practical alternative (harness-layer logging and review). |
| **LLM-native** | Foundation concept. Every observability, auditing, and verification design decision in this wiki exists partly in response to the opacity described here. |

---

*Last updated: v1.0 · May 2026*
