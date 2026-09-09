<!--meta
category: Reliability & Quality
short: A model refusing work that was perfectly safe — the failure safety measures cause rather than prevent, and the one almost nobody puts a number on
aliases: [over-refusal, false refusal, exaggerated safety, over-conservatism, overcautious refusal, refusing safe requests, false positive refusal, safety tax]
tags: [Evaluation, Safety, Model Behavior]
established: emerging
-->
# Overrefusal

> **Term status — Emerging.** The phenomenon is well documented and benchmarked in peer-reviewed work, but the naming has not settled — *overrefusal*, *over-refusal*, *false refusal* and *exaggerated safety* all circulate for the same behavior, and the benchmark that defined it uses a different phrase again. Filed `emerging` on the naming, not on the evidence.

## One-line essence
A model declining a request that was entirely safe — the cost side of safety training, produced by the same mechanism that produces the benefit, and systematically less measured than the harms it trades against.

---

## Technical definition

Overrefusal is the refusal of a request that a well-calibrated system should have fulfilled. It is a **false positive in a safety classifier**, whether that classifier is a separate [guardrail](guardrails-ai-systems.md) or behavior trained into the model itself.

**It is not a bug in safety training; it is the other half of it.** Röttger et al. state the tension precisely: harmlessness requires refusing unsafe prompts, and refusing is not being helpful — so any system tuned toward one moves along an axis away from the other. **A refusal threshold is a threshold, and every threshold has two error rates** ([false positives and false negatives](false-positives-and-false-negatives.md)).

**The trigger is usually surface form rather than substance.** Their XSTest suite is built on exactly this: **250 safe prompts across ten prompt types** that a calibrated model should not refuse, paired with **200 unsafe contrast prompts** that it should. The safe prompts are constructed to *look* like unsafe ones — homonyms, figurative language, safe targets, sensitive topics discussed legitimately. Models fail these systematically, which tells you the refusal is keyed on vocabulary and framing rather than on what is being asked ([tokenization](tokenization.md) is the wrong level; the point is that pattern resemblance is doing the work).

**The asymmetry in how the two errors are measured is the governance content.** A harmful completion is a visible, reportable, sometimes newsworthy event. **A wrongful refusal produces no artifact at all**: the user rephrases, gives up, or goes elsewhere, and nothing is logged as a failure ([observability](observability.md)). So safety reporting routinely gives a harm rate with no accompanying refusal rate, which is half a measurement presented as a whole one.

**The costs land unevenly, and that is what makes it more than an annoyance.** Refusals concentrate on legitimate work in medicine, law, security research, harm reduction, abuse support and history — domains where the vocabulary of the harm is also the vocabulary of the help. **The people most affected are those doing the work that most resembles the thing being prevented**, and a model that will not discuss overdose thresholds is failing a clinician and a harm-reduction worker before it fails anyone else.

**Two second-order effects worth naming.** Overrefusal teaches users to route around the control — rephrasing until it passes is a skill, and one that also defeats the control when the request really was unsafe ([jailbreak](jailbreak.md)). And a system that refuses unpredictably erodes the trust that makes the refusals people *should* heed credible ([human–AI collaboration](human-ai-collaboration-model.md)).

---

## Plain-language version

Everyone has met this: you ask an AI something completely ordinary and it declines, apologetically, as though you had asked for something terrible. That is overrefusal, and it is not a glitch. **It is the predictable cost of the thing that stops the model answering genuinely dangerous questions.**

Think of it as a filter with a dial. Turn it toward caution and fewer harmful answers get through — along with more harmless ones. Turn it the other way and more legitimate requests succeed, and so do more bad ones. There is no setting that only catches the bad. Any threshold has two ways to be wrong, and moving it trades one for the other.

**What actually triggers a wrongful refusal is usually how a request looks rather than what it asks.** Researchers built a test set for this: hundreds of clearly safe questions deliberately worded to resemble unsafe ones — words with two meanings, figures of speech, difficult topics discussed for perfectly good reasons. Models refuse these at rates that show the decision is being made on vocabulary, not on meaning.

