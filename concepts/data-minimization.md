# Data Minimization

## One-line essence
Only giving the AI the data it actually needs — nothing extra. Less data means less risk of privacy problems, lower cost, and a more focused system.

---

## Technical definition

Data minimization is the principle that a system should collect, process, and retain only the personal data that is adequate, relevant, and limited to what is necessary for a specified purpose. It is codified in GDPR Article 5(1)(c) and is one of the foundational data-protection principles. Minimization operates along several axes: collection (don't gather what you don't need), granularity (collect at the coarsest resolution that serves the purpose), retention (delete when the purpose is fulfilled), and access (expose data only to the processes and people that require it).

In AI systems the principle is in structural tension with the prevailing "more data is better" engineering instinct. The EU AI Act's data-governance provisions extend minimization-adjacent obligations to training and operational data for high-risk systems. Crucially, minimization is not always free: empirical work shows that reducing data can leave aggregate model performance largely intact while disparately degrading performance for some user groups (Biega et al. 2020) — so minimization decisions are themselves subject to fairness scrutiny.

---

## Plain-language version

Data minimization means: don't give the AI — or the company running it — more personal information than the job actually requires. If a system only needs your age range, don't give it your birth date. If it only needs data for a month, don't keep it for a year.

The logic is simple risk math. Data you never collected can't leak, can't be subpoenaed, can't be misused, and doesn't cost anything to secure. Every extra field and every extra month of retention is a liability you're choosing to carry. Minimization is the discipline of carrying as little as possible.

It runs against the instinct of modern AI, which is "collect everything, you might need it later." Minimization says: justify what you collect, against a specific purpose, now.

---

## AI literacy notes

1. **Minimization is a default, not an afterthought.** The principle is "necessary for a stated purpose" — which means you need the purpose first, then the data. "We might find a use for it" is precisely the reasoning the principle exists to block.
2. **Less data is often a feature, not a sacrifice.** Smaller, purpose-scoped datasets reduce attack surface, lower storage and compute cost, simplify compliance, and frequently improve model focus. Minimization and performance are not always opposed.
3. **But minimization can have distributional effects.** Cutting data can hurt some user groups more than others (sparse-data users, minorities). Minimization decisions should be checked for disparate impact, not assumed neutral (Biega et al. 2020).

---

## Governance notes

**Core question:** For each piece of personal data this system collects or retains, can you state the specific purpose it serves — and the date it will be deleted?

**Watch for:**
- Data collected "in case it's useful later"
- Indefinite retention with no deletion criteria
- Prompt/inference logs quietly accumulating personal data
- Training corpora assembled by maximal scraping rather than purpose scoping
- Access not scoped to need

**Practice:**
- Define purpose before collection; set retention limits with automated deletion
- Scope access to need
- Review minimization decisions for disparate impact on sparse-data groups
- Treat AI training/RAG/logging data as in-scope for minimization, not exempt from it

**Key accountability owner:** the data/privacy owner for the system is accountable for purpose specification, retention limits, and the disparate-impact check.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established (legal), developing (AI practice).** The principle is settled law under GDPR Article 5(1)(c) and echoed across global privacy regimes. Its application to large-scale AI training — where data appetite is enormous and purpose specification is loose — is an active and contested area. The fairness implications of minimization are documented but not yet standardized in practice (Biega et al. 2020).

---

## Related concepts

- [Data Quality](data-quality.md) — minimization and quality are complementary disciplines on the same input data: collect less, but ensure what you collect is fit for use
- [Grounding](grounding.md) — RAG corpora and retrieval indexes are data-collection decisions that fall within minimization scope
- [AI Governance](ai-governance.md) — minimization is a governance obligation, enforced through retention and access policy
- [Compliance (AI Systems)](compliance-ai-systems.md) — minimization is a binding GDPR requirement, not just good practice
- [Bias (AI Systems)](bias-ai-systems.md) — minimization choices can disparately affect groups, making them a fairness concern
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — accountability for what data is held, and why, stays with the humans operating the system

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-126 | European Union — *GDPR Article 5(1)(c): data 'adequate, relevant and limited to what is necessary'* (Reg. (EU) 2016/679) · [link](https://gdpr-info.eu/art-5-gdpr/) | Primary legal anchor for the data-minimization principle. |
| SRC-127 | Biega, A. et al. — *Operationalizing the Legal Principle of Data Minimization for Personalization* (SIGIR, 2020) · [link](https://arxiv.org/abs/2005.13718) | Peer-reviewed: performance loss from minimization may be modest in aggregate but disparately impacts user groups; minimization as a fairness-relevant choice. |
| SRC-129 | European Parliament — *EU Artificial Intelligence Act* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | Data and data-governance obligations for high-risk AI training and operational data. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Informs schema design, retention policies, feature selection, and access scoping. Minimization is implemented in collection, granularity, retention, and access controls — not in a policy document alone. |
| **Organizational** | The cheapest risk reduction available — data not held cannot be breached. A GDPR compliance requirement and a defensible cost-control argument simultaneously. |
| **Client-facing** | Answers "what data do you take and why?" — and lets you demonstrate that you collect against purpose, not by default. |
| **LLM-native** | Directly relevant to RAG corpora, fine-tuning datasets, and prompt/inference logging — each is a data-collection decision that should be purpose-scoped and retention-bounded. |

---

*Last updated: v1.0 · June 2026*
