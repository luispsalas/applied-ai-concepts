<!--meta
category: Observability & Governance
short: A structured assessment of what a system could do to people, completed before deployment — and, in the strongest implementations, published
aliases: [AIA, impact assessment, algorithmic impact assessments, AIA tool, impact level, pre-deployment assessment, impact assessment tool]
tags: [Regulatory, Ethics, Data Governance]
established: established
-->
# Algorithmic Impact Assessment

> **Term status — Established.** A mandatory instrument in at least one national government's policy framework, with an open published tool and a public register of completed assessments.

## One-line essence
A structured, pre-deployment assessment of the risks an automated decision system poses to the people it affects — scored to an impact level that determines what safeguards apply.

---

## Technical definition

An algorithmic impact assessment is a questionnaire-driven risk assessment completed **before** a system is deployed, producing a **graded impact level** that in turn determines proportionate obligations. It is modeled on established practice — environmental and data-protection impact assessments — applied to automated decision-making.

**Canada's is the reference implementation and is unusually concrete.** The Treasury Board's AIA is a **mandatory** tool supporting its Directive on Automated Decision-Making, composed of **65 risk questions and 41 mitigation questions**, scoring across the system's design, algorithm, decision type, impact and data. It was **developed in the open and released under an open license**, and — the property that distinguishes it from most governance instruments — **completed assessments are published and publicly searchable**.

**The mitigation questions are the structurally interesting half.** Score is not risk alone: declared mitigations reduce the assessed level. **That makes the assessment a commitment, not just a measurement** — an organization lowers its obligations by promising controls, which creates something later auditable against reality.

**Distinguish it from the EU's FRIA, which is narrower in every dimension.** A [fundamental rights impact assessment](fundamental-rights-impact-assessment.md) is EU AI Act Article 27, binds only certain deployer categories, and is not generally published. **AIA is the generic instrument**; FRIA is one jurisdiction's specific obligation. Conflating them overstates what EU law requires and understates what good practice looks like.

**The governance property that matters most is that it is pre-deployment and graded.** An assessment completed after launch documents a decision already made, and an ungraded one produces the same paperwork for a chatbot and a benefits eligibility system. **Both failures are common, and both hollow out the instrument while preserving its appearance.**

**Its known weakness is self-assessment.** The party with the strongest interest in a low impact level is the one completing the questionnaire. Publication is the main counterweight — an assessment nobody outside can read cannot be challenged by anyone whose interests it affects ([third-party audit](compliance-ai-systems.md)).

---

## Plain-language version

An algorithmic impact assessment is a structured set of questions you answer **before** deploying a system that makes decisions about people. The answers produce a score, the score produces an impact level, and the impact level determines how much oversight the system needs. A low-impact tool gets light obligations; a high-impact one gets heavy ones.

The idea is borrowed from environmental and privacy assessments, where it has worked for decades: force the thinking to happen while changing course is still cheap.

**Canada's version is the one worth knowing**, because it is real rather than aspirational. It is mandatory for federal automated decision systems, it has 65 risk questions and 41 mitigation questions, and the tool itself is published under an open license so anyone can use it. Most importantly: **completed assessments are published where the public can search them.**

That publication step is doing more work than it appears to. An assessment is filled in by the organization deploying the system — the party least motivated to conclude it is dangerous. **If nobody outside can read the result, nothing corrects that.** Publication is what makes the self-assessment challengeable.

There is a second clever feature. The questionnaire does not just measure risk; it lets you **lower your score by committing to mitigations.** So the finished assessment is a set of promises, not just a rating — and promises can be checked later.

Two ways this goes wrong, both common and both leaving the paperwork intact. Doing it **after** the decision to deploy, so it documents rather than informs. And doing it **ungraded**, so a scheduling assistant gets the same treatment as a benefits eligibility system — which trains everyone to treat it as a formality.

---

## AI literacy notes

1. **Pre-deployment is the whole point** — an assessment after launch documents rather than informs.
2. **Graded obligations keep it credible**; identical process for every system trains people to skip it.
3. **Mitigation questions make it a commitment**, and commitments are auditable later.
4. **Not the same as FRIA** — AIA is the generic instrument, FRIA is EU AI Act Article 27 for specific deployers.
5. **Self-assessment is the weakness**, and publication is the main counterweight.
6. **Canada's tool is open-licensed** and reusable by anyone, including private organizations.
7. **Completed Canadian assessments are publicly searchable** — rare among governance instruments.
8. **The lineage is environmental and privacy assessment**, which is why the structure feels familiar.

---

## Governance notes

**Core question:** Was this assessment completed while the deployment decision could still change — and can anyone outside the team that wrote it read it?

