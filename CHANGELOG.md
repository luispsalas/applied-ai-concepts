# Changelog

## v1.19 — September 2026

**5 concepts published — the evaluation-integrity pair, the containment control, the auditable retrieval substrate, and the oldest argument in AI safety. Count 95 → 100.**

- `data-leakage-model-evaluation` — v1.0 (the same name as an existing entry, the opposite failure)
- `llm-as-judge` — v1.0 (the only evaluation that scales, and its self-enhancement bias)
- `sandboxing` — v1.0 (bounding beats enumerating)
- `knowledge-graphs` — v1.0 (declared relationships you can audit, versus learned proximity you can only measure)
- `recursive-self-improvement` — v1.0 (a sound argument from 1965 whose premises remain unmet)

**Data Leakage (Model Evaluation) resolves a name collision the corpus had already flagged.** The published *Data Leakage (AI Systems)* is about sensitive information **escaping** — a confidentiality failure. This one is about evaluation information **entering** — a measurement failure. Unrelated concepts, one name, and the existing entry had carried a standing pointer to it for weeks. The load-bearing property: **leakage errors only ever flatter**, so a surprisingly good result deserves more scrutiny than a disappointing one.

**LLM-as-Judge is unusually clean to source, because the method and its limits arrived in the same paper.** Strong judges reach *"over 80% agreement, the same level of agreement between humans"* — and the same work names position, verbosity, self-enhancement and limited-reasoning bias. **Self-enhancement is the one with governance teeth:** a judge prefers output resembling its own, so grading a model with its own family is a conflict of interest built into the setup, not a correction factor. The deeper limit is that agreement is concordance, not correctness.

**Sandboxing states the distinction the corpus needed.** Guardrails *enumerate* forbidden behavior and every enumeration is incomplete — which is why prompt injection and jailbreaks keep working. **A sandbox does not enumerate; it bounds.** The question stops being "can we stop it doing X?" and becomes "what could reaching everything available here do?" With the failure mode named: sandboxes erode by widening, one "just allow this so it works" at a time, and those are security decisions that rarely get recorded as such.

**Knowledge Graphs is framed as an auditability trade, not a performance claim.** A wrong answer traces to one correctable triple; a wrong vector result is retuned and re-measured. That is a real advantage bought with real cost, and the entry declines to claim accuracy improvements from graph augmentation, which are workload-specific and mostly vendor-benchmarked. Its failure mode is **silent staleness** — a graph returns yesterday's relationship as confidently as today's.

**Recursive Self-Improvement makes no forecast, and says so.** Good's 1965 formulation is quoted from the original chapter — *"the design of machines is one of these intellectual activities"* — because that clause is the whole argument. The structure is valid; the premises are unmet. **The entry's contribution is a reframing:** treated as a prediction this generates a debate nobody can settle, but treated as a present-tense property it is answerable — *does anything here modify itself, its training, or its successor without a human in the path?* The confidence level flags both directions as unsupported: claims it is underway, and claims it is impossible.

**Source registry:** 5 added (SRC-241–245), 13 reused. Good (1965) was quoted only after extracting the text layer of a scanned copy of the original — the passage circulates widely in secondary sources and was not taken from any of them.

**Two checks caught defects in this batch, both in work written the same day.** The alias gate found `LLM as judge` registered as an alias of *Scalable Oversight*, now colliding with a real entry title. The spelling sweep found `favours` three times in new prose — its first true positives, after being tuned down from 14 hits to 2 by excluding quoted material. A stale `LLM-as-judge` link pointing at `evaluation.md` was also retargeted: an anchor pointing at the *wrong existing entry* resolves perfectly and is invisible to link checking.

---

## v1.18 — September 2026

**8 concepts published — the missing mechanism layer, two organizational gaps, and the last two score-4 terms. Plus a term-status gate, and the rename it produced on its first real use.**

