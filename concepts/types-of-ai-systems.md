<!--meta
category: Foundations
short: A taxonomy of AI by capability and autonomy — from narrow task tools to general-purpose models — that determines governance, risk, and oversight
aliases: [AI taxonomy, kinds of AI, narrow vs general AI, AI classification, what counts as AI]
tags: [Architecture, Regulatory]
-->
# Types of AI Systems

## One-line essence
A taxonomy of AI by capability and autonomy — from narrow task tools to general-purpose models — that determines appropriate governance, risk profiles, and oversight requirements.

---

## Technical definition

Classification of AI systems along the axes that determine governance treatment: capability breadth (narrow task-specific systems vs general-purpose models), autonomy (predictive/classification systems → generative models → tool-using agents → multi-agent systems), and risk (the EU AI Act's tiers: prohibited, high-risk, limited-risk, minimal-risk, plus general-purpose AI obligations).

Within this taxonomy, **general-purpose AI (GPAI)** is a distinct regulatory category: the EU AI Act's term for a model trained on broad data at scale, displaying significant generality, and capable of performing a wide range of distinct tasks (Art. 3(63)), with obligations — technical documentation, training-data summaries, and systemic-risk assessment for the most capable models — that scale with the model's capability rather than attaching to a specific use case, the way the Act's other risk tiers do.

ISO/IEC 22989 provides the standardized vocabulary — an AI system is "an engineered system that generates outputs such as content, forecasts, recommendations or decisions for a given set of human-defined objectives" (3.1.4). The OECD definition — a machine-based system inferring outputs from inputs with varying levels of autonomy and adaptiveness — anchors intergovernmental usage, and the OECD Classification Framework operationalizes typing along five dimensions: People & Planet, Economic Context, Data & Input, AI Model, Task & Output. The workflow-vs-agent distinction captures the autonomy axis as used in current engineering practice.

---

## Plain-language version

Not all AI is the same kind of thing. A spam filter, a chatbot, and an agent that books your travel differ in what they can do on their own — and in how much can go wrong. Knowing which type you're dealing with tells you how much oversight it needs.

---

## AI literacy notes

1. **Type determines governance.** A classifier needs different controls than an autonomous agent. Autonomy is the key axis for oversight — the more a system can act without a human, the more consequential its failure modes.
2. **The generic word "AI" flattens the distinctions that matter.** Insist on specificity before assessing risk: what kind of system, with what autonomy, in what use?
3. **Taxonomies are unstable.** Agent definitions are still contested, and regulatory tiers classify by risk of use, not by architecture — the same architecture can land in different tiers depending on deployment.
4. **GPAI obligations attach to the model, not the use.** Unlike the Act's other risk tiers, which classify by what a system is used for, general-purpose AI obligations (documentation, training-data summaries, systemic-risk assessment for the most capable models) attach to the model itself — because one GPAI model gets embedded in many different downstream use cases, each with its own risk profile.

---

## Governance notes

**Core question:** Has every deployed system been classified — and does its oversight match its type?

**Watch for:**
- Governance designed for chatbots applied unchanged to autonomous agents
- "AI" used generically in policies — what can't be classified can't be governed
- Type drift: a system gaining tools or autonomy without being reclassified

**Practice:**
- Classify every system on capability/autonomy/risk at intake
- Trigger reclassification on any capability change

**Key accountability owner:** the AI governance function.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The definitional and classification anchors are standardized (ISO/IEC 22989 vocabulary, OECD definition and classification framework, EU AI Act risk tiers); capability/autonomy taxonomies in engineering practice remain contested and fast-moving.

---

## Related concepts

- [AI Agent](ai-agent.md) — the high-autonomy end of the type spectrum, where oversight requirements concentrate
- [AI Governance](ai-governance.md) — classification is the intake step that determines which governance regime applies
- [AI Use Case](ai-use-case.md) — regulatory tiers classify by use-risk, so type and use case are assessed together
- [Harness Paradigm](harness-paradigm.md) — the control layer must match the system type: more autonomy demands more harness

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-133 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 22989:2022 — AI Concepts and Terminology* (2022) · [link](https://www.iso.org/standard/74296.html) | Standardized vocabulary; canonical "AI system" definition (3.1.4), verified verbatim. |
| SRC-112 | OECD — *AI Principles Overview* (2024) · [link](https://oecd.ai/en/ai-principles) | Intergovernmental definition of an AI system (autonomy and adaptiveness axes). |
| SRC-134 | OECD — *Framework for the Classification of AI Systems* (2022) · [link](https://www.oecd.org/en/publications/oecd-framework-for-the-classification-of-ai-systems_cb6d9eca-en.html) | Five-dimension operational classification tool. |
| SRC-129 | European Parliament — *EU Artificial Intelligence Act* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Risk-tier taxonomy (prohibited / high / limited / minimal) plus general-purpose AI category. |
| SRC-104 | Anthropic — *Building Effective AI Agents* (2024) · [link](https://www.anthropic.com/engineering/building-effective-agents) | Workflow vs agent distinction; the autonomy spectrum in engineering practice. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Architecture choices (workflow vs agent, narrow vs general-purpose) carry governance consequences — type is a design decision. |
| **Organizational** | Classification at intake is the practical first step of AI governance: what can't be classified can't be governed. |
| **Client-facing** | Answers "what kind of AI is this?" — setting accurate expectations about autonomy and oversight. |
| **LLM-native** | General-purpose models blur old category lines; typing by autonomy and use-risk replaces typing by architecture. |

---

*Last updated: v1.1 · July 2026*
