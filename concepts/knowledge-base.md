<!--meta
category: Knowledge & Memory
short: The collection of documents an AI can look up when answering — the quality of the library determines the quality of the answers
aliases: [document corpus, reference library, the documents it searches, KB, knowledge repository]
tags: [Architecture, Data Governance]
-->
# Knowledge Base

## One-line essence
The collection of documents and information an AI can look up when answering questions — like a reference library it can search. The quality and governance of the library directly determines the quality and trustworthiness of the answers.

---

## Technical definition

A curated, governed collection of documents and structured information made available for an AI system to retrieve at inference time — the retrieval substrate for RAG and grounding. Distinct from model weights (parametric knowledge) and from memory (session-accumulated state): a knowledge base is externally maintained, versionable, and auditable.

The RAG survey literature frames external knowledge quality as the determinant of output quality across the retrieval–generation–augmentation triad (Gao et al.); construction practice covers collection, chunking, vectorization, and storage with iterative refinement; and its governance inherits established data-management discipline (DAMA-DMBOK).

---

## Plain-language version

A knowledge base is the reference library you give the AI — the documents it can look up instead of relying only on what it "remembers" from training. The AI's answers are only as good as the library: outdated, wrong, or missing documents become confident wrong answers.

---

## AI literacy notes

1. **Knowledge-base quality is the ceiling for RAG quality.** Many "hallucinations" trace back to retrieval and content gaps, not the model.
2. **A knowledge base is governable in a way model weights are not.** You can audit it, correct it, version it, and delete from it — which is exactly why regulated deployments lean on retrieval over fine-tuning.
3. **Curation is ongoing, not one-time.** Stale content is a quiet form of drift. And access control matters: whatever is in the knowledge base defines what the AI can expose.

---

## Governance notes

**Core question:** Who curates the knowledge base — and who answers for what's in it?

**Watch for:**
- Stale content silently degrading answers
- Missing provenance — a wrong answer that can't be traced to its source document
- Permissive ingestion exposing sensitive documents through retrieval

**Practice:**
- Assign content ownership and a review cadence per knowledge-base section
- Log retrievals so every answer is traceable to documents

**Key accountability owner:** the data steward / knowledge manager.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** Established concept with mature practice; the AI-specific instantiation (vector stores, RAG substrates) is newer but well-documented.

---

## Related concepts

- [Retrieval-Augmented Generation (RAG)](rag.md) — the mechanism that turns a knowledge base into grounded answers
- [Grounding](grounding.md) — the knowledge base is what outputs are anchored to
- [Data Quality](data-quality.md) — the upstream discipline the knowledge base inherits
- [Memory (AI Systems)](memory-ai-systems.md) — the sibling store: curated reference content vs accumulated operational state
- [Domain](domain.md) — knowledge bases are how generic models acquire domain competence

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) · [link](https://arxiv.org/abs/2005.11401) | Foundational: external knowledge store + retrieval as the mechanism. |
| SRC-138 | Gao, Y. et al. — *Retrieval-Augmented Generation for Large Language Models: A Survey* (arXiv, 2023, rev. 2024; preprint) · [link](https://arxiv.org/abs/2312.10997) | Canonical survey: Naive/Advanced/Modular RAG; external knowledge quality as the determinant of output quality. |
| SRC-052 | Karunakaran Ponon, N. — *How to Build an Efficient Knowledge Base for AI Models* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/how-to-build-an-efficient-knowledge-base-for-ai-models/) | Construction practice: collection, chunking, vectorization, storage, iterative refinement. |
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | The data-management discipline a knowledge base inherits (quality, stewardship, lifecycle). |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The construction pipeline (collection, chunking, vectorization, storage) and retrieval logging are the implementation surface. |
| **Organizational** | The most governable part of an AI system: content ownership and review cadence are assignable in a way model behavior is not. |
| **Client-facing** | Answers "where do the AI's answers come from?" — with document-level traceability when retrieval is logged. |
| **LLM-native** | The practical alternative to fine-tuning for domain knowledge: auditable, correctable, and deletable. |

---

*Last updated: v1.0 · July 2026*
