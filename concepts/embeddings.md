<!--meta
category: System Architecture
short: Turning text into coordinates so that similar meanings sit close together — the representation that makes semantic search work, and that carries the training data's biases as geometry
aliases: [vector embeddings, word embeddings, sentence embeddings, vectors, vector search, semantic search, word2vec, vector database, latent space]
tags: [Architecture, AI Literacy]
established: established
-->
# Embeddings

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Representing text as points in a high-dimensional space arranged so that related meanings land near each other — the layer that makes semantic retrieval possible, and that encodes whatever associations its training data contained as measurable direction.

---

## Technical definition

An embedding is a **dense vector of real numbers** standing in for a piece of text — a token, a sentence, a document. The defining property is that **geometric proximity approximates semantic relatedness**: texts about similar things produce vectors close together, usually measured by cosine similarity.

The representations are learned, not designed. Mikolov et al. (2013) showed that useful word vectors could be trained cheaply at scale — *"less than a day to learn high quality word vectors from a 1.6 billion words data set"* — reaching state-of-the-art on measures of *"syntactic and semantic word similarities."* Cheapness is the historically important part: it moved distributed representations from a research technique to default infrastructure.

**Word-level embeddings are not enough for retrieval, and the gap was practical rather than theoretical.** Comparing sentences with a full transformer means running the model on every pair. Reimers & Gurevych (EMNLP 2019) quantified the wall: *"Finding the most similar pair in a collection of 10,000 sentences requires about 50 million inference computations (~65 hours) with BERT."* Their sentence-embedding approach produces one vector per sentence that can be compared by cosine similarity, cutting the same task *"to about 5 seconds ... while maintaining the accuracy from BERT."* **That result is why semantic search over a corpus is feasible at all**, and therefore why [RAG](rag.md) exists as an architecture.

**What the geometry does and does not encode.** Similarity is the only relation the space represents. It has no notion of truth, authority, recency, or permission. A false statement and its correction sit close together because they are *about* the same thing — which is a feature for retrieval and a hazard for anything that treats retrieval rank as a judgment of quality.

**Bias in embeddings is structural, not incidental.** Bolukbasi et al. (NIPS 2016) found that embeddings trained on Google News *"exhibit female/male gender stereotypes to a disturbing extent"* and — the load-bearing finding — that such bias operates as *"a direction in the word embedding."* Two things follow. It is **measurable**, because a direction can be computed and projected onto. And it is **inherited and propagated**: the authors warn that widespread use *"tends to amplify these biases"* in every downstream system built on the representation. Debiasing methods exist and reduce the effect while preserving useful structure; they are mitigations applied to a specific measured axis, not a general solution.

---

## Plain-language version

Computers compare numbers, not meanings. An embedding is the trick that bridges the two: every piece of text gets converted into a long list of numbers — coordinates — arranged so that texts about similar things end up near each other.

Once meaning is coordinates, "find me things related to this" becomes "find the nearest points," which computers do extremely fast. That is the whole basis of semantic search, and the reason a system can retrieve a relevant document without you using the same words the document uses.

The speed matters more than it sounds. Comparing 10,000 sentences with each other the slow way takes roughly **65 hours**. With sentence embeddings it takes about **5 seconds**, at comparable accuracy. That difference is why searching your documents by meaning is a product feature and not a research demo.

Two things to keep in mind. First, closeness means "about the same thing" — not "true," "recent," or "authoritative." A claim and its correction sit right next to each other. Second, the arrangement is learned from human text, so human associations come along with it. Researchers found gender stereotypes sitting in these spaces as a measurable *direction* you can point at. That is unwelcome, but being measurable is the useful part: something you can compute, you can check for.

---

## AI literacy notes

1. **Proximity means relatedness, not correctness.** A false statement and its refutation are close neighbors, because closeness is topical.
2. **The space has no clock and no hierarchy.** Recency, authority and reliability are not represented — they must be added as separate metadata and filters.
3. **Bias is a direction, and therefore measurable — but measurable is not fixable.** The geometric handle makes it auditable; published debiasing methods conceal it rather than remove it.
4. **Downstream systems inherit it.** Anything built on an embedding — search, classification, recommendation, retrieval — carries the representation's associations forward and can amplify them.
5. **Embeddings are derived data, not anonymized data.** They are computed from the source text and retain enough of it to be treated as sensitive when the source was.
6. **Different models produce incompatible spaces.** Vectors from one embedding model cannot be compared with another's; changing the model means re-embedding the whole corpus.
7. **Chunking decides what can be found.** A document split badly produces vectors that represent fragments nobody would search for.
8. **Similarity search always returns something.** There is no natural "no match" — the nearest neighbors of an irrelevant query are simply the least-distant irrelevant items.

---

## Governance notes

**Core question:** Our vector store holds a derived copy of our source material — who may query it, what does it retain, and what is the demonstrated basis for treating retrieval rank as relevance?

**Watch for:**
- A vector database treated as an index rather than as a **data store**, and so excluded from retention, deletion, access-control and [privacy](privacy-ai-systems.md) scope
- Embeddings assumed to be anonymized because they are numbers ([data leakage](data-leakage-ai-systems.md))
- Deletion honored in the source system but not in the derived vectors — the source record removed, the embedding still retrievable ([data minimization](data-minimization.md))
- Retrieval rank presented to users as authority or correctness, when it measures topical proximity
- No recency or provenance filtering over retrieval, on a corpus where staleness matters ([data provenance](data-provenance-lineage.md))
- Embedding-model changes made as an infrastructure upgrade, silently altering what the system retrieves ([model version & update](model-version-update.md))
- Source-document permissions not enforced at retrieval time, so the index becomes a way around access control ([permission model](permission-model-ai.md))
- No measurement of representational [bias](bias-ai-systems.md) in a space used for anything touching people — hiring, ranking, triage

