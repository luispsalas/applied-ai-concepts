<!--meta
category: Reliability & Quality
short: The two ways a system can be wrong — and the choice of which one to make more often is a policy decision that usually gets made by default
aliases: [false positive, false negative, false positives, false negatives, type I error, type II error, precision and recall, sensitivity and specificity, confusion matrix, base rate, threshold, what does 99% accurate mean]
tags: [Evaluation, Ethics, AI Literacy]
established: established
-->
# False Positives and False Negatives

> **Term status — Established.** Recognized terms of art, in independent use across statistics, medicine, security and machine learning long before AI.

## One-line essence
The two ways a classifier can be wrong — flagging something it should not, or missing something it should catch — and the balance between them is a policy choice, not a technical one.

---

## Technical definition

A system that sorts things into two categories can be wrong in two directions. A **false positive** flags something that should not have been flagged; a **false negative** misses something that should have been. In statistics these are Type I and Type II error; in medicine, a test's **specificity** and **sensitivity**; in machine learning they surface as **precision** and **recall**. The four possible outcomes together form the **confusion matrix**, and no single accuracy figure can represent it.

**The two errors trade against each other, and the exchange rate is set by a threshold.** Almost every classifier produces a score, not a verdict; a threshold turns the score into a decision. Move it to catch more of what you are looking for and you flag more of what you are not. **There is no setting that reduces both, only settings that choose between them** — so the threshold is where the policy lives, whatever the documentation says.

**Which error is worse is a question about consequences, not about accuracy.** A missed tumor and an unnecessary biopsy are not commensurable; neither are a fraudulent transaction let through and a legitimate customer locked out. **The technical work cannot answer it, and the people who set the threshold are frequently not the people who own the consequence.**

**Accuracy is close to meaningless when the base rate is low, and this is the single most consequential misunderstanding here.** If one in ten thousand cases is genuinely positive, a system that answers "no" every time is 99.99% accurate and useless. Worse, a test with a 1% false-positive rate applied to that population produces roughly a hundred false alarms for every true one — **so most people the system flags are not what it flagged them as, even though the system is working as specified.** The arithmetic is unintuitive and it does not go away with a better model.

**Across groups, the two error rates cannot generally be equalized at once.** Chouldechova established the constraint formally: where base rates differ between groups, a classifier that is **calibrated** cannot also have equal false-positive and false-negative rates across those groups — the properties are mathematically incompatible except in degenerate cases. **So "make the system fair" is under-specified until someone names which fairness it means**, and that choice will advantage one group's error profile over another's ([bias](bias-ai-systems.md)).

**In generative systems the same structure appears as over- and under-blocking** — a safety filter's false positives are refused legitimate requests, its false negatives are harmful outputs let through — and the two are almost never reported together ([guardrails](guardrails-ai-systems.md)).

---

## Plain-language version

Any system that makes a yes/no call can be wrong two ways: it says yes when the answer was no, or no when the answer was yes. A **false positive** is a false alarm. A **false negative** is a miss.

You cannot get rid of both. Systems work off a score, and someone picks the cutoff. Move the cutoff to catch more real cases and you also catch more innocent ones; move it the other way and you catch fewer of both. **Every system has a dial, and someone has set it — usually without describing the decision as a decision.**

Which mistake is worse depends entirely on what happens next. Missing a disease is not the same kind of wrong as an unnecessary follow-up test. Blocking a real customer is not the same kind of wrong as letting fraud through. **That is a judgment about consequences, and no amount of technical work answers it.**

Here is the part that surprises almost everyone. **When the thing you are looking for is rare, a very accurate system still produces mostly false alarms.** Suppose one in ten thousand people has some condition and the test gets it wrong 1% of the time. Test a million people and you get about a hundred real cases — and about ten thousand false alarms. **Ninety-nine out of every hundred people flagged do not have it, and the test is performing exactly as advertised.** Any claim of the form "99% accurate" tells you nothing until you know how rare the thing is.

One more, and it matters when someone promises a fair system: **you generally cannot make the false-alarm rate and the miss rate equal across two groups at the same time as keeping the scores honest.** That is a mathematical result, not an engineering shortfall. Someone has to choose which kind of fairness the system will have — and that choice is usually invisible.

---

## AI literacy notes

1. **Two errors, one dial** — a threshold sets the exchange rate between them, and it always exists.
2. **Which error is worse is a consequence question**, unanswerable from the data alone.
3. **Accuracy hides the trade entirely.** Ask for both error rates, or the confusion matrix.
4. **At low base rates, most flags are false** even from a system working as specified.
5. **The people setting the threshold are often not the people bearing the error.**
6. **Equal error rates across groups and calibration are mathematically incompatible** when base rates differ.
7. **"Make it fair" is under-specified** until someone names which of those properties is wanted.
8. **In generative systems this is over- and under-blocking**, and the two halves are rarely reported together.

