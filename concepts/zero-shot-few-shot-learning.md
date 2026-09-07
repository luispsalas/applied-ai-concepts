<!--meta
category: Foundations
short: Getting a task done with no examples or a handful, without changing the model — and the measured finding that the examples do not teach it what you think
aliases: [zero-shot, few-shot, in-context learning, ICL, one-shot, learning from examples, giving it examples, no training needed]
tags: [AI Literacy, Model Behavior, Prompting]
established: established
-->
# Zero-shot / Few-shot Learning

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
An AI model's ability to perform a task from no examples (zero-shot) or a handful of examples (few-shot) — without retraining the model.

---

## Technical definition

**Zero-shot** means performing a task described only in the request, with no worked examples. **Few-shot** means performing it after being shown a small number of input–output demonstrations *in the prompt itself*. In both cases the model's weights are unchanged.

Brown et al. (2020) established this as a general capability of scale: GPT-3, at 175 billion parameters, was applied across tasks **without any gradient updates or fine-tuning, with tasks and few-shot demonstrations specified purely via text interaction**, sometimes reaching competitiveness with fine-tuned approaches. The conceptual shift is the important part: **task adaptation moved from training time to inference time.**

**"Learning" is a misnomer, and the misnomer causes real errors.** Nothing is learned in the ordinary sense — no weights change, nothing persists, and the next request starts from nothing. The model conditions on what is in front of it ([context](context-ai-systems.md)). This is why the same examples must be re-supplied every time, and why success in one session tells you nothing about the next unless the same context is rebuilt.

**The finding that should change practice.** Min et al. (EMNLP 2022) tested what demonstrations actually do and found that **randomly replacing the labels in few-shot examples barely hurts performance** across classification and multiple-choice tasks on twelve models including GPT-3. What matters instead is the **label space** (which answers are possible), the **input distribution** (what the inputs look like), and the **sequence format** (how an answer should be shaped).

**Read plainly: your examples are mostly demonstrating form, not teaching correctness.** The widespread belief that supplying correct examples teaches the model to be correct is not supported for this class of task. That belief underlies a lot of practice — and a lot of assurance language.

**It is a capability, not a technique**, which distinguishes it from [prompt engineering](prompt-engineering.md). Few-shot prompting is one technique that exploits this capability; the capability itself is a property of the model, and it is also what makes a model attempt tasks nobody scoped for it.

---

## Plain-language version

Ask a model to do something it was never specifically trained for, and it will often just do it. Ask with no examples at all, and that is zero-shot. Give it two or three worked examples first, and that is few-shot.

The important thing is that nothing about the model changes. You are not training it. You are putting examples in front of it, it uses them for that one answer, and then they are gone. Ask again tomorrow without them and you are back to square one.

Now the part that surprises almost everyone. Researchers tested what those examples are actually doing by **deliberately giving the model wrong answers** in the examples — right questions, scrambled labels. Performance barely dropped.

What the examples mainly do is show the *shape* of the job: which answers are available, what the inputs look like, and what format the response should take. They are much less about teaching the model the right answer than people assume.

That matters if you have ever said, or heard, "we gave it examples of how to handle these cases correctly." That is weaker evidence than it sounds. The examples establish the format and the range of options. They are not a guarantee of correct handling, and testing is still the only thing that tells you whether it handles them correctly.

There is a second consequence. Because the model will attempt almost anything asked of it, it will attempt things nobody planned for, tested, or approved. The ability to do unscoped work is not a bug you can configure away — it comes with the capability.

---

## AI literacy notes

1. **Nothing is learned and nothing persists.** Weights do not change; the examples work only for the request that carries them.
2. **Task adaptation moved from training time to inference time** — that is the actual innovation, and it is why capability arrived without retraining.
3. **Demonstrations mainly convey format, label space and input distribution** — not correctness. Random labels barely hurt performance in the studied tasks.
4. **"We showed it correct examples" is weak evidence of correct behavior**, and it is used as strong evidence surprisingly often.
5. **It is a capability, not a technique.** Few-shot prompting exploits it; [prompt engineering](prompt-engineering.md) is the craft around it.
6. **Zero-shot capability means unscoped use is structural** — the model will attempt tasks nobody authorized or tested.
7. **Success is not portable between sessions** unless the same context is deliberately rebuilt.
8. **It is not a substitute for [fine-tuning](fine-tuning.md)** when behavior must persist, be measured, or be guaranteed.

---

## Governance notes

**Core question:** For the tasks this system performs, what is our evidence that it performs them correctly — and is any of that evidence just "we put examples in the prompt"?

**Watch for:**
- Example-based prompting cited as a control or as evidence of correct handling, without task-level testing ([evaluation](evaluation.md))
- Examples containing real customer or personal data, re-sent on every request ([privacy](privacy-ai-systems.md), [data minimization](data-minimization.md))
- Prompt examples treated as configuration and changed without review, when they materially shape output
- A system used for tasks it was never scoped or tested for, because it will attempt anything ([AI use case](ai-use-case.md), [shadow AI](shadow-ai.md))
- Zero-shot performance on a demo generalized into an assurance about production behavior
- Few-shot chosen where the requirement is durable, auditable behavior — a case for [fine-tuning](fine-tuning.md) or a deterministic control instead
- Example sets that quietly encode a bias in the label space nobody reviewed ([bias](bias-ai-systems.md))
- Failures blamed on "bad prompting" when the underlying capability was never suited to the task