**Watch for:**
- An assessment completed after the build, or after go-live, documenting a settled decision
- One process applied at the same depth regardless of what the system decides about people
- Mitigations declared to lower a score with no follow-up confirming they were implemented
- Assessment treated as a compliance artifact filed once and never revisited ([model version and update](model-version-update.md))
- AIA and FRIA used interchangeably, overstating what EU law requires ([FRIA](fundamental-rights-impact-assessment.md))
- No route for an affected person to see or contest the assessment ([automated decision-making](automated-decision-making.md))
- Scope drawn around the model rather than the decision, so the human process around it goes unassessed
- Reassessment not triggered by a material change in purpose, data or model

**Practice:**
- **Complete it before the deployment decision, and record the date relative to that decision** — timing is the property that makes it real
- Grade obligations to impact; reserve depth for systems whose decisions carry legal or significant effects
- **Track declared mitigations to implementation**, since the score was reduced on their promise
- **Publish, or at minimum share with the affected constituency.** Self-assessment without external readership has no corrective
- Reassess on material change — new purpose, new data, new model version ([model version and update](model-version-update.md))
- Reuse the Canadian instrument rather than inventing a questionnaire: it is open-licensed, tested, and its scoring is documented
- Keep the assessment with the system's documentation so it can be produced on request ([audit trail](audit-trail-ai.md))

**Key accountability owner:** the business owner deploying the system, not the assessment's author — the questionnaire produces obligations, and someone with authority over the deployment has to accept them for the instrument to bind anything.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the instrument, unevidenced on its effectiveness — and the gap is worth stating.** Canada's AIA is documented in detail by the government operating it: the question counts, the scoring dimensions, the open license and the public register are all verifiable facts, quoted here from the source. **What no source in this registry establishes is whether impact assessments change outcomes.** The instrument is young in the AI context, its environmental and privacy predecessors have a mixed evaluation record, and this entry's claims about failure modes — post-hoc completion, ungraded application, unverified mitigations — are **reasoned from how the instrument works and from analogous practice, not measured.** The self-assessment weakness is structural and follows from who completes the form. Treat AIA as a well-designed process whose effect is not yet demonstrated.

---

## Related concepts

- [Fundamental Rights Impact Assessment (FRIA)](fundamental-rights-impact-assessment.md) — the EU's narrower, deployer-specific obligation
- [Automated Decision-Making](automated-decision-making.md) — the systems an AIA is designed for
- [Compliance (AI Systems)](compliance-ai-systems.md) — the regime an assessment discharges obligations within
- [AI Governance](ai-governance.md) — where assessment sits among organizational controls
- [Accountability (AI Systems)](accountability-ai-systems.md) — who accepts the obligations an assessment produces
- [Audit Trail (AI)](audit-trail-ai.md) — retaining the assessment as producible evidence
- [Model Version & Update](model-version-update.md) — the change that should trigger reassessment
- [Bias (AI Systems)](bias-ai-systems.md) — the harm class these assessments most often probe
- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — the management frame assessments sit inside
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the mitigations promised can actually be run

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-310 | Treasury Board of Canada Secretariat — *Algorithmic Impact Assessment tool* (Government of Canada) · [link](https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/algorithmic-impact-assessment.html) | The reference implementation and every concrete figure in this entry: a **mandatory** tool supporting the Directive on Automated Decision-Making, **65 risk questions and 41 mitigation questions**, scoring on design, algorithm, decision type, impact and data, **developed in the open under an open license**, with **completed assessments published and publicly searchable**. The mitigation half is what makes an assessment a commitment rather than a measurement. |
| SRC-211 | European Parliament / Council of the EU — *EU AI Act, Article 27: Fundamental rights impact assessment for high-risk AI systems* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The contrast that keeps the two instruments distinct: FRIA binds only specific deployer categories, is not generally published, and is one jurisdiction's obligation rather than the generic practice. ⚠️ Conflating AIA with FRIA overstates what EU law requires. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The Govern/Map/Measure/Manage frame that pre-deployment assessment implements — establishing impact assessment as a recognized control rather than one jurisdiction's invention. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The management-system context in which assessments are scheduled, retained and re-triggered rather than completed once. ⚠️ Paywalled standard. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The mitigations you declare reduce the assessed impact level — so they become commitments someone will check. Track them to implementation. |
| **Organizational** | Timing is what makes it real: completed before the deployment decision, or it documents rather than informs. Publication is what corrects self-assessment. |
| **Client-facing** | A concrete, borrowable instrument — Canada's is open-licensed — for showing that risk was assessed before launch rather than after. |
| **LLM-native** | Scope the assessment around the decision, not the model; the human process surrounding it is usually where the impact actually lands. |

---

*Last updated: v1.0 · September 2026*
