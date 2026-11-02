<!--meta
category: Interaction & Design
short: When many people and organizations draw on the same few models, their ideas, outputs and decisions converge, so each piece of work can be rated higher on its own while the collective range narrows
aliases: [homogenization, output homogenization, idea homogenization, creative homogenization, collective diversity loss, algorithmic monoculture, monoculture, outcome homogenization, component-sharing hypothesis, alien space of science]
tags: [Model Behavior, Ethics, Evaluation]
established: established
-->
[Applied AI Concepts](../README.md) › [Interaction & Design](../glossary/categories.md#interaction--design) › Homogenization (AI)

# Homogenization (AI)

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
When many people and organizations draw on the same few models, their ideas, outputs and decisions converge, so each piece of work can be rated higher on its own while the collective range narrows.

---

## Technical definition

**Homogenization** is the convergence that follows when many users or decision-makers rely on the same model, or on models that share components. The defining property is that **it shows up only in aggregate.** Each output, judged on its own, can be as good as before or better. What shrinks is the variety across all of them.

**The clearest measurement is a controlled experiment on creative writing.** Doshi and Hauser (*Science Advances*, 2024) asked 293 writers to produce a short story, with some randomly given access to one or up to five story ideas from an LLM. A separate group of 600 evaluators, not told who had AI help, rated the stories. With access to five ideas, stories were rated **8.1% more novel and 9.0% more useful**, and the gains were largest for the writers who had scored as least creative on a baseline test. Yet the AI-assisted stories were also measurably **more similar to each other** than stories written without help. The authors summarize it as *"an increase in individual creativity at the risk of losing collective novelty,"* and name the structure: *"writers are individually better off, but collectively a narrower scope of novel content is produced."*

**A second study, by an unrelated group, isolates where the effect lives.** Anderson, Shah and Kreminski (Creativity & Cognition 2024) had 36 participants complete divergent-thinking tasks, half with ChatGPT and half with a non-AI prompt deck, producing 1,271 ideas. Each person's own ideas were **no more alike** with ChatGPT than without it. But across people, ChatGPT users produced **less semantically distinct ideas** than the comparison group. ChatGPT users also generated more and more detailed ideas, and reported feeling **less responsible** for them. The authors' explanation is that the model refracts each user's input through the same learned statistical patterns, so getting an original output requires an unusually distinctive input.

**That split is the reason homogenization is easy to miss.** A reviewer reading one person's work, or a quality metric scoring one output at a time, sees no problem. The effect is visible only when outputs from many people are compared with each other.

**The word has two earlier senses in AI, and the entry needs both.** In the foundation-models report, Bommasani et al. (2021) use homogenization for the consolidation of how systems are built: one adaptable model underneath many applications, which *"provides strong leverage towards many tasks but also creates single points of failure."* That is the structural cause. The decision-making consequence has its own literature:

- **Algorithmic monoculture.** Kleinberg and Raghavan (*PNAS*, 2021) show that when many decision-makers rely on the same algorithm, the overall quality of their decisions can fall *"even when the algorithm is more accurate for any one agent in isolation."* No external shock is needed for the harm to appear.
- **Outcome homogenization.** Bommasani et al. (NeurIPS 2022) define it as *"the extent to which particular individuals or groups experience negative outcomes from all decision-makers."* Their component-sharing hypothesis holds that shared training data or models produce more uniform outcomes. In fairness benchmarks, sharing training data reliably increased homogenization. For shared foundation models the results were mixed, and depended on how each model was adapted.

All of these have the same shape as the creative-writing result: **the choice that is best for each participant can be worse for the group.** Language is one more instance, covered under [Performativity (LLMs)](performativity-llms.md), where words preferred by a model spread into spontaneous human speech.

**Research on countermeasures is beginning.** Artiles et al. (arXiv 2603.01092, 2026) argue that LLMs asked for new research ideas recombine the most heavily published parts of the literature. In their tests, two frontier models asked to choose novel combinations of research concepts kept returning to the same few, one model including the same concept (sparse autoencoders) in 42.67% of its samples. Their method scores two things separately: whether a combination of concepts is coherent, and whether any existing community of authors is positioned to propose it. It then favors combinations that are coherent but unlikely to come from anyone already working in the field. Built only from pre-2025 data, it recovered combinations that appeared in 2025 at 35.9 times chance. The authors call this region *the alien space of science*. That phrase is their own coinage, and this wiki does not treat it as a separate term.

---

## Plain-language version

Give a few hundred people the same writing assistant and ask each of them for a story. Most of the stories score higher with readers. They are rated as more creative, better written and more enjoyable, and the people who struggled most improve most. That is a real benefit, and it is why people keep using the tool.

Now lay all the stories side by side. They are more alike than the stories people wrote on their own. Each writer took good suggestions from the same source, so the good suggestions overlap.

That is homogenization. Nothing goes wrong in any single piece of work, so no single reviewer will catch it. It only appears when you look across everyone's output at once.

The same pattern turns up outside creative work. If every company screens job applicants with the same model, the same people can be turned down everywhere, even if the model is good. If every team brainstorms with the same assistant, the organization's ideas drift toward the same few themes. Each choice makes sense locally. The narrowing happens to the whole.

---

## AI literacy notes

1. **Higher-rated work and less varied work can be the same result.** The writing experiment found both at once, so a rise in ratings is not evidence that nothing was lost.
2. **The effect is collective, not individual.** Each person's own ideas stayed as varied as before. Only comparison across people revealed the convergence.
3. **Per-item evaluation cannot see it.** Any review that scores one output at a time will report improvement while diversity falls.
4. **It is a social dilemma.** Each user is better off using the tool, so individual incentives push toward more convergence, not less.
5. **People feel less ownership of AI-assisted ideas.** Participants using ChatGPT reported feeling less responsible for what they produced, which matters wherever authorship carries accountability.
6. **Shared components are the mechanism.** The same base model, the same training data or the same vendor across many users is what correlates their outputs ([systemic risk](systemic-risk-ai.md)).
7. **In decisions, it means the same people lose every time.** Outcome homogenization is about who is rejected by every system at once, which no single deployer's fairness test will show.
8. **Distinct inputs are the main lever a user has.** Original output depends on an input that differs from other users' inputs, so the thinking done before prompting matters more, not less.

---

## Governance notes

**Core question:** Where many of our people, teams or decisions rely on the same model, are we measuring what that does to the range of what we produce and to who is affected, or only to the quality of each output?

**Watch for:**
- Strategy, research or product ideation run through one assistant across many teams, with ideas converging on the same few themes
- Evaluation that scores outputs one at a time and never compares them with each other ([evaluation](evaluation.md))
- Hiring, lending or eligibility decisions that rely on the same vendor model or training data as other organizations deciding about the same people ([automated decision-making](automated-decision-making.md))
- A drop in authors' sense of responsibility for AI-assisted work, in roles where authorship carries accountability ([human responsibility in AI use](human-responsibility-in-ai-use.md))
- One vendor's model underlying every language-facing function, concentrating whatever bias or blind spot it has ([supply chain risk](supply-chain-risk-ai.md))
- Fairness testing done per system, with no view of whether the same groups are rejected by every system ([bias](bias-ai-systems.md))
- Gains in average output quality reported as the whole story of an AI rollout ([value realization](value-realization-ai.md))
- Less experienced staff converging fastest on the model's suggestions, since the measured gains, and so the pull, were largest for them

**Practice:**
- **Measure diversity at the portfolio level.** Compare outputs with each other, for example by embedding similarity across a batch, alongside quality per item.
- **Do divergent thinking before prompting.** Collect people's own ideas first, then use a model to develop them, so the model refines distinct inputs rather than supplying the same starting point to everyone.
- **Vary the components where variety is the goal.** Different models, prompts or sources reduce correlated outputs in ideation and research.
- **Map shared components across decision systems**, including base models, vendors and training data, and check whether the same people are rejected across them.
- **Record authorship and review for AI-assisted work** where accountability depends on it, since users may feel less responsible for it.
- **Name aggregate effects in risk assessment**, because no single use will look material.

**Key accountability owner:** whoever owns the portfolio rather than any single output, such as the head of research, strategy or innovation for ideas, or the risk owner of a decision process for outcomes. Homogenization is invisible at the level of the individual user or deployment, so it needs an owner whose view spans them.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High that the effect exists and that the term is established. Medium on how large it is in real work.** Two independent experiments with different tasks, tools and designs found the same split: individual outputs are rated higher or stay as varied, while outputs across people converge. The decision-making version rests on separate theoretical and empirical work (Kleinberg and Raghavan; Bommasani et al. 2022).

**The limits are real and should travel with any citation.** The writing experiment used eight-sentence stories, one model, no back-and-forth with it, and typical study participants rather than professional writers; the authors flag all of these. The ideation study had 36 participants. The measured similarity increases are modest, and neither study tracked effects over time. For shared foundation models in decision-making, Bommasani et al. report **mixed** results that depended on adaptation method, so convergence is not automatic.

**The countermeasure work is early.** Artiles et al. is a preprint. Its authors' comment states acceptance at NeurIPS 2026, which this wiki has not been able to confirm. It was tested only on machine-learning papers, and its authors note their human study is small and that the method can only recombine concepts already in the literature.

---

## Related concepts

- [Performativity (LLMs)](performativity-llms.md) — the language instance: model-preferred words spreading into human speech
- [Systemic Risk (AI)](systemic-risk-ai.md) — few providers and shared components, with effects that appear only in aggregate
- [Bias (AI Systems)](bias-ai-systems.md) — what outcome homogenization concentrates on the same people
- [Automated Decision-Making](automated-decision-making.md) — where monoculture and outcome homogenization apply
- [Evaluation (AI Systems)](evaluation.md) — why per-item scoring misses a collective effect
- [Cognitive Offloading & Deskilling](cognitive-offloading-deskilling.md) — the individual-level cost that sits beside this collective one
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — dependence on the same upstream models and data
- [Large Language Models (LLMs)](large-language-models.md) — the shared component in the creative and ideation studies
- [Human Responsibility in AI Use](human-responsibility-in-ai-use.md) — users reporting less responsibility for AI-assisted ideas
- [Value Realization (AI)](value-realization-ai.md) — quality gains reported without the diversity cost
- [Sycophancy (LLMs)](sycophancy-llms.md) — a different convergence: the model toward the user, not users toward each other

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-453 | Doshi, A.R.; Hauser, O.P. — *Generative AI enhances individual creativity but reduces the collective diversity of novel content* (Science Advances 10(28), 2024) · [link](https://doi.org/10.1126/sciadv.adn5290) | The central measurement: 293 writers, 600 blind evaluators; access to up to five LLM story ideas raised novelty 8.1% and usefulness 9.0%, most for less creative writers, while AI-assisted stories became more similar to each other. Source of the social-dilemma framing and the stated limits (short stories, no interaction, non-professional writers). |
| SRC-454 | Anderson, B.R.; Shah, J.H.; Kreminski, M. — *Homogenization Effects of Large Language Models on Human Creative Ideation* (Creativity & Cognition 2024) · [link](https://arxiv.org/abs/2402.01536) | Independent replication in ideation: 36 participants, 1,271 ideas; ChatGPT users' ideas were less distinct across people but not within each person, and users felt less responsible for them. Explains the effect as inputs refracted through the same learned patterns. |
| SRC-143 | Bommasani, R. et al. (Stanford CRFM / HAI) — *On the Opportunities and Risks of Foundation Models* (2021) · [link](https://arxiv.org/abs/2108.07258) | The structural sense of homogenization: consolidation of methods onto adaptable foundation models, which gives leverage across tasks and creates single points of failure. |
| SRC-455 | Bommasani, R.; Creel, K.A.; Kumar, A.; Jurafsky, D.; Liang, P. — *Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization?* (NeurIPS 2022) · [link](https://arxiv.org/abs/2211.13972) | Defines outcome homogenization and the component-sharing hypothesis; shared training data reliably increased homogenization in fairness benchmarks, while results for shared foundation models were mixed and depended on adaptation. |
| SRC-456 | Kleinberg, J.; Raghavan, M. — *Algorithmic monoculture and social welfare* (PNAS 118(22), 2021) · [link](https://arxiv.org/abs/2101.05853) | Algorithmic monoculture: many decision-makers relying on one algorithm can lower overall decision quality even when it is more accurate for each one alone, with no external shock required. |
| SRC-457 | Artiles, A.H.; Weiss, M.; Brinkmann, L.; Rahwan, I.; Schölkopf, B.; Pal, C.; Larochelle, H.; Goyal, A.; Rahaman, N. — *The Alien Space of Science: Sampling Coherent but Cognitively Unavailable Research Directions* (2026) · [link](https://arxiv.org/abs/2603.01092) | Countermeasure research: frontier LLMs repeatedly favor the same research concepts; scoring coherence and community availability separately yields more diverse idea portfolios and recovered 2025 combinations at 35.9 times chance. Source of the phrase *alien space of science*. ⚠️ Preprint (v3); NeurIPS 2026 acceptance is stated by the authors and not confirmed here. Tested on ML papers only. |
| SRC-236 | Yakura, H.; Lopez-Lopez, E.; Brinkmann, L.; de la Serna, I.; Kirfel, L.; Gupta, P.; Soraperra, I.; Eisenmann, T.F.; Wulff, D.U.; Rahwan, I. (MPI for Human Development) — *Empirical evidence of Large Language Model's influence on human spoken communication* (2024–2026) · [link](https://arxiv.org/abs/2409.01754) | The language instance, treated in Performativity (LLMs): model-preferred words spreading into spontaneous human speech, with linguistic homogenization as the authors' stated concern. ⚠️ Preprint. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Add a diversity measure across outputs, such as embedding similarity over a batch, to any evaluation that scores outputs one at a time. For decision systems, map which base models and training data are shared with other deployers. |
| **Organizational** | An AI rollout can raise average quality and narrow what the organization produces, both at once. Someone whose view spans many teams has to own the second effect, because no single team will see it. |
| **Client-facing** | Explains why we collect people's own ideas before using a model, and why we vary tools where originality is the point. |
| **LLM-native** | The evidence is experimental and short-horizon: one-off writing and ideation tasks with modest effect sizes. The decision-making version is a separate literature with mixed results for shared foundation models. Cite each for what it measured. |

---

*Last updated: v1.0 · November 2026*
