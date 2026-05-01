# Persistent Synthesis

## One-line essence
Knowledge compounds when contradictions are resolved — not when information is accumulated.

---

## Technical definition

Persistent synthesis is a knowledge management approach in which new information is integrated into an existing knowledge structure by resolving conflicts, updating superseded entries, and tracing relationships — rather than being appended as an additional source. The core principle, as stated by Ghumare (2024): **"stop re-deriving, start compiling."** The result is a living artifact that reflects the current state of understanding, not a growing archive of everything that was ever written.

The approach is defined by several operational commitments:

**Resolution over accumulation** (Karpathy, 2023; Ghumare, 2024)
When new information contradicts existing content, the contradiction is addressed explicitly — one position is updated, deprecated, or flagged as context-dependent. Both versions are not left to coexist without annotation.

**Temporal decay of confidence** (Ghumare, 2024 — extending Ebbinghaus forgetting curve principles)
Knowledge entries carry a confidence level that degrades over time unless actively refreshed. Facts decay unless reinforced, with different decay rates for different knowledge types — architecture decisions decay more slowly than transient implementation details.

**Typed relationships** (Ghumare, 2024)
Connections between concepts are explicit and directional: *uses*, *depends on*, *contradicts*, *supersedes*, *specializes*. A flat list of "related concepts" is not a knowledge graph; typed edges enable graph traversal — surfacing downstream dependencies that keyword search misses.

**The schema document as primary artifact** (Ghumare, 2024)
The most important file in a persistent knowledge system is not the content — it is the schema: the document that encodes entity types, relationship types, quality standards, and consolidation schedules. Without a schema, synthesis is informal and non-reproducible.

**Automation as maintenance infrastructure** (Ghumare, 2024)
Manual-only processes kill wikis over time. A maintainable system includes auto-triggers — on new source ingestion, session end, contradiction detection, and periodic consolidation. Humans curate direction; the system handles bookkeeping. A lint/self-healing operation fixes orphaned pages, marks stale claims, and repairs broken references.

This approach draws on a memory architecture that distinguishes between working memory (immediate context), episodic memory (session-specific learning), semantic memory (generalized concepts), and procedural memory (operational patterns) — each requiring different maintenance cadences (Ghumare, 2024).

---

## Plain-language version

Most knowledge systems are archives: you add things, but you rarely update or remove them. Over time, you accumulate contradictions you're not aware of, outdated entries that still feel authoritative, and connections that are implied but never mapped.

Persistent synthesis is the alternative — expressed simply as: **stop re-deriving, start compiling.**

Instead of rediscovering the same insight repeatedly across sessions, you compile it once, maintain it actively, and build on it. The discipline requires treating knowledge entries like living documents — updating them when they're superseded, flagging them when confidence has decayed, and tracking how concepts relate to each other rather than just listing them side by side.

The payoff is compounding: every new thing you learn sharpens what you already have, instead of just adding to the pile.

---

## AI literacy notes

Persistent synthesis has direct relevance to how AI systems store and use knowledge — and to how humans should maintain knowledge bases that feed into AI workflows.

Three implications:

1. **Accumulation without synthesis creates drift.** A knowledge base that grows by addition drifts gradually away from current reality. Entries written months ago carry the same apparent authority as entries written today. The system doesn't know what it doesn't know.
2. **AI systems inherit the quality of their knowledge inputs.** A retrieval-augmented system or a context-engineered workflow is only as current as the knowledge base it draws from. Garbage-in-garbage-out applies to knowledge architecture, not just to data pipelines.
3. **The wiki as an artifact.** This repository is itself an application of persistent synthesis: source documents are inputs, resolved entries are outputs, and contradictions between sources are addressed in the entries rather than surfaced to the reader as conflicting references.

---

## Confidence level

**Emerging — practitioner application.** The core insight (Karpathy, 2023) is widely validated in practice. The extended framework (Ghumare, 2024) adds significant structural depth, but carries known implementation gaps flagged in community review:

- Confidence scoring lacks a rigorous operational definition
- "Crystallization" (the point at which synthesized knowledge becomes stable) is underspecified
- Automation timelines assume compositional tooling that may not yet exist at scale
- Human-in-the-loop failure modes are not fully addressed

*(Source for limitations: @gnusupport community critique of Ghumare gist, 2024)*

These gaps do not invalidate the framework — they define its frontier. The principles are sound; the engineering details require careful, context-specific implementation.

---

## Related concepts

- [Context Engineering](context-engineering.md) — a well-maintained knowledge base is a reusable context asset; synthesis is how it stays useful over time
- [Hallucination](hallucination.md) — synthesis disciplines (contradiction resolution, confidence decay) are responses to hallucination risk in knowledge pipelines
- Memory (AI Systems) — the memory lifecycle model (working / episodic / semantic / procedural) informs synthesis maintenance cadences
- Knowledge Base — the artifact that persistent synthesis produces and maintains
- Model/Data Drift — the failure mode that persistent synthesis prevents: gradual divergence between a knowledge system and current reality

---

## Sources

| Source | Contribution |
|---|---|
| Karpathy, A. — *LLM Wiki* (gist, 2023) | Original synthesis philosophy; wiki as compounding artifact; contradictions flagged not accumulated; source docs as inputs, wiki as output |
| Ghumare, R. — *LLM Wiki v2* (gist, 2024) · [link](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) | "Stop re-deriving, start compiling"; memory lifecycle tiers; confidence scoring with temporal decay (Ebbinghaus); typed relationships; hybrid search (BM25 + vector + graph); schema doc as primary artifact; automation & event hooks; lint/self-healing operation |
| @gnusupport — community critique of Ghumare gist (2024) | Implementation limitations: confidence scoring underspecified, crystallization undefined, timeline assumptions, HITL failure modes |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs knowledge base design for AI systems: how to structure entries, when to deprecate content, how to model relationships between concepts, and what automation is needed for long-term maintenance. |
| **Organizational** | The principle that explains why AI knowledge assets degrade without active maintenance — and what "active maintenance" actually means in practice. |
| **LLM-native** | The operating philosophy of this wiki. Every design decision in this repository reflects the synthesis principle: source documents are inputs; the wiki is the output. |

---

*Last updated: v1.1 · April 2026*
