# Fundamental Rights Impact Assessment (FRIA)

## One-line essence
A required pre-deployment analysis of how a high-risk AI system could affect people's fundamental rights — fairness, privacy, non-discrimination — before it goes live, not after.

---

## Technical definition

An assessment obligation created by Article 27 of the EU AI Act, performed by the **deployer** rather than the provider, and focused on the *use* of a system rather than its construction.

**Who it binds — and this is the most misstated part of the whole provision.** It applies to deployers *"that are bodies governed by public law, or are private entities providing public services,"* plus specific deployers under Annex III points 5(b) and (c). **It is not a general duty on every high-risk deployer**, and practitioner writing routinely says otherwise. Check the deployer category before asserting the obligation exists.

**When.** Prior to deploying, applying to first use. A previous assessment can be reused for similar cases, and must be updated when any assessed element changes.

**What it must contain**, per Art. 27:

1. The deployer's processes for using the system in line with its intended purpose
2. Timeframe and frequency of intended use
3. Categories of persons and groups likely to be affected
4. Specific risks of harm to those identified populations
5. Implementation of human oversight measures
6. Measures if risks materialize — including internal governance and **complaint mechanisms**

Results are notified to the market surveillance authority on a template developed by the AI Office.

**The relationship to a DPIA is complementary, not duplicative.** Art. 27(4): where obligations are already met through a GDPR Art. 35 data protection impact assessment, the FRIA *complements* that assessment and may cross-reference it. **The two are not interchangeable** — a DPIA is scoped to personal data processing; a FRIA covers fundamental rights more broadly, including effects that involve no personal data at all.

**What makes it structurally different from a technical assessment.** The unit is not the model but **the deployment in its context**: who is affected, how often, with what recourse. Two organizations running the identical system owe different assessments, because the affected populations and the consequences differ. That is also why it cannot be procured from the provider — the provider does not know your context, and the obligation is deliberately placed with whoever creates the exposure.

---

## Plain-language version

Before certain organizations switch on a high-risk AI system, EU law requires them to work out — and write down — how it could affect people's basic rights.

Not whether the model works. Whether *using it here, on these people, this often* could cause harm: unfair treatment, discrimination, privacy intrusion, or a decision someone has no way to contest.

The obligation falls on the organization *deploying* the system, not the one that built it, and that placement is deliberate. The builder does not know who your users are, how often you will run it, or what happens to someone the system gets wrong. Only you do.

Two things are commonly misunderstood. It does not apply to everyone using high-risk AI — mainly to public bodies and private organizations providing public services, plus a few specific categories. And it is not the same as the data protection assessment many organizations already do; that one is about personal data, this one is about rights more broadly, and where they overlap you can cross-reference rather than repeat yourself.

The part that gives it teeth is unglamorous: you have to say what happens when something goes wrong, including how a person complains.

---

## AI literacy notes

1. **It does not apply to all high-risk deployers.** Public bodies, private entities providing public services, and specific Annex III categories. The over-broad reading is the most common error about this provision.
2. **It is a deployer duty, and cannot be bought from the provider.** The assessment is about your context — your users, your frequency, your consequences — which the provider does not have.
3. **The unit of analysis is the deployment, not the model.** Two organizations running the same system owe different assessments.
4. **Complaint mechanisms are an enumerated element**, not an afterthought. If the people affected have no route to object, the assessment is incomplete on its face.
5. **A DPIA does not discharge it.** They overlap and cross-reference; a DPIA is scoped to personal data, and fundamental rights extend beyond it.
6. **It is prospective and reusable.** Before first use, updated when things change — designed as a living document, not a launch artifact filed once.
7. **Its value survives the jurisdiction.** Even where the legal duty does not apply, the six questions are a good pre-deployment structure — who is affected, how often, what could go wrong for them, who oversees it, what happens when it does, how do they complain.

---

## Governance notes

**Core question:** Who is affected by this deployment, what happens to them when it goes wrong, and how would they tell you?

**Watch for:**
- The obligation asserted or dismissed without checking the deployer category — wrong in both directions is common
- The provider's conformity documentation treated as covering it; those are different duties on different parties
- A DPIA presented as a FRIA, which misses rights effects that involve no personal data
- Affected groups described generically ("users") rather than as identified categories with specific risks — the enumeration is the point
- No complaint mechanism, or one that exists but is unreachable by the people the system actually affects
- Filed once and never updated, despite the explicit duty to update when assessed elements change
- Human oversight described as available rather than implemented, which Art. 27 asks about specifically ([agency](agency-ai-systems.md), [HITL](human-in-the-loop.md))