---

## Governance notes

**Core question:** Who chose this system's threshold, on what grounds — and do they bear either kind of error?

**Watch for:**
- A single accuracy figure quoted with no base rate and no error breakdown ([evaluation](evaluation.md), [AI benchmarking](ai-benchmarking.md))
- A threshold set by whoever built the model, with no record of the decision or its owner
- Screening deployed against a rare condition with no estimate of how many flags will be false
- A fairness claim that does not say which fairness criterion it means ([bias](bias-ai-systems.md))
- Only one side of the trade measured — usually the visible one, since false negatives leave no trace
- Human reviewers presented with flags carrying no confidence or base-rate context ([automation bias](automation-bias.md))
- Safety filters reported by harms blocked, with refused legitimate requests uncounted ([guardrails](guardrails-ai-systems.md))
- Threshold changes shipped as tuning rather than as policy changes needing the same approval

**Practice:**
- **Report both error rates and the base rate together**, always; a single accuracy number should not leave the team
- **Name the threshold's owner** and record why it sits where it does, so a change is a decision rather than a tweak
- Estimate the absolute number of false flags at the expected volume before deployment — the rate understates it and the count is what people experience
- **Measure the invisible side deliberately.** False negatives generate no complaints, so absent an explicit sampling effort they read as success
- State which fairness criterion the system is held to, and record what it costs the other one
- Give reviewers the base rate along with the flag, since a flag without it invites over-trust
- Re-check both rates after any change to the model, the data, or the population it runs against ([model/data drift](model-data-drift.md))

**Key accountability owner:** whoever owns the consequence of the errors — not the team that set the threshold, unless those are deliberately the same people. **Where they differ, the threshold has been delegated to someone who does not experience being wrong.**

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** This is settled statistical material with decades of independent use across medicine, security and machine learning, and the arithmetic of base rates is not in dispute. The impossibility result is a formal theorem with an explicit condition — it holds where base rates genuinely differ between groups, and the degenerate cases where all criteria can be satisfied at once are named in the source rather than hidden. **The one claim stated here on judgment rather than evidence is the accountability point** — that threshold-setting is routinely delegated to people who do not bear the error. That is this wiki's framing, consistent with what the fairness literature observes but not a finding any single source reports.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — where both error rates should be measured and reported
- [Bias (AI Systems)](bias-ai-systems.md) — error rates differing across groups, and the incompatible fairness criteria
- [AI Benchmarking](ai-benchmarking.md) — published accuracy figures and what they omit
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — a stated score is not a correctness rate
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — over-blocking and under-blocking as the same trade
- [Automation Bias](automation-bias.md) — why a flag without a base rate invites over-trust
- [Human-in-the-Loop](human-in-the-loop.md) — the reviewer who sees flags but not the miss rate
- [Overfitting](overfitting.md) — the other reason a reported score overstates real-world behavior
- [Model/Data Drift](model-data-drift.md) — error rates move when the population does
- [Accountability (AI Systems)](accountability-ai-systems.md) — who answers for the error that was chosen

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-300 | Chouldechova, Alexandra (Carnegie Mellon University) — *Fair Prediction with Disparate Impact: A Study of Bias in Recidivism Prediction Instruments* (Big Data 5(2), pp. 153–163, 2017) · [link](https://doi.org/10.1089/big.2016.0047) | The **impossibility result** this entry's fairness paragraph rests on: where base rates differ between groups, a calibrated classifier cannot also equalize false-positive and false-negative rates across them. Establishes that "make it fair" is under-specified rather than merely unachieved. ⚠️ The constraint is conditional on differing base rates — state the condition, not just the result. |
| SRC-122 | Mehrabi, N. et al. — *A Survey on Bias and Fairness in Machine Learning* (ACM Computing Surveys 54(6), 2021) · [link](https://doi.org/10.1145/3457607) | The wider map of fairness criteria — demographic parity, equalized odds, calibration — used here to support the claim that a fairness claim must name which criterion it means. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Standards grounding for treating differential error rates as a governance concern with named owners rather than a modeling detail. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Never ship a single accuracy number. Report both error rates with the base rate, and record who owns the threshold. |
| **Organizational** | The threshold is a policy decision that usually gets made by default, by people who do not bear either error. Naming its owner is the cheapest control here. |
| **Client-facing** | Explains plainly why a highly accurate system can still be wrong about most of the people it flags. |
| **LLM-native** | Same structure as over- and under-blocking in safety filters — and the refused legitimate requests are almost never counted. |

---

*Last updated: v1.0 · September 2026*
