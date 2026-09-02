<!--meta
category: Reliability & Quality
short: Using one language model to grade another's output — the only way to evaluate at volume, with documented biases including a preference for its own writing
aliases: [LLM as a judge, model graded evaluation, AI grading AI, automated evaluation, model as evaluator, auto-eval, judge model]
tags: [Evaluation, AI Literacy]
established: established
-->
# LLM-as-Judge

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Using a language model to grade another model's output — the only evaluation method that scales to production volume, and one whose known biases mean its agreement with you is not the same as its correctness.

---

## Technical definition

A judge model is given a task, one or more candidate outputs, and a rubric, and returns a score or a preference. It substitutes for human raters in the places where human rating is too slow or too expensive — regression testing, A/B comparison, production monitoring, and preference data collection.

**The case for it is empirical, not merely practical.** Zheng et al. (NeurIPS 2023) found that strong judges *"can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans."* That last clause is the load-bearing one: **the judge disagrees with humans about as often as humans disagree with each other**, which is the standard any human process is already held to.

**The same paper names the failure modes, and they are systematic rather than random** — which matters, because random error averages out across a large evaluation set and systematic error does not:

| Bias | What it does |
|---|---|
| **Position** | Prefers a candidate based on where it appears in the prompt |
| **Verbosity** | Prefers longer answers, independent of quality |
| **Self-enhancement** | Prefers output resembling its own |
| **Limited reasoning** | Grades poorly on tasks it cannot itself perform |

**Self-enhancement bias is the one with governance consequences.** If the judge and the system under test come from the same model family, the evaluation is structurally predisposed toward passing. That is not a subtle effect to be corrected for; it is a conflict of interest built into the setup.

**The deeper limit: agreement is concordance, not correctness.** An 80% agreement rate says the judge and the humans reach the same verdict, not that either is right. Where both share a blind spot — a plausible-sounding wrong answer, a confidently-argued falsehood — the metric rises while quality does not. And the judge cannot reliably grade what it cannot do, which is precisely the case ([scalable oversight](scalable-oversight.md)) where automated review is most wanted.

---

## Plain-language version

Checking AI output by hand works until there is too much of it. The obvious fix is to have another AI do the marking, and it works better than you might expect: in one study, a strong judge model agreed with human raters about 80% of the time — which is roughly how often two humans agree with each other.

But the mistakes it makes are not random, and that is the problem. Random errors cancel out over a large test set. These do not, because they lean consistently in one direction:

- It favors whichever answer it sees first
- It favors longer answers
- **It favors writing that resembles its own**
- It marks badly on anything it could not do itself

The third one deserves attention. If you use a model to grade output from the same family of models, you have built something predisposed to approve. It looks like an independent check and is not.

And there is a limit underneath all of it. Agreeing with people is not the same as being right. If the judge and the humans share the same blind spot — a confident, well-written, wrong answer — the score goes up and the quality does not.

---

## AI literacy notes

1. **Agreement is not correctness.** An 80% agreement rate measures concordance with human raters; it says nothing about whether either was right.
2. **The biases are systematic, so scale does not cancel them.** More evaluation examples reduce noise, not a consistent lean.
3. **Self-enhancement bias makes same-family judging a conflict of interest**, not a minor correction.
4. **Verbosity bias rewards length**, so a system optimized against a judge drifts toward longer output regardless of value.
5. **Position bias is testable and cheap to control** — swap the order and see whether the verdict follows the position.
6. **A judge cannot grade what it cannot do**, which is exactly the hard case automated review is wanted for.
7. **A rubric is part of the instrument.** Vague criteria produce plausible scores with no defined meaning.
8. **Judges drift with model versions.** A score series that spans a provider update is not one series ([model version & update](model-version-update.md)).

---

## Governance notes

**Core question:** What does our judge's score actually license us to say — and would we notice if it were systematically wrong in the direction we like?

**Watch for:**
- Judge and system-under-test drawn from the same model family, with no acknowledgement of self-enhancement bias
- Judge agreement with humans reported as accuracy ([confidence vs accuracy](confidence-vs-accuracy.md))
- No held-out human-rated sample, so there is nothing to detect judge drift against
- A judge used as a quality *gate* on tasks its own capability does not cover ([scalable oversight](scalable-oversight.md))
- Automated scores in a governance artifact presented as an independent control
- Candidate order held constant across a comparison, leaving position bias uncontrolled
- Judge model or prompt changed mid-series, breaking comparability without a version record
- Systems tuned against the judge until they optimize for the metric rather than the goal ([reward hacking](reward-hacking.md))

