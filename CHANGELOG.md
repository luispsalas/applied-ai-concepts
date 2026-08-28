# Changelog

## v1.9.1 — August 2026

**RACI updated to v1.1 — the AI-era application marked as contested, not settled.**

- Research for a parallel governance-asset project surfaced that whether an AI system belongs in a responsibility matrix at all is genuinely unresolved: practitioner frameworks published months apart take opposite positions, no standard admits AI systems as role-holders, and there is no peer-reviewed treatment of RACI-with-agents. The entry now says so.
- Confidence level split in two: the R/A distinction stays well grounded, while any *notation* for machine execution is flagged as in active development. Also notes the formal argument that above a threshold of autonomy, naming an accountable human buys completeness at the cost of foreseeability — a designated blame-holder rather than an accountable person.
- No claim was removed. The entry stops where the evidence stops rather than implying a settled practice exists.

---

## v1.9 — August 2026

**6 concepts published — completing the score-5 tier: the organizational and operational half of AI governance.**

- `human-ai-collaboration-model` — v1.0 (the division of labor as a design artifact; over-reliance and under-reliance as the two stable failures of leaving it unspecified)
- `model-data-drift` — v1.0 (data drift vs concept drift, and why nothing breaking is what makes it dangerous)
- `operational-readiness-ai` — v1.0 (whether you can *run* it, not whether it works; the model is the small part)
- `raci` — v1.0 (the system can hold Responsible; only a person can hold Accountable)
- `sycophancy-llms` — v1.0 (agreement carries no information — and it is rewarded by the training signal, not an incidental bug)
- `ai-management-system-iso-42001` — v1.0 (certifiable, voluntary, and not compliance — it certifies the process, not the product)

**Three distinctions these entries draw that are routinely collapsed elsewhere:** data drift is not concept drift and they need different remedies; ISO 42001 certification is not regulatory compliance and does not vouch for any model; and an AI system can be *Responsible* for a task while never being *Accountable* for it — which is where the responsibility gap opens in practice.

**Source registry:** 6 sources added (SRC-165–169 plus reuse), including four peer-reviewed anchors — Gama et al. on concept drift (ACM Computing Surveys), Sculley et al. on hidden technical debt (NIPS), Sharma et al. on sycophancy (ICLR), and Amershi et al. on human-AI interaction guidelines (CHI) — and ISO/IEC 42001:2023 itself, cited for scope and clause structure only, since the standard text is paywalled and was not read in full.

---

## v1.8 — August 2026

**AI Incident (Reporting) published — completing the score-5 governance cluster.**

- `ai-incident-reporting` — v1.0. Separates an **AI incident** (harm occurred) from an **AI hazard** (harm nearly occurred), using the OECD definitions — the near-miss being the cheaper and more abundant evidence that informal processes routinely discard. Sets out the EU AI Act Article 73 obligation with its tiered deadlines (15 days generally, 2 days for critical-infrastructure disruption, 10 where a person has died), the fact that the clock starts at *awareness* rather than diagnosis, and the aviation analogy behind public incident cataloguing.
- The entry makes its dependency explicit: an incident you cannot reconstruct from an audit trail is an incident you cannot report.

**Source registry:** 3 sources added (SRC-162–164) — EU AI Act Art. 73, the OECD's *Defining AI incidents and related terms*, and McGregor's peer-reviewed AAAI paper on the AI Incident Database. Article 73's deadlines were verified against the article text rather than taken from secondary summaries; the Commission's operational guidance was still in draft and is flagged as such.

---

## v1.7 — August 2026

**5 concepts published — a security cluster, plus the two entries that had been parked as unsourceable.**

- `jailbreak` — v1.0 (why safety training fails structurally: competing objectives and mismatched generalization; and why model refusal is the weakest possible boundary)
- `red-teaming` — v1.0 (manual and automated modes; findings are specific to a deployment and expire on every change)
- `data-leakage-ai-systems` — v1.0 (three distinct pathways — memorization, context leakage, cross-tenant — needing different controls)
- `permission-model-ai` — v1.0 (least privilege applied to AI: the enforcement point, not the prompt, is the control)
- `small-language-models` — v1.0 (size as a per-task decision; the governance shift comes from where the model runs, not how big it is)

**Jailbreak and prompt injection are now explicitly distinguished** — one attacks the model's safety behavior, the other the application's instruction hierarchy. They co-occur and are routinely conflated, but they call for different defenses.

**Source registry:** 5 sources added (SRC-157–161), including two peer-reviewed anchors — Wei et al. on how safety training fails (NeurIPS 2023) and Perez et al. on automated red teaming (EMNLP 2022) — and Saltzer & Schroeder's 1975 least-privilege paper, which grounds AI permission design in fifty-year-old security practice rather than treating it as a new discipline.

---

## v1.6 — August 2026

**3 concepts published — the agent action layer, and how models "think."**

- `multi-agent-systems` — v1.0 (orchestrator–workers; why coordination adds failure surface rather than removing it; per-agent attribution as a governance requirement)
- `tool-use` — v1.0 (the model requests, your system executes — and that boundary is where permission logic belongs)
- `reasoning-models` — v1.0 (test-time compute as a tunable dial; the trap of reading a reasoning trace as an explanation)

**Two terms folded in rather than kept separate.** *Function Calling* and *Model Context Protocol (MCP)* are covered inside Tool Use — function calling as the mechanism by which a model selects a tool and binds its parameters, MCP as the open standard for exposing tools through a common interface. Neither is a distinct concept from the capability itself.

**Source registry:** 5 sources added (SRC-152–156) — an IJCAI survey of LLM-based multi-agent systems, a production multi-agent case study, a tool-selection guide, Snell et al. on compute-optimal test-time scaling, and DeepSeek-R1 (peer-reviewed in Nature) on reasoning incentivized through reinforcement learning. Nine existing sources were reused rather than re-registered.

---

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
