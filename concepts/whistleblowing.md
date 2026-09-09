<!--meta
category: Observability & Governance
short: Protected disclosure by an insider — the control that operates when every internal one has failed, and whose legal protection covers illegality rather than danger
aliases: [protected disclosure, whistleblower, whistleblower protection, reporting of infringements, right to warn, speaking up, internal reporting channel, retaliation protection]
tags: [Regulatory, Ethics, Safety]
established: established
-->
# Whistleblowing

> **Term status — Established.** A legal term of art with dedicated EU legislation, national statutes across most jurisdictions, and an explicit article in the EU AI Act. Independent of any vendor.

## One-line essence
An insider reporting wrongdoing they encountered through their work, under protection from retaliation — the control that operates precisely when every internal control has already failed.

---

## Technical definition

Whistleblowing is disclosure by a person who learned of wrongdoing through their working relationship, to a channel outside the ordinary chain of command, with legal protection against retaliation.

**In the EU the AI Act does not create its own regime — it borrows one, in a single sentence.** Article 87 reads, in full: *"Directive (EU) 2019/1937 shall apply to the reporting of infringements of this Regulation and the protection of persons reporting such infringements."* Recital 172 gives the reasoning: persons acting as whistleblowers on infringements of the Regulation should be protected under Union law.

**That borrowing is efficient and it has a consequence worth stating plainly.** Directive (EU) 2019/1937 protects reports of **breaches of Union law**. So the AI Act's protection attaches to *reporting an infringement of the Regulation* — not to reporting a danger the Regulation does not make illegal. **A researcher alarmed by a capability that is entirely lawful is outside it.**

**That gap is not a hypothesis; it is the stated motivation of the people closest to the systems.** The *Right to Warn* letter, signed by current and former employees of frontier AI companies, puts it in one line: *"Ordinary whistleblower protections are insufficient because they focus on illegal activity, whereas many of the risks we are concerned about are not yet regulated."* Their further claim is the structural one — that these companies hold substantial non-public information about capabilities, limitations and risk levels, with weak obligations to share it, so **current and former employees are among the few people positioned to hold them accountable** ([third-party audit](third-party-audit.md) being the other, and dependent on access it often does not get).

**What the letter asks for is a private-ordering supplement to law**, and reading it as a checklist is the practical use: no contractual terms prohibiting risk-related criticism; a verifiably anonymous route to the board, to regulators, and to an independent expert body; support for open criticism where trade secrets are protected; and no retaliation for public disclosure of risk-related information *after other processes have failed*. They accept that concerns should go through an adequate internal process first — **once one exists**.

**Two design properties determine whether any of this works:**

- **Anonymity must be verifiable by the reporter**, not asserted by the recipient. A channel whose confidentiality the organization guarantees to itself is not a channel a frightened person will use.
- **The escalation path must not terminate inside the organization.** A route that ends at the board is a route the board can close; the directive's architecture assumes external and public tiers exist ([accountability](accountability-ai-systems.md)).

**Where this sits among AI controls:** it is the last one. [Audit trails](audit-trail-ai.md), [evaluation](evaluation.md), [incident reporting](ai-incident-reporting.md) and [third-party audit](third-party-audit.md) all assume the organization is functioning. **Whistleblowing is the mechanism for when the organization is the problem** — which is exactly when its own processes cannot be relied on to surface anything.

---

## Plain-language version

Whistleblowing is when someone inside an organization reports serious wrongdoing they found through their job, using a route that goes around their own management, with legal protection so they cannot simply be fired for it.

Europe has a dedicated law for this, and the EU AI Act connects to it in one sentence: the existing whistleblower directive applies to people reporting breaches of the AI Act.

**That single sentence is efficient, and it leaves a specific hole.** The directive protects you for reporting **breaches of the law**. So if you report a company breaking the AI Act, you are protected. **If you are frightened by something the company is building that is not against any law, you are not** — and a great deal of what worries people about advanced AI is not yet regulated at all.

This is not a theoretical gap. It is the exact complaint made by employees and former employees of the largest AI companies, who wrote it down: ordinary whistleblower protections focus on illegal activity, while many of the risks they are concerned about are not yet regulated. Their other point is harder to argue with: **these companies know things about their own systems that nobody outside does, they are under little obligation to share it, and so their staff are among the very few people in a position to say anything.**

