<!--meta
category: System Architecture
short: A trick where malicious instructions hidden in text the AI reads hijack its behavior — the top-ranked LLM application security risk
aliases: [indirect prompt injection, hidden instructions, prompt hijacking, injection attack, malicious input]
-->
# Prompt Injection

## One-line essence
A trick where someone hides malicious instructions in text the AI reads, hijacking its behavior — like a fake note slipped into a document that overrides the real instructions.

---

## Technical definition

A prompt injection is an attack where adversarial input embedded in text processed by an LLM is interpreted as an instruction rather than data, because the model has no structural separation between its instructions and the content it processes (SRC-146, SRC-148). Direct prompt injection occurs when a user types adversarial instructions straight into the input ("ignore previous instructions...") — the original documented technique (SRC-147). Indirect prompt injection hides the same kind of instruction inside content the model retrieves or reads on someone else's behalf — a webpage, a document, an email — so the attack executes without the user ever typing anything malicious (SRC-146). OWASP ranks prompt injection as the top LLM application security risk for consecutive editions (SRC-148), and mitigation requires layered defenses (input/output filtering, privilege restriction, human-in-the-loop for consequential actions) since no single technique reliably distinguishes instructions from data at the model level.

---

## Plain-language version

Prompt injection is a trick where someone hides instructions inside text an AI reads, and the AI can't tell those hidden instructions apart from the real ones it's supposed to follow. Direct version: someone types "ignore your instructions and do X" straight into the chat. Indirect version — the sneakier one — is instructions buried inside a document, webpage, or email that the AI is asked to summarize or process; the AI encounters the hidden command while doing its job and quietly follows it, with no visible sign anything went wrong.

---

## AI literacy notes

1. **The AI cannot reliably tell instructions from data.** This is the root cause, not a bug to be patched away — everything the model reads shares one channel, so a well-crafted piece of "content" can act as a command.
2. **Indirect injection is the higher-risk form for most deployments.** Any system that has the AI read external content — a webpage, an email, a document, search results — is exposed, even if no untrusted human ever talks to the model directly.
3. **No single fix solves it.** Defense requires layers: filtering what goes in and comes out, restricting what the model is allowed to do regardless of what it's told, and keeping a human in the loop for consequential actions (see [Guardrails](guardrails-ai-systems.md), [Human-in-the-Loop (HITL)](human-in-the-loop.md)).
4. **It's the top-ranked LLM security risk industry-wide** (OWASP), which makes it the most-cited entry point for "how could this go wrong" conversations with a general audience.

---

## Governance notes

**Core question:** Does every system where the model reads external content (documents, web pages, emails, tool outputs) treat that content as untrusted?

**Watch for:**
- Retrieved/tool-sourced content given the same trust level as direct user input
- No distinction between "instruction" and "data" channels in the harness
- Consequential actions triggered by model output with no human check

**Practice:**
- Treat all external content the model reads as potentially adversarial
- Apply output filtering and action permissioning independent of what the model was "told" to do
- Require human approval for high-consequence actions triggered by model behavior after reading untrusted content

**Key accountability owner:** the harness/security owner.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The mechanism (single-channel instructions and data) is well understood and consistently reproduced across systems; ranked the top LLM application risk in successive OWASP editions. Reliable technical prevention remains an open problem — mitigation is layered defense, not a solved fix.

---

## Related concepts

- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the layered defenses (input/output filtering, action constraints) that mitigate injection risk
- [Harness Paradigm](harness-paradigm.md) — the control layer where instruction/data separation and permission enforcement must be implemented
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — prompt injection is a named, high-severity failure mode for any system that reads external content
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — a common objective and consequence of a successful injection attack
- [Permission Model (AI)](permission-model-ai.md) — the enforced access control that limits what an injected instruction can actually achieve
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the checkpoint that catches consequential actions an injection attempts to trigger

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-146 | Greshake, K. et al. — *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023) · [link](https://arxiv.org/abs/2302.12173) | Foundational paper on indirect prompt injection: adversarial instructions embedded in retrieved content, demonstrated against real systems. |
| SRC-147 | Perez, F. & Ribeiro, I. — *Ignore Previous Prompt: Attack Techniques For Language Models* (NeurIPS ML Safety Workshop, 2022) · [link](https://arxiv.org/abs/2211.09527) | Earliest documented direct prompt injection techniques (goal hijacking, prompt leaking). |
| SRC-148 | OWASP — *Top 10 for LLM Applications, LLM01: Prompt Injection* (2025 ed.) · [link](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Industry-standard ranking and definition; prompt injection as the top LLM application security risk. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Implementation surface: input/output filtering, action permissioning, and treating retrieved content as untrusted by default. |
| **Organizational** | The top-ranked AI security risk industry-wide — a concrete, board-legible reason to fund harness and guardrail investment. |
| **Client-facing** | Explains a real, named risk in AI products a general audience has likely heard of — a chatbot "hijacked" by a hidden instruction. |
| **LLM-native** | Fundamental to any agentic or tool-using deployment: the risk scales directly with how much external content the system reads. |

---

*Last updated: v1.0 · July 2026*
