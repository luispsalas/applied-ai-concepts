# applied-ai-concepts

A persistently maintained knowledge base of foundational AI and data concepts — written for practitioners who work with AI systems, not just use them.

---

## What this is

A structured reference for concepts that matter when designing, deploying, or governing AI systems. Each entry is built to compound over time: definitions evolve, cross-references sharpen, and contradictions are flagged rather than glossed over.

This is not a glossary of buzzwords. It is a working map of how AI systems actually behave — and what that means for the people responsible for them.

---

## Design philosophy

**Persistent synthesis over retrieval.**
New sources are synthesized into existing entries, not appended. The wiki is the output; source documents are inputs.

**Context as leverage.**
The quality of any AI interaction is bounded by the quality of context it receives. Understanding *why* changes how you design systems, not just how you prompt them.

**Explicit over implicit.**
Assumptions, confidence levels, and knowledge gaps are surfaced in every entry. Uncertainty is documented, not hidden.

---

## Concepts

| Concept | One-line essence | Status |
|---|---|---|
| [Context Engineering](concepts/context-engineering.md) | Designing what an AI model receives is as important as the model itself | ✅ v1.0 |
| [Hallucination](concepts/hallucination.md) | AI models generate plausible-sounding content that is factually incorrect | 🔲 Draft |
| [Human-in-the-Loop (HITL)](concepts/human-in-the-loop.md) | A design pattern that keeps humans as decision authorities at critical points | 🔲 Draft |
| [Harness Paradigm](concepts/harness-paradigm.md) | Intelligence and control are separate layers — governance lives in the harness | 🔲 Draft |
| [Persistent Synthesis](concepts/persistent-synthesis.md) | Knowledge compounds when contradictions are resolved, not accumulated | 🔲 Draft |
| [Prompt Engineering](concepts/prompt-engineering.md) | Structuring inputs to consistently elicit useful, accurate model outputs | 🔲 Draft |

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

**Phase 1 (current):** Core repository published with 6 foundational concepts.
**Phase 2:** Cross-reference layer + 2–3 additional concepts.
**Phase 3:** Manifesto drafted from wiki principles.
