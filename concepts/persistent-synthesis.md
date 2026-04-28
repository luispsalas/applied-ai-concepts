# Persistent Synthesis

## One-line essence
Knowledge compounds when contradictions are resolved — not when information is accumulated.

---

## Technical definition

Persistent synthesis is a knowledge management approach in which new information is integrated into an existing knowledge structure by resolving conflicts, updating superseded entries, and tracing relationships — rather than being appended as an additional source. The result is a living artifact that reflects the current state of understanding, not a growing archive of everything that was ever written.

The approach is defined by three operational commitments:

1. **Resolution over accumulation.** When new information contradicts existing content, the contradiction is addressed explicitly — one position is updated, deprecated, or flagged as context-dependent. Both versions are not left to coexist without annotation.
2. **Temporal decay of confidence.** Knowledge entries carry a confidence level that degrades over time unless actively refreshed. An entry that has not been reviewed recently is flagged, not silently trusted.
3. **Typed relationships.** Connections between concepts are explicit and directional: *uses*, *depends on*, *contradicts*, *supersedes*, *specializes*. A flat list of "related concepts" is not a knowledge graph; typed edges are.

This approach draws on memory architecture research that distinguishes between working memory (immediate context), episodic memory (session-specific learning), semantic memory (generalized concepts), and procedural memory (operational patterns) — each requiring different maintenance cycles.

---

## Plain-language version

Most knowledge systems are archives: you add things, but you rarely update or remove them. Over time, you accumulate contradictions you're not aware of, outdated entries that still feel authoritative, and connections that are implied but never mapped.

Persistent synthesis is the alternative: a knowledge base that is actively maintained to reflect what you currently know, not everything you ever wrote down.

The discipline requires treating knowledge entries like living documents — updating them when they're superseded, flagging them when confidence has decayed, and tracking how concepts relate to each other rather than just listing them side by side.

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

**Emerging — practitioner application.** The underlying principles draw from established knowledge management and cognitive science literature. The specific application to LLM-native knowledge systems is newer, with active development in the practitioner community (2023–present).

---

## Related concepts

- [Context Engineering](context-engineering.md) — a well-maintained knowledge base is a reusable context asset; synthesis is how it stays useful over time
- [Hallucination](hallucination.md) — synthesis disciplines (contradiction resolution, confidence decay) are responses to hallucination risk in knowledge pipelines
- Memory (AI Systems) — the memory lifecycle model (working / episodic / semantic / procedural) informs synthesis maintenance cadences
- Knowledge Base — the artifact that persistent synthesis produces and maintains
- Model/Data Drift — the failure mode that persistent synthesis prevents: gradual divergence between a knowledge system and current reality

---

## Sources

- Karpathy, A. — LLM Wiki (gist, 2023) — persistent synthesis as a design philosophy; wiki as a compounding knowledge artifact; contradictions flagged, not accumulated
- Ghumare, R. — LLM Wiki v2 (gist) — memory lifecycle model (working/episodic/semantic/procedural); confidence scoring with temporal decay; typed knowledge graph relationships (*uses*, *depends on*, *contradicts*, *supersedes*); hybrid search (BM25 + vector + graph)

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs knowledge base design for AI systems: how to structure entries, when to deprecate content, how to model relationships between concepts. |
| **Organizational** | The principle that explains why AI knowledge assets degrade without active maintenance — and what "active maintenance" actually means in practice. |
| **LLM-native** | The operating philosophy of this wiki. Every design decision in this repository reflects the synthesis principle: source documents are inputs; the wiki is the output. |

---

*Last updated: v1.0 · April 2026*
