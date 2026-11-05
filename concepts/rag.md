<!--meta
category: System Architecture
short: A technique that grounds model outputs in retrieved, verifiable information
aliases: [RAG, retrieval augmented generation, search plus generation, document Q&A, grounded retrieval, cache-augmented generation, CAG, preloading the knowledge base]
tags: [Architecture, Data Governance]
established: established
-->
[Applied AI Concepts](../README.md) › [System Architecture](../glossary/categories.md#system-architecture) › Retrieval-Augmented Generation (RAG)

# Retrieval-Augmented Generation (RAG)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
A technique that grounds language model outputs in retrieved, verifiable information, reducing hallucination by giving the model current, specific content to work from.

---

## Technical definition

Retrieval-Augmented Generation (RAG) is an architecture that combines a retrieval system with a language model in a two-stage pipeline. When a query arrives, the retrieval component searches an external knowledge base and selects the most relevant content. That content is injected into the model's context window alongside the original query, giving the model specific, current information to reason from, rather than relying solely on knowledge encoded during training.

Key components:

- **Retrieval layer:** indexes documents as vector embeddings; retrieves semantically similar content at query time using dense or hybrid (keyword + semantic) search
- **Context injection:** retrieved content is placed in the prompt before the model generates a response; how content is structured and ranked here is a context engineering decision
- **Knowledge base:** the document corpus being searched; its quality, currency, and access controls directly determine output quality and safety

RAG addresses two structural limitations of base language models:
1. **Knowledge cutoff:** training data has a fixed end date; the model has no awareness of events or documents after it
2. **Domain specificity:** model weights encode only what was in the training corpus; proprietary, confidential, or specialized documents are absent by default

A structural limitation that compounds both: **temporal ranking blindness**. Vector similarity has no awareness of document freshness or version status. When a knowledge base contains both a document and its superseded replacement, the older version can outrank the newer one, because vector search measures semantic distance, not recency. Three distinct temporal failure modes require different mitigations: *expiration* (documents whose validity has lapsed), *versioning* (superseded documents that coexist with their replacements), and *temporality* (time-bounded content valid only within a specific window). Addressing these requires architectural layers beyond basic retrieval: explicit document validity classification, post-retrieval reranking gated on both freshness and relevance thresholds, and decay profiles calibrated to content type (policy documents decay differently from mathematical reference material).

**When the knowledge base is small, retrieval can be skipped.** Chan et al. (WWW Companion '25) propose **cache-augmented generation (CAG)**: load all the relevant documents into a long-context model in advance, compute the model's internal state for them once (its key-value cache), and answer every question from that cached state with no retrieval step. The approach is meant for knowledge sources *"of limited, manageable size"*, and the authors state that it *"becomes impractical for significantly larger datasets."* On two question-answering benchmarks with an 8-billion-parameter model, it removed retrieval time and scored highest in most of their comparisons against sparse and dense retrieval. They also suggest hybrids that preload a core of documents and retrieve only for edge cases. The trade-off moves rather than disappears. CAG avoids retrieval errors, but it depends on the model using everything in a long context equally well, which is not guaranteed ([context rot](context-rot.md)).

The acronym is sometimes expanded as *context-augmented generation*. That form has no settled meaning in the literature, so this wiki uses the cache-augmented sense.

---

## Plain-language version

Language models know only what they were trained on, which means their knowledge has a cutoff date and doesn't include your organization's internal documents, policies, or current data.

RAG solves this by connecting the model to a searchable knowledge base at the time of the query. Instead of asking the model to recall information from memory, RAG retrieves the relevant documents first and hands them to the model as reading material before it answers.

The result is a model that can reason over your specific information, not just general knowledge baked in during training. But the quality of those answers is only as good as the documents it's working from.

---

## AI literacy notes

RAG is one of the most widely deployed techniques for making language models useful in organizational contexts, because most organizational use cases require domain-specific or current information the model wasn't trained on.

Five things practitioners need to understand:

1. **RAG shifts the quality ceiling to the knowledge base.** A model working from a stale, inconsistent, or poorly organized knowledge base will produce stale, inconsistent, or poorly reasoned outputs. The retrieval architecture doesn't compensate for knowledge base quality. It inherits it.
2. **Retrieval is not search.** Semantic similarity retrieves content that is conceptually related to the query, which is not the same as content that is factually correct or complete. A retrieved chunk can be semantically relevant and still be the wrong answer.
3. **RAG reduces hallucination risk but does not eliminate it.** The model can still misinterpret, misquote, or confabulate based on retrieved content. Human verification remains necessary for consequential outputs.
4. **Temporal blindness is a structural failure mode, not a data quality gap.** Vector search measures angular distance between embeddings. It has no concept of document age or version status. Older documents with strong semantic overlap can consistently outrank their current replacements without any visible signal in the output. This is not solved by better knowledge base hygiene alone; it requires architectural mitigations: temporal reranking layers, explicit document validity metadata (current / expired / time-bounded), and decay profiles calibrated to content type.
5. **Retrieval is a choice, not a requirement.** When a knowledge base is small and stable enough to fit in a model's context, preloading it (cache-augmented generation) removes the retrieval step and its errors. The cost shifts to how well the model uses a long context, and to recomputing the cache whenever the documents change.

---

## Governance notes

**Core question:** Who owns the knowledge base that RAG retrieves from? And is it governed with the same rigor as any other organizational data asset?

**Watch for:**
- Knowledge base treated as set-and-forget: populated once, never updated, with no process for identifying stale or superseded content. RAG makes the knowledge base authoritative; governance must match that authority. **Temporal blindness compounds this**: vector similarity cannot distinguish document versions, so superseded content can outrank current content in retrieval without any visible signal in the output.
- Access controls not applied to retrieved content: if the retrieval system can surface restricted documents to unauthorized users, the RAG architecture becomes a data access bypass. What the model can retrieve is what the user can effectively read.
- Hallucination assumed solved: RAG reduces hallucination risk, it does not eliminate it. Removing verification steps on consequential outputs because "RAG grounds it" is a governance failure mode.
- A whole knowledge base preloaded into context (cache-augmented generation) for users with different permissions. Retrieval can filter documents per user; a shared preloaded cache gives every user's questions access to everything in it. This follows from the mechanism rather than from a reported incident.

**Practice:**
- Treat the knowledge base as a governed data asset: versioned, owned, with a defined update cadence and explicit retirement criteria for outdated content.
- Apply the same access controls to retrieved content that you would apply to direct document access. The retrieval layer is a data access layer, so govern it accordingly.
- If you preload instead of retrieving, build one cache per permission level, and rebuild it whenever the documents change, so the cache is never older than the knowledge base.

**Key accountability owner:** Knowledge base owner, the role responsible for the quality, currency, and access controls of the document corpus the retrieval system draws from.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High.** RAG has a canonical academic origin (Lewis et al., 2020) and is widely deployed in production. The core retrieval-injection-generation pipeline is stable. Implementation patterns (chunking strategies, re-ranking, hybrid search, agentic RAG) are active development areas. **Cache-augmented generation is newer and less tested:** one short conference paper, one 8-billion-parameter model, two question-answering benchmarks, and answers scored by similarity to reference answers. Read it as evidence that retrieval is optional for small knowledge bases, not as a general replacement for RAG.

---

## Related concepts

- [Hallucination](hallucination.md) — RAG's primary motivation; reduces but does not eliminate hallucination risk
- [Context Engineering](context-engineering.md) — RAG is a dynamic context injection strategy; context engineering governs how retrieved content is structured and prioritized within the prompt
- [Persistent Synthesis](persistent-synthesis.md) — the knowledge base RAG retrieves from requires the same maintenance discipline as any managed knowledge system; accumulation without synthesis degrades RAG quality over time
- [Harness Paradigm](harness-paradigm.md) — the retrieval layer, knowledge base access controls, and logging of retrieved content are harness-layer design decisions
- [Grounding](grounding.md) — RAG is the most common technical implementation of grounding in production systems
- [Context Window](context-window.md) — the physical constraint that bounds how much retrieved content can be injected per query, and how large a knowledge base cache-augmented generation can preload
- [Context Rot](context-rot.md) — why a preloaded long context is not used uniformly, the main limit on skipping retrieval
- [Embeddings](embeddings.md) — the representation layer that makes semantic retrieval possible

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401, 2020) · [link](https://arxiv.org/abs/2005.11401) | Canonical paper introducing the RAG architecture: retriever-generator pipeline, dense passage retrieval, knowledge-intensive NLP benchmarks. Foundational definition and architectural framing. |
| SRC-028 | Alexander, Emmimal P. — *RAG Is Blind to Time: I Built a Temporal Layer to Fix It in Production* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/rag-is-blind-to-time-i-built-a-temporal-layer-to-fix-it-in-production/) | Production case study for RAG temporal blindness: vector similarity cannot distinguish document freshness or version status; three temporal failure modes (expiration, versioning, temporality); temporal reranking layer with two-axis document classification (validity states × document kinds); content-specific decay profiles; relevance gating to prevent fresh-but-irrelevant results. |
| SRC-052 | Karunakaran Ponon, Nidhin (Towards Data Science) — *How to Build an Efficient Knowledge Base for AI Models* (2026) · [link](https://towardsdatascience.com/how-to-build-an-efficient-knowledge-base-for-ai-models/) | Access controls on retrieved content and RAG as a data access layer: documents role-based access control applied at the chunk level and metadata-driven retrieval, so the knowledge base is a governed access surface, not a passive store. |
| SRC-025 | DAMA International — *DAMA-DMBOK* (2nd ed., 2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | Knowledge base as a governed data asset: standard data-governance treatment (ownership, quality, access) applies to the retrieval corpus, framing RAG content as a managed asset subject to the same controls as any data store. |
| SRC-458 | Chan, B.J.; Chen, C.-T.; Cheng, J.-H.; Huang, H.-H. — *Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks* (WWW Companion '25, short paper) · [link](https://arxiv.org/abs/2412.15605) | Cache-augmented generation: preload a limited, manageable knowledge base into a long-context model and cache its key-value state, answering without retrieval. On SQuAD and HotPotQA with Llama 3.1 8B, removed retrieval time and scored highest by BERTScore in most comparisons; impractical for significantly larger datasets; suggests preload-plus-retrieval hybrids. |
| SRC-117 | Shi, Kezhan — *10 Common RAG Mistakes We Keep Seeing in Production* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/10-common-rag-mistakes-we-keep-seeing-in-production/) | Production failure taxonomy across four components: document parsing, question interpretation, retrieval mechanisms, and answer generation. Key argument: parsing correctness precedes parameter tuning; structured, typed data flows outperform embedding-only approaches. Grounds the AI literacy note that retrieval is not search, and the governance note that the knowledge base is a governed asset, not a passive store. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core architectural pattern for deploying language models on organizational data. Informs knowledge base design, retrieval strategy, chunking, and re-ranking decisions. |
| **Organizational** | The technique that makes "AI on our documents" feasible, and explains why the quality of those documents determines the quality of AI outputs. Reframes AI adoption as an information architecture problem. |
| **Client-facing** | Answers the question: "can the AI work with our internal information?", and explains what that requires in terms of knowledge base maintenance and access governance. |
| **LLM-native** | A foundational deployment pattern. Understanding RAG is a prerequisite for understanding most production AI systems that go beyond general-purpose chat. |

---

*Last updated: v1.3 · November 2026*