- `tokenization` — v1.0 (the unit of the mechanism, the context window and the bill)
- `temperature-llms` — v1.0 (a variability knob widely mistaken for an accuracy knob)
- `embeddings` — v1.0 (meaning as position; bias as a measurable direction)
- `pre-training` — v1.0 (where everything a model knows is fixed, irreversibly)
- `continuous-feedback-improvement` — v1.0 (the loop is only real if someone may act on it)
- `tacit-knowledge` — v1.0 (Polanyi's paradox, and the articulation bottleneck it moved)
- `moral-crumple-zone` — v1.0 (the operator who absorbs blame for a system they could not control)
- `performativity-llms` — v1.0 (the model changing the user, measured in spontaneous speech)

**The automated gap report went flat, and the fallback found more than it did.** Top score was 2, and all three hits at that score — `Skill`, `NLP`, `Inference` — were verified as the known common-word false positives, matching "Skills," "EMNLP" and "inference" as a phase word. **Inbound demand as a selection signal is exhausted**: three consecutive batches drained it, because published entries are careful not to leave unlinkable jargon lying around.

**Falling back to the curation criteria surfaced a signal the report structurally cannot see.** Five of the six terms were already *promised* by published entries — named in a Related-concepts list with no link behind them: Embeddings (from RAG), Temperature (from Determinism vs Probabilism), Pre-training (from Training Data), Tacit Knowledge (from Curse of Knowledge), Continuous Feedback (from Model & Data Drift). The report scored these 1 or 0 and buried them. **A mention in a Related-concepts list is a promise; a mention in prose is a usage.** They are different demand signals and the report weights them identically.

**Tokenization was selected on a different basis again, and it is the strongest of the six.** It had *zero* unlinked mentions — because the corpus says "token," not "Tokenization." Eleven published entries depend on the unit: "next-token prediction is the whole engine," "per-token pricing," "token limits." **None defined it.** A structural hole is invisible to a term-matching report by construction.

**The hand-assigned scores were wrong in the same direction as last release, and further.** The six published here scored 4, 4, 3, 3, 3 and **2**. Temperature (LLMs) sat at score 2 while a published entry pointed at it by name. Two releases running, the foundational mechanism terms have been under-scored relative to what the corpus demonstrably needs.

**Tokenization and Temperature both carry findings that contradict common practice.** Tokenizers make the same text up to **15× longer** in some languages than others — and since cost, latency and context capacity share the token as their unit, one disparity propagates into all three: same model, same posted price, less service. And sampling temperature between 0.0 and 1.0 has **no statistically significant effect on problem-solving accuracy** across nine models and five prompting methods. Lowering it buys consistency, not correctness — so it is not a risk control unless an evaluation shows it acting as one.

**Embeddings carries a negative result rather than a mitigation.** Bias in an embedding space is a measurable *direction*, which makes it auditable. But published debiasing methods "hide the bias, not remove it" — it survives in inter-word distances and can be recovered. The entry states that measurement is reliable and any claim a space has been debiased is not, and cites both papers so the pairing is visible.

**Continuous Feedback names the step that actually fails.** Not instrumentation — that gets budgeted. The **decision authority**: organizations build the dashboards and find nobody owns the call to act on them. The entry also treats the loop as a hazard in its own right, since a system improved on data it influenced confirms itself and reports progress while doing so.

**The last two score-4 terms are published, and the tier is now empty.** Custodial Agency and Performativity (LLMs) had sat unpicked through five batches. Both were parked as sourcing risks — and, as with Small Language Models and Red Teaming before them, **"source-blocked" again meant "nobody has looked."** Both had strong anchors available, and Custodial Agency's four best sources were *already in the registry*, filed against other entries.

**A term-status gate now runs on every entry, and it changed one of them.** Every entry declares, in a line under its title, whether its name is `established`, `emerging`, this wiki's own `house` label, or `vendor`-coined. This is a **separate axis from the confidence level** — that rates the evidence, this rates the term, and they vary independently: *Cognitive Offloading & Deskilling* is a completely standard term resting on weak evidence, and the corpus's one house term was assembled entirely from peer-reviewed work. Both are machine-checked; `check` fails the publish on a missing or unknown status, or on a visible line that disagrees with the metadata.

**Custodial Agency was the gate's first real test, and it failed three of four checks — so it was renamed to `Moral Crumple Zone`, keeping the content.** Check 4 passed and mattered: the substance was measurably absent from the rest of the corpus, and 2 of its 6 sources were unique to it. What failed was the name. And the failure was not the expected one — **the phrase was not unattested, it was already taken**, occupied by three unrelated established senses (custodial *funds*, custodial *services*, government *agency oversight*). A reader searching it lands in facilities management.

**That distinction is now part of the gate.** An unattested coinage and a collision are different failures: a coinage can honestly be labeled and kept, whereas a collision means the confusion is active rather than merely absent, and argues for renaming. Candidate replacements were run through the same four checks before adoption rather than after — which eliminated *Meaningful Human Control* on check 4, since the corpus already covers it in two entries, and eliminated *Embedded Oversight* and *Operator Accountability* on checks 1 and 3, where the only usage found was vendor governance blogs using the words descriptively with no stable definition. **Moral Crumple Zone passed all four**, on Elish (ESTS 2019) plus genuinely independent peer-reviewed uptake — Hohenstein & Jung put it in the title of a *Computers in Human Behavior* paper with no authorship overlap.

**The rename was not a title swap, and should not be read as one.** A title promising an established concept has to deliver it, so the entry was re-centered: the crumple zone is now the subject, with the responsibility gap and the many-hands problem explaining why AI widens the opening, and the "embedded and accountable" framing kept as the honest counterpart — the same position, legitimate when four conditions hold. `custodial agency` survives as an alias. **Net effect: the corpus now has zero house terms.**

**The confidence field was silently doing two jobs, and 25 entries were migrated.** They led with `**Established.**` or `**Emerging.**` in a field meant for evidence strength — term maturity in the confidence slot. Rather than add a second authored field, **the rating is now derived from the prose**, per the schema's own "derive rather than author" rule: a derived value cannot drift from its source, so no reconciliation gate is needed, and `check` fails any entry whose confidence does not open with a parseable rating. **The derivation deliberately refuses to flatten compound ratings** — 21 entries lead with statements like *"High on the mechanism, low on effectiveness in the wild,"* and taking the first word would have advertised confidence about the half the entry is not confident in. Two ratings in one statement derives as `split`. Corpus calibration is now a standing report section: **43 high · 17 medium-high · 16 medium · 1 low-medium · 18 split** — and the 18 split entries are a quality signal, evidence of per-part calibration rather than uniform hedging.

**Its central move is to carry the hazard, not just the ideal.** Elish's *moral crumple zone* — the nearest human absorbing moral and legal responsibility for a system they could not control, protecting the technology at the operator's expense — is the same position described from the outside. The entry's position is that **"you are embedded and therefore accountable" can describe a genuine duty or launder an institutional one, and the phrasing does not distinguish them.** The test it offers is four conditions: authority, information, time, incentive.

**Performativity carries a deliberate scope correction against its own one-line essence.** The seed definition says these systems shape what people *believe, say, and expect*. The evidence — a synthetic control over 737,083 hours of podcast speech linking ChatGPT-preferred words (*delve*, *showcase*, *meticulous*) to its release, plus a preregistered experiment (N=496) showing the adoption entrenches — covers **say**. The confidence level states that belief and expectation are plausible extensions and not findings, and tells readers not to cite the study for them. **A version trap is flagged in the registry:** the current paper uses the podcast corpus; v1 used a YouTube corpus, and secondary summaries conflate the two sets of figures.

**Source registry:** 17 sources added (SRC-221–237), 14 reused. All 11 archive URLs captured at registration — the Nonaka DOI returned no snapshot until the publisher URL form was tried, the same literal-matching trap the workflow warns about. One source (Gonen & Goldberg) was registered specifically because a claim in a draft confidence level would otherwise have gone uncited.

**One duplicate resolved as already-clean.** The standing "Pre-training / Pre-trainining typo" note in the project record described a tracker row that no longer exists.

---

## v1.17 — September 2026

**6 concepts published — the training-pipeline chain, plus three long-run costs.**

- `rlhf` — v1.0 (humans rank outputs; the step that imports whoever did the ranking)
- `fine-tuning` — v1.0 (cheap enough to be routine, and it silently degrades safety)
- `model-version-update` — v1.0 (the system you tested may not be the one you're running)
- `cognitive-offloading-deskilling` — v1.0 (delegating judgment erodes the judgment needed to check)
- `value-realization-ai` — v1.0 (the gap is complementary investment, not a better model)
- `scalable-oversight` — v1.0 (AI reviewing AI, and who checks the checker)

**Selected by the gap report, which is now automated.** `build.py report` counts unlinked plain-text mentions of every unpublished term and prints a flatness warning. It surfaced RLHF, Model Version & Update and Fine-tuning at the top — **all score-3 tracker terms, ahead of the remaining score-4s.** The corpus reached for them more than their score predicted, which is exactly the signal the report exists to expose. Three apparent hits (`Skill`, `NLP`, `Inference`) were verified as false positives on prose and source titles before being discarded.

**RLHF and Fine-tuning complete a chain the corpus kept gesturing at.** Training Data was published; what happens *to* a model afterwards was not. Three published entries — Alignment, Sycophancy, Concealing Uncertainty — rest their central claims on preference optimization, and none could link to it. **The RLHF entry's point is that its two documented side effects are one mechanism**: optimizing against approval, which is adjacent to truth and not the same thing.

**Fine-tuning carries the finding most likely to change practice.** Safety alignment was stripped from a production model with 10 adversarial examples for under $0.20 — but the load-bearing half is the second: *"simply fine-tuning with benign and commonly used datasets can also inadvertently degrade the safety alignment."* A team adapting a model on ordinary internal data has changed its refusal behavior with no warning, and the provider's safety evaluation now describes a model they are not running.

**Model Version & Update deliberately refuses the popular reading of its own headline source.** The widely-cited prime-number result (84% → 51%) is presented with the parts usually dropped: the *other* model improved on the same task, and the drop is substantially reduced amenability to chain-of-thought prompting — **a behavior change, not demonstrated capability loss.** The entry cites it for *that behavior changes unannounced*, never as evidence any model got worse.

**Two entries are unusually explicit about weak evidence.** Cognitive Offloading & Deskilling states plainly that **no longitudinal study of AI-specific deskilling exists** — the mechanism is established, the loop is reasoned, the outcome is not observed — and warns against confident claims in either direction. Scalable Oversight is flagged as **the least settled entry in the corpus**, and carries the counter-evidence its own headline source omits: in one task a fallible assistant improved human performance, in another it *degraded* it, and nobody knows what predicts which.

**Value Realization is anchored in economics rather than consultancy material.** The J-curve — complementary intangible investment producing a dip before a rebound — means a disappointing early return is the predicted shape, and equally that the rebound is not automatic. The entry cites no AI ROI figure deliberately, and says why.

**Source registry:** 7 sources added (SRC-214–220). Two Crossref-verified.

**Generator did the mechanical work.** One `build.py write` synced six README rows, regenerated the glossary, updated the count, and rebuilt the search index and page — four previously manual steps. `check` gates the result.

**Two of my own errors caught by round-trip verification, both worth recording.** Reverse-index values for SRC-173 and SRC-192 were composed by hand instead of from the report, and were wrong in both directions (one missing an entry, one with three spurious ones); comparing the sheet against the generator's output found them. And a tracker cell was cleared by writing an **empty string** rather than being blanked — an empty-string cell is not a blank cell, `"" < "X"`, and it sorted an unpublished term to the top of the published block. Both are the same lesson: verify the write, don't trust it.

---

## v1.16 — August 2026

**6 concepts published — the authenticity and attribution cluster, plus two governance gaps.**

- `copyright-ai-output` — v1.0 (two questions, one with a US answer and one genuinely open)
- `ai-disclosure-attribution` — v1.0 (a human practice, distinct from machine marking)
- `synthetic-media-deepfakes` — v1.0 (generation scales, verification does not)
- `fundamental-rights-impact-assessment` — v1.0 (a deployer duty binding far fewer organizations than commonly claimed)
- `bluewashing` — v1.0 (the test is whether anything can constrain a decision)
- `multimodal-ai` — v1.0 (every text risk carried across, with weaker tooling to detect it)

**The inbound-demand tiebreak was weak this round, and that is worth recording.** Last release it separated the field cleanly. Here it returned 2, 2, then seven candidates tied at 1 — so the top two were selected by it and the rest by cluster coherence and the dual curation lens. **A tiebreak that works once is not a rule**; when it goes flat, say so and fall back rather than pretending the signal decided.

**Copyright's value is in refusing to give one answer.** Two questions get merged — is the output protectable, and was training lawful — with different parties at risk. On the first, the US Copyright Office is quotable and precise: *"prompts alone do not provide sufficient human control to make users of an AI system the authors of the output."* On the second, nothing is settled anywhere. The entry states the asymmetry rather than smoothing it, **makes no forecast about how training litigation resolves**, and flags that the Office's conclusion is explicitly technology-dependent.

**AI Disclosure separates two things that are routinely conflated**, in both directions: a voluntary human disclosure does not discharge the Art. 50(2) machine-marking duty, and a technical watermark does not tell a reader what was actually done. The ICMJE position supplies the principle worth borrowing well beyond publishing — **an AI cannot be an author because it cannot be answerable for the work**, which settles the crediting question by reasoning rather than etiquette.

**Synthetic Media puts its practical weight where the harm is.** The documented damage concentrates in non-consensual intimate imagery and in fraud, not primarily in political deception — so the highest-value control is procedural: **remove voice and video from the trust path and require out-of-band confirmation.** That belongs to fraud prevention, not the AI team. The entry also carries a finding that should change how detection tooling is deployed: in a 15,016-participant study, *"inaccurate model predictions often decrease participants' accuracy."* A wrong detector makes a reviewer worse. And it names the *liar's dividend* — a harm requiring no successful fake at all, which detection cannot address.

**FRIA is written primarily to correct an over-broad reading.** Art. 27 binds deployers that are public bodies or private entities providing public services, plus specific Annex III categories — **not every high-risk deployer**, which is how practitioner writing routinely states it. Also that a DPIA does not discharge it, and that complaint mechanisms are an enumerated element rather than a nicety.

**Bluewashing adopts the peer-reviewed framing rather than a hypocrisy charge**, which makes it more useful and fairer. The diagnostic: *the tell is not that a company published principles — it is whether anything can constrain a decision.* Four tells, and an explicit defense for honest immaturity, because the accusation is serious and often wrong. It also names the symmetrical failure — dismissing ethics wholesale — which lands in the same place.

**Multimodal AI earns a governance entry rather than a technical one:** adding a modality does not add one risk, it multiplies the existing set across a surface with weaker instrumentation. Image-borne prompt injection is the most commonly missed, since most filtering stops at text.

**Source registry:** 6 sources added (SRC-208–213). The Copyright Office conclusion was verified by full-text search of the report PDF rather than from a summary, and two citations were confirmed through Crossref — one DOI written from recall had resolved to an unrelated call for papers.

**Cross-reference sweep:** six references converted. One mislink caught before shipping.

---

## v1.15 — August 2026

**6 concepts published — the score-4 terms that other entries were already reaching for.**

- `training-data` — v1.0 (where knowledge, gaps and bias all originate, and which you usually cannot inspect)
- `shadow-ai` — v1.0 (unsanctioned use — a signal about the sanctioned option, not only a violation)
- `model-card-system-card` — v1.0 (a scoping document whose job is to say where *not* to use a model)
- `frontier-ai` — v1.0 (a category defined by capability being discovered after training, not by size)
- `curse-of-knowledge-ai-context` — v1.0 (you cannot un-know what you know, so you under-specify)
- `content-provenance-watermarking` — v1.0 (a positive detection means something; a negative one does not)

**Selected by inbound demand rather than by score.** All eighteen remaining candidates sat at 4, so the tiebreak was which terms other entries were already mentioning as unlinkable plain text: Training Data had four such references, the next four had two each. That converted nine dangling references into links — a better signal than re-reading the scores, and worth reusing as a tiebreak when a score tier is flat.

**Training Data's most useful content is an audit, not a definition.** A direct examination of C4 found machine-generated text inside the corpus, **evaluation examples from other benchmarks** (contamination that inflates measured performance), unexpected sources including patents and military websites, and — the finding that should change how people think about data cleaning — **blocklist filtering that disproportionately removed text from and about minority individuals.** The cleaning step is itself a source of bias, not a correction for it. The entry is explicit that the auditable corpora are dated precisely because they are the ones that could be audited, and that frontier composition is undisclosed.

**Content Provenance leads with the asymmetry that matters:** a positive detection is informative, a negative one is not. "No watermark found" is not evidence of human authorship, and treating it as such is the most consequential misreading available. The entry also carries the specification's own limit verbatim — C2PA "SHOULD NOT provide value judgments about whether a given set of provenance data is 'good' or 'bad'" — because **validation establishes integrity and attribution, never that the content is true.** And it separates the machine obligation under Art. 50(2) from voluntary human disclosure, which does not discharge it.

**Model Card is framed as a scoping instrument** — its stated purpose is to *minimize* use in contexts a model is not suited to — with disaggregated evaluation as the test of whether a card is doing governance work or is a brochure with sections. It also draws the model-card/system-card line: you deploy systems, not models, and no provider will document your guardrails, retrieval and prompts for you.

**Shadow AI argues it is a supply problem.** Three properties separate it from classic Shadow IT — data leaves on every interaction rather than at setup, there is no procurement event to catch, and adoption has zero marginal cost — but the response inherits the Shadow IT finding that suppression without a usable alternative displaces behavior downward, onto personal accounts where visibility is worse. **Deliberately cites no prevalence figures**, since the circulating numbers are vendor-commissioned and measure salience.

**Frontier AI is written about properties, not membership**, because the membership dates. And it keeps "frontier" separate from the EU's "systemic risk" designation, which are used interchangeably and are not the same set.

**Source registry:** 7 sources added (SRC-201–207). Two citations were verified through Crossref rather than written from recall, and three carry publisher-block flags so future link audits do not re-raise them as dead.

**Cross-reference sweep:** nine plain-text references converted across six entries. **Four mislinks were caught before shipping** — *Datasheets*, *Model Version & Update*, *Scalable Oversight* and *AI Disclosure* had each been pointed at a different existing entry. All four resolve correctly and would pass a broken-link check, which is why the anchor-text comparison now runs as its own step.

---

## v1.14.1 — August 2026

**No new concepts. One entry revised to state a curation decision it had been leaving implicit.**

- `data-provenance-lineage` — v1.0 → v1.1

**The question that prompted it:** if provenance and lineage answer different questions, why are they one entry? The entry made the distinction in its first paragraph and never gave the reason for the pairing — so the slash in the title was carrying an argument instead of stating one.

**The reason, now written down:** they are *governed* as one practice even though they are *understood* as two. EU AI Act Art. 10 places origin and transformation history inside a single obligation, discharged by one record and audited together, and both are captured or lost at the same moment — when data enters the pipeline. Splitting them would let a reader satisfy half a duty with no signal that the other half belonged to it. **Keep the distinction when reasoning; keep the record whole.**

Worth noting the argument that cuts the other way, since it is a real one: this wiki keeps Confidence vs Accuracy separate from Concealing Uncertainty on the grounds that things with different remedies deserve different entries — and provenance failures are remedied legally while lineage failures are remedied by instrumentation. The regulatory-unity argument was judged stronger for a governance corpus, but the pairing is a decision rather than an obvious fact, which is precisely why it now appears in the text.

---

## v1.14 — August 2026

**7 concepts published — the largest batch so far, filling the structural gaps rather than the safety ones.**

- `context-ai-systems` — v1.0 (the object; one bounded, undifferentiated stream, assembled fresh every time)
- `local-llms` — v1.0 (the data stays in; every duty the provider was carrying becomes yours)
- `data-provenance-lineage` — v1.0 (origin and history — now a legal duty, and currently broken)
- `human-llm-communication-skills` — v1.0 (mostly noticing what you left unstated)
- `orchestration-ai-systems` — v1.0 (the control layer, where failures hide in the seams)
- `scalability-ai-systems` — v1.0 (volume scales, review capacity does not)
- `systemic-risk-ai` — v1.0 (a precise legal threshold, and an unregulated risk everyone else carries)

**Context is published as the object, with Context Engineering remaining the practice.** The entry's load-bearing claim is that context is *one undifferentiated stream* — the model cannot distinguish operator instruction from user text from tool result except by what surrounds it. That is not an oversight to be patched; it is why prompt injection works, and why "tell it to ignore untrusted content" is not a control.

**Data Provenance / Lineage separates two things routinely merged.** Provenance answers *may we use this*; lineage answers *what is this and what breaks if it changes*. EU AI Act Art. 10 makes the first a documented obligation for high-risk systems, naming "the origin of data" and the original collection purpose explicitly. The state of practice is worse than most teams assume: an audit of 1,800+ widely used datasets found **license omission above 70% and error rates above 50%**. And the AI-specific asymmetry gets its own note — training *absorbs* while retrieval *references*, so the provenance check that counts is the one before training, since weights cannot be selectively unlearned.

**Scalability's central claim is a governance one, and it is flagged as an inference.** Four things scale independently — load, data, complexity, and human review — and the fourth does not scale at all. Volume rises, verification capacity does not, and a reviewed assistive tool becomes an unreviewed pipeline with no decision taken and no alarm raised. **The entry proposes the review rate — what proportion of output is actually checked — as a first-class metric**, precisely so the claim can be observed rather than assumed. The Confidence level says plainly that this pattern is reasoned from the automation-bias and verification-cost literature rather than directly measured.

**Systemic Risk is split down the middle, deliberately.** The regulatory sense is precise and quotable: Art. 51's classification, the 10^25 FLOP presumption, and Art. 55's four provider obligations. The analytical sense has no agreed measurement. The entry's practical weight goes on the question that is actionable today and that no regulation covers — **single-provider concentration risk, which sits with deployers and belongs to third-party and continuity risk, not to the AI team.** The compute threshold is stated as a rebuttable presumption about capability, chosen because compute is observable, and explicitly not a safety line in either direction.

**Orchestration's contribution is that its failures look like success.** Peer-reviewed fault taxonomy places agentic failures in the seams — a malformed result consumed as valid, an error swallowed, a loop that neither completes nor terminates — so the run finishes and returns something plausible. That is why the trace, not the output, is the unit of review.

**Source registry:** 4 sources added (SRC-197–200) — EU AI Act Arts. 10, 51 and 55, the Data Provenance Initiative audit, and *Datasheets for Datasets*. The remaining 35 citations across these seven entries reuse existing registry rows, and every reverse index was regenerated from the files rather than appended to.

**Cross-reference sweep:** three plain-text references converted in `small-language-models`, `multi-agent-systems` and `power-seeking`. Two mislinks were caught during drafting and removed rather than shipped — *Training Data* and *Shadow AI* had each been pointed at a different existing entry, which is the exact failure the anchor-text check exists for.

---

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
