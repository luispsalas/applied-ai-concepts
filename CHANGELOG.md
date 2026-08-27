# Changelog

## v1.5.3 — August 2026

**An open invitation to contribute, made visible.**

- CONTRIBUTING.md has always documented how to propose a term, flag an error, or supply a missing source — but the README linked it only inside the sourcing section, so a reader had no visible reason to think contributions were wanted. New "Can I suggest a term or a correction?" section surfaces the four issue labels and states plainly that disagreement is in scope.
- It also states what doesn't change: nothing merges automatically, every change is human-reviewed, and new claims need sources like any other.

---

## v1.5.2 — August 2026

**Authorship declared, not just disclaimed.**

- The README previously said only that content is "AI-assisted and periodically human-reviewed" — an honest claim, but an unquantified one, and the kind of vague disclosure this wiki's own entries on accountability and explainability argue against. It now points to a structured [authorship declaration](https://luispsalas.github.io/authorship-meter/declarations/applied-ai-concepts.html) breaking the human/AI contribution down across five process stages.
- New `## Authorship` section stating what the declaration covers: the wiki as a whole at a named release version, not any single entry, re-assessed at each minor release.
- The declaration is hosted externally and linked, never embedded or copied here, so there is one source of truth that can't silently go stale.

---

## v1.5.1 — July 2026

**Types of AI Systems updated to v1.1 — General-Purpose AI (GPAI) folded in as a named regulatory category.**

- `types-of-ai-systems` — v1.1: adds an explicit definition of general-purpose AI (GPAI) under the EU AI Act (Art. 3(63)) — a model trained on broad data at scale with obligations that scale with capability rather than attach to a specific use case. New AI literacy note: GPAI obligations attach to the model, not the use.
- This closes a tracker item: a standalone "General-Purpose AI (GPAI)" term was folded into this entry rather than kept separate, since it's a category within the existing taxonomy, not a distinct concept.
- Also folded (tracker only, not yet published): "Deceptive Alignment (Alignment Faking)" folded into the not-yet-drafted "Alignment (AI Systems)" entry's essence, for the same reason.

---

## v1.5 — July 2026

**3 fast-follow concepts published — a general-audience security term, a common failure people already name, and a privacy pairing for Data Minimization.**

- `prompt-injection` — v1.0 (direct vs. indirect injection; the top-ranked LLM application security risk per OWASP)
- `context-window` — v1.0 ("it forgot / hit its limit"; the "lost in the middle" recall effect)
- `privacy-ai-systems` — v1.0 (broader than Data Minimization; AI-specific training-data memorization risk)

**Source registry:** 6 sources added (SRC-146–151) — Greshake et al. and Perez & Ribeiro (indirect/direct prompt injection), OWASP Top 10 for LLM Applications, Liu et al. ("Lost in the Middle"), Carlini et al. (training-data extraction), NIST Privacy Framework 1.1. The NIST source is an unfinalized Initial Public Draft — cited only for its general direction, no section numbers or exact wording treated as settled, and flagged in the Sources table for review once a final version ships.

---

## v1.4 — July 2026

**3 foundational "grounding" concepts published — the terms the rest of the wiki assumes.**

- `large-language-models` — v1.0 (Transformer, next-token prediction, the foundation-model framing)
- `determinism-vs-probabilism` — v1.0 (why the same prompt gives different answers; temperature; inference reproducibility)
- `system-prompt` — v1.0 (the unseen instruction layer; a soft control and a versioned governance artifact)

**Source registry:** 5 sources added (SRC-141–145) — Vaswani et al. (Transformer), Zhao et al. (LLM survey), Bommasani et al. (foundation models), Holtzman et al. (nucleus sampling), He / Thinking Machines Lab (inference nondeterminism).

---

## v1.3.1 — July 2026

**Harness Paradigm updated to v1.3 — harness engineering named as a discipline.**

