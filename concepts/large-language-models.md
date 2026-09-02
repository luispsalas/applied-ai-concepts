<!--meta
category: Foundations
short: Neural networks trained on vast text corpora that generate language by predicting what comes next — the foundation of most modern AI tools and agents
aliases: [LLM, foundation model, language model, GPT, chatbot model]
tags: [Architecture]
established: established
-->
# Large Language Models (LLMs)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Neural networks trained on vast text corpora that generate language by predicting what comes next — the foundation of most modern AI assistants, tools, and agents.

---

## Technical definition

A large language model (LLM) is a neural network — in practice a Transformer (SRC-141) — trained on very large text corpora to model the probability of the next token given the preceding ones. Text is generated autoregressively: at each step the model produces a probability distribution over the next token and samples from it (see [Determinism vs Probabilism](determinism-vs-probabilism.md)). Training runs in two broad stages — self-supervised pre-training on broad data, then adaptation (instruction tuning, RLHF) — a pattern the survey literature organizes as pre-training, adaptation, utilization, and evaluation (SRC-142). Because one pre-trained base is adaptable to many downstream tasks, LLMs are the prototypical "foundation models": broadly capable, broadly reused, and therefore broad in their risks (SRC-143). An LLM is not a fact database and not a classical reasoning engine — it is a statistical model of language whose apparent knowledge and reasoning are emergent properties of next-token prediction at scale.

---

## Plain-language version

A large language model is the engine behind tools like ChatGPT and Claude. It was trained by reading an enormous amount of text and learning, over and over, to guess the next word. That is essentially all it does when you use it: given what has been written so far, predict what comes next, one piece at a time. It has no memory of you between conversations unless a system is built around it to add one, and no separate store of facts it looks things up in — its answers come from patterns in the text it was trained on. That single mechanism, at enormous scale, is enough to write, summarize, translate, and code surprisingly well — and also to be confidently wrong.

---

## AI literacy notes

1. **Next-token prediction is the whole engine.** Everything an LLM appears to "know" or "reason" is a byproduct of predicting likely text — which is why it can be fluent and wrong at the same time; fluency and truth are different targets.
2. **The model is frozen; the system around it is not.** A base model's knowledge stops at its training cutoff and doesn't change per user. Memory, current facts, and tool access come from the harness around the model (see [Harness Paradigm](harness-paradigm.md)), not the model itself.
3. **Capability is emergent and uneven.** Abilities appear as models scale but are "spiky" — strong at some tasks, surprisingly weak at adjacent ones — so capability must be evaluated per use case, not assumed from general impressiveness.
4. **"Foundation model" is the governance-relevant framing:** one model reused across many applications means one model's flaws propagate across all of them.

---

## Governance notes

**Core question:** Does everyone deploying this system understand it is a probabilistic text model — not a fact database or a reasoning engine?

**Watch for:**
- Treating LLM output as retrieved fact
- Assuming the model "knows" current information (it stops at its training cutoff)
- Assuming general capability implies capability on your specific task

**Practice:**
- Pair every LLM deployment with grounding/verification and per-use-case evaluation
- Document the model, its version, and its training cutoff

**Key accountability owner:** the system owner who selects and deploys the model.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The architecture (Transformer), the training paradigm (pre-train then adapt), and the next-token-prediction mechanism are well-established and settled. What remains actively debated is interpretation — whether emergent abilities amount to "understanding" or "reasoning" — which this entry deliberately leaves open.

---

## Related concepts

- [AI Hallucination](hallucination.md) — the characteristic failure of next-token prediction: fluent output that is confidently untrue
- [Grounding](grounding.md) — anchoring an LLM's output to real sources, the main remedy for its lack of a fact store
- [Retrieval-Augmented Generation (RAG)](rag.md) — the dominant pattern for giving a frozen model current, specific knowledge at run time
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — the probabilistic nature of next-token sampling, and why the same prompt can differ
- [Fine-tuning](fine-tuning.md) — adapting a pre-trained base to a domain or task; the "adaptation" stage of the LLM lifecycle
- [Types of AI Systems](types-of-ai-systems.md) — where LLMs sit within the wider taxonomy of AI by capability and autonomy
- [Harness Paradigm](harness-paradigm.md) — the control layer around the model that supplies the memory, tools, and governance the model itself lacks
- [AI Agent](ai-agent.md) — an LLM placed in a loop with tools and goals; the agentic extension of a base model

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-141 | Vaswani, A. et al. — *Attention Is All You Need* (NeurIPS, 2017) · [link](https://arxiv.org/abs/1706.03762) | The Transformer architecture underlying modern LLMs. |
| SRC-142 | Zhao, W.X. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Reference overview: pre-training, adaptation, utilization, and evaluation. |
| SRC-143 | Bommasani, R. et al. — *On the Opportunities and Risks of Foundation Models* (Stanford CRFM, 2021) · [link](https://arxiv.org/abs/2108.07258) | The foundation-model framing and its risk surface. |
| SRC-007 | Karpathy, A. — *LLM Wiki* (2023) · [link](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | Accessible foundational framing of how LLMs work. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The base substrate you build on: architecture, training cutoff, and probabilistic generation set what the surrounding system must compensate for. |
| **Organizational** | The thing being governed is not "AI" in the abstract but a specific model with a version, a cutoff, and known failure modes — name it. |
| **Client-facing** | Answers "what is actually answering me?" — a text predictor trained on past data, not a live oracle. |
| **LLM-native** | The foundation every other concept in this wiki builds on; understanding next-token prediction is the prerequisite for the rest. |

---

*Last updated: v1.0 · July 2026*
