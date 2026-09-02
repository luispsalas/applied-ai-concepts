<!--meta
category: Observability & Governance
short: When sensitive information from training data or context surfaces in model outputs — exposing what was never meant to be accessible
aliases: [memorization, training data extraction, it leaked our data, PII in output, data exposure]
tags: [Security, Privacy]
established: established
-->
# Data Leakage (AI Systems)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
When sensitive information from training data unintentionally surfaces in model outputs — exposing content that was never meant to be accessible.

---

## Technical definition

The unintended disclosure of information through an AI system's outputs. Three distinct pathways, often conflated but requiring different controls:

- **Training-data memorization.** Models retain and can reproduce verbatim fragments of their training data, including personally identifiable information. This is *extractable memorization*: data an adversary can recover by querying the model, without prior knowledge of the training set. Larger models memorize more. Alignment training does not remove it — a divergence attack that pushes a production chat model off its conversational distribution has been shown to raise the rate of memorized emission by roughly two orders of magnitude.
- **Context leakage.** Information supplied at inference — retrieved documents, [system prompt](system-prompt.md) contents, prior turns, tool results — surfaced to a user who was not entitled to it. The model has no concept of who is authorized to see what; anything in its context is a candidate for its output.
- **Cross-tenant or cross-session leakage.** Data from one user, customer, or session appearing in another, typically caused by shared [memory](memory-ai-systems.md), a shared retrieval index, or caching that ignores an authorization boundary.

Note that "data leakage" also has an unrelated meaning in machine learning evaluation — training and test data contaminating each other and inflating measured performance. That is a *measurement* defect, not a disclosure one. This entry covers disclosure; the wiki tracks the evaluation sense separately.

The governance consequence is that data minimization at *training* time and access control at *retrieval* time are different controls addressing different pathways, and neither substitutes for the other.

---

## Plain-language version

Sometimes a model repeats things it shouldn't: fragments memorized from its training data, or content pulled into the conversation that this particular person had no right to see. It isn't malice and it isn't a break-in — the model has no idea who you are or what you're allowed to know. It only knows what is in front of it, and anything in front of it can come back out.

---

## AI literacy notes

1. **A model does not know who is asking.** It has no concept of authorization. Every control over who sees what must live in the system around it — in what gets retrieved and placed into context, never in an instruction asking the model to keep a secret.
2. **Anything in the context can leave in the output.** System prompts, retrieved documents, and tool results are all candidates for disclosure. "Do not reveal this" is a request, not a control.
3. **Alignment training does not remove memorization.** A model that behaves well conversationally can still be pushed off-distribution into emitting training data. Safety behavior and memorization are separate properties.
4. **Scale increases exposure.** Larger models memorize more of their training data. Capability and privacy risk grow together, which is a trade-off worth naming explicitly rather than discovering later.
5. **The word is overloaded.** In AI security it means disclosure; in ML evaluation it means train/test contamination. They share a name and nothing else — check which one a document means before acting on it.

---

## Governance notes

**Core question:** If a user asked the system to reveal everything it currently knows, what would come out that they are not entitled to?

**Watch for:**
- Confidentiality of the system prompt or retrieved content protected only by an instruction telling the model not to disclose it
- Retrieval indexes or memory stores shared across users, customers, or tenants without an enforced authorization filter
- Personal data placed in training or fine-tuning sets without a lawful basis or a removal path
- No monitoring for disclosure patterns — repeated extraction attempts going unnoticed
- Assuming a vendor model is memorization-free because it is well-behaved in conversation

**Practice:**
- Filter at retrieval, not at generation: enforce the requesting user's permissions when assembling context, so unauthorized content is never present to be leaked
- Apply [data minimization](data-minimization.md) to training and fine-tuning sets — the strongest protection against memorization is absence
- Partition memory and retrieval by tenant and session; treat cross-boundary reuse as a design defect
- [Red-team](red-teaming.md) for extraction specifically, including off-distribution and divergence-style prompts, not only conversational probing
- Keep an inventory of what personal data has entered training, so a deletion request can be answered honestly

**Key accountability owner:** the data owner, jointly with the system owner and (where personal data is involved) the privacy function.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on training-data memorization — demonstrated repeatedly in peer-reviewed and widely replicated work across open, semi-open, and production models. **Medium** on context and cross-tenant leakage, where the mechanisms are well understood but published incident evidence is thinner and mostly vendor-reported.

---

## Related concepts

- [Privacy (AI Systems)](privacy-ai-systems.md) — the broader obligation; leakage is one way privacy fails
- [Data Minimization](data-minimization.md) — the most reliable defense against memorization: never train on it
- [Prompt Injection](prompt-injection.md) — a common delivery mechanism for extraction attempts
- [Red Teaming](red-teaming.md) — how extraction exposure is discovered before someone else finds it
- [Knowledge Base](knowledge-base.md) — retrieval scope decides what is even available to leak
- [Memory (AI Systems)](memory-ai-systems.md) — persistence across sessions creates cross-session exposure
- [Audit Trail (AI)](audit-trail-ai.md) — disclosure is only investigable if inputs and outputs were recorded
- [Permission Model (AI)](permission-model-ai.md) — the enforced boundary that decides what may enter context in the first place
- Data Leakage (Model Evaluation) — the unrelated sense of the same term: train/test contamination inflating measured performance

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-150 | Carlini, N.; Tramer, F.; Wallace, E.; Jagielski, M. et al. — *Extracting Training Data from Large Language Models* (USENIX Security, 2021) · [link](https://arxiv.org/abs/2012.07805) | Foundational demonstration that models memorize and can be made to reproduce verbatim training data, including PII; larger models are more vulnerable. |
| SRC-161 | Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M. et al. — *Scalable Extraction of Training Data from (Production) Language Models* (2023) · [link](https://arxiv.org/abs/2311.17035) | Extraction at scale against aligned production models, and the divergence attack; establishes that alignment does not eliminate memorization. |
| SRC-148 | OWASP Foundation (GenAI Security Project) — *OWASP Top 10 for LLM Applications* (2025) · [link](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Industry-standard treatment of sensitive-information disclosure as an application security risk. |
| SRC-039 | European Parliament — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The legal frame: unauthorized disclosure of personal data is a breach with defined obligations, whatever the mechanism. |
| SRC-060 | He, Yifeng et al. (UC Davis) — *Security of AI Agents* (2026) · [link](https://arxiv.org/abs/2406.08689) | Confidentiality failures in agent architectures, where context and tool results cross boundaries. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Authorization must be enforced when context is assembled. Filtering at generation time is not a control. |
| **Organizational** | Disclosure through a model output is a data breach with the same obligations as any other — the novel mechanism does not change the duty. |
| **Client-facing** | Answers "could our data end up in someone else's answer?" — a question with a real mechanism behind it, not a hypothetical. |
| **LLM-native** | Memorization scales with model size and survives alignment; design retrieval and memory boundaries as though the model will disclose anything it holds. |

---

*Last updated: v1.0 · August 2026*