- `harness-paradigm` — v1.3: distinguishes the harness *paradigm* (the architectural claim that intelligence and control are separate layers) from harness *engineering* (the practice of designing, versioning, and iterating the control layer). Adds the *agent = model + harness* formulation and the harness-gap argument, plus a fifth AI literacy note on the failure-driven ratchet — constraints earned from observed failures rather than anticipated ones.
- Governance notes gain a matching watch-for (configuration that accretes instead of ratcheting) and practice (tie each constraint to the failure that motivated it).
- **SRC-071** (Osmani, *Agent Harness Engineering*, O'Reilly Radar) now cited. It had been registered and reverse-indexed to this entry in the source registry without ever being cited in the file — a dangling reference, now resolved.
- Related concepts: `AI Agent` link fixed (previously plain text despite the entry existing); Guardrails, Failure Modes, and Memory cross-links added.

---

## v1.3 — July 2026

**6 new concepts, standards-grounded definitions, and glossary backfill.**

**6 new concepts published:**
- `ai-use-case` — v1.0 (definition composed from ISO/IEC/IEEE 24765 "use case" + ISO/IEC 22989 "AI system" + ISO/IEC TR 24030 documentation structure — each verified against standard text)
- `guardrails-ai-systems` — v1.0 (peer-reviewed anchor: NeMo Guardrails, EMNLP 2023)
- `types-of-ai-systems` — v1.0 (ISO/IEC 22989 vocabulary + OECD Classification Framework + EU AI Act risk tiers)
- `domain` — v1.0
- `knowledge-base` — v1.0
- `memory-ai-systems` — v1.0

**Source registry:** 8 sources added (SRC-133–SRC-140), including three international standards (ISO/IEC 22989, ISO/IEC TR 24030, ISO/IEC/IEEE 24765) and reference surveys for guardrails, domain specialization, agent memory, and RAG.

**Glossary backfill:** the 4 concepts published June 2026 (`bias-ai-systems`, `data-minimization`, `explainability-xai`, `failure-modes-ai-systems`) are now indexed in the glossary — they were published without a glossary/changelog update.

---

## v1.2.1 — June 2026

**4 new concepts published** (recorded retroactively — not logged at publish time):
- `bias-ai-systems` — v1.0
- `data-minimization` — v1.0
- `explainability-xai` — v1.0
- `failure-modes-ai-systems` — v1.0

Also: source-ID reconciliation audit across all entries (SRC-129–132 added, SRC-009 restored); contemporary responsibility-gap scholarship added to `human-responsibility-in-ai-use` (v1.1).

---

## v1.2 — May 2026

**Governance layer, 5 new concepts, source verification, and README restructure.**

**Governance notes added to all 6 original entries:**
- Each concept now includes a `## Governance notes` section: core accountability question, failure modes to watch for, actionable practices, named accountability owner, and link to the standalone governance doc
- New standalone document: `/notes/governance-and-observability.md` — cross-cutting accountability checklist and observability signals across all concepts

**Source quality upgrade:**
- All 6 original entries: vague citations replaced with SRC-ID format traceable to Wiki-Sources registry
- Remaining unverified claims flagged `⚠️ Source needed` rather than left as silent assumptions
- SRC-018 author corrected: Birgitta Böckeler (not Martin Fowler), April 2026

**5 new concepts published:**
- `rag` — v1.1 (includes temporal blindness failure mode; SRC-028: Alexander, Emmimal P., 2026)
- `ai-agent` — v1.0
- `black-box` — v1.0
- `data-quality` — v1.0
- `observability` — v1.0

**README restructured:**
- Concepts section reorganized into 6 categories: Foundations · Interaction & Design · System Architecture · Knowledge & Memory · Human Oversight · Observability & Governance
- Design philosophy and What this is sections rewritten to reflect AI literacy focus, Karpathy backbone attribution, and data governance perspective

---

## v1.1 — April 2026

**All 6 core concepts fully drafted.**

- `hallucination` — v1.0
- `human-in-the-loop` — v1.0
- `harness-paradigm` — v1.0
- `persistent-synthesis` — v1.0
- `prompt-engineering` — v1.0
- Glossary index updated with full one-line essences for all concepts

---

## v1.0 — April 2026

**Initial publication.**

- Repository created with core structure: `/concepts`, `/glossary`, `README.md`
- 6 concepts established:
  - `context-engineering` — fully drafted (v1.0)
  - `hallucination` — placeholder
  - `human-in-the-loop` — placeholder
  - `harness-paradigm` — placeholder
  - `persistent-synthesis` — placeholder
  - `prompt-engineering` — placeholder
- Glossary index created
- Design philosophy documented in README

**Phase 1 goal met:** repository live with 1 fully drafted concept and 5 structured placeholders ready for synthesis.