**Practice:**
- **Use a different model family for the judge than for the system under test**, and say so in the evaluation record
- **Randomize or swap candidate order** and check the verdict does not follow position — the cheapest bias control available
- Keep a standing human-rated sample and re-measure judge–human agreement periodically; a judge that has drifted looks identical to one that has not
- Control for length, or measure whether the judge's preference tracks it
- State the rubric explicitly and version it alongside the judge model and prompt ([audit trail](audit-trail-ai.md))
- **Do not use a judge as the final gate on anything a human could not adjudicate** — that is the substitution [scalable oversight](scalable-oversight.md) warns about
- Report judge scores as evidence for a claim, alongside what would falsify it

**Key accountability owner:** whoever owns the evaluation evidence for the system — because a judge is an instrument, and the person relying on a measurement owns the question of whether the instrument is calibrated.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** Both halves come from the same peer-reviewed NeurIPS paper, which is unusually clean: the method's value and its named failure modes were established together rather than the caveats arriving later. **The scope limit matters more than the confidence rating:** the 80% agreement figure is for strong judges on general chat-quality comparison, and does not transfer to domain-specific, safety-critical or expert-level grading, where the judge's own capability is the binding constraint. Mitigations for position and verbosity bias are practical and tested; **no reliable mitigation exists for the case where judge and reviewed system share a blind spot**, which is the failure most likely to matter and the least likely to be visible in the metric.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — the practice this is a method within
- [Scalable Oversight](scalable-oversight.md) — the general problem, and the circularity this instance inherits
- [Automation Bias](automation-bias.md) — why an automated score gets accepted more readily than it should
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — agreement and correctness are separate claims
- [Reward Hacking (Specification Gaming)](reward-hacking.md) — what happens when a system is optimized against the judge
- [Sycophancy (LLMs)](sycophancy-llms.md) — the same agreeableness pressure, on the generating side
- [Model Version & Update](model-version-update.md) — a judge is a dependency, and score series break across versions
- [Data Leakage (Model Evaluation)](data-leakage-model-evaluation.md) — the other way an evaluation number stops meaning what it says
- [Audit Trail (AI Systems)](audit-trail-ai.md) — judge model, prompt and rubric belong in the record

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-242 | Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.; Lin, Z.; Xing, E.P.; Zhang, H.; Gonzalez, J.E.; Stoica, I. — *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena* (NeurIPS Datasets & Benchmarks, 2023) · [link](https://arxiv.org/abs/2306.05685) | Both halves: strong judges achieve "over 80% agreement, the same level of agreement between humans", and the four named biases — position, verbosity, self-enhancement, and limited reasoning ability. |
| SRC-220 | Bowman, S.R.; Hyun, J.; Perez, E. et al. (Anthropic) — *Measuring Progress on Scalable Oversight for Large Language Models* (2022) · [link](https://arxiv.org/abs/2211.03540) | The circularity this method inherits: where a human could not adjudicate the output, an automated judge relocates the trust question rather than answering it. ⚠️ Vendor-authored preprint. |
| SRC-174 | Goddard, K.; Roudsari, A.; Wyatt, J.C. — *Automation bias: a systematic review* (JAMIA, 2012) · [link](https://doi.org/10.1136/amiajnl-2011-000089) | Why a judge's score is accepted more readily than a human rater's, and degrades rather than informs the reviewer's own judgment. |
| SRC-065 | Liang, P. et al. (Stanford CRFM) — *Holistic Evaluation of Language Models (HELM)* (TMLR, 2023) · [link](https://arxiv.org/abs/2211.09110) | Multi-metric, multi-scenario evaluation as the surrounding practice — a judge supplies one metric among several, not a verdict. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Use a different model family than the system under test, randomize candidate order, version the judge model, prompt and rubric together, and keep a human-rated sample to detect drift. |
| **Organizational** | A judge score is an instrument reading, not an independent control. Same-family judging is a conflict of interest, and agreement with humans is not accuracy. |
| **Client-facing** | Explains how quality is checked at volume, and what human review still covers. |
| **LLM-native** | The biases are systematic, so scale does not cancel them — and self-enhancement bias means a model family grading itself is predisposed to pass. |

---

*Last updated: v1.0 · September 2026*
