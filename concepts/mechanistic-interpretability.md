<!--meta
category: Foundations
short: Reverse-engineering what a model actually computes, rather than asking it to explain itself — the only route to knowing why that does not depend on the model's own account
aliases: [mech interp, circuits, features and circuits, superposition, sparse autoencoders, dictionary learning, what is going on inside the model, opening the black box]
tags: [Model Behavior, Safety, Evaluation]
established: established
-->
# Mechanistic Interpretability

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The effort to reverse-engineer what's actually happening inside a model — identifying which internal components produce which behaviors, not just what the model outputs.

---

## Technical definition

Mechanistic interpretability tries to recover the *algorithm* a trained network implements, expressed in terms a person can follow — as opposed to explaining an individual output after the fact.

Olah et al. (Distill, 2020) set out the research program as three claims: **features** are the fundamental unit of a network, **circuits** are the computational subgraphs formed when features connect through weights, and **universality** holds that analogous features and circuits recur across different models and tasks. The program's ambition is not a summary of behavior but a mechanism — the same sense in which one understands a compiled program by reading it.

**Superposition is the obstacle that shaped the field.** Networks represent more distinct features than they have neurons, so an individual neuron is typically *polysemantic* — it activates for several unrelated things. Reading a model neuron by neuron therefore does not work, and early interpretability work that did so was reading an artifact of the coordinate system rather than the model's own units.

**Dictionary learning is the current answer.** Sparse autoencoders decompose activations into a larger set of sparsely-active directions that are closer to monosemantic. Templeton et al. (Anthropic, 2024) scaled this to a production model, Claude 3 Sonnet, extracting millions of features including safety-relevant ones, and demonstrated that features are **causal rather than merely correlational**: artificially amplifying or suppressing a feature changes the model's behavior in the corresponding direction. That is the property that separates this from a description.

**The distinction from explainability is the one to hold onto.** [Explainability (XAI)](explainability-xai.md) generally produces a post-hoc account of a decision — saliency, attributions, or a natural-language rationale. Mechanistic interpretability targets the computation itself. This matters because a model's own explanation of its reasoning **can be unfaithful to the computation that produced the answer**, which is measured, not hypothetical ([reasoning models](reasoning-models.md)). A method that does not route through the model's self-report is therefore the only kind that can contradict it.

**What it cannot do yet, stated plainly.** There is no complete circuit-level account of any production model. Finding interpretable features is not the same as explaining a behavior end to end, coverage is unknown, and the analysis is expensive and model-specific. **Interpretability results are evidence, not certification** — no current method licenses a claim that a deployed model is safe.

---

## Plain-language version

Most attempts to understand why an AI did something either ask the model to explain itself, or look at which inputs seemed to matter. Mechanistic interpretability tries something harder: to open the model up and work out what it is actually computing, the way you might read a program's source code rather than its logs.

The research program assumes there are recognizable parts inside — recurring "features" that detect particular things, wired together into small circuits that do particular jobs — and that similar parts show up across different models.

There is a catch that took years to work around. A model packs far more concepts into it than it has components, so any single unit inside tends to respond to several unrelated things at once. Looking at units one by one tells you very little. The workaround is a technique that pulls the tangle apart into a much larger set of cleaner pieces. Applied to a real commercial model, it surfaced millions of recognizable concepts — and, importantly, turning one of those up or down actually changed how the model behaved. That is the difference between spotting a pattern and finding a lever.

Why it matters more than it sounds: a model can give you a fluent account of its reasoning that does not match what it actually did. Every method that relies on the model explaining itself inherits that problem. This one does not, which makes it the only approach that can catch the model out.

The honest limit is that nobody has a full explanation of any deployed model, and none of this yet supports saying a system is safe. It is a live research direction, not an audit tool.

---

## AI literacy notes

1. **This is not the model explaining itself** — that is the whole point, and the reason it is worth the cost.
2. **A model's stated reasoning can diverge from its actual computation**, so self-report-based methods cannot detect the cases that matter most.
3. **Individual neurons are not concepts.** Networks pack more features than units, so reading neuron by neuron mostly misleads.
4. **Features found this way are causal**, not just correlated — you can steer behavior by manipulating them, which is what makes them real findings.
5. **Interpretable ≠ explained.** Millions of features is not an account of any single behavior end to end.
6. **Coverage is unknown.** Nobody can say what fraction of a model's computation current methods capture.
7. **It does not certify anything.** Treat any vendor claim that interpretability makes a model "verified safe" as unsupported.
8. **It is the main non-behavioral route to oversight** — every other approach tests outputs, which only reveals what you thought to test ([red teaming](red-teaming.md), [evaluation](evaluation.md)).

---

## Governance notes

**Core question:** When this system does something we did not expect, what would we actually inspect — its output, its own explanation of itself, or its computation? And which of those can be wrong without anyone noticing?

**Watch for:**
- Interpretability cited as evidence a model is safe, rather than as one input among several ([bluewashing](bluewashing.md))
- A model's natural-language rationale treated as an account of its reasoning ([explainability (XAI)](explainability-xai.md), [reasoning models](reasoning-models.md))
- Feature steering used to shape behavior in production without a record of what was clamped and who approved it
- Interpretability findings from one model generalized to another, where universality is a research claim rather than a guarantee
- Vendor-published interpretability results accepted without noting that the vendor chose which features to show
- "Explainable" and "interpretable" used interchangeably in procurement documents, where they mean materially different things
- Oversight resting entirely on behavioral testing, which cannot see a capability nobody probed for ([scalable oversight](scalable-oversight.md))

