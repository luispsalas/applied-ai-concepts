# Systemic Risk (AI)

## One-line essence
Risk from an AI model's capabilities being significant enough to cause large-scale harm across society — a defined regulatory threshold that triggers extra obligations under frameworks like the EU AI Act.

---

## Technical definition

A category that is genuinely two things, and the entry is most useful when they are kept apart.

**The regulatory definition, which is precise.** Under Article 51 of the EU AI Act, a general-purpose AI model has systemic risk if it *"has high impact capabilities evaluated on the basis of appropriate technical tools and methodologies, including indicators and benchmarks,"* or if the Commission decides so — on its own or on a qualified alert from the scientific panel — against the criteria in Annex XIII. High-impact capability is **presumed** where *"the cumulative amount of computation used for its training measured in floating point operations is greater than 10^25."*

**Read that threshold carefully, because it is routinely misreported.** It is a *rebuttable presumption about capability*, not a measurement of harm and not a definition of risk. A provider can argue their model does not have high-impact capabilities despite exceeding it; the Commission can designate a model below it. And the figure is explicitly amendable — it is a regulatory proxy chosen because compute is observable and capability is not, which is a pragmatic choice, not a scientific one.

**What designation actually costs.** Article 55 obligations on providers of such models: perform model evaluation to standardized protocols *"including conducting and documenting adversarial testing"*; assess and mitigate systemic risks at Union level; track, document and report serious incidents to the AI Office without undue delay; and ensure adequate cybersecurity for the model and its physical infrastructure. Concrete, auditable duties — not a warning label.

**The analytical sense, which is broader and much less settled.** Borrowed from financial regulation, where systemic risk means harm propagating through a system rather than staying local. Applied to AI it names concerns like widespread dependence on a small number of models, correlated failure when many organizations run the same one, and society-scale effects on information, labor or infrastructure. **This sense has no agreed measurement**, and the vocabulary substantially outruns the evidence.

**Why the distinction matters practically.** The regulatory sense creates duties for a handful of *model providers*. The analytical sense describes an exposure that applies to *deployers* — and the AI Act does not address it. **An organization whose critical process depends on one model has a concentration risk that no systemic-risk designation covers**, because the regulation governs the model's capabilities, not your dependence on it.

---

## Plain-language version

Most AI risk is local: a system gives a wrong answer, someone is harmed, and it stays within that situation. Systemic risk is the concern that harm does not stay contained.

In EU law the term now has a specific meaning. The most capable general-purpose models get formally designated, and their providers take on extra duties — adversarial testing, risk assessment, incident reporting to a regulator, security requirements. The trigger is a training-compute threshold, chosen because compute can be observed and capability cannot. It is a proxy and a starting presumption, not a statement that a model above it is dangerous or one below it is safe.

Outside the legal sense, the phrase describes something the law does not cover and that affects far more organizations. When a great many businesses, hospitals and agencies build on the same handful of models, they share the same weaknesses. A flaw or an outage stops being one company's problem. That risk sits with everyone who *builds on* these systems — and nothing in the designation regime deals with it. It is your own dependency, and it is your own to manage.

---

## AI literacy notes

1. **Two senses, one phrase.** A precise legal category for a few model providers, and a loose analytical concern about propagation. They are used interchangeably and mean different things.
2. **10^25 FLOP is a presumption, not a verdict.** Rebuttable by the provider, overridable by the Commission, explicitly amendable — and about training compute, which is a stand-in for capability, which is itself a stand-in for harm.
3. **Compute was chosen because it is observable.** Capability is hard to measure and harm is harder. That is a defensible regulatory design and a poor scientific one, and the threshold should be read as the former.
4. **Designation attaches to providers, not to you.** If you deploy a designated model you are not thereby regulated under Art. 55 — your obligations come from what you build with it.
5. **The exposure that affects you is concentration, and no one regulates it.** Depending on one model for a critical process is an availability and correlated-failure risk that sits entirely with you.
6. **Correlated failure is the underrated part.** When many organizations run the same model, they share its blind spots. Independent-looking systems fail in the same direction at the same time.
7. **Treat unqualified claims skeptically in both directions.** The analytical sense has no agreed measurement, so both "AI poses systemic risk" and "systemic risk is hype" are usually reasoning past what has been shown.

---

## Governance notes

**Core question:** What in your organization would stop working if one model provider had a bad week — and is that dependency written down anywhere?

**Watch for:**
- The compute threshold quoted as a safety line, in either direction — "below it, therefore fine" and "above it, therefore dangerous" are both misreadings
- Systemic-risk designation treated as relevant to a deployer's obligations, when it governs providers
- **Single-provider dependency across multiple critical processes, never assessed as concentration risk** — the exposure most organizations actually carry
- No continuity plan for provider outage, deprecation, policy change or price change; the failure modes here are commercial as often as technical
- Provider incident reporting to a regulator assumed to reach you — Art. 55(c) runs to the AI Office, not to customers
- The term used rhetorically in either direction with no measurement behind it

