# Data Quality

## One-line essence
The fitness of data for its intended use — and the upstream constraint that determines the reliability of every AI system built on it.

---

## Technical definition

Data quality refers to the degree to which data is fit for the purposes it is used for. It is assessed across multiple dimensions, each measuring a different property of the data relative to its intended use:

- **Accuracy** — data correctly represents the real-world entity or event it describes
- **Completeness** — required data is present; records and fields are not missing
- **Consistency** — data does not contradict itself across systems, records, or time periods
- **Timeliness** — data is current enough for its intended use; not stale relative to the decisions it informs
- **Validity** — data conforms to defined formats, ranges, and business rules
- **Uniqueness** — records are not duplicated across the dataset

In AI systems, data quality operates as a constraint at multiple layers:
- **Training data** — quality determines what the model learns; biases, gaps, and errors in training data become systematic model behaviors
- **Knowledge base / RAG corpus** — quality determines what the retrieval system surfaces; stale or inconsistent documents produce stale or inconsistent answers
- **Context engineering inputs** — structured data injected into prompts carries the same quality requirements as any other data asset

Poor data quality does not merely degrade output quality in proportion — it can introduce systematic errors and biases that are invisible to downstream users, because the model presents outputs with the same fluency regardless of the quality of the underlying data.

---

## Plain-language version

AI systems are built on data. Whatever errors, gaps, inconsistencies, or biases exist in that data will appear in the AI's outputs — often invisibly, and often stated with more confidence than the underlying data deserves.

This is the "garbage in, garbage out" principle extended: data quality isn't just a database concern. It is a constraint on every AI system that uses data — including RAG systems that retrieve from knowledge bases, models trained on organizational datasets, and context-engineered workflows that inject structured information into prompts.

Three data quality failures are especially consequential in AI contexts: outdated data presented as current (timeliness failure), missing records that skew patterns (completeness failure), and inconsistent definitions across systems that produce contradictory signals (consistency failure). None of these announce themselves in the output — the model doesn't know the data is wrong.

---

## AI literacy notes

Data quality is often treated as a data engineering concern — something to solve before AI work begins. In practice, it is a continuous governance responsibility that runs alongside AI deployment.

Three implications:

1. **Data quality problems become model behavior.** Poor training data becomes systematic model error. Poor knowledge base data becomes confidently wrong retrieval. The model doesn't flag data quality problems — it incorporates them into outputs that look indistinguishable from correct ones.
2. **Quality is always relative to use.** Data that is high quality for one purpose may be unfit for another. Assessing data quality requires knowing what the AI system will do with it — not just checking whether data exists and conforms to a schema.
3. **Data quality governance cannot be delegated to the AI.** AI systems can help identify quality issues (anomaly detection, deduplication, completeness checks), but the governing decisions — what counts as accurate, who resolves conflicts, what completeness threshold is acceptable — require human domain knowledge and accountability.

---

## Governance notes

**Core question:** Are data quality requirements defined relative to the AI use case — and is quality monitored continuously, not just assessed at ingestion?

**Watch for:**
- Quality assessed once at ingestion and not revisited: data quality degrades over time as source systems change, business rules evolve, and records become stale. A one-time quality check creates false confidence in data that is continuously changing.
- Quality dimensions evaluated in isolation: high record-level accuracy does not guarantee cross-system consistency. Multi-system AI deployments inherit inconsistencies that single-system checks miss.
- AI systems delegated quality control: AI can surface candidates for review, but the judgment of what "correct" means for a given domain cannot be fully automated. Delegating that decision creates an accountability gap where no human has explicitly accepted responsibility for data fitness.

**Practice:**
- Define data quality requirements by use case: specify which dimensions matter (accuracy, completeness, timeliness, etc.), at what threshold, for the specific AI task. A customer service knowledge base has different requirements than a financial reporting dataset.
- Build quality monitoring into the data pipeline continuously: freshness indicators, completeness metrics, and consistency checks belong in the observability stack alongside model performance metrics — not as a pre-deployment gate that is then forgotten.

**Key accountability owner:** Data quality owner — the role responsible for defining quality standards relative to the AI use case, monitoring quality signals over time, and authorizing data as fit for use in AI systems.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established.** Data quality as a discipline has a stable, canonical framework (DAMA-DMBOK defines the authoritative quality dimensions) with extensive literature and practitioner adoption. Its application as an upstream constraint on AI system reliability is well-understood and increasingly documented in responsible AI and MLOps literature.

---

## Related concepts

- [Retrieval-Augmented Generation (RAG)](rag.md) — knowledge base quality is the upstream constraint on RAG output quality; data quality governance is the control that keeps it current and reliable
- [Persistent Synthesis](persistent-synthesis.md) — the synthesis discipline applied to knowledge maintenance; addresses the same degradation risk (accumulation without governance) from a knowledge management perspective
- [Hallucination](hallucination.md) — poor data quality can produce factually incorrect outputs that are indistinguishable from model-generated hallucinations; both require structural verification
- [Context Engineering](context-engineering.md) — data injected into model context is subject to the same quality requirements as any other data asset; context engineering governs what the model receives
- [Harness Paradigm](harness-paradigm.md) — data access controls and quality monitoring are harness-layer responsibilities; the harness is where data governance meets AI deployment
- Observability (AI Systems) — data quality metrics (freshness, completeness, consistency) are a component of a complete AI observability stack
- Model/Data Drift — the failure mode when data quality degrades silently post-deployment, causing model behavior to shift without a visible trigger

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed., 2017) · [link](https://www.dama.org/cpages/body-of-knowledge) | Canonical framework for data quality dimensions and data management practice. Authoritative definitions for accuracy, completeness, consistency, timeliness, validity, and uniqueness as the standard quality dimension set. Industry reference for data governance roles and responsibilities. |
| — | ⚠️ Source needed | AI-specific framing: data quality as upstream constraint on model and RAG system behavior; quality governance as a continuous responsibility rather than a pre-deployment gate; the "garbage in, garbage out" extension to training data, knowledge bases, and context inputs. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Defines the data requirements that must be met before AI systems can be trusted. Informs knowledge base design, RAG pipeline governance, training data curation, and context injection validation. |
| **Organizational** | The concept that explains why "we have the data" is not sufficient — and why data fitness for purpose, not mere availability, is what determines AI system reliability. Essential for any AI adoption roadmap. |
| **Client-facing** | Answers "why is the AI giving us wrong information about our own products/policies?" — and points to the data, not the model, as the likely root cause. |
| **LLM-native** | The upstream constraint that bounds everything downstream. No context engineering, RAG architecture, or harness design compensates for data that is inaccurate, incomplete, or stale. |

---

*Last updated: v1.0 · May 2026*
