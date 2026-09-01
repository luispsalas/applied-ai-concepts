<!--meta
category: Observability & Governance
short: The rights and obligations that govern how personal data is used in AI training and deployment — and the responsibility to uphold them
aliases: [GDPR, personal data, data protection, PII, privacy compliance]
tags: [Privacy, Regulatory]
-->
# Privacy (AI Systems)

## One-line essence
The rights and obligations that govern how personal data is used in AI training and deployment — and the organizational responsibility to uphold them.

---

## Technical definition

Privacy in AI systems concerns what personal data is collected, processed, retained, and potentially exposed across the AI lifecycle — training, fine-tuning, retrieval, logging, and generation. It intersects with but is not identical to [Data Minimization](data-minimization.md): minimization governs how much data is collected; privacy governs the fuller set of obligations around consent, purpose, retention, and an individual's rights over their own data (GDPR Art. 5(1)(c) plus the broader regulation — SRC-126, SRC-039). AI introduces privacy risks with no equivalent in traditional data systems: models can memorize and later regurgitate verbatim fragments of their training data, including personally identifiable information, when queried in the right way (SRC-150) — a risk that scales with model size. Regulatory frameworks are actively extending to cover this: NIST's Privacy Framework update addresses AI-specific privacy risk across the AI lifecycle in general terms (SRC-151, an unfinalized draft as of publication — see Sources for details).

---

## Plain-language version

Privacy asks: what personal information does this AI system touch, and what happens to it? That's bigger than just "how much data did you collect" (that's Data Minimization) — it also covers whether people agreed to it, how long it's kept, and whether it can come back to bite them. AI has a genuinely new privacy problem: a model trained on text can sometimes be coaxed into repeating exact snippets of that training data back to you — including things like real names, phone numbers, or emails that were in there, even though nobody meant for the AI to memorize them.

---

## AI literacy notes

1. **Privacy is broader than minimization.** Minimization is one privacy discipline (collect less); privacy overall also covers consent, purpose limitation, retention, and rights of access/deletion (see [Data Minimization](data-minimization.md)).
2. **Models can memorize and leak training data verbatim.** This is a distinct AI-specific privacy risk — not hypothetical: demonstrated at scale, and larger models are more prone to it (SRC-150).
3. **Privacy risk doesn't stop at training.** Prompts, retrieved documents, conversation logs, and fine-tuning data can all carry personal information that needs the same discipline as the original training corpus.
4. **Regulation is actively catching up.** Existing privacy law (GDPR) already applies to AI systems; frameworks like NIST's are being updated specifically to address AI-era privacy risk, meaning the compliance bar is still moving.

---

## Governance notes

**Core question:** What personal data does this system touch across its full lifecycle — training, retrieval, logging — and who is accountable for it?

**Watch for:**
- Privacy treated as solved by data minimization alone
- Training/fine-tuning data not screened for personal information
- Logs and retrieval corpora accumulating personal data outside formal privacy review

**Practice:**
- Extend privacy review to training data, retrieval corpora, and logs, not just the point of user input
- Monitor for training-data memorization risk in deployed models
- Track evolving AI-specific privacy guidance (e.g. NIST) alongside existing law (GDPR)

**Key accountability owner:** the privacy officer, with the system owner for AI-specific implementation.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High for the underlying privacy principles** (well-established in law and practice); **Medium for AI-specific instantiation** — training-data memorization is empirically demonstrated, but frameworks and mitigations specific to AI privacy risk are still being formalized.

---

## Related concepts

- [Data Minimization](data-minimization.md) — the collection-side discipline that is one part of a full privacy program
- [AI Governance](ai-governance.md) — privacy obligations are one of the regulatory pillars governance structures must satisfy
- [Compliance (AI Systems)](compliance-ai-systems.md) — privacy law (GDPR and successors) is a binding compliance requirement, not optional practice
- [Audit Trail (AI)](audit-trail-ai.md) — knowing what personal data was processed and when depends on a working audit trail
- [Memory (AI Systems)](memory-ai-systems.md) — persistent memory is where privacy risk concentrates over time
- [AI Use Case](ai-use-case.md) — privacy risk should be assessed per use case, since the personal data involved varies by application

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-150 | Carlini, N. et al. — *Extracting Training Data from Large Language Models* (USENIX Security, 2021) · [link](https://arxiv.org/abs/2012.07805) | LLMs memorize and can regurgitate verbatim training data including PII; risk scales with model size. |
| SRC-126 | European Union — *GDPR Article 5(1)(c): Data Minimisation* (Reg. (EU) 2016/679) · [link](https://gdpr-info.eu/art-5-gdpr/) | The collection-side privacy principle already governing AI training/operational data. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation* (2016) · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | The broader regulatory framework AI privacy obligations sit within. |
| SRC-151 | NIST — *Privacy Framework 1.1* (Initial Public Draft, 2025) · [link](https://www.nist.gov/privacy-framework) | Draft framework extending privacy risk management guidance to AI-specific risks across the AI lifecycle. Cited only for its general direction — no section numbers or exact wording are treated as settled. ⚠️ **Unfinalized draft:** public comment closed June 2025; NIST targeted Q4 2025 for final release; still not published as of this entry's publication (July 2026). **Review again** before the next major update of this entry — if a finalized version has shipped, replace this citation and update the entry accordingly. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Privacy review must extend to training data, retrieval corpora, and logs — not just the point of user input. |
| **Organizational** | Privacy risk is broader and newer than most compliance checklists assume; AI-specific guidance is still catching up to the technology. |
| **Client-facing** | Answers "what happens to my data once it's near this AI system?" — including the AI-specific memorization risk most people don't expect. |
| **LLM-native** | Training-data memorization is a risk with no equivalent in traditional software — it exists because of how the model learns, not because of a configuration mistake. |

---

*Last updated: v1.0 · July 2026*
