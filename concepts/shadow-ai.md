<!--meta
category: Observability & Governance
short: Unsanctioned AI use — invisible to the processes meant to govern it, and usually a signal about the sanctioned option
aliases: [shadow IT, unsanctioned AI, ungoverned AI, unapproved AI tools, rogue AI]
tags: [Security, Data Governance, Regulatory]
established: established
-->
# Shadow AI

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
AI tools used inside an organization without official sanction, review, or governance — invisible to the very processes meant to manage AI risk.

---

## Technical definition

Unsanctioned AI use: employees pasting work into consumer chatbots, teams wiring an unreviewed API into a process, a department running a tool nobody assessed, browser extensions and IDE assistants installed personally. It is the AI instance of **Shadow IT**, a well-studied organizational phenomenon, and inherits its central finding — that unsanctioned adoption is usually driven by the sanctioned option being slower, worse, or absent, which makes it **a signal about the official offering as much as a compliance failure.**

**Three properties make it worse than classic Shadow IT, and they are the reason a separate entry is warranted:**

- **Data leaves on every interaction, not at setup.** Shadow IT typically meant data sitting somewhere unapproved. Shadow AI means a stream of prompts — client material, source code, personal data, unreleased strategy — crossing a boundary continuously, under terms nobody read.
- **There is no procurement event to catch.** No purchase order, no install, no integration request. A browser tab and a free tier leave no trace in any of the processes designed to detect new systems.
- **Zero marginal cost and instant capability.** Shadow IT required effort proportional to the benefit. Shadow AI's most consequential uses are the cheapest, so the usual friction that made adoption visible is gone.

**The governance failure is compound.** Every duty the organization thinks it holds — [privacy](privacy-ai-systems.md), [data minimization](data-minimization.md), [audit trail](audit-trail-ai.md), [verification](verification.md), [evaluation](evaluation.md), incident reporting — is unmet for exactly the uses nobody knows about. **An AI governance program with a Shadow AI problem is not partially effective; it is effective only over the portion of use it can see**, and it has no measurement of what portion that is.

**Suppression alone has a poor track record.** The Shadow IT literature is consistent that prohibition without a usable alternative displaces the behavior rather than ending it — and it does so *downward*, into channels with even less visibility. Personal devices and personal accounts are worse than an unsanctioned corporate tool, because they remove the last remaining observability.

---

## Plain-language version

Somewhere in most organizations, people are pasting work into AI tools nobody approved. Contract text, customer emails, code, half-finished strategy documents.

They are not being reckless. They are usually doing it because it makes them better at their job, and because whatever they were officially given is slower, worse, or does not exist.

This is an old problem — people have always adopted software faster than IT could approve it — but AI changes the shape of it. There is nothing to install and nothing to buy, so none of the usual tripwires fire. And instead of data sitting somewhere unapproved, data leaves the building a little at a time, every time someone uses the tool.

The consequence for governance is uncomfortable. Every policy an organization has about AI applies only to the use it knows about, and nobody knows what fraction that is. Banning the tools mostly moves the behavior onto personal phones and personal accounts, where you can see even less of it.

---

## AI literacy notes

1. **It is usually a symptom, not a violation.** People reach for unsanctioned tools when the sanctioned path is slower or missing. The adoption pattern is diagnostic information about your own provisioning.
2. **The tripwires do not fire.** No purchase, no install, no integration request. Detection methods built for software procurement will not find this.
3. **Free tiers often train on your input.** Consumer terms and enterprise terms differ substantially on data use and retention, and most people have not read either.
4. **Banning pushes it out of sight, not out of existence.** Prohibition without a usable alternative moves the behavior to personal devices and accounts, which is strictly worse for visibility.
5. **Your governance covers only what you can see.** And you have no measurement of how much that is — which makes any claim about AI governance coverage unverifiable.
6. **The most valuable uses are the most invisible.** Cheap and fast means the highest-leverage use is a browser tab, and browser tabs leave no record.
7. **Local and on-device deployment can be Shadow AI with better cover.** "The data never leaves" is a genuine argument that also makes unsanctioned adoption easier to justify and harder to detect — see [Local LLMs](local-llms.md).

---

## Governance notes

**Core question:** What proportion of AI use in this organization is visible to you — and if you cannot answer, what does your governance program actually cover?

**Watch for:**
- An AI policy with no corresponding discovery capability; the policy applies to the sanctioned set only
- Prohibition as the whole response, with no sanctioned alternative that meets the need people were solving
- Governance metrics reported over approved systems only, presented as organization-wide coverage
- Consumer-tier terms in use for work material, with data-use and retention terms nobody has read
- Unsanctioned use surfacing only through incidents, which is the most expensive possible detection method
- Individual and departmental use treated as out of scope because it is not a "system"
- Discovery framed punitively, which reliably drives the behavior further out of sight

