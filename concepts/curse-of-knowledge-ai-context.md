# Curse of Knowledge (AI Context)

## One-line essence
The tendency to assume shared context that doesn't exist — the primary cause of poor AI outputs when users fail to surface what they already know.

---

## Technical definition

A cognitive bias, established experimentally long before AI: once you know something, **you cannot reliably disregard it when estimating what someone else knows.** The better informed you are, the worse your model of the uninformed listener — and the effect persists under financial incentives to correct for it, which is the finding that matters most here.

Applied to AI: a person specifying a task has a rich internal model of the situation — the constraints, the audience, the standards of a good answer, the decisions already made, the things that are obviously out of scope. **They supply a fraction of it, because the rest does not feel like information.** It feels like the background against which information appears.

**Three properties make this the dominant failure mode in practice:**

- **Expertise makes it worse, not better.** The more fluent you are in a domain, the more of it has become tacit and the less of it you think to state. Domain experts frequently write worse task specifications than newcomers, while being far better at judging the output.
- **The model does not surface the gap.** A colleague asks a clarifying question. A model produces a confident answer to the question it inferred, so **underspecification returns as a wrong result rather than as a request** — and the diagnosis has to run backwards from the output to the omission.
- **Awareness does not fix it.** The original experiments found the bias survived incentives to overcome it. Knowing about the curse of knowledge does not let you introspect your way out, which is why the remedy has to be procedural rather than attitudinal.

**This is the mechanism underneath [Human–LLM Communication Skills](human-llm-communication-skills.md)**, which names the broader competence. This entry names the specific cognitive reason its hardest component is hard, and it is separated because the remedy follows from the mechanism: if the failure were carelessness, the answer would be to try harder; because it is a structural feature of knowing things, the answer is a checklist.

---

## Plain-language version

Once you know something, you lose the ability to imagine not knowing it. This is well documented and it applies to everyone, including people who are aware of it.

When you ask an AI model to do something, you have a whole picture in your head: who this is for, what has already been decided, what would obviously be wrong, what "good" looks like here. You write down a small part of that, because the rest does not feel like something that needs saying. It feels like the situation, not like information.

The model has none of it. And unlike a colleague, it will not ask — it fills the gaps with something plausible and hands you a confident answer to a question you did not quite ask. So instead of "what do you mean by X?", you get a fluent, wrong result, and you have to work backwards to figure out what you left out.

The frustrating part is that expertise makes this worse. The more you know a subject, the more of it has become second nature and the less of it you think to mention. The people best placed to judge whether an answer is right are often the worst at explaining what they wanted.

---

## AI literacy notes

1. **You cannot introspect your way out.** The bias survives knowing about it and being paid to overcome it. Treat it as a permanent condition to be worked around, not a habit to fix.
2. **Therefore use a checklist, not effort.** The reliable remedy is external structure. **Audience, constraints, what "good" looks like, what has already been decided, what is out of scope** — five prompts that recover most of what gets omitted.
3. **Expertise is a risk factor.** The more you know, the more is tacit. If you are the expert, assume your specification is thinner than it feels.
4. **The model will not ask.** Silence is not comprehension. A confident answer is what underspecification looks like from the outside.
5. **Diagnose backwards.** When output is wrong, the first question is *what did I not say?* — before *is this model good enough?* The second question is asked far more often and is usually the wrong one.
6. **Iterating on the request beats editing the output.** Fixing the answer treats a symptom; the same gap will produce the same class of error next time.
7. **Reading back is a cheap test.** Asking the model to restate the task and its assumptions before starting exposes the inferred gaps while they are still cheap to correct.

---

## Governance notes

**Core question:** When AI output disappoints here, does anyone check the request before concluding the tool is inadequate?

**Watch for:**
- Poor output attributed to model capability with no examination of the specification — the standard misdiagnosis, and the one that leads to unnecessary tool churn
- Prompt libraries and templates that capture phrasing but omit the situational context the phrasing was standing in for, so they transfer badly between teams
- Subject-matter experts writing specifications alone, which maximizes tacit-knowledge loss precisely where the stakes are highest
- Training that teaches technique but never the diagnostic habit of asking what was unstated
- Systems where the interface allows no way to express constraints or audience, guaranteeing the omission structurally
- Repeated failures on the same task type, which usually indicate a missing shared context rather than a model limitation

