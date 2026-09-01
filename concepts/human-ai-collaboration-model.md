<!--meta
category: Human Oversight
short: The explicit design of how people and AI systems divide work, hand over, and resolve disagreement — documented, not assumed
aliases: [division of labor with AI, who does what, handoff design, human AI teaming, collaboration pattern]
-->
# Human–AI Collaboration Model

## One-line essence
The explicit design of how humans and AI systems divide tasks, share information, and maintain oversight — not assumed, but documented and enforced.

---

## Technical definition

The specified division of labor between people and an AI system in a given workflow: which steps the system performs, which a person performs, where control passes between them, what information each needs at the handover, and who decides when they disagree.

The peer-reviewed design literature treats this as an artifact to be authored rather than a property that emerges. Guidelines for human-AI interaction organize the problem by *when* each decision applies — what the system establishes **initially** (making clear what it can do and how well), what happens **during interaction** (showing contextually relevant information, matching relevant social norms), what happens **when the system is wrong** (supporting efficient correction, dismissal, and appeal, and scoping services when uncertain), and what happens **over time** (learning from behavior, notifying users of change). The "when wrong" cluster is the one most often skipped, and it is where a collaboration model earns its keep.

A workable model specifies at least: **task allocation** (who does what, and why that split); **the handover contract** (what information moves in each direction, in what form); **the authority boundary** — which is the [permission model](permission-model-ai.md) viewed from the human side; **the disagreement rule** (what happens when the human and the system reach different conclusions, and who prevails); and **the correction path** (how a person overrides, appeals, or reverses an output, and how that feedback returns to the system).

Two failure patterns recur, in opposite directions. **Over-reliance** — the human becomes a rubber stamp, nominally in the loop but not exercising judgment, so oversight exists on paper only. **Under-reliance** — the human duplicates the system's work out of distrust, so the system adds cost without removing any. Both are collaboration-design failures, not user failures, and both are invisible unless someone measures whether the human's involvement changes outcomes.

The distinction from [human-in-the-loop](human-in-the-loop.md) is one of scope: HITL is the *pattern* of inserting human judgment at a decision point. The collaboration model is the *whole design* — allocation, information flow, authority, disagreement, and correction across the workflow, of which HITL checkpoints are one component.

---

## Plain-language version

Most teams never actually decide who does what when a person and an AI system share a job — it just settles into whatever happens. Then two things go wrong: either the person starts approving everything without really looking, or they redo the work themselves and the system saves nobody anything. Writing the split down, including what happens when the two disagree, is what prevents both.

---

## AI literacy notes

1. **An undesigned collaboration model is still a collaboration model — just an accidental one.** If nobody specified the split, it will be settled by convenience and habit, and it will drift.
2. **"A human reviews it" is not a design.** Reviews what, against what, with what information, with authority to do what, and with how much time? Unspecified review reliably becomes approval.
3. **Over-reliance and under-reliance are both design failures.** Rubber-stamping and shadow-duplication are the two stable outcomes of an unspecified model. Neither is the user's fault.
4. **The disagreement rule is the part everyone forgets.** When the human and the system reach different conclusions, what happens? If there is no answer, the default is whichever is easier — usually the system's.
5. **Design for being wrong, not for working.** The strongest published guidelines cluster around what happens *when the system errs* — correction, dismissal, appeal, and scoping when uncertain. That is the part most implementations omit.
6. **The model must be re-specified when capability changes.** Adding [tools](tool-use.md) or autonomy silently moves the boundary; the documented split becomes fiction unless it is revisited.

---

## Governance notes

**Core question:** Is the division of labor between people and this system written down — and does the human's involvement demonstrably change outcomes?

**Watch for:**
- Human oversight asserted in a policy with no specification of what the reviewer sees, decides, or can override
- Approval rates near 100%, the signature of rubber-stamping — oversight that exists formally but not functionally
- Reviewers given no time budget, so the review is nominal by construction
- Users quietly redoing the system's work, indicating under-reliance and unrealized value
- No defined path to contest or reverse an output, leaving affected people with no recourse
- Capability added (new tools, more autonomy) without re-specifying the split

