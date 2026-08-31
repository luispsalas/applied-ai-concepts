# AI Incident (Reporting)

## One-line essence
A documented event where an AI system caused or nearly caused harm — with a growing set of legal obligations to report and investigate it, not just fix it quietly.

---

## Technical definition

An **AI incident** is an event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly leads to actual harm — to a person's health, to the operation of critical infrastructure, to human rights or legally protected fundamental, labour and intellectual property rights, or to property, communities, or the environment. The intergovernmental definition deliberately separates this from an **AI hazard**: an event that is *potentially* harmful but where harm has not occurred. The distinction matters operationally, because near-misses are the cheapest evidence a system produces and are the first thing an informal process discards.

Reporting is increasingly a legal duty rather than a discretionary practice. Under the EU AI Act, providers of high-risk AI systems must report serious incidents to the market surveillance authorities of the member states where the incident occurred, on tiered deadlines: **15 days** in the general case, **2 days** where the incident involves widespread infringement or serious and irreversible disruption of critical infrastructure, and **10 days** where a person has died. An incomplete initial report followed by a complete one is expressly permitted — the obligation is to report promptly, not to wait for a finished investigation.

Beyond the regulatory duty sits a collective-memory argument, made by analogy to aviation: mature safety-critical sectors maintain shared incident databases so that a failure at one organization informs safety everywhere. AI has lacked that shared memory, so organizations repeat each other's failures. Public catalogs — the AI Incident Database, and the OECD's AI Incidents Monitor built on the definition above — exist to close that gap.

Note that the Commission guidance operationalising the EU obligation was still in draft and consultation at the time of writing. The statutory duty is settled; the reporting mechanics are not.

---

## Plain-language version

An AI incident is when an AI system actually hurt someone or something — and a near-miss is when it almost did. If your system is high-risk in the EU, you now have a legal deadline to tell a regulator, measured in days, not a quarter. The wider point is older than AI: aviation got safer because crashes were investigated and published, so nobody had to relearn the same lesson by crashing.

---

## AI literacy notes

1. **Incident and hazard are different, and the near-miss is the valuable one.** Harm that nearly happened is the cheapest possible warning. A process that only records realized harm throws away most of its evidence — and most of its warning time.
2. **"We fixed it" is no longer a complete response.** Where the reporting duty applies, quietly patching a failure and moving on is a compliance breach regardless of how well the fix worked.
3. **The clock starts at awareness, not at diagnosis.** Deadlines run from becoming aware of the incident, and an incomplete initial report is explicitly allowed. Waiting for a confident root cause is the standard way organizations miss a statutory deadline.
4. **You cannot report what you did not record.** Incident reporting depends entirely on an [audit trail](audit-trail-ai.md) that can reconstruct what the system received, decided, and did. That dependency is invisible until the day it is needed.
5. **Publishing failures is a public good with a private cost.** The collective-memory case is strong, but disclosure carries reputational and legal exposure. Organizations that only report what is compulsory should recognize the asymmetry rather than mistake it for a neutral choice.

---

## Governance notes

**Core question:** If this system caused harm today, would anyone notice, would anyone be told, and could you reconstruct what happened within the statutory deadline?

**Watch for:**
- No definition of what counts as an incident for your systems, so nothing is ever formally classified as one
- Near-misses discussed informally and never recorded, leaving no data before the first real harm
- Detection depending on user complaints rather than monitoring — external discovery is late discovery
- Reporting deadlines nobody owns, or a process that waits for root cause before notifying
- Logging insufficient to reconstruct the event, discovered only when a report is due

**Practice:**
- Define incident and hazard thresholds per system *before* deployment, using the harm categories above rather than inventing local ones
- Name the accountable owner and the notification path, with the deadline attached, so the clock has a keeper
- Record near-misses in the same register as incidents; track the ratio, since a register with no hazards is evidence of under-detection, not of safety
- Verify that [audit trail](audit-trail-ai.md) retention is long enough to support a post-hoc investigation
- Run the notification path as a drill at least once — an untested reporting process fails on the day it is first needed
- Feed every incident back into [evaluation](evaluation.md) and [red teaming](red-teaming.md) as a permanent regression case

**Key accountability owner:** the system owner, jointly with the compliance function for the notification duty.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the definitions and the statutory obligation — the OECD definition is the intergovernmental reference and the EU AI Act text is in force, with deadlines verified against the article. **Medium** on practice: the Commission's operational guidance was still in draft at the time of writing, incident taxonomies remain inconsistent across jurisdictions, and public reporting is voluntary and demonstrably incomplete outside the regulated cases.

---

## Related concepts

- [Audit Trail (AI)](audit-trail-ai.md) — the precondition; an incident you cannot reconstruct is one you cannot report
- [Observability](observability.md) — determines whether you detect an incident yourself or hear about it from a user or regulator
- [Compliance (AI Systems)](compliance-ai-systems.md) — reporting is now an obligation with deadlines, not a discretionary practice
- [Accountability (AI Systems)](accountability-ai-systems.md) — an incident is the moment answerability stops being theoretical
- [Failure Modes (AI Systems)](failure-modes-ai-systems.md) — the taxonomy of what goes wrong; incidents are those failures realized in the world
- [Red Teaming](red-teaming.md) — finds incidents before users do, and should absorb every real incident as a regression case
- [Evaluation (AI Systems)](evaluation.md) — where incident learnings become permanent checks
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the duty to notice, report, and answer does not transfer to the system
- [AI Governance](ai-governance.md) — incident response is a core governance function, not an operational afterthought

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-163 | OECD — *Defining AI incidents and related terms* (2024) · [link](https://www.oecd.org/en/publications/defining-ai-incidents-and-related-terms_d1a8d965-en.html) | The reference definitions: AI incident vs AI hazard, and the enumerated harm categories. |
| SRC-162 | European Parliament / Council of the EU — *EU Artificial Intelligence Act, Article 73: Reporting of serious incidents* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The legal obligation and its tiered deadlines (15 days / 2 days / 10 days), and that an incomplete initial report is permitted. ⚠️ Commission operational guidance still in draft at time of writing. |
| SRC-164 | McGregor, Sean — *Preventing Repeated Real World AI Failures by Cataloging Incidents: The AI Incident Database* (AAAI, 2021) · [link](https://ojs.aaai.org/index.php/AAAI/article/view/17817) | The aviation analogy and the collective-memory argument for cataloging incidents publicly. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places incident response inside a recognized risk-management lifecycle rather than treating it as an ad-hoc reaction. |
| SRC-130 | European Parliament / Council of the EU — *EU AI Act, Article 12: Record-keeping* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The logging obligation that makes incident reconstruction possible; the two duties are designed to work together. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Retention and log detail are set by what a post-incident investigation will need, not by what is convenient day to day. |
| **Organizational** | Reporting deadlines are measured in days and start at awareness. Someone must own the clock before the first incident, not after. |
| **Client-facing** | Answers "what happens if it goes wrong?" with a defined process and a named owner rather than a reassurance. |
| **LLM-native** | Near-misses are abundant and cheap to collect; recording them is the difference between learning early and learning from a realized harm. |

---

*Last updated: v1.0 · August 2026*
