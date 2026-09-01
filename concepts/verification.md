<!--meta
category: Reliability & Quality
short: Checking this output against ground truth before trusting it — and the finding that people check least on the problems that most need it
aliases: [fact checking AI output, checking the answer, should I trust this, validating output, double checking]
tags: [Evaluation, AI Literacy]
-->
# Verification

## One-line essence
Checking AI output against ground truth before trusting it — run the code, check the source, test the claim — because plausible is not the same as correct.

---

## Technical definition

The act of establishing, for a specific output, that it is actually true or actually works — by reference to something outside the system that produced it. Running the code. Opening the cited page and reading it. Testing the claim against a system of record. Asking someone who knows.

**Verification is not [evaluation](evaluation.md), and conflating them is the most common mistake here.** Evaluation is a *system-level* practice: does this system perform acceptably, measured across many cases, before deployment and continuously after. Verification is *instance-level*: is **this** output, the one in front of me right now, correct. A system with excellent evaluation scores still produces individual outputs that are wrong, and the evaluation cannot tell you which. They are complements, and neither substitutes for the other.

Three findings define why this is harder in practice than it sounds:

- **A citation is not verification — it is where verification starts.** Human evaluation of generative search engines found only **51.5% of generated sentences fully supported by their citations**, and only **74.5% of citations actually supporting the statement they were attached to**. Grounding a system in sources improves it; it does not discharge the reader's obligation to open them.
- **Assistance can lower quality and raise confidence at the same time.** In a controlled study, participants with an AI coding assistant wrote *significantly less secure* code than those without — **and were more likely to believe their code was secure.** Output got worse; confidence in it got better. That inversion is the specific reason verification cannot be left to felt need.
- **Verification is an economic decision, and the economics run the wrong way.** People weigh the cost of checking against the cost of relying, and **checking drops as task difficulty rises** — so the hardest problems, where a system is least reliable, are the ones people verify least. Explanations help only when they genuinely reduce the cost of checking; complex ones that add cognitive load do not.

That last finding is the entry's central claim. **Verification fails hardest exactly where it matters most**, and it fails for structural reasons rather than for want of diligence — which means the remedy is design, not exhortation.

---

## Plain-language version

An AI system produces answers that sound right. Sounding right is what it is built to do. Whether it *is* right is a separate question, and nothing in the output distinguishes the two cases.

Verification is the step where you find out: run the code instead of reading it, open the link instead of trusting the citation, check the figure against the actual record. It is unglamorous and it takes time, which is exactly why it gets skipped — and it gets skipped most on hard problems, where you are most tired, least sure, and least able to spot the error. That is not a personal failing. It is what the research finds people do, predictably, and it is the reason verification has to be built into how work happens rather than left to whoever remembers.

---

## AI literacy notes

1. **Plausible and correct are produced by the same process.** Fluency is not a signal of accuracy — the model generates confident phrasing and correct content through the same mechanism, so tone carries no information about truth. See [Confidence vs Accuracy](confidence-vs-accuracy.md).
2. **"It gave me a source" is not verification.** Roughly a quarter of citations do not support the sentence they are attached to, and around half of generated sentences are not fully supported. The citation tells you where to look, not what you will find.
3. **You will verify least when it matters most.** Difficulty raises the cost of checking, so verification quietly collapses on hard problems. Knowing this about yourself is more useful than resolving to try harder.
4. **Confidence in your own work can rise while its quality falls.** The coding study found both at once. Your sense that you have checked enough is not evidence that you have.
5. **Verification is domain work, not AI work.** Nothing about understanding language models tells you whether a contract clause is enforceable or a dosage is safe. The check requires the expertise the output is about — which is why the person best placed to verify is often not the person who prompted.
6. **Some outputs cannot be verified at the cost you have available.** That is a legitimate finding, not a failure. The correct response is to change what the output is used for, not to verify it badly and call it done.
7. **Skepticism measurably works.** In the same coding study, participants who distrusted the tool and reworked their prompts produced fewer vulnerabilities. Treating output as a draft to be interrogated is not just good manners — it changes the result.

---

## Governance notes

**Core question:** For each way this system's output is used, who verifies it, against what, and what happens when they do not have time?

**Watch for:**
- Verification assumed rather than assigned — "someone would catch it" naming no one
- Verification assigned to whoever prompted, who is often the person least equipped to check and most invested in the answer being right
- No budgeted time for it, which means it is being decided by workload rather than by policy
- Reliance on the presence of citations or a reasoning trace as evidence that checking occurred
- Volume scaled up without scaling the checking capacity — the fastest way to convert an assistive tool into an unreviewed pipeline
- Interfaces that make accepting output one click and verifying it ten