**Practice:**
- **Provide a good sanctioned path first, then discover.** Detection without a usable alternative produces concealment rather than compliance; this ordering is the single most consequential choice here
- Run discovery through what you already have: network and DNS telemetry, SSO and OAuth grants, expense and card data, browser extension inventories, and — most productively — asking people without consequence
- Treat amnesty as a governance instrument: a stated, non-punitive window to register existing use surfaces more than any scan
- Read the tier that people actually use, not the enterprise agreement you signed, and publish the difference in plain language
- Make registration cheap and fast enough to be worth doing; a heavyweight intake process is itself a cause of Shadow AI
- Track the *ratio* of sanctioned to discovered use over time as a program metric — it is the only measure of whether governance coverage is improving
- Feed discovered use back into provisioning: repeated unsanctioned use of a capability is a requirements document

**Key accountability owner:** the AI governance owner for the program, but the practical lever sits with whoever owns the **sanctioned toolset** — because supply, not enforcement, is what determines the size of the shadow.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The organizational mechanism is well established in the peer-reviewed Shadow IT literature, and the compliance consequences follow directly from obligations that are themselves binding. **Two honest limits.** The three properties that distinguish Shadow AI from Shadow IT are this entry's argument from the technology's characteristics, not findings from a study of Shadow AI specifically — the phenomenon is too recent for a solid empirical base. And **prevalence figures should be treated with suspicion**: most circulating numbers come from vendor-commissioned surveys measuring salience rather than incidence, and this entry deliberately cites none. If you need a number, generate it internally through discovery.

---

## Related concepts

- [AI Governance](ai-governance.md) — the program whose coverage this silently bounds
- [Compliance (AI Systems)](compliance-ai-systems.md) — obligations that go unmet precisely where use is invisible
- [Privacy (AI Systems)](privacy-ai-systems.md) — the duty most directly breached by unsanctioned use
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — where pasted material can end up
- [Data Minimization](data-minimization.md) — impossible to apply to use you cannot see
- [Local LLMs](local-llms.md) — a data-transfer argument that can also make unsanctioned adoption easier to justify
- [Observability (AI Systems)](observability.md) — discovery is the observability problem applied to the organization rather than the system
- [Audit Trail (AI)](audit-trail-ai.md) — absent entirely for shadow use
- [AI Literacy](ai-literacy.md) — capability and a sanctioned path are the durable remedy
- [AI Use Case](ai-use-case.md) — registration turns shadow use into a governable unit
- [Ownership (AI Systems)](ownership-ai-systems.md) — shadow systems have users but no owner
- [Operational Readiness (AI)](operational-readiness-ai.md) — a slow sanctioned path is a readiness gap that manufactures shadow use
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — responsibility does not lapse because the tool was unapproved

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-207 | Haag, S.; Eckhardt, A. — *Shadow IT* (Business & Information Systems Engineering 59(6), 2017) · [link](https://doi.org/10.1007/s12599-017-0497-x) | The established organizational mechanism: unsanctioned adoption driven by deficits in the sanctioned offering, and the poor track record of suppression without an alternative. |
| SRC-077 | Huang, K. — *How to Discover Shadow AI Agents* (2025) · [link](https://open.substack.com/pub/kenhuangus/p/how-to-discover-shadow-ai-agents) | Practitioner discovery techniques for the AI-specific case. ⚠️ Practitioner/vendor-adjacent — used for method, not for prevalence claims. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The obligations that continue to apply to use the organization has not sanctioned and cannot see. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Deployer duties that presuppose the deployer knows the system is in use. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The map function assumes an inventory; shadow use is the gap between the inventory and reality. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Discovery runs on telemetry you already have — DNS, SSO and OAuth grants, expense data, extension inventories — but works far better after a sanctioned alternative exists. |
| **Organizational** | Your governance covers the use you can see, and you have no measure of that fraction. Supply, not enforcement, determines the size of the shadow; track the sanctioned-to-discovered ratio over time. |
| **Client-facing** | Explains why organizations need an approved AI path rather than a prohibition, and why confidentiality assurances depend on which tools people can actually reach for. |
| **LLM-native** | No procurement event, no install, zero marginal cost, and data leaving on every interaction rather than at setup — every tripwire built for software adoption misses this. |

---

*Last updated: v1.0 · August 2026*
