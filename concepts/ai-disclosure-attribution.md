<!--meta
category: Observability & Governance
short: Saying AI was used — a human practice, distinct from machine marking, and only one of them satisfies the law
aliases: [declaring AI use, AI attribution, should I say I used AI, AI-assisted disclosure, transparency statement]
tags: [Ethics, Regulatory, AI Literacy]
-->
# AI Disclosure (Attribution)

## One-line essence
When and how to say AI was used in producing something — an emerging expectation with real reputational and, increasingly, regulatory weight.

---

## Technical definition

A statement, by the person or organization responsible for a work, about how AI contributed to it. **It is a human practice, and it is not the same thing as machine detection.**

| | |
|---|---|
| **Detection / marking** | *Did this artifact pass through a generative system?* Machine-checked, per-artifact, provider-specific, objective, narrow. This is what [C2PA and watermarking](content-provenance-watermarking.md) do, and what EU AI Act Art. 50(2) obliges. |
| **Disclosure** | *How was this made, by whom, at which stage, to what degree?* Declared by a person, structured, tool-agnostic, broad — and unverifiable except by trust. |

**They are complementary, and only one satisfies the law.** A voluntary human disclosure does not discharge Art. 50(2)'s machine-readable marking obligation. Conflating them is a live error in practitioner writing, and it runs both ways: organizations claim compliance through a byline, or dismiss disclosure as redundant because their model already watermarks.

**The clearest worked example of a profession settling this is scholarly publishing**, and its reasoning transfers well beyond it. The ICMJE position: *"Chatbots (such as ChatGPT) should not be listed as authors because they cannot be responsible for the accuracy, integrity, and originality of the work."* **Authorship is grounded in answerability, not in who produced the text** — which is why the question "should the AI be credited?" has a principled answer rather than an etiquette answer. Disclosure is then required and placed *by function*: writing assistance in acknowledgments, data collection or analysis in methods. And the governing principle: *"Humans are responsible for any submitted material that included the use of AI-assisted technologies."*

**Where regulation has arrived.** Art. 50(1) requires telling people they are interacting with an AI system unless obvious. Art. 50(4) requires deployers to disclose deepfakes — narrowed for artistic, creative and satirical work — and requires disclosure for AI-generated text published on matters of public interest, **unless it underwent human editorial review.** That carve-out is doing real work: editorial review substitutes for disclosure, which tells you the obligation is about accountability for content, not about purity of process.

**The hard part is not whether to disclose but what to disclose.** "AI was used" spans proofreading and wholesale generation. A disclosure that does not distinguish degree conveys almost nothing, which is why the useful formats state *stage* and *extent* rather than a binary.

---

## Plain-language version

Disclosure is saying that AI helped make something. It sounds simple and it is not, because "AI was used" covers everything from fixing typos to writing the whole thing.

Two things get confused here. Some AI systems now stamp their output with an invisible technical marker, and in the EU that stamping is legally required. That is a machine telling machines. Disclosure is a person telling people how the work was actually made — and one does not replace the other. Saying so in a byline does not satisfy the legal marking rule, and a technical watermark does not tell a reader what you actually did.

Academic publishing has thought this through more than most fields, and its answer is useful. An AI cannot be an author — not because using one is shameful, but because an author has to be answerable for the work, and a system cannot be. So the human stays the author, and says where AI was used and for what: writing help goes in one place, data analysis in another.

The practical difficulty is degree. A disclosure that does not say *how much* tells the reader nearly nothing, and is the reason most disclosure statements are not very useful.

---

## AI literacy notes

1. **Disclosure and detection answer different questions.** One is declared by a person about process; the other is checked by a machine about an artifact. Neither substitutes for the other.
2. **A voluntary disclosure does not satisfy a marking obligation.** If Art. 50(2) applies to your system, the technical mark is the compliance step and the human statement is separate.
3. **Authorship follows answerability.** The reason an AI cannot be credited as author is that it cannot be responsible for the work — which is a stronger and more useful reason than convention.
4. **Degree is the missing element in most disclosures.** "AI-assisted" spanning proofreading to generation conveys little. State the stage and the extent.
5. **Disclosure does not transfer responsibility — it is the opposite.** Saying AI was used does not reduce your accountability for the content, and the professional standards say so explicitly.
6. **Expectations differ sharply by context.** Scholarly publishing, journalism, education, procurement and creative fields have materially different norms, and there is no universal standard to appeal to.
7. **Over-disclosure has costs too.** A blanket "AI may have been used" on everything is noise, and it dilutes the disclosures that carry information. Disclose what would change how someone reads or relies on the work.

---

## Governance notes

**Core question:** For work your organization publishes, what triggers a disclosure, what does it say, and who decided that?