**Practice:**
- Publish a short specification checklist and make it the default first response to a bad result: audience, constraints, definition of good, decisions already made, out of scope
- **Have the model restate the task and its assumptions before executing**, on anything consequential — the cheapest available check
- Pair an expert with a non-expert when specifying high-stakes tasks; the non-expert asks the questions the expert cannot see are needed
- Capture recurring context once, in a [system prompt](system-prompt.md) or retrieved brief, rather than relying on each person to remember it ([context engineering](context-engineering.md))
- Make "what did we leave unstated?" a required step in reviewing AI-related failures, ahead of any tooling decision

**Key accountability owner:** whoever owns AI enablement — because the fix is a shared checklist and a diagnostic habit, both of which are program-level artifacts rather than individual virtues.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High on the bias, Medium on the application.** The cognitive effect is peer-reviewed, foundational, replicated across decades and disciplines, and the incentive-resistance finding is from the original experiments. **The application to AI task specification is an argument by analogy** — reasoned from the mechanism and consistent with practitioner experience, but not itself measured. No study has quantified how much AI output quality is attributable to unstated context, and the claim that it is *the primary* cause is a practitioner judgment, stated as such. The recommended remedies are correspondingly conservative: external structure and a read-back, both of which are cheap and fail safely.

---

## Related concepts

- [Human–LLM Communication Skills](human-llm-communication-skills.md) — the broader competence this is the hardest component of
- [Context (AI Systems)](context-ai-systems.md) — what the omitted material would have become
- [Context Engineering](context-engineering.md) — capturing recurring context structurally instead of per-request
- [Prompt Engineering](prompt-engineering.md) — technique, which does not substitute for supplied context
- [System Prompt](system-prompt.md) — where shared context is placed once rather than remembered each time
- [AI Literacy](ai-literacy.md) — the competency set this sits inside
- [Hallucination](hallucination.md) — what fills the gap left unstated
- [Domain](domain.md) — the field-specific standards most likely to go unsaid
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — why people expect the clarifying question that never comes
- [Verification](verification.md) — the check that catches what the omission produced
- Tacit Knowledge — the knowledge type this bias operates on

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-206 | Camerer, C.; Loewenstein, G.; Weber, M. — *The Curse of Knowledge in Economic Settings: An Experimental Analysis* (Journal of Political Economy 97(5), 1989) · [link](https://doi.org/10.1086/261651) | The experimental origin: better-informed agents cannot disregard what they know when predicting less-informed others, **and the bias persists under financial incentives** — which is why the remedy must be procedural. |
| SRC-068 | Long, D.; Magerko, B. — *What is AI Literacy? Competencies and Design Considerations* (2020) · [link](https://dl.acm.org/doi/10.1145/3313831.3376727) | The competency framework this failure sits inside, and the design implication that structure beats exhortation. ⚠️ `dl.acm.org` blocks automated clients. |
| SRC-041 | White, J. et al. (Vanderbilt University) — *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT* (2023) · [link](https://arxiv.org/abs/2302.11382) | That specification has teachable structure — the basis for a checklist remedy rather than an appeal to care. |
| SRC-190 | Perry, N.; Srivastava, M.; Kumar, D.; Boneh, D. — *Do Users Write More Insecure Code with AI Assistants?* (ACM CCS, 2023) · [link](https://arxiv.org/abs/2211.03622) | Measured evidence that reworking the request changes the result: participants who reframed prompts produced fewer vulnerabilities. |
| SRC-069 | Anthropic — *Effective Context Engineering for AI Agents* (2025) · [link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | The systematic answer — capturing context deliberately rather than relying on recall. ⚠️ Vendor-produced. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Have the model restate the task and its assumptions before executing. When output is wrong, diagnose the request before the model. |
| **Organizational** | Repeated disappointment with an AI tool is more often a specification problem than a capability one — and the cheap fix is a shared checklist, not a different vendor. |
| **Client-facing** | Explains why AI work needs the brief written out more fully than a human colleague would need, and why that is not a limitation of the person asking. |
| **LLM-native** | The model never asks, so underspecification returns as a confident wrong answer. Awareness of the bias does not remove it — external structure does. |

---

*Last updated: v1.0 · August 2026*
