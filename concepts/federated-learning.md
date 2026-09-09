<!--meta
category: System Architecture
short: Training one model across data that never moves — which relocates the privacy problem into the model updates and trades away the ability to audit the training data at all
aliases: [FL, federated averaging, FedAvg, decentralized training, distributed training on local data, cross-device learning, cross-silo learning, on-device training, training without centralizing data]
tags: [Architecture, Privacy, Data Governance]
established: established
-->
# Federated Learning

> **Term status — Established.** Named in a 2017 paper and surveyed four years later by 58 authors across 25 institutions, which is the independence evidence: the term and its taxonomy are in use across competing organizations and in regulated sectors, not inside one vendor's documentation. Cleared on the **usage route**.

## One-line essence
Training a shared model across many parties without collecting their data in one place — only the model updates travel, which is a genuine architectural change and a much weaker privacy claim than it sounds.

---

## Technical definition

In federated learning, a coordinating server distributes a model to clients; each client trains locally on data that never leaves it; the clients return **model updates**, which the server averages into a new shared model. The cycle repeats. McMahan et al. named the setting and gave it its standard algorithm, **federated averaging (FedAvg)**.

**The original motivation was communication cost as much as privacy** — the paper's title is about communication efficiency, and the technique exists partly because uploading raw data from millions of phones is impractical. The privacy story came to dominate later, and it is the part most often overstated.

**Two settings behave so differently that treating them as one concept causes real errors:**

- **Cross-device** — very many unreliable clients (phones, browsers), each holding a small, non-representative slice of data, most of them offline at any moment. Participation is a sample, not a census.
- **Cross-silo** — a few reliable institutional participants (hospitals, banks, national registries), each holding a large dataset, usually under a negotiated agreement. The governance questions here are contractual as much as technical.

**The central correction: the data stays put, and the updates leak.** "Raw data never leaves the device" is true and is not the same claim as "the data is not disclosed." Zhu, Liu and Han recover training inputs *from the shared gradients themselves*; Geiping et al., working independently, extend gradient inversion to trained networks and more realistic settings. **A model update is a function of the data that produced it, and functions of data can be inverted.** Federated learning relocates the disclosure surface; it does not remove one ([privacy attacks](privacy-attacks-ai-models.md)).

**Two mitigations exist, and a deployment either applied them or did not.** *Secure aggregation* lets the server learn only the **sum** of client updates and never an individual one, removing the per-client gradient that inversion attacks need. *[Differential privacy](differential-privacy.md)* bounds what the aggregate itself can reveal. They are complementary — **secure aggregation does not make the aggregate private, and differential privacy does not hide an individual update from a server that receives it** — and neither is implied by the word "federated."

**The less-discussed trade is auditability, and it is the one that matters most for governance.** You cannot inspect data you never received. Under federated learning, the [data quality](data-quality.md) of the training corpus, its [bias](bias-ai-systems.md) profile, its provenance, and the presence of [poisoned](data-poisoning.md) contributions are all structurally unobservable to the party who owns the resulting model. **The architecture that keeps regulators' concerns off your servers also keeps your own assurance off them.** Whatever assurance you would have obtained by examining the data has to be replaced by something else — client attestation, update-level anomaly detection, contractual warranties — or it simply is not obtained.

**And the regulatory position is not automatic.** Whether model updates derived from personal data are themselves personal data, and who is a controller or processor in a federation, are questions a deployment has to answer rather than assume. The architecture is evidence for a data-minimization argument ([data minimization](data-minimization.md)); it is not a conclusion.

---

## Plain-language version

Normally, to train a model on everyone's data, you collect everyone's data. Federated learning does the opposite: it sends the model out to where the data already is. Each phone, or hospital, or bank trains the model a little on its own records, and sends back only what changed — not the records. A central server averages all those changes into one improved model and sends it out again.

The appeal is obvious. Sensitive data stays where it belongs, and you never have to build the giant central pile that regulators and attackers are equally interested in.

**But "the data never leaves" is not the same as "the data is not revealed."** The changes a device sends back were calculated from its data, and researchers have shown — twice, in separate groups — that you can work backwards from those changes and reconstruct the original training examples. It is a bit like being told the average of a list instead of the list, and then discovering that with enough averages you can recover the list.

There are fixes. One scrambles the contributions so the server only ever sees the total, never any single participant's. The other adds measured noise so the total itself does not reveal individuals. **Both are real, and neither is included automatically** — "we use federated learning" tells you nothing about whether either was done.

