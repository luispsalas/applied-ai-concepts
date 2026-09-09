<!--meta
category: Observability & Governance
short: How a high-risk AI system is certified before it goes on the EU market — and the fact that for most of them, the provider certifies itself
aliases: [conformity assessment, notified body, CE marking, internal control, declaration of conformity, Annex VI, Annex VII, who certifies AI, third-party assessment]
tags: [Regulatory, Data Governance, Evaluation]
established: established
-->
# Conformity Assessment (AI Systems)

> **Term status — Established.** A defined procedure in EU product law and in the AI Act, with a named institutional apparatus behind it.

## One-line essence
The procedure by which a high-risk AI system is shown to meet its legal requirements before being placed on the EU market — carried out either by the provider itself or, in defined cases, with a notified body.

---

## Technical definition

Conformity assessment is EU product-law machinery applied to AI: before a high-risk system is placed on the market, the provider must demonstrate it satisfies the Act's requirements, then draw up a declaration of conformity and affix **CE marking**. A **notified body** is a conformity assessment organization designated by a member state to perform that assessment independently.

**The fact that matters most, and that most summaries omit: for the majority of high-risk systems, no external body is involved.** Article 43 gives providers of Annex III high-risk systems a choice between **internal control** (Annex VI) and **assessment involving a notified body** (Annex VII) — and the third-party route becomes mandatory only in specific circumstances: where harmonised standards do not exist, where the provider did not apply them or applied them only in part, or where a standard was published with a restriction.

**So "high-risk" does not mean "externally audited."** A provider that applies the harmonised standards may self-assess, declare conformity, and CE-mark the system. **The CE mark on an AI system is, in the common case, the provider's own declaration** — which is exactly how the mark works across EU product law, and exactly what non-specialist readers assume it is not.

**That places enormous weight on the harmonised standards**, since applying them is what unlocks self-assessment. Where they are absent or incomplete, the third-party route engages by default — making standards availability, not risk level, the practical determinant of who checks.

**Notified-body capacity is the structural constraint** behind that design. Independent assessment of every high-risk AI system would require a body of assessors that does not exist at scale, and the self-assessment route is the pressure valve.

**Two boundaries worth holding.** Conformity assessment is about the **provider** placing a system on the market; it is not the deployer-side obligation ([FRIA](fundamental-rights-impact-assessment.md), [algorithmic impact assessment](algorithmic-impact-assessment.md)). And it certifies conformity **at a point in time** — a substantially modified system may require reassessment, and modification can also make the modifier the provider ([supply chain risk](supply-chain-risk-ai.md)).

---

## Plain-language version

Before certain AI systems can be sold in the EU, someone has to certify they meet the legal requirements. That process is conformity assessment, and it ends with a **CE mark** — the same mark you see on a kettle or a toy.

Here is the part that surprises almost everyone, and it is worth being precise about.

**A CE mark usually does not mean an independent body checked the product.** For most high-risk AI systems the provider gets a choice: assess it themselves under "internal control", or bring in a **notified body** — an organization a member state has designated to do independent assessment. The independent route becomes compulsory only in particular situations: mainly when the relevant technical standards do not exist yet, or the provider did not fully apply them.

So a company can build a high-risk AI system, apply the standards, check its own work, sign a declaration, apply the CE mark, and sell it. **That is the law working as designed, not a loophole** — it is how CE marking has always worked across European product law. But "high-risk" and "independently certified" are not the same thing, and people routinely assume they are.

This puts a lot of weight on the technical standards, because applying them is what earns the right to self-assess. Where standards are missing, the independent route kicks in automatically. **In practice, what decides who checks your system is not how dangerous it is — it is whether the standards exist yet.**

There is a practical reason behind the design: there are nowhere near enough accredited assessors to independently examine every high-risk AI system, and self-assessment is the pressure valve.

Two limits to remember. This is about the **provider** putting a system on the market — separate from the duties that fall on the organization *using* it. And it certifies the system as it was at that moment: change it substantially and the question reopens.

---

## AI literacy notes

1. **CE marking on AI is usually a self-declaration**, not an independent certification.
2. **Article 43 gives a choice** between internal control and notified-body assessment for Annex III systems.
3. **The third-party route is mandatory only in defined cases** — chiefly missing or unapplied harmonised standards.
4. **Standards availability, not risk level, often determines who assesses.**
5. **Notified-body capacity is the structural constraint** the design accommodates.
6. **This is a provider obligation**, distinct from deployer-side assessments.
7. **Conformity is certified at a point in time**; substantial modification reopens it.
8. **Modifying a system can make you its provider**, and therefore responsible for its assessment ([supply chain risk](supply-chain-risk-ai.md)).