**Watch for:**
- Disclosure treated as satisfying a marking obligation, or a technical watermark treated as satisfying a disclosure expectation
- A binary "AI was used" flag with no indication of stage or extent, which is technically true and practically uninformative
- No policy at all, so disclosure varies by individual judgment and is inconsistent in exactly the cases that matter
- The Art. 50(4) editorial-review carve-out claimed for published text without a documented review actually taking place
- Disclosure framed as a confession, which suppresses it — and drives the behavior toward non-disclosure rather than toward honesty
- Client and contractual expectations unstated, so disclosure decisions get made after a question is asked rather than before
- Blanket disclaimers applied everywhere, which is over-disclosure and carries no information

**Practice:**
- Define the trigger: **disclose where AI use would change how a reasonable person reads or relies on the work.** That test is more useful than a tool-based or percentage-based rule
- State stage and extent, not just presence — where in the process, and how much
- Keep the responsibility statement attached: disclosure names the method, it does not move accountability ([human responsibility](human-responsibility-in-ai-use.md))
- Where you rely on the editorial-review exemption, **document the review**; the exemption is conditional on it having happened
- Separate the marking obligation from the disclosure practice as distinct line items with distinct owners
- Agree expectations with clients and partners in advance rather than at the point of challenge
- Make disclosing normal — a routine metadata field rather than a caveat — since a format that reads as an apology will be avoided

**Key accountability owner:** whoever owns publication or delivery of the work, since disclosure attaches to the output rather than to the system. The Art. 50 marking duty is a separate obligation with a separate owner and does not transfer here.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the regulatory and professional positions, low on general practice.** Art. 50 is binding text and the ICMJE position is the governing standard across thousands of journals — both quotable and stable enough to rely on. **What is genuinely unsettled is everything outside those two:** there is no cross-domain standard, no agreed vocabulary for degree of assistance, no evidence on how disclosure affects reader trust, and rapidly shifting norms in journalism, education and creative work. The guidance here is a reasoned synthesis of two well-developed cases plus the marking/disclosure distinction, not a description of settled practice.

---

## Related concepts

- [Content Provenance & Watermarking (C2PA)](content-provenance-watermarking.md) — the machine half; complementary, and the one the law obliges
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — the principle disclosure rests on and does not dilute
- [Accountability (AI Systems)](accountability-ai-systems.md) — answerability, which is why an AI cannot be an author
- [Copyright & AI Output](copyright-ai-output.md) — a separate question: disclosing use is not the same as establishing ownership
- [Bluewashing](bluewashing.md) — disclosure's failure mode: a claim about practice with nothing behind it
- [Synthetic Media (Deepfakes)](synthetic-media-deepfakes.md) — where non-disclosure does the most direct harm
- [Compliance (AI Systems)](compliance-ai-systems.md) — where Art. 50 duties are demonstrated
- [AI Literacy](ai-literacy.md) — reading a disclosure correctly is itself a literacy skill
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — Art. 50(1)'s duty to say a user is talking to an AI addresses the same reflex
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the editorial review the public-interest exemption depends on
- [Model Card / System Card](model-card-system-card.md) — disclosure about the *system*, as against disclosure about a *work*

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-209 | International Committee of Medical Journal Editors — *Recommendations: Defining the Role of Authors and Contributors* (AI provisions) · [link](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html) | Authorship grounded in answerability, disclosure placed by function, and the principle that humans remain responsible for AI-assisted material. ⚠️ Domain-specific and revised periodically — check the current version. |
| SRC-204 | European Parliament / Council of the EU — *EU AI Act, Article 50: Transparency obligations* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The binding duties: AI-interaction notice, machine-readable marking of synthetic output, deepfake disclosure, and the public-interest text duty with its human-editorial-review exemption. |
| SRC-205 | Coalition for Content Provenance and Authenticity — *C2PA Technical Specification v2.4* (2026) · [link](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) | The machine-marking mechanism this practice is complementary to, and its stated limits. ⚠️ Industry consortium standard; versions rapidly. |
| SRC-208 | United States Copyright Office — *Copyright and Artificial Intelligence, Part 2: Copyrightability* (2025) · [link](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | Why the extent of human contribution is a substantive question rather than an etiquette one — it carries legal consequences beyond disclosure. ⚠️ US only. |
| SRC-119 | Vallor, S.; Vierkant, T. — *Find the Gap: AI, Responsible Agency and Vulnerability* (2024) · [link](https://doi.org/10.1007/s11023-024-09674-0) | Why responsibility for AI-assisted work stays with the human, which is the principle a disclosure states rather than transfers. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Marking and disclosure are separate obligations with separate owners. If you claim the editorial-review exemption for published text, document the review. |
| **Organizational** | Define the trigger as *would this change how someone reads or relies on the work* — more useful than a tool list or a percentage. And make disclosing routine rather than confessional, or it will be avoided. |
| **Client-facing** | Explains what a useful disclosure contains — stage and extent, not a binary — and why it should be agreed in advance rather than at the point of challenge. |
| **LLM-native** | An AI cannot be an author because it cannot be answerable. That reasoning, not convention, is what settles the crediting question. |

---

*Last updated: v1.0 · August 2026*
