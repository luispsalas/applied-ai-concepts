<!--meta
category: Knowledge & Memory
short: How an AI remembers — what it keeps in a conversation, what carries over to future sessions, and what it reuses as learned skill
aliases: [does it remember me, conversation history, persistence, session memory, long-term memory]
-->
# Memory (AI Systems)

## One-line essence
How an AI remembers things — what it keeps during a conversation, what carries over to future sessions, and what it can reuse as a learned skill.

---

## Technical definition

Mechanisms by which an AI system retains and reuses information beyond a single model call. The survey literature distinguishes in-trial memory (within a task or session — the context window) from cross-trial memory (persisting across sessions), and analyzes memory by its sources, forms, and operations — what is stored, in what representation, and how it is written, read, and forgotten (Zhang et al.).

In practice this spans in-context/session memory, persistent memory (files, databases, learned preferences), and externalized state (file-system-as-memory patterns). Memory failure is a leading cause of enterprise agent failure — systems that don't retain learning repeat their errors — and unmanaged memory growth also degrades retrieval precision without a management layer. Distinct from a knowledge base (curated reference content): memory is accumulated operational state.

---

## Plain-language version

Memory is what the AI keeps: what it holds during one conversation, what carries over to the next, and what it learns about how you work. Without memory it starts from zero every time; with it, corrections compound into something useful — but errors and sensitive data can compound the same way.

---

## AI literacy notes

1. **The context window is not memory.** In-session recall is ephemeral and degrades as the window fills (context rot). Anything that must survive the session needs an explicit persistence mechanism.
2. **Persistent memory is where privacy risk concentrates.** What is remembered, for how long, and who can see it are governance questions, not implementation details.
3. **Memory compounds errors as easily as learning.** A wrong "lesson" persists until corrected. Externalized memory (files, logs, state documents) is inspectable and auditable; hidden memory is neither.

---

## Governance notes

**Core question:** What is this system allowed to remember — and who can inspect or erase it?

**Watch for:**
- Sensitive data persisting in memory beyond its lawful or intended lifetime
- Wrong "learnings" compounding across sessions
- Memory stores that sit outside the audit trail

**Practice:**
- Define retention and erasure rules per memory type
- Keep persistent memory in inspectable, versioned stores

**Key accountability owner:** the system owner, with privacy officer sign-off.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** Rapidly evolving architecture area; a reference survey (Zhang et al. 2024) is consolidating the space (in-trial vs cross-trial; sources/forms/operations), but patterns are far from standardized.

---

## Related concepts

- [Context Engineering](context-engineering.md) — deciding what enters the window each turn is memory management in practice
- [Knowledge Base](knowledge-base.md) — the sibling store: curated reference content vs accumulated operational state
- [Persistent Synthesis](persistent-synthesis.md) — the discipline of making cross-session memory compound instead of accumulate
- [Audit Trail (AI)](audit-trail-ai.md) — memory stores belong inside the auditable record, not outside it
- [Retrieval-Augmented Generation (RAG)](rag.md) — retrieval quality degrades as unmanaged memory grows

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-137 | Zhang, Z. et al. — *A Survey on the Memory Mechanism of Large Language Model based Agents* (arXiv, 2024; preprint) · [link](https://arxiv.org/abs/2404.13501) | Reference survey: in-trial vs cross-trial memory; memory sources, forms, and operations; evaluation methods. |
| SRC-050 | Xu, X. et al. — *Everything is Context: Agentic File System Abstraction for Context Engineering* (CSIRO/ArcBlock, 2025) · [link](https://arxiv.org/abs/2512.05470) | Externalized file-system state as agent memory. |
| SRC-079 | Plumb, T. — *Enterprise AI Agents Keep Failing Because They Forget What They Learned* (VentureBeat, 2026) · [link](https://venturebeat.com/orchestration/enterprise-ai-agents-keep-failing-because-they-forget-what-they-learned) | Memory loss as a leading enterprise agent failure mode. |
| SRC-064 | Alexander, E.P. — *Your RAG Gets Confidently Wrong as Memory Grows* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/your-rag-gets-confidently-wrong-as-memory-grows-i-built-the-memory-layer-that-stops-it/) | Unmanaged memory growth degrades accuracy; the case for a memory-management layer. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Memory architecture (session vs persistent vs externalized) and retention/erasure rules are design decisions with governance consequences. |
| **Organizational** | Where AI privacy exposure concentrates: what systems remember about people and processes must be inventoried and owned. |
| **Client-facing** | Answers "what does it remember about me?" — and whether that memory can be inspected and erased. |
| **LLM-native** | The difference between a tool and a collaborator: memory is what lets corrections compound — for better and worse. |

---

*Last updated: v1.0 · July 2026*
