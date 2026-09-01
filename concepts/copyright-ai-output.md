<!--meta
category: Knowledge & Memory
short: Who owns what a model makes, and whether training was lawful — two questions, one with a US answer and one genuinely open
aliases: [who owns AI output, AI copyright, intellectual property, can I copyright this, training data copyright]
tags: [Regulatory, Ethics, AI Literacy]
-->
# Copyright & AI Output

## One-line essence
Who owns what a model produces, whether it can reproduce protected work, and why the answer is genuinely unsettled rather than merely unclear.

---

## Technical definition

Two separate legal questions, constantly merged, with different answers and different parties at risk:

| | |
|---|---|
| **Output side** | Is what the model produced protectable, and by whom? A question about *your* rights. |
| **Input side** | Was training on protected work lawful? A question about the *provider's* exposure that can reach you through indemnities and injunctions. |

**On the output side, the clearest available position is the US Copyright Office's**, and the operative sentence is worth quoting exactly: *"The Office concludes that, given current generally available technology, prompts alone do not provide sufficient human control to make users of an AI system the authors of the output. Prompts essentially function as instructions that convey unprotectible ideas."*

The rest of the Office's position follows from human authorship:

- Material generated **wholly** by AI is not copyrightable, and existing law is adequate to reach that conclusion — no new statute needed.
- **Human contributions can be protectable**: expressive inputs you authored, your selection and arrangement of AI-generated material, and your modifications — each assessed case by case against the ordinary originality standard.
- The conclusion is explicitly **technology-dependent**. The Office notes that if tools develop to give creators more control, the analysis may change.

**This is a US position, not a global one.** It is the Office's reasoned view rather than binding precedent, litigation is active, and other jurisdictions differ materially. Anything written as if "AI output can't be copyrighted" is a settled worldwide fact is wrong.

**On the input side, nothing is settled.** Whether training on protected work is fair use, or falls under a text-and-data-mining exception, is under active litigation and legislative development. What *is* established is adjacent and load-bearing: models can and do reproduce training data verbatim, so the risk is not only that training was unlawful but that an output reproduces something protected. And the licensing status of widely used corpora is frequently unknown — an audit of 1,800+ datasets found license omission above 70%.

**The practical position for a deploying organization** is that you likely hold weaker rights in AI output than you assume, and carry more exposure from what it might reproduce than you assume. Both errors run the same direction.

---

## Plain-language version

Two questions get mixed together and they are not the same.

*Can you own what the AI made for you?* In the US, the Copyright Office's answer is: not from prompting alone, however detailed the prompt. Prompts count as instructions and ideas, and ideas are not protectable. What you *can* own is your own contribution — text you wrote, how you selected and arranged what came out, what you changed. Purely AI-generated material is not protected, which also means anyone can use it.

*Was it legal to train the model on other people's work?* Nobody knows yet. It is being litigated and legislated right now, and the answer will differ by country.

A third thing is more settled and more immediately practical: models can reproduce chunks of their training data word for word. So even setting aside whether training was lawful, an output can contain someone else's protected material without anyone intending it.

The honest summary is that this is genuinely unsettled — not that the answer exists and is hard to find. Anyone giving you a confident universal answer is overstating.

---

## AI literacy notes

1. **Two questions, not one.** Ownership of output and legality of training are separate, with different parties at risk. Merging them produces confused policy.
2. **Prompts alone don't get you authorship** — in the US, and however elaborate the prompt. The Office was explicit, and its reasoning is that prompts convey ideas rather than control expression.
3. **Your own contribution can still be protected.** Text you wrote, arrangement you chose, edits you made. This is why "AI-assisted" and "AI-generated" are different legal situations, and why keeping a record of what you did matters.
4. **Unprotected also means unprotected from others.** If output is not copyrightable, you cannot stop anyone reusing it. That cuts against you commercially, not just legally.
5. **Verbatim reproduction is a demonstrated capability**, not a theoretical risk. Extraction research shows models emit training data, so an output may carry protected material regardless of how training is resolved.
6. **Jurisdiction matters enormously.** The US Copyright Office does not speak for the EU or UK, and positions diverge. Treat any single-jurisdiction answer as scoped.
7. **The conclusion is dated by design.** It rests on "currently available technology" and the Office says so. Re-check rather than treating it as permanent.

---

## Governance notes

**Core question:** For AI-assisted work your organization produces or ships, what rights do you actually hold — and what happens if an output turns out to reproduce someone else's protected material?

**Watch for:**
- Commercial or product material assumed to be owned because it was commissioned, when purely AI-generated portions may be unprotectable
- No record of the human contribution, which is exactly the evidence a protectability claim depends on
- Provider indemnities relied on without reading the conditions, which are usually narrower than the marketing summary
- The training question and the output question conflated in policy, producing rules that address neither
- A single jurisdiction's position applied across a multinational footprint
- Model or dataset licensing unchecked before commercial use ([data provenance](data-provenance-lineage.md))
- Contributor and vendor agreements silent on AI use, leaving ownership ambiguous by omission

