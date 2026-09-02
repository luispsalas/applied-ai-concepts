<!--meta
category: Interaction & Design
short: Working well with a model is mostly noticing what you left unstated — and knowing when not to trust the answer
aliases: [talking to AI, how to work with AI, AI communication, getting better answers, working with a model]
tags: [AI Literacy, Prompting]
established: emerging
-->
# Human–LLM Communication Skills

> **Term status — Emerging.** In active use and genuinely useful, but not yet settled — definitions still vary between sources. Read the Confidence level before relying on the term in a formal document.

## One-line essence
The ability to communicate effectively with language models — structuring inputs, recognizing output limitations, and knowing when not to trust the result.

---

## Technical definition

The practical competence of working with a language model as a *counterpart* rather than as a search box or a command line. It is a subset of [AI literacy](ai-literacy.md) — the operational part — and it is broader than [prompt engineering](prompt-engineering.md), which concerns the construction of the input.

Three capabilities, and the second and third are the ones that separate practitioners:

- **Externalizing what you know.** A model has none of your situation unless you supply it. The hardest part is not phrasing but *noticing what you have not said* — the constraints, audience, prior decisions and standards of "good" that feel too obvious to state. This is the curse of knowledge operating against you: expertise makes tacit assumptions less visible, so the people best placed to judge the output are often worst placed to specify it.
- **Reading output for what it can and cannot tell you.** Fluency is generated independently of correctness, so tone carries no reliability signal. Recognizing a plausible-but-unsupported answer, noticing an absent caveat, spotting where a confident passage crosses a gap — these are reading skills, and they are not the same as domain expertise.
- **Calibrating trust per task.** Knowing which classes of work this system is reliable at, which it is confidently bad at, and which need [verification](verification.md) you can actually afford. The competence is *deciding*, not *trusting less*.

**It is a communication skill in a strict sense, and that has a specific consequence:** the model will not tell you when your request was underspecified. A human colleague asks. A model produces a confident answer to the question it inferred — so ambiguity surfaces as a wrong result rather than as a clarifying question, and the diagnosis has to run backwards from the output.

**Why this is a distinct competency and not just experience.** Peer-reviewed AI-literacy frameworks converge on the same structure: knowing what these systems are, evaluating their output, using them effectively, and understanding their ethical implications. The communication layer sits across all four, and unlike the others it is *behavioral* — it is exercised in every interaction and it degrades when [automation bias](automation-bias.md) sets in.

---

## Plain-language version

Working well with an AI model is a learnable skill, and it is not mostly about knowing clever phrasings.

The largest part is noticing what you have not said. The model does not know your organization, your constraints, who the output is for, or what you would consider a good answer. It also will not ask — it will produce something confident based on whatever it inferred. So a vague request comes back as a wrong answer rather than as a question, and you have to work backwards to see what was missing.

The second part is reading the answer properly. These systems sound equally certain whether they are right or wrong, so the confidence in the text tells you nothing. Learning to spot the sentence that glides over a gap is a real skill and takes practice.

The third is judgment about when to rely on it at all — which tasks it does well, which it does badly while sounding fine, and when the checking would cost more than doing the work yourself. That judgment is the competence. Not trusting it more, and not trusting it less.

---

## AI literacy notes

1. **Underspecification returns as a wrong answer, not a question.** The model fills gaps rather than flagging them. If the output is off, the first thing to examine is what you left unstated.
2. **Your expertise works against you here.** The more you know a domain, the more of it is tacit and the less of it you think to say. Experts often write worse requests than novices for exactly this reason.
3. **Say who it is for and what "good" looks like.** Audience, constraints and success criteria are the three omissions that account for most disappointing output.
4. **Confidence in the text is not information.** Assertive phrasing is generated the same way as correct content. Read for support, not for tone — see [Confidence vs Accuracy](confidence-vs-accuracy.md).
5. **Ask for what would change the answer.** Requesting counter-arguments, alternatives, or the weakest part of a claim recovers some of what a fluent answer smoothed over. It is the single highest-yield habit.
6. **Iterate on the input, not just the output.** Rewriting your request usually beats editing the response — and there is measured evidence that people who rework their prompts and stay skeptical get materially better results.
7. **The skill decays quietly.** As a system becomes usually-right, checking stops, and the reading skill erodes with it. Sustaining the competence is a discipline, not a milestone.
8. **Knowing when *not* to use it is part of the skill.** Tasks where verification would cost more than doing the work are tasks to do yourself. That is a competent judgment, not a failure of adoption.

---

## Governance notes

**Core question:** Do the people using these systems have the competence the deployment assumes — and how would you know if they did not?

**Watch for:**
- Tool access rolled out with no accompanying capability, on the assumption that a chat interface is self-explanatory
- Training that covers prompting technique but not output evaluation or trust calibration — the two parts that actually determine outcomes
- Quality attributed entirely to the model when the variance is between users
- No shared record of what has worked: every person rediscovering the same patterns privately, which is the reuse failure this domain makes expensive
- The competence assumed to be uniform across staff, when it varies enormously and correlates poorly with seniority
- Skill erosion as reliance grows, with nothing measuring it ([automation bias](automation-bias.md))

