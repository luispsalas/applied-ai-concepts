<!--meta
category: Knowledge & Memory
short: The maximum amount of text an AI model can consider at once — a hard limit on what it can reason about
aliases: [token limit, how much can it read, input length limit, maximum context, context size]
tags: [Architecture]
-->
# Context Window

## One-line essence
The maximum amount of text an AI model can consider at once — a hard limit on what it can reason about when generating any given response.

---

## Technical definition

The context window is the maximum number of tokens a model can process in a single forward pass — the system prompt, conversation history, retrieved content, and the model's own output all draw from this shared, finite budget. Attention computation scales with the square of sequence length (SRC-141), which historically bounded window size; even as windows have grown to hundreds of thousands or millions of tokens, models do not use that capacity uniformly: performance degrades for information placed in the middle of a long context, with strongest recall for content near the start or end (SRC-149, the "lost in the middle" effect). A model's effective context — how much it can actually use reliably — is therefore often smaller than its advertised window.

---

## Plain-language version

The context window is how much text an AI can "hold in mind" at once — your conversation so far, any documents it's been given, and its own instructions all share this one limited space. When it fills up, older or excess content gets dropped or summarized, and the AI can lose track of things you said earlier — "hit its limit" or "forgot" is usually this. And even within a window that isn't full, information buried in the middle of a long document tends to get less attention than what's at the start or end — so a bigger window isn't the same as reading everything equally well.

---

## AI literacy notes

1. **"Hit the limit" and "forgot" are the same failure.** When people say an AI "forgot" something from earlier, it's frequently the context window: that information is no longer in the window, not erased from some deeper memory (see [Memory (AI Systems)](memory-ai-systems.md)).
2. **A bigger window is not the same as reliable recall.** Models retrieve content near the start and end of a long context far better than content buried in the middle — so pasting in more text is not a substitute for good context design (see [Context Engineering](context-engineering.md)).
3. **Everything competes for the same budget.** System prompt, conversation history, retrieved documents, and tool outputs all draw from one shared window — a bloated system prompt or an oversized retrieval leaves less room for everything else.
4. **Advertised size ≠ effective size.** A model's stated window (e.g. 1M tokens) is a ceiling, not a guarantee of uniform performance across that whole range.

---

## Governance notes

**Core question:** Does the system's design account for the window being finite and unevenly used — not just "big enough"?

**Watch for:**
- Assuming a larger advertised window solves recall problems
- System prompts or retrieved content bloating the window with no monitoring
- Important instructions or facts placed in the middle of a long context where they're least likely to be used

**Practice:**
- Monitor token usage per turn/session, not just total window size
- Place critical instructions near the start or end of context, not buried in the middle
- Test long-context behavior directly rather than assuming uniform recall

**Key accountability owner:** the harness/context owner.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The architectural mechanism (finite token budget, quadratic attention cost) and the "lost in the middle" degradation pattern are both well-documented and independently reproduced; window sizes and mitigation techniques (e.g. compaction) continue to evolve quickly.

---

## Related concepts

- [Context Engineering](context-engineering.md) — designing what fills the window is the practical discipline that follows from its being finite
- [Memory (AI Systems)](memory-ai-systems.md) — the window is in-session/ephemeral memory; anything meant to persist needs a mechanism outside it
- [Large Language Models (LLMs)](large-language-models.md) — the attention mechanism inside the model is what makes the window both possible and bounded
- [Harness Paradigm](harness-paradigm.md) — context compaction and window management are implemented at the harness layer
- [Retrieval-Augmented Generation (RAG)](rag.md) — RAG exists partly to fit relevant knowledge inside the window rather than requiring the whole knowledge base in context
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — silently dropped or "lost in the middle" content is a named failure mode

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-149 | Liu, N.F. et al. — *Lost in the Middle: How Language Models Use Long Contexts* (TACL, 2023) · [link](https://arxiv.org/abs/2307.03172) | The reference finding: recall degrades for information in the middle of long contexts; best performance when relevant content is at the start or end. |
| SRC-141 | Vaswani, A. et al. — *Attention Is All You Need* (NeurIPS, 2017) · [link](https://arxiv.org/abs/1706.03762) | The attention mechanism whose computational cost is the architectural origin of a bounded context window. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Token budget management, compaction strategy, and content placement are direct engineering levers for reliability. |
| **Organizational** | Explains a common support complaint ("it forgot") in terms that lead to a fix (context/memory design), not just a shrug. |
| **Client-facing** | Sets accurate expectations: a long conversation or a huge document dump doesn't guarantee the AI is using all of it equally well. |
| **LLM-native** | The finite, shared resource every other context-handling concept in this wiki is designed around. |

---

*Last updated: v1.0 · July 2026*