**Practice:**
- **Record the human contribution** as work proceeds — drafts, edits, selection decisions. Retrospective reconstruction is weak evidence, and this is the one thing under your control that improves your position
- Distinguish AI-*assisted* from AI-*generated* in internal classification, since they sit differently
- Read the provider's indemnity for its conditions — often requiring filters enabled, unmodified output, no infringing prompt
- Where output must be ownable, keep substantial human authorship in the loop by design, not by accident
- Check licensing of models and datasets before commercial deployment
- Get a jurisdiction-specific position rather than a general one, and date it
- Where reproduction risk is material, add output-side checks rather than relying on the training question resolving favorably

**Key accountability owner:** legal or contracts, with the system owner accountable for the evidence — because whether human contribution can be *demonstrated* is an operational question that legal cannot answer after the fact.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the US output-side position, low on nearly everything else — and the asymmetry is the point.** The Copyright Office's conclusions are quotable and reasoned, but they are one jurisdiction's administrative view, not binding precedent, and the Office itself flags them as technology-dependent. **The input side is genuinely unresolved**: active litigation, divergent legislative approaches, and no stable answer in any major jurisdiction. This entry is written to be useful under uncertainty rather than to predict outcomes, and **it deliberately makes no forecast** about how the training question resolves. Re-check before relying on any specific claim here; this is the fastest-moving topic in the corpus.

---

## Related concepts

- [Data Provenance / Lineage](data-provenance-lineage.md) — the licensing record the input-side question turns on
- [Training Data](training-data.md) — what the model absorbed, and the corpus whose licensing is frequently unknown
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — verbatim reproduction as a demonstrated capability
- [AI Disclosure (Attribution)](ai-disclosure-attribution.md) — saying AI was used, which is a separate question from who owns the result
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — accountability for output does not depend on who owns it
- [Compliance (AI Systems)](compliance-ai-systems.md) — where jurisdiction-specific positions get operationalized
- [Prompt Engineering](prompt-engineering.md) — the activity the Office found insufficient for authorship
- [Synthetic Media (Deepfakes)](synthetic-media-deepfakes.md) — adjacent rights questions around likeness and voice
- [Content Provenance & Watermarking (C2PA)](content-provenance-watermarking.md) — the record of what was machine-made, useful evidence in an ownership dispute
- [Local LLMs](local-llms.md) — open weights say nothing about training-data licensing
- [Ownership (AI Systems)](ownership-ai-systems.md) — governance ownership, a different sense of the word entirely

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-208 | United States Copyright Office — *Copyright and Artificial Intelligence, Part 2: Copyrightability* (January 2025) · [link](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf) | The output-side position: prompts alone do not confer authorship; wholly AI-generated material is not copyrightable; human expressive inputs, arrangement and modification can be, case by case. ⚠️ US only, administrative not judicial, explicitly technology-dependent. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | That the licensing status of widely used corpora is frequently unknown or wrong — license omission above 70%, error rates above 50%. |
| SRC-150 | Carlini, N.; Tramer, F.; Wallace, E.; Jagielski, M. et al. — *Extracting Training Data from Large Language Models* (2021) · [link](https://arxiv.org/abs/2012.07805) | Verbatim reproduction of training data as a demonstrated capability — the output-side reproduction risk, independent of how the training question resolves. |
| SRC-161 | Nasr, M.; Carlini, N.; Hayase, J.; Jagielski, M. et al. — *Scalable Extraction of Training Data from (Production) Language Models* (2023) · [link](https://arxiv.org/abs/2311.17035) | That alignment does not eliminate memorization, and extraction scales against production systems. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The EU's copyright-policy and training-content-summary duties on general-purpose model providers — a different regulatory approach from the US position. |
| SRC-199 | Gebru, T. et al. — *Datasheets for Datasets* (CACM 64(12), 2021) · [link](https://doi.org/10.1145/3458723) | The documentation practice that makes licensing answerable rather than investigable. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Record the human contribution as you work — it is the one thing under your control that improves the position, and it cannot be reconstructed convincingly afterwards. |
| **Organizational** | You likely hold weaker rights in AI output than assumed and carry more reproduction exposure than assumed; both errors run the same way. Get a jurisdiction-specific, dated position. |
| **Client-facing** | Explains why deliverables distinguish AI-assisted from AI-generated, and why "who owns this?" has a real answer in some places and no settled answer in others. |
| **LLM-native** | Prompting is instruction, not expression — that is the Office's reasoning, and it is why prompt sophistication does not convert into authorship. |

---

*Last updated: v1.0 · August 2026*
