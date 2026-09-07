<!--meta
category: Knowledge & Memory
short: The agreed list of what kinds of things exist and how they may relate — a schema that quietly decides what a system can never record
aliases: [ontologies, OWL, semantic model, domain model, taxonomy, controlled vocabulary, schema, classes and relations, what can the system represent]
tags: [Data Governance, Architecture, AI Literacy]
established: established
-->
# Ontology

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
A formal, shared specification of the kinds of things that exist in a domain and the relationships they may have — the schema that decides what a system is able to record, and therefore what it can never say.

---

## Technical definition

Gruber's 1993 formulation remains the canonical one: *"A specification of a representational vocabulary for a shared domain of discourse — definitions of classes, relations, functions, and other objects — is called an ontology."* The paper is also the origin of the widely-repeated short form, *a specification of a conceptualization*.

The computing sense is standardized rather than merely conventional. **OWL 2 is a W3C Recommendation** (2012), and it describes ontologies as *"formalized vocabularies of terms, often covering a specific domain and shared by a community of users"*, providing *"classes, properties, individuals, and data values"*.

**The distinction that does the work here is schema versus instance.** An ontology says what *kinds* of things can exist and how they may be related; a [knowledge graph](knowledge-graphs.md) holds the things that actually do. You can build a graph with no formal ontology — loose triples, no constraints — and you can specify an ontology that nothing has yet populated. **They are different layers, and the wiki previously treated the second as covering the first.**

**There is a ladder, and conflating its rungs is the most common error in practice.** A **controlled vocabulary** fixes the permitted terms. A **taxonomy** adds hierarchy — broader and narrower. An **ontology** adds arbitrary typed relations, constraints on how they may be used, and formal semantics. Requirements documents routinely use all three words for whichever one somebody meant.

**Formal semantics buys inference, and inference is where the governance surface opens.** OWL reasoners answer *class consistency, subsumption and instance retrieval* queries — meaning **the system can assert things nobody wrote down.** If the ontology says every `Supplier` is an `Organization` and every `Organization` has a `jurisdiction`, facts follow that no one typed. Those derived assertions sit alongside stated ones and are, by default, indistinguishable from them ([data provenance](data-provenance-lineage.md)).

**And the expressiveness of the schema bounds what the system can ever record.** A category absent from the ontology is not merely undocumented — it is *unsayable*: there is no field for it, no query that returns it, and no way to measure it later. **That makes an ontology a policy artifact wearing technical clothing**, and it connects directly to measurement: what cannot be represented cannot be counted, audited, or shown to be unequal ([bias](bias-ai-systems.md)).

**Its characteristic cost is ossification.** An ontology is expensive to change once systems depend on it, so early modeling choices persist long past the understanding that produced them.

---

## Plain-language version

If a knowledge graph is a set of filled-in forms, the ontology is the form's design: which boxes exist, what may go in each, and which boxes are allowed to point at which others.

That sounds like paperwork. It is actually a decision about what your organization can say. **If the form has no box for something, that thing cannot be recorded** — and a year later, nobody can ask about it either, because the data was never captured. The absence does not look like a decision. It looks like the question was never relevant.

There is a second thing worth understanding. Because the design is formal, software can draw conclusions from it. Say suppliers are a kind of organization, and every organization has a home country, and the system will conclude that a supplier has a home country without anyone entering it. That is useful, and it means **some of what the system "knows" was never stated by a person.** Unless those inferred facts are marked as inferred, they look identical to the ones somebody checked.

Three words get used interchangeably and mean different things. A *controlled vocabulary* is an approved word list. A *taxonomy* arranges things into broader and narrower groups. An *ontology* does both and adds rules about how things may relate, precisely enough for software to reason over them.

The honest catch: ontologies are hard to change once anything depends on them. So the choices made early — by whoever happened to be modeling — tend to outlive the reasons for them.

---

## AI literacy notes

1. **Schema, not data.** The ontology says what kinds of things can exist; the knowledge graph holds the ones that do.
2. **A missing category is unsayable, not just undocumented** — no field, no query, no later measurement.
3. **It is a policy artifact.** Deciding the class list is deciding what your organization can assert.
4. **Formal semantics permit inference**, so a system can hold facts nobody entered.
5. **Inferred and asserted facts look identical** unless something deliberately distinguishes them.
6. **Controlled vocabulary ≠ taxonomy ≠ ontology** — increasing expressiveness, increasing cost, routinely conflated.
7. **Ontologies ossify.** Early choices outlive their rationale because changing them breaks dependents.
8. **The computing sense is standardized** (W3C), which is what separates it from the philosophical sense sharing the word.

---

## Governance notes

**Core question:** What does our ontology make it impossible to record — and who decided that, on what authority?

**Watch for:**
- A class list authored by data modelers or a vendor, never reviewed by anyone accountable for the domain it describes
- Inferred assertions stored indistinguishably from stated ones, so provenance is lost at the point of reasoning ([data provenance](data-provenance-lineage.md))
- Protected attributes, harm categories or exception cases absent from the schema, making them permanently unmeasurable ([bias](bias-ai-systems.md))
- A vendor-supplied ontology adopted wholesale, importing its categories and its assumptions with it
- "Glossary", "taxonomy" and "ontology" used interchangeably in requirements, so nobody knows which was actually built
- Ontology changes made without knowing which systems consume it ([data quality](data-quality.md))
- Reasoning enabled with no one having checked what it will conclude, or what happens when it concludes something false
- An owner named for the data but not for the schema — the more consequential of the two
- Categories that encode a contested judgment as though it were a fact of the world

