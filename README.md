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

| Concept | One-line essence | Status |
|---|---|---|
| [Context Engineering](concepts/context-engineering.md) | Designing what an AI model receives is as important as the model itself | ✅ v1.1 |
| [Hallucination](concepts/hallucination.md) | AI models generate plausible-sounding content that is factually incorrect — confidently and without warning | ✅ v1.1 |
| [Human-in-the-Loop (HITL)](concepts/human-in-the-loop.md) | A design pattern that keeps humans as decision authorities at critical points | ✅ v1.1 |
| [Harness Paradigm](concepts/harness-paradigm.md) | Intelligence and control are separate layers — governance lives in the harness | ✅ v1.1 |
| [Persistent Synthesis](concepts/persistent-synthesis.md) | Knowledge compounds when contradictions are resolved, not accumulated | ✅ v1.2 |
| [Prompt Engineering](concepts/prompt-engineering.md) | Structuring inputs to consistently elicit useful, accurate, and safe model outputs | ✅ v1.1 |

---

## Glossary

A quick-reference index of all terms with one-line definitions: [glossary/index.md](glossary/index.md)

---

## Versioning

Each entry carries a version number and last-updated date. The repository follows a simple model:

- `v1.x` — initial publication and refinements
- `v2.x` — cross-reference layer and additional concepts
- `v3.x` — audience rendering and glossary automation

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## Status

**Phase 1 (current):** Core repository published with 6 foundational concepts, all sourced and versioned.
**Phase 2:** Cross-reference layer + governance notes + 2–3 additional concepts.
**Phase 3:** Manifesto drafted from wiki principles.
