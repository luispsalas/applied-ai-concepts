<!--meta
category: System Architecture
short: Bypassing a model's safety training through crafted prompts rather than a technical flaw — getting it to do what it was trained to refuse
aliases: [prompt jailbreaking, bypassing safety, getting it to break its rules, safety bypass, DAN]
tags: [Security, Safety]
established: established
-->
# Jailbreak

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Bypassing an AI model's safety training through crafted prompts, rather than exploiting a technical flaw — getting the model to do what it was trained to refuse, from the inside.

---

## Technical definition

An input crafted to make a model produce output its safety training was intended to prevent. The attack surface is the model's own behavior: no code is exploited, no system is breached, and the request arrives through the ordinary input channel. The model is persuaded rather than compromised.

Peer-reviewed analysis identifies two structural reasons safety training fails, both consequences of how models are trained rather than bugs to be patched:

- **Competing objectives** — the model is trained both to be helpful and to refuse certain requests, and those goals conflict. An attack constructs a framing in which refusing appears to violate the stronger objective (role-play, a fictional premise, an authority claim, a prefix that makes refusal grammatically awkward).
- **Mismatched generalization** — safety training does not cover every domain the model has capabilities in. Where capability extends further than safety coverage, an input expressed in that gap (an unusual encoding, another language, an obscure format) reaches the capability without triggering the trained refusal.

The distinction from [prompt injection](prompt-injection.md) matters and is often blurred. Jailbreaking targets the **model's safety behavior**, and the attacker is typically the user. Prompt injection targets the **application's instruction hierarchy**, smuggling instructions through content the model consumes, and the attacker is typically a third party. A jailbreak makes a model say something; an injection makes an application do something. They co-occur but call for different defenses.

Because the mechanism is behavioral, there is no patch that closes the category. Safety training raises the cost of an attack; it does not establish a boundary.

---

## Plain-language version

A jailbreak is talking a model into something it was trained to refuse — with a role-play setup, a hypothetical framing, or wording that slips past what it learned to catch. Nothing is hacked in the usual sense; the model is convinced. And because it works by persuasion, there is no single fix that ends it — which is why anything that actually matters needs a check outside the model.

---

## AI literacy notes

1. **A jailbreak is a failure of behavior, not of code.** There is no vulnerability to patch and no version that closes the class. Safety training shifts the odds; it does not draw a line. Treat model refusal as a deterrent, never as a control.
2. **Refusal is the weakest possible boundary.** If the only thing preventing an outcome is that the model was trained to say no, the outcome is reachable. Anything consequential belongs behind an enforced control — a [permission model](permission-model-ai.md), a [guardrail](guardrails-ai-systems.md), or a human approval — that operates whatever the model says.
3. **Not the same as prompt injection, and the difference changes the defense.** Jailbreak: the user attacks the model's safety behavior. Injection: a third party attacks the application through content. Conflating them leads to defending the wrong layer.
4. **The severity depends entirely on what the model can reach.** A jailbroken chatbot produces text someone shouldn't have. A jailbroken agent with [tools](tool-use.md) takes an action against a live system. Capability, not the jailbreak, sets the blast radius.
5. **Publicly known jailbreaks are the visible fraction.** Techniques circulate, get patched, and are re-derived in variants. Absence of a known working jailbreak is not evidence of robustness.

---

## Governance notes

**Core question:** If the model's refusal failed right now, what would actually stop the harmful outcome?

**Watch for:**
- Safety training cited as a control in a risk assessment, with nothing enforced behind it
- Consequential capability reachable purely by persuading the model, with no authorization step
- No monitoring for refusal-bypass attempts, so repeated probing goes unnoticed
- Vendor safety claims accepted without independent [red teaming](red-teaming.md) against your own deployment and use case

**Practice:**
- Enforce outside the model: authorization, tool permissions, and approval gates that do not depend on the model choosing to refuse
- [Red-team](red-teaming.md) your own deployment rather than relying on the model provider's evaluations, which were not run against your context
- Log and alert on refusal-bypass patterns; treat a spike as a security signal, not a curiosity
- Re-test after every model, [system prompt](system-prompt.md), or tool change — safety behavior is not stable across versions

**Key accountability owner:** the system owner, with the security function.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the mechanism — the competing-objectives / mismatched-generalization account is peer-reviewed and has held up as models changed. **Lower** on defense: no method reliably prevents jailbreaks, effectiveness claims are contested, and published attacks and mitigations both age quickly.

---

## Related concepts

- [Prompt Injection](prompt-injection.md) — the adjacent attack, aimed at the application's instruction hierarchy rather than the model's safety behavior
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the enforced constraints that hold when refusal doesn't
- [Red Teaming](red-teaming.md) — the practice of finding these failures before someone else does
- [System Prompt](system-prompt.md) — a soft control, and a frequent target of bypass attempts
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — where this sits among the ways AI systems go wrong
- [Tool Use](tool-use.md) — what determines whether a jailbreak yields bad text or a real-world action
- [Permission Model (AI)](permission-model-ai.md) — the enforced boundary that makes model refusal non-load-bearing
- [Alignment (AI Systems)](alignment-ai-systems.md) — safety training is an alignment technique; jailbreaks are evidence of its limits

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-157 | Wei, A.; Haghtalab, N.; Steinhardt, J. (UC Berkeley) — *Jailbroken: How Does LLM Safety Training Fail?* (NeurIPS, 2023) · [link](https://papers.nips.cc/paper_files/paper/2023/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | The two structural failure modes — competing objectives and mismatched generalization — and evidence they defeat frontier models. |
| SRC-148 | OWASP Foundation (GenAI Security Project) — *OWASP Top 10 for LLM Applications* (2025) · [link](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Industry-standard framing of model-behavior attacks and layered mitigation in application security terms. |
| SRC-060 | He, Yifeng et al. (UC Davis) — *Security of AI Agents* (2026) · [link](https://arxiv.org/abs/2406.08689) | Why agent capability determines the consequence of a safety bypass; separates agent security from model security. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Model refusal cannot be an enforcement point. Anything consequential needs a control that holds when the model is talked out of refusing. |
| **Organizational** | "The model won't do that" is not a risk control and should not survive a risk assessment as one. |
| **Client-facing** | Explains why safety claims come with limits, and why guarantees rest on system design rather than on model behavior. |
| **LLM-native** | Safety training is a probabilistic deterrent with a known failure structure — design as though it will be defeated. |

---

*Last updated: v1.0 · August 2026*
