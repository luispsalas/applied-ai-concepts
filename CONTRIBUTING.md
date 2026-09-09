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

**Six outcomes:**

| Status | Meaning | What happens |
|---|---|---|
| `established` | Recognized term of art, in independent use | Publish normally |
| `emerging` | Real and useful, definitions still vary | Publish with the status shown, and say what is unsettled |
| `house` | This wiki's own label for something sources call other things | Publish only if the entry says so plainly and names what to cite instead |
| `vendor` | Originated with one vendor | **Do not publish under the vendor's term.** Publish the concept under a neutral name, citing the vendor as one implementation |
| `declined` | Not a term at all — a product name, a feature name, or a phrase with no stable meaning | **Do not publish, under any name.** The row stays in the register with the reason, so the decision is visible rather than silent |
| `covered` | A real term the corpus already covers under another name | **Do not publish separately.** Add it as an alias of the entry that covers it — the register then links there, so the term stays findable without duplicating the entry |

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

---

## Maintenance

A corpus this size decays in ways that are invisible from inside a single entry. Three tiers, by what each check needs and how fast the thing it watches actually moves.

### Every publish — automatic, blocking
`python3 scripts/build.py check` — fails the publish on schema gaps, README/glossary/count desync, unresolved links, alias collisions, unknown tags, a term status that disagrees with its visible line, an unparseable confidence rating, and any disagreement between the tracker export and the entries. **It also fails on a non-Latin script or invisible character anywhere in published content** — entries, notes, README, CONTRIBUTING and the generated glossary. Accented Latin, Greek and symbols are deliberately not flagged; CJK, Cyrillic (the homoglyph risk — U+0430 renders identically to a Latin `a`), Hebrew, Arabic, Devanagari, Thai, Hangul and zero-width characters are. Including the generated register is what catches a stray character that entered through a **sheet cell** rather than a file. `export-tracker.py` sweeps both sheets on every run for the same thing, because a registry cell reaches the repo only by being retyped and nothing else looks at it. Then the numbered steps in the publishing workflow: cross-reference sweep, tracker re-sort.

**Most historical drift checks are gone rather than automated.** Essence, version and count drift used to need their own checks; those fields are now *derived* from entry front-matter, so there is nothing left to drift. Writing a check for them today would be dead code.

### Every publish that cites a reused source — `python3 scripts/citecheck.py <new files>`
**The only check that can catch a wrong *referent*.** It extracts every `| SRC-NNN | …` row from the files you name and compares each against how the same ID is rendered elsewhere in the corpus, reporting `DIFFERS` (exit 1) when the form is one the corpus has never used.

Nothing else can catch this. A wrong-but-well-formed URL resolves, so the link checker passes it; a real-but-wrong ID exists in the registry, so the ID gate passes it; the schema is intact, so `build.py check` passes it. The failures it has caught were not typos but **misattributions** — an InfoQ article cited for a generalization paper, an ISO technical report cited for InstructGPT, a vendor blog cited for an evaluation paper. Each was plausible and pointed at a real but different source.

**It ranks candidate forms by frequency, and that is the whole reason it is a script rather than a grep.** Older IDs carry several rendered forms — `citecheck.py --all` reports **96 of 262 IDs with more than one** — so comparing against whichever sorts first alphabetically produces false positives, and a false positive is how a check earns being skimmed. The *dominant* form is the corpus's actual convention.

A `NEW` line is not a defect; it means the ID is cited nowhere else, so the corpus cannot vouch for it — **verify that one against the registry by hand.**

**`citecheck.py --all --substantive` is the periodic version**, and it answers a question that comes up whenever the raw drift number looks alarming: *which of these actually matter?* It reports only IDs whose variants point at a **different URL**, because that is the only difference that can mean a different document — a preprint cited over the published paper, or a superseded draft over the final edition. Both defects found this way in Sep 2026 were of exactly that kind.

**Everything else is left alone deliberately.** Two citations sharing a URL cite the same document however differently they name it, and the corpus carries ~93 IDs with more than one rendered form for reasons that are purely presentational — a dropped subtitle, an expanded abbreviation, `&` for `;`. **Normalizing those is not worth a 130-file diff**: the ranking in the per-publish check already steers new citations to the dominant form, so the drift stops growing without a cleanup pass. The filter's calibration is the evidence — treating any title difference as substantive flagged 26 IDs, prefix-tolerance brought it to 13, keying on URL gives the handful that are real.

