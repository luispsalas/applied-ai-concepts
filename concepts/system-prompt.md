# System Prompt

## One-line essence
The behind-the-scenes instructions that set up how an AI behaves before you start talking to it — like a job description the AI reads first. Changing it changes the AI's behavior.

---

## Technical definition

A system prompt is the standing set of instructions supplied to a language model before any user input — establishing role, task framing, tone, constraints, and available context for the session. It is distinct from the user prompt (the turn-by-turn input) and is authored using prompt-engineering technique (SRC-013); in context terms it is the baseline layer of engineered context the model always receives (SRC-069). Architecturally it is a harness component — one of the "guides" that steer behavior before the model acts (SRC-018) — not a property of the model: the same model behaves differently under different system prompts. It is also a soft control, not a hard boundary: a system prompt shapes behavior probabilistically and can be undermined by adversarial user input (see Prompt Injection), which is why it complements rather than replaces enforced controls like the permission model and guardrails.

---

## Plain-language version

Before you type anything, the AI has usually already been given a set of instructions you never see — its system prompt. Think of it as the job description and house rules handed to a new hire before their first shift: "You are a support assistant for this company, be concise, never discuss pricing, here is what you have access to." Change that briefing and the same underlying AI behaves like a different assistant. It is powerful — it sets the whole tone and scope — but it is guidance, not a lock: a clever or malicious user can sometimes talk the model out of following it, which is why it is paired with harder safeguards.

---

## AI literacy notes

1. **A lot of "the AI's personality" actually lives in the system prompt.** Behavior you might attribute to the model is often the system prompt talking — two products on the same model can feel completely different because of it.
2. **It is a control surface, and therefore a governance artifact.** Because changing it changes behavior, it should be versioned, owned, and change-reviewed like any production configuration (see [Harness Paradigm](harness-paradigm.md)), not edited casually.
3. **It is a soft control, not a boundary.** A system prompt steers; it does not enforce. Anything that must not happen (data access, irreversible actions) needs a hard control — a permission model or guardrail — because system-prompt instructions can be overridden by prompt injection.
4. **It counts as context.** Everything in the system prompt consumes the context budget and competes with user input and retrieved content, so longer is not always better.

---

## Governance notes

**Core question:** Is the system prompt treated as a governed, versioned artifact — and does anything critical depend on it that shouldn't?

**Watch for:**
- System prompts edited in production without versioning or review
- Security or policy rules placed only in the system prompt (a soft control) instead of enforced by permission model/guardrails
- Prompt sprawl that quietly consumes the context budget

**Practice:**
- Version and change-review the system prompt like code
- Put must-not-happen rules in hard controls, not just the prompt
- Test the system prompt against prompt-injection attempts

**Key accountability owner:** the harness/system owner.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established practice.** The concept and its use are stable and universal across deployed LLM systems; terminology varies by vendor ("system prompt", "system message", "developer message") but refers to the same layer.

---

## Related concepts

- [Prompt Engineering](prompt-engineering.md) — the discipline used to author an effective system prompt
- [Context Engineering](context-engineering.md) — the system prompt is the baseline layer of a model's engineered context
- [Harness Paradigm](harness-paradigm.md) — the system prompt is a harness-layer control (a "guide"), owned and versioned at the system level
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the hard controls that back up a system prompt, since the prompt only steers
- Prompt Injection — the adversarial input that can override system-prompt instructions
- Permission Model (AI) — the enforced access control that must carry any must-not-happen rule, not the system prompt

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-013 | Anthropic — *Prompt engineering overview* (2024) · [link](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | The system prompt as role/instruction layer and its authoring technique. |
| SRC-069 | Anthropic — *Effective Context Engineering for AI Agents* (2025) · [link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | The system prompt as the baseline layer of engineered context the model always receives. |
| SRC-018 | Böckeler, B. — *Harness engineering for coding agent users* (martinfowler.com, 2026) · [link](https://martinfowler.com/articles/harness-engineering.html) | The system prompt as a harness-layer "guide" (feedforward control), owned and versioned at the system layer, not the model. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | A versioned configuration artifact: authored with prompt-engineering technique, owned, and change-reviewed like code. |
| **Organizational** | Where much of a product's behavior and policy actually lives — govern it, and don't rely on it for hard rules. |
| **Client-facing** | Explains why the same underlying model behaves as a tailored assistant — and why that tailoring is guidance, not a guarantee. |
| **LLM-native** | The baseline context layer; a soft steering control that pairs with hard controls (permissions, guardrails). |

---

*Last updated: v1.0 · July 2026*
