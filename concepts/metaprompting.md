<!--meta
category: Interaction & Design
short: Prompting about prompting — three different practices share the name, and the governance question is the same for all of them
aliases: [meta prompting, prompt generation, prompt optimization, using AI to write prompts, self-improving prompts]
tags: [AI Literacy, Prompting]
established: emerging
-->
# Metaprompting

> **Term status — Emerging.** In active use, but the term is not yet stable: it is used for at least three distinct practices, and this entry names them rather than picking one.

## One-line essence
Prompting about prompting — using a model to write, refine or structure the instructions given to a model, a practice whose several meanings share one governance consequence.

---

## Technical definition

**Metaprompting has no single agreed meaning.** The term is in active use across research and practice for at least three distinct things, and a document using it without saying which is ambiguous:

1. **Prompt generation and refinement** — using a model to write or improve a prompt that will then be given to a model. This is the dominant practitioner sense, and the one behind vendor "prompt improver" features. The output is a prompt; a human may or may not read it before it runs.

2. **Structural scaffolding** — a prompting method that supplies the *shape* of a solution rather than examples of one. Zhang, Yuan and Yao define meta prompting as focusing on the structural and syntactic pattern of a problem over its content, contrasting it with example-driven few-shot prompting ([zero-shot and few-shot learning](zero-shot-few-shot-learning.md)). The output is an answer, produced under an abstract template.

3. **Self-critique loops** — a model evaluating and revising its own instructions or outputs across iterations. This is the least well-supported use of the name; the underlying practice is real, but it is more often called self-refinement or reflection.

**Senses 1 and 3 share the property that matters here: the instruction layer stops being human-authored.** In a conventional system, a person writes the prompt, a reviewer can read it, and it can be diffed, versioned and approved like any other artifact. When a model generates the prompt, that artifact still exists — but nobody has necessarily read it, and it may differ on every run.

**Non-determinism is what makes this a governance question rather than a style question.** A generated prompt is not a fixed asset unless it is captured and pinned. An evaluation run against a prompt that regenerates each time is measuring a moving target, and the improvement it reports may not survive to production ([evaluation](evaluation.md)).

**Sense 2 does not have this problem** — the scaffold is human-authored and stable; only the answer varies. Conflating the three is how a genuinely safe technique lends its reputation to a riskier one.

---

## Plain-language version

Metaprompting means using AI to help with the instructions you give AI. That is the short version, and it hides a problem: **people use the word for three different things.**

The most common one is asking a model to write or improve a prompt for you. You describe roughly what you want, it produces a better-worded instruction, and that instruction is what actually runs.

The second is a research sense: instead of showing the model examples of what a good answer looks like, you give it the *structure* of one — a template for how to approach the problem. The template is written by a person and stays put.

The third is a model checking and rewriting its own instructions as it goes.

The first and third have something in common worth pausing on. **Normally, the instructions given to an AI system are written by a person. Someone can read them, review them, keep a copy, and see what changed.** Once the model writes them, that stops being automatically true. The instructions still exist — but nobody may have looked at them, and they might be different tomorrow.

That is not an argument against the technique, which genuinely produces better prompts than most people write unaided. It is an argument for one small habit: **when a model generates a prompt you are going to use repeatedly, save the text and treat it as yours.** Otherwise you are testing one thing and shipping another.

---

## AI literacy notes

1. **Say which sense you mean.** A document that uses "metaprompting" without defining it is ambiguous across three practices with different risk profiles.
2. **Generated prompts are usually better than hand-written ones** for people who do not prompt professionally — the technique works.
3. **A generated prompt is still a prompt**: it can be read, saved, versioned and reviewed. The technique does not remove that option; convenience does.
4. **Regenerating on every run breaks evaluation** — you cannot measure a prompt that changes.
5. **Structural scaffolding (sense 2) keeps the human-authored artifact** and does not carry the review problem.
6. **The model's stated reason for a prompt change is not evidence** that the change is what improved the result ([hallucination](hallucination.md)).
7. **A prompt is where policy usually lives** — tone, refusals, scope limits. Regenerating the prompt can quietly regenerate the policy.
8. **Improvement claims need a before/after on held-out cases**, not a judgment from the same model that wrote the prompt.

---

## Governance notes

**Core question:** If a model wrote the instructions our system runs on, who read them — and can we produce the exact text that was live last Tuesday?

