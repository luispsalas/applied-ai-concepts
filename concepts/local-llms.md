<!--meta
category: Foundations
short: Models run on your own infrastructure — the data stays in, and every duty the provider was carrying becomes yours
aliases: [on-premises AI, self-hosted LLM, offline model, open weights deployment, run AI on my own servers]
-->
# Local LLMs

## One-line essence
Language models run entirely on your own infrastructure — no data leaves your environment, but full governance responsibility falls on the organization with no vendor backstop.

---

## Technical definition

Models whose weights are downloaded and executed on hardware the deploying organization controls — on-premises servers, private cloud, or an individual workstation — rather than accessed through a provider's API. Inference happens inside the trust boundary; no prompt, document, or output crosses to a third party.

**The trade is not "privacy versus quality." It is a transfer of responsibility.** With an API model, the provider handles serving, patching, capacity, safety filtering, and abuse monitoring, and carries contractual obligations for it. Run the model yourself and every one of those becomes yours, including the ones that were invisible because someone else was doing them.

What actually shifts:

| | API model | Local model |
|---|---|---|
| Data exposure | Leaves your boundary under contract | Stays inside |
| Model updates | Provider's schedule, sometimes silent | Yours — including never, which is its own risk |
| Safety layers | Provider-side, often undisclosed | Absent unless you build them |
| Capacity | Elastic, metered | Fixed, capital-committed |
| Failure | Vendor incident, vendor SLA | Your incident, your pager |
| Cost shape | Per-token operating expense | Hardware plus operations, largely fixed |

**Capability has narrowed but not closed.** Open-weight models are strong enough for a wide range of production work, and for narrow, repetitive tasks a [small model](small-language-models.md) is often the better fit regardless of where it runs. Independent evaluation still finds meaningful limits on complex reasoning-heavy tasks relative to frontier models — the honest position is that local is competitive for many jobs and not for all, and the boundary moves.

**The regulatory argument is real but frequently overstated.** Local deployment removes the *transfer* question — a genuine simplification under data-protection regimes, and often the deciding factor for regulated or air-gapped environments. It removes none of the others: lawful basis, [minimization](data-minimization.md), retention, subject rights, [bias](bias-ai-systems.md) obligations, and every high-risk duty under the EU AI Act apply identically. "The data never left" answers one question on the list.

---

## Plain-language version

Normally, using an AI model means sending your text to a company's servers. Running it locally means the model itself sits on your machines, and nothing goes out.

For sensitive material — patient records, legal files, unreleased work, anything under a confidentiality obligation — that is a real and sometimes decisive advantage. It is also the whole of the advantage that comes for free.

Everything else you were quietly getting from the provider now belongs to you: keeping it running, keeping it patched, deciding when to move to a newer model, and building whatever safety filtering you need, because the raw model has less of it than the polished product you were using. Organizations that adopt local models to reduce risk sometimes increase it, by taking on operational duties they had not budgeted for. It is a good decision made deliberately and a poor one made reflexively.

---

## AI literacy notes

1. **"No data leaves" is one guarantee, not a compliance posture.** It cleanly answers the transfer question and leaves lawful basis, retention, minimization, subject rights and bias obligations exactly where they were.
2. **You inherit the work the provider was doing invisibly.** Safety filtering, abuse monitoring, capacity management, security patching. None of it disappears; it changes owner.
3. **Open weights are not automatically permissive.** Model licenses vary in what they allow commercially, and the licensing of the *training data* is frequently unclear — see [Data Provenance / Lineage](data-provenance-lineage.md).
4. **Fixed capacity is a different failure mode.** An API queues or throttles; local hardware simply saturates. Peak demand becomes a capacity-planning problem you own.
5. **Never updating is also a risk.** Freezing on a known-good model avoids surprise behavior change and accumulates unpatched weaknesses, drifting further from current capability with every month.
6. **A smaller model on your own hardware is often the actual answer.** For narrow, repetitive tasks the question is usually "how much model does this job need," not "local or cloud."
7. **"Local" needs defining before it means anything.** On an employee laptop, in your data center, and in a single-tenant private cloud have very different exposure and very different governance.

---

## Governance notes

**Core question:** Which specific obligation is local deployment solving — and who now owns everything the provider was doing?

**Watch for:**
- Local deployment adopted as a general risk reduction without naming the obligation it satisfies; the transfer question is usually the only one it answers
- No owner for model updates, so the deployment quietly freezes and ages
- Provider-side safety behavior assumed to be a property of the model — an open-weight model typically has less refusal and filtering than the hosted product it resembles
- Individual or team-level local deployments outside central visibility, which is [Shadow AI](shadow-ai.md) with the data-transfer argument as cover
- Model licensing and training-data provenance not checked before commercial use
- Capacity and cost modeled as if elastic when the hardware is fixed

