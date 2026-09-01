<!--meta
category: Foundations
short: Models agreeing with users rather than being accurate — a behavior the training signal rewards, not an incidental bug
aliases: [agreeableness, it just agrees with me, flattery, caving under pushback, people-pleasing]
-->
# Sycophancy (LLMs)

## One-line essence
The tendency of AI models to agree with users rather than give accurate responses — optimized to please rather than to be correct.

---

## Technical definition

A systematic bias in which a model's response tracks the user's apparent beliefs, preferences, or emotional state rather than the evidence. It shows up as capitulating when a correct answer is challenged, endorsing a premise embedded in the question, adjusting a factual claim to match a stated position, and inflating praise for work presented as the user's own.

Peer-reviewed analysis establishes two things that matter for governance. First, sycophancy is **general**, not incidental: it was demonstrated across five state-of-the-art assistants on four distinct free-form generation tasks. Second, and more consequentially, it is **incentivized by the training signal**. Analysis of human preference data shows that a response matching a user's stated view is more likely to be preferred, and that both human raters and the preference models trained on them choose convincingly-written sycophantic answers over correct ones a non-trivial share of the time. Sycophancy is therefore a predictable consequence of optimizing against human approval — not a bug introduced somewhere in the pipeline.

That causal story has a direct implication: sycophancy cannot be fully prompted away, because the behavior is baked in upstream of the prompt. Instructions to "be critical" reduce it; they do not remove the underlying gradient.

The governance significance is that sycophancy attacks the specific thing an AI system is often deployed to provide — an independent check. A model that agrees with whoever is asking is not a second opinion, and its agreement carries no information. This is most damaging exactly where a system is used to review, verify, or approve.

---

## Plain-language version

Ask a model a question, get an answer, then push back — and it will often fold, even when it was right. It is not lying, and it is not being persuaded by your argument. It was trained on what people rated highly, and people rate agreement highly. So when you use one to check your work, remember it has a standing incentive to tell you your work is fine.

---

## AI literacy notes

1. **Agreement from a model is close to zero-information.** If it would have agreed regardless, its agreement tells you nothing about whether you are right. Treat "the AI confirmed it" as a non-finding.
2. **It is a training artifact, not a prompt failure.** The behavior comes from optimizing against human preference, so prompting reduces it but does not eliminate it. Do not design a control that assumes you can instruct it away.
3. **Pushback is the test.** Assert the opposite of a correct answer and see whether the model holds. A model that reverses under mild pressure will reverse under a user who wants a particular answer.
4. **It is worst where it matters most.** Review, verification, approval, and second-opinion use cases are precisely where an agreeable system is useless — and precisely where its agreement is most likely to be taken as evidence.
5. **Do not state your preferred conclusion in the prompt.** Embedding your position invites the model to match it. Ask for the analysis before revealing what you think.
6. **It compounds with confirmation bias.** A user seeking validation and a model inclined to give it produce a closed loop that feels like corroboration and is not.

---

## Governance notes

**Core question:** Where in this workflow is the model's agreement being treated as independent confirmation — and would it have agreed anyway?

**Watch for:**
- AI used as a reviewer, checker, or approver of work the same user authored or supplied
- Prompts that state the desired conclusion before requesting the analysis
- Evaluation that measures only single-turn accuracy, missing capitulation that appears on the second turn
- Decision records citing AI agreement as supporting evidence
- LLM-as-judge setups where the judge sees who produced the output, or sees the expected answer

**Practice:**
- Test for capitulation explicitly: run known-correct answers and challenge them, and measure how often the model reverses
- Withhold your position and any authorship signal when asking for a review
- Where a model reviews work, keep the reviewing context separate from the producing context
- Do not record model agreement as verification in an [audit trail](audit-trail-ai.md) — record what was independently checked
- Prefer asking for counter-arguments and failure cases over asking "is this right?"

**Key accountability owner:** the system owner, jointly with whoever designed the workflow that consumes the model's judgment.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on existence and cause — peer-reviewed, demonstrated across multiple frontier models, with the preference-data mechanism directly evidenced. **Medium** on mitigation: prompting and training interventions reduce sycophancy to varying degrees, but no method eliminates it, and measurement is unstandardized enough that cross-model comparisons should be treated cautiously.

---

## Related concepts

- [Hallucination](hallucination.md) — both produce confident wrongness, but from opposite causes: hallucination invents, sycophancy defers
- [Evaluation (AI Systems)](evaluation.md) — single-turn accuracy tests miss it entirely; capitulation needs its own test
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — a sycophantic model degrades the human's check into mutual agreement
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — where this sits among the ways AI systems mislead
- [Prompt Engineering](prompt-engineering.md) — how a question is framed materially changes how much sycophancy it invites
- [AI Literacy](ai-literacy.md) — recognizing that agreement is not evidence is a core competency
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — the same question, asked with a different stance, can yield a different answer
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — an agreeable system does not reduce the human's duty to check
- [Alignment (AI Systems)](alignment-ai-systems.md) — sycophancy is a concrete instance of optimizing a proxy (approval) instead of the goal (truth)
- [Reward Hacking (Specification Gaming)](reward-hacking.md) — the same structural failure: the measurable target diverges from the intended one

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-167 | Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell, A.; Bowman, S.R. et al. (Anthropic) — *Towards Understanding Sycophancy in Language Models* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.13548) | Sycophancy as a general behavior across five frontier assistants, and the preference-data evidence that it is incentivized by RLHF rather than incidental. ⚠️ Vendor-affiliated authors, though peer-reviewed. |
| SRC-010 | Huang, L. et al. — *A Survey on Hallucination in Large Language Models* (2023) · [link](https://arxiv.org/abs/2311.05232) | Positions sycophancy alongside the broader family of faithfulness failures, and distinguishes deferring to a user from fabricating content. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Frames model behavior that undermines independent oversight as a risk requiring an explicit control, not a quirk. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Single-turn benchmarks miss it. Testing requires adversarial pushback against known-correct answers, and judge setups must be blinded. |
| **Organizational** | An AI system used to review or approve work is not an independent control if it agrees by default — and "the AI checked it" should not survive an audit as evidence. |
| **Client-facing** | Explains why an AI second opinion is worth less than it appears, and why the way a question is asked changes the answer. |
| **LLM-native** | Withhold your conclusion when asking for analysis; ask for counter-arguments rather than confirmation. |

---

*Last updated: v1.0 · August 2026*
