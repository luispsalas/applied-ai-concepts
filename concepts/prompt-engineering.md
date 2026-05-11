# Prompt Engineering

## One-line essence
Structuring inputs to consistently elicit useful, accurate, and safe model outputs.

---

## Technical definition

Prompt engineering is the practice of designing and refining the instructions, examples, and framing provided to a language model in order to produce outputs that are more accurate, relevant, consistent, and appropriate for a given task. It operates at the level of individual interactions — how a request is phrased, sequenced, and structured.

Core techniques:

- **Role assignment** — establishing a persona or functional context for the model ("You are a careful legal reviewer...")
- **Few-shot examples** — providing sample inputs and outputs to demonstrate the expected pattern before the actual request
- **Chain-of-thought prompting** — instructing the model to reason step-by-step before producing a conclusion, which tends to improve accuracy on complex tasks
- **Constraint specification** — explicitly stating format, length, tone, or exclusions to reduce variance in outputs
- **Decomposition** — breaking a complex task into a sequence of smaller, more manageable prompts rather than requesting everything at once

Prompt engineering is task-level work. It shapes a single interaction. It is distinct from — and operates within — the broader environment defined by context engineering.

---

## Plain-language version

Prompt engineering is the skill of asking well.

The same underlying question, phrased differently, can produce dramatically different results from the same model. Prompt engineering is the practice of understanding *why* that happens and using that understanding deliberately — to get more useful outputs, more consistently, with less back-and-forth.

It is not about finding magic phrases. It is about understanding enough about how language models process instructions to structure your requests in ways that play to their strengths and compensate for their weaknesses.

The skill compounds with use: patterns that work get reused, patterns that fail get refined, and over time you develop a working vocabulary for any given task type.

---

## AI literacy notes

Prompt engineering is the most accessible entry point into effective AI use — but it is also frequently over-indexed as the primary lever. Two calibrations matter:

1. **Prompt engineering operates within context engineering.** The quality ceiling for any prompt is set by the context it runs inside. A well-written prompt in a poorly designed context will underperform a mediocre prompt in a well-designed one. Understanding this relationship prevents practitioners from optimizing the wrong layer.
2. **Prompt engineering is not a substitute for system design.** Techniques that work well for individual interactions do not automatically generalize to production systems. What works in a single session may be brittle at scale, across users, or under adversarial conditions. System-level reliability requires harness-layer controls, not better prompts.

That said, prompt engineering is a genuine high-leverage skill at the practitioner level — and the place where AI literacy becomes immediately actionable for most people.

---

## Confidence level

**Established.** Prompt engineering is a recognized discipline with stable core techniques and active research frontiers (2022–present). Some specific techniques evolve as models improve; the underlying principles — clarity, structure, example provision, constraint specification — are durable.

---

## Related concepts

- [Context Engineering](context-engineering.md) — context engineering defines the environment; prompt engineering operates within it. The distinction matters: improving prompts has diminishing returns if the context is poorly designed
- [Harness Paradigm](harness-paradigm.md) — system prompts are a harness-layer component; prompt engineering techniques inform their design
- Context Framing — the specific sub-skill of structuring how information is presented within a prompt
- System Prompt — the persistent, baseline prompt layer that precedes user interaction; authored using prompt engineering principles
- Guardrails — constraints encoded in the system prompt and harness layer to bound model behavior regardless of user prompt variation

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-013 | Anthropic — *Prompt engineering overview* (documentation, 2024) · [link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Official taxonomy of prompt engineering techniques: role assignment, few-shot examples, chain-of-thought prompting, constraint specification. Authoritative naming conventions for the core techniques listed in the technical definition. |
| SRC-014 | OpenAI — *Prompt engineering* (documentation, 2023) · [link](https://platform.openai.com/docs/guides/prompt-engineering) | Official guide covering system messages, role assignment, formatting, and few-shot patterns. Second authoritative reference corroborating the technique taxonomy. |
| — | ⚠️ Source needed | Practitioner framing: prompt engineering as a discipline distinct from context engineering; the argument that system-level design matters more than prompt optimization at scale. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Practical skill for workflow design, system prompt authoring, and evaluation pipeline construction. Most useful when understood in relation to context engineering. |
| **Organizational** | The highest-adoption AI skill across knowledge-worker roles. Training in prompt engineering is the most common starting point for organizational AI literacy programs — and a good one, as long as it doesn't stop there. |
| **Client-facing** | The entry point for most people's AI skill development. Tangible, learnable, immediately applicable — and a gateway to understanding why context and system design matter. |
| **LLM-native** | Foundation skill, but deliberately not the ceiling. This wiki's design philosophy assumes practitioners have moved beyond prompt-level optimization toward context and system design. |

---

*Last updated: v1.1 · May 2026*
