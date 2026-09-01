<!--meta
category: Foundations
short: Every model was trained up to a fixed date and knows nothing after it — and cannot reliably tell you when a question falls outside what it knows
aliases: [training cutoff, why doesn't it know about recent events, out of date model, cutoff date, stale knowledge]
tags: [Model Behavior, AI Literacy]
-->
# Knowledge Cutoff

## One-line essence
Every model was trained up to a fixed point in time and knows nothing after it — which is why it can be confidently wrong about recent events, and why it may not know it is out of date.

---

## Technical definition

The date at which a model's training data ends. Everything the model learned during training reflects the world up to that point; nothing after it exists in the model's parameters unless supplied at the time of the question.

Three properties matter more than the date itself:

- **The boundary is not clean.** Coverage thins out approaching the cutoff rather than stopping at it, because recent events are underrepresented in a corpus assembled shortly afterward. A model's effective knowledge of the last months before its cutoff is usually weaker than its knowledge of the years before that.
- **Degradation continues after deployment, and grows.** Peer-reviewed evaluation found language models perform measurably worse on text from beyond their training period, and **worse the further past it you go**. A model does not merely stop learning at the cutoff; its usefulness decays as the world moves on.
- **Scale does not fix it.** The same work found that increasing model size alone does not solve temporal generalization. **A bigger model is not a more current one** — only continual updating, or supplying current information at question time, addresses it.

The model also has no reliable way to know that a question falls after its cutoff. It has no clock and no sense of the present date unless told. Asked about something recent, it will often answer from what it has, in the same register it uses for everything else — see [Confidence vs Accuracy](confidence-vs-accuracy.md).

The practical remedy is not a better model but a different architecture: supplying current information at question time, through search or [retrieval](rag.md), so the answer is [grounded](grounding.md) in something the model did not have to remember. Note that this moves the staleness problem rather than eliminating it — a retrieval corpus ages too.

---

## Plain-language version

A model learned from a snapshot of the world that ends on a particular date. Ask about anything after that and it is working from nothing — but it usually will not say so, because it has no way of knowing what it missed. It does not know what today's date is unless you tell it, and it cannot tell the difference between a question it can answer and one that happened after it stopped learning.

---

## AI literacy notes

1. **It cannot reliably tell you when it does not know.** The missing information is missing — there is no gap-shaped hole the model can detect and report. This is why "are you sure that's current?" is a weak check: the model has nothing to consult.
2. **The last few months before the cutoff are the weakest, not the strongest.** Coverage thins as the date approaches. Recent-but-pre-cutoff facts are exactly where confident errors cluster.
3. **A newer or larger model is not automatically more current.** Model size and cutoff date are independent, and scale does not solve temporal decay. Check the stated cutoff rather than assuming the newest option knows the most.
4. **It gets worse with time, not just stuck.** A model deployed for two years is measurably less useful than it was at launch, without anything having changed about the model.
5. **If a system answers current questions well, something else is doing the work** — search or retrieval, not the model's memory. That component has its own freshness problem worth asking about.

---

## Governance notes

**Core question:** Where does this system answer questions whose correct answer changes over time — and what supplies the current information, if anything does?

**Watch for:**
- Time-sensitive use cases (prices, regulation, policy, personnel, availability) served from model memory alone
- Cutoff dates undocumented, so nobody can say what the system should and should not be asked
- Users assuming an upgraded model is a more current one
- Retrieval treated as solving staleness while the retrieval corpus itself goes unmaintained
- No re-evaluation as time passes since deployment, despite documented ongoing degradation

**Practice:**
- Record the cutoff date of every model in use, and re-check it on every version change
- Identify time-sensitive use cases explicitly and route them to [retrieval](rag.md) or search rather than model memory
- Where the answer must be current, show provenance and date so a reader can judge freshness themselves
- Treat corpus freshness as a monitored metric, not a one-time load — see [Model/Data Drift](model-data-drift.md)
- Tell users the cutoff where it plausibly affects them; it is one of the cheapest literacy interventions available

**Key accountability owner:** the system owner, with the data owner for whatever supplies current information.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** That models have a training cutoff is definitional; that performance degrades beyond it, worsens with distance, and is not fixed by scale is peer-reviewed and replicated. Less settled: how vendors document cutoffs (inconsistently, and sometimes imprecisely), and how well models can be made to recognize and disclose the boundary — an active research area with no reliable method.

---

## Related concepts

- [Confidence vs Accuracy](confidence-vs-accuracy.md) — an out-of-date answer arrives in exactly the same confident register as a current one
- [Hallucination](hallucination.md) — asked past its cutoff, a model often fills the gap rather than declining
- [RAG](rag.md) — the standard architectural answer: supply current information at question time
- [Grounding](grounding.md) — anchoring an answer in something checkable rather than remembered
- [Model/Data Drift](model-data-drift.md) — the same staleness problem seen from the organization's side
- [Concealing Uncertainty](concealing-uncertainty.md) — the model rarely volunteers that a question falls outside what it knows
- [Large Language Models (LLMs)](large-language-models.md) — why knowledge lives in fixed parameters at all
- [Knowledge Base](knowledge-base.md) — a retrieval corpus has its own freshness obligation
- Model Version & Update — a new version means a new cutoff, and a new set of things it does not know

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-177 | Lazaridou, A.; Kuncoro, A.; Gribovskaya, E. et al. (DeepMind) — *Mind the Gap: Assessing Temporal Generalization in Neural Language Models* (NeurIPS, 2021) · [link](https://proceedings.neurips.cc/paper/2021/hash/f5bf0ba0a17ef18f9607774722f5698c-Abstract.html) | Performance degrades beyond the training period, worsens with distance from it, and **is not solved by increasing model size**. |
| SRC-028 | Alexander, Emmimal P. — *RAG Is Blind to Time* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/rag-is-blind-to-time-i-built-a-temporal-layer-to-fix-it-in-production/) | That retrieval relocates the staleness problem rather than removing it — the corpus ages too. |
| SRC-142 | Zhao, W.X. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Background: knowledge encoded in fixed parameters at training time is what creates the boundary. |
| SRC-010 | Huang, L. et al. — *A Survey on Hallucination in Large Language Models* (2023) · [link](https://arxiv.org/abs/2311.05232) | What tends to happen when a question falls outside what the model knows. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Route time-sensitive questions to retrieval or search; treat corpus freshness as monitored, and re-check the cutoff on every model version change. |
| **Organizational** | An undocumented cutoff means nobody can say what the system should be asked. Record it, and re-evaluate as deployment time accumulates. |
| **Client-facing** | Explains why an AI system can be wrong about something that happened recently, and why that is a property rather than a defect. |
| **LLM-native** | A newer or larger model is not necessarily more current — cutoff and capability are independent, and scale does not fix temporal decay. |

---

*Last updated: v1.0 · August 2026*
