<!--meta
category: Reliability & Quality
short: Saving state at known-good points so a long run can be resumed or undone — and the boundary where undo stops working, which is wherever the system already touched the world
aliases: [checkpoint, model checkpoint, training checkpoint, save point, restore point, state snapshot, snapshotting, resume from checkpoint, checkpoint and restore]
tags: [Architecture, Security, Agents]
established: established
-->
# Checkpointing

> **Term status — Established.** A standard term in distributed systems since the 1980s and in machine learning practice throughout, used identically across frameworks, cloud providers and research literature. Independent of any vendor.

## One-line essence
Saving a system's state at known-good points so work can be resumed or rolled back — which turns an all-or-nothing run into a recoverable one, up to the boundary where the system has already acted on the world.

---

## Technical definition

A checkpoint is a saved representation of a system's state, written at a point from which execution can later resume. Checkpointing is the practice of writing them on a schedule or at chosen boundaries.

**Two uses share the word, and conflating them causes real confusion:**

- **Training checkpoints** — periodic saves of model weights and optimizer state during a training run, so that a run measured in weeks survives a node failure, and so that a training trajectory can be inspected or reverted to an earlier point ([pre-training](pre-training.md), [fine-tuning](fine-tuning.md)).
- **Execution checkpoints** — saved state of a running process, pipeline or agent, so a long task can resume after interruption or be rolled back to a point before something went wrong ([AI agent](ai-agent.md), [orchestration](orchestration-ai-systems.md)).

Both answer the same question: *what do we need to have written down for this not to have to start over?*

**The difficulty is consistency, not storage.** Chandy and Lamport established the requirement for any system with more than one moving part: a useful snapshot must record a state the system could actually have been in. A checkpoint assembled from components captured at different moments describes a state that never existed, and resuming from it produces behavior the system would never have produced. **Saving state is easy; saving a state you can resume from is the engineering problem.**

**For AI systems there is a boundary the checkpoint cannot cross, and it is the one that matters for governance.** An agent's own state — its context, its plan, its intermediate results — can be captured and restored. **The effects of the tools it already called cannot.** A refund issued, a message sent, a record deleted, a file written to a shared drive: rolling back the agent restores its memory of having acted, not the action ([tool use](tool-use.md), [agency](agency-ai-systems.md)). **A resumed run therefore begins in a state where the agent's beliefs and the world disagree**, and every side-effecting tool call becomes a candidate for duplication on resume.

**A checkpoint is not an audit trail.** It records *where the system got to*, not *how it got there or why*. The two are routinely conflated because both are "saved state," but a checkpoint answers a recovery question and an audit trail answers an accountability one — and EU AI Act Article 12 requires the second ([audit trail](audit-trail-ai.md), [observability](observability.md)).

**A checkpoint file is executable code, not a file of numbers.** Python's pickle format — still the de facto standard for exchanging model checkpoints — permits a saved object to import and invoke arbitrary callables *during loading*. Loading a checkpoint runs whatever it says to run. Kellas et al. measure the exposure: **44.9% of popular models on the Hugging Face hub still use the insecure pickle format**, repositories holding only pickle models are **downloaded over 400 million times per month**, and **15% of those cannot be loaded by PyTorch's safer weights-only loader** — so the safe path is not universally available. They also report that existing model scanners produce both false positives and false negatives ([supply chain risk](supply-chain-risk-ai.md), [sandboxing](sandboxing.md)).

**And a checkpoint is a data artifact with everything that implies.** An execution checkpoint contains whatever was in context when it was written — customer records, retrieved documents, credentials passed to a tool. A training checkpoint contains a model, and intermediate checkpoints are not necessarily less memorizing than the final one ([data leakage](data-leakage-ai-systems.md), [privacy attacks](privacy-attacks-ai-models.md)). Checkpoints accumulate quietly, are rarely covered by a retention schedule, and are frequently stored somewhere the production system's access controls do not reach.

---

## Plain-language version

If a job takes three weeks and the machine dies in week two, you would like not to start again. So the system writes down where it had got to, at intervals — and if something goes wrong, it picks up from the last written point instead of the beginning. That is checkpointing. It is the same idea as saving your work, applied to processes that run far too long to babysit.

