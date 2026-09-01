<!--meta
category: Reliability & Quality
short: Deliberately attacking your own AI system — probing for jailbreaks, data leaks, and harmful outputs before anyone else finds them
aliases: [adversarial testing, attacking your own system, penetration testing AI, stress testing, safety testing]
tags: [Security, Evaluation, Safety]
-->
# Red Teaming

## One-line essence
Deliberately attacking your own AI system — probing for jailbreaks, data leaks, and harmful outputs before adversaries or users find them.

---

## Technical definition

The structured adversarial evaluation of an AI system: deliberately attempting to elicit the behavior the system is supposed to prevent, and treating what succeeds as findings to be fixed. It is distinct from ordinary [evaluation](evaluation.md), which measures whether a system does what it should on representative inputs. Red teaming asks the opposite question — what can be made to happen on hostile ones.

Two complementary modes, established in the foundational literature:

- **Manual red teaming** — human testers probe the system, producing a dataset of successful attacks alongside operational lessons. Scaling studies across model sizes and training regimes found that harmlessness training changes attack success substantially, and that the resulting attack data is itself a reusable asset.
- **Automated red teaming** — one language model generates test cases designed to elicit harmful behavior from another, then a classifier scores the responses. This converts red teaming from a periodic manual exercise into a repeatable, scalable process that can run continuously and cover far more of the input space than humans can.

Neither replaces the other: automated methods provide coverage and regression testing; human testers find the framings and contexts a generator does not think to produce.

Scope has widened as systems have. Red teaming a model means probing outputs. Red teaming a *system* means probing the whole surface — [tool](tool-use.md) permissions, retrieval sources, the [system prompt](system-prompt.md), and the boundaries between [agents](multi-agent-systems.md) — because that is where real consequences live.

Critically, findings are only meaningful against a specific deployment. A model provider's red teaming was not run against your prompts, your tools, your data, or your users.

---

## Plain-language version

Red teaming is attacking your own system on purpose, before someone else does. You try to make it say and do the things it shouldn't, write down everything that works, and fix it. It is the difference between hoping a system is safe and having actually tried to break it.

---

## AI literacy notes

1. **Red teaming answers a different question than evaluation.** Evaluation asks "does it work?"; red teaming asks "what can I make it do?" A system can score well on every benchmark and fail immediately under adversarial pressure. You need both.
2. **The vendor's red teaming is not yours.** Providers test base model behavior. They did not test your system prompt, your tool permissions, your retrieval corpus, or your users' incentives — which is where deployment-specific failures live.
3. **Findings expire.** A red-team result describes one system state. A new model version, a changed prompt, or an added tool invalidates it. Treat red teaming as a recurring activity tied to change, not a launch-day certificate.
4. **Automate for coverage, use humans for imagination.** Generated attacks cover volume and catch regressions; human testers find the socially or contextually creative framings that a generator wouldn't produce.
5. **The output is a fix list, not a score.** A red-team exercise that produces a reassuring number and no remediated findings has been run as theater.

---

## Governance notes

**Core question:** Has anyone genuinely tried to break *this* system, in *this* configuration — and what happened to what they found?

**Watch for:**
- The provider's model-level safety testing cited as evidence that the deployment is safe
- Red teaming performed once before launch and never repeated after model or tool changes
- Findings logged without owners, deadlines, or verification that the fix worked
- Scope limited to model outputs while tool permissions and data access go untested
- Red teaming conducted by the team that built the system, with no independent perspective

**Practice:**
- Trigger a red-team pass on change, not on the calendar — new model version, new tool, new data source, new user population
- Test the system, not just the model: tool permissions, retrieval sources, prompt hierarchy, agent boundaries
- Track findings like security defects — owner, severity, remediation, retest
- Keep and reuse successful attacks as a regression suite, so old failures cannot return silently
- Define rules of engagement in advance, including how genuinely harmful generated content is handled and stored

**Key accountability owner:** the security function, jointly with the system owner who must accept or remediate each finding.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The methods are documented in peer-reviewed and widely replicated work, and the practice is established in industry and named in regulatory guidance. Less settled: what constitutes adequate coverage, how to measure whether a red-team exercise was sufficient, and how findings should be disclosed.

---

## Related concepts

- [Jailbreak](jailbreak.md) — a primary class of what red teaming looks for
- [Prompt Injection](prompt-injection.md) — another, targeting the application rather than the model
- [Evaluation (AI Systems)](evaluation.md) — the complementary practice: expected behavior on representative inputs
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — where findings typically get remediated
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the map of what to probe for
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — a specific target: can the system be made to reveal what it shouldn't?
- [Tool Use](tool-use.md) — the highest-consequence surface, and the one most often left out of scope
- [Compliance (AI Systems)](compliance-ai-systems.md) — adversarial testing increasingly appears as a regulatory expectation, not just good practice

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-158 | Perez, E.; Huang, S.; Song, F.; Cai, T.; Ring, R.; Aslanides, J.; Glaese, A.; McAleese, N.; Irving, G. — *Red Teaming Language Models with Language Models* (EMNLP, 2022) · [link](https://aclanthology.org/2022.emnlp-main.225/) | Automated red teaming: using one model to generate test cases against another, making the practice scalable and repeatable. |
| SRC-159 | Ganguli, D.; Lovitt, L.; Kernion, J.; Askell, A.; Bai, Y. et al. (Anthropic) — *Red Teaming Language Models to Reduce Harms* (2022) · [link](https://arxiv.org/abs/2209.07858) | Manual red-teaming methodology at scale, scaling behaviors across models, and operational lessons on running a program. ⚠️ Vendor-authored. |
| SRC-157 | Wei, A.; Haghtalab, N.; Steinhardt, J. — *Jailbroken: How Does LLM Safety Training Fail?* (NeurIPS, 2023) · [link](https://papers.nips.cc/paper_files/paper/2023/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | The failure structure red teaming exploits, and why findings are model-state-specific. |
| SRC-148 | OWASP Foundation (GenAI Security Project) — *OWASP Top 10 for LLM Applications* (2025) · [link](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Application-security framing and the risk categories a system-level red team should cover. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places adversarial testing within a recognized risk-management lifecycle rather than treating it as an ad-hoc activity. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Adversarial testing belongs in the delivery pipeline, with successful attacks kept as a regression suite. |
| **Organizational** | The question to ask before approving a deployment: has anyone tried to break this specific configuration, and what was fixed? |
| **Client-facing** | Distinguishes "the vendor says it's safe" from "we tested it in our context" — a meaningful assurance difference. |
| **LLM-native** | Model and prompt changes invalidate prior findings; red teaming is continuous, not a launch gate. |

---

*Last updated: v1.0 · August 2026*
