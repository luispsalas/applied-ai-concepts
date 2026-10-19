<!--meta
category: Observability & Governance
short: A voluntary US framework for managing AI risk through four functions, Govern, Map, Measure and Manage. Laws now point to it by reference, and it is being rewritten
aliases: [NIST AI RMF, AI RMF, AI RMF 1.0, NIST, NIST AI 100-1, NIST AI 600-1, Generative AI Profile, Govern Map Measure Manage, NIST framework]
tags: [Regulatory, Safety]
established: established
-->
[Applied AI Concepts](../README.md) › [Observability & Governance](../glossary/categories.md#observability--governance) › NIST AI Risk Management Framework (AI RMF)

# NIST AI Risk Management Framework (AI RMF)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
A voluntary US framework for managing AI risk through four functions, Govern, Map, Measure and Manage. Laws now point to it by reference, and it is being rewritten.

---

## Technical definition

The US National Institute of Standards and Technology published the AI Risk Management Framework in January 2023 as AI RMF 1.0 (NIST AI 100-1). It describes itself as *"intended to be voluntary, rights-preserving, non-sector-specific, and use-case agnostic"*, written for anyone who designs, develops, deploys or uses AI systems. It has two parts.

**The first part says what trustworthy AI looks like.** It names seven characteristics: valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy enhanced; and fair, with harmful bias managed. It treats AI systems as socio-technical, so risks come from how a system is used and by whom as much as from the model.

**The second part, the Core, says how to manage the risk.** It has four functions. **Govern** sets the culture, policies and accountability, and applies across everything else. **Map** establishes the context a system operates in and the risks that context creates. **Measure** analyzes and tracks those risks. **Manage** prioritizes and acts on them. Each function breaks down into categories and subcategories, and a companion Playbook suggests actions for each. Many entries in this wiki cite the framework because these four functions are a shared vocabulary for the controls they describe.

**It structures the decision and leaves the threshold to you.** The framework states that *"it does not prescribe risk tolerance"*. How much risk is acceptable is the organization's call, informed by law and context. Two organizations can both follow the framework closely and accept very different levels of risk.

**Profiles adapt it to a sector or a technology.** The best known is the Generative AI Profile (NIST AI 600-1, July 2024). It names 12 risks unique to or made worse by generative AI, among them confabulation, information integrity, information security, data privacy and harmful bias, and maps suggested actions onto the four functions. The profile says it was issued under Executive Order 14110. That order was revoked on January 20, 2025, by Executive Order 14148. The profile is still listed on NIST's framework page.

**The framework is being rewritten.** It was designed as a living document, with versioned updates and a formal review due no later than 2028. That schedule has been overtaken: NIST's page now states that *"The AI RMF 1.0 is being revised as part of the White House AI Action Plan."* The Action Plan, published in July 2025, directs NIST to *"revise the NIST AI Risk Management Framework to eliminate references to misinformation, Diversity, Equity, and Inclusion, and climate change."* What the revised version will contain has not been published.

**Voluntary does not mean inconsequential, because laws can adopt it by reference.** Colorado's 2024 AI Act asks deployers of high-risk systems to keep a risk management program that is reasonable considering *"the latest version"* of the NIST framework, ISO/IEC 42001, or another recognized framework at least as stringent. Complying with those frameworks also forms part of an affirmative defense when the state's Attorney General enforces the law. Because the statute says the latest version, a revision in Washington changes what a Colorado obligation points to, with no change to the statute itself.

**It is not a certification.** NIST offers no certification against the framework, so an organization's conformance is self-declared. That is the main difference from [ISO/IEC 42001](ai-management-system-iso-42001.md), which an accredited auditor certifies. It also does not discharge legal duties such as those in the EU AI Act.

---

## Plain-language version

The NIST AI Risk Management Framework is a free guide from a US government standards agency on how to manage the risks of AI. Nobody is required to follow it, and NIST does not certify anyone against it. It is widely cited anyway, including throughout this wiki and in at least one US state law.

It does two things. It lists what a trustworthy AI system should be, such as reliable, safe, secure, explainable, private and fair. And it organizes the work into four jobs: set up who is responsible and how decisions get made, understand the setting each system works in, measure the risks, and act on them.

What it does not do is tell you how much risk is acceptable. That decision stays with you.

Two things changed recently. The framework is being rewritten on instructions from the White House, which has asked for some topics to be removed. And at least one US state has written it into law by pointing at "the latest version", so when the framework changes, what that law asks for can change with it.

---

## AI literacy notes

1. **Voluntary, self-declared and not certified by NIST.** Saying an organization follows it is a claim, not a finding. Ask what was done and who checked.
2. **It organizes decisions without making them.** Risk tolerance is explicitly left to the organization, so two organizations both following the framework can accept very different levels of risk.
3. **A claim of NIST alignment needs a version and a scope.** Which version, which functions, and which subcategories were actually implemented.
4. **The version is about to change.** Version 1.0 is under revision, with some topics directed for removal, so wording copied from it today may not survive.
5. **A framework can become a legal reference.** When a statute points to "the latest version", the framework's revisions change what the law points to.
6. **The Generative AI Profile has lost its mandate, but not its content.** The executive order it was issued under has been revoked. Its list of risks is still a useful checklist; just do not cite it as current federal policy.

---

## Governance notes

**Core question:** Which version of the framework does our program claim to follow, which parts did we implement, who decided our risk tolerance, and who would notice if the framework changed underneath us?

**Watch for:**
- Claims of NIST alignment with no version, no date and no mapping to specific functions or subcategories
- Risk tolerance never set, so the framework is followed in form while the actual decision is never made
- Framework adoption presented as legal compliance, here or in another jurisdiction ([compliance](compliance-ai-systems.md))
- Policies, contracts or vendor questionnaires that reference the NIST AI RMF without naming a version, which makes the obligation a moving target
- The Generative AI Profile cited as current federal policy, when the order behind it has been revoked
- Self-attested conformance used where an independent check is needed ([third-party audit](third-party-audit.md))

**Practice:**
- **Record the version and date of every framework you claim to follow**, and the functions and subcategories you implemented
- Set and document risk tolerance explicitly, with a named owner ([accountability](accountability-ai-systems.md))
- Keep a crosswalk between the framework and the standards and laws you are actually bound by, such as ISO/IEC 42001 and the EU AI Act, so each control is traceable to its source
- Track the revision as a change event: when a new version is published, review what was removed or added and decide what changes for you
- Where a law or contract references "the latest version", treat each framework revision as a potential change in obligations and route it to legal review

**Key accountability owner:** the AI governance lead, who owns the claim of conformance, with legal review wherever a law or contract incorporates the framework by reference.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High on what the framework says, medium on where it is going.** Every description here is taken from the primary documents: the framework, its Generative AI Profile, NIST's own page, the Action Plan, the executive order, and the Colorado statute as signed. **What is not known is the content of the revised version**, which has not been published, and this entry does not guess at it. The Colorado provisions are described from the 2024 signed text, and state AI law has been amended actively since, so check the current statute before relying on them. How widely the framework is adopted, and how faithfully, has not been measured in any source cited here.

---

## Related concepts

- [AI Management System (ISO 42001)](ai-management-system-iso-42001.md) — the certifiable counterpart: an audited management system where this framework is self-declared
- [AI Governance](ai-governance.md) — the function the Govern function describes, and where conformance claims are owned
- [Compliance (AI Systems)](compliance-ai-systems.md) — why adopting a voluntary framework is not the same as meeting a legal obligation
- [Algorithmic Impact Assessment](algorithmic-impact-assessment.md) — a concrete way to carry out the Map function for one system
- [Accountability (AI Systems)](accountability-ai-systems.md) — the named ownership the Govern function asks for
- [Third-Party Audit](third-party-audit.md) — the independent check that self-declared conformance lacks
- [Red Teaming](red-teaming.md) — one of the Measure activities, and a term state law borrows from NIST
- [Systemic Risk (AI)](systemic-risk-ai.md) — the EU's frame for risks that a voluntary US framework addresses differently

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The framework itself (AI RMF 1.0, NIST AI 100-1, January 2023): the quoted scope, the seven characteristics, the four functions, the risk-tolerance statement, the living-document schedule, and the page's quoted statement that it is being revised. ⚠️ Under revision; this entry describes version 1.0. |
| SRC-412 | NIST — *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)* (2024) · [link](https://doi.org/10.6028/NIST.AI.600-1) | The 12 generative-AI risks and suggested actions by function, and the profile's statement that it was issued under Executive Order 14110. ⚠️ That order has been revoked. |
| SRC-413 | The White House — *Winning the Race: America's AI Action Plan* (July 2025) · [link](https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf) | The quoted instruction to revise the framework and remove named topics. ⚠️ A policy document; cited for what it directs, not for what the revision will contain. |
| SRC-414 | The White House — *Executive Order 14148: Initial Rescissions of Harmful Executive Orders and Actions* (January 20, 2025) · [link](https://www.govinfo.gov/content/pkg/FR-2025-01-28/html/2025-01901.htm) | Section 2(ggg), revoking Executive Order 14110. |
| SRC-415 | Colorado General Assembly — *Senate Bill 24-205: Consumer Protections for Artificial Intelligence (as signed)* (2024) · [link](https://leg.colorado.gov/sites/default/files/2024a_205_signed.pdf) | The framework adopted by reference: risk programs judged against "the latest version", and framework compliance as part of an affirmative defense in Attorney General enforcement. ⚠️ Read from the 2024 signed text; check the current statute. |
| SRC-169 | ISO/IEC JTC 1/SC 42 — *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system* (2023) · [link](https://www.iso.org/standard/81230.html) | The certifiable standard named alongside the framework in the Colorado statute, and the contrast between certification and self-declaration. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding obligations that adopting a voluntary framework does not discharge. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | The four functions give a common structure for mapping controls, metrics and tests, and the subcategories are the level at which "we follow NIST" can actually be checked. |
| **Organizational** | Conformance is self-declared, risk tolerance is yours to set, and the version is changing. All three need an owner and a record. |
| **Client-facing** | Explains what a claim of NIST alignment does and does not promise, and why a certification such as ISO 42001 is a different kind of assurance. |
| **LLM-native** | A voluntary US framework, version 1.0 under politically directed revision, now referenced by state law. Cite the version, and never treat the Generative AI Profile as current federal policy. |

---

*Last updated: v1.0 · October 2026*
