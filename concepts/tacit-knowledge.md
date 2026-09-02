<!--meta
category: Organizational Readiness
short: The expertise people have but cannot fully put into words — the hardest thing to give an AI system as context, and the first thing lost when people stop practicing
aliases: [know-how, unwritten knowledge, Polanyi's paradox, we can know more than we can tell, implicit knowledge, expert intuition, institutional knowledge, undocumented expertise]
tags: [AI Literacy]
established: established
-->
# Tacit Knowledge

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Competence that people demonstrably possess but cannot fully articulate — the reason expert judgment resists being written down, the hardest input to supply an AI system deliberately, and the capacity that erodes quietly when the work is delegated.

---

## Technical definition

The concept is Michael Polanyi's, from *The Tacit Dimension* (1966), and rests on a single observation: **"we can know more than we can tell."** A person recognizes a face without being able to describe how, judges a document as off without being able to say which sentence, or performs a skilled physical task they could never write instructions for. The knowledge is real and demonstrable in performance; it is not available for inspection, including by the person holding it.

Nonaka (1994) made this an organizational problem rather than a philosophical one, treating knowledge creation as **conversion between tacit and explicit forms** — and treating the tacit half as the part that transfers through shared practice, apprenticeship and observation rather than through documentation.

**Why this became central to AI rather than remaining a knowledge-management topic.** Autor (2014) named **Polanyi's paradox** as the explanation for why computerization stalled where it did: tasks demanding tacit knowledge — adaptability, common sense, judgment — resisted automation precisely because nobody could specify the rules to program, producing labor-market polarization rather than broad displacement.

**Machine learning is a direct attack on that paradox, and this is the shift the term now marks.** Autor's own framing is that contemporary AI aims to overcome the paradox by **learning from human examples — inferring the tacit rules people apply intuitively but cannot codify.** A system trained on demonstrations does not need the rule stated. That is why the automation boundary moved where it did, and why capabilities that seemed structurally protected turned out not to be.

**The practical inversion, and the part most relevant to daily use.** Working with an LLM through prompts and context is an **explicit-knowledge interface**: you get the benefit of your expertise only insofar as you can state it. Experts are systematically bad at this, because the knowledge most worth transferring is the part they cannot see themselves holding — the mechanism the [curse of knowledge](curse-of-knowledge-ai-context.md) describes. **So a model may be capable of the task while the expert is unable to specify it**, and the bottleneck sits on the human side of the interface.

The same asymmetry runs through oversight. A reviewer who says *"this is wrong, I can't tell you why yet"* is exercising tacit judgment, and it is frequently correct. A review process that accepts only articulated objections discards exactly the signal that is hardest to replace.

---

## Plain-language version

There is a lot you know that you could not write down. You can tell a colleague is uneasy in a meeting. You can read a contract and feel that something is off before you find it. An experienced nurse notices a patient is deteriorating before the numbers say so. That knowledge is real — it shows up in what people get right — but it is not available as words, not even to the person using it.

This used to be the line automation could not cross. You cannot program a rule nobody can state, so jobs built on judgment stayed put while jobs built on stated procedures did not.

Modern AI attacks that line from a different angle. Instead of being given the rules, it is shown enormous numbers of examples and picks up the patterns underneath. It never needs anyone to explain the rule. That is why capabilities people assumed were safely human turned out not to be.

But there is a catch that lands on us rather than the machine. When you work with an AI, you communicate in words. So you get the value of your expertise only to the extent you can say it — and the most valuable part is the part you cannot. Experts are especially prone to this: they skip what feels obvious, which is usually the thing that took fifteen years to learn.

And it cuts a third way. When someone reviews AI output and says "this is wrong, I don't know why yet," that hunch is often right and is very hard to replace. A process that only accepts objections with reasons attached throws it away.

---

## AI literacy notes

1. **Polanyi's paradox has narrowed, not closed.** Learning from examples bypasses the need to state a rule — which is why the automation frontier moved.
2. **Prompting is an explicit-knowledge interface.** Your expertise reaches the system only in the words you manage to supply.
3. **Experts under-specify most.** The knowledge that matters is the knowledge they cannot see themselves using ([curse of knowledge](curse-of-knowledge-ai-context.md)).
4. **The bottleneck is often articulation, not capability.** A disappointing result frequently means the task was under-described, not that the model could not do it.
5. **"It's wrong but I can't say why" is signal, not noise.** Discarding unarticulated objections removes the hardest-to-replace part of human review.
6. **Tacit knowledge is acquired by doing.** Delegating the doing removes the acquisition path, which is the mechanism behind [deskilling](cognitive-offloading-deskilling.md).
7. **It is the least documented and most load-bearing organizational asset**, and therefore systematically absent from any [knowledge base](knowledge-base.md) an AI system is given.
8. **Examples transfer more than instructions do.** Where a rule cannot be stated, showing cases is usually the better channel — for models and for people.

---

## Governance notes

**Core question:** What does this system depend on that nobody has written down — and where are we requiring people to articulate judgment that is valuable precisely because it cannot be?

**Watch for:**
- An AI system given the documented process while the real process lives in practitioners' heads, and the gap discovered only in production ([context engineering](context-engineering.md))
- Review procedures that accept only reasoned objections, filtering out unarticulated expert doubt
- Automation of the routine parts of a role, removing the practice through which judgment about the hard parts was acquired ([cognitive offloading & deskilling](cognitive-offloading-deskilling.md))
- Knowledge-capture programs that record procedures and miss the exceptions, workarounds and judgment calls that constitute the actual expertise
- [Human oversight](human-in-the-loop.md) assigned to reviewers who never developed the tacit competence the role assumes — oversight that is present on paper and unexercisable in fact
- Poor output blamed on the model where the input was an under-specified task ([human–LLM communication skills](human-llm-communication-skills.md))
- Succession and single-point-of-knowledge risk unexamined because the knowledge was never inventoried
- Training data assembled from documented outcomes only, so the corpus inherits the documentation's blind spots ([training data](training-data.md))

**Practice:**
- **Elicit through cases, not questionnaires** — ask experts to work through real examples, including near-misses and exceptions, rather than to describe their method
- Capture *why* alongside *what*: the rejected alternative usually carries more of the expertise than the chosen answer
- Design review so an unarticulated objection can stop or escalate a decision without requiring a justification first
- Preserve deliberate practice on tasks where human judgment must remain available — competence that is not exercised does not persist
- Treat "the model got it wrong" as a hypothesis to test against task specification before it is accepted as a capability limit
- Inventory where undocumented knowledge is load-bearing, and name the risk in the same register as any other single point of failure
- Where a rule cannot be stated, supply worked examples instead — for the system and for new practitioners

**Key accountability owner:** the process or function owner, not the AI team — because the knowledge in question is theirs, its absence is invisible from outside the function, and no one else is positioned to notice that what the system was given is not what the work actually requires.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the concept, which is foundational, sixty years old, and uncontested across philosophy, organizational theory and labor economics. **Medium on the AI-specific claims.** That machine learning erodes Polanyi's paradox is well argued and evidently borne out, but *how far* it extends is genuinely open and actively disputed — learning tacit patterns from examples is not the same as holding the understanding those patterns came from, and the distinction is unresolved. The articulation-bottleneck and oversight arguments here are **reasoned extensions of established findings rather than directly measured results**; the underlying mechanisms (the curse of knowledge, skill decay through disuse) are evidenced, their specific application to LLM interfaces is not yet well studied. Autor's 2014 analysis also predates modern LLMs and is cited here for the paradox and its framing, not for current predictions about which tasks remain out of reach.

---

## Related concepts

- [Curse of Knowledge (AI Context)](curse-of-knowledge-ai-context.md) — why experts omit exactly what they most need to supply
- [Human–LLM Communication Skills](human-llm-communication-skills.md) — the articulation capability this makes load-bearing
- [Context Engineering](context-engineering.md) — the practice of getting unwritten knowledge into a system deliberately
- [Cognitive Offloading & Deskilling](cognitive-offloading-deskilling.md) — the erosion path: delegate the doing, lose the acquisition
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — oversight that depends on competence the reviewer must actually have
- [AI Literacy](ai-literacy.md) — the counterpart capability on the human side of the interface
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — where the division of labor is set, and where tacit judgment should stay
- [Knowledge Base](knowledge-base.md) — holds the explicit half, and is silently missing this one
- [Persistent Synthesis](persistent-synthesis.md) — the attempt to accumulate what would otherwise stay unwritten
- [Training Data](training-data.md) — learning from examples is how models reach knowledge nobody codified
- [Verification](verification.md) — checking often relies on judgment the checker cannot fully justify
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — responsibility assumes a capacity to judge, which has to be maintained

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-229 | Polanyi, M. — *The Tacit Dimension* (Doubleday, Garden City NY, 1966; based on the 1962 Terry Lectures, Yale University) · [link](https://press.uchicago.edu/ucp/books/book/chicago/T/bo6035368.html) | The originating formulation — "we can know more than we can tell" — and the claim that such knowledge is unavailable to inspection by its holder. ⚠️ Print monograph; link is to the 2009 University of Chicago Press reissue. |
| SRC-230 | Nonaka, I. — *A Dynamic Theory of Organizational Knowledge Creation* (Organization Science 5(1), 14–37, 1994) · [link](https://doi.org/10.1287/orsc.5.1.14) | Moves the concept from philosophy to organizations: knowledge creation as conversion between tacit and explicit forms, with the tacit half transferring through shared practice rather than documentation. |
| SRC-231 | Autor, D. — *Polanyi's Paradox and the Shape of Employment Growth* (NBER Working Paper 20485, 2014) · [link](https://www.nber.org/papers/w20485) | Names Polanyi's paradox as the constraint on computerization and the driver of labor-market polarization — and identifies the AI response: learning from human examples to infer tacit rules that cannot be codified. ⚠️ Working paper; predates modern LLMs. |
| SRC-017 | Verma, Rahul (LangChain) — *Human judgment in the agent improvement loop* (2026) · [link](https://blog.langchain.com/human-judgment-in-the-agent-improvement-loop/) | Tacit knowledge capture as a core design challenge for human oversight: expert judgment must be encoded into evaluation pipelines because human review alone does not scale. ⚠️ Vendor-authored. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Treat "the model got it wrong" as a hypothesis about task specification first. Where a rule cannot be stated, supply worked examples — including near-misses — rather than instructions. |
| **Organizational** | Inventory where undocumented knowledge is load-bearing and name it as a single point of failure. Elicit through real cases, not questionnaires, and preserve the practice through which judgment is acquired. |
| **Client-facing** | Explains why a system given all the documentation still misses what an experienced person would catch, and why expert review remains part of the service. |
| **LLM-native** | Learning from examples bypasses the need to state a rule, which is why the automation frontier moved. But the prompt is an explicit-knowledge interface, so the bottleneck relocated to what the expert can articulate. |

---

*Last updated: v1.0 · September 2026*