**Practice:**
- Treat this as a named competency in the [AI literacy](ai-literacy.md) program, with the emphasis on output evaluation and trust calibration rather than prompt phrasing
- Give people a way to share working patterns internally, so the learning compounds instead of being rediscovered
- Make "what did you leave unstated?" the first diagnostic question for a poor result, before anyone concludes the tool is inadequate
- Pair the training with an explicit statement of what the deployment is and is not for, so trust calibration has a reference point ([AI use case](ai-use-case.md))
- Where output quality matters, make the reviewer someone with the domain knowledge to read it — communication skill does not substitute for expertise ([verification](verification.md))

**Key accountability owner:** whoever owns the AI literacy or enablement program — with the system owner accountable for stating what the deployment is fit for, since trust cannot be calibrated against an unstated purpose.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium.** The component competencies are well grounded — AI-literacy frameworks are peer-reviewed and convergent, prompt-pattern taxonomies are documented, and the skepticism-improves-outcomes finding is from a controlled study. **Weaker on the whole:** there is no established assessment for this competency, no evidence on what training actually transfers, and the practitioner literature is dominated by technique lists that overweight phrasing relative to evaluation and trust calibration. Treat the structure here as a reasoned organization of established parts rather than as a validated model.

---

## Related concepts

- [AI Literacy](ai-literacy.md) — the broader competency set; this is its operational layer
- [Prompt Engineering](prompt-engineering.md) — the narrower, technique-focused subset
- [Context (AI Systems)](context-ai-systems.md) — what you are actually supplying when you communicate with a model
- [Verification](verification.md) — the check that trust calibration decides the level of
- [Confidence vs Accuracy](confidence-vs-accuracy.md) — why reading for tone fails
- [Concealing Uncertainty](concealing-uncertainty.md) — the absent caveat this skill learns to notice
- [Sycophancy (LLMs)](sycophancy-llms.md) — why pushing back on a model is not a reliable test of a claim
- [Automation Bias](automation-bias.md) — the mechanism by which the skill quietly stops being exercised
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — the reflex this competency has to work against
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the obligation this skill is exercised in service of
- [Human–AI Collaboration Model](human-ai-collaboration-model.md) — the organizational counterpart of an individual competency
- [Curse of Knowledge (AI Context)](curse-of-knowledge-ai-context.md) — the specific mechanism behind the hardest part of this skill
- [Cognitive Offloading & Deskilling](cognitive-offloading-deskilling.md) — what happens to the competency under sustained reliance

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-068 | Long, D.; Magerko, B. — *What is AI Literacy? Competencies and Design Considerations* (2020) · [link](https://dl.acm.org/doi/10.1145/3313831.3376727) | The competency structure this entry's layer sits across, from a peer-reviewed framework rather than practitioner convention. ⚠️ `dl.acm.org` blocks automated clients — the DOI is live, not dead. |
| SRC-067 | OECD / European Commission — *Empowering Learners for the Age of AI: An AI Literacy Framework* (2025) · [link](https://ailiteracyframework.org/wp-content/uploads/2025/05/AILitFramework_ReviewDraft.pdf) | Intergovernmental convergence on the same four-part structure — knowing, evaluating, using, and understanding implications. ⚠️ Review draft, not final. |
| SRC-041 | White, J. et al. (Vanderbilt University) — *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT* (2023) · [link](https://arxiv.org/abs/2302.11382) | That effective interaction has documented, teachable structure rather than being purely tacit craft. |
| SRC-190 | Perry, N.; Srivastava, M.; Kumar, D.; Boneh, D. — *Do Users Write More Insecure Code with AI Assistants?* (ACM CCS, 2023) · [link](https://arxiv.org/abs/2211.03622) | The measured payoff: participants who stayed skeptical and reworked their prompts produced fewer vulnerabilities — while the assisted group overall did worse *and* felt more confident. |
| SRC-172 | Zhou, K.; Hwang, J.D.; Ren, X.; Sap, M. — *Relying on the Unreliable: The Impact of Language Models' Reluctance to Express Uncertainty* (ACL, 2024) · [link](https://aclanthology.org/2024.acl-long.198/) | Why reading output is a learned skill: the uncertainty signal a reader would use was trained out, and overreliance is the documented result. |
| SRC-013 | Anthropic — *Prompt engineering overview* (2024) · [link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Standard technique vocabulary. ⚠️ Vendor documentation — naming conventions only, not authority. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Iterate on the input rather than the output; ask what would change the answer; make "what did I leave unstated?" the first diagnostic on a bad result. |
| **Organizational** | Output quality varies more between users than between models. Access without capability is an unfunded assumption, and the training that matters is evaluation and trust calibration, not phrasing. |
| **Client-facing** | Explains why working with these systems is a skill worth developing, and why the valuable part is judgment about when to rely on them. |
| **LLM-native** | The model never asks a clarifying question — underspecification returns as a confident wrong answer, so diagnosis runs backwards from the output to the omission. |

---

*Last updated: v1.0 · August 2026*
