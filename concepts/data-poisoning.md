<!--meta
category: System Architecture
short: Corrupting what a model learns rather than what it is asked. It is an integrity attack on the training set that no amount of input filtering can reach
aliases: [poisoning, training data poisoning, dataset poisoning, backdoor attack, split-view poisoning, frontrunning poisoning, integrity attack]
tags: [Security, Data Governance, Safety]
established: established
-->
[Applied AI Concepts](../README.md) › [System Architecture](../glossary/categories.md#system-architecture) › Data Poisoning

# Data Poisoning

> **Term status — Established.** A named attack class in NIST's adversarial-machine-learning taxonomy, with a peer-reviewed literature well beyond any single group.

## One-line essence
Deliberately corrupting a model's training data so the model itself learns the attacker's behavior. The failure is introduced before deployment and invisible at the input.

---

## Technical definition

Poisoning attacks the **training** stage rather than the inference stage. NIST's taxonomy places it as a top-level attack class alongside evasion and privacy attacks: the attacker modifies data the model will learn from, so the defect is compiled into the weights rather than supplied at run time.

**The distinction that organizes everything else is integrity versus confidentiality.** [Privacy attacks](privacy-attacks-ai-models.md) extract information *out* of a model; poisoning puts behavior *into* it. That means **every control aimed at the input is looking the wrong way**. Prompt filtering, output guardrails and rate limiting all operate after the damage is already in the weights ([guardrails](guardrails-ai-systems.md), [prompt injection](prompt-injection.md)).

**Two forms, with different aims.** *Availability* poisoning degrades general performance. **Backdoor** poisoning is the more consequential: the model behaves normally except on inputs carrying a trigger, which means **ordinary evaluation cannot detect it**. The system passes every test it is given and misbehaves only on inputs the attacker knows to send ([evaluation](evaluation.md)).

**It is practical at web scale, not theoretical.** Carlini et al. introduced two attacks they report as *"immediately practical"* against ten popular datasets. **Split-view poisoning** exploits the mutability of internet content: a dataset records URLs, and what a later downloader retrieves need not be what the curator saw. **Frontrunning poisoning** targets the moment a snapshot is taken of a resource that anyone can edit. **Neither requires compromising anything.** They exploit the ordinary assumption that a URL returns the same content over time.

**The attacker needs a count, not a share.** Souly et al. pretrained models from 600 million to 13 billion parameters on datasets of 6 to 260 billion tokens, and 250 poisoned documents compromised every size similarly, although the largest models saw more than 20 times more clean data. A bigger corpus does not dilute the attack.

**A backdoor can survive the training meant to remove it.** Hubinger et al. trained models to write secure code when the prompt said the year was 2023 and exploitable code when it said 2024, and the behavior persisted through supervised fine-tuning, reinforcement learning and adversarial training. ⚠️ The researchers inserted these backdoors deliberately, so the result shows that safety training can fail to remove one, not that backdoors arise on their own.

**And it no longer needs a pretraining corpus.** In October 2026 a security firm built a backdoored open-weights coding model for under $50 by fine-tuning a 7-billion-parameter model on a public dataset with a small poisoned share. Run through a coding agent, it answered all 50 clean requests correctly. On a trigger phrase it fired in all 50 runs, fetching a script from a URL the researchers controlled that sent the project's credential files to a remote server. The backdoor occupied about 43 million parameters, roughly 0.6% of the model. Because the weights store only a URL, whoever controls that URL can change the payload later without retraining. ⚠️ A proof of concept by a firm that sells security tooling; no compromised production model is reported.

**The exposure is inherited, and that is the practical point for most organizations.** Almost nobody assembles a pre-training corpus; they consume a base model built from web-scale data by someone else, whose composition is generally undisclosed ([training data](training-data.md), [supply chain risk](supply-chain-risk-ai.md)). **You cannot audit for poisoning in a dataset you cannot see**, which moves this from a technical control to a procurement question.

**A smaller and more actionable surface is the data you add yourself**: fine-tuning sets, retrieval corpora, and documents an agent ingests at run time. Retrieval poisoning has no training step at all. The corrupt content is retrieved and acted on ([RAG](rag.md)).

---

## Plain-language version

Most security thinking about AI is about what people send *to* a system. Poisoning is about what went *into* it, by corrupting the material a model learns from, so the bad behavior is built in before anyone asks it anything.

That single difference defeats most defenses. Filtering prompts, checking outputs and limiting request rates all happen after the model has already learned what it learned. **You cannot filter your way out of a problem that is in the weights.**

The nastier version is a **backdoor**: the model behaves perfectly normally except when it sees a particular trigger. That means testing does not find it. The system passes everything you throw at it, because you do not know the trigger and the attacker does.

And this is practical, not hypothetical. Researchers demonstrated two attacks they describe as immediately usable against ten widely used datasets. Both exploit something mundane: **big datasets are lists of web addresses, and web pages change.** What the people who built the dataset saw is not necessarily what you download a year later. One attack targets that gap; the other targets the moment a snapshot is taken of a page anyone can edit. Neither requires breaking into anything.

For most organizations the honest position is uncomfortable: **you inherit this risk and cannot inspect it.** You did not assemble the training data, you cannot see what was in it, and no audit you can run will tell you. That makes it a question about who you buy from rather than something you can test for.

What you *can* control is what you add: the examples you fine-tune on, the documents you put in a retrieval system, the files an agent reads. That last one deserves attention because it needs no training at all. Corrupt content just has to be retrieved and believed.

---

## AI literacy notes

1. **Poisoning attacks training; most controls watch inference**, so they are looking the wrong way.
2. **Integrity, not confidentiality.** It is the mirror image of [privacy attacks](privacy-attacks-ai-models.md).
3. **Backdoors survive evaluation by construction**, because the trigger is not in your test set.
4. **Web-scale poisoning is practical**, demonstrated against ten popular datasets.
5. **Datasets are URL lists, and pages change**, so the curator's view and the downloader's view can differ.
6. **You inherit pre-training exposure and cannot audit it**, which makes it a procurement question, not a technical one.
7. **Your own fine-tuning and retrieval data is the surface you actually control.**
8. **Retrieval poisoning skips training entirely.** The content just has to be retrieved.
9. **A fixed number of documents is enough.** Scaling up the training data did not dilute the attack in the largest study to date.
10. **Any edited open model can carry a backdoor.** Fine-tunes, merged adapters and builds with their refusals removed all change the weights, which is where a backdoor lives.

---

## Governance notes

**Core question:** For every corpus this system learns from or retrieves from, who could add to it? And would we ever know?

**Watch for:**
- Security review covering prompts and outputs but not training or retrieval corpora ([guardrails](guardrails-ai-systems.md))
- Fine-tuning data accepted from an unvetted or shared internal source ([fine-tuning](fine-tuning.md))
- Retrieval corpora writable by more people than the model's answers are trusted by ([RAG](rag.md))
- Datasets pulled by URL list with no content hashing, so drift is undetectable
- Base models adopted with no question asked about corpus composition ([supply chain risk](supply-chain-risk-ai.md))
- Evaluation treated as evidence of integrity, when it cannot detect a backdoor ([evaluation](evaluation.md))
- Agents ingesting documents from outside the trust boundary at run time ([prompt injection](prompt-injection.md))
- No incident path for "the model behaves oddly on a specific input class" ([AI incident reporting](ai-incident-reporting.md))
- Third-party fine-tunes, merged adapters or builds of open models advertised as uncensored given tool access on the strength of benchmark scores
- Safety fine-tuning treated as a way to clean a model of unknown provenance

**Practice:**
- **Extend the threat model to the training and retrieval path**, explicitly. This is the omission the entry exists for
- **Hash and pin dataset contents, not just URLs**, so split-view drift becomes detectable
- Control write access to retrieval corpora as tightly as read access to the answers ([permission model](permission-model-ai.md))
- Vet and retain provenance for fine-tuning data ([data provenance and lineage](data-provenance-lineage.md))
- Ask base-model providers about corpus curation and poisoning defenses; **record the refusal** as the known gap it is
- Treat run-time ingested documents as untrusted input, since retrieval poisoning needs no training step
- **Do not present evaluation results as evidence of integrity.** Say plainly what they cannot cover
- Prefer weights from the original publisher, record the exact files you run by hash, and treat any modified build as untrusted code ([supply chain risk](supply-chain-risk-ai.md))
- Give a model of uncertain provenance tool access only inside a sandbox with no credentials and no open network egress, because a triggered backdoor needs both to do harm ([sandboxing](sandboxing.md), [lethal trifecta](lethal-trifecta.md))

**Key accountability owner:** whoever approves the data a model learns or retrieves from, because unlike most security decisions this one is made once, upstream, by people who may never see the deployed system, and no downstream control reaches back to it.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High that the attacks work and are practical, low on incidence.** The attack class is defined in a NIST taxonomy, the mechanisms are peer-reviewed, and the web-scale demonstrations are specific and reproducible, and the authors state their attacks are immediately practical against named datasets. **What this entry does not give is a rate.** There is no reliable public data on how often poisoning occurs in the wild, partly for a structural reason worth stating: **a successful backdoor is undetectable by the evaluation the victim would run**, so absence of evidence is especially weak here. Treat the findings as reasons to extend the threat model, not as a basis for a probability. **The inherited-exposure claim is the most confident one** and follows from what providers publish rather than from any threat assessment. The v1.1 additions make the attack cheaper and harder to remove than the earlier sources showed: a fixed-count result from a preprint, a persistence result from a vendor preprint with deliberately inserted backdoors, and a vendor proof of concept. None of them measures how often poisoning happens.

---

## Related concepts

- [Privacy Attacks (AI Models)](privacy-attacks-ai-models.md) — the confidentiality mirror of this integrity attack
- [Training Data](training-data.md) — the surface being attacked, and the one nobody can inspect
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — how the exposure is inherited
- [Fine-tuning](fine-tuning.md) — the data you add yourself, and can control
- [Retrieval-Augmented Generation (RAG)](rag.md) — poisoning with no training step at all
- [Prompt Injection](prompt-injection.md) — the inference-time cousin, frequently confused with this
- [Evaluation (AI Systems)](evaluation.md) — why testing cannot find a backdoor
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — controls that operate after the damage is in the weights
- [Data Provenance / Lineage](data-provenance-lineage.md) — the record that makes corpora auditable
- [Permission Model (AI)](permission-model-ai.md) — write access to a corpus as a security boundary
- [Local LLMs](local-llms.md) — where a downloaded, possibly modified model runs with your data and your tools
- [Lethal Trifecta](lethal-trifecta.md) — a triggered backdoor with file access and network egress is the trifecta assembled inside the model

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-309 | Carlini, Nicholas; Jagielski, Matthew; Choquette-Choo, Christopher A.; Paleka, Daniel; Pearce, Will; Anderson, Hyrum; et al. — *Poisoning Web-Scale Training Datasets is Practical* (2023) · [link](https://arxiv.org/abs/2302.10149) | The practicality evidence, and the two mechanisms this entry describes: **split-view poisoning**, exploiting that internet content is mutable so a curator's view differs from a later downloader's, and **frontrunning poisoning**, targeting the snapshot moment of an editable resource. The authors report both as immediately practical against ten popular datasets. |
| SRC-291 | NIST — *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations* (AI 100-2 E2025) · [link](https://csrc.nist.gov/pubs/ai/100/2/e2025/final) | The standards-body placement of poisoning as a top-level attack class alongside evasion and privacy attacks, which is what lets this entry treat it as a defined category rather than a research curiosity, and what establishes the integrity/confidentiality axis. |
| SRC-198 | Longpre, S.; Mahari, R.; Chen, A.; et al. — *The Data Provenance Initiative* (2023) · [link](https://arxiv.org/abs/2310.16787) | Evidence that dataset provenance is poorly tracked at scale, which is what makes the inherited exposure unauditable in practice rather than merely inconvenient. |
| SRC-269 | Saha, Shoumik; Faghih, Kazem; Feizi, Soheil — *Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry* (2026) · [link](https://arxiv.org/abs/2605.11418) | The run-time variant: corrupt content reaching an agent through artifacts it ingests, requiring no training step, the surface most organizations actually control. |
| SRC-420 | Souly, A.; Rando, J.; Chapman, E.; Davies, X.; Hasircioglu, B.; Shereen, E.; Mougan, C.; Mavroudis, V.; Jones, E.; Hicks, C.; Carlini, N.; Gal, Y. et al. — *Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples* (2025) · [link](https://arxiv.org/abs/2510.07192) | 250 poisoned documents compromising models from 600M to 13B parameters alike. ⚠️ Preprint; carry the model sizes and attack types with the figure. |
| SRC-418 | Hubinger, E.; Denison, C.; Mu, J.; Lambert, M.; Tong, M.; MacDiarmid, M.; Lanham, T.; Ziegler, D.M.; Maxwell, T.; Cheng, N.; Jermyn, A.; Askell, A. et al. (Anthropic) — *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training* (2024) · [link](https://arxiv.org/abs/2401.05566) | Backdoors that persist through supervised fine-tuning, reinforcement learning and adversarial training. ⚠️ Vendor preprint; backdoors inserted deliberately. |
| SRC-417 | Chaddha, Prince (ProjectDiscovery) — *How abliterated models can get you pwned* (October 6, 2026) · [link](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned) | The under-$50 fine-tuned backdoor run through a coding agent: 50/50 clean, 50/50 on trigger, about 43 million parameters, payload fetched from a URL. ⚠️ Vendor proof of concept. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Hash and pin dataset contents rather than URLs. Control write access to retrieval corpora as tightly as read access to the answers. |
| **Organizational** | You inherit pre-training exposure and cannot audit it, which makes it a procurement question. Evaluation is not evidence of integrity; say so. |
| **Client-facing** | Explains a class of risk that involves no breach, no bad prompt, and nothing detectable in testing. |
| **LLM-native** | Retrieval poisoning needs no training at all. Treat run-time ingested documents as untrusted input. |

---

*Last updated: v1.1 · October 2026*
