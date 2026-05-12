<p align="center">
  <img src="assets/robot.png" alt="Applied AI Concepts" width="220">
</p>

<h1 align="center">applied-ai-concepts</h1>

<p align="center">A persistently maintained AI literacy resource — foundational concepts for practitioners who design, deploy, and govern AI systems.</p>

---

## What this is

This repository is an AI literacy resource. It covers the concepts that matter when designing, deploying, or governing AI systems — written for people who need to understand AI at a working level: practitioners, governance professionals, and anyone accountable for the consequences of AI in their organization.

Each entry is built to compound over time: definitions evolve, cross-references sharpen, and contradictions are flagged rather than glossed over. This is not a glossary of buzzwords. It is a working map of how AI systems actually behave — and what that means for the people responsible for them.

**Data governance perspective.** This wiki treats AI and data governance as inseparable. Entries are written to surface the accountability, auditability, and control implications of each concept — not just the technical ones.

**Methodology.** Entries are built on the persistent synthesis model developed by Andrej Karpathy and extended by practitioners: source documents are inputs; the wiki is the output. New sources are synthesized into existing entries rather than appended. Contradictions are resolved and documented, not accumulated.

---

## Design philosophy

**Persistent synthesis over retrieval.**
New sources are synthesized into existing entries, not appended. The wiki is the output; source documents are inputs. Inspired by Karpathy's LLM Wiki model — *stop re-deriving, start compiling.*

**Context as leverage.**
The quality of any AI interaction is bounded by the quality of context it receives. Understanding *why* changes how you design systems, not just how you prompt them.

**Governance lives in the design.**
Every entry surfaces the control, accountability, and oversight implications of a concept. AI literacy without governance awareness is incomplete.

**Explicit over implicit.**
Assumptions, confidence levels, and knowledge gaps are surfaced in every entry. Uncertainty is documented, not hidden.

---

## Concepts

### Foundations
*How models behave — and why that behaviour matters*

| Concept | One-line essence | Status |
|---|---|---|
| [Hallucination](concepts/hallucination.md) | AI models generate plausible-sounding content that is factually incorrect — confidently and without warning | ✅ v1.1 |
| [Black Box](concepts/black-box.md) | An AI system whose internal reasoning process cannot be observed or interpreted — even when its outputs can | ✅ v1.0 |

### Interaction & Design
*How you work with models effectively*

| Concept | One-line essence | Status |
|---|---|---|
| [Context Engineering](concepts/context-engineering.md) | Designing what an AI model receives is as important as the model itself | ✅ v1.1 |
| [Prompt Engineering](concepts/prompt-engineering.md) | Structuring inputs to consistently elicit useful, accurate, and safe model outputs | ✅ v1.1 |

### System Architecture
*The control layer that makes models governable*

| Concept | One-line essence | Status |
|---|---|---|
| [Harness Paradigm](concepts/harness-paradigm.md) | Intelligence and control are separate layers — governance lives in the harness | ✅ v1.1 |
| [AI Agent](concepts/ai-agent.md) | A language model that doesn't just respond — it plans, acts, and iterates across multiple steps | ✅ v1.0 |
| [Retrieval-Augmented Generation (RAG)](concepts/rag.md) | A technique that grounds model outputs in retrieved, verifiable information | ✅ v1.1 |

### Knowledge & Memory
*How knowledge persists, degrades, and stays fit for use*

| Concept | One-line essence | Status |
|---|---|---|
| [Persistent Synthesis](concepts/persistent-synthesis.md) | Knowledge compounds when contradictions are resolved, not accumulated | ✅ v1.2 |
| [Data Quality](concepts/data-quality.md) | The fitness of data for its intended use — and the upstream constraint on every AI system built on it | ✅ v1.0 |

### Human Oversight
*Humans in control by design — not by assumption*

| Concept | One-line essence | Status |
|---|---|---|
| [Human-in-the-Loop (HITL)](concepts/human-in-the-loop.md) | A design pattern that keeps humans as decision authorities at critical points | ✅ v1.1 |

### Observability & Governance
*Making AI system behaviour visible and accountable*

| Concept | One-line essence | Status |
|---|---|---|
| [Observability](concepts/observability.md) | The ability to understand what an AI system is doing — and reconstruct why — from the outside | ✅ v1.0 |

---

## Governance & Observability Notes

Practical notes on what to control, monitor, and be accountable for — organized by theme across the core concepts.

| Note | Covers |
|---|---|
| [Governance & Observability](notes/governance-and-observability.md) | Verification · Context governance · System control · Accountability checklist |

---

## Glossary

A quick-reference index of all terms with one-line definitions: [glossary/index.md](glossary/index.md)

---

## Using this as context

The concepts in this wiki are designed to be used as structured context in your own AI projects — not just read. Each entry is self-contained, schema-consistent, and written to be machine-readable as well as human-readable.

**Clone or download**
```bash
git clone https://github.com/luispsalas/applied-ai-concepts.git
```
Or download as a ZIP from the repository's main page (Code → Download ZIP).

**Obsidian**
Copy the `/concepts/` and `/glossary/` directories into your Obsidian vault. The entries use standard markdown and will render as-is. Internal links follow standard markdown format and will resolve within the vault. Useful as a reference layer alongside your own project notes.

**LogSeq**
Import the `/concepts/` directory into a LogSeq graph. Entries are flat markdown files with no proprietary syntax — they will load without modification.

**Claude Projects**
Upload individual concept files or the full `/concepts/` directory as project knowledge. The model will use the shared vocabulary and governance framing as context across your conversations.

**ChatGPT (custom GPTs)**
Add concept files as knowledge sources when configuring a custom GPT. The `glossary/index.md` file is particularly useful as a lightweight single-file attachment for non-technical audiences.

**Cursor / Windsurf / AI-assisted editors**
Add the `/concepts/` directory to your project workspace. These editors will index the files and make them available as context when generating or reviewing code that involves AI system design decisions.

**RAG pipelines (LangChain, LlamaIndex, etc.)**
The `/concepts/` directory works as a document collection out of the box. Each file is a discrete, well-structured chunk — no pre-processing required before embedding.

---

## Versioning

Each entry carries a version number and last-updated date. The repository follows a simple model:

- `v1.x` — initial publication and refinements
- `v2.x` — cross-reference layer and additional concepts
- `v3.x` — audience rendering and glossary automation

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## Status

**Phase 1 ✅:** 11 concepts published across 6 categories — all sourced, versioned, and with governance notes sections. Standalone governance & observability notes doc live.
**Phase 2 (current):** Expanding concept base · glossary rendering · cross-reference layer.
**Phase 3:** Manifesto drafted from wiki principles.