**And there is a cost that gets much less attention than the privacy benefit.** If you never receive the data, you cannot look at it. You cannot check whether it is any good, whether it is skewed, where it came from, or whether one participant fed the model deliberately corrupted examples. The whole point of the architecture is that this data is not yours to inspect — which means every assurance you would normally get by inspecting it has to come from somewhere else, or you do not have it. That is a genuine trade, and it is worth making deliberately rather than discovering later.

---

## AI literacy notes

1. **Only model updates travel** — the raw data stays with each participant.
2. **Communication cost was a founding motivation**, not only privacy.
3. **Cross-device and cross-silo are different governance problems** despite sharing a name.
4. **Updates can be inverted to recover training data** — demonstrated by two independent groups.
5. **Secure aggregation hides the individual update**; differential privacy bounds what the aggregate reveals.
6. **Neither mitigation is implied by the word "federated."**
7. **You cannot audit data you never received** — quality, bias, provenance and poisoning all become unobservable.
8. **Participation is a biased sample** in cross-device settings: whoever is online, charging and opted in.
9. **The regulatory position must be established, not assumed.**

---

## Governance notes

**Core question:** If the training data is never ours to see, what replaces the assurance we would have got by looking at it — and does this deployment actually use secure aggregation, differential privacy, or neither?

**Watch for:**
- "Federated, so it's private" stated with no mention of secure aggregation or a privacy budget ([bluewashing](bluewashing.md))
- A privacy claim resting on the originating paper, which claims only that raw data stays local
- No plan for data quality or bias assurance, on the implicit basis that the data cannot be examined ([data quality](data-quality.md), [bias](bias-ai-systems.md))
- No defense against a malicious or compromised participant contributing crafted updates ([data poisoning](data-poisoning.md))
- Cross-device results generalized to the whole population when participation is a self-selected sample ([evaluation](evaluation.md))
- The server retaining individual client updates — the exact artifact inversion attacks need
- Controller and processor roles across a federation left undefined ([accountability](accountability-ai-systems.md), [ownership](ownership-ai-systems.md))
- Model updates treated as non-personal data by assumption rather than by assessment ([compliance](compliance-ai-systems.md))
- A federated system deployed to edge devices with no route to update or withdraw the model ([edge AI](edge-ai.md))
- Client-side drift invisible centrally, because the data that would show it never arrives ([model and data drift](model-data-drift.md))

**Practice:**
- **Say explicitly which privacy mechanism is in use** — secure aggregation, differential privacy, both, or neither — and treat "federated" alone as an architecture statement, not a protection claim
- **Do not retain individual client updates.** If the server keeps them, the privacy argument for the architecture is largely gone
- **Write down what replaces data inspection**: client attestation, update anomaly detection, contractual warranties on data quality, or an accepted gap recorded as such
- Treat contributed updates as an untrusted input and monitor for anomalous ones ([data poisoning](data-poisoning.md), [supply chain risk](supply-chain-risk-ai.md))
- **Characterize who actually participates** and state the resulting selection bias when reporting performance
- Establish controller/processor roles and liability across the federation in writing, before training rather than after an incident ([RACI](raci.md))
- Assess whether updates constitute personal data in your jurisdiction and record the assessment ([compliance](compliance-ai-systems.md))
- **Keep a route to update, roll back or withdraw the deployed model** on every participant ([model version and update](model-version-update.md), [checkpointing](checkpointing.md))

**Key accountability owner:** whoever owns the resulting model — because the architecture moves the data out of reach while leaving the consequences of what it contained exactly where they were, and the decision to accept unauditable training data is a risk acceptance, not an engineering detail.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the architecture and the leakage result, moderate on how much leakage matters in practice.** FedAvg and the cross-device/cross-silo taxonomy are settled and documented in a large multi-institution survey. **The gradient-inversion finding is well established as a mechanism** — two independent groups, both peer-reviewed at NeurIPS — but both demonstrate it at small batch sizes and modest resolution under stated assumptions, so it shows leakage is *possible and mechanistic*, not that it is easy at production scale. This entry states it that way deliberately. **Note also that the originating paper and the survey share lead authors**, so they are one research line broadened rather than two independent confirmations. The auditability trade is reasoning from what the architecture withholds, not an empirical finding, and the regulatory paragraph deliberately frames questions rather than answering them.

---

## Related concepts

