<!--meta
category: Organizational Readiness
short: The number you commit to before anyone is angry — and the question of what it can even mean when the output is probabilistic rather than up-or-down
aliases: [SLO, SLI, SLA, service level agreement, service level indicator, service level, error budget, uptime commitment, what can we promise]
tags: [Architecture, Evaluation, Data Governance]
established: established
-->
# Service Level Objective

> **Term status — Established.** A standard term of art in site reliability engineering, defined in the canonical SRE literature and in independent use across the industry.

## One-line essence
A target value for a measured aspect of service quality — and, for AI systems, the awkward question of what to promise when correctness is probabilistic rather than binary.

---

## Technical definition

Three terms, routinely conflated, defined here from the canonical source:

- An **SLI** is a *service level indicator* — *"a carefully defined quantitative measure of some aspect of the level of service that is provided."* Latency and error rate are the common ones.
- An **SLO** is a *service level objective* — *"a target value or range of values for a service level that is measured by an SLI,"* structured as `SLI ≤ target` or `lower ≤ SLI ≤ upper`.
- An **SLA** is a *service level agreement* — *"an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain."*

**The distinction that matters: an SLO is internal and has no consequences attached; an SLA has consequences.** The SRE literature's own test is to ask what happens if the target is missed. If nothing contractual follows, it is an objective, not an agreement.

**All of this transfers cleanly to AI systems for the operational dimensions** — availability, latency, throughput, error rate. [Latency](latency-ai-systems.md) in particular has a well-formed SLI, and the percentile discipline applies unchanged.

**Where it stops transferring is quality, and that is the whole AI-specific problem.** A conventional SLI measures something with a definite value: the request succeeded or it did not, in 200ms or 900ms. **Model output correctness has no equivalent ground truth at serving time.** You cannot compute "was that answer right" as a live signal the way you compute a status code, so the SLI that everybody actually cares about is the one that cannot be instrumented directly.

**What is available instead are proxies, and each is a different thing from correctness**: agreement with a reference set on a fixed evaluation ([evaluation](evaluation.md)), an [LLM-as-judge](llm-as-judge.md) score with its own biases, human review of a sample, or downstream signals like escalation, correction and abandonment rates. **A quality SLO in practice is a commitment about one of these proxies**, and the honest version says which.

**Two structural cautions follow.** A percentage-correct target is **only meaningful against a fixed distribution of requests** — the number moves when traffic changes, with no change to the system ([model/data drift](model-data-drift.md)). And **an objective set on what is easy to measure will be optimized for**, which reintroduces the false-positive/false-negative trade under a different name: a system tuned to hit a quality SLO measured by refusals will refuse more ([false positives and false negatives](false-positives-and-false-negatives.md)).

---

## Plain-language version

Three abbreviations, constantly muddled, and the difference is simple.

An **SLI** is a measurement — how long did it take, how often did it fail. An **SLO** is the target you set for that measurement. An **SLA** is a promise to someone else with consequences if you break it. The quickest test: *what happens if we miss it?* If the answer is "we have a problem internally", it's an objective. If money or a contract moves, it's an agreement.

For the operational parts of an AI system, all of this works exactly as it always has. You can commit to availability and response times, and you should.

**The trouble starts with quality.** In ordinary software, a request either worked or it didn't — the system knows, and can count. With a model, there is no equivalent: **the system cannot tell you at the time whether the answer was any good.** So the thing everyone most wants a commitment about is the one thing that cannot be measured live.

What you can do instead is measure something *related*: how it scored on a fixed test set, what a second model thinks of the output, what human reviewers say about a sample, or what users do afterwards — do they escalate, correct it, give up. All of these are useful. **None of them is "correct".** So a quality target is really a promise about a stand-in, and the honest way to write one says which stand-in it is.

Two traps worth knowing:

**A "95% correct" target only means something for one particular mix of questions.** Change what people ask and the number moves, with nothing about the system having changed.

**Whatever you set a target on will get optimized.** If your quality measure counts bad answers, and refusing counts as not-bad, you will get more refusals. The target starts steering the system, which is fine when you chose it deliberately and a problem when you did not.

---

## AI literacy notes

1. **SLI measures, SLO targets, SLA obligates** — the test is what happens when you miss.
2. **Operational SLOs transfer to AI unchanged** — availability, latency, throughput, error rate.
3. **Output correctness has no live ground truth**, so the quality SLI cannot be instrumented directly.
4. **Every quality proxy is a different thing from correctness** — say which one the target is about.
5. **A percentage target assumes a fixed request distribution** and moves when traffic changes.
6. **An objective becomes an optimization target**, with the side effects that implies.
7. **A quality SLA is a much stronger claim than a quality SLO** — attach consequences deliberately.
8. **Latency is the AI dimension with a clean SLI**, and percentiles are the honest unit there.

---

## Governance notes

**Core question:** For every number we have committed to about this system's quality, what is actually being measured — and would we notice it drifting before a customer did?

**Watch for:**
- A quality commitment with no named proxy behind it, so nobody can say what would falsify it
- Percentage-correct targets quoted without the request distribution they were measured on ([evaluation](evaluation.md))
- An SLO promoted into a customer contract without anyone re-examining whether the proxy supports it
- LLM-as-judge scores treated as ground truth rather than as a second model's opinion ([LLM-as-judge](llm-as-judge.md))
- Only operational SLIs monitored, so quality degrades silently while dashboards stay green ([observability](observability.md))
- Targets set where measurement is easy rather than where harm is, then optimized toward ([false positives and false negatives](false-positives-and-false-negatives.md))
- No error budget or defined response when the objective is missed — a target with no consequence changes nothing
- Objectives never revisited after a model version change ([model version and update](model-version-update.md))

