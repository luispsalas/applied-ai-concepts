# Contributing

This wiki is maintained as a persistently synthesised knowledge base — new information is integrated into existing entries rather than appended. This document explains how the maintenance model works and how you can suggest additions or improvements.

---

## Maintenance model

**Human review is required before anything changes.** No entry is updated, added, or modified without explicit human approval. This is not a policy statement — it is structurally enforced: all changes go through pull request review before merging.

**Sources are required, not optional.** Every claim in this wiki must be traceable to a real source with a verifiable link. Vague attributions ("general consensus", "practitioner knowledge") are replaced with real sources or flagged `⚠️ Source needed` — a visible, upgradeable marker that makes knowledge gaps explicit rather than hiding them.

**Synthesis over accumulation.** When new information contradicts an existing entry, the contradiction is resolved and documented — not left to coexist. Both versions are not kept without annotation. This is the core principle behind the wiki's design, described in detail in the [Persistent Synthesis](concepts/persistent-synthesis.md) entry.

---

## How to suggest a new term or correction

Open a **GitHub Issue** with one of the following labels:

- `new-term` — you believe a concept is missing and should be added
- `correction` — an existing entry contains an error, a broken link, or an outdated citation
- `source` — you have a real source that could replace or support a `⚠️ Source needed` flag
- `discussion` — you want to raise a question about scope, framing, or accuracy

For new terms, include:
1. The term name (canonical English form)
2. A one-line essence (what it is in a single sentence)
3. Why it belongs here (what it adds that isn't covered by existing entries)
4. At least one real, verifiable source

For corrections, include the specific claim, the reason it's wrong or incomplete, and a source if you have one.

---

## What this wiki does not cover

- Vendor-specific features or product documentation
- Proprietary frameworks or internal tooling
- Terms that are well-defined elsewhere and add no distinctive governance, literacy, or design insight
- Buzzwords without stable technical meaning

If you're unsure whether something fits, open a `discussion` issue.

---

## Planned: automated proposal pipeline

A future version of this workflow will include a scheduled agent that monitors primary sources (academic publications, practitioner blogs, key authors) and proposes new terms or updates to existing entries as pull requests. Every proposal will still require human review before merging — the automation handles discovery and drafting; human judgment handles approval.

This is not yet implemented. When it is, the mechanics will be documented here.

---

## Entry schema

All entries follow a consistent schema:

| Section | Purpose |
|---|---|
| One-line essence | Single sentence — what the concept is |
| Technical definition | Precise, sourced definition |
| Plain-language version | Accessible explanation for non-technical readers |
| AI literacy notes | What practitioners need to understand and why it matters |
| Governance notes | Core accountability question, failure modes, practices, named owner |
| Confidence level | How well-established this concept and its framing are |
| Related concepts | Cross-links with typed relationship notes |
| Sources | SRC-ID table — all claims traceable to real sources |
| Audience relevance | How this concept applies across different reader types |

New entries must follow this schema in full.

---

*Maintenance model: human-reviewed, HITL-first, source-required.*
