<!--meta
category: Foundations
short: The architecture underneath almost everything — and the reason a weakness in one model is rarely local to it
aliases: [transformer, self-attention, attention mechanism, encoder decoder, attention is all you need, what architecture do LLMs use]
tags: [AI Literacy, Architecture, Model Behavior]
established: established
-->
# Transformers

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The neural network architecture underlying most modern AI systems — designed to process sequences by learning which parts to pay attention to, enabling the scale that powers LLMs.

---

## Technical definition

The Transformer (Vaswani et al., 2017) is a sequence architecture built on **attention** — a learned, weighted lookup in which every position in a sequence can draw on every other position, with the weights computed from the content itself rather than fixed by distance or order.

**Its decisive move was subtractive.** Earlier sequence models processed inputs step by step, each step depending on the last. The Transformer dispensed with recurrence and convolution entirely and relied on attention alone. **That is what made it parallelizable across sequence positions**, and parallelism is what made training at current scale economically possible. The architecture did not win because it understood language better; it won because it could be trained on far more data with the hardware available.

**The same architecture generalized past text**, which was not the original claim. Vision, audio, code and joint image-text models are Transformer-based, and cross-modal systems align them in a shared representation ([multimodal AI](multimodal-ai.md)). One architecture now underlies most of the field.

**Two costs follow directly from attention, and both are visible to users.** Attention compares positions pairwise, so cost grows **quadratically** with sequence length — the reason a [context window](context-window.md) is a bounded, expensive resource rather than a free parameter. And attention is not uniform across a long input: models retrieve less reliably from the middle of a long context than from either end, a measured effect rather than an implementation quirk.

**The governance consequence is architectural homogenization, and it is the point this entry exists to make.** Bommasani et al. name it directly: when one architecture and a small number of base models underlie a whole field, **a defect, bias or vulnerability in the foundation is inherited by everything built on it.** Failures stop being independent. Two vendors' products can share a weakness not because either copied the other, but because both descend from the same architectural and training lineage — which is precisely the condition under which diversification stops providing the protection people assume it does.

---

## Plain-language version

Before 2017, systems that handled language read a sentence roughly the way you do — one word after another, each step depending on the one before. That is slow, and it is hard to speed up by buying more computers, because step two cannot start until step one finishes.

The Transformer threw that out. Instead of reading in order, it looks at everything at once and learns which parts matter for which other parts — "attention." The word "it" in a sentence can look back and weight the thing it refers to, directly, without walking through everything in between.

The important consequence is not elegance. It is that the work can be split across thousands of processors at the same time. That made it possible to train on far more text than before, and nearly everything since follows from that. The architecture did not win by understanding language better — it won by being trainable at a scale nothing else could reach.

It then turned out to work for images, audio and code too, which nobody promised at the outset. Almost every AI system you hear about now is built on it.

Two practical consequences. Comparing everything to everything gets expensive fast — costs rise sharply as inputs get longer, which is why there is a limit on how much you can paste in and why long inputs cost more. And attention is uneven: put something important in the middle of a very long document and the model is measurably more likely to overlook it than if it were at the start or end.

One thing worth knowing that rarely gets said: because nearly everything is built the same way, and often on the same handful of base models, weaknesses tend to be shared rather than isolated. Using two different vendors may give you less independence than it looks like.

---

## AI literacy notes

1. **Attention is a learned weighting, not a spotlight of comprehension** — the model computes which positions to draw on from the content itself.
2. **It won on parallelism, not on understanding.** Removing sequential dependence is what made training at scale affordable.
3. **The architecture is modality-agnostic** — text, vision, audio and code, which was a discovery rather than a design goal.
4. **Cost grows quadratically with input length**, which is why context windows are bounded and long inputs are expensive.
5. **Attention is uneven across a long input** — the middle is retrieved less reliably than either end.
6. **Homogenization means correlated failure.** A flaw in the foundation propagates to everything downstream.
7. **Multi-vendor is not automatically diversification** if the vendors share an architecture and a training lineage.
8. **"Transformer" says nothing about capability or safety** — it describes structure, and structure is not a quality claim.

---

## Governance notes

**Core question:** If a weakness were found in the architecture or base model underneath our AI systems, how many of them would be affected at once — and would we currently be able to tell?

**Watch for:**
- Vendor diversification assumed to give independence when the products share a base model or architectural lineage ([systemic risk](systemic-risk-ai.md))
- Long documents pasted into a context on the assumption that everything in them is attended to equally ([context window](context-window.md))
- Cost models that treat input length as linear when the underlying cost is not ([inference](inference.md))
- "Built on Transformers" or a named architecture used as a capability or safety assurance in procurement material
- No inventory of which systems descend from which base model, so blast radius is unknown ([shadow AI](shadow-ai.md))
- Bias or failure treated as a property of one product, when it may be inherited from a shared foundation ([bias](bias-ai-systems.md))
- Concentration risk unexamined because each individual purchase looked like an independent decision

