<!--meta
category: Observability & Governance
short: Assurance by someone with no stake in the answer — whose value is set almost entirely by what access they were granted, not by their independence
aliases: [external audit, independent audit, algorithmic audit, AI audit, external assurance, auditor access, black-box audit, white-box audit, who audits the auditors]
tags: [Regulatory, Evaluation, Data Governance]
established: established
-->
# Third-Party Audit

> **Term status — Established.** A standard governance mechanism across finance, safety-critical engineering and data protection, applied to AI systems in a peer-reviewed literature with its own field scan and its own critiques. Independent of any vendor.

## One-line essence
Examination of an AI system by a party with no stake in the result — a mechanism whose value depends far more on the access the auditor was granted than on their independence.

---

## Technical definition

A third-party audit is an assessment conducted by an external party that is independent of both the developer and the deployer. The word does a lot of work: **independence is a *precondition* for an audit meaning anything, and on its own it establishes nothing.**

**Access is the variable that decides what an audit can conclude.** Casper et al. distinguish three levels, and the distinction is the single most useful thing in this entry:

| Access | What the auditor has | What they can establish |
|---|---|---|
| **Black-box** | Query the system, observe outputs | Behavior on the inputs they thought to try |
| **White-box** | Weights, activations, gradients | Stronger attacks, interpretation, fine-tuning experiments |
| **Outside-the-box** | Methodology, code, documentation, data, deployment details, internal evaluation findings | Scrutiny of the *development process*, and targeted evaluations designed from it |

Their conclusion is the operative one: **different forms of access lead to very different levels of evaluation**, so *transparency about what access an auditor had* is itself necessary for an audit's findings to be interpretable. **An audit report without an access statement is not assessable** — a clean result from black-box access and a clean result from white-box access are not the same claim.

**The failure this produces in practice: an auditor who cannot see weights, data or logs is auditing documentation.** That is a real activity with real value — it catches internal inconsistency, missing process, and claims the organization cannot substantiate — but it is an audit of what the organization *says*, and it should be reported as such rather than as an audit of the system.

**Third-party audit is not the same as conformity assessment, and the EU AI Act makes the distinction consequential.** Under the Act, providers of Annex III high-risk systems can in most cases choose **internal control** over third-party assessment, with the external route mandatory only where harmonised standards are missing or unapplied. **So "high-risk under the AI Act" does not imply "externally audited"** ([conformity assessment](conformity-assessment-ai.md)) — a point worth holding onto whenever a CE mark is offered as external assurance.

**The ecosystem has its own accountability gap.** Costanza-Chock, Raji and Buolamwini's field scan of the algorithmic auditing ecosystem finds it lacking the things that make audit meaningful in mature professions: **shared standards, methodological transparency, professional accreditation, and any mechanism of consequence when an audit is wrong or captured.** Auditors are typically paid by the audited, may have no right to publish, and in many cases the target chooses both the auditor and the scope — the structural conditions that produced audit failures in other industries, reproduced without their remedies.

**And a right to audit is not the same as a right to say what you found.** Publication rights, scope control, and the ability to report adverse findings to a regulator rather than only to the client are the terms that determine whether an audit is assurance or reputation management ([accountability](accountability-ai-systems.md)).

---

## Plain-language version

A third-party audit is when someone from outside — not the builder, not the buyer — examines a system and reports what they find. It is the mechanism nearly every proposal for AI accountability quietly depends on.

**The thing most people get wrong is thinking the important word is "independent."** It is not. Independence stops the auditor having a reason to lie. It does not give them anything to look at.

The variable that actually determines whether an audit means anything is **access**. There are roughly three levels:

- They can use the system and see what it does — like assessing a car by driving it.
- They can look inside at the model itself — opening the bonnet.
- They can see how it was built: the data, the code, the internal test results, the decisions along the way — the factory and the design notes.

These produce completely different kinds of conclusion. And here is the consequence: **"we passed an independent audit" is not a claim you can evaluate until you know which of those the auditor had.** A clean report from someone who could only send it messages is a much smaller statement than a clean report from someone who saw the training data.

