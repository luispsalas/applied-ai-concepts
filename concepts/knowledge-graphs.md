<!--meta
category: Knowledge & Memory
short: Facts and their relationships stored as an explicit, inspectable network — the retrieval substrate you can audit, as opposed to one you can only measure
aliases: [knowledge graph, graph database, semantic network, ontology, triples, entity relationships, GraphRAG, graph RAG, structured retrieval]
tags: [Architecture, Data Governance]
established: established
-->
# Knowledge Graphs

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Facts and the relationships between them stored as an explicit network of entities and typed links — a retrieval substrate whose contents can be inspected and corrected, rather than one whose behavior can only be measured.

---

## Technical definition

A knowledge graph represents information as **entities** (nodes) joined by **typed, directional relationships** (edges), commonly as subject–predicate–object triples: *`Contract-7` → `governed_by` → `Jurisdiction:Spain`*. Hogan et al. (ACM Computing Surveys, 2021) survey the field: graph data models and query languages, the roles of schema and identity, deductive and inductive knowledge representation, and how graphs are created, enriched, quality-assessed and published.

**The property that matters for AI systems is that the relationships are declared rather than inferred.** This is the direct contrast with [embeddings](embeddings.md), and the two fail in opposite ways:

| | Knowledge graph | Vector retrieval |
|---|---|---|
| Relationship | **Explicit and typed** — you can read it | Implicit — proximity in a learned space |
| Wrong answer | Traceable to a specific triple you can fix | Diffuse; you retune and re-measure |
| Handles | Precision, constraints, multi-hop paths | Fuzzy similarity, unanticipated phrasing |
| Needs | A schema, and effort to build and maintain | A corpus and an embedding model |

**Multi-hop questions are where the difference becomes structural, not stylistic.** *"Which of our suppliers are indirectly exposed to a sanctioned entity?"* is a path traversal — it has an answer the graph can derive and show its working for. Vector search retrieves passages that *resemble* the question, which is a different operation that can be right by luck. Combining the two (commonly *GraphRAG*) is now a standard pattern: the graph supplies structure and constraints, retrieval supplies coverage of things nobody modeled.

**The governance argument, stated plainly:** a knowledge graph is **auditable in a way a vector index is not.** You can ask *why* it returned something and get a path; you can correct a wrong fact by editing one triple; you can attach provenance to an edge and know where a claim came from ([data provenance](data-provenance-lineage.md)). That is a genuine advantage for regulated and high-stakes use — and it is bought with real cost.

**The cost is the reason most projects do not do it.** A graph needs a schema, which means deciding in advance what kinds of things and relationships exist, and it needs continuous maintenance as reality changes. **Its failure mode is silent staleness**: unlike a retrieval index that visibly misses, a graph confidently returns the relationship it was told about, long after that relationship stopped being true.

---

## Plain-language version

Most AI retrieval works by similarity: turn everything into coordinates, find what sits nearest the question. It is fast, needs almost no setup, and copes well with people phrasing things unexpectedly.

A knowledge graph works differently. Instead of "these documents seem related," it stores specific facts and the specific connections between them — *this contract is governed by Spanish law*, *this supplier owns that subsidiary*. Written down, one link at a time.

That costs a lot more. Someone has to decide what kinds of things and connections exist, then keep it current. Which is why most projects reach for the similarity approach first.

Two things make it worth the cost.

**You can follow the chain.** "Which of our suppliers are indirectly connected to a sanctioned company?" is a question about links between links. A graph can walk that path and show you the route. Similarity search finds text that sounds like the question, which is not the same thing and can be accidentally right.

**You can see and fix what it knows.** A wrong answer traces to a specific stated fact you can correct. With similarity search you get a wrong result, adjust settings, and measure again — you cannot point at the mistake.

The catch: a graph will confidently keep telling you something long after it stopped being true. Nothing about a stale fact looks stale.

---

## AI literacy notes

1. **The relationships are declared, not inferred** — which is exactly why they can be audited and corrected.
2. **A wrong answer is traceable to one triple.** With vector retrieval you tune and re-measure; with a graph you fix a fact.
3. **Multi-hop questions are the structural advantage.** Chains of connection are a traversal, not a resemblance.
4. **Its failure mode is silent staleness.** A graph returns yesterday's relationship as confidently as today's, and nothing in the answer signals age.
5. **The schema is a modeling commitment**, made in advance — it decides what questions are even askable.
6. **Graphs and vectors are complements, not rivals.** Structure and constraints from one, coverage of the unmodeled from the other.
7. **Provenance attaches naturally to an edge**, which makes "where did this claim come from?" answerable rather than aspirational.
8. **Build cost is the real barrier**, and it is ongoing rather than one-off.

---

## Governance notes

**Core question:** For the facts this system reasons over, can we say where each one came from, when it was last confirmed, and who is responsible for it still being true?