**Here is the part that matters for anyone governing one of these systems.** When a model produces something harmful, that is visible. Someone screenshots it; it may make the news; it gets logged and counted. When a model wrongly refuses, **nothing happens at all**. The person shrugs, rewords it, or goes somewhere else. There is no incident, no ticket, no number.

So the two errors are not equally visible, which means they do not get equally managed. Safety reports quote harm rates. They very rarely quote refusal rates. **A safety claim with only one of those numbers is telling you about one side of a trade.**

And the burden is not spread evenly. The people who get refused are disproportionately the ones whose legitimate work sounds like the dangerous thing: doctors, lawyers, security researchers, people working in addiction or abuse support, historians. **A model that will not talk about poisons is obstructing a toxicologist long before it obstructs anyone dangerous** — who has other options anyway.

---

## AI literacy notes

1. **Overrefusal is the false-positive half of a safety threshold**, not a defect in it.
2. **Helpfulness and harmlessness are in tension by construction** — moving one moves the other.
3. **Refusals key on surface form**: vocabulary, framing and topic, rather than intent.
4. **A wrongful refusal leaves no artifact**, which is why it is under-measured.
5. **Harm rates are reported; refusal rates usually are not.**
6. **Costs concentrate in medicine, law, security, harm reduction and history.**
7. **It teaches users to rephrase around controls** — a skill that also defeats real ones.
8. **Unpredictable refusal erodes the credibility** of refusals that matter.
9. **The naming is unsettled**; the phenomenon is benchmarked and reproducible.

---

## Governance notes

**Core question:** What is this system's wrongful-refusal rate, on our own work — and if nobody knows, how is the safety configuration being justified?

**Watch for:**
- A safety evaluation reporting a harm rate with no refusal rate beside it ([evaluation](evaluation.md))
- Refusal treated as always-safe, so tightening is a decision nobody has to defend
- No route for a user to report a wrongful refusal, so the error rate is structurally unobservable ([observability](observability.md))
- Guardrail thresholds set once at launch and never revisited against realized costs ([guardrails](guardrails-ai-systems.md))
- Deployment into a domain whose legitimate vocabulary overlaps the blocked vocabulary, with no domain-specific testing
- Users trained to rephrase around refusals, and that treated as a workaround rather than a control failure
- Vendor safety claims accepted without asking what they cost in false refusals ([supply chain risk](supply-chain-risk-ai.md))
- The same refusal policy applied to a specialist internal tool and a public consumer product ([permission model](permission-model-ai.md))

**Practice:**
- **Measure both error rates and publish them together.** A refusal rate without a harm rate is as incomplete as the reverse
- **Build a domain-specific safe-prompt set from your own real, legitimate requests** — the published suites establish the method; your users' vocabulary is what you actually need to test
- **Give users a one-click way to flag a wrongful refusal**, and treat that stream as a measurement rather than as complaints
- Set thresholds per context rather than globally: a clinical tool and a public chatbot should not share a refusal policy ([AI use case](ai-use-case.md))
- **Re-measure after every model or guardrail change** — this moves silently with updates ([model version and update](model-version-update.md))
- Prefer a scoped, explained refusal over a blanket one; a model that says what it will not do and why leaves the user somewhere to go
- **Record who bears the cost.** If refusals fall mainly on one professional group or one language, that is a fairness finding, not a tuning detail ([bias](bias-ai-systems.md))
- Treat a rise in user rephrasing as a signal about the threshold, not as user sophistication

