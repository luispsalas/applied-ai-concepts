<!--meta
category: Knowledge & Memory
short: Everything the model receives before it answers — one bounded, undifferentiated stream, assembled fresh every time
aliases: [context window contents, what the model sees, input context, the prompt plus everything else, what does it actually know]
-->
# Context (AI Systems)

## One-line essence
Everything an AI model receives before generating a response — the information, instructions, and framing that shape every output it produces.

---

## Technical definition

The complete input a model conditions on for a single generation. Not just the user's message: the [system prompt](system-prompt.md), conversation history, retrieved documents, tool definitions and tool results, file contents, and any scaffolding the application inserts. All of it arrives as one sequence, and the model has no way to distinguish "instructions from the operator" from "text pasted by a user" from "content returned by a tool" except by what the surrounding text implies.

**That indistinguishability is the entry's most consequential fact.** It is the reason [prompt injection](prompt-injection.md) works at all: content that entered as data occupies the same channel as content that entered as instruction. Context is not a container with compartments; it is a single stream with conventions layered on top.

Three properties govern what context can do:

- **It is bounded.** The [context window](context-window.md) is a hard limit. Everything competes for the same finite budget, so including one thing means excluding another — context is an allocation problem, not a storage problem.
- **Position matters, and not linearly.** Model performance degrades on information placed in the *middle* of a long input relative to the beginning or end, and the degradation grows with length. Where something sits changes whether it is used.
- **It does not persist.** Each generation starts from whatever was assembled for it. Apparent [memory](memory-ai-systems.md) is context being reconstructed and re-sent, which is why "it forgot" is usually "it was not included this time."

**Context is the layer most under your control.** The model's weights are fixed; the [prompt](prompt-engineering.md) is one part of the input; but *what gets assembled into the window* is an engineering and governance decision made by the application on every request. That is why [context engineering](context-engineering.md) exists as a discipline — this entry is the object, that one is the practice.

---

## Plain-language version

An AI model has no background knowledge of your situation and no memory of yesterday. Everything it knows about *your* problem, at the moment it answers, is whatever was placed in front of it — your question, plus whatever the surrounding system decided to include: earlier messages, documents it looked up, instructions the vendor or your organization set, results from tools it called.

That bundle is the context. It is assembled fresh for every single response, it has a size limit, and things placed in the middle of a long one get used less reliably than things at either end.

The practical consequence is that most disappointing AI output is a context problem rather than a model problem. The system did not fail to reason; it reasoned about the wrong material, or about material that was missing something you assumed was obvious. And because the model cannot tell instructions apart from content, anything that reaches the context can influence the answer — including text from a document nobody read closely.

---

## AI literacy notes

1. **The model knows only what is in the window.** Not your organization, not last week's conversation, not the document you meant to attach. Unstated context is absent context, and the model will fill the gap rather than flag it.
2. **You are usually not seeing all of it.** System prompts, retrieved passages and tool results are typically invisible in the interface. The context that produced an answer is generally larger than what is on screen.
3. **Everything competes for the same budget.** Adding a long document may push out earlier instructions. More context is not monotonically better — beyond a point it displaces what mattered.
4. **Position affects use.** Material buried in the middle of a long input is used less reliably than material at the start or end. If something is critical, placement is a real lever.
5. **The model cannot tell instruction from data.** This is a structural property, not an oversight. It is why a document, a web page, or a tool result can change behavior, and why "just tell it to ignore untrusted content" is not a control.
6. **"It forgot" almost always means "it was not re-sent."** Context resets each turn; continuity is something the surrounding system manufactures.
7. **The most common fix for bad output is better context, not a better model.** Missing constraints, absent examples, unstated audience, no source material. Reach for that before concluding the model is inadequate.

---

## Governance notes

**Core question:** For any given response, could you reconstruct exactly what the model received — and does anything untrusted reach that window?

**Watch for:**
- No record of assembled context, so an output cannot be explained after the fact — the [audit trail](audit-trail-ai.md) logs the answer but not the input that produced it
- Untrusted content (user uploads, scraped pages, tool results, email bodies) entering the window with no separation from operator instructions
- Sensitive data pulled into context because retrieval was scoped generously and nobody checked what was reachable ([data minimization](data-minimization.md), [privacy](privacy-ai-systems.md))
- Context assembly logic that no one owns — accreted across features, with no single place that decides what goes in
- Silent truncation: input exceeding the window and being dropped without a signal to the user or the log
- Assumptions about persistence — features built as if the system remembers, when continuity is being re-sent each time