What they asked for is worth knowing because any organization can adopt it without waiting for a law:

- Do not make people sign agreements that stop them criticizing the company over risk.
- Give them a genuinely anonymous way to raise concerns — to the board, to regulators, and to an independent expert body outside.
- Allow open criticism, with commercial secrets still protected.
- Do not retaliate against someone who goes public about a risk **after the other routes have failed**.

Two details decide whether such a scheme is real or decorative.

**The anonymity has to be verifiable by the person using it.** If the only assurance is the company saying "don't worry, it's confidential," nobody with something serious to report will believe it — and they are right not to.

**And the escalation cannot dead-end inside the building.** If the highest place a concern can go is the board, then the board can bury it. There has to be somewhere further.

Finally, the thing that makes this different from every other control: **most governance mechanisms assume the organization is working properly.** Audits, incident logs, evaluations, sign-offs — all of them depend on people doing their jobs honestly. Whistleblowing is the one designed for when that assumption has failed. Which is why judging it by how often it gets used is the wrong test.

---

## AI literacy notes

1. **The EU AI Act creates no separate regime** — Article 87 applies Directive (EU) 2019/1937.
2. **Protection attaches to reporting a breach of law**, not to reporting an unregulated danger.
3. **That gap is the stated motivation** of the *Right to Warn* signatories.
4. **Frontier developers hold non-public information** about their own systems, with weak duties to share it.
5. **Anonymity must be verifiable by the reporter**, not asserted by the recipient.
6. **An escalation path that ends at the board can be closed by the board.**
7. **Non-disparagement terms covering risk criticism** are the mechanism that suppresses disclosure.
8. **It is the control of last resort** — it operates when the others have already failed.
9. **Low usage is not evidence it is working**, and may be evidence of the opposite.

---

## Governance notes

**Core question:** If someone here believed this organization was building something dangerous but lawful, what would they do — and would it cost them their job?

**Watch for:**
- Employment, severance or equity agreements restricting risk-related criticism ([acceptable use policy](acceptable-use-policy.md) governs users; this governs staff)
- A reporting channel whose anonymity is asserted by the organization and not verifiable by the reporter
- An escalation route that terminates internally, with no external or regulatory tier
- Whistleblower policy scoped to legal breaches only, in an organization whose main risks are unregulated
- A channel that exists on paper with no evidence of use, treated as evidence that nothing is wrong
- Reports routed through the line management most likely to be implicated
- No protection for **former** employees, who are frequently the ones able to speak
- Concerns raised and closed with no record of what was decided or by whom ([audit trail](audit-trail-ai.md))
- Retaliation in indirect forms — reassignment, exclusion, withheld vested benefits — that a policy naming only dismissal does not cover
- Safety staff with no route that bypasses the commercial owner of the product they are assessing ([accountability](accountability-ai-systems.md))

**Practice:**
- **Scope the policy to risk, not only to illegality** — this is the single change that closes the gap the AI Act inherits, and it requires no legislation
- **Provide a route to an independent external body**, not only to the board and the regulator
- Make anonymity technically verifiable by the reporter, and say how it works rather than that it exists
- **Remove non-disparagement terms covering risk-related concerns**, including from severance agreements, and say so publicly
- Extend protection explicitly to former employees and contractors
- Route reports away from implicated management by design, with a named alternative recipient
- **Record every report and its disposition**, so a pattern of dismissal is visible to a reviewer ([observability](observability.md))
- Publish counts and outcomes at an aggregate level; a channel nobody can see the effect of is a channel nobody trusts
- **Do not treat low volume as assurance.** Ask instead whether anyone has ever used it and what happened to them
- Connect it to the incident process, so a disclosure that reveals a realized harm enters the same pipeline ([AI incident reporting](ai-incident-reporting.md))