**Practice:**
- **Treat the ontology as a governed artifact**: named owner, version, change process, and a review that includes the people accountable for the domain rather than only the modelers
- **Record what was deliberately excluded and why.** An absence is a decision, and it is the only part of the schema that leaves no trace
- **Mark inferred assertions as inferred**, in storage and in any export, so a derived fact never masquerades as a stated one
- Test the schema against the questions you expect to be asked *later* — including the awkward ones — before adopting it
- Know your downstream consumers before changing anything; ossification is a consequence of dependents, not of the format
- Where a vendor ontology is adopted, review its class list as you would review a policy document ([model card / system card](model-card-system-card.md))
- Say which rung of the ladder you actually need — a controlled vocabulary is often enough and vastly cheaper

**Key accountability owner:** whoever owns the domain the ontology describes — because the class list is a claim about what exists in that domain and what may be said about it, and it is routinely written by people who were never asked to make that call and would not have accepted it if asked.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the concept, medium on AI-era practice.** The definition is canonical and heavily cited, the computing sense is fixed by a W3C Recommendation, and the ladder from controlled vocabulary to ontology is standard data-management material. **Weaker ground is how ontologies interact with current AI systems:** whether LLM-based systems should consume formal ontologies, generate them, or route around them entirely is unsettled and moving, and this entry deliberately makes no claim about which wins. **The governance argument — that a schema bounds what can later be measured — is a structural consequence rather than a measured finding**, and no study is cited for how often organizations discover the limit too late, because none was found. It is offered as a question to ask before adopting a schema, not as a documented failure rate.

---

## Related concepts

- [Knowledge Graphs](knowledge-graphs.md) — the instance data this is the schema for; the two are layers, not synonyms
- [Data Quality](data-quality.md) — what conformance to a schema does and does not guarantee
- [Domain](domain.md) — the bounded subject an ontology is written for
- [Knowledge Base](knowledge-base.md) — curated content, as against a formal specification of structure
- [Data Provenance & Lineage](data-provenance-lineage.md) — the distinction inference erases if nothing preserves it
- [Bias (AI Systems)](bias-ai-systems.md) — categories bound what can be measured, and therefore what inequality can be shown
- [Embeddings](embeddings.md) — meaning as learned proximity, the opposite approach to declared structure
- [Retrieval-Augmented Generation (RAG)](rag.md) — where graphs and ontologies are increasingly combined with retrieval
- [AI Governance](ai-governance.md) — where a schema decision should be reviewed, and rarely is
- [Model Card / System Card](model-card-system-card.md) — the disclosure surface for an adopted vendor schema

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-274 | Gruber, Thomas R. — *A translation approach to portable ontology specifications* (Knowledge Acquisition 5(2), pp. 199–220, June 1993) · [link](https://doi.org/10.1006/knac.1993.1008) | The canonical definition, quoted verbatim from the author's own hosted copy: a specification of a representational vocabulary for a shared domain of discourse — definitions of classes, relations, functions and other objects. Also the origin of the widely-repeated short form, *a specification of a conceptualization*. Metadata verified via Crossref. |
| SRC-275 | World Wide Web Consortium (W3C) — *OWL 2 Web Ontology Language Document Overview (Second Edition)* (W3C Recommendation, 11 December 2012) · [link](https://www.w3.org/TR/owl2-overview/) | The standardization that separates the computing sense from the philosophical one: ontologies as formalized vocabularies of terms shared by a community, providing classes, properties, individuals and data values. Source for reasoners answering class consistency, subsumption and instance retrieval queries — the basis of this entry's inference argument. Wording verified against the raw specification, not a summary. |
| SRC-241 | Hogan, A.; Blomqvist, E.; Cochez, M.; d'Amato, C.; de Melo, G.; Gutiérrez, C.; Navigli, R.; Staab, S. et al. — *Knowledge Graphs* (ACM Computing Surveys, 2021) · [link](https://arxiv.org/abs/2003.02320) | The survey treatment of schema and identity as distinct roles within graph knowledge representation — the schema/instance separation this entry is built on. |
| SRC-025 | DAMA International — *DAMA-DMBOK: Data Management Body of Knowledge* (2nd ed.) · [link](https://www.dama.org/cpages/body-of-knowledge) | The data-management framing of the vocabulary/taxonomy/ontology ladder, and of schema as a governed artifact with an owner rather than a technical detail. |
| SRC-121 | Schwartz, R.; Vassilev, A.; Greene, K.; Perine, L.; Burt, A.; Hall, P. (NIST) — *Towards a Standard for Identifying and Managing Bias in Artificial Intelligence* (NIST SP 1270, 2022) · [link](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf) | Support for the measurement consequence: category and representation choices made upstream determine what can later be observed and evaluated, which is why an absent class is not a neutral omission. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Version the schema, name its owner, mark inferred assertions as inferred, and test the model against the awkward questions before adopting it. |
| **Organizational** | The class list is a claim about what exists in your domain and what may be said about it — usually written by people never asked to make that call. What is absent from it becomes permanently unmeasurable. |
| **Client-facing** | Explains why a system cannot answer a reasonable question — the category was never in the model — without it sounding like an excuse. |
| **LLM-native** | Ontology is the schema, the knowledge graph is the instances. Formal semantics buy inference, so the store holds facts nobody wrote, indistinguishable from the ones somebody checked. |

---

*Last updated: v1.0 · September 2026*
