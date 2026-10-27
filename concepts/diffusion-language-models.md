<!--meta
category: Foundations
short: Language models that write by refining a whole draft in parallel over several steps, instead of producing one token after another
aliases: [diffusion LLM, DLM, dLLM, diffusion-based language model, masked diffusion language model, discrete diffusion, text diffusion, non-autoregressive generation, LLaDA, Mercury]
tags: [Architecture, Safety, Model Behavior]
established: established
-->
[Applied AI Concepts](../README.md) › [Foundations](../glossary/categories.md#foundations) › Diffusion Language Models

# Diffusion Language Models

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Language models that write by refining a whole draft in parallel over several steps, instead of producing one token after another. They can be much faster, and their safety behavior differs from the models most safeguards were built for.

---

## Technical definition

Most [large language models](large-language-models.md) are autoregressive: they produce text one token at a time, left to right, each token conditioned on everything before it. A diffusion language model works differently. It starts from a draft that is pure noise, either a sequence of masked positions or random vectors, and improves every position at once over a series of steps until readable text emerges. A 2025 survey describes these models as *"generating tokens in parallel through an iterative denoising process"*. The idea comes from the diffusion models behind image generators, adapted to text.

**Two families.** The *continuous* family turns text into vectors and removes noise from them: Diffusion-LM (2022) denoises random vectors into word vectors, and its intermediate states let a simple gradient-based method steer fine-grained properties such as sentence structure. The *discrete* or *masked* family works on tokens directly. Austin et al. (2021) showed that corrupting text by masking tokens draws *"a connection between diffusion models and autoregressive and mask-based generative models."* Building on that, Sahoo et al. (2024) reduced the training objective to *"a mixture of classical masked language modeling losses"* and reported masked diffusion models that approach autoregressive quality on standard language-modeling measures.

**At scale, and in products.** LLaDA (2025) trained a masked diffusion model at 8 billion parameters with the usual pre-training and fine-tuning, and reported it competitive with LLaMA3 8B at in-context learning, with instruction following shown in case studies after fine-tuning. The authors also report that it *"addresses the reversal curse, surpassing GPT-4o in a reversal poem completion task"*, a task that trips models which only read forward. Inception Labs offers Mercury, a commercial diffusion model for code. Its report gives throughputs of 1,109 and 737 tokens per second for two sizes on NVIDIA H100 GPUs, measured by the independent evaluator Artificial Analysis, and up to ten times the speed of speed-optimized frontier models at comparable quality. Those are a vendor's figures for its own product, and speed depends on hardware and setup.

**The trade-offs.** Speed comes from producing many tokens per step, so it falls when more steps are needed. A 2026 paper proposing an alternative states that diffusion models *"degrade quickly with fewer sampling steps, process the full sequence at every step, and require many passes over the dataset to reach good quality."* The 2025 survey lists efficiency, long sequences and infrastructure among the open problems.

**Related approaches that also move above the single token.** Other recent work changes the unit of generation without, or alongside, diffusion. Next Concept Prediction (2026) adds a prediction of multi-token "concepts" to ordinary next-token training. Meta's Large Concept Models (2024) predict whole sentences as embeddings, exploring diffusion-based variants among other approaches. Next-Concept Modeling (2026) generates a hierarchy of compressed codes from coarse to fine and reports quality comparable to the strongest diffusion model at 10 to 31 times the speed. The word "concept" means a different thing in each, which is why this wiki records these as approaches rather than as terms of their own.

**Not to be confused with "AI diffusion".** In policy writing, *diffusion* also means the spread of a technology, as in AI adoption or export controls on AI. This entry is about a way of building language models and has nothing to do with that sense.

**Why this matters for governance.** Safety work on language models assumed text arrives left to right. Diffusion models break that assumption, and early research shows their safety behavior is different, though not uniformly worse. Yamabe and Sakuma (2025) found that if an affirmative token for a harmful request appears at an intermediate step, *"subsequent denoising can be steered toward a harmful response even in aligned models"*, bypassing the safety training. Rahimi et al. (2026) found the opposite tendency elsewhere: *"diffusion remasking can promote recovery from harmful intermediate generations"*, and switching the same model from autoregressive to diffusion sampling improved its resistance to [jailbreaks](jailbreak.md). Both are preprints. Read together, they say a diffusion model's safety has to be tested as a diffusion model, with the controls built for it.

---

## Plain-language version

Most AI chat models write the way people type: one word after another, left to right. A diffusion language model works more like a photo coming into focus. It starts with a page of blanks and fills in and corrects the whole thing over several passes until the text is finished.

That has two practical effects. It can be much faster, because it works on many words at once; one commercial model reports speeds several times higher than conventional fast models. And because it sees the whole draft at every pass, it can handle some tasks that trip up left-to-right models, such as completing a poem in reverse.

The catch is that a great deal of AI safety practice assumes text arrives in order. Filters that watch words as they stream out, and safety training designed around left-to-right writing, do not automatically carry over. Early research found one weakness specific to these models and one way they are actually more resistant to attack. The honest summary is that their safety has to be checked on its own terms.

---

## AI literacy notes

1. **Not every language model writes left to right.** Diffusion models refine a whole draft in parallel, so "the model predicts the next word" is no longer a universal description.
2. **Faster comes from parallelism, and it has limits.** Speed falls when quality needs more refinement steps, and vendor speed figures depend on the hardware they were measured on.
3. **Two families sit under one name:** continuous models that denoise vectors, and masked models that fill in hidden tokens. LLaDA, the largest open model discussed here, is of the masked kind.
4. **Their safety behavior is different, not simply better or worse.** One study found a new way to steer them toward harm; another found they recover from harmful drafts more often than left-to-right models.
5. **Comparisons need care.** Claims of parity with autoregressive models often rest on the authors' own baselines and on measures that differ between the two kinds of model.
6. **"Diffusion" is overloaded.** In policy writing it also means the spread of AI technology. Check which sense a document means.
7. **"Concept" models are a separate, unsettled area.** Several 2024–2026 approaches generate above the level of single tokens, and each uses "concept" to mean something different.

---

## Governance notes

**Core question:** If a model in your stack generates text in parallel rather than left to right, which of your safeguards assume the opposite, and have they been tested against this kind of model?

**Watch for:**
- Output filters, stop rules and [guardrails](guardrails-ai-systems.md) that act on text as it streams, applied to a model whose output is not produced in reading order (this entry's reasoning from the mechanism; no study cited here tests it directly)
- Safety evaluations and red-team results from autoregressive models carried over to a diffusion model without retesting
- Vendor speed or quality claims adopted without the hardware, settings and benchmark they were measured under ([AI benchmarking](ai-benchmarking.md))
- Parity claims with autoregressive models that rest on the authors' own baselines
- Intermediate drafts treated as harmless because they are never shown, when research shows they can steer the final output
- Documents that use "diffusion" without making clear whether they mean the model architecture or the spread of AI technology

**Practice:**
- **Record the generation method of every model you deploy**, alongside its version, so safeguards can be matched to it ([model version and update](model-version-update.md))
- Re-run jailbreak and refusal testing on any diffusion model before deployment, including attacks that target intermediate steps ([red teaming](red-teaming.md))
- Apply output checks to the finished text as well as, or instead of, the stream
- Evaluate speed and quality on your own workload and hardware before relying on published figures ([latency](latency-ai-systems.md), [evaluation](evaluation.md))
- Treat safety findings for this model class as provisional: the evidence is recent, mostly preprints, and points in more than one direction

**Key accountability owner:** whoever owns model selection and its safety sign-off, because the change is in how the model generates, which no prompt or policy setting can see.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High on what the term means; medium on how the models compare.** The definition, the two families and the link to masked language modeling are established in peer-reviewed work and a 2025 survey. **Comparisons with autoregressive models are still moving**: parity claims come largely from the authors of each model, the speed figures cited are a vendor's, and the trade-offs depend on the number of refinement steps. **The safety findings are early and partly contradictory**, from preprints in 2025 and 2026, so this entry reports both directions rather than a verdict. The claim about streaming filters is reasoning from the mechanism, labeled as such. The venues of three foundational papers were confirmed through one bibliographic index only.

---

## Related concepts

- [Large Language Models](large-language-models.md) — the autoregressive default this approach departs from
- [Transformers](transformers.md) — the network inside both kinds of model
- [Inference](inference.md) — where the speed difference appears
- [Latency (AI Systems)](latency-ai-systems.md) — the property diffusion models mainly improve
- [Tokenization](tokenization.md) — the units both kinds of model work with
- [Jailbreak](jailbreak.md) — attacks whose behavior changes with the generation method
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — safeguards that may assume left-to-right output
- [AI Benchmarking](ai-benchmarking.md) — why cross-paradigm comparisons need care
- [Recurrent Depth](recurrent-depth.md) — another architecture that changes how a model spends computation

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-444 | Li, T.; Chen, M.; Guo, B.; Shen, Z. — *A Survey on Diffusion Language Models* (2025) · [link](https://arxiv.org/abs/2508.10875) | The quoted definition, the contrast with autoregressive models, and the open problems. ⚠️ Preprint survey. |
| SRC-440 | Austin, J.; Johnson, D.D.; Ho, J.; Tarlow, D.; van den Berg, R. — *Structured Denoising Diffusion Models in Discrete State-Spaces* (2021) · [link](https://arxiv.org/abs/2107.03006) | Diffusion for discrete data, and the link between masking-based corruption and masked language modeling. |
| SRC-441 | Li, X.L.; Thickstun, J.; Gulrajani, I.; Liang, P.; Hashimoto, T.B. — *Diffusion-LM Improves Controllable Text Generation* (NeurIPS 2022) · [link](https://arxiv.org/abs/2205.14217) | The continuous family and gradient-based control of fine-grained properties. |
| SRC-442 | Sahoo, S.S.; Arriola, M.; Schiff, Y.; Gokaslan, A.; Marroquin, E.; Chiu, J.T. et al. — *Simple and Effective Masked Diffusion Language Models* (NeurIPS 2024) · [link](https://arxiv.org/abs/2406.07524) | The quoted masked-language-modeling objective, and masked diffusion approaching autoregressive quality. |
| SRC-443 | Nie, S.; Zhu, F.; You, Z.; Zhang, X.; Ou, J.; Hu, J. et al. — *Large Language Diffusion Models* (NeurIPS 2025) · [link](https://arxiv.org/abs/2502.09992) | LLaDA at 8 billion parameters, competitive with LLaMA3 8B at in-context learning, and the reversal task. ⚠️ Comparisons partly against the authors' own baselines. |
| SRC-445 | Inception Labs; Khanna, S.; Kharbanda, S.; Li, S.; Varma, H.; Wang, E. et al. — *Mercury: Ultra-Fast Language Models Based on Diffusion* (2025) · [link](https://arxiv.org/abs/2506.17298) | A commercial diffusion model and its reported throughput. ⚠️ Vendor-authored; speed depends on hardware. |
| SRC-448 | Kumbong, H.; Khare, I.S.; Mlauzi, I.; Woen, A.; Ding, C.; Buchanan, E.K. et al. — *Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation* (2026) · [link](https://arxiv.org/abs/2610.14162) | The quoted weaknesses of diffusion models, and coarse-to-fine generation as an alternative. ⚠️ Preprint. |
| SRC-450 | Liu, Y.; Song, Y.; Wang, Y.; Ge, K.; Lamb, A.; Guo, Q. et al. — *Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models* (2026) · [link](https://arxiv.org/abs/2602.08984) | Concept-level prediction added to next-token training, as a related approach. ⚠️ Preprint. |
| SRC-449 | LCM team (Meta); Barrault, L.; Duquenne, P.-A.; Elbayad, M.; Kozhevnikov, A.; Alastruey, B. et al. — *Large Concept Models: Language Modeling in a Sentence Representation Space* (2024) · [link](https://arxiv.org/abs/2412.08821) | Generation at the level of sentence embeddings, including diffusion-based variants, as a related approach. |
| SRC-446 | Yamabe, S.; Sakuma, J. — *Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability* (2025) · [link](https://arxiv.org/abs/2510.00565) | The quoted priming vulnerability: intermediate tokens steering an aligned model toward harm. ⚠️ Preprint. |
| SRC-447 | Rahimi, E.; Hirshel, E.; Himelstein, R.; LeVi, A.; Mendelson, A.; Baskin, C. — *Step-Wise Refusal Dynamics in Autoregressive and Diffusion Language Models* (2026) · [link](https://arxiv.org/abs/2602.02600) | The quoted recovery from harmful drafts, and better jailbreak resistance under diffusion sampling. ⚠️ Preprint. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Record which generation method each model uses, and retest safety and speed for diffusion models on your own workload rather than inheriting autoregressive results. |
| **Organizational** | A faster model class with different safety behavior. Model selection now includes the generation method, and safety sign-off has to cover it. |
| **Client-facing** | Explains why a model can be much faster without being bigger, and why that speed comes with safety checks of its own. |
| **LLM-native** | Parallel iterative denoising instead of next-token prediction: two families (continuous, masked), real speed gains, and safety behavior that early research finds different in both directions. |

---

*Last updated: v1.0 · October 2026*
