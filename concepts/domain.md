<!--meta
category: Knowledge & Memory
short: The specific field the AI is working in — what counts as a "good" or "wrong" answer depends entirely on the domain
aliases: [subject area, field, vertical, domain expertise, what counts as a good answer here]
tags: [Data Governance]
established: established
-->
# Domain

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The specific field or world the AI is working in — healthcare, legal, finance, architecture. What counts as a "good" or "wrong" answer depends entirely on the domain.

---

## Technical definition

The bounded field of knowledge, practice, and standards within which an AI system operates — determining terminology, valid reasoning patterns, quality criteria, and error severity. Domain conditions everything downstream: data semantics and stewardship (the data-domain framing of DAMA-DMBOK), evaluation validity (HELM's scenario-based evaluation shows model performance is domain- and scenario-specific and does not transfer), and adaptation strategy — the domain-specialization literature taxonomizes how general-purpose models are adapted to fields where they underperform: external augmentation (retrieval), prompting, and fine-tuning (Ling et al.).

---

## Plain-language version

The domain is the world the AI works in — medicine, law, music, finance. The same answer can be brilliant in one domain and dangerous in another; what "correct" means, and how bad a mistake is, depends entirely on the field.

---

## AI literacy notes

1. **Model performance does not transfer across domains.** A benchmark score in one field says little about yours — evaluation has to happen in-domain (HELM).
2. **Domain expertise is what makes evaluation possible.** Only someone who knows the field can judge whether the output is actually right. High-stakes domains (health, legal, finance) also carry their own regulatory overlays on top of AI rules.
3. **The standard adaptation pattern is generic model plus domain context.** Retrieval (RAG), fine-tuning, and curated knowledge bases are the three main routes for making a general-purpose model domain-competent.

---

## Governance notes

**Core question:** Who holds the domain expertise needed to judge the AI's output?

**Watch for:**
- Cross-domain reuse without revalidation
- Evaluation performed by people without domain expertise
- Domain-specific regulation missed because the system is framed as "generic"

**Practice:**
- Name the domain(s) in every use-case record
- Require domain-expert review in evaluation loops

**Key accountability owner:** the domain lead / subject-matter expert.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High (concept) / Medium-High (AI framing).** The concept is long-established in knowledge and data management. Domain-dependence of LLM performance is well-evidenced (HELM) and the domain-specialization literature now provides a systematic treatment, though the term still has no formal AI definition.

---

## Related concepts

- [AI Use Case](ai-use-case.md) — every use case lives in a domain that sets its quality criteria and error severity
- [Evaluation (AI Systems)](evaluation.md) — evaluation validity is domain-bound: scores do not transfer across fields
- [AI Literacy](ai-literacy.md) — domain experts are the indispensable judges of AI output in their field
- [Knowledge Base](knowledge-base.md) — the curated route for giving a generic model domain competence
- [Grounding](grounding.md) — grounding sources are domain artifacts; their authority is domain-defined

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | Data-domain framing: domains define semantics, stewardship, and quality standards. |
| SRC-065 | Liang, P. et al. — *Holistic Evaluation of Language Models (HELM)* (Stanford CRFM, 2023) · [link](https://arxiv.org/abs/2211.09110) | Scenario-based evaluation: performance is domain/scenario-specific and does not transfer. |
| SRC-136 | Ling, C. et al. — *Domain Specialization as the Key to Make Large Language Models Disruptive: A Comprehensive Survey* (arXiv, 2023, rev. 2024; preprint) · [link](https://arxiv.org/abs/2305.18703) | Taxonomy of domain-adaptation techniques: external augmentation, prompting, fine-tuning. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Adaptation strategy (RAG vs fine-tuning vs prompting) and evaluation design are domain decisions before they are technical ones. |
| **Organizational** | Explains why "it worked for them" doesn't transfer — and why domain experts belong in every AI evaluation loop. |
| **Client-facing** | Answers "does this AI know our field?" — the honest answer depends on what domain context it was given. |
| **LLM-native** | General-purpose models make domain framing more important, not less: capability breadth without domain grounding produces confident out-of-field errors. |

---

*Last updated: v1.0 · July 2026*
