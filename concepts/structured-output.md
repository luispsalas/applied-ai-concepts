<!--meta
category: System Architecture
short: Making a model emit machine-parseable output that conforms to a schema — a guarantee about shape that is routinely mistaken for a guarantee about content
aliases: [structured generation, JSON mode, JSON output, schema-constrained output, constrained decoding, guided generation, grammar-constrained decoding, schema conformance, typed output]
tags: [Architecture, Evaluation, Prompting]
established: established
-->
# Structured Output

> **Term status — Established.** In independent use across every major model provider, across open-source inference libraries, and in peer-reviewed research that studies it as a named technique. Cleared on the **usage route**: the mechanism is implemented independently in competing systems and the schema language it depends on is an open specification owned by no vendor.

## One-line essence
Getting a model to emit output a program can parse, conforming to a declared schema — which guarantees the shape of the answer and says nothing whatever about whether it is right.

---

## Technical definition

Structured output is the practice of constraining a model's generation so the result conforms to a machine-readable format — most often JSON against a JSON Schema, sometimes XML, a grammar, or a regular expression.

**There are two fundamentally different ways to get it, and the difference matters for what you may rely on:**

- **Ask and validate.** Instruct the model to produce JSON, parse the result, and retry or repair on failure. Conformance is probabilistic; the failure mode is a parse error, which is at least visible.
- **Constrain the decoding.** At each generation step, mask the vocabulary so only tokens that keep the output valid can be sampled. Willard and Louf reformulate this as transitions between the states of a finite-state machine, allowing an index over the model's vocabulary — a model-agnostic approach that adds little overhead and **guarantees** the structure of the generated text.

**Constrained decoding is a generation-time guarantee, which is categorically different from validation after the fact.** It is not a [guardrail](guardrails-ai-systems.md): a guardrail inspects an output and decides whether to allow it, while constrained decoding makes the invalid output unreachable. Both are useful; only one can be described as a guarantee.

**Structured output is the general case of which [function calling](tool-use.md) is one application.** A tool call is a structured object naming a function and binding its parameters — the same machinery, pointed at an action rather than at a datum. The concept is broader than tools: extraction, classification, scoring and inter-service payloads all use it with no tool involved ([agent interoperability](agent-interoperability-a2a.md)).

**The governance point, and the reason the entry exists: schema conformance is not correctness.** A response that validates perfectly against its schema can be entirely fabricated. **Structure eliminates parse failures, which were the visible errors, and leaves the invisible ones untouched** — a well-typed hallucination arrives looking like a database row ([hallucination](hallucination.md)). Worse, a schema field named `confidence` produces a number that is generated like every other token and is not a measurement of anything ([confidence vs accuracy](confidence-vs-accuracy.md), [concealing uncertainty](concealing-uncertainty.md)).

**And the format is not free.** Tam et al., comparing models restricted to structured formats against free-form generation on the same tasks, report **a significant decline in reasoning ability under format restrictions, with stricter constraints producing greater degradation.** Machine-readability is purchased with reasoning quality. The trade is rarely measured, because the constrained pipeline is usually the only one anyone runs ([evaluation](evaluation.md)).

**The schema is a governed artifact.** It is a versioned contract between a model and everything downstream: change a field's meaning and every consumer silently reinterprets history. JSON Schema is an open specification with its own draft history — which is why the version belongs in the record ([data provenance and lineage](data-provenance-lineage.md)).

---

## Plain-language version

Models produce prose. Programs need fields. Structured output is how you get the second from the first: you declare the shape you want — these keys, these types, this one must be present — and the model returns something a program can read directly instead of text a human has to interpret.

There are two ways to do it, and they are not equally strong. You can *ask* for the shape and check what comes back, retrying when it is malformed. Or you can *constrain the model as it writes*, so that at every step only the characters that keep the result valid are even available to it. The second cannot produce an invalid result — not "rarely does," cannot.

