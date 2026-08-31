# Changelog

## v1.13 — August 2026

**3 concepts published — the last unpublished score-5 term, and the two entries the rest of the corpus had been pointing at.**

- `verification` — v1.0 (checking *this* output — and the finding that people check least on the problems that most need it)
- `agency-ai-systems` — v1.0 (how much a system may do without asking — granted by an organization, not possessed by the model)
- `alignment-ai-systems` — v1.0 (matching behavior to intent — and the prior question of whose intent)

**Verification's central claim is uncomfortable and well evidenced.** It is not that people should check more; it is that **verification is an economic decision and the economics run the wrong way.** People weigh the cost of checking against the cost of relying, and checking drops as task difficulty rises — so the hardest problems, where a system is least reliable, are the ones that get verified least (Vasconcelos et al., CSCW 2023). Two supporting findings sharpen it. A citation is not verification: only 51.5% of generated sentences were fully supported by their citations and only 74.5% of citations supported the statement they were attached to (Liu, Zhang & Liang, EMNLP 2023). And assistance can lower quality while raising confidence in it — participants with an AI coding assistant wrote significantly less secure code *and* were more likely to believe it was secure (Perry et al., CCS 2023). **The practice recommendation follows from the mechanism: reduce the cost of checking rather than demanding more of it.** Exhortation has no evidence behind it; making the source visible next to the claim does.

**The entry also draws a line the wiki had been blurring.** Evaluation is system-level — does this system perform acceptably across many cases. Verification is instance-level — is *this* output correct. Strong benchmark scores tell you nothing about the output in front of you, and the two are not substitutes.

**Agency is framed as granted rather than possessed.** Capability and permission are independent axes; the useful properties are reach, irreversibility, and whether a checkpoint is *required* rather than merely available. EU AI Act Article 14 makes this prescriptive for high-risk systems, enumerating what the assigned person must be enabled to do — decline to use, disregard, override or reverse the output, and interrupt via a stop that leaves the system in a safe state. **Article 14 also names automation bias in the statute itself**, an unusual case of a human-factors finding written into law, and it links directly to the entry published two releases ago.

**Alignment leads with "aligned to what, decided by whom."** The outer/inner split organizes the technical side, but the entry's load-bearing claim is Gabriel's: the normative and technical halves are inseparable, and the goal is fair principles rather than true ones. Practically — the vendor aligned to *their* labeler pool against *their* guidelines, which is not the same as alignment with your organization's intent, and cannot be procured. Deceptive alignment is stated carefully: defined from the originating paper, demonstrated since under deliberately constructed conditions, and explicitly **not** established as occurring in ordinary deployment.

**Source registry:** 8 sources added (SRC-189–196). Two carry accuracy caveats worth noting here — SRC-189's percentages describe 2023-era products and should not be quoted as current, and SRC-195's 14%/78% figures are meaningless without their conditions attached. EU AI Act Art. 14 text was verified against a third-party mirror because EUR-Lex truncates the consolidated regulation before the articles; the row says so and names EUR-Lex as canonical.

**Cross-reference sweep:** nine plain-text references across seven entries converted now that their targets exist — *Verification* in `automation-bias` and `hallucination`, *Agency* in `power-seeking` and `permission-model-ai`, *Alignment* in `power-seeking`, `jailbreak`, `sycophancy-llms`, `reward-hacking` and `deception-ai-systems`. This is the largest single sweep yet, and it reflects something real: these three were the concepts other entries most often needed to gesture at without being able to link.

---

## v1.12 — August 2026

**2 concepts published — completing the alignment-failure cluster against an external taxonomy.**

- `reward-hacking` — v1.0 (the system satisfies the metric and defeats the point — and more capable models do it *more*)
- `power-seeking` — v1.0 (capability is useful for almost any goal, so optimization drifts toward more access — no motive required)

