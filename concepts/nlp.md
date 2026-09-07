<!--meta
category: Foundations
short: The field concerned with making computers process human language — the discipline LLMs came out of, and the reason its older, unglamorous problems are still the ones that break production systems
aliases: [natural language processing, computational linguistics, language technology, text processing, NLP pipeline, how do computers understand language]
tags: [AI Literacy, Model Behavior]
established: established
-->
# NLP

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
The field of AI focused on enabling computers to understand, process, and generate human language — the foundational discipline behind modern LLMs and conversational AI.

---

## Technical definition

Natural language processing is the field concerned with computational handling of human language — analyzing it, transforming it, and producing it. Jurafsky and Martin's standard text scopes it alongside computational linguistics and speech recognition, spanning classical annotation tasks (parsing, coreference resolution, named-entity recognition, machine translation) and contemporary neural methods under one discipline.

**The field is much older than the current generation of systems, and that history is not decoration.** Weizenbaum's ELIZA (1966) held apparently fluent conversations using pattern substitution and no understanding whatsoever — and its users, including people who knew exactly how it worked, attributed comprehension to it anyway. The observation that fluency reads as understanding was made about a program with a few hundred rules, sixty years before anyone deployed an LLM ([anthropomorphism](anthropomorphism-ai.md)).

**Three eras, and the residue of each is still in production.** Rule and grammar systems gave way to statistical methods in the 1990s, which gave way to neural sequence models, which the Transformer architecture (Vaswani et al., 2017) reorganized around attention — the change that made scaling to today's [large language models](large-language-models.md) tractable. Organizations rarely run one era at a time: a regex, a classifier, and an LLM commonly sit in the same pipeline, with different failure behavior and different owners.

**What changed is the interface, not the problem set.** The classical tasks did not disappear when a general model became capable of most of them; they became *implicit*. A system that used to have a named entity recognizer with a measurable F1 score now has an LLM doing entity recognition invisibly, inside a larger generation step, with no separate measurement. **The capability got better and the observability got worse** — which is the single most important governance consequence of the shift.

**Language is not uniform, and NLP inherits every unevenness in it.** Performance varies sharply by language, dialect, register and domain. Petrov et al. (2023) showed that tokenizers alone impose the disparity before any modeling happens: the same content costs several times more tokens in some languages than in English, which translates directly into higher price, more [context window](context-window.md) consumed, and worse effective performance for those users ([tokenization](tokenization.md)). This is a property of the field, not a bug in one product.

---

## Plain-language version

Natural language processing is the long-running effort to get computers to work with human language — reading it, sorting it, translating it, answering with it. It is the field that today's chatbots came out of, and it is much older than they are.

An early program called ELIZA, written in 1966, imitated a therapist by rearranging whatever you typed back at you as a question. It understood nothing. People talked to it anyway, and some of them were convinced it understood — including people who had read the code. The lesson that fluent language reads as intelligence is nearly sixty years old.

For most of that history the work was broken into named jobs: find the names in this text, work out what "it" refers to, translate this sentence, decide if this review is positive. Each job had its own tool and its own score, so you could say how well it worked.

Large language models do most of those jobs at once, better, and invisibly. That is the improvement and the catch together. The old pipeline was clunky but you could see where it failed. The new one is smoother and you often cannot — the entity extraction that used to have a number attached is now a step inside a paragraph of generated text.

One more thing worth knowing: none of this works equally well in every language. Some languages cost several times more to process than English for the same content, before any question of quality comes up. If your users do not all write in English, that difference is theirs to bear.

---

## AI literacy notes

1. **LLMs are a chapter in NLP, not a replacement for it.** The field's older results — on ambiguity, evaluation, and language variation — still describe what these systems do.
2. **Fluency has never been evidence of understanding.** ELIZA established this in 1966 with pattern matching, and the effect is stronger now, not weaker.
3. **The classical tasks did not go away; they went implicit.** Entity extraction, classification and translation still happen — just inside a generation step, unmeasured.
4. **Capability rose and observability fell in the same move.** This is the trade most organizations made without noticing they were making it.
5. **Performance is unevenly distributed across languages**, and part of that gap is fixed at the tokenizer, before the model runs.
6. **Most real systems are hybrids** — regex, classifier, and LLM in one pipeline, with three different failure modes and often three different owners.
7. **Benchmarks in this field measure tasks, not language competence** ([AI benchmarking](ai-benchmarking.md)) — a distinction the field itself has argued about for decades.
8. **"Understanding" is a contested word here**, not a settled technical claim, and it should be used carefully in anything client-facing.

---

## Governance notes

**Core question:** Which language-handling steps in this system used to be separately measurable, and what is our evidence that they still work now that a general model absorbed them?