**Practice:**
- **Classify the vector store at the sensitivity of its source material** and put it under the same retention, access and deletion regime
- Propagate deletion into derived vectors, and test that it happens
- Filter and re-rank on metadata — recency, provenance, permission — rather than on distance alone
- Measure bias directly where the application touches people; the geometry makes this tractable, so absence of measurement is a choice
- Treat an embedding-model change as a **system change**: re-embed the corpus, re-baseline retrieval [evaluation](evaluation.md), and version the space
- Enforce document-level permissions at query time, not only at ingestion
- Evaluate retrieval on whether the right material was returned, separately from whether the final answer read well

**Key accountability owner:** the data owner of the *source* corpus — because the vector store is a derivative of their material, and the common failure is that ownership does not follow the data into its embedded form.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High** on the mechanism and its properties: distributed representations are foundational, long-established, and anchored in heavily-cited peer-reviewed work (NIPS 2016; EMNLP 2019), and the speed and bias findings are direct measurements rather than interpretations. **Low on mitigation, and this is a genuine negative result rather than mere uncertainty.** Gonen & Goldberg (NAACL 2019) showed that debiasing methods *"hide the bias, not remove it"* — the information survives in the distances between words and can be recovered — concluding that such techniques *"should not be trusted for providing gender-neutral modeling."* So **treat measurement as reliable and any claim that a space has been debiased as unsupported.** Specific numbers are also implementation-bound: the 65-hours-to-5-seconds comparison is for one model pair on one task size, and illustrates the order of the effect rather than a general constant.

---

## Related concepts

- [RAG (Retrieval-Augmented Generation)](rag.md) — the architecture this representation makes possible
- [Knowledge Base](knowledge-base.md) — what gets embedded, and whose permissions should follow it
- [Tokenization](tokenization.md) — the units that become vectors in the first place
- [Grounding](grounding.md) — retrieval supplies the evidence; proximity alone does not make it correct
- [Bias (AI Systems)](bias-ai-systems.md) — here it is geometric, measurable, and inherited by everything downstream
- [Privacy (AI Systems)](privacy-ai-systems.md) — embeddings are derived data, not anonymized data
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — a vector store is an exfiltration surface like any other copy
- [Memory (AI Systems)](memory-ai-systems.md) — semantic recall is usually embedding lookup underneath
- [Data Provenance & Lineage](data-provenance-lineage.md) — a derived artifact whose lineage is routinely untracked
- [Multimodal AI](multimodal-ai.md) — the shared representation space that lets images and text be compared at all
- [Model Version & Update](model-version-update.md) — changing the embedding model invalidates the existing space
- [Pre-training](pre-training.md) — where the associations in the space come from

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-224 | Mikolov, T.; Chen, K.; Corrado, G.; Dean, J. — *Efficient Estimation of Word Representations in Vector Space* (2013) · [link](https://arxiv.org/abs/1301.3781) | The result that made distributed representations practical infrastructure: high-quality word vectors from a 1.6-billion-word corpus in under a day, with state-of-the-art syntactic and semantic similarity. |
| SRC-225 | Reimers, N.; Gurevych, I. — *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks* (EMNLP, 2019) · [link](https://arxiv.org/abs/1908.10084) | The enabling result for semantic search at corpus scale: pairwise comparison of 10,000 sentences reduced from ~65 hours to ~5 seconds while maintaining BERT-level accuracy. |
| SRC-226 | Bolukbasi, T.; Chang, K.-W.; Zou, J.; Saligrama, V.; Kalai, A. — *Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings* (NIPS, 2016) · [link](https://arxiv.org/abs/1607.06520) | Bias in embeddings is a measurable direction, present "to a disturbing extent" in news-trained vectors, and amplified by widespread downstream use. Also the source of the debiasing-with-caveats position. |
| SRC-227 | Gonen, H.; Goldberg, Y. — *Lipstick on a Pig: Debiasing Methods Cover up Systematic Gender Biases in Word Embeddings But do not Remove Them* (NAACL, 2019) · [link](https://arxiv.org/abs/1903.03862) | The negative result on mitigation: debiasing hides rather than removes bias, which remains recoverable from inter-word distances, and should not be trusted for gender-neutral modeling. |
| SRC-020 | Lewis, P. et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks* (2020) · [link](https://arxiv.org/abs/2005.11401) | The canonical architecture built on this representation layer: dense passage retrieval feeding a generator. |
| SRC-141 | Vaswani, A.; Shazeer, N.; Parmar, N.; Uszkoreit, J.; Jones, L.; Gomez, A.N.; Kaiser, L.; Polosukhin, I. (Google) — *Attention Is All You Need* (2017) · [link](https://arxiv.org/abs/1706.03762) | The architecture in which token embeddings are the input representation, and from which contextual sentence embeddings are derived. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Filter and re-rank on metadata rather than distance alone; enforce source permissions at query time; treat an embedding-model swap as a system change requiring full re-embedding and re-baselined retrieval evaluation. |
| **Organizational** | The vector store is a derived copy of your source material and belongs in the same retention, access and deletion regime. Deletion that does not propagate into it is not deletion. |
| **Client-facing** | Explains how a system finds relevant material without keyword matches — and why "most relevant" means "closest in meaning," not "most reliable." |
| **LLM-native** | Similarity is the only relation the space encodes: no truth, no time, no authority. Bias is a computable direction, which makes it auditable — and makes not auditing it a decision. |

---

*Last updated: v1.0 · September 2026*
