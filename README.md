<p align="center">
  <img src="assets/robot.png" alt="Applied AI Concepts" width="120">
</p>

<h1 align="center">applied-ai-concepts</h1>

<p align="center">A persistently maintained AI literacy resource — foundational concepts for practitioners who design, deploy, and govern AI systems.</p>

---

## Glossary

Browse all published terms in a single alphabetical list, with one-line definitions and links to full entries: [glossary/index.md](glossary/index.md)

---

## What is this?

This repository is an [AI literacy](concepts/ai-literacy.md) resource that explains the concepts behind designing, using, and governing AI systems. It is written for practitioners, governance teams, and anyone responsible for AI-related decisions and outcomes in their organization.

### How it works

This wiki is continuously refined over time. New source materials are integrated into existing entries instead of simply added on top. Definitions evolve, links between concepts become clearer, and conflicting perspectives are identified and documented rather than ignored.

Content is AI-assisted and periodically human-reviewed. Each published entry is validated and supported by maintained source references.

### Data governance perspective

This wiki treats AI and data governance as closely connected. Alongside technical explanations, entries also highlight accountability, auditability, risk, observability, and control considerations relevant to real-world organizations.

→ [Governance & Observability Notes](notes/governance-and-observability.md)

### Using the glossary in projects

The glossary can also be downloaded as a context package for AI and governance-related projects. It can help support governance-aware implementations, best practices, observability initiatives, and shared terminology across teams.

→ See the [Using this as context](#using-this-as-context) section for setup instructions.

---

## Design philosophy

> <img src="https://www.readmecodegen.com/api/social-icon?name=arrowRight&size=32" height="16"> **Persistent synthesis over retrieval.**  
> New sources are synthesized into existing entries, not appended. The wiki is the output; source documents are inputs. Inspired by Karpathy's LLM Wiki model — *stop re-deriving, start compiling.*

> <img src="https://www.readmecodegen.com/api/social-icon?name=arrowRight&size=32" height="16"> **Context as leverage.**  
> The quality of any AI interaction is bounded by the quality of context it receives. Understanding *why* changes how you design systems, not just how you prompt them.

> <img src="https://www.readmecodegen.com/api/social-icon?name=arrowRight&size=32" height="16"> **Governance lives in the design.**  
> Every entry surfaces the control, accountability, and oversight implications of a concept — AI literacy without governance awareness is incomplete.

> <img src="https://www.readmecodegen.com/api/social-icon?name=arrowRight&size=32" height="16"> **Explicit over implicit.**  
> Assumptions, confidence levels, and knowledge gaps are surfaced in every entry. Uncertainty is documented, not hidden.

---

## How are entries written?

Each concept is explained through several complementary "lenses" within a single entry, so readers can understand both the idea itself and its practical implications.

- **One-line essence:** A short, memorable explanation of the concept designed for quick understanding and easy reference.

- **Technical definition:** A more precise explanation of how the concept works, using accurate terminology and clarifying differences between related concepts.

- **Plain-language version:** The same idea explained in simpler, non-technical language for business teams, decision-makers, and non-engineering audiences.

- **AI literacy notes:** Practical guidance on why the concept matters in real organizations. It includes common misunderstandings, workflow impacts, and what teams should pay attention to when adopting AI.

- **Governance notes:** The accountability, oversight, risk, and control considerations connected to the concept. Entries highlight key governance questions, common failure modes, recommended practices, and the organizational roles typically responsible for oversight.

---

## Concepts

### Foundations
*How models behave — and why that behavior matters*

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
| [Grounding](concepts/grounding.md) | Anchoring model outputs to specific, verifiable sources — reducing hallucination by giving the model something real to reason from | ✅ v1.0 |

### Human Oversight
*Humans in control by design — not by assumption*

| Concept | One-line essence | Status |
|---|---|---|
| [Human-in-the-Loop (HITL)](concepts/human-in-the-loop.md) | A design pattern that keeps humans as decision authorities at critical points | ✅ v1.1 |

### Reliability & Quality
*Measuring and maintaining what AI systems actually do*

| Concept | One-line essence | Status |
|---|---|---|
| [Evaluation (AI Systems)](concepts/evaluation.md) | The structured practice of measuring whether an AI system does what it is supposed to do — before deployment and continuously in production | ✅ v1.0 |

### Observability & Governance
*Making AI system behavior visible and accountable*

| Concept | One-line essence | Status |
|---|---|---|
| [Observability](concepts/observability.md) | The ability to understand what an AI system is doing — and reconstruct why — from the outside | ✅ v1.0 |
| [AI Governance](concepts/ai-governance.md) | The frameworks, policies, and accountability structures that determine who decides how AI systems behave — and who is answerable when they don't | ✅ v1.0 |

### Organizational Readiness
*The human and organizational conditions for responsible AI adoption*

| Concept | One-line essence | Status |
|---|---|---|
| [AI Literacy](concepts/ai-literacy.md) | The competencies required to engage with, use, and govern AI systems responsibly — at an individual, team, and organizational level | ✅ v1.0 |

---

## Governance & Observability Notes

Practical notes on what to control, monitor, and be accountable for — organized by theme across the core concepts.

| Note | Covers |
|---|---|
| [Governance & Observability](notes/governance-and-observability.md) | Verification · Context governance · System control · Accountability checklist |

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
**Phase 2 (current):** 15 concepts published across 8 categories · glossary rendering · cross-reference layer.
**Phase 3:** Manifesto drafted from wiki principles.