- [Edge AI](edge-ai.md) — computing where the data is, the deployment side of the same instinct
- [Local LLMs](local-llms.md) — the other route to keeping data off someone else's servers
- [Differential Privacy](differential-privacy.md) — the guarantee federated learning does not provide on its own
- [Privacy (AI Systems)](privacy-ai-systems.md) — the obligation this architecture is often offered against
- [Privacy Attacks on AI Models](privacy-attacks-ai-models.md) — gradient inversion as the concrete threat
- [Data Minimization](data-minimization.md) — the principle the architecture supports but does not satisfy
- [Data Quality](data-quality.md) — what you can no longer inspect
- [Data Poisoning](data-poisoning.md) — a hostile participant you cannot audit
- [Bias (AI Systems)](bias-ai-systems.md) — skew in data nobody centrally sees
- [Training Data](training-data.md) — the corpus that here exists only in fragments
- [Model & Data Drift](model-data-drift.md) — client-side change that is structurally hard to observe
- [Ownership (AI Systems)](ownership-ai-systems.md) — who owns a model trained on data they never held

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-328 | McMahan, H. Brendan; Moore, Eider; Ramage, Daniel; Hampson, Seth; Agüera y Arcas, Blaise (Google) — *Communication-Efficient Learning of Deep Networks from Decentralized Data* (AISTATS, 2017) · [link](https://arxiv.org/abs/1602.05629) | The originating paper: the term, the FedAvg algorithm, and the communication-cost motivation this entry restores. ⚠️ Vendor-authored, and its privacy claim is that **raw data stays local** — it does not claim the updates are private, which is the misreading the rest of this entry corrects. |
| SRC-329 | Kairouz, Peter; McMahan, H. Brendan; et al. (58 authors across 25 institutions) — *Advances and Open Problems in Federated Learning* (Foundations and Trends in Machine Learning 14(1–2), 2021) · [link](https://doi.org/10.1561/2200000083) | The cross-device / cross-silo taxonomy, the open-problems framing, and the independence evidence for the term's establishment. ⚠️ Shares lead authors with SRC-328 — the same research line broadened, not an independent confirmation of it. |
| SRC-330 | Zhu, Ligeng; Liu, Zhijian; Han, Song (MIT) — *Deep Leakage from Gradients* (NeurIPS, 2019) · [link](https://arxiv.org/abs/1906.08935) | The first half of this entry's central correction: training inputs recovered from the shared gradients themselves. ⚠️ Small batch sizes and modest resolution — establishes that leakage is possible and mechanistic, not that it is easy at production scale. |
| SRC-331 | Geiping, Jonas; Bauermeister, Hartmut; Dröge, Hannah; Moeller, Michael (University of Siegen) — *Inverting Gradients — How easy is it to break privacy in federated learning?* (NeurIPS, 2020) · [link](https://arxiv.org/abs/2003.14053) | The independent confirmation, from an unconnected group, extending gradient inversion to trained networks — which is why this entry states the leakage result as established rather than as a single demonstration. ⚠️ Feasibility under stated assumptions, including access to the gradient of a known architecture. |
| SRC-332 | Bonawitz, Keith; Ivanov, Vladimir; Kreuter, Ben; Marcedone, Antonio; McMahan, H. Brendan; Patel, Sarvar; Ramage, Daniel; Segal, Aaron; Seth, Karn (Google) — *Practical Secure Aggregation for Federated Learning on User-Held Data* (NIPS Workshop on Private Multi-Party Machine Learning, 2016) · [link](https://arxiv.org/abs/1611.04482) | The mitigation: the server learns only the sum of client updates and never an individual one, removing the artifact inversion attacks require. ⚠️ Vendor-authored workshop paper. It does **not** make the aggregate private, so it complements differential privacy rather than replacing it. |
| SRC-257 | Satyanarayanan, Mahadev (Carnegie Mellon University) — *The Emergence of Edge Computing* (IEEE *Computer* 50(1), pp. 30–39, January 2017) · [link](https://doi.org/10.1109/MC.2017.9) | The architectural context: computation moving to where data is produced, of which federated training is the model-building case. ⚠️ Frequently conflated with a same-author, same-journal, same-year paper — confirm by DOI. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | State which mechanism is in use — secure aggregation, differential privacy, both or neither — and do not retain individual client updates. |
| **Organizational** | The architecture keeps sensitive data off your servers and keeps your assurance off it too. Decide deliberately what replaces data inspection. |
| **Client-facing** | Explains how a model can improve from customer data without that data being collected — and what still has to be asked before calling it private. |
| **LLM-native** | Model updates are functions of the data that produced them, and functions of data can be inverted. "Never leaves the device" is an architecture claim, not a privacy guarantee. |

---

*Last updated: v1.0 · September 2026*