### Monthly — `python3 scripts/maintain.py offline`
Report-only, no network. US-English sweep (quotations and Sources rows excluded), Sources-table completeness, SRC-IDs cited in prose but missing from a Sources table, and **archive state** (below).

### Quarterly — `python3 scripts/maintain.py links`
The above plus HTTP liveness on every cited source URL, via curl. Slow. Publishers that block automated clients are skipped by name rather than re-raised every quarter.

### Semi-annual — `python3 scripts/maintain.py vocab`
**Term review against an outside list.** Reports every term in `scripts/vocabulary.txt` that is not an entry, not an alias, not in the tracker, and never mentioned in any entry.

**Why this exists, and why the other signals cannot replace it.** The gap report counts unlinked prose mentions; the promise sweep reads Related-concepts bullets. **Both measure demand generated by text the corpus already wrote — so absence produces no signal at all.** In Sep 2026 *overfitting*, *underfitting* and *catastrophic forgetting* were found missing from 120 entries, not even appearing in *Fine-tuning*, and both signals scored them near zero. A corpus that never learned a word cannot generate demand for it.

Three rules govern the list, and the first is the one that matters:
- **It must come from outside** — a syllabus, a textbook index, a standards glossary. Regenerating it from the entries would make it agree with the corpus by construction and read clean forever.
- **It must be scoped, or it becomes noise.** The first draft was a general ML syllabus and returned 67 hits from 136 terms, most correctly out of scope. A term earns a place only if it could plausibly clear the exclusion above. *Overfitting* earns it; *learning rate* does not.
- **A hit is a prompt to judge, not an instruction to publish.** `covered` and `declined` are good outcomes, and each triaged term gets a tracker row.

**Expect the first run to be a backlog and later runs to be a delta.** Anything given a tracker row stops reporting, so the count decays toward zero and subsequent runs surface only vocabulary genuinely new to the field.

### Archive state — part of the monthly offline run
Reads `scripts/registry-archive.tsv`, regenerated by `export-tracker.py`. It reports one thing only: **sources whose archive lookup never concluded** — a rate-limited or errored check, as distinct from a source that genuinely has no snapshot.

**The distinction is the whole point.** Both leave an empty archive cell and look identical. One is a finished answer; the other is a question nobody came back to. A Wayback rate-limit once nearly recorded eleven archived sources as unarchived, and SRC-354 shipped with a deliberately empty cell that nothing else would have surfaced.

- **Only `unresolved` is reported as work.** Roughly half the registry has no record of an archive check at all; that is a coverage number printed to stderr, not a worklist. A check that lists 176 rows is one nobody reads.
- **A missing input is reported as `COULD NOT RUN`, never as clean** — the same rule the check itself enforces.
- Classification reads **both** the `Risk Flags` and `Version / Commit` columns, because the "checked N forms, none archived" note is written to one or the other and nothing says which.

### Manual, quarterly — the registry
Not scriptable from here: the Sources sheet is reached through an MCP, not a library.
- Reverse index (`col L`) in **both** directions — regenerate with `build.py report` and compare; do not hand-edit.
- `Outstanding` ↔ `Sources` promotion drift.
- **Export the tracker to CSV.** The repo has git history, a remote and a local clone. The tracker is a single Sheet whose only recovery path is Google's version history, and it holds pertinence scores, statuses and essences that exist nowhere else. It is the one thing here without a backup.

### Two standing rules
- **Nothing in `maintain.py` blocks a publish.** Every check it runs needs a human call: a British spelling inside a quoted EU or ISO passage is *correct*, and a 403 is usually a bot policy rather than a dead link.
- **A check must never let its failure path and its negative result be the same value.** No answer is not the same as no. Return found / absent / could-not-determine and make the third one loud — this is why the archive check exists at all.
- **Suspect the checker before the corpus.** The first version of the liveness check reported 146 live sources as dead — Python's urllib had no CA bundle. If a check suddenly fails everywhere, that is the shape of an environment problem.