**An auditor who cannot see the model, the data, or the logs is auditing the paperwork.** That is genuinely worth doing — it catches things the organization cannot back up — but it is a review of what a company says about itself, and it should be described that way.

Two further things worth knowing.

**Being classed as high-risk in Europe does not mean somebody outside checked it.** For most high-risk categories the provider may assess its own system against the requirements, with the external route required only in narrower circumstances. The mark on the product is usually the provider's own declaration.

**And the auditing profession for AI does not yet have the things that make auditing trustworthy elsewhere** — shared standards, accreditation, the right to publish, consequences for a bad audit. Researchers who surveyed the field found the auditor is generally paid by the organization being audited, which frequently also picks what gets examined. Those are the conditions that produced famous audit failures in other industries, without the safeguards those industries eventually built.

---

## AI literacy notes

1. **Independence is necessary and not sufficient** — access decides what an audit can conclude.
2. **Three access levels**: black-box, white-box, and outside-the-box (process and data).
3. **An audit report without an access statement cannot be interpreted.**
4. **No access to weights, data or logs means the audit is of the documentation.**
5. **High-risk under the EU AI Act does not imply third-party assessment** — internal control is usually available.
6. **The auditor is normally paid by the audited**, who often also sets the scope.
7. **The field lacks standards, accreditation and consequences** for a bad or captured audit.
8. **A right to audit without a right to publish** is not assurance.
9. **Findings are only as good as the questions asked** — black-box results cover what the auditor thought to try.

---

## Governance notes

**Core question:** For any audit relied on here — what access did the auditor have, who chose the scope, who paid, and could they have published an adverse finding?

**Watch for:**
- "Independently audited" with no statement of the access level granted
- An audit scope set by the audited organization, with the boundaries unstated in the report
- Contracts giving the auditor no right to publish, or a veto over findings
- A CE mark or high-risk classification offered as evidence of external examination ([conformity assessment](conformity-assessment-ai.md))
- Certification of a *management system* presented as assurance about a *model* ([AI management system](ai-management-system-iso-42001.md))
- Audits repeated on a fixed calendar while the model changes continuously ([model version and update](model-version-update.md))
- No route for the auditor to report to a regulator rather than only to the client
- Auditor selection with no disclosed conflicts, including consulting work for the same client
- Findings closed without evidence of remediation, or remediation asserted by the audited party alone
- An audit of a full-precision model used to assure a quantized deployment ([quantization](quantization.md))

**Practice:**
- **State the access level in the report, and require it in anyone else's** — this is the single disclosure that makes an audit assessable
- **Negotiate publication rights and adverse-finding routes before the engagement**, not after a finding exists
- Give auditors the outside-the-box material — methodology, internal evaluation results, data documentation — since it is what lets them design targeted tests rather than guess ([model card / system card](model-card-system-card.md), [data provenance and lineage](data-provenance-lineage.md))
- **Scope by risk rather than by convenience**, and record what was excluded and why; an unstated exclusion is the most common way a clean report misleads
- Make the audit trail and evaluation records available in a form an outsider can use — audits are cheap when the evidence already exists and expensive when it must be reconstructed ([audit trail](audit-trail-ai.md), [observability](observability.md))
- Trigger re-audit on material change, not only on the calendar
- **Disclose the auditor's other commercial relationships with you**, and treat their absence from a report as a gap
- Track findings to closure with evidence, and keep the record ([continuous feedback and improvement](continuous-feedback-improvement.md))

**Key accountability owner:** whoever commissions the audit — because the commissioner sets access, scope and publication rights, and those three decisions determine the audit's value before any auditing happens.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High.** The access taxonomy comes from a large multi-author FAccT paper, and the ecosystem critique from a peer-reviewed field scan by researchers who have conducted audits themselves; the EU AI Act point is read from the regulation. **One scope note.** The field-scan findings describe the algorithmic-auditing ecosystem **as surveyed in 2022**, and the regulatory picture has moved since — the AI Act's obligations were not in force then. The structural conditions it identifies (auditor paid by the audited, scope chosen by the target, no accreditation, no consequence for a bad audit) are the durable finding; treat any claim about the *current* state of the profession as needing fresh evidence. This entry describes what makes an audit assessable rather than recommending any framework or provider.

