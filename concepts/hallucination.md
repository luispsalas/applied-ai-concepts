# Hallucination

## One-line essence
AI models generate plausible-sounding content that is factually incorrect — confidently and without warning.

---

## Technical definition

Hallucination refers to the tendency of language models to produce outputs that are factually incorrect, logically inconsistent, or entirely fabricated, while presenting them with the same fluency and apparent confidence as accurate information. The term covers two distinct phenomena:

1. **Factual hallucination:** The model asserts false facts — incorrect dates, non-existent citations, wrong attributions, invented statistics.
2. **Reasoning hallucination (confabulation):** The model produces plausible-sounding explanations for its outputs that do not reflect its actual computational process. The explanation may be coherent and convincing while having no reliable relationship to why the output was generated.

Hallucination is not a malfunction. It is an emergent property of how language models work: they generate statistically probable next tokens, not verified facts. Fluency and accuracy are trained independently; the model has no built-in mechanism to distinguish between what it knows and what it has confabulated.

---

## Plain-language version

When an AI model gets something wrong, it rarely says "I'm not sure." It usually sounds just as confident as when it's right.

This matters because the signal most people use to judge whether information is trustworthy — how clearly and confidently it's stated — is exactly the signal that fails with AI. A hallucinated answer looks identical to a correct one.

There are two kinds to watch for: wrong facts (the model invents a source, misremembers a date, creates a statistic) and wrong reasoning (the model explains why it gave an answer, but the explanation doesn't reflect what actually drove the output).

---

## AI literacy notes

Hallucination is the most consequential literacy gap in organizational AI adoption. Teams that understand it change their workflows; teams that don't build false confidence into decisions.

Three practical implications:

1. **Verification can't be selective.** If you only verify outputs that seem suspicious, you will miss hallucinations — because they don't seem suspicious. Verification must be structural, not reactive.
2. **Confidence is not a reliability signal.** The model's tone, fluency, and assertiveness carry no information about factual accuracy. Treat them as noise.
3. **Explanations are not transparent.** When a model explains its reasoning, that explanation is itself a generated output — subject to the same hallucination risk as any other content. A convincing rationale is not a reliable rationale.

Grounding strategies (RAG, retrieval from verified sources, tool use) reduce hallucination risk but do not eliminate it. Human verification remains necessary for any output where accuracy is consequential.

---

## Governance notes

**Core question:** Who is accountable for verifying AI outputs before they influence decisions?

**Watch for:**
- Verification that is reactive (checking outputs that seem suspicious) rather than structural (checking by design). Hallucinated outputs do not seem suspicious — so reactive verification misses them.
- Fluency and confidence of tone used as a proxy for factual accuracy. They carry no information about correctness.
- AI-generated explanations treated as transparent insight into the model's reasoning. They are generated outputs subject to the same hallucination risk as any other content.

**Practice:**
- Define verification as a structural step before deployment: which outputs, at what volume, reviewed by whom, using what criteria.
- Grounding strategies (RAG, retrieval, tool use) reduce hallucination risk but do not eliminate it. Do not treat them as a substitute for verification on consequential outputs.

**Key accountability owner:** Output quality owner — the role responsible for verifying AI outputs before they reach downstream use or decision-making.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** Hallucination is a well-documented property of current-generation language models. The mechanisms are understood; mitigation strategies are active areas of research and engineering. The term has stabilized.

---

## Related concepts

- [Persistent Synthesis](persistent-synthesis.md) — a synthesis approach that flags contradictions rather than accumulating potentially hallucinated content
- [Harness Paradigm](harness-paradigm.md) — grounding and verification controls are implemented at the harness layer
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — human review as a structural check on hallucinated outputs
- [Grounding](grounding.md) — the practice of anchoring model outputs to verified external sources
- Retrieval-Augmented Generation (RAG) — a technical pattern that reduces hallucination by providing the model with retrieved reference material

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-010 | Zhang et al. — *A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions* (arXiv:2311.05232, 2023) · [link](https://arxiv.org/abs/2311.05232) | Defines factuality hallucination (discrepancy with verifiable real-world facts) and faithfulness hallucination (divergence from user input or internal consistency). Provides taxonomy, detection methods, and mitigation overview. Peer-reviewed — ACM Transactions on Information Systems. |
| — | ⚠️ Source needed | Organizational implications framing: verification as structural rather than reactive; confidence as a non-reliability signal; model-generated explanations as subject to the same hallucination risk as any other output. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs verification architecture, grounding strategy, and output review pipelines. Hallucination risk is a design constraint, not an edge case. |
| **Organizational** | The highest-impact literacy concept for non-technical leaders. Changes how AI outputs should be integrated into decision-making workflows. |
| **Client-facing** | Explains why AI tools require human oversight — and why "it sounded right" is not a sufficient quality check. |
| **LLM-native** | Foundation assumption for all output evaluation. Every downstream concept (grounding, HITL, harness controls) exists partly in response to hallucination. |

---

*Last updated: v1.2 · May 2026*
