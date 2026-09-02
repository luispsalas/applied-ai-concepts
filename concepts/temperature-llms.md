<!--meta
category: Foundations
short: The sampling knob that tunes how varied a model's output is — widely believed to be an accuracy control, and measurably not one
aliases: [temperature setting, temp, sampling temperature, creativity slider, top-p, nucleus sampling, why is my output different each time, set temperature to zero]
tags: [Model Behavior, AI Literacy]
established: established
-->
# Temperature (LLMs)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The sampling parameter that controls how much variety a model allows itself when choosing each next token — a trade-off between consistency and range, and, on the evidence, not the accuracy dial most people take it for.

---

## Technical definition

At every step, a language model produces a probability distribution over its whole vocabulary. **Temperature rescales that distribution before a token is drawn from it.** Low temperature sharpens it — probability mass concentrates on the already-likely candidates. High temperature flattens it, giving unlikely tokens a real chance. At temperature 0 the sampler degenerates to always taking the single most probable token.

It is one of several sampling controls, not the only one. **Top-p (nucleus) sampling** truncates the distribution to the smallest set of tokens whose cumulative probability exceeds *p*; **top-k** keeps the *k* most probable. These are independent knobs and are frequently confused with temperature in practice.

**Maximizing likelihood is not the goal, and this is the non-obvious part.** Holtzman et al. (ICLR 2020) established that decoding strategies which maximize probability — beam search and greedy decoding — produce text that is *"generic, repetitive, and awkward,"* degenerating into loops. Human text is not the most probable text. Some sampling variety is what makes output read as language rather than as a stuck record, which is why nucleus sampling was introduced.

**The finding that contradicts standard practice.** The widespread belief is that lowering temperature makes a model more accurate. Renze & Guven (Findings of EMNLP 2024) tested it directly and report that *"changes in temperature from 0.0 to 1.0 do not have a statistically significant impact on LLM performance for problem-solving tasks."* The result held across nine models, five prompt-engineering approaches, and multiple problem domains, over a tested range of 0.0 to 1.6.

Read precisely, this says the knob is doing something other than what it is usually turned for. **Across the band people actually deploy in, temperature changes the variability of the answer, not its correctness.** Lowering it to chase accuracy buys consistency — the same answer more often — which is easy to mistake for the same answer more often being *right*.

**Temperature 0 is not determinism, and treating it as such is the most consequential error here.** It removes sampling randomness; it does not make inference reproducible. Floating-point non-associativity, batch composition and kernel selection mean identical inputs can still produce different outputs — a problem that is *"achievable but engineered,"* not a default. See [Determinism vs Probabilism](determinism-vs-probabilism.md).

---

## Plain-language version

Every time a model writes a word, it has a ranked list of candidates with scores. Temperature decides how strictly it sticks to the top of that list. Turn it down and the model plays it safe. Turn it up and it takes more chances.

You might assume playing it safe means being more correct. Researchers checked this across nine different models and a range of tasks, and found that between the low and middle settings people normally use, **accuracy did not meaningfully change.** What changed was how much the answer varied between runs.

That is a real distinction. Turning temperature down gets you the same answer more often. It does not get you a better one. Consistency and correctness feel like the same thing and are not — a model can be reliably wrong.

There is also a reason not to turn it all the way down by default: text produced by always picking the most likely word comes out flat and repetitive, sometimes looping. A little variety is what makes output read like writing.

And the most common misunderstanding: setting temperature to zero does **not** guarantee identical output every time. It removes one source of randomness. Others live deeper in how the computation runs on the hardware, and getting genuine repeatability takes deliberate engineering.

---

## AI literacy notes

1. **Temperature is a variability control, not a correctness control.** The measured effect on problem-solving accuracy between 0.0 and 1.0 was not statistically significant.
2. **Consistency is not accuracy.** Lower temperature narrows the spread of answers around whatever the model tends to produce — including when that is wrong.
3. **Temperature 0 ≠ reproducible.** It removes sampling randomness only; bitwise reproducibility is an engineering achievement, not a setting.
4. **Maximum likelihood is not the target.** Always taking the top token produces degenerate, repetitive text — the finding that motivated nucleus sampling.
5. **Temperature, top-p and top-k are different knobs** that are routinely conflated. Changing two at once makes any result uninterpretable.
6. **Raising temperature does not add creativity.** It widens the sampling distribution. What surfaces from the tail may be novel or may be wrong; the parameter does not distinguish.
7. **Defaults vary by provider and change between versions**, so "temperature 0.7" is not a portable specification.
8. **Tuning temperature is often the wrong lever.** When output quality is the problem, prompt, context and grounding usually have far more leverage.

---

## Governance notes

**Core question:** What is each temperature setting in this system actually buying us — and if the answer given is "accuracy," what evidence supports that rather than consistency?

