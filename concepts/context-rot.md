<!--meta
category: Knowledge & Memory
short: Reliability falling as the input gets longer — the failure the context window does not warn you about, because everything still fits
aliases: [context degradation, long context degradation, lost in the middle, position effect, degradation with input length, long context problem, why does it get worse with more context]
tags: [Model Behavior, Evaluation, Architecture]
established: emerging
-->
# Context Rot

> **Term status — Emerging.** Named in a 2025 cross-vendor technical report and picked up independently by engineering teams and technology journalism within months. Filed `emerging` rather than `established` because the naming is recent and no standards body has adopted it — **the underlying effect, however, is established**, documented in peer-reviewed work two years earlier under a different name.

## One-line essence
Model reliability falls as the input gets longer — the same task answered worse at a hundred thousand tokens than at one thousand — so "it fits in the context window" is not an assurance that the model will use what is in there.

---

## Technical definition

Context rot is the degradation of a model's performance as its input grows, holding the task constant. It is a claim about **non-uniform use of the context**, not about the limit of the context.

**This is the distinction that makes the term worth having.** The [context window](context-window.md) is a capacity: a hard boundary past which text is refused or truncated. Context rot describes what happens *inside* that boundary. **The window tells you whether the text fits; it tells you nothing about whether the model will attend to it**, and there is no error, warning or truncation notice when it does not.

**The effect was documented before it was named.** Liu et al. found that performance on multi-document question answering and key-value retrieval depends on *where* the relevant information sits: highest when it appears at the beginning or end of the input, and — in their words — it "significantly degrades when models must access relevant information in the middle of long contexts, **even for explicitly long-context models**." A model advertised as handling long inputs is not thereby a model that uses them evenly.

**The cross-vendor measurement is what turned it into a general claim.** Chroma evaluated 18 frontier models — including releases from four competing vendors — and reports that reliability decreases significantly with longer inputs *even on simple tasks* such as retrieval and text replication. Their framing is the useful one: models **do not use their context uniformly**, and performance grows increasingly unreliable as input length grows.

**Three consequences follow for anything built on long inputs:**

- **A [RAG](rag.md) system that retrieves more passages does not thereby know more.** Adding a twentieth document can lower the answer quality that ten produced, and the retrieval metrics will look better while the answers get worse.
- **Evaluation on short inputs does not transfer.** A system benchmarked on compact prompts and deployed against long documents, long transcripts or long agent histories has been tested in a regime it does not operate in ([evaluation](evaluation.md)).
- **It compounds over an agent's run.** A long-running agent's context grows monotonically until something reduces it, so degradation is not a rare edge case but the default trajectory ([context compaction](context-compaction.md), [AI agent](ai-agent.md)).

**"Rot" is a metaphor and slightly misleading.** Nothing decays over time; the model is not losing information it once had. The dependence is on **length and position within a single forward pass**, which is why the same content at the top of a short prompt and buried inside a long one produces different behavior with no state changing in between ([determinism vs probabilism](determinism-vs-probabilism.md)).

---

## Plain-language version

Everyone knows a model has a limit on how much text you can give it. Fewer people know that getting under the limit is not the same as being understood.

**Context rot is the finding that models get less reliable the more you give them** — on the same question, with the same right answer sitting in the pile. Put the key fact at the start or the end of a long document and the model usually finds it. Put it in the middle and it often does not.

Two things make this genuinely dangerous rather than merely annoying.

**Nothing tells you it happened.** If you exceed the window, you get an error. If you stay inside it but the model quietly stops attending to the middle of what you sent, you get a confident, well-formed, wrong answer. There is no warning, no truncation notice, no flag. The system behaves as though it read everything.

**And the obvious fix makes it worse.** When an answer is poor, the instinct is to supply more context — more retrieved documents, more history, more background. That is the direction that degrades performance. **More context is not more knowledge**, and past a point it is less.

This is measured across models from four different companies, so it is not a quirk of one product. It is also not new: researchers documented the position effect in 2023, before anyone was calling it rot.

One caution about the name. Nothing is actually rotting. The model is not forgetting things it knew a moment ago — it is that a long input is used less evenly than a short one, right now, in this single pass. The word is memorable and a bit wrong.

---

## AI literacy notes

1. **Fitting in the window is not being used** — the limit and the attention are different things.
2. **There is no signal when it happens.** No error, no truncation, no flag.
3. **Position matters**: beginning and end are attended to more reliably than the middle.
4. **Measured across 18 models from four vendors** — not a single-product quirk.
5. **Documented in peer-reviewed work in 2023**, before the name existed.
6. **Adding more context is the intuitive fix and often the wrong one.**
7. **Long-context marketing is about capacity, not about uniform use.**
8. **Agent runs trend toward the degraded regime** as history accumulates.
9. **The metaphor is imprecise** — length and position, not decay over time.

---

## Governance notes

**Core question:** Was this system evaluated at the input lengths it actually runs at in production — and if the answer degrades quietly, how would anyone find out?