**Watch for:**
- A graph built once for a project and never given a maintenance owner — the silent-staleness path
- No provenance on edges, so a wrong answer cannot be traced past "the graph said so" ([data provenance](data-provenance-lineage.md))
- Schema decisions made by whoever was building, encoding contestable definitions as structure
- Graph output treated as ground truth because it is structured, when it is only as current as its last update
- Vector retrieval chosen by default for a precision or constraint problem it cannot express ([RAG](rag.md))
- No freshness signal, so consumers cannot distinguish a confirmed fact from a stale one
- Access control applied at the document layer but not to the graph derived from it ([permission model](permission-model-ai.md))
- Inferred edges stored indistinguishably from asserted ones, so derived claims look like stated facts

**Practice:**
- **Attach provenance and a last-confirmed date to edges, not just to nodes** — the relationship is the claim, and it is what goes stale
- Name a maintenance owner at build time; a graph without one degrades invisibly ([continuous feedback & improvement](continuous-feedback-improvement.md))
- **Distinguish asserted from inferred edges** so derived conclusions can be re-derived rather than trusted
- Treat the schema as a governed artifact with a change process — it encodes definitions the organization is committing to
- Use the graph for precision, constraints and traversal; use retrieval for coverage. Choosing one for the other's job is the common design error
- Enforce source-document permissions on the derived graph, not only on the source
- Expose the path behind an answer where the answer matters — the auditability is the point, and it is wasted if unsurfaced

**Key accountability owner:** the owner of the underlying business facts — supplier relationships, contract terms, org structure — not the team that built the graph, because staleness is a domain fact going out of date, and only that owner will notice.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the technology, medium on the AI application.** Knowledge graphs are a mature field with a peer-reviewed survey in ACM Computing Surveys and decades of production use at scale. **The LLM-grounding application is younger and moves faster:** graph-augmented retrieval is an active pattern rather than a settled architecture, published comparisons against vector RAG are mostly vendor-authored or benchmark-specific, and **there is no reliable general answer to when a graph earns its build cost over plain retrieval** — that remains a judgment about the question types a system must answer. The auditability advantage is structural and not in dispute; claims about accuracy improvements from graph augmentation should be read as workload-specific.

---

## Related concepts

- [Knowledge Base](knowledge-base.md) — the broader container; a graph is one way to structure it
- [RAG (Retrieval-Augmented Generation)](rag.md) — the retrieval architecture a graph augments or replaces
- [Embeddings](embeddings.md) — the contrast: proximity in a learned space versus declared, typed relationships
- [Grounding](grounding.md) — what both approaches exist to serve
- [Data Provenance & Lineage](data-provenance-lineage.md) — attaches naturally to edges, which is much of the value
- [Data Quality](data-quality.md) — a graph's usefulness is bounded by the correctness of its assertions
- [Explainability (XAI)](explainability-xai.md) — a traversal path is a genuine account of *why*, unlike a similarity score
- [Continuous Feedback & Improvement](continuous-feedback-improvement.md) — the loop that keeps a graph from going quietly stale
- [Permission Model (AI)](permission-model-ai.md) — derived structures need the source's access rules

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-241 | Hogan, A.; Blomqvist, E.; Cochez, M.; d'Amato, C.; de Melo, G.; Gutiérrez, C.; Navigli, R.; Staab, S. et al. — *Knowledge Graphs* (ACM Computing Surveys 54(4), 2021) · [link](https://arxiv.org/abs/2003.02320) | The definitional anchor: graph data models and query languages, schema and identity, deductive and inductive representation, and graph creation, enrichment, quality assessment and publication. |
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) · [link](https://arxiv.org/abs/2005.11401) | The retrieval architecture a graph is an alternative substrate for, and the baseline the comparison in this entry is drawn against. |
| SRC-224 | Mikolov, T.; Chen, K.; Corrado, G.; Dean, J. (Google) — *Efficient Estimation of Word Representations in Vector Space* (2013) · [link](https://arxiv.org/abs/1301.3781) | The representation the contrast turns on: meaning as position in a learned space, where relationships are implicit rather than declared. |
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | Stewardship and ownership of the underlying facts — the maintenance discipline without which a graph goes silently stale. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Use graphs for precision, constraints and traversal; use retrieval for coverage. Attach provenance and a last-confirmed date to edges, and keep asserted and inferred edges distinguishable. |
| **Organizational** | The auditability is the reason to pay the build cost — a wrong answer traces to one correctable fact. Name a maintenance owner at build time or it degrades invisibly. |
| **Client-facing** | Explains how a system can show *why* it reached an answer, and what keeping that capability accurate requires. |
| **LLM-native** | Declared relationships versus learned proximity, failing in opposite ways. The graph's failure mode is confident staleness, which nothing in the output signals. |

---

*Last updated: v1.0 · September 2026*