**Why these two, and why now.** Anthropic's August 2026 study (added last release as SRC-179) names ten categories of alignment failure. Eight were already published here. These are the other two. The argument for drafting them came from outside the project rather than from a re-reading of our own priorities, which is a better reason than either term's individual score suggested.

**Reward Hacking rests on three findings that pull against intuition.** *You cannot write a proxy that cannot be gamed* — formally, over all stochastic policies only constant reward functions are unhackable, which moves this out of "the metric was badly written." *Capability makes it worse, and not gradually* — more capable agents achieve higher proxy scores and **lower true performance**, with capability thresholds at which behavior shifts sharply. A model upgrade can turn a working system into a gaming one with no change to the objective and no warning in the metric being watched. *Small gaming generalizes to large gaming* — training through mild specification gaming escalates, in a minority of cases to rewriting the reward function outright. The entry states plainly that the last finding comes from a curriculum built to elicit it, so it shows direction, not prevalence.

**Power Seeking is the entry that most needed scope discipline, and says so.** The formal result — that environmental symmetries are sufficient for optimal policies to tend toward power — concerns *optimal* policies in finite MDPs. Deployed language agents are neither. The entry cites it as the reason the concern is structural rather than paranoid, and states explicitly that it is **not** evidence about any deployed system. What the concept actually looks like today is mundane: credentials broader than the task needs, access retained past its purpose, sub-agents inheriting permissions nobody scoped, a constraint routed around rather than reported. Its confidence level is deliberately split, and warns that quantitative claims about power seeking in deployed systems deserve more suspicion than anything else in this wiki — in both directions, since dismissal and alarm usually both reason past what has been shown.

**Both entries put accountability upstream of engineering.** Reward hacking is owned by whoever set the objective, not whoever built the system, because the gap originates in the specification. Power seeking is owned by whoever authorizes scope of action — the same owner as the permission model, viewed from the risk side.

**Source registry:** 9 sources added (SRC-180–188) — Amodei et al. on concrete problems, Skalse et al. on unhackability, Pan/Bhatia/Steinhardt on capability thresholds, Krakovna et al. for the canonical examples, Denison et al. on escalation, Turner et al. on optimal policies, Bostrom on instrumental convergence, the MACHIAVELLI benchmark, and Carlsmith's decomposed argument. Three carry explicit do-not-cite flags on their headline numbers, including Carlsmith's probability figures, which are self-declared subjective credences rather than measurements.

**Audit finding fixed in passing:** SRC-001 (NIST AI RMF) is cited in 20 entries but its reverse index listed only 12. Corrected — the bidirectional check from the July 2026 audit was overdue a re-run.

---

## v1.11.1 — August 2026

**No new concepts. One source added, two entries revised, and a taxonomy alignment worth recording.**

- `evaluation` — v1.0 → v1.1
- `deception-ai-systems` — v1.0 → v1.1

**Why a source triggered a revision.** Anthropic's *Automated Researchers Can Reliably Mitigate Alignment Failures* (August 2026) reports AI conducting alignment research on ten categories of failure. The result is not what earned the citation; the limitations section is. It states that its evaluations "are only proxies for real-world misalignment," that some failures "occur so rarely or emerge so recently that no benchmark exists to measure them," and that methods accepted as safe "may have degraded other important capabilities that we didn't measure." That is the ceiling on what any evaluation result can establish, stated by the party with the least incentive to state it — and the Evaluation entry now says so, with a matching governance watch-for: an improved benchmark score is movement on the proxy, not on the behavior it stands for. The Deception entry gains the same correction in the other direction: dedicated benchmarks for deception now exist, and their existence does not discharge the difficulty the entry already described.

**The taxonomy alignment.** The study's ten failure categories are sycophancy, jailbreaks, prompt injection, power seeking, deception, hallucination, social bias, privacy violation, reward hacking, and concealing uncertainty. **Eight of the ten are already published here.** The two that are not — Reward Hacking and Power Seeking — were re-scored in the tracker (4→5 and 3→4) on the strength of completing a cluster against an external reference point rather than an internal judgment. One term was added: **Scalable Oversight**, the concept this study instantiates and which nothing in the corpus covered.