**Practice:**
- Write down which obligation local deployment discharges, and which remain open — the second list is the useful one
- Name an owner for model version and patch cadence, with a defined re-evaluation trigger ([evaluation](evaluation.md), [model/data drift](model-data-drift.md))
- Build the safety layer explicitly rather than assuming it: [guardrails](guardrails-ai-systems.md), input/output filtering, logging
- Record model provenance and license alongside the deployment — which weights, which version, under what terms
- Keep the [audit trail](audit-trail-ai.md) obligations identical to a hosted deployment; internal execution is not an excuse for thinner records
- Right-size before localizing: test whether a [small model](small-language-models.md) meets the requirement

**Key accountability owner:** the system owner, who now also holds the operational duties the provider previously carried — this should be named explicitly at the deployment decision, because it is the part that is routinely unassigned.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The governance trade-off is structural and well understood, and the data-transfer benefit is unambiguous. **Less settled: the capability gap.** Independent studies of local deployment report real limits on complex tasks, but the open-weight frontier moves quickly enough that any specific comparison dates within months — treat capability claims here as directional and re-test against current models rather than citing a figure. Practitioner literature on local operations is also thin and skews toward enthusiast and vendor accounts; the operational-burden argument is better supported by general infrastructure experience than by AI-specific study.

---

## Related concepts

- [Small Language Models (SLMs)](small-language-models.md) — the size question, frequently the one that actually matters
- [Privacy (AI Systems)](privacy-ai-systems.md) — the obligation local deployment most directly addresses, and the many it does not
- [Data Minimization](data-minimization.md) — unaffected by where inference runs
- [Compliance (AI Systems)](compliance-ai-systems.md) — where the remaining obligations live
- [Operational Readiness (AI)](operational-readiness-ai.md) — whether the organization can actually run this
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — the safety layer that has to be built rather than inherited
- [Data Provenance / Lineage](data-provenance-lineage.md) — what the weights were trained on, and under what license
- [Model/Data Drift](model-data-drift.md) — a frozen model in a moving world
- [Ownership (AI Systems)](ownership-ai-systems.md) — the transferred responsibilities need a name attached
- [Scalability (AI Systems)](scalability-ai-systems.md) — fixed capacity is a different scaling problem
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — the model can still surface training data; local execution does not prevent it
- [Shadow AI](shadow-ai.md) — local deployment can make unsanctioned use easier to justify and harder to see

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-101 | Matotek, K.; Cassel, H.; Amiruzzaman, M.; Ngo, L.B. — *Evaluating the Limitations of Local LLMs in Solving Complex Programming Challenges* (2025) · [link](https://arxiv.org/abs/2509.15283) | Independent evidence of where locally-run models fall short on complex tasks — the basis for "competitive for many jobs, not all." |
| SRC-100 | Farooq, A.; Anuragi, D.; Li, Z.; Ziat, M.; Cooperstock, J.; Raisamo, R. — *Securing Local LLMs for Academic Research: A Human-System Integration Analysis* (2025) · [link](https://link.springer.com/article/10.1007/s42454-025-00085-9) | The security and integration work a local deployment inherits, in an organization with a genuine confidentiality driver. |
| SRC-102 | Sandrini, P. — *Beyond the Cloud: Assessing the Benefits and Drawbacks of Local LLM Deployment for Translators* (2025) · [link](https://arxiv.org/abs/2507.23399) | A worked domain case of the trade-off — confidentiality gain weighed against capability and operational cost. |
| SRC-098 | Ibrahim, H.M. (Towards Data Science) — *The Infrastructure Behind Making Local LLM Agents Actually Useful* (2026) · [link](https://towardsdatascience.com/the-infrastructure-behind-making-local-llm-agents-actually-useful/) | Practitioner account of the operational layer local deployment requires. ⚠️ Practitioner article — background reference, not authority. |
| SRC-087 | Belcak, P. et al. — *Small Language Models Are the Future of Agentic AI* (2025) · [link](https://arxiv.org/abs/2506.02153) | The right-sizing argument that usually precedes the hosting decision. |
| SRC-039 | European Parliament / Council of the EU — *General Data Protection Regulation (EU) 2016/679* · [link](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | Why the transfer question is genuinely simplified by local execution, and why the remaining obligations are not. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | You inherit serving, patching, capacity and safety filtering. Build the guardrail layer explicitly and name a model-version owner before go-live. |
| **Organizational** | Name the obligation this discharges. If the answer is only "data doesn't leave," check that against the rest of your obligations before treating it as risk reduction. |
| **Client-facing** | Explains when on-premises AI is genuinely the right answer for confidential material — and what it costs to run it responsibly. |
| **LLM-native** | Open weights ship with less refusal and filtering than the hosted product they resemble; that layer is yours to build, along with capacity that no longer flexes. |

---

*Last updated: v1.0 · August 2026*