**Watch for:**
- Classical NLP tasks folded into an LLM call with no remaining task-level metric ([evaluation](evaluation.md))
- A pipeline mixing rules, classifiers and LLMs where no one owns the whole path end to end
- Quality assessed only in English while the system serves users writing in other languages
- Cost and [context window](context-window.md) budgets set from English text, then applied to languages that tokenize far less efficiently
- "The model understands X" appearing in documentation or client material as a capability claim
- Legacy components retained long after the model superseded them, with nobody willing to remove them
- Language variation — dialect, register, domain jargon — treated as user error rather than as system scope

**Practice:**
- **Name the language tasks the system actually performs**, including the ones now hidden inside a generation step, and decide which need their own measurement
- Keep a task-level evaluation for any language step that carries consequence, rather than relying only on end-to-end output quality
- Test across the languages, dialects and registers your users actually write in, and report performance by segment rather than in aggregate
- Budget cost and context per language, not once in English ([tokenization](tokenization.md))
- Document which era each pipeline component belongs to and who owns it — hybrid stacks fail at the seams
- Prefer capability descriptions to comprehension claims in client-facing text ([AI disclosure](ai-disclosure-attribution.md))

**Key accountability owner:** whoever owns the system's quality metrics — because the risk here is not that a step performs badly, but that it stopped being measured when it stopped being a separate component.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** NLP is a mature academic and industrial discipline with a standard reference text, decades of peer-reviewed literature, and stable subfield definitions. The historical account and the tokenizer-disparity finding are both directly sourced. **What is genuinely unsettled is internal to the field, not to this entry:** whether large language models should be understood as continuous with earlier NLP or as a break from it is actively argued, and terms like "understanding" and "reasoning" carry no agreed technical definition here. **The claim this entry makes most confidently, and the one least often stated, is the observability trade** — that absorbing named tasks into general models removed their measurement. That is an inference from how the field's practice changed rather than a quantified finding, and it is offered as such.

---

## Related concepts

- [Large Language Models (LLMs)](large-language-models.md) — the current dominant approach within this field
- [Tokenization](tokenization.md) — where cross-language disparity is fixed before modeling begins
- [Embeddings](embeddings.md) — the representation that made statistical language work generalize
- [Pre-training](pre-training.md) — how a general language capability is acquired before any task is named
- [Multimodal AI](multimodal-ai.md) — the extension of the same architecture beyond text
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — the ELIZA effect, named for a program from this field
- [Evaluation](evaluation.md) — what happens to task-level measurement when tasks stop being components
- [AI Benchmarking](ai-benchmarking.md) — how this field has historically measured itself, and the critique of that
- [Grounding](grounding.md) — connecting language output to a verifiable source
- [Hallucination](hallucination.md) — the field's most consequential open problem

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-246 | Jurafsky, D.; Martin, J.H. (Stanford / University of Colorado Boulder) — *Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics, and Speech Recognition with Language Models*, 3rd ed. draft, August 19 2026 · [link](https://web.stanford.edu/~jurafsky/slp3/) | The field's standard reference text; establishes the scope used here — classical annotation tasks and neural methods within one discipline. ⚠️ Draft edition, revised periodically; some chapters incomplete. Cite the dated draft, not a page number. |
| SRC-178 | Weizenbaum, Joseph (MIT) — *ELIZA — a computer program for the study of natural language communication between man and machine* (Communications of the ACM, 1966) · [link](https://doi.org/10.1145/365153.365168) | The founding demonstration that fluent language output produces attributions of understanding independent of any understanding being present. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (NeurIPS, 2017) · [link](https://arxiv.org/abs/1706.03762) | The architectural change that reorganized the field around attention and made current-scale language models tractable. |
| SRC-221 | Sennrich, R.; Haddow, B.; Birch, A. (University of Edinburgh) — *Neural Machine Translation of Rare Words with Subword Units* (ACL, 2016) · [link](https://arxiv.org/abs/1508.07909) | Subword segmentation as the standard solution to open-vocabulary language, and the mechanism behind modern tokenizers. |
| SRC-222 | Petrov, A.; La Malfa, E.; Torr, P.H.S.; Bibi, A. (University of Oxford) — *Language Model Tokenizers Introduce Unfairness Between Languages* (NeurIPS, 2023) · [link](https://arxiv.org/abs/2305.15425) | Evidence that cross-language cost and performance disparity is imposed at tokenization, before modeling — the basis for this entry's per-language budgeting practice. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Name the language tasks now hidden inside generation steps and decide which still need their own metric. Test and budget per language rather than once in English. |
| **Organizational** | The move to general models raised capability and lowered observability at the same time. That trade was rarely an explicit decision, and it is the one worth revisiting. |
| **Client-facing** | Gives the vocabulary to describe what a system does with language without claiming it understands — a distinction the field itself has never settled. |
| **LLM-native** | LLMs are a chapter in a sixty-year discipline, not a fresh start. Its oldest result — that fluency reads as comprehension — was demonstrated in 1966 and still holds. |

---

*Last updated: v1.0 · September 2026*