**Key accountability owner:** the board, or the highest body not operationally responsible for the products being reported on — because a channel owned by the people it might implicate is not a channel, and this is the one control whose whole purpose is to work when management is the problem.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the legal position, which is read directly from the regulation.** Article 87 was quoted verbatim from the EUR-Lex text of Regulation (EU) 2024/1689, as was the recital behind it, and the *Right to Warn* language was read from the letter itself rather than from coverage of it. **What this entry does not do is offer legal advice**: whether a particular disclosure is protected depends on national implementation of the directive, the reporter's status, and the channel used, none of which this entry can assess. **The claim that the protection gap matters is an argument, not a finding** — it follows from the directive's scope being breaches of law, and it is corroborated by the signatories' own statement of motivation, but no one has measured how many concerns go unreported for this reason, and by the nature of the thing no one can.

---

## Related concepts

- [Accountability (AI Systems)](accountability-ai-systems.md) — the answerability whistleblowing enforces when nothing else does
- [Third-Party Audit](third-party-audit.md) — the other route to outside scrutiny, and its access problem
- [AI Incident Reporting](ai-incident-reporting.md) — the process a disclosure should feed into
- [Audit Trail (AI)](audit-trail-ai.md) — the record that makes a suppressed concern visible later
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the duty that persists when the process fails
- [Moral Crumple Zone](moral-crumple-zone.md) — what happens to the individual when responsibility is diffuse
- [Compliance (AI Systems)](compliance-ai-systems.md) — the legal obligations a report may concern
- [AI Governance](ai-governance.md) — where the policy and the channel are owned
- [Dangerous Capability](dangerous-capability.md) — the lawful-but-alarming case the protection misses
- [Frontier AI](frontier-ai.md) — where the information asymmetry is largest
- [Observability](observability.md) — making disclosure patterns visible to a reviewer

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-351 | European Parliament / Council of the EU — *EU AI Act, Article 87: Reporting of infringements and protection of reporting persons* (Reg. (EU) 2024/1689, 2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The AI Act's entire whistleblowing provision, quoted verbatim from EUR-Lex — one sentence applying Directive (EU) 2019/1937 — together with Recital 172. The brevity is the finding: the Act borrows a regime rather than building one, and inherits its scope. |
| SRC-352 | European Parliament / Council of the EU — *Directive (EU) 2019/1937 on the protection of persons who report breaches of Union law* (23 October 2019, OJ L 305, 26.11.2019, p. 17) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L1937) | The borrowed instrument, and the source of the scope limit this entry turns on: protection attaches to reporting **breaches of Union law**, which is what leaves lawful-but-dangerous conduct outside it. ⚠️ National implementations vary; this entry states the scope, not the remedies available in any jurisdiction. |
| SRC-353 | Hilton, Jacob; Kokotajlo, Daniel; Kumar, Ramana; Nanda, Neel; Saunders, William; Wainwright, Carroll; Ziegler, Daniel; et al. (current and former employees of frontier AI companies) — *A Right to Warn about Advanced Artificial Intelligence* (2024) · [link](https://righttowarn.ai/) | The gap stated by the people inside it, verbatim: *"Ordinary whistleblower protections are insufficient because they focus on illegal activity, whereas many of the risks we are concerned about are not yet regulated."* Also the four-principle framework this entry's practice section draws on. ⚠️ An advocacy document by interested parties, several anonymous — cite for the stated position and the proposed principles, never as evidence about any company's conduct. |
| SRC-264 | UK AI Security Institute — *Incident Report: unsanctioned agent behaviour during cyber testing* (August 4, 2026) · [link](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) | The contrast case: an independent regulator publishing findings about models from two competing vendors — which is what external scrutiny produces when it exists, and the alternative to relying on insiders. ⚠️ Safeguards were deliberately reduced and configurations were not commercially available. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | If your concern is about something lawful, the statutory protection probably does not cover it. Know what your organization's policy is scoped to before you need it. |
| **Organizational** | Scoping the policy to *risk* rather than to *illegality* closes the gap the AI Act inherits, and needs no legislation. A channel owned by the people it might implicate is not a channel. |
| **Client-facing** | Explains why a supplier's internal reporting policy is a reasonable due-diligence question, and what a good answer looks like. |
| **LLM-native** | Developers hold non-public information about capability and risk. Where disclosure obligations are weak, insiders are structurally among the few who can surface anything. |

---

*Last updated: v1.0 · September 2026*
