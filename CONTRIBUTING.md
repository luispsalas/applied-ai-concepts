# Contributing

This wiki is maintained as a persistently synthesised knowledge base — new information is integrated into existing entries rather than appended. This document explains how the maintenance model works and how you can suggest additions or improvements.

---

## Maintenance model

**Human review is required before anything changes.** No entry is updated, added, or modified without explicit human approval. This is not a policy statement — it is structurally enforced: all changes go through pull request review before merging.

**Sources are required, not optional.** Every claim in this wiki must be traceable to a real source with a verifiable link. Vague attributions ("general consensus", "practitioner knowledge") are replaced with real sources or flagged `⚠️ Source needed` — a visible, upgradeable marker that makes knowledge gaps explicit rather than hiding them.

**Source IDs map to one source each.** Every `SRC-###` identifier corresponds to exactly one source in the master source registry. Before adding or reusing a citation, check the ID against the registry — never invent, guess, or reassign an ID inside an entry. This keeps the same ID from drifting to different sources across entries.

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

## Term status — the admission test

The field names things faster than it settles them. A term can be widely repeated and still mean something different in every source, and publishing those without comment would make this a list of buzzwords rather than a reference. So **every entry declares what kind of term it is**, on the entry itself, directly under the title.

This is a **separate question** from the entry's `## Confidence level`, and the two are deliberately not merged:

| | Asks | Example |
|---|---|---|
| **Term status** | Is this a real, recognized term? | *Cognitive Offloading* — yes, entirely standard |
| **Confidence level** | How good is the evidence for these claims? | *Cognitive Offloading* — weak; no longitudinal study exists |

They vary independently. A settled term can rest on thin evidence, and a term invented here can be assembled entirely from peer-reviewed work. One score cannot express both, and trying made earlier entries put "Established" in a field meant for evidence strength.

**Four checks, applied before drafting** — the cost of skipping them is a finished entry nobody can agree about:

1. Does the term appear in peer-reviewed work, a standard, or regulation — **by someone other than whoever coined it?**
2. **Filter the originator's own domains out of a search.** What is left? **Two different failures hide here, and they call for different actions:** *nothing found* means a clean coinage — a `house` label is honest and workable. *Something found, in unrelated fields* means *the phrase is already taken*, and a reader who searches it lands somewhere else entirely. **A collision is a much stronger argument for renaming than mere novelty is**, because the confusion is active rather than absent.
3. Is the meaning **stable** across independent uses, or does each source redefine it?
4. Does this wiki already cover the concept under an established name?

**Four outcomes:**

| Status | Meaning | What happens |
|---|---|---|
| `established` | Recognized term of art, in independent use | Publish normally |
| `emerging` | Real and useful, definitions still vary | Publish with the status shown, and say what is unsettled |
| `house` | This wiki's own label for something sources call other things | Publish only if the entry says so plainly and names what to cite instead |
| `vendor` | Originated with one vendor | **Do not publish under the vendor's term.** Publish the concept under a neutral name, citing the vendor as one implementation |

A fifth outcome — *not a term* — is a decline, recorded with its reason rather than silently dropped.

**All of it is public.** Status lives in the term tracker and is published, for every tracked term, in the [term register](glossary/register.md) — what was admitted, what is queued, what is still unassessed, and what was coined by a vendor and so will not appear under that name. The register is generated from the tracker export, never hand-written, and `build.py check` fails the publish if the export and the entries disagree about whether a term is published or what its status is.

**The status judges the concept, not the wording of the title.** Entry titles are editorial; many are descriptive compounds. The question a reader needs answered is whether the *thing* is real, not whether the exact phrase is a standard string.

**It is machine-checked.** `established:` is a required field in each entry's metadata block, and `build.py check` fails the publish if it is missing, holds an unknown value, or disagrees with the visible line on the entry.

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