**Practice:**
- Log what was actually assembled, not just the user's message, at least to a level that allows reconstruction ([observability](observability.md))
- Treat everything that enters the window as untrusted unless you placed it there, and design assuming it may attempt to instruct
- Scope retrieval to the requester's entitlements — context is where an access-control failure becomes a disclosure
- Make truncation explicit and observable rather than silent
- Name an owner for context assembly, since it is a design surface with real risk and it otherwise belongs to nobody
- Put critical constraints where they are used reliably, and re-state them near the end of long inputs rather than assuming placement is neutral

**Key accountability owner:** the system owner, specifically for what the assembly layer is permitted to pull in — because retrieval scope and untrusted-content handling are both decided there, not in the model.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanism is architectural and not in dispute: transformer models condition on a bounded token sequence, and the instruction/data indistinguishability follows directly from that. The positional-degradation finding is peer-reviewed and replicated. **Lower on practice:** how to allocate a limited window well is an active engineering area with strong vendor-published heuristics and little independent comparative evidence — the practitioner guidance here is convergent industry experience, not settled method.

---

## Related concepts

- [Context Engineering](context-engineering.md) — the practice of deciding what goes into the window; this entry is the object it acts on
- [Context Window](context-window.md) — the hard limit that makes context an allocation problem
- [System Prompt](system-prompt.md) — operator instructions, occupying the same stream as everything else
- [Prompt Engineering](prompt-engineering.md) — shaping one component of the context rather than the whole
- [Prompt Injection](prompt-injection.md) — the attack that exists because instruction and data share a channel
- [Memory (AI Systems)](memory-ai-systems.md) — how continuity is manufactured across a stateless boundary
- [Grounding](grounding.md) — putting verifiable source material into the context on purpose
- [Retrieval-Augmented Generation (RAG)](rag.md) — the dominant mechanism for assembling context from a corpus
- [Tool Use](tool-use.md) — tool results are context, and arrive from outside your control
- [Data Minimization](data-minimization.md) — what should *not* reach the window
- [Audit Trail (AI)](audit-trail-ai.md) — an output is only explainable if its input was recorded
- [Hallucination](hallucination.md) — what tends to fill an unstated gap
- [Curse of Knowledge (AI Context)](curse-of-knowledge-ai-context.md) — why the missing piece is usually the thing that seemed too obvious to say

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-149 | Liu, N.F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; Liang, P. — *Lost in the Middle: How Language Models Use Long Contexts* (2023) · [link](https://arxiv.org/abs/2307.03172) | That position within the context changes whether information is used — middle-of-input degradation, worsening with length. The basis for treating placement as a design lever. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (2017) · [link](https://arxiv.org/abs/1706.03762) | The architecture that makes context a single bounded sequence rather than a structured input with compartments. |
| SRC-069 | Anthropic — *Effective Context Engineering for AI Agents* (2025) · [link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | Context as a finite budget to be allocated, and the practitioner framing of assembly as the primary design surface. ⚠️ Vendor-produced — background reference for technique, not independent authority. |
| SRC-070 | Manus — *Context Engineering for AI Agents: Lessons from Building Manus* (2025) · [link](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus) | Production experience of context assembly and its failure modes in a long-running agent. ⚠️ Vendor-produced. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. (Renmin University + multi-institution) — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Where conditioning-on-input sits in the broader model lifecycle, and the vocabulary used consistently across this wiki. |
| SRC-146 | Greshake, K.; Abdelnabi, S.; Mishra, S.; Endres, C.; Holz, T.; Fritz, M. — *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023) · [link](https://arxiv.org/abs/2302.12173) | That content entering context as data can act as instruction — the security consequence of a single undifferentiated stream. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Context assembly is the design surface you actually control. Log it, scope retrieval to entitlements, make truncation visible, and treat placement as a parameter. |
| **Organizational** | Most disappointing output is a context failure, not a model failure — and context is also where an access-control mistake becomes a data disclosure. It needs a named owner. |
| **Client-facing** | Explains why AI systems need the right material supplied and why they cannot draw on things nobody gave them. |
| **LLM-native** | One bounded stream with no type system: instructions, data and tool results are indistinguishable to the model, and everything competes for the same budget. |

---

*Last updated: v1.0 · August 2026*
