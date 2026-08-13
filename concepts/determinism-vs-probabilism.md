# Determinism vs Probabilism

## One-line essence
The difference between systems that always produce the same output from the same input and those that generate statistically likely outputs — AI models are probabilistic, not deterministic.

---

## Technical definition

A deterministic system always produces the same output for a given input; a probabilistic system produces outputs drawn from a probability distribution. LLMs are probabilistic by construction: at each step the model emits a distribution over possible next tokens and a decoding strategy selects from it (SRC-144). Sampling parameters — temperature, top-p/nucleus, top-k — control how strongly selection favors the most-likely token versus explores less-likely ones; higher temperature widens the effective distribution and increases variability. Even at temperature 0 ("greedy" decoding, nominally deterministic), production inference is frequently not bitwise-reproducible: batching, hardware, and kernel implementation make results vary with operational load (SRC-145). LLM behavior therefore sits on a spectrum — tunable toward repeatability but not guaranteed identical — a structural property of the technology, not a bug to be fully engineered away.

---

## Plain-language version

Give a calculator "2+2" and you get "4" every time — that is deterministic. Ask an AI model the same question twice and you may get two different answers, because it doesn't compute one correct output; it draws from a range of statistically likely ones. A setting called "temperature" controls how adventurous those draws are: low temperature makes it stick to the safest, most predictable wording; high temperature makes it more varied and creative. You can turn the dial toward consistency, but you generally cannot make it behave like a calculator — and even the most consistent setting can still wobble because of how the computation runs on the hardware.

---

## AI literacy notes

1. **Same input, different output is normal — not a malfunction.** It follows directly from how the model generates. Any process that assumes an AI will repeat itself exactly has to be designed with that in mind.
2. **Temperature is a controllable trade-off, not a correctness knob.** Lower temperature buys consistency and reduces (not eliminates) surprising outputs; higher buys diversity. Neither makes the output more true.
3. **"Deterministic" settings are only approximately deterministic.** Temperature-0 reduces variability, but production systems can still differ run to run (SRC-145) — so reproducibility for audits, evaluation, and debugging must be engineered and verified, not assumed.
4. **This is why evaluation must be statistical.** Passing a test once is not reliability; a probabilistic system has to be measured across many runs (see Evaluation, Failure Modes).

---

## Governance notes

**Core question:** Does the process treat AI output as repeatable when it is not?

**Watch for:**
- Workflows that assume identical re-runs (caching, reconciliation, "it said X last time")
- Reliability judged from a single successful run
- Audit or debugging that assumes an output can be exactly reproduced later

**Practice:**
- Design for variability (tolerances, not exact matches)
- Evaluate across many runs, not once
- Where reproducibility is genuinely required (audit, RL, regression testing), engineer and verify it (fixed seed/decoding + batch-invariant inference) rather than assuming temperature-0 suffices

**Key accountability owner:** the system owner, with the evaluation owner for reliability measurement.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** That LLMs are probabilistic next-token samplers is settled and mechanistically understood. The one nuance still being actively engineered is inference-level reproducibility (SRC-145) — recent work shows it is achievable but not the default.

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — the probabilistic generator whose next-token sampling this concept explains
- [AI Hallucination](hallucination.md) — a downstream consequence: probabilistic generation with no truth constraint produces confident errors
- [Evaluation (AI Systems)](evaluation.md) — why evaluation must be statistical: a probabilistic system is measured across many runs, not one
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — non-reproducibility is itself a failure surface for testing, debugging, and audit
- Temperature (LLMs) — the sampling parameter that tunes the determinism–variability trade-off
- [Prompt Engineering](prompt-engineering.md) — prompt design interacts with sampling: structure reduces (but never removes) output variance

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-144 | Holtzman, A. et al. — *The Curious Case of Neural Text Degeneration* (ICLR, 2020) · [link](https://arxiv.org/abs/1904.09751) | Output is sampled from a token distribution; decoding strategy (nucleus/top-p) determines it — the mechanism behind output variability. |
| SRC-142 | Zhao, W.X. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | The probabilistic next-token foundation of LLMs. |
| SRC-145 | He, H. / Thinking Machines Lab — *Defeating Nondeterminism in LLM Inference* (2025) · [link](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) | Even temperature-0 inference is often not bitwise-reproducible (batch/kernel effects); reproducibility is achievable but engineered. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Sampling parameters and reproducibility are design decisions; anything needing exact repeatability must be engineered and verified. |
| **Organizational** | Processes that assume repeatable outputs (reconciliation, caching, "it said X before") need rethinking for a probabilistic system. |
| **Client-facing** | Explains why the AI can answer the same question two ways — expected behavior, not a defect. |
| **LLM-native** | The reason evaluation is statistical and a single-run "it worked" is not reliability. |

---

*Last updated: v1.0 · July 2026*