**Watch for:**
- Evaluation performed on short prompts for a system that runs on long documents or long histories ([evaluation](evaluation.md))
- A retrieval system tuned on retrieval metrics while answer quality is never measured against the number of passages supplied ([RAG](rag.md))
- "It fits in the context window" offered as an assurance that the model considered the whole input
- Long-context capacity in a vendor claim treated as evidence of uniform attention ([supply chain risk](supply-chain-risk-ai.md))
- Poor answers met by adding more context, with no test of whether that helps
- Critical instructions or policy text placed in the middle of a long system prompt ([system prompt](system-prompt.md))
- Agent runs with unbounded context growth and no compaction strategy ([context compaction](context-compaction.md))
- A model version upgrade assumed to have fixed it, with no re-measurement ([model version and update](model-version-update.md))

**Practice:**
- **Evaluate at production input lengths, not convenient ones** — and report the length alongside the score, because a score without it is not comparable
- **Measure quality as a function of context length deliberately**: run the same task at several input sizes and look for the point where it turns over
- **Put load-bearing instructions at the beginning or the end**, and treat the middle of a long input as the least reliable position
- Test retrieval systems for the passage count at which answers stop improving, and cap there rather than at the window limit ([RAG](rag.md))
- **Prefer selecting the right context over supplying all available context** ([context engineering](context-engineering.md))
- Give long-running agents an explicit compaction or summarization strategy, and know what it discards ([context compaction](context-compaction.md))
- Re-measure after any model change — this is a per-model behavior, not a fixed property of the technique
- Where a long input is unavoidable, chunk the task rather than the prompt, so each pass operates in the reliable regime ([prompt chaining](prompt-chaining.md))

**Key accountability owner:** whoever owns the evaluation — because the defining property of this failure is that it produces confident, well-formed, wrong output with no operational signal, so the only place it can be caught is in a test designed to look for it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the effect, moderate on the term.** The underlying finding is peer-reviewed (TACL) and independently reproduced at scale across 18 models from four competing vendors, which is unusually strong evidence for a claim about model behavior. **Two caveats worth carrying.** The cross-vendor measurement comes from a **retrieval-infrastructure vendor**, for whom "long context degrades" is a commercially useful finding — the measurement is published with its method and the peer-reviewed antecedent agrees with it, but the framing is not disinterested. And **the magnitude is model-specific and dates quickly**: the direction is robust, the numbers are a snapshot of a particular set of releases, so this entry deliberately quotes no percentage. **A figure sometimes attached to the 2023 paper — a drop of more than thirty points — is not in its abstract and was not verified here**; it is omitted rather than repeated.

---

## Related concepts

- [Context Window](context-window.md) — the limit this is explicitly not about
- [Context (AI Systems)](context-ai-systems.md) — what gets assembled for each response
- [Context Engineering](context-engineering.md) — selecting context rather than maximizing it
- [Context Compaction](context-compaction.md) — reducing history to stay in the reliable regime
- [Context Anxiety](context-anxiety.md) — a different length-related failure, about the model's own estimate
- [Memory (AI Systems)](memory-ai-systems.md) — where in-session degradation is felt
- [RAG](rag.md) — the architecture most exposed to it
- [Evaluation (AI Systems)](evaluation.md) — where testing at the wrong length hides it
- [Prompt Chaining](prompt-chaining.md) — splitting work to keep each pass short
- [System Prompt](system-prompt.md) — instructions whose position matters
- [AI Agent](ai-agent.md) — the workload whose context grows without bound
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the family this belongs to

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-333 | Hong, Kelly; Troynikov, Anton; Huber, Jeff (Chroma) — *Context Rot: How Increasing Input Tokens Impacts LLM Performance* (Chroma Research, 14 July 2025) · [link](https://www.trychroma.com/research/context-rot) | The anchor for the term and the cross-vendor measurement: 18 frontier models across four competing vendors, with reliability decreasing as input length grows even on simple retrieval and replication tasks, and the framing that models **do not use their context uniformly**. ⚠️ Vendor-produced by a retrieval-infrastructure company, and not peer-reviewed — cite the measurement, not the framing. |
| SRC-149 | Liu, N.F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; Liang, P. — *Lost in the Middle: How Language Models Use Long Contexts* (2023) · [link](https://arxiv.org/abs/2307.03172) | The peer-reviewed antecedent (TACL) and the independent corroboration: performance is highest when relevant information is at the beginning or end and **significantly degrades in the middle of long contexts, even for explicitly long-context models**. ⚠️ No percentage figure is quoted here; the widely repeated 30-point number is not in the abstract. |
| SRC-342 | Lee, Timothy B. (Understanding AI) — *Context rot: the emerging challenge that could hold back LLM progress* (2025) · [link](https://www.understandingai.org/p/context-rot-the-emerging-challenge) | Registered as **evidence of independent adoption** for the term-status call rather than for any factual claim — an independent journalist with no product to sell treating the term as a named phenomenon. ⚠️ Secondary; all measurements belong to the two rows above. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | The practitioner framing for why agent workloads trend into the degraded regime: long-running loops accumulate context by construction. ⚠️ Vendor-produced — used for the architectural observation only. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Evaluate at production input lengths and report length with the score. Find the passage count where answers stop improving, and cap there. |
| **Organizational** | A bigger context window is a capacity claim, not a comprehension claim. The failure produces confident wrong answers with no error to notice. |
| **Client-facing** | Explains why sending the whole document is not always better than sending the right part of it. |
| **LLM-native** | Position matters: beginning and end beat the middle. An agent's context grows monotonically, so degradation is the default trajectory, not an edge case. |

---

*Last updated: v1.0 · September 2026*