**Key accountability owner:** whoever sets the refusal threshold — because it is a single decision that allocates error between two populations, one of which files incident reports and one of which silently gives up, and only an explicit owner will weigh the side that does not complain.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the phenomenon, moderate on its size anywhere in particular.** The tension is structural rather than empirical — it follows from what a threshold is — and the behavior is systematically benchmarked in peer-reviewed work with a published test suite. **What this entry deliberately does not give is a rate.** Published refusal rates are specific to a model version, a prompt set and a moment, and they move with every safety update, so quoting one would be misleading within months; the entry gives the method for measuring your own instead. **The distributional claim — that costs concentrate in domains whose legitimate vocabulary resembles the blocked vocabulary — follows from the mechanism** (refusals keyed on surface form) and from the construction of the benchmark, and is stated as a structural expectation rather than as a measured disparity.

---

## Related concepts

- [False Positives and False Negatives](false-positives-and-false-negatives.md) — the error-rate frame this is an instance of
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — where the threshold usually lives
- [Alignment (AI Systems)](alignment-ai-systems.md) — the helpfulness/harmlessness tension at its source
- [RLHF](rlhf.md) — the training process that produces both sides of it
- [Jailbreak](jailbreak.md) — what rephrasing-to-pass becomes when the request is unsafe
- [Dual Use](dual-use.md) — why refusal is a retail control rather than a complete one
- [Evaluation (AI Systems)](evaluation.md) — where only half the trade usually gets measured
- [Observability](observability.md) — the missing signal for an error that leaves no artifact
- [Bias (AI Systems)](bias-ai-systems.md) — when the cost lands unevenly by domain or language
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — trust as the thing unpredictable refusal spends
- [Sycophancy (LLMs)](sycophancy-llms.md) — the opposite miscalibration, agreeing when it should not

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-345 | Röttger, Paul; Kirk, Hannah Rose; Vidgen, Bertie; Attanasio, Giuseppe; Bianchi, Federico; Hovy, Dirk — *XSTest: A Test Suite for Identifying Exaggerated Safety Behaviours in Large Language Models* (NAACL, 2024) · [link](https://arxiv.org/abs/2308.01263) | The benchmark and the framing: **250 safe prompts across ten prompt types** that a well-calibrated model should not refuse, against **200 unsafe contrast prompts** that it should — plus the stated tension that harmlessness requires refusal and refusal is not helpfulness. The safe prompts are built to resemble unsafe ones, which is what shows the decision is keyed on surface form. ⚠️ Model-version specific; the method transfers, the rates do not. |
| SRC-135 | Rebedea, T.; Dinu, R.; Sreedhar, M.; Parisien, C.; Cohen, J. (NVIDIA) — *NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails* (EMNLP, 2023) · [link](https://arxiv.org/abs/2310.10501) | Establishes the guardrail as a user-defined, model-independent layer — which is where a refusal threshold is set explicitly and can therefore be tuned, measured and owned rather than inherited from training. ⚠️ Vendor-authored. |
| SRC-196 | Ouyang, L.; Wu, J.; Jiang, X. et al. (OpenAI) — *Training language models to follow instructions with human feedback* (NeurIPS, 2022) · [link](https://arxiv.org/abs/2203.02155) | The training process that installs the behavior: preference data from a labeler pool following guidelines, which is where the helpfulness/harmlessness balance is actually decided — by people, in a document, before any threshold is set. |
| SRC-001 | NIST — *AI Risk Management Framework* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The framework position that a trustworthy system balances validity and reliability against safety rather than maximizing either — the risk-management basis for treating a refusal rate as a managed quantity rather than a free good. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Build a safe-prompt set from your own users' real requests, measure both error rates, and re-measure after every model or guardrail change. |
| **Organizational** | A safety report with a harm rate and no refusal rate describes one side of a trade. Refusal is not free, and its cost is invisible by default. |
| **Client-facing** | Explains why the system sometimes declines something obviously fine, and why that is a tuning decision someone made rather than a malfunction. |
| **LLM-native** | Refusals key on surface form, not intent — which is why rephrasing works, and why the same skill defeats the control when the request really was unsafe. |

---

*Last updated: v1.0 · September 2026*