**Practice:**
- Document the model per use case: allocation, handover contract, authority boundary, disagreement rule, correction path
- Give reviewers what a real decision needs — inputs, confidence, provenance — not just the output to sign
- Measure whether oversight is functioning: track override rates, time-on-review, and outcome differences with and without the human step
- Design the error paths first, since that is where the model is tested
- Re-specify on any capability change and treat it as a change requiring reassessment

**Key accountability owner:** the process owner for the workflow, jointly with the system owner.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The interaction-design guidance is peer-reviewed and empirically validated, and the over/under-reliance failure patterns are well documented across the human-factors literature. Less settled: how to measure whether oversight is *meaningful* rather than nominal, and how these designs should change for agentic systems that act across many steps rather than returning a single output for review.

---

## Related concepts

- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the checkpoint pattern; this entry is the whole design that positions those checkpoints
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the duty that persists regardless of how the split is drawn
- [Permission Model (AI)](permission-model-ai.md) — the same authority boundary, specified from the system's side
- [Ownership (AI Systems)](ownership-ai-systems.md) — someone must own the workflow, not just the system
- [Accountability (AI Systems)](accountability-ai-systems.md) — a collaboration model determines who can actually answer for an outcome
- [AI Literacy](ai-literacy.md) — reviewers cannot exercise judgment over a system they do not understand
- [Sycophancy (LLMs)](sycophancy-llms.md) — a system that agrees by default corrodes the human check the model depends on
- [Explainability (XAI)](explainability-xai.md) — a reviewer needs a reason, not just an output, to add anything
- [Evaluation (AI Systems)](evaluation.md) — whether oversight changes outcomes is an empirical question
- [RACI](raci.md) — the coarser organizational counterpart: who is responsible, accountable, consulted, informed

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-168 | Amershi, S.; Weld, D.; Vorvoreanu, M.; Fourney, A. et al. (Microsoft Research) — *Guidelines for Human-AI Interaction* (CHI, 2019) · [link](https://doi.org/10.1145/3290605.3300233) | The 18 validated guidelines and their organization by phase — initially, during interaction, when wrong, over time — establishing the division of labor as a design artifact. ⚠️ Vendor-affiliated authors, peer-reviewed. |
| SRC-015 | Stanford HAI — *Humans in the Loop: The Design of Interactive AI Systems* (2019) · [link](https://hai.stanford.edu/news/humans-loop-design-interactive-ai-systems) | The autonomy spectrum from full human control to full system autonomy, and the framing of oversight as an interaction-design problem. |
| SRC-016 | Google Cloud — *What is Human-in-the-Loop (HITL) in AI & ML?* (2024) · [link](https://cloud.google.com/discover/human-in-the-loop) | Three concrete handover patterns — pre-approval, exception handling, periodic review. ⚠️ Vendor-authored. |
| SRC-109 | Green, Ben — *The Flaws of Policies Requiring Human Oversight of Government Algorithms* (Computer Law & Security Review 45, 2022) · [link](https://doi.org/10.1016/j.clsr.2022.105681) | Evidence that mandated human oversight frequently fails to function as intended — the empirical case for measuring whether oversight is meaningful rather than assuming it. |
| SRC-017 | Verma, Rahul (LangChain) — *Human judgment in the agent improvement loop* (2026) · [link](https://blog.langchain.com/human-judgment-in-the-agent-improvement-loop/) | The correction path: converting human review into durable evaluation rather than one-off fixes. ⚠️ Vendor-authored. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The handover contract is a design specification — what the human sees, when, with what authority — not a UI afterthought. |
| **Organizational** | "A human reviews it" is not a control until the split is documented and someone measures whether the review changes outcomes. |
| **Client-facing** | Answers "where are the people in this?" concretely, including how an output can be contested or reversed. |
| **LLM-native** | Agentic systems act across many steps rather than returning one output to approve, which is exactly where existing review designs break down. |

---

*Last updated: v1.0 · August 2026*
