<!--meta
category: Knowledge & Memory
short: Knowledge compounds when contradictions are resolved, not accumulated
aliases: [knowledge compounding, integrating sources, compile don't re-derive, living document, cumulative knowledge, LLM wiki, Open Knowledge Format]
tags: [Architecture, Data Governance]
established: emerging
-->
[Applied AI Concepts](../README.md) › [Knowledge & Memory](../glossary/categories.md#knowledge--memory) › Persistent Synthesis

# Persistent Synthesis

> **Term status — Emerging.** In active use and genuinely useful, but not yet settled, and definitions still vary between sources. Read the Confidence level before relying on the term in a formal document.

## One-line essence
Knowledge compounds when contradictions are resolved, not when information is accumulated.

---

## Technical definition

Persistent synthesis is a knowledge management approach in which new information is integrated into an existing knowledge structure by resolving conflicts, updating superseded entries, and tracing relationships, rather than being appended as an additional source. The core principle, as stated by Ghumare (2026): **"stop re-deriving, start compiling."** The result is a living artifact that reflects the current state of understanding, not a growing archive of everything that was ever written.

The approach is defined by several operational commitments:

**Resolution over accumulation** (Karpathy, 2026; Ghumare, 2026)
When new information contradicts existing content, the contradiction is addressed explicitly. One position is updated, deprecated, or flagged as context-dependent. Both versions are not left to coexist without annotation.

**Temporal decay of confidence** (Ghumare, 2026, extending Ebbinghaus forgetting curve principles)
Knowledge entries carry a confidence level that degrades over time unless actively refreshed. Facts decay unless reinforced, with different decay rates for different knowledge types. Architecture decisions decay more slowly than transient implementation details.

**Typed relationships** (Ghumare, 2026)
Connections between concepts are explicit and directional: *uses*, *depends on*, *contradicts*, *supersedes*, *specializes*. A flat list of "related concepts" is not a knowledge graph; typed edges enable graph traversal, surfacing downstream dependencies that keyword search misses.

**The schema document as primary artifact** (Ghumare, 2026)
The most important file in a persistent knowledge system is not the content. It is the schema: the document that encodes entity types, relationship types, quality standards, and consolidation schedules. Without a schema, synthesis is informal and non-reproducible.

**Automation as maintenance infrastructure** (Ghumare, 2026)
Manual-only processes kill wikis over time. A maintainable system includes auto-triggers, firing on new source ingestion, session end, contradiction detection, and periodic consolidation. Humans curate direction; the system handles bookkeeping. A lint/self-healing operation fixes orphaned pages, marks stale claims, and repairs broken references.

This approach draws on a memory architecture that distinguishes between working memory (immediate context), episodic memory (session-specific learning), semantic memory (generalized concepts), and procedural memory (operational patterns), each requiring different maintenance cadences (Ghumare, 2026).

**Where the pattern stands.** Karpathy published the pattern as a gist in April 2026, and Ghumare's extension followed two days later. By the end of the year it had a proposed file format and its first measured tests.

**A shared file format (Google Cloud, 2026).** In June 2026, two Google Cloud engineers published the Open Knowledge Format (OKF), which their announcement calls "an open specification that formalizes the LLM-wiki pattern into a portable, interoperable format" (McVeety & Hormati, 2026). A bundle is a folder of markdown files with YAML frontmatter. Version 0.2 of the specification adds optional fields for several of the commitments above. A document can list the sources it was derived from, record who verified it, carry a lifecycle status of draft, stable or deprecated, and name the moment after which it counts as stale (`stale_after`). The specification makes two choices that bear on this entry. It declines to store a credibility score, because "a score is subjective, unportable across consumers, and goes stale", and asks readers to infer trust from signals recorded on each source. That departs from the numeric confidence scoring in Ghumare's framework. It also defines no field for resolving a contradiction or for naming the document that replaces a deprecated one, so the central discipline of this entry is still left to whoever maintains the corpus. OKF is a vendor-published draft below version 1.0, maintained in a Google Cloud repository, and no standards body has adopted it.

**First measured tests (2026 preprints).** Ming, Li, Wu and Que (2026) built a system that compiles documents into linked wiki pages, which an agent searches, reads and follows by link, and that keeps an "Error Book for persistent structural and semantic self-correction." On three multi-hop question-answering benchmarks, they report that it outperformed three graph-based retrieval systems "by 2.0-8.1 F1 points." Wang (2026) treats the contradiction step formally. The paper names four strategies that production memory systems use to settle a new claim that conflicts with a stored one: last-writer-wins, evidence-weighted merge, await-confirmation, and per-rule policy. It argues that each should state what it guarantees, and it keeps the losing fact in an audit row instead of erasing it. Both are arXiv preprints with no confirmed peer-reviewed venue, and Wang's has a single author. Treat them as early evidence.

---

## Plain-language version

Most knowledge systems are archives: you add things, but you rarely update or remove them. Over time, you accumulate contradictions you're not aware of, outdated entries that still feel authoritative, and connections that are implied but never mapped.

Persistent synthesis is the alternative, expressed simply as: **stop re-deriving, start compiling.**

Instead of rediscovering the same insight repeatedly across sessions, you compile it once, maintain it actively, and build on it. The discipline requires treating knowledge entries like living documents, which means updating them when they're superseded, flagging them when confidence has decayed, and tracking how concepts relate to each other rather than just listing them side by side.

The payoff is compounding: every new thing you learn sharpens what you already have, instead of just adding to the pile.

---

## AI literacy notes

Persistent synthesis has direct relevance to how AI systems store and use knowledge, and to how humans should maintain knowledge bases that feed into AI workflows.

Three implications:

1. **Accumulation without synthesis creates drift.** A knowledge base that grows by addition drifts gradually away from current reality. Entries written months ago carry the same apparent authority as entries written today. The system doesn't know what it doesn't know.
2. **AI systems inherit the quality of their knowledge inputs.** A retrieval-augmented system or a context-engineered workflow is only as current as the knowledge base it draws from. Garbage-in-garbage-out applies to knowledge architecture, not just to data pipelines.
3. **The wiki as an artifact.** This repository is itself an application of persistent synthesis: source documents are inputs, resolved entries are outputs, and contradictions between sources are addressed in the entries rather than surfaced to the reader as conflicting references.

---

## Governance notes

**Core question:** Who is responsible for maintaining the knowledge base? And is there a defined, enforced process for keeping it current?

**Watch for:**
- Knowledge bases that grow by addition only: new entries appended, old entries never updated or deprecated. A knowledge base without a deprecation process accumulates drift silently. Entries from a year ago carry the same apparent authority as entries written today.
- RAG and retrieval systems inheriting the quality problems of an ungoverned knowledge base. If the knowledge base is stale, inconsistent, or unverified, retrieval makes those problems invisible rather than surfacing them.
- Synthesis treated as informal practice rather than a governed process: no defined cadence, no ownership, no schema doc. Synthesis that depends on individual attention does not survive organizational change.
- A deprecated flag with no pointer to what replaced it. A reader learns that an entry is no longer current but not where the current answer lives. OKF's lifecycle field has the same gap, so a corpus using it needs the pointer in the document body.

**Practice:**
- Define a maintenance cadence by knowledge type. Architecture decisions and foundational concepts require less frequent review than implementation details and vendor-specific information, so set schedules accordingly, not uniformly.
- Deprecate explicitly. When an entry is superseded, mark it so, with a pointer to the replacement. Silent obsolescence is worse than acknowledged obsolescence.
- Record how contradictions are settled. Whichever rule decides between two conflicting claims (newest wins, stronger evidence wins, or wait for a person to confirm), keep the losing claim and the reason it lost, so the decision can be audited later (Wang, 2026).

**Key accountability owner:** Knowledge base owner, the role responsible for maintaining synthesis cadence, enforcing the schema, and ensuring that entries reflect current understanding rather than historical accumulation.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The core pattern (Karpathy, 2026) spread quickly in practice, and within two months Google Cloud engineers had published a file format for it. Measured evidence is still thin. The first tests are 2026 arXiv preprints (Ming et al., 2026; Wang, 2026), and none has a confirmed peer-reviewed venue. The extended framework (Ghumare, 2026) adds significant structural depth, but carries known implementation gaps flagged in community review:

- Confidence scoring lacks a rigorous operational definition
- "Crystallization" (the point at which synthesized knowledge becomes stable) is underspecified
- Automation timelines assume compositional tooling that may not yet exist at scale
- Human-in-the-loop failure modes are not fully addressed

*(Source for limitations: a comment by @gnusupport on the Ghumare gist, April 2026. The account has since been deleted, and a later commenter refers to the comment as gnusupport's critique.)*

These gaps do not invalidate the framework. They define its frontier. The principles are sound; the engineering details require careful, context-specific implementation.

---

## Related concepts

- [Context Engineering](context-engineering.md) — a well-maintained knowledge base is a reusable context asset; synthesis is how it stays useful over time
- [Hallucination](hallucination.md) — synthesis disciplines (contradiction resolution, confidence decay) are responses to hallucination risk in knowledge pipelines
- [Memory (AI Systems)](memory-ai-systems.md) — the memory lifecycle model (working / episodic / semantic / procedural) informs synthesis maintenance cadences
- [Knowledge Base](knowledge-base.md) — the artifact that persistent synthesis produces and maintains
- [Knowledge Graphs](knowledge-graphs.md) — typed relationships turn a wiki into a graph that can be traversed; the LLM-Wiki tests compare against graph-based retrieval
- [Retrieval-Augmented Generation (RAG)](rag.md) — the approach persistent synthesis is usually contrasted with: retrieve raw chunks at question time versus compile them ahead of time
- [Model/Data Drift](model-data-drift.md) — the failure mode that persistent synthesis prevents: gradual divergence between a knowledge system and current reality

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-007 | Karpathy, Andrej — *LLM Wiki* (gist, April 2026) · [link](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Original synthesis philosophy; wiki as compounding artifact; contradictions flagged not accumulated; source docs as inputs, wiki as output. |
| SRC-008 | Ghumare, Rohit — *LLM Wiki v2* (gist, April 2026) · [link](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) | "Stop re-deriving, start compiling"; memory lifecycle tiers; confidence scoring with temporal decay (Ebbinghaus); typed relationships (uses, depends on, contradicts, supersedes); hybrid search (BM25 + vector + graph); schema doc as primary artifact; automation & event hooks; lint/self-healing operation. |
| SRC-009 | @gnusupport — comment on the Ghumare gist (April 14, 2026; account since deleted) · [link](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2) | Implementation limitations: confidence scoring underspecified, crystallization undefined, automation timeline assumptions, HITL failure modes not addressed. |
| SRC-459 | Ming, Haoliang; Li, Feifei; Wu, Xiaoqing; Que, Wenhui — *Retrieval as Reasoning: Self-Evolving Agent-Native Retrieval via LLM-Wiki* (arXiv preprint 2605.25480, 2026) · [link](https://arxiv.org/abs/2605.25480) | First measured test found: documents compiled into linked wiki pages with an Error Book for self-correction; reported gains of 2.0 to 8.1 F1 points over graph-based retrieval on three multi-hop benchmarks. Preprint. |
| SRC-460 | Wang, Ziming — *TOKI: A Bitemporal Operator Algebra for Contradiction Resolution in LLM-Agent Persistent Memory* (arXiv preprint 2606.06240, 2026) · [link](https://arxiv.org/abs/2606.06240) | Four contradiction-resolution strategies used in production memory systems; the case for keeping the losing fact in an audit row. Single-author preprint. |
| SRC-461 | McVeety, Sam; Hormati, Amir (Google Cloud) — *Introducing the Open Knowledge Format* (Google Cloud Blog, June 12, 2026) · [link](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) | Announcement of OKF as a format that formalizes the LLM-wiki pattern; publication date and authors. Vendor source. |
| SRC-462 | Google Cloud — *Open Knowledge Format (OKF)* specification, version 0.2 · [link](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) | Frontmatter fields for sources, verification, lifecycle status and staleness; the stated reason for storing no credibility score; no field for contradictions or successors. Vendor draft. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs knowledge base design for AI systems: how to structure entries, when to deprecate content, how to model relationships between concepts, and what automation is needed for long-term maintenance. |
| **Organizational** | The principle that explains why AI knowledge assets degrade without active maintenance, and what "active maintenance" actually means in practice. |
| **LLM-native** | The operating philosophy of this wiki. Every design decision in this repository reflects the synthesis principle: source documents are inputs; the wiki is the output. |

---

*Last updated: v1.3 · November 2026*
