# Grounding

## One-line essence
Anchoring model outputs to specific, verifiable sources — reducing hallucination by giving the model something real to reason from.

---

## Technical definition

Grounding is the practice of connecting a language model's outputs to external, verifiable information sources rather than allowing the model to generate from training knowledge alone. It is not a single technique but a family of approaches with different mechanisms and different failure modes:

1. **Context grounding** — verified content is placed in the model's context window before generation. The model reasons from the provided material rather than recalling from weights. Retrieval-Augmented Generation (RAG) is the most common implementation: a retrieval system selects relevant documents and injects them into the prompt. Grounding and RAG are not synonyms — RAG is one grounding mechanism; grounding is the broader practice.
2. **Tool grounding** — the model is given access to external tools (search, calculators, databases, APIs) that it can invoke during generation to verify or supplement its outputs. Reduces reliance on static training knowledge for time-sensitive or domain-specific queries.
3. **Source attribution** — the model is required to cite the specific source for each claim in its output. Forces the model to connect assertions to retrievable material; makes ungrounded claims visible.

**Grounding reduces hallucination risk but does not eliminate it.** Three failure modes survive grounding:
- **Source hallucination**: the model generates a plausible-sounding citation that does not exist — or misrepresents a real source. Citation presence is not citation accuracy.
- **Context override**: the model's training priors override the provided context when they conflict — the model generates from memory rather than from the material in front of it. Empirical evidence shows models frequently fail to use retrieved documents when those documents contradict training-encoded beliefs.
- **Stale grounding**: the knowledge base or retrieved material is outdated, superseded, or contains versioning conflicts. The model reasons correctly from incorrect inputs. RAG's temporal blindness (vector similarity has no awareness of document freshness) makes this failure mode systematic rather than incidental.

---

## Plain-language version

Grounding is what you do when you don't want the AI to make things up — you give it material to work from and require it to use that material rather than relying on its training.

The clearest example: instead of asking an AI model what your company's refund policy is (and getting a plausible but potentially invented answer), you retrieve the actual policy document and give it to the model as reading material before it answers.

The model is still the one generating language. Grounding changes what it is generating language about — specific, verifiable content rather than recalled patterns.

---

## AI literacy notes

Grounding is widely misunderstood as a solution to hallucination rather than a mitigation. The distinction matters operationally.

Three things practitioners need to understand:

1. **RAG is one grounding strategy, not the definition of grounding.** RAG grounds through retrieval and injection; tool use grounds through real-time external calls; structured prompting with provided documents also grounds. Treating these as interchangeable obscures when each is appropriate and what each leaves unaddressed.
2. **Source attribution creates accountability pressure, not accuracy guarantees.** Requiring the model to cite sources forces grounded claims — but does not prevent source hallucination (invented citations) or source misrepresentation (real citations, misquoted content). Source attribution is an accountability mechanism, not a verification substitute.
3. **Models trained on internet-scale data have strong priors that can override retrieved content.** When retrieved documents contradict training-encoded beliefs, models frequently default to their priors. This is not a retrieval failure — it is a generation failure. Grounding strategies must be designed with this in mind: retrieved content may need to be explicitly framed as authoritative and the model instructed to defer to it.

---

## Governance notes

**Core question:** When AI systems produce outputs grounded in retrieved content, who is responsible for the quality, currency, and access controls of the material being retrieved?

**Watch for:**
- Grounding treated as a technical fix rather than a governance dependency. A grounded AI system is only as reliable as the sources it is grounded in. Stale, inconsistent, or poorly governed knowledge bases produce stale, inconsistent, or poorly governed outputs — with a veneer of citation that can make them harder to question.
- Source attribution used as a quality signal without verification. The presence of a citation does not confirm the citation is real, accurate, or correctly quoted. Treating cited outputs as verified outputs is a governance failure mode.
- Access controls not applied to retrieved content. If the grounding layer can surface restricted documents to unauthorized users, it functions as a data access bypass. What the model can retrieve is what the user can effectively read.

**Practice:**
- Govern the grounding layer as a data asset: the knowledge base or retrieval corpus must have a named owner, a defined update cadence, explicit retirement criteria for outdated content, and access controls that match direct document access.
- Require citation verification on consequential outputs: source attribution establishes accountability pressure; a spot-check process confirms citation accuracy.

**Key accountability owner:** Knowledge base owner — the role responsible for the quality, currency, and access governance of the material the grounding layer retrieves from.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established, active.** Context grounding and RAG-based approaches are widely deployed and well-documented. The failure modes — source hallucination, context override, stale grounding — are empirically documented. Tool grounding and multi-step agentic grounding are active development areas. The distinction between grounding as a practice and RAG as one implementation is underappreciated in practitioner literature and warrants continued emphasis.

---

## Related concepts

- [Retrieval-Augmented Generation (RAG)](rag.md) — the most widely deployed grounding implementation; RAG is one grounding mechanism, not grounding itself
- [Hallucination](hallucination.md) — grounding's primary motivation; reduces but does not eliminate hallucination risk
- [Context Engineering](context-engineering.md) — grounding decisions are context engineering decisions: what to retrieve, how to structure it, how to frame its authority to the model
- [Harness Paradigm](harness-paradigm.md) — grounding infrastructure (retrieval layer, knowledge base access, citation logging) is implemented at the harness layer
- [Observability](observability.md) — grounding makes outputs attributable; observability makes that attribution auditable
- [Persistent Synthesis](persistent-synthesis.md) — the knowledge base a grounding system retrieves from requires the same synthesis discipline as any managed knowledge system

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (arXiv:2005.11401, 2020) · [link](https://arxiv.org/abs/2005.11401) | Canonical RAG architecture as grounding implementation: retriever-generator pipeline, dense passage retrieval, knowledge-grounding for NLP tasks. Defines the mechanism underpinning context grounding. |
| SRC-028 | Alexander, Emmimal P. — *RAG Is Blind to Time: I Built a Temporal Layer to Fix It in Production* (Towards Data Science, 2026) · [link](https://towardsdatascience.com/rag-is-blind-to-time-i-built-a-temporal-layer-to-fix-it-in-production/) | Stale grounding as a systematic failure mode: vector similarity cannot distinguish document freshness; three temporal failure modes (expiration, versioning, temporality); production mitigations. |
| SRC-066 | Yoran, O. et al. — *Making Retrieval-Augmented Language Models Robust to Irrelevant Context* (ICLR, 2024) · [link](https://arxiv.org/abs/2310.01558) | Empirical documentation of context override failure: models frequently default to training priors when retrieved content conflicts with encoded beliefs. Demonstrates that retrieval presence does not guarantee retrieval use. Peer-reviewed. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Core implementation concept for production AI systems. Informs RAG architecture, tool use design, citation pipeline design, and knowledge base governance. |
| **Organizational** | Explains why "we connected the AI to our documents" is not the same as "the AI uses our documents reliably." Frames the knowledge base as the accountability dependency it is. |
| **Client-facing** | Answers the question: "how do you ensure the AI is working from our information, not making things up?" — and establishes what knowledge base governance is required to support that claim. |
| **LLM-native** | Required context for any RAG implementation. Understanding grounding at the practice level clarifies why retrieval ≠ grounding and why context override is a design constraint, not an edge case. |

---

*Last updated: v1.0 · May 2026*