The word covers two things. During training, a checkpoint is a saved copy of the model as it stands part-way through. During a long task, a checkpoint is a saved copy of what a program or an agent was in the middle of doing.

**The hard part is not saving — it is saving something coherent.** If you capture one part of a system now and another part a second later, you have written down a situation that never actually happened, and starting from it produces nonsense. This was worked out in 1985 and has not become easier.

**And here is the part that matters most, which the word "rollback" hides.** You can restore an agent to how it was ten minutes ago. You cannot restore the world. If it sent an email, issued a refund, or deleted a record in those ten minutes, that happened, and rewinding the agent just means it no longer remembers doing it — so it may well do it again. **Undo works inside the system and stops at its edge.** Any process that touches customers, money or shared data has this boundary, and it is worth knowing exactly where it falls before relying on the ability to roll back.

Two more things people are surprised by.

**A checkpoint is not a record of what happened.** It says where the system ended up, not what it decided along the way or why. If you need to explain a decision later, a checkpoint will not tell you — that is a different artifact, and in the EU it is a legal requirement.

**And opening a checkpoint file can run code.** The standard format for sharing models is one that executes instructions while it loads. Researchers found that nearly half of popular models on the largest public model hub still use it, downloaded hundreds of millions of times a month. Loading a model from an untrusted source is running a program from an untrusted source.

---

## AI literacy notes

1. **Checkpointing converts an all-or-nothing run into a recoverable one** — that is its whole purpose.
2. **Two senses share the word**: saved model weights during training, and saved execution state during a task.
3. **Consistency is the engineering problem**, not storage — a state that never existed cannot be resumed from.
4. **Rollback stops at the system boundary.** Side effects already committed are not undone.
5. **A resumed run starts with the agent's beliefs and the world out of step** — expect duplicate actions.
6. **A checkpoint is not an audit trail** — state, not the sequence of decisions.
7. **Loading a checkpoint executes code** in the still-dominant pickle format.
8. **Checkpoints contain whatever was in context** and are usually outside the retention schedule.
9. **Checkpoint frequency is a cost/exposure trade** — more frequent means less lost work and more copies of sensitive state.

---

## Governance notes

**Core question:** For each long-running or agentic process here, what exactly can be rolled back, what cannot, and who decided where that line falls?

**Watch for:**
- "We can just roll it back" asserted for a process that issues payments, sends messages or writes to shared systems ([agency](agency-ai-systems.md))
- Side-effecting tool calls with no idempotency key, so a resume repeats them ([tool use](tool-use.md))
- A checkpoint being offered as the record of what the system did ([audit trail](audit-trail-ai.md))
- Model checkpoints loaded from public hubs without format or provenance checks ([supply chain risk](supply-chain-risk-ai.md))
- Pickle-format checkpoints loaded in a process with production credentials ([sandboxing](sandboxing.md))
- A model scanner treated as sufficient assurance — the research reports both false positives and false negatives
- Checkpoint storage outside the access controls and retention schedule that cover the production data it contains ([data minimization](data-minimization.md))
- Intermediate training checkpoints retained indefinitely with no owner
- Recovery paths that have never been exercised — an untested restore is a hypothesis ([verification](verification.md))

**Practice:**
- **Write down explicitly what is inside the rollback boundary and what is outside it**, per process, and review it whenever a tool is added
- **Make side-effecting tool calls idempotent, or record their completion inside the checkpoint** so a resume does not repeat them
- Require a [human checkpoint](human-in-the-loop.md) before irreversible actions rather than relying on being able to undo them
- **Keep the audit trail separate from the checkpoint** and hold it to the record-keeping requirement, not to the recovery requirement
- **Prefer non-executable checkpoint formats** and load anything else only in an isolated process without production credentials ([sandboxing](sandboxing.md))
- Verify checkpoint provenance the way you would any dependency — publisher, integrity, and what it was trained or run from ([data provenance and lineage](data-provenance-lineage.md))
- **Put checkpoints on the retention schedule**, classified by what they contain rather than by what they are called
- **Exercise restore on a schedule.** A recovery procedure nobody has run is not known to work
- Set checkpoint frequency deliberately against both lost-work cost and the number of copies of sensitive state it creates