---

## Governance notes

**Core question:** For each high-risk system we provide or procure, which assessment route was used — and does anyone here know the answer?

**Watch for:**
- CE marking read as evidence of independent assessment, in procurement or in assurance to customers
- A supplier's conformity claim accepted without asking which route was taken
- Self-assessment chosen on standards that were applied only partially, without the consequence examined
- Substantial modification of a CE-marked system with no reassessment considered ([model version and update](model-version-update.md))
- A deployer assuming the provider's conformity assessment discharges deployer obligations ([FRIA](fundamental-rights-impact-assessment.md))
- Technical documentation assembled for assessment and then not maintained as the system changes
- Fine-tuning or rebranding a third-party system with no thought to provider status ([fine-tuning](fine-tuning.md))
- Conformity treated as the end of a process rather than a state to be maintained

**Practice:**
- **Ask suppliers which route was used and record the answer** — internal control or notified body, and which standards were applied. This one question separates a real assurance claim from an assumed one
- Keep technical documentation current rather than assembling it once for assessment ([audit trail](audit-trail-ai.md))
- **Assess your own provider status before modifying a CE-marked system**, since modification can transfer the obligation to you
- Track which harmonised standards exist for your system type; their availability determines the route open to you
- Separate provider-side conformity from deployer-side assessment in your compliance mapping ([compliance](compliance-ai-systems.md))
- Treat reassessment as triggered by substantial modification, and define in advance what your organization counts as substantial
- **Do not present a CE mark to customers as third-party certification** unless a notified body was in fact involved

**Key accountability owner:** the provider placing the system on the market — and, where an organization rebrands or substantially modifies someone else's system, that organization, which may not realize the obligation has moved to it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, which is quoted from the regulation; lower on how it will operate in practice.** Article 43's routes, the conditions triggering notified-body involvement, and the internal-control option are legal text and are stated here from the source. **What is genuinely uncertain is everything downstream of that**: which harmonised standards will exist and when, how much notified-body capacity will be available, and how "substantial modification" will be interpreted — all of which are being settled through standardization work and supervisory practice rather than by the Act. **The capacity argument in this entry is reasoned rather than sourced**: the Act does not say self-assessment exists because assessors are scarce, and this entry presents that as an explanation of the design, not as a finding. **Verify current guidance before relying on any route determination for a specific system.**

---

## Related concepts

- [Compliance (AI Systems)](compliance-ai-systems.md) — the wider regime this discharges one obligation within
- [Fundamental Rights Impact Assessment (FRIA)](fundamental-rights-impact-assessment.md) — the deployer-side counterpart, frequently confused with this
- [Algorithmic Impact Assessment](algorithmic-impact-assessment.md) — the generic pre-deployment instrument
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — how modifying a system transfers provider obligations
- [Model Card / System Card](model-card-system-card.md) — the technical documentation assessment rests on
- [Audit Trail (AI)](audit-trail-ai.md) — keeping that documentation producible
- [Model Version & Update](model-version-update.md) — the change that can reopen conformity
- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — the quality-management system Annex VII assesses
- [Evaluation (AI Systems)](evaluation.md) — the evidence a conformity claim rests on
- [Accountability (AI Systems)](accountability-ai-systems.md) — who signs the declaration

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-312 | European Parliament / Council of the EU — *EU AI Act, Article 43: Conformity assessment* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The entry's central fact, read verbatim from EUR-Lex: for Annex III point 1 high-risk systems where the provider has applied harmonised standards, the provider **shall opt for one of** internal control (Annex VI) **or** assessment involving a notified body (Annex VII) — with the third-party route required where harmonised standards do not exist, were not applied, were applied only in part, or were published with a restriction. This is what establishes that **high-risk does not mean externally audited**. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The surrounding regime — risk tiers, provider obligations, CE marking and the declaration of conformity — that gives the assessment its consequences. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The management-system standard relevant to the Annex VII route, which assesses the quality management system alongside the technical documentation. ⚠️ Paywalled standard. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The non-EU comparison point: a voluntary framework with no conformity mechanism at all, which is what makes the EU's mandatory, marked, declared route distinctive rather than typical. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Keep technical documentation current rather than assembling it once. Which harmonised standards you applied decides which route is open to you. |
| **Organizational** | Ask every supplier which route was used. A CE mark is usually the provider's own declaration, and presenting it as third-party certification is a claim you cannot support. |
| **Client-facing** | Explains precisely what a CE mark on an AI system does and does not mean, without implying anyone acted improperly. |
| **LLM-native** | Substantially modifying or rebranding a CE-marked system can make you its provider — and therefore responsible for its conformity. |

---

*Last updated: v1.0 · September 2026*