**Watch for:**
- Temperature 0 documented as making the system deterministic, reproducible, or auditable — the claim does not hold ([determinism vs probabilism](determinism-vs-probabilism.md))
- Low temperature cited as a risk control in a governance artifact, with no evaluation demonstrating an accuracy effect
- Reduced answer variance read as improved quality, when it is a narrower spread around the same tendency
- Temperature tuned as a response to hallucination — it is not a [hallucination](hallucination.md) control ([grounding](grounding.md) is the relevant lever)
- Settings undocumented or drifting between environments, so a production result cannot be reproduced from a test one
- Temperature changed at the same time as prompt or model, making the [evaluation](evaluation.md) uninterpretable
- Provider defaults assumed stable across [model versions](model-version-update.md)

**Practice:**
- Record temperature and every other sampling parameter alongside model version in the [audit trail](audit-trail-ai.md) — it is part of what produced the output
- **Set it from the variability requirement, not from an accuracy hope**: low where the same input should give a stable answer, higher where range is genuinely wanted
- Where reproducibility is a real requirement (audit, regression testing, regulatory evidence), engineer and **verify** it rather than assuming temperature 0 delivers it
- Change one sampling parameter at a time when evaluating, and evaluate on accuracy, not on how consistent the output looks
- Do not present a sampling setting as a safety or accuracy control unless your own evaluation shows it functioning as one
- Pin settings per environment and treat a change as a change to the system

**Key accountability owner:** whoever signs off the system's evaluation evidence — because the failure mode is a setting entering a control narrative on folklore rather than on measurement.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The mechanism is elementary and uncontested, and both key findings are peer-reviewed (ICLR 2020; Findings of EMNLP 2024). The accuracy result is a **null finding**, which carries its own caveats: it is evidence of no *detected* effect on the tasks, models and range studied, not proof that temperature never matters anywhere. The study covered nine models and multiple domains, which is unusually broad, but problem-solving tasks are not all tasks — creative, summarization and long-form generation work were not the target. **The strong, well-supported claim is the negative one: there is no basis for treating temperature as an accuracy control by default.**

---

## Related concepts

- [Determinism vs Probabilism](determinism-vs-probabilism.md) — the trade-off this parameter tunes, and why temperature 0 is not determinism
- [Large Language Models (LLMs)](large-language-models.md) — the next-token distribution temperature rescales
- [Tokenization](tokenization.md) — the units the distribution is over
- [Hallucination](hallucination.md) — not fixed by lowering temperature; a common and costly misattribution
- [Evaluation (AI Systems)](evaluation.md) — the only way to know what a setting is buying
- [Audit Trail (AI Systems)](audit-trail-ai.md) — sampling parameters belong in the record of what produced an output
- [Model Version & Update](model-version-update.md) — defaults and behavior shift between versions
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — consistency and correctness are separate properties, here as elsewhere
- [Grounding](grounding.md) — the lever that does address factual reliability
- [Prompt Engineering](prompt-engineering.md) — usually far more leverage than sampling settings

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-223 | Renze, M.; Guven, E. — *The Effect of Sampling Temperature on Problem Solving in Large Language Models* (Findings of the ACL: EMNLP 2024, pp. 7346–7356) · [link](https://arxiv.org/abs/2402.05201) | The central finding: temperature changes from 0.0 to 1.0 show no statistically significant impact on problem-solving performance, across nine LLMs, five prompt-engineering approaches and multiple domains (range tested 0.0–1.6). |
| SRC-144 | Holtzman, A.; Buys, J.; Du, L.; Forbes, M.; Choi, Y. — *The Curious Case of Neural Text Degeneration* (ICLR, 2020) · [link](https://arxiv.org/abs/1904.09751) | Why maximizing likelihood is not the goal: greedy and beam decoding produce generic, repetitive, degenerate text. Introduces nucleus (top-p) sampling as the alternative truncation strategy. |
| SRC-145 | He, Horace (Thinking Machines Lab) — *Defeating Nondeterminism in LLM Inference* (2025) · [link](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/) | Temperature 0 does not deliver reproducibility: batch and kernel effects break bitwise determinism, which is achievable only by deliberate engineering. ⚠️ Vendor-authored, not peer-reviewed. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Places temperature among the standard decoding controls (alongside top-p and top-k) and confirms the prevailing conventions across model families. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Set it from the variability requirement, log it with the model version, and change one sampling parameter at a time when evaluating. Reproducibility must be engineered and verified, not assumed from temperature 0. |
| **Organizational** | A temperature setting is not a risk control unless your own evaluation shows it functioning as one. "We set it to zero" is a statement about variance, not about accuracy or auditability. |
| **Client-facing** | Explains why the same question can produce differently-worded answers, and why turning that variation down does not make the answers more correct. |
| **LLM-native** | The parameter most often misattributed. It tunes the spread of the next-token distribution — consistency — and the measured effect on problem-solving accuracy across the usual deployment band is not significant. |

---

*Last updated: v1.0 · September 2026*
