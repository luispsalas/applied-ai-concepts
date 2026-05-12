# Retrieval-Augmented Generation (RAG)

## One-line essence
A technique that grounds language model outputs in retrieved, verifiable information — reducing hallucination by giving the model current, specific content to work from.

---

## Technical definition

Retrieval-Augmented Generation (RAG) is an architecture that combines a retrieval system with a language model in a two-stage pipeline. When a query arrives, the retrieval component searches an external knowledge base and selects the most relevant content. That content is injected into the model's context window alongside the original query, giving the model specific, current information to reason from — rather than relying solely on knowledge encoded during training.

Key components:

- **Retrieval layer** — indexes documents as vector embeddings; retrieves semantically similar content at query time using dense or hybrid (keyword + semantic) search
- **Context injection** — retrieved content is placed in the prompt before the model generates a response; how content is structured and ranked here is a context engineering decision
- **Knowledge base** — the document corpus being searched; its quality, currency, and access controls directly determine output quality and safety

RAG addresses two structural limitations of base language models:
1. **Knowledge cutoff** — training data has a fixed end date; the model has no awareness of events or documents after it
2. **Domain specificity** — model weights encode only what was in the training corpus; proprietary, confidential, or specialized documents are absent by default

A structural limitation that compounds both: **temporal ranking blindness**. Vector similarity has no awareness of document freshness or version status. When a knowledge base contains both a document and its superseded replacement, the older version can outrank the newer one — because vector search measures semantic distance, not recency. Three distinct temporal failure modes require different mitigations: *expiration* (documents whose validity has lapsed), *versioning* (superseded documents that coexist with their replacements), and *temporality* (time-bounded content valid only within a specific window). Addressing these requires architectural layers beyond basic retrieval: explicit document validity classification, post-retrieval reranking gated on both freshness and relevance thresholds, and decay profiles calibrated to content type (policy documents decay differently from mathematical reference material).

---

## Plain-language version

Language models know only what they were trained on — which means their knowledge has a cutoff date and doesn't include your organization's internal documents, policies, or current data.

RAG solves this by connecting the model to a searchable knowledge base at the time of the query. Instead of asking the model to recall information from memory, RAG retrieves the relevant documents first and hands them to the model as reading material before it answers.

The result is a model that can reason over your specific information — not just general knowledge baked in during training. But the quality of those answers is only as good as the documents it's working from.

---

## AI literacy notes

RAG is one of the most widely deployed techniques for making language models useful in organizational contexts — because most organizational use cases require domain-specific or current information the model wasn't trained on.

Three things practitioners need to understand:

1. **RAG shifts the quality ceiling to the knowledge base.** A model working from a stale, inconsistent, or poorly organized knowledge base will produce stale, inconsistent, or poorly reasoned outputs. The retrieval architecture doesn't compensate for knowledge base quality — it inherits it.
2. **Retrieval is not search.** Semantic similarity retrieves content that is conceptually related to the query — which is not the same as content that is factually correct or complete. A retrieved chunk can be semantically relevant and still be the wrong answer.
3. **RAG reduces hallucination risk but does not eliminate it.** The model can still misinterpret, misquote, or confabulate based on retrieved content. Human verification remains necessary for consequential outputs.
4. **Temporal blindness is a structural failure mode, not a data quality gap.** Vector search measures angular distance between embeddings — it has no concept of document age or version status. Older documents with strong semantic overlap can consistently outrank their current replacements without any visible signal in the output. This is not solved by better knowledge base hygiene alone; it requires architectural mitigations: temporal reranking layers, explicit document validity metadata (current / expired / time-bounded), and decay profiles calibrated to content type.

---

## Governance notes

**Core question:** Who owns the knowledge base that RAG retrieves from — and is it governed with the same rigor as any other organizational data asset?

**Watch for:**
- Knowledge base treated as set-and-forget: populated once, never updated, with no process for identifying stale or superseded content. RAG makes the knowledge base authoritative; governance must match that authority. **Temporal blindness compounds this**: vector similarity cannot distinguish document versions, so superseded content can outrank current content in retrieval without any visible signal in the output.
- Access controls not applied to retrieved content: if the retrieval system can surface restricted documents to unauthorized users, the RAG architecture becomes a data access bypass. What the model can retrieve is what the user can effectively read.
- Hallucination assumed solved: RAG reduces hallucination risk, it does not eliminate it. Removing verification steps on consequential outputs because "RAG grounds it" is a governance failure mode.

**Practice:**
- Treat the knowledge base as a governed data asset: versioned, owned, with a defined update cadence and explicit retirement criteria for outdated content.
- Apply the same access controls to retrieved content that you would apply to direct document access. The retrieval layer is a data access layer — govern it accordingly.

**Key accountability owner:** Knowledge base owner — the role responsible for the quality, currency, and access controls of the document corpus the retrieval system draws from.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** RAG has a canonical academic origin (Lewis et al., 2020) and is widely deployed in production. The core retrieval-injection-generation pipeline is stable. Implementation patterns — chunking strategies, re-ranking, hybrid search, agentic RAG — are active development areas.

---

## Related concepts

- [Hallucination](hallucination.md) — RAG's primary motivation; reduces but does not eliminate hallucination risk
- [Context Engineering](context-engineering.md) — RAG is a dynamic context injection strategy; context engineering governs how retrieved content is structured and prioritized within the prompt
- [Persistent Synthesis](persistent-synthesis.md) — the knowledge base RAG retrieves from requires the same maintenance discipline as any managed knowledge system; accumulation without synthesis degrades RAG quality over time
- [Harness Paradigm](harness-paradigm.md) — the retrieval layer, knowledge base access controls, and logging of retrieved content are harness-layer design decisions
- Grounding — RAG is the most common technical implementation of grounding in production systems
- Context Window — the physical constraint that bounds how much retrieved content can be injected per query
- Vector Embeddings — the representation layer that makes semantic retrieval possible

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401, 2020) · [link](https://arxiv.org/abs/2005.11401) | Canonical paper introducing the RAG architecture: retriever-generator pipeline, dense passage retrieval, knowledge-intensive NLP benchmarks. Foundational definition and architectural framing. |
| SRC-028 | Alexander, Emmimal P. — *RAG Is Blind to Time: I Built a Temporal Layer to Fix It in Production* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/rag-is-blind-to-time-i-built-a-temporal-layer-to-fix-it-in-production/) | Production case study for RAG temporal blindness: vector similarity cannot distinguish document freshness or version status; three temporal failure modes (expiration, versioning, temporality); temporal reranking layer with two-axis document classification (validity states × document kinds); content-specific decay profiles; relevance gating to prevent fresh-but-irrelevant results. |
| — | ⚠️ Source needed | Governance framing: knowledge base as a governed data asset; access controls on retrieved content; RAG as a data access layer. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core architectural pattern for deploying language models on organizational data. Informs knowledge base design, retrieval strategy, chunking, and re-ranking decisions. |
| **Organizational** | The technique that makes "AI on our documents" feasible — and explains why the quality of those documents determines the quality of AI outputs. Reframes AI adoption as an information architecture problem. |
| **Client-facing** | Answers the question: "can the AI work with our internal information?" — and explains what that requires in terms of knowledge base maintenance and access governance. |
| **LLM-native** | A foundational deployment pattern. Understanding RAG is a prerequisite for understanding most production AI systems that go beyond general-purpose chat. |

---

*Last updated: v1.1 · May 2026*