**Practice:**
- Map model dependency the way you map any critical supplier: which processes, which provider, what happens if it stops
- Keep a documented fallback for critical paths — a second provider, a degraded mode, or a manual process that has been exercised
- Track designation status of models you rely on: it signals both provider maturity and a heavier regulatory surface that may reach your contracts
- Distinguish the two senses explicitly in internal writing, since conflating them makes both harder to act on
- Where you are a *deployer*, focus on what you actually control: concentration, continuity, and [operational readiness](operational-readiness-ai.md) — not the model's capability designation
- Treat [incident](ai-incident-reporting.md) obligations as a separate live question; yours are not discharged by the provider's

**Key accountability owner:** for a model provider, the party carrying Art. 55 duties. **For everyone else — which is almost everyone — this belongs with whoever owns third-party and continuity risk**, not with the AI team, because the exposure is a supplier-dependency question wearing AI vocabulary.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Split, and sharply.**

**High on the regulatory sense:** the classification criteria, the compute threshold, and the Art. 55 obligations are binding law with quotable clause text, verified against the article.

**Low on the analytical sense.** There is no agreed method for measuring systemic risk from AI, no established threshold at which concentration becomes dangerous, and the compute proxy is acknowledged even by its drafters as administratively convenient rather than principled. The concentration and correlated-failure arguments are reasoning by analogy from financial and supply-chain risk, not findings about AI. **Both alarm and dismissal are common and both usually outrun the evidence** — this entry deliberately puts its practical weight on the dependency question, which is measurable and actionable today, rather than on the society-scale claims, which are not.

---

## Related concepts

- [Compliance (AI Systems)](compliance-ai-systems.md) — where Art. 51/55 obligations are demonstrated
- [AI Governance](ai-governance.md) — the structures that decide who owns dependency risk
- [AI Incident (Reporting)](ai-incident-reporting.md) — Art. 55(c) reporting, and why yours is separate
- [Operational Readiness (AI)](operational-readiness-ai.md) — continuity and fallback for a critical dependency
- [Red Teaming](red-teaming.md) — the adversarial testing Art. 55(a) requires be conducted and documented
- [Evaluation (AI Systems)](evaluation.md) — the "indicators and benchmarks" the classification leans on, with the proxy limits that implies
- [Power Seeking](power-seeking.md) — a capability concern in the same register, with the same evidence caveats
- [Alignment (AI Systems)](alignment-ai-systems.md) — where much of the underlying capability concern originates
- [Scalability (AI Systems)](scalability-ai-systems.md) — concentration is what scale looks like across an economy rather than one system
- [Local LLMs](local-llms.md) — one structural answer to provider concentration, with its own costs
- [Model/Data Drift](model-data-drift.md) — a provider changing a model underneath you is the everyday version of dependency risk
- Frontier AI (Frontier Model) — the informal category the regulatory one formalizes
- Model Version & Update — the mechanism by which provider dependency becomes a live operational issue

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-200 | European Parliament / Council of the EU — *EU Artificial Intelligence Act, Articles 51 and 55: General-purpose AI models with systemic risk* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The classification criteria, the 10^25 FLOP presumption in its exact wording, and the four Art. 55 provider obligations — evaluation with documented adversarial testing, Union-level risk mitigation, incident reporting to the AI Office, and cybersecurity of model and infrastructure. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The surrounding risk-tier architecture that gives the GPAI provisions their context, and the deployer obligations that are *not* discharged by a provider's designation. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | A non-EU lifecycle framing of large-scale and third-party AI risk, and the govern function where dependency decisions belong. |
| SRC-112 | OECD — *OECD AI Principles Overview* (2024) · [link](https://oecd.ai/en/ai-principles) | The intergovernmental framing of society-scale AI risk, endorsed well beyond the EU — useful for showing the concern is not a single jurisdiction's invention. |
| SRC-164 | McGregor, S. (XPRIZE Foundation / Partnership on AI / Syntiant) — *Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database* (AAAI, 2021) · [link](https://ojs.aaai.org/index.php/AAAI/article/view/17817) | The empirical alternative to speculation: what large-scale AI harm has actually looked like when cataloged, rather than as projected. |
| SRC-115 | Stanford HAI — *AI Index Report* (2026) · [link](https://hai.stanford.edu/ai-index) | Concentration data on model development and deployment. ⚠️ Annual publication — verify the edition permalink and re-check figures before citing any specific number. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The actionable version is dependency mapping and a tested fallback for critical paths. Provider designation status is worth tracking; it is not your obligation. |
| **Organizational** | Almost no organization is regulated by Art. 55, and almost every organization carries concentration risk. That belongs with third-party and continuity risk, not with the AI team. |
| **Client-facing** | Explains why the most capable models carry extra legal duties, and separately why depending on a single provider for a critical process is a business-continuity question. |
| **LLM-native** | 10^25 FLOP is a rebuttable presumption about capability, chosen because compute is observable — not a harm measurement and not a safety line in either direction. |

---

*Last updated: v1.0 · August 2026*