**Practice:**
- Define the verification method per use, not per system: what counts as ground truth here, and what is the cheapest reliable check against it
- **Reduce the cost of checking rather than demanding more of it** — surface the source next to the claim, link to the record, show the diff, make the test runnable. This is the intervention with evidence behind it
- Assign verification to someone with the domain knowledge to perform it, and record that the assignment exists
- Where verification is genuinely infeasible, constrain the use case instead: advisory rather than decisional, draft rather than final ([permission model](permission-model-ai.md))
- Log what was verified and by whom, so the [audit trail](audit-trail-ai.md) reflects the check and not only the output
- Sample and re-check accepted output periodically — the failure mode is silent drift in how much checking actually happens

**Key accountability owner:** the person who acts on the output. Verification is the operational form of [human responsibility](human-responsibility-in-ai-use.md), which does not transfer to the system — but the *organization* owns making it affordable, and an unaffordable check is an unperformed one.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** Unusually well supported for a practice entry: the citation-support rates, the security-and-confidence inversion, and the cost-benefit account of when people check are each peer-reviewed empirical findings rather than recommendations. Two limits worth stating. The specific percentages come from 2023-era systems and specific tasks — the direction is what transfers, not the magnitudes. And there is no established method for verifying open-ended generative output at scale; the practices above lower exposure and do not close it.

---

## Related concepts

- [Evaluation (AI Systems)](evaluation.md) — the system-level counterpart; measures the system, cannot tell you which individual output is wrong
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — verification is what that responsibility looks like in practice
- [Automation Bias](automation-bias.md) — the mechanism by which verification quietly stops happening
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — why the output gives you no signal about whether it needs checking
- [Hallucination](hallucination.md) — the failure verification is most often expected to catch
- [Concealing Uncertainty](concealing-uncertainty.md) — removes the cue that would have prompted a check
- [Grounding](grounding.md) — makes verification cheaper by showing the source; does not perform it
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the design pattern that places a verifier where one is needed
- [Audit Trail (AI)](audit-trail-ai.md) — the record of whether checking actually happened
- [Explainability (XAI)](explainability-xai.md) — explanations reduce overreliance only when they lower the cost of checking
- [Cognitive Offloading & Deskilling](cognitive-offloading-deskilling.md) — the long-run cost when verification stops being practiced

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-189 | Liu, N.F.; Zhang, T.; Liang, P. — *Evaluating Verifiability in Generative Search Engines* (Findings of EMNLP, 2023) · [link](https://arxiv.org/abs/2304.09848) | That citations frequently fail to support their claims — 51.5% of sentences fully supported, 74.5% of citations supporting their statement. The basis for "a citation is where verification starts." |
| SRC-191 | Vasconcelos, H.; Jörke, M.; Grunde-McLaughlin, M.; Gerstenberg, T.; Bernstein, M.; Krishna, R. — *Explanations Can Reduce Overreliance on AI Systems During Decision-Making* (CSCW, 2023) · [link](https://arxiv.org/abs/2212.06823) | The cost-benefit account: verification drops as difficulty rises, and explanations help only when they lower the cost of checking. The entry's central claim and its main practice recommendation. |
| SRC-190 | Perry, N.; Srivastava, M.; Kumar, D.; Boneh, D. — *Do Users Write More Insecure Code with AI Assistants?* (ACM CCS, 2023) · [link](https://arxiv.org/abs/2211.03622) | Worse output and higher confidence in it, measured together — plus the finding that skepticism and prompt reworking reduced vulnerabilities. |
| SRC-174 | Goddard, K.; Roudsari, A.; Wyatt, J.C. — *Automation bias: a systematic review of frequency, effect mediators, and mitigators* (JAMIA, 2012) · [link](https://doi.org/10.1136/amiajnl-2011-000089) | The prior literature on why checking stops when a system is usually right, established long before language models. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places instance-level checking inside a lifecycle that requires evidence rather than assurance. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Run it, don't read it. Assume the citation is unchecked until you open it, and design the workflow so checking is the cheap path rather than the diligent one. |
| **Organizational** | Verification that is assumed rather than assigned and budgeted is not happening. Lowering its cost is a more effective control than requiring more of it. |
| **Client-facing** | Explains why AI-assisted work still carries a review step, and why that step is a feature of the process rather than a lack of confidence in the tool. |
| **LLM-native** | Evaluation is system-level and verification is instance-level; strong benchmarks tell you nothing about the output in front of you. |

---

*Last updated: v1.0 · August 2026*
