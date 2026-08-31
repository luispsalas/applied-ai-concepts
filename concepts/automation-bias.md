# Automation Bias

## One-line essence
The documented human tendency to accept what an automated system says and to stop checking — the mechanism by which a flawed output becomes a bad decision.

---

## Technical definition

The tendency to use an automated aid as a heuristic replacement for vigilant information seeking and processing: treating the system's output as a shortcut past the work of verifying it.

The peer-reviewed literature separates two error types, and the distinction is practical:

- **Commission errors** — acting on incorrect automated advice. Visible after the fact, because there is a wrong action to trace.
- **Omission errors** — failing to notice something *because the system did not flag it*. Far harder to detect, because nothing happened. There is no artifact, no decision to review, no trace.

Two findings should change how anyone designs oversight:

**People accept incorrect automated advice rather than challenge it — even when contradictory information is available to them.** The failure is not that the information was missing. It was there, and the aid's answer displaced the effort of consulting it.

**A highly reliable but imperfect aid can produce worse performance than no aid at all.** In experimental work, participants without automation outperformed those given a very-but-not-perfectly reliable aid on a monitoring task. This is the counterintuitive result that matters most: **reliability is what causes the problem.** An unreliable system keeps people checking. A system that is right almost always trains them to stop — and then it is wrong.

A systematic review of automation bias in clinical decision support found the same pattern at the system level: overall performance improves while **new errors are introduced that users fail to recognize**. Measuring aggregate improvement conceals the harm, because the aid is genuinely helping on average and quietly hurting in a specific, invisible category.

This is the mechanism that makes human oversight fail. A [human-in-the-loop](human-in-the-loop.md) who has stopped checking is a control on paper only — see the over-reliance failure in [Human–AI Collaboration Model](human-ai-collaboration-model.md). Automation bias is *why* that happens, and it is a property of people rather than of any particular system.

---

## Plain-language version

When something answers reliably enough, for long enough, people stop checking it. Not through laziness — it is what everyone does with anything that keeps being right. The trap is that the better the system gets, the less anyone verifies, so the rare wrong answer is the one most likely to sail straight through. And the errors you never see are the ones where the system simply did not mention something, and neither did you.

---

## AI literacy notes

1. **Reliability is what causes it.** A system that is wrong often keeps you alert. One that is right 95% of the time trains you to stop looking — and the remaining 5% then passes unchallenged. Improving accuracy without changing the checking habit can make outcomes worse.
2. **Omission errors are the invisible half.** You cannot review the thing the system did not flag. Any oversight process that only examines what the system produced is blind to half the problem by construction.
3. **Available information does not get consulted.** People accept wrong advice with the contradicting evidence in front of them. "The reviewer had access to the data" is not evidence the data was used.
4. **It is not carelessness and blaming individuals does not fix it.** This is a well-documented human-factors effect, studied for decades across aviation and medicine. Design and process change it; exhortation does not.
5. **Aggregate metrics hide it.** "Accuracy improved" can be true while a new class of unrecognized error is being introduced. Ask what *kind* of errors changed, not just how many.
6. **It compounds with the other biases here.** [Confident tone](confidence-vs-accuracy.md), [agreement](sycophancy-llms.md), and [attributed understanding](anthropomorphism-ai.md) all make the output easier to accept — automation bias is what converts that ease into an unchecked decision.

---

## Governance notes

**Core question:** Is the human step in this workflow actually checking — and what evidence do you have either way?

**Watch for:**
- Approval rates approaching 100%, the clearest available signal that review has become ratification
- Reviewers with no time budget for review, which guarantees the outcome regardless of intent
- Oversight processes that examine what the system produced but never what it failed to raise
- Accuracy reported without a breakdown of error *types* before and after deployment
- Highly reliable systems treated as lower-risk for oversight, when reliability is precisely what erodes it
- Human oversight cited as a control with no measurement that it functions

**Practice:**
- **Measure whether oversight changes outcomes** — override rates, time-on-task, and where feasible outcomes with and without the human step. Unmeasured oversight is an assumption
- Design for omission: require reviewers to consider what is *missing*, not only to assess what is present
- Give reviewers grounds — sources, provenance, competing options — rather than a single answer to accept or reject
- Reserve deliberate friction for consequential decisions; frictionless approval is approval in name
- Rotate or sample independent checks so some cases are assessed without seeing the system's answer first
- Treat this as a training topic in its own right, and frame it as a normal human response rather than a failing

**Key accountability owner:** the process owner for the workflow — because the remedy is process and interface design, not a better model.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** Automation bias is among the best-evidenced concepts in this wiki: decades of experimental human-factors research, a peer-reviewed systematic review, and consistent replication across aviation and clinical decision support. **Medium** on the AI-specific magnitude — the foundational studies predate generative AI, and while there is every reason to expect the effect is at least as strong with fluent, general-purpose systems, that quantification is recent and still accumulating. Mitigations are evidenced but partial: none eliminates it.

---

## Related concepts

- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the control automation bias quietly disables
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — over-reliance as a design failure; this entry is the cognitive mechanism behind it
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — attributed understanding makes the output easier to accept
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — confident delivery lowers the perceived need to check
- [Sycophancy (LLMs)](sycophancy-llms.md) — a system that agrees with you is especially easy to stop questioning
- [Verification](verification.md) — the habit automation bias erodes
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the duty persists even when the checking stops
- [Explainability (XAI)](explainability-xai.md) — grounds give a reviewer something to engage with rather than accept
- [AI Literacy](ai-literacy.md) — knowing the effect exists is a prerequisite for designing around it
- [Evaluation (AI Systems)](evaluation.md) — aggregate accuracy conceals the new error classes this introduces

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-175 | Skitka, L.J.; Mosier, K.L.; Burdick, M. — *Does automation bias decision-making?* (Int. J. Human-Computer Studies, 1999) · [link](https://doi.org/10.1006/ijhc.1999.0252) | The omission/commission distinction; that people accept wrong advice even with contradictory information available; and that participants without automation outperformed those with a highly-but-imperfectly reliable aid. |
| SRC-174 | Goddard, K.; Roudsari, A.; Wyatt, J.C. — *Automation bias: a systematic review of frequency, effect mediators, and mitigators* (JAMIA, 2012) · [link](https://doi.org/10.1136/amiajnl-2011-000089) | Systematic review evidence that systems improve average performance while introducing new errors users fail to recognize; mediators and partial mitigations. |
| SRC-109 | Green, Ben — *The Flaws of Policies Requiring Human Oversight of Government Algorithms* (Computer Law & Security Review, 2022) · [link](https://doi.org/10.1016/j.clsr.2022.105681) | Why mandated human oversight frequently fails to function as intended — the policy-level consequence. |
| SRC-015 | Stanford HAI — *Humans in the Loop: The Design of Interactive AI Systems* (2019) · [link](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems) | Oversight as an interaction-design problem rather than a staffing one. |
| SRC-167 | Sharma, M. et al. (Anthropic) — *Towards Understanding Sycophancy in Language Models* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.13548) | The compounding case: a system that agrees is one people are least inclined to challenge. ⚠️ Vendor-affiliated, peer-reviewed. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Improving accuracy without changing the checking habit can worsen outcomes. Design for omission errors and instrument whether review actually happens. |
| **Organizational** | "A human reviews it" is not a control until measured. Approval rates near 100% mean the control is not operating. |
| **Client-facing** | Explains why a human sign-off step is not automatically reassurance, and what would make it one. |
| **LLM-native** | The better your tooling gets, the less you check it. That is normal, predictable, and worth building explicit friction against where it matters. |

---

*Last updated: v1.0 · August 2026*