**Watch for:**
- A generated prompt going into production without a human reading it end to end
- Prompts regenerated at run time, so no two runs share an instruction layer
- Policy language — refusals, tone, scope limits — silently dropped by a rewrite ([system prompt](system-prompt.md))
- Evaluation results attributed to a prompt that no longer exists in that form ([evaluation](evaluation.md))
- The same model judging whether its own prompt rewrite was an improvement
- "Metaprompting" used in a design document without saying which of the three practices is meant
- A self-critique loop with no stopping rule, drifting further from the original intent each pass
- Prompt text treated as scratch rather than as a versioned artifact ([prompt engineering](prompt-engineering.md))

**Practice:**
- **Generate freely; pin what ships.** Capture the generated text, commit it, and run that fixed version.
- **Review generated prompts as you would review code** — a person reads the whole thing before it runs against anything that matters
- Diff a rewrite against the prompt it replaces, and check specifically that policy and constraint language survived
- Evaluate the pinned prompt on held-out cases, with a judge that is not the model that authored it ([evaluation](evaluation.md))
- Give any self-critique loop an explicit iteration limit and an exit condition
- Say which sense of metaprompting a document means, on first use
- Keep prompt history where changes are attributable, so a behavior change can be traced to an instruction change ([data provenance and lineage](data-provenance-lineage.md))

**Key accountability owner:** whoever owns the system's behavior in production — because a generated prompt moves the instruction layer out of review by default, and only a deliberate pin-and-review step puts it back.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium — and the uncertainty is in the term, not the practice.** The three senses documented here are all attested in current use, and the entry deliberately declines to pick one, because the field has not. Sense 2 has the clearest published definition (Zhang, Yuan and Yao); sense 1 is dominant in practitioner usage and vendor tooling but has no canonical definition; sense 3 is the weakest attachment to this name and overlaps with self-refinement, which is a better-established label for it. **Expect the meaning to consolidate**, most likely on sense 1, at which point this entry should be narrowed. The governance analysis — that a model-authored instruction layer leaves review by default — holds across senses 1 and 3 and is stated with more confidence than any claim about which definition will win.

---

## Related concepts

- [Prompt Engineering](prompt-engineering.md) — the practice metaprompting is applied to
- [System Prompt](system-prompt.md) — the instruction layer most affected when generation replaces authorship
- [Context Engineering](context-engineering.md) — the wider design of what a model is given
- [Zero-Shot and Few-Shot Learning](zero-shot-few-shot-learning.md) — the example-driven approach sense 2 defines itself against
- [Reasoning Models](reasoning-models.md) — where structured, staged prompting overlaps with model-side deliberation
- [Evaluation](evaluation.md) — what a regenerated prompt makes impossible to measure
- [Hallucination](hallucination.md) — why a model's account of its own prompt change is not evidence
- [Agentic Design Patterns](agentic-design-patterns.md) — reflection and self-critique as named patterns
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — constraints that a prompt rewrite can silently remove
- [Human-in-the-Loop](human-in-the-loop.md) — the review step this technique quietly removes and must deliberately restore

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-281 | Zhang, Yifan; Yuan, Yang; Yao, Andrew Chi-Chih — *Meta Prompting for AI Systems* (2023) · [link](https://arxiv.org/abs/2311.11482) | The only sense with a clear published definition: prompting focused on the **structural and syntactic pattern** of a problem rather than its content, defined in contrast to example-driven few-shot prompting. Basis for sense 2 and for the observation that it does not carry the review problem. |
| SRC-259 | Brown, T.B.; Mann, B.; Ryder, N. et al. (OpenAI — 31 authors) — *Language Models are Few-Shot Learners* (NeurIPS, 2020) · [link](https://arxiv.org/abs/2005.14165) | The example-driven baseline that sense 2 defines itself against — needed to state the contrast accurately rather than from paraphrase. |
| SRC-013 | Anthropic — *Prompt engineering overview* (documentation, 2024) · [link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Vendor documentation of prompt-authoring practice, including tooling that generates prompts — the practical grounding for sense 1. ⚠️ Vendor source; describes one provider's tooling, used here for what the practice is rather than for how widespread it is. |
| SRC-014 | OpenAI — *Prompt engineering* (documentation, 2023) · [link](https://platform.openai.com/docs/guides/prompt-engineering) | A second vendor's account of the same practice, used to establish that prompt-generation tooling is not specific to one provider. ⚠️ Vendor source. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Generate freely, but pin what ships and diff it against what it replaced — especially the constraint language. |
| **Organizational** | If a model writes the instructions your system runs on, the instruction layer has left review unless someone deliberately put it back. |
| **Client-facing** | Useful vocabulary, and a term to define on first use — three different practices answer to it. |
| **LLM-native** | Prompt improvers work. The failure is evaluating a prompt that regenerates, then shipping a different one. |

---

*Last updated: v1.0 · September 2026*