**Practice:**
- **Test the task, not the prompt.** Held-out evaluation is the only evidence that a few-shot arrangement works; the examples are not evidence of themselves
- Treat prompt example sets as **versioned, reviewed artifacts** with an owner, since they shape behavior as much as configuration does
- Check example sets for personal data before they become part of every request
- Review the **label space** your examples imply — it constrains what the model will produce, and it is rarely examined
- Where behavior must be durable and auditable, prefer fine-tuning or a rule, and record why
- Scope which tasks the system is *approved* for explicitly, since capability alone will not stop it attempting others
- Re-test after any model version change — in-context behavior is not stable across versions ([model version and update](model-version-update.md))

**Key accountability owner:** whoever approves the task the system is used for — because zero-shot capability makes scope a policy decision rather than a technical limit, and nothing in the system will refuse a task simply because nobody authorized it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the capability, high on the demonstrations finding, medium on how far that finding generalizes.** That large models perform tasks from zero or few in-context examples without weight updates is established in a heavily-cited paper and is directly observable. The label-randomization result is peer-reviewed at EMNLP and tested across twelve models, which is unusually strong for a counterintuitive claim. **The stated limit is scope:** it was measured on classification and multiple-choice tasks, and this entry does not claim it holds equally for open-ended generation, code, or reasoning tasks where a wrong worked example may well mislead. **Treat the direction as established and the strength as task-dependent** — and note that in-context behavior varies between model versions, so any specific result about how examples behave is dated the moment the model is updated.

---

## Related concepts

- [Prompt Engineering](prompt-engineering.md) — the craft that exploits this capability; technique against property
- [Context (AI Systems)](context-ai-systems.md) — where the examples live, and why they must be re-sent every time
- [Fine-tuning](fine-tuning.md) — the alternative when behavior must persist and be measured
- [Large Language Models (LLMs)](large-language-models.md) — where this capability emerged with scale
- [Pre-training](pre-training.md) — where the underlying ability actually comes from
- [Evaluation](evaluation.md) — the only real evidence that a few-shot arrangement works
- [AI Use Case](ai-use-case.md) — scoping, which becomes a policy act once the model will attempt anything
- [Model Version & Update](model-version-update.md) — why in-context results do not carry across versions
- [Reasoning Models / Test-Time Compute](reasoning-models.md) — the other thing that happens at inference time rather than training time
- [Bias (AI Systems)](bias-ai-systems.md) — what an unreviewed label space can quietly encode

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-259 | Brown, T.B.; Mann, B.; Ryder, N. et al. (OpenAI — 31 authors) — *Language Models are Few-Shot Learners* (NeurIPS, 2020) · [link](https://arxiv.org/abs/2005.14165) | Establishes the capability at scale: GPT-3 (175B) applied **without any gradient updates or fine-tuning**, with tasks and demonstrations specified purely via text — the basis for this entry's claim that task adaptation moved to inference time. |
| SRC-260 | Min, S.; Lyu, X.; Holtzman, A.; Artetxe, M.; Lewis, M.; Hajishirzi, H.; Zettlemoyer, L. — *Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?* (EMNLP, 2022) · [link](https://arxiv.org/abs/2202.12837) | The load-bearing counterintuitive finding: randomly replacing labels in demonstrations barely hurts performance across 12 models; what matters is label space, input distribution and sequence format. ⚠️ Measured on classification and multiple-choice tasks — do not extend to open-ended generation without saying so. |
| SRC-142 | Zhao, W.X.; Zhou, K.; Li, J. et al. (Renmin University of China + multi-institution) — *A Survey of Large Language Models* (2023) · [link](https://arxiv.org/abs/2303.18223) | Situates in-context learning within the pre-train / adapt / utilize pipeline, and as a utilization rather than a training stage. |
| SRC-041 | White, Jules et al. (Vanderbilt University) — *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT* (2023) · [link](https://arxiv.org/abs/2302.11382) | The technique layer built on this capability, and the basis for treating example sets as reviewable artifacts rather than ad-hoc text. |
| SRC-013 | Anthropic — *Prompt engineering overview* (documentation, 2024) · [link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Vendor guidance on supplying examples in practice. ⚠️ Vendor documentation — describes recommended use, not independent evidence of effectiveness. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Test the task, not the prompt. Version and review example sets, check them for personal data, and re-test after every model update. |
| **Organizational** | "We gave it correct examples" is weak evidence of correct handling. Because the model will attempt anything asked, scope becomes a policy decision rather than a technical limit. |
| **Client-facing** | Explains why a system can handle a request it was never specifically built for, and why that flexibility is not itself an assurance of quality. |
| **LLM-native** | Nothing is learned and nothing persists. Demonstrations convey label space, input distribution and format — randomizing the labels barely hurts, which is not what most practice assumes. |

---

*Last updated: v1.0 · September 2026*