That sounds like a solved problem, and here is where it goes wrong.

**Getting the shape right is not getting the answer right.** A perfectly formed record with every required field present can be completely made up. What structure removes is the *visible* class of errors — the ones that used to crash your parser and get noticed. What remains is the invisible class: confident, well-typed, wrong. **You have not reduced the errors; you have removed the ones that announced themselves.**

The sharpest version of this is a field called something like `confidence`. It looks like the model telling you how sure it is. It is a number the model generated the same way it generated everything else, and it is not a measurement.

**There is also a cost that surprises people.** Researchers compared models answering freely against the same models forced into structured formats, and found reasoning got measurably worse under the constraint — and worse still as the constraint got tighter. Making the output easy for a machine to read makes the thinking behind it a little worse. That is usually a trade worth making. It is not usually a trade anyone measures, because once the pipeline is built, nobody runs the unconstrained version again.

Finally: the schema is a contract, not a config detail. Everything downstream depends on what a field means. Change that meaning quietly and every consumer keeps reading old data with new assumptions.

---

## AI literacy notes

1. **Constrained decoding makes invalid output unreachable**; asking and validating only makes it rarer.
2. **Schema conformance is not correctness** — a valid object can be entirely fabricated.
3. **Structure removes the visible errors** and leaves the invisible ones in place.
4. **A `confidence` field is a generated token**, not a measurement.
5. **Format restriction measurably degrades reasoning**, and stricter formats degrade more.
6. **Function calling is a special case** of structured output, not the other way round.
7. **It is not a guardrail** — one constrains generation, the other inspects a result.
8. **The schema is a versioned contract** with everything downstream.
9. **JSON Schema is an open standard** with its own draft history; name the version.

---

## Governance notes

**Core question:** What is actually guaranteed about this output — that it parses, or that it is true — and does anyone downstream know the difference?

**Watch for:**
- Schema validation described or treated as quality assurance ([verification](verification.md))
- A `confidence`, `score` or `certainty` field consumed as though it were calibrated ([confidence vs accuracy](confidence-vs-accuracy.md))
- Structured extraction feeding metrics or decisions with no accuracy measurement of the fields themselves ([generated variables](generated-variables.md))
- Reasoning quality never compared against an unconstrained baseline, so the format cost is unknown
- Schema changes shipped without versioning, silently reinterpreting historical records
- Enum fields that force a category on inputs that fit none, converting "unknown" into a confident label
- No representation for absence or refusal in the schema, so the model must invent a value
- Retry-on-parse-failure loops that mask a systematically failing prompt ([observability](observability.md))
- Structured output used to satisfy an interface while the underlying uncertainty is discarded at the boundary ([concealing uncertainty](concealing-uncertainty.md))

**Practice:**
- **Say which guarantee you have.** Constrained decoding guarantees shape; nothing in the pipeline guarantees content, and that distinction belongs in the documentation
- **Design the schema to permit honesty**: nullable fields, an explicit `unknown`, a refusal path. A schema with no way to say "not present" compels fabrication
- **Measure field-level accuracy separately from conformance rate** — a 100% conformance rate is compatible with any accuracy at all
- **Run the unconstrained baseline at least once** and record the difference, so the reasoning cost of the format is a known quantity rather than an assumption
- Version the schema, record the version with the data, and treat a change to a field's meaning as a breaking change ([model version and update](model-version-update.md))
- Do not model confidence as a schema field unless it is derived from something measurable; prefer omitting it to inviting misreading
- Validate at the consumer boundary as well as at generation — the schema is a contract, and contracts are checked at both ends
- **Log conformance failures rather than silently retrying**, so a degrading prompt or model is visible ([observability](observability.md))