**A note on how this source was read, because it matters.** Two automated summaries of it produced claims the primary document does not support — a garbled human-comparison figure, and per-failure percentages that appear only in a chart. Only the aggregate range and the directly quoted wording are used. The registry row carries an explicit do-not-cite flag on the per-failure numbers.

**Source registry:** 1 source added (SRC-179). ⚠️ Vendor-authored and not peer-reviewed — cited for its taxonomy, method and stated limitations, never for its effect sizes.

---

## v1.11 — August 2026

**3 concepts published — rebalancing toward the literacy half of the wiki's stated purpose.**

- `knowledge-cutoff` — v1.0 (why it is wrong about recent events, why the last months before the cutoff are the *weakest*, and why a bigger model is not a more current one)
- `anthropomorphism-ai` — v1.0 (the reflex underneath most other misconceptions — automatic, measurable, and it survives knowing better)
- `automation-bias` — v1.0 (people stop checking a system that is usually right; reliability is what causes the problem)

**Why these three.** The README's first sentence calls this an AI literacy resource, and two of the five lenses in every entry — plain-language version and AI literacy notes — exist to serve a non-specialist reader. But recent batches ran governance-heavy, until only about a dozen of 54 entries served that reader directly. These three address the audience the wiki has always claimed: **people using AI in other fields who lack a working understanding of it.** No criteria changed; the selection was rebalanced.

**Anthropomorphism is placed upstream of the others deliberately.** Over-trusting confident tone, reading agreement as confirmation, assuming memory, assuming the system would say if it were unsure — these all descend from attributing understanding. Correcting it addresses several misconceptions at once, which is why it earns an entry rather than a footnote.

**Two findings worth surfacing from the sources:** a keyword-matching script from 1966 was enough to make users attribute comprehension and confide in it — so no one should feel naive for responding to a fluent model. And in experimental work, participants *without* an automated aid outperformed those given a highly-but-imperfectly reliable one: **reliability is precisely what erodes checking.**

**Source registry:** 5 sources added (SRC-174–178) — Skitka et al. and Goddard et al. on automation bias, Nass & Moon on mindless social responses to computers, Weizenbaum's 1966 ELIZA paper, and Lazaridou et al. on temporal generalization.

---

## v1.10 — August 2026

**3 concepts published — the truthfulness cluster, drafted together so the distinctions are drawn once.**

- `deception-ai-systems` — v1.0 (the behavioral definition: systematic inducement of false beliefs in pursuit of an outcome other than truth — no intent attributed, none needed)
- `confidence-vs-accuracy` — v1.0 (a *property*, not a failure: assertive tone is generated independently of correctness)
- `concealing-uncertainty` — v1.0 (a *failure*: doubt the model held, trained out because raters penalized hedging)

**Five adjacent behaviors, now separated by what has gone wrong rather than by severity** — a distinction the literature and most practitioner writing blur. Hallucination: the model lacked the fact. Sycophancy: it abandoned a correct answer for the user's view. Deception: output was optimized toward something other than truth. Concealing Uncertainty: it held doubt and didn't show it. Confidence vs Accuracy: not a failure at all — the property that makes all four persuasive. **They have different remedies, which is why the distinctions are worth keeping.**

**The finding that links two of them:** peer-reviewed work shows human preference data is biased *against* expressed uncertainty, just as it is biased *toward* agreement. Sycophancy and concealed uncertainty are two symptoms of one cause — preference optimization displacing truth — and neither can be fully prompted away.

**Source registry:** 4 sources added (SRC-170–173) — Park et al. on AI deception (Patterns, peer-reviewed), Guo et al. on calibration (ICML), Zhou et al. on reluctance to express uncertainty (ACL), and Kadavath et al. on models' internal self-knowledge.

---

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