**Practice:**
- **Name the proxy in the objective itself** — "95% agreement with the reference set on the Q3 evaluation suite" rather than "95% accurate"
- Keep operational and quality objectives separate; they have different evidence and different failure modes
- **Record the request distribution a quality target was set against**, and re-measure when traffic shifts ([model/data drift](model-data-drift.md))
- Define what happens when the objective is missed, before agreeing it — an objective with no response is decoration
- Sample human review continuously rather than only at evaluation time, so the proxy itself stays validated
- **Ask what a target will incentivize before setting it**, and check for the induced behavior afterwards
- Re-baseline every objective on a model version change; the provider's change is your regression ([model version and update](model-version-update.md))
- Be more conservative in an SLA than in an SLO, deliberately — consequences convert a measurement problem into a liability

**Key accountability owner:** whoever signs the customer-facing commitment — because the gap between a quality *objective* measured on a proxy and a quality *agreement* enforced by contract is where an unmeasurable property quietly becomes an obligation.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the framework, medium on its application to output quality.** The SLI/SLO/SLA definitions are quoted from the canonical SRE source and are stable, uncontroversial, and unchanged by AI. The operational transfer is straightforward. **What this entry states with less confidence — deliberately — is what a quality SLO should look like for a generative system**, because there is no settled industry answer: the proxies listed here are in real use, none is authoritative, and practice is still forming. The claim made most strongly is negative and follows from how these systems work: **output correctness has no live ground truth**, so any quality objective is necessarily a commitment about a stand-in. Where a specific proxy is adequate is a judgment this entry does not attempt to make for the reader.

---

## Related concepts

- [Latency (AI Systems)](latency-ai-systems.md) — the AI dimension with a clean, well-understood SLI
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the organization can actually run to a commitment
- [Evaluation (AI Systems)](evaluation.md) — where quality proxies come from
- [LLM-as-Judge](llm-as-judge.md) — a common proxy, and its biases
- [Observability (AI Systems)](observability.md) — the signals that make an objective monitorable
- [Model/Data Drift](model-data-drift.md) — why a percentage target moves without any change to the system
- [False Positives and False Negatives](false-positives-and-false-negatives.md) — what a quality target quietly optimizes
- [Model Version & Update](model-version-update.md) — the provider's change that becomes your missed objective
- [Scalability (AI Systems)](scalability-ai-systems.md) — the load conditions an objective must hold under
- [Continuous Feedback & Improvement](continuous-feedback-improvement.md) — the loop that keeps a proxy honest

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-304 | Beyer, Betsy; Jones, Chris; Petoff, Jennifer; Murphy, Niall Richard (eds.), Google — *Site Reliability Engineering*, Chapter 4: Service Level Objectives (O'Reilly, 2016) · [link](https://sre.google/sre-book/service-level-objectives/) | The three definitions, quoted verbatim from the freely published text: an SLI is *"a carefully defined quantitative measure of some aspect of the level of service that is provided"*; an SLO is *"a target value or range of values for a service level that is measured by an SLI"*; SLAs are *"an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain."* Also the practical test used here — ask what happens if the target is missed. ⚠️ Predates generative AI entirely; it supplies the framework, and nothing in it addresses probabilistic output quality. |
| SRC-247 | Kwon, W.; Li, Z.; Zhuang, S.; Sheng, Y.; Zheng, L.; Yu, C.H.; Gonzalez, J.E.; Zhang, H.; Stoica, I. (UC Berkeley et al.) — *Efficient Memory Management for Large Language Model Serving with PagedAttention* (SOSP, 2023) · [link](https://arxiv.org/abs/2309.06180) | Evidence that the operational dimensions — throughput, latency under load — are engineering variables an organization can actually target and improve, which is what makes operational SLOs meaningful for AI serving. |
| SRC-280 | Dean, Jeffrey; Barroso, Luiz André (Google) — *The Tail at Scale* (Communications of the ACM 56(2), pp. 74–80, February 2013) · [link](https://doi.org/10.1145/2408776.2408794) | Why an SLI must be expressed in percentiles rather than averages — in a fan-out system the slowest component determines the response, so a mean conceals exactly the behavior an objective is meant to bound. |
| SRC-047 | Wei, Jason et al. (Google Research, Brain Team) — *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* (2023) · [link](https://arxiv.org/abs/2201.11903) | Illustrates that output quality varies with prompting technique rather than being a fixed property of the deployed system — part of why a quality target must name the conditions it was measured under. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Name the proxy inside the objective. Keep operational and quality targets separate — different evidence, different failure modes. |
| **Organizational** | The move from objective to contractual agreement is where an unmeasurable property becomes a liability. Be deliberately more conservative there. |
| **Client-facing** | Lets you commit to what can genuinely be measured, and explain honestly why output quality is expressed differently from uptime. |
| **LLM-native** | There is no live ground truth for correctness, so every quality SLO is a promise about a stand-in — and whatever you target will get optimized. |

---

*Last updated: v1.0 · September 2026*