**Practice:**
- **Keep an inventory of the base models and providers your systems actually sit on**, not just the vendors you contract with — that mapping is what makes blast radius answerable
- Treat correlated failure as a live scenario in continuity planning: assume a foundation-level defect affects several systems at once
- Where genuine independence matters, verify it at the model and architecture level rather than at the supplier level
- Place critical material at the start or end of long inputs, and test retrieval from the middle rather than assuming it
- Model cost against actual input length behavior, not a linear approximation
- Treat architecture as a structural fact in documentation ([model card / system card](model-card-system-card.md)), never as evidence of quality or safety

**Key accountability owner:** whoever maintains the AI system inventory — because homogenization only becomes visible when someone can say which systems share a foundation, and that question is almost never asked at purchase time, when each decision still looks independent.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The architecture, the removal of recurrence, the parallelism argument and the quadratic cost of attention are textbook and uncontested, each traceable to the originating paper or to well-cited follow-on work. The positional-reliability effect and the homogenization argument both come from named peer-reviewed sources rather than from practitioner impression. **The one claim stated more carefully than the rest is the correlated-failure conclusion:** that shared foundations *imply* correlated risk follows from the homogenization argument and is widely accepted, but **this entry cites no study measuring how often a defect in a base model actually propagates into downstream products** — the inventories that would allow such a study are not public. Treat it as a well-grounded structural expectation to plan against, not as a measured failure rate. Architecture-level details also move: efficiency variants that reduce the quadratic cost exist and are actively developed, so the cost claim describes the standard mechanism rather than every deployed system.

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — the application that made this architecture ubiquitous
- [NLP](nlp.md) — the field this reorganized
- [Context Window](context-window.md) — the bounded resource that quadratic attention cost creates
- [Multimodal AI](multimodal-ai.md) — the same architecture applied beyond text
- [Embeddings](embeddings.md) — the representations attention operates over
- [Pre-training](pre-training.md) — the training regime this architecture made economically possible
- [Recurrent Depth](recurrent-depth.md) — a modification that reuses layers rather than stacking them
- [Frontier AI](frontier-ai.md) — where the largest instances of this architecture sit
- [Systemic Risk (AI)](systemic-risk-ai.md) — the risk category homogenization creates
- [Inference](inference.md) — where the cost of attention is actually paid

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (NeurIPS, 2017) · [link](https://arxiv.org/abs/1706.03762) | The originating architecture: attention without recurrence or convolution, and the parallelism across sequence positions that follows from removing sequential dependence. |
| SRC-143 | Bommasani, R. et al. (Stanford Center for Research on Foundation Models / HAI — 100+ authors) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | Names **homogenization** — one architecture and a few base models underlying a field — and the inherited-defect consequence this entry builds its governance section on. |
| SRC-149 | Liu, N.F.; Lin, K.; Hewitt, J.; Paranjape, A.; Bevilacqua, M.; Petroni, F.; Liang, P. — *Lost in the Middle: How Language Models Use Long Contexts* (2023) · [link](https://arxiv.org/abs/2307.03172) | The measured positional effect: retrieval from the middle of a long context is less reliable than from either end. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. (Renmin University of China + multi-institution) — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Survey treatment of the architecture and the pre-train/adapt pipeline built on it. |
| SRC-213 | Radford, A.; Kim, J.W.; Hallacy, C.; Ramesh, A.; Goh, G.; Agarwal, S.; Sastry, G.; Askell, A.; Mishkin, P.; Clark, J.; Krueger, G.; Sutskever, I. (OpenAI) — *Learning Transferable Visual Models From Natural Language Supervision (CLIP)* (2021) · [link](https://arxiv.org/abs/2103.00020) | Evidence of the architecture generalizing beyond text into a shared image-text representation. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Cost is not linear in input length, and the middle of a long context is retrieved less reliably. Test both rather than assuming either. |
| **Organizational** | Keep an inventory of the base models your systems actually sit on. Multi-vendor is not diversification when the vendors share a foundation, and that question is never asked at purchase time. |
| **Client-facing** | Explains why long documents are not attended to evenly and why input length drives cost, without requiring the architecture to be explained. |
| **LLM-native** | It won on parallelism, not on understanding. Homogenization means failures are correlated rather than independent — a flaw in the foundation is inherited by everything above it. |

---

*Last updated: v1.0 · September 2026*