**Practice:**
- Establish the deployer category first; it determines whether this is a legal obligation or a voluntary good practice, and both are legitimate outcomes
- Enumerate affected populations concretely, including people who are subject to the system without being its users — the group most often omitted
- Cross-reference an existing DPIA rather than duplicating it, and state clearly what the FRIA adds
- Make the complaint mechanism real and reachable, then test that a person outside the organization can actually use it
- Treat it as versioned and re-triggered by change: new population, higher frequency, changed purpose, changed model
- Where the duty does not apply, **use the structure anyway** for consequential deployments — it is a better pre-deployment brief than most internal templates
- Track the AI Office template as a live dependency

**Key accountability owner:** the deployer's system owner, jointly with whoever owns fundamental-rights or compliance obligations — and, because the assessment concerns people outside the organization, it should be reviewable by someone who does not own the system's success.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the obligation, lower on practice.** Art. 27 is binding text with an enumerated element list, verified against the article. **What is not settled is how it is actually done**: the AI Office template is a live dependency, no body of completed assessments exists to learn from, there is no established methodology for assessing fundamental-rights impact of an AI deployment as distinct from a data protection impact, and enforcement practice is untested. The recommendations here derive from the article's own structure and from mature DPIA practice, not from established FRIA practice, which does not yet exist.

---

## Related concepts

- [Compliance (AI Systems)](compliance-ai-systems.md) — where the obligation is demonstrated
- [AI Use Case](ai-use-case.md) — the deployment-in-context unit this assesses
- [Bias (AI Systems)](bias-ai-systems.md) — the discrimination risks the assessment must identify
- [Privacy (AI Systems)](privacy-ai-systems.md) — the DPIA's territory, which this complements rather than repeats
- [Agency (AI Systems)](agency-ai-systems.md) — the human oversight measures Art. 27 asks to see implemented
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — oversight as an enumerated assessment element
- [Accountability (AI Systems)](accountability-ai-systems.md) — complaint mechanisms as the recourse side of answerability
- [AI Governance](ai-governance.md) — where the assessment is commissioned and reviewed
- [Model Card / System Card](model-card-system-card.md) — provider-side documentation, a different duty on a different party
- [Systemic Risk (AI)](systemic-risk-ai.md) — the provider-side obligations at the other end of the Act
- [Operational Readiness (AI)](operational-readiness-ai.md) — a completed assessment is part of what "ready" means
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the deployer's duty that placement of this obligation reflects

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-211 | European Parliament / Council of the EU — *EU AI Act, Article 27: Fundamental rights impact assessment for high-risk AI systems* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The obligation, the deployer categories it actually binds, the six enumerated elements, the notification duty, and Art. 27(4) on complementing rather than duplicating a GDPR Art. 35 DPIA. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The high-risk classification and Annex III categories that determine whether the duty is reachable at all. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The Art. 35 DPIA this cross-references, and the mature impact-assessment practice the FRIA borrows structure from. |
| SRC-109 | Green, B. — *The Flaws of Policies Requiring Human Oversight of Government Algorithms* (Computer Law & Security Review 45, 2022) · [link](https://doi.org/10.1016/j.clsr.2022.105681) | Why an assessment that records oversight as *available* rather than effective fails — directly relevant to the human-oversight element, and to public-sector deployment specifically. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Method for identifying which groups are affected and how — the enumeration the assessment requires. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | A non-EU structure for the same pre-deployment questions, useful where the legal duty does not apply. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Human oversight must be described as *implemented*, not available — the article asks about implementation, and "a person can review" is not an answer. |
| **Organizational** | Check the deployer category before asserting or dismissing the duty; both errors are common. The assessment cannot be procured from the provider, because it is about your context. |
| **Client-facing** | Explains why a high-risk deployment carries a documented pre-launch assessment about affected people and their recourse, separate from any data protection review. |
| **LLM-native** | The unit is the deployment, not the model — same system, different organizations, different assessments. And complaint mechanisms are an enumerated element, not a nicety. |

---

*Last updated: v1.0 · August 2026*