---

## Related concepts

- [Conformity Assessment (AI)](conformity-assessment-ai.md) — the regulatory route, which is usually internal
- [Compliance (AI Systems)](compliance-ai-systems.md) — the obligations an audit tests against
- [AI Management System (ISO/IEC 42001)](ai-management-system-iso-42001.md) — certifying the process, not the model
- [Algorithmic Impact Assessment](algorithmic-impact-assessment.md) — the self-assessment an external audit is meant to check
- [Audit Trail (AI)](audit-trail-ai.md) — the evidence that makes an audit feasible
- [Observability](observability.md) — whether the system produces anything to audit
- [Accountability (AI Systems)](accountability-ai-systems.md) — what an audit is supposed to enable
- [Red Teaming](red-teaming.md) — adversarial testing, which needs the same access question asked
- [Model Card / System Card](model-card-system-card.md) — the disclosure an auditor starts from
- [Whistleblowing](whistleblowing.md) — the channel that operates when audit has not
- [Evaluation (AI Systems)](evaluation.md) — what an auditor can actually run
- [Bluewashing](bluewashing.md) — an audit used as a badge rather than as a check

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-349 | Casper, Stephen; Ezell, Carson; Siegmann, Charlotte; Kolt, Noam; Curtis, Taylor Lynn; Bucknall, Benjamin; Haupt, Andreas; et al. (21 authors) — *Black-Box Access is Insufficient for Rigorous AI Audits* (FAccT, 2024) · [link](https://arxiv.org/abs/2401.14446) | The access taxonomy this entry is built on — black-box, white-box, outside-the-box — and the operative conclusion that different access produces very different levels of evaluation, so **transparency about the access granted is necessary for findings to be interpretable**. |
| SRC-350 | Costanza-Chock, Sasha; Raji, Inioluwa Deborah; Buolamwini, Joy — *Who Audits the Auditors? Recommendations from a field scan of the algorithmic auditing ecosystem* (ACM FAccT, pp. 1571–1583, 2022) · [link](https://doi.org/10.1145/3531146.3533213) | The ecosystem critique: absence of shared standards, accreditation, methodological transparency and consequences, with the auditor typically paid by the audited and the scope frequently chosen by the target. ⚠️ Surveyed in 2022, before the AI Act's obligations — the structural conditions are the durable finding, not the state of the profession today. |
| SRC-312 | European Parliament / Council of the EU — *EU AI Act, Article 43: Conformity assessment* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The regulatory distinction that keeps this entry honest: for most Annex III high-risk systems the provider may use **internal control**, with third-party assessment mandatory only in narrower circumstances — so high-risk status is not evidence of external examination. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The certifiable object that is most often confused with an audit of a system: certification here attests to a **management system**, not to any model's behavior. ⚠️ Paywalled; cited for scope and structure only. |
| SRC-201 | Mitchell, M.; Wu, S.; Zaldivar, A.; Barnes, P.; Vasserman, L.; Hutchinson, B.; Spitzer, E.; Raji, I.D.; Gebru, T. — *Model Cards for Model Reporting* (ACM FAT*, 2019) · [link](https://doi.org/10.1145/3287560.3287596) | The documentation an external auditor starts from, and the reason outside-the-box access matters: a card states what the developer chose to disclose, which is the floor of an audit rather than its conclusion. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Give auditors outside-the-box material so they can design targeted tests. Make the audit trail usable by an outsider before the engagement, not during it. |
| **Organizational** | Access, scope and publication rights are set by whoever commissions the audit — and they determine its value before any auditing happens. |
| **Client-facing** | Explains why "independently audited" is a question rather than an answer, and what the follow-up questions are. |
| **LLM-native** | Black-box access covers what the auditor thought to try. An audit of the full-precision model does not cover the quantized build you are serving. |

---

*Last updated: v1.0 · September 2026*