**Key accountability owner:** whoever owns the schema — because the schema decides what the system is permitted to say, including whether it can say "I do not know," and that is a design decision with consequences no downstream consumer can undo.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanism is well documented with a widely used open implementation, the schema language is an open specification, and the format-cost finding is peer-reviewed at an EMNLP industry track with a direct constrained-versus-free comparison. **Two limits.** The degradation result is measured on a **2024 model generation and on reasoning tasks specifically** — the direction is the durable finding, the magnitude is not, and models trained more heavily on structured output may behave differently, so this entry states the trade without quoting a size. And the constrained-decoding paper is an arXiv preprint whose authors maintain the library it introduces, so its performance comparisons are an author's evaluation of their own system; the structural guarantee, which is what this entry relies on, follows from the method rather than from the benchmark. ⚠️ **A widely circulated "0% to 100%" improvement figure for a structured-output control layer was deliberately excluded**: it is n=10 against a mock model configured to fail most first attempts, so the baseline is guaranteed by construction.

---

## Related concepts

- [Tool Use](tool-use.md) — function calling as the action-shaped special case
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — inspecting an output, as against constraining generation
- [Hallucination](hallucination.md) — what a valid schema does nothing to prevent
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — why a `confidence` field is not a measurement
- [Concealing Uncertainty](concealing-uncertainty.md) — a schema with no way to express doubt
- [Generated Variables](generated-variables.md) — what extracted fields become once you compute on them
- [Verification](verification.md) — checking the content, not the shape
- [Prompt Engineering](prompt-engineering.md) — the ask-and-validate route
- [Agent Interoperability (A2A)](agent-interoperability-a2a.md) — structured payloads between systems
- [Determinism vs Probabilism](determinism-vs-probabilism.md) — why conformance had to be engineered rather than assumed
- [Evaluation (AI Systems)](evaluation.md) — where the unconstrained baseline belongs
- [Data Provenance / Lineage](data-provenance-lineage.md) — the schema version travelling with the data

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-339 | Willard, Brandon T.; Louf, Rémi — *Efficient Guided Generation for Large Language Models* (arXiv, 2023) · [link](https://arxiv.org/abs/2307.09702) | The mechanism and the entry's central distinction: reformulating generation as transitions between finite-state-machine states allows an index over the vocabulary, so schema-breaking tokens are never sampled — a **generation-time guarantee of shape**, model-agnostic and low-overhead. ⚠️ Preprint; the authors maintain the library it introduces. It guarantees shape only. |
| SRC-340 | Tam, Zhi Rui; Wu, Cheng-Kuang; Tsai, Yi-Lin; Lin, Chieh-Yen; Lee, Hung-yi; Chen, Yun-Nung — *Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models* (EMNLP Industry Track, 2024) · [link](https://arxiv.org/abs/2408.02442) | The cost: comparing structured-format generation against free-form on the same tasks, **a significant decline in reasoning ability under format restrictions, with stricter constraints producing greater degradation.** ⚠️ 2024 models and reasoning tasks specifically — cite the direction and re-measure the magnitude on your own models. |
| SRC-341 | JSON Schema project — *JSON Schema Specification (version 2020-12)* · [link](https://json-schema.org/specification) | The vendor-neutral contract language, registered so the entry describes schemas through an open standard rather than any provider's API — which is what makes a structured-output contract a reviewable, versioned artifact. ⚠️ A living specification with a draft history; record the version cited. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Practitioner grounding for structured output as the interface between an agent's reasoning and the systems around it, and for the retry and validation patterns built on it. ⚠️ Vendor-produced — used for the architectural framing only. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Measure field accuracy separately from conformance rate, run the unconstrained baseline once to price the format, and give the schema a way to say "unknown." |
| **Organizational** | Valid output is not correct output. Structure removes the errors that used to announce themselves and leaves the rest. |
| **Client-facing** | Explains why a tidy, complete-looking record from an AI system still needs checking — the tidiness was guaranteed, the content was not. |
| **LLM-native** | Function calling is a special case of this. A `confidence` field is a generated token. Constraining the format costs reasoning, and almost nobody measures how much. |

---

*Last updated: v1.0 · September 2026*