**Key accountability owner:** the owner of the process being checkpointed — because the decision that actually matters is where the rollback boundary falls, and that is a design and risk decision about the process, not a storage decision for the platform team.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanics are long-settled engineering, and the consistency requirement comes from a foundational result that has been standard for forty years. **Two limits worth stating.** Chandy and Lamport predate machine learning entirely — the consistency requirement transfers exactly, but the application to agent state and tool side effects is this entry's own reasoning from it, not a claim the paper makes. And the pickle exposure figures are a **measurement of one hub at one time**: the mechanism is stable, the percentages are not, and they should be re-checked rather than quoted indefinitely. The rollback-boundary point is stated as a structural property of side effects rather than as an empirical finding, because it follows from what a side effect is.

---

## Related concepts

- [Audit Trail (AI)](audit-trail-ai.md) — the accountability record a checkpoint is not
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — what checkpointing exists to survive
- [AI Agent](ai-agent.md) — the long-running process most in need of it
- [Tool Use](tool-use.md) — where the side effects that cannot be rolled back originate
- [Agency (AI Systems)](agency-ai-systems.md) — how much a system may do before a human confirms
- [Human-in-the-Loop](human-in-the-loop.md) — the confirmation that beats an undo you do not have
- [Sandboxing](sandboxing.md) — where to load a checkpoint you do not fully trust
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — a model file as an untrusted dependency
- [Data Poisoning](data-poisoning.md) — the other way a downloaded model file can be hostile
- [Model Version & Update](model-version-update.md) — the version a checkpoint pins
- [Memory (AI Systems)](memory-ai-systems.md) — persistence across sessions, a related but distinct problem
- [Context Compaction](context-compaction.md) — reducing state rather than saving it
- [Verification](verification.md) — the untested restore path
- [Observability](observability.md) — knowing a run failed before the checkpoint is needed

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-319 | Chandy, K. Mani; Lamport, Leslie — *Distributed snapshots: determining global states of distributed systems* (ACM Transactions on Computer Systems 3(1), pp. 63–75, 1985) · [link](https://doi.org/10.1145/214451.214456) | The consistency requirement that separates a saved state from a resumable one: a snapshot must record a global state the system could actually have been in. ⚠️ Predates machine learning entirely — the transfer to agent state and tool side effects is this entry's reasoning, not the paper's claim. |
| SRC-320 | Kellas, A.D.; Christou, N.; Jiang, W.; Li, P.; Simon, L.; David, Y.; Kemerlis, V.P.; Davis, J.C.; Yang, J. — *PickleBall: Secure Deserialization of Pickle-based Machine Learning Models* (ACM CCS, 2025) · [link](https://cs.brown.edu/people/vpk/papers/pickleball.ccs25.pdf) | The evidence that loading a checkpoint executes code, with the ecosystem measurement this entry quotes: **44.9%** of popular Hugging Face models still use the insecure pickle format, repositories holding only pickle models are downloaded **over 400 million times per month**, **15%** cannot be loaded by the weights-only unpickler, and model scanners have both false positives and false negatives. ⚠️ The authors propose their own tool; the ecosystem measurements are what is cited here. Percentages are a snapshot and will move. |
| SRC-130 | European Parliament / Council of the EU — *EU AI Act, Article 12: Record-keeping* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The obligation that a checkpoint does not satisfy: automatic recording of events over the system's lifetime, for traceability. Grounds this entry's distinction between recovery state and accountability record. |
| SRC-001 | NIST — *AI Risk Management Framework* (2023) · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Resilience and recoverability as named characteristics of a trustworthy AI system, which is where checkpointing sits in a risk framework rather than in an engineering backlog. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Make side-effecting calls idempotent and record their completion in the checkpoint; load untrusted checkpoint formats only in an isolated process. |
| **Organizational** | "We can roll it back" is true up to the point where the system acted on the world. Know where that line is before you rely on it. |
| **Client-facing** | Explains why a long automated process can be resumed, and why some steps still have to be confirmed by a person first. |
| **LLM-native** | An agent restored from a checkpoint has its old beliefs and the world's new state. Every committed tool call is a candidate for duplication on resume. |

---

*Last updated: v1.0 · September 2026*
