<!--meta
category: Foundations
short: How text is chopped into the units a model actually processes — the same units you are billed for, and the reason cost and context differ by language
aliases: [tokens, what is a token, token count, BPE, byte pair encoding, subword units, tokenizer, why am I charged per token, how many r's in strawberry]
tags: [AI Literacy, Architecture]
established: established
-->
# Tokenization

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Splitting text into the subword units a language model actually reads and writes — the unit of the mechanism, of the context window, and of the bill, which is why the same sentence can cost several times more in one language than another.

---

## Technical definition

A language model does not process characters or words. Before anything else happens, input text is segmented into **tokens** — items drawn from a fixed vocabulary learned during training — and each is mapped to an integer ID. Everything downstream operates on those IDs.

The dominant method is **subword segmentation**, established for neural sequence models by the byte-pair-encoding approach of Sennrich et al. (ACL 2016). Their argument was that *"various word classes are translatable via smaller units than words"* — proper names, compounds, loanwords — so a vocabulary of frequent fragments can represent **open vocabulary**: any string, including words never seen in training, without an "unknown word" escape hatch.

The practical consequence is that **token boundaries do not align with word boundaries, and are not intuitive**. Common words are usually one token. Rare words, names, code, URLs, numbers and non-Latin scripts fragment into several. A leading space is typically part of the token.

**Three separate things are all measured in this same unit**, which is why the term shows up in places that look unrelated:

| | |
|---|---|
| **Mechanism** | The model predicts the next *token*, not the next word — see [Large Language Models](large-language-models.md) |
| **Capacity** | The [context window](context-window.md) is a token budget, not a word or page budget |
| **Cost** | Per-token pricing, rate limits, and latency all scale with token count — see [Scalability](scalability-ai-systems.md) |

**The distributional finding that makes this a governance concern, not a curiosity:** tokenizers are learned from training corpora, which are not linguistically balanced. Petrov et al. (NeurIPS 2023) measured the result directly — *"the same text translated into different languages can have drastically different tokenization lengths, with differences up to 15 times in some cases,"* and even character- and byte-level models show *"over 4 times the difference in the encoding length for some language pairs."*

Because the three quantities above share the unit, one disparity propagates into all three at once. A user working in a poorly-tokenized language pays more per unit of meaning, waits longer, **and gets less usable context** — from the same model, at the same posted price. The authors' framing is unambiguous: this is *unfairness between languages*, produced by an implementation detail nobody chose as policy.

---

## Plain-language version

An AI model cannot read letters or words. Text first gets chopped into pieces from a fixed list the model learned during training — pieces roughly the size of a syllable or a short word. Those pieces are called tokens, and they are all the model ever sees.

The chopping is not tidy. Ordinary English words are usually one piece each. Unusual words, names, numbers, code and anything not written in the Latin alphabet get broken into several.

This matters more than it sounds, because the same unit is used for three different things: how the model works, how much text it can hold at once, and what you are charged. So the chopping is not just a technical detail — it is the meter.

And the chopping is not fair. The pieces were learned mostly from English text, so English gets chopped efficiently and other languages do not. Researchers measured the same sentence taking **up to fifteen times as many pieces** depending on the language. Because all three things share the unit, someone writing in an unlucky language pays more, waits longer, and can fit less into a conversation — same model, same advertised price.

It also explains a famous embarrassment. When a model miscounts the letters in a word, it is not being stupid about spelling: it never saw the letters. It saw two or three chunks, and the letters inside them are not something it can look at.

---

## AI literacy notes

1. **A token is not a word.** Common English words are roughly one token; the usual planning figure is about ¾ of a word per token, but that ratio is an English ratio and does not travel.
2. **The letter-counting failures are a tokenization artifact, not a reasoning failure.** A model asked how many times a letter appears in a word is being asked about something below the resolution of its own input.
3. **Rare words, names, numbers, code and non-Latin scripts cost more tokens** than their length suggests — which means more money, more latency, and more of your context window consumed.
4. **Your context window is smaller in some languages than others,** for the same posted number. A 200k-token window is 200k tokens, not 200k units of meaning.
5. **Cost estimates built on English samples will under-forecast** a multilingual deployment, sometimes by a large multiple.
6. **The vocabulary is fixed at training time.** It cannot be extended for your domain without changing the model; heavy jargon simply fragments.
7. **Different models tokenize differently**, so token counts are not portable between providers — a prompt that fits one context window may not fit another of the same nominal size.
8. **Arithmetic weakness has a tokenization component.** Numbers split into fragments that do not correspond to digits or place value.

---

## Governance notes

**Core question:** In the languages and content types we actually deploy in, what does one unit of work cost and how much context do we really have — measured, not extrapolated from an English sample?

**Watch for:**
- Cost and capacity forecasts built on English test data for a multilingual service — the structural under-estimate
- A single per-token price presented as equal treatment across languages, when the token itself is the inequity ([bias](bias-ai-systems.md))
- Context-window figures quoted as a capability without stating the language they were measured in
- Prompt or document budgets set in words, pages or characters, then silently exceeded in token terms
- Token counts compared across providers as if the unit were standard
- Character-level tasks (counting, spelling, redaction on exact strings) delegated to a model, where the failure is structural rather than occasional
- Retrieval chunk sizes tuned in characters while the [context window](context-window.md) is spent in tokens
- Vendor contracts with per-token commitments signed before measuring the token profile of the real workload

**Practice:**
- **Measure token counts on real workload samples, in every deployed language**, before committing to pricing, context budgets, or rate limits
- State language coverage alongside cost per interaction — a flat per-token rate is not a flat per-user rate
- Where a service is offered multilingually, treat the tokenization disparity as a known, quantified equity issue with an owner, rather than an invisible one
- Do not route character-exact work (counting, exact-string redaction, checksum-style validation) through a model; use conventional code
- Re-measure on every [model version change](model-version-update.md) — a new tokenizer changes cost and effective capacity with no announcement that it has
- Keep a headroom margin on context budgets rather than filling to the nominal limit

**Key accountability owner:** whoever owns the commercial and capacity forecast for the service — because the disparity lands as a budget and fairness outcome, not as a technical defect anyone will file.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** Subword tokenization is settled, long-standing engineering with a canonical peer-reviewed reference (ACL 2016), and the cross-language disparity is a peer-reviewed measurement at NeurIPS 2023 rather than an inference. The one caveat is that specific numbers date quickly: vocabularies, ratios and the size of the disparity are properties of particular tokenizers and shift with each model generation, so **treat the 15× figure as evidence that the effect is large, and measure your own.**

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — next-token prediction is the mechanism; this is what a token is
- [Context Window](context-window.md) — the budget this is the unit of
- [Embeddings](embeddings.md) — what each token ID becomes once inside the model
- [Pre-training](pre-training.md) — where the vocabulary is learned, and from which corpus
- [Scalability (AI Systems)](scalability-ai-systems.md) — per-token pricing is why AI unit economics run the wrong way
- [Bias (AI Systems)](bias-ai-systems.md) — a training-corpus imbalance surfacing as unequal cost and capacity
- [Multimodal AI](multimodal-ai.md) — images and audio are tokenized too, on different and less intuitive ratios
- [Local LLMs](local-llms.md) — where the per-token meter is replaced by fixed hardware cost
- [Model Version & Update](model-version-update.md) — a changed tokenizer silently changes cost and capacity
- [Hallucination](hallucination.md) — distinct failure; letter-counting errors are tokenization, not fabrication

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-221 | Sennrich, R.; Haddow, B.; Birch, A. — *Neural Machine Translation of Rare Words with Subword Units* (ACL, 2016) · [link](https://arxiv.org/abs/1508.07909) | The canonical subword/BPE reference: encoding rare and unknown words as sequences of subword units enables open-vocabulary models, because "various word classes are translatable via smaller units than words." |
| SRC-222 | Petrov, A.; La Malfa, E.; Torr, P.H.S.; Bibi, A. — *Language Model Tokenizers Introduce Unfairness Between Languages* (NeurIPS, 2023) · [link](https://arxiv.org/abs/2305.15425) | The measured cross-language disparity — up to 15× tokenization length for the same text, and over 4× even for character- and byte-level models — and its consequences for cost, latency and available context. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (2017) · [link](https://arxiv.org/abs/1706.03762) | The architecture that consumes token sequences, establishing tokens as the unit of the model's input and output. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Situates tokenization within the standard LLM pipeline and confirms subword vocabularies as the prevailing practice across model families. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Token counts are not portable between providers and not proportional to text length. Measure on real samples per language; never route character-exact work through a model. |
| **Organizational** | The token is the meter for cost, capacity and latency at once. A flat per-token price is not flat per user, and English-based forecasts under-estimate multilingual deployments. |
| **Client-facing** | Explains why cost and conversation length vary by language, and why a model can be excellent at analysis while miscounting the letters in a word. |
| **LLM-native** | The model never sees characters. Every property that seems to be about words — cost, capacity, spelling failures, arithmetic weakness — is downstream of a vocabulary learned from an unbalanced corpus. |

---

*Last updated: v1.0 · September 2026*