**Practice:**
- **Ask which evidence a claim about model behavior actually rests on** — output, self-report, or mechanism — and record the answer alongside the claim
- Treat interpretability results as evidence that raises or lowers confidence, never as a pass/fail gate
- Where feature steering is used, log the intervention as a configuration change with an owner ([audit trail](audit-trail-ai.md))
- Distinguish explainability obligations (which regulation increasingly imposes) from mechanistic understanding (which no method currently delivers) in [compliance](compliance-ai-systems.md) work
- Prefer suppliers who publish limitations and negative results, not only successful feature extractions
- Keep behavioral testing regardless — mechanism and behavior are complements, and neither substitutes for the other

**Key accountability owner:** whoever signs off that a model is understood well enough to deploy — because that sign-off is routinely supported by explanations the model generated about itself, and this is the field that exists to say why that is not sufficient.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the research program, low-medium on operational readiness — and the gap between those is the entry's point.** The features/circuits framing, superposition, and the causal demonstration of steering at production scale are each documented in named published work. **What is not established is anything an organization can rely on today:** there is no complete mechanistic account of any deployed model, no measure of what fraction of computation current methods explain, no standard for what counts as sufficient interpretability, and no method that supports a safety certification. **A significant share of the leading work is published by the labs that build the models**, on their own systems, choosing which results to show — that is a real limitation on the evidence base even where the methods are sound, and it is the reason this entry cites the ambition and the demonstrated mechanism separately from any claim about assurance.

---

## Related concepts

- [Explainability (XAI)](explainability-xai.md) — post-hoc accounts of decisions; the contrast that defines this field
- [Black Box](black-box.md) — the problem both are responses to
- [Reasoning Models / Test-Time Compute](reasoning-models.md) — where self-reported reasoning is measurably unfaithful
- [Recurrent Depth](recurrent-depth.md) — reasoning that leaves no trace at all, making mechanism the only available evidence
- [Alignment (AI Systems)](alignment-ai-systems.md) — what interpretability is ultimately meant to verify
- [Scalable Oversight](scalable-oversight.md) — the limits of supervising by behavior alone
- [Deception (AI Systems)](deception-ai-systems.md) — the failure mode self-report cannot be trusted to reveal
- [Evaluation](evaluation.md) — behavioral testing, the complement to mechanism
- [Red Teaming](red-teaming.md) — adversarial probing, which finds only what it thinks to look for
- [Frontier AI](frontier-ai.md) — where most of this research is done, and by whom

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-255 | Olah, C.; Cammarata, N.; Schubert, L.; Goh, G.; Petrov, M.; Carter, S. — *Zoom In: An Introduction to Circuits* (Distill, March 10 2020) · [link](https://distill.pub/2020/circuits/zoom-in/) | The research program's founding statement: features as the fundamental unit, circuits as their computational subgraphs, and universality across models. |
| SRC-256 | Templeton, A.; Conerly, T.; Marcus, J.; Lindsey, J.; Bricken, T.; Chen, B. et al. (Anthropic) — *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet* (Transformer Circuits Thread, May 21 2024) · [link](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) | Dictionary learning scaled to a production model; millions of features extracted, and the demonstration that they are **causal** — amplifying or suppressing one changes behavior. ⚠️ Vendor-authored, on the vendor's own model, with the vendor selecting which features to present. |
| SRC-125 | Singh, C.; Inala, J.P.; Galley, M.; Caruana, R.; Gao, J. — *Rethinking Interpretability in the Era of Large Language Models* (2024) · [link](https://arxiv.org/abs/2402.01761) | Situates mechanistic work against natural-language explanation in the LLM era, and why the two answer different questions. |
| SRC-123 | Doshi-Velez, F.; Kim, B. — *Towards a Rigorous Science of Interpretable Machine Learning* (2017) · [link](https://arxiv.org/abs/1702.08608) | The standing argument that "interpretability" needs stated criteria rather than intuition — the basis for this entry's refusal to treat results as certification. |
| SRC-023 | Lipton, Zachary C. — *The Mythos of Model Interpretability* (2016) · [link](https://arxiv.org/abs/1606.03490) | That interpretability names several incompatible goals, which is why explainability and mechanistic understanding must not be used interchangeably. |
| SRC-240 | Chen, Y.; Benton, J.; Radhakrishnan, A.; Uesato, J.; Denison, C.; Schulman, J. et al. (Anthropic) — *Reasoning Models Don't Always Say What They Think* (2025) · [link](https://arxiv.org/abs/2505.05410) | The measured unfaithfulness of self-reported reasoning — the reason a non-self-report method is necessary rather than merely preferable. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Record which kind of evidence supports each claim about model behavior — output, self-report, or mechanism. Treat interpretability as confidence-shifting evidence, never as a gate. |
| **Organizational** | "Explainable" and "interpretable" are not synonyms, and procurement documents routinely treat them as such. No current method licenses a claim that a model is verified safe. |
| **Client-facing** | Explains why "the AI told us why it did that" is weaker evidence than it sounds, without overclaiming what the alternative can currently deliver. |
| **LLM-native** | Neurons are not concepts — superposition means models pack more features than units. Features found by dictionary learning are causal, and steering one changes behavior. |

---

*Last updated: v1.0 · September 2026*
