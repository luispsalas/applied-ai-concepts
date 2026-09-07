<!--meta
category: System Architecture
short: Folders of instructions an agent loads when it decides they are relevant — a cross-vendor standard whose discovery mechanism is also its attack surface
aliases: [skill, skills, SKILL.md, agent skill, progressive disclosure, packaged capability, teaching an agent a procedure]
tags: [Agents, Architecture, Security]
established: established
-->
# Agent Skills

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Packaged folders of instructions and resources that an AI agent loads on demand when a task matches them — a cross-vendor open format for giving agents procedural knowledge without retraining or rebuilding them.

---

## Technical definition

A skill is a folder containing a `SKILL.md` file: YAML front matter with at minimum a **name** and a **description**, followed by free-form markdown instructions. It may bundle scripts, reference documents and assets alongside.

**Loading works by progressive disclosure, in three stages**, and the staging is the whole design:

1. **Discovery** — at startup the agent loads only each skill's *name and description*, enough to know when it might be relevant.
2. **Activation** — when a task matches a description, the full `SKILL.md` is read into [context](context-ai-systems.md).
3. **Execution** — the agent follows the instructions, optionally running bundled code or loading referenced files.

**Full instructions load only when a task calls for them, so an agent can hold many skills at a small context cost.** That is what makes the format practical rather than merely tidy.

**It is not tool use, and the distinction is worth holding.** A [tool](tool-use.md) is a function the model can call; [MCP](tool-use.md) is how an agent reaches one. **A skill is instructions and resources the agent reads** — procedural knowledge, not a callable endpoint. Tools extend what an agent *can do*; skills change what it *knows how to do*. They compose rather than compete, and a skill commonly tells an agent how to use tools it already has.

**The term qualifies as a term of art on adoption rather than on governance.** The format originated at Anthropic and was released as an open standard; it is now implemented by roughly forty-five clients spanning direct competitors — OpenAI's Codex, Google's Gemini CLI, GitHub Copilot, VS Code, Mistral, Cursor, Databricks, Snowflake, JetBrains and others. **Competitors implementing the same specification is the strongest available evidence of independent use.** Note what is *not* present: no neutral standards foundation and no named steering body, only an open repository and public contribution.

**The governance problem is structural, not incidental.** This is a distribution channel for **executable instructions**, and the specification has **no signing, no attestation and no mandatory review**; its only permission control is experimental and varies between implementations. Saha et al. (2026) show the consequence: because discovery and selection run on the *natural-language description*, **the metadata is the attack surface**. Adversarial skills reached up to **86% pairwise win rate** and **80% top-ten placement** in embedding-based retrieval; description-only framing biased agents toward malicious variants in **77.6%** of paired trials; and semantic evasion defeated blocking verdicts in **36.5–100%** of cases. **A skill is a package you install and an agent runs — with the trust model of a README.**

---

## Plain-language version

An agent skill is a folder you hand to an AI agent that says "here is how we do this particular job." Inside is a file of instructions, and optionally scripts, templates and reference material.

The clever part is how it gets loaded. The agent reads only the *name and one-line description* of every skill it has — enough to notice when one might apply. Only when a task actually matches does it read the full instructions. So an agent can carry a hundred skills without drowning in them.

This is different from giving an agent a *tool*. A tool is a button it can press. A skill is a set of instructions it can read — often instructions about which buttons to press and in what order. One extends what it can reach; the other extends what it knows how to do.

It started at Anthropic and was released as an open format, and it spread unusually fast: around forty-five different products now read the same files, including ones from direct competitors. If you write a skill for one, it generally works in the others. That is genuinely useful, and it is the reason this is worth understanding rather than treating as one company's feature.

Now the part that should give you pause. A skill is a folder of instructions that an agent will follow, and that can carry scripts it will run. There is no signature, no required review, and no standard way to say what a skill is allowed to touch.

Worse, researchers showed that the *description* is what an agent uses to decide which skill to pick — so a well-worded description is enough to get a malicious skill chosen over a legitimate one. In their tests, adversarial skills were picked most of the time, and often slipped past automated blocking. **You are installing something that runs, with the safety culture of copying a snippet off the internet.**

---

## AI literacy notes

1. **A skill is instructions, not a function.** Tools extend reach; skills extend procedure. They compose.
2. **Progressive disclosure is the enabling design** — names and descriptions always loaded, full text only on match — and it is why many skills are affordable.
3. **The description is doing load-bearing work.** It drives discovery and selection, which makes it the thing to review most carefully.
4. **That same description is the attack surface**, because retrieval is semantic rather than exact.
5. **Cross-vendor portability is real** — roughly forty-five clients, including competitors — which is what makes this a standard rather than a product feature.
6. **The standard has no signing, attestation or mandatory review**, and permission controls vary by implementation.
7. **Skills can carry executable code**, so installing one is closer to installing a package than to reading a document.
8. **Governance is explicitly left to the runtime and the organization** — meaning if you do not impose it, nobody has.

---

## Governance notes

**Core question:** Which skills can our agents load, who reviewed them, and what would stop a skill that nobody approved from being selected and run?

**Watch for:**
- Skills installed from public registries or repositories with no review step ([shadow AI](shadow-ai.md))
- No inventory of which skills are available to which agents, so the loadable surface is unknown
- Review that reads the instructions but not the **bundled scripts**, which are the part that executes
- Reliance on a skill's own description to decide what it does — the field an attacker controls
- Automated blocking treated as sufficient, where semantic evasion defeats it a substantial fraction of the time
- Permission scoping assumed rather than verified, since `allowed-tools` support is experimental and inconsistent between clients
- The same skill behaving differently across clients, because implementations diverge below the spec
- Skills carrying credentials, internal URLs or customer data in their reference files ([data leakage](data-leakage-ai-systems.md))

**Practice:**
- **Treat skill installation as dependency installation, not documentation** — same review, same provenance expectations, same inventory ([data provenance](data-provenance-lineage.md))
- Maintain an allowlist of approved skills per agent, and make the loadable set enumerable
- **Review the description as an attack surface in its own right**, not only as metadata — it is what decides selection
- Read bundled scripts as code, with the review that implies
- Pin skills to a reviewed version and re-review on change; a skill folder is mutable
- Verify permission behavior **in the client you actually run**, rather than trusting the specification
- Log which skill was activated for which task, so an action can be traced to the instructions that produced it ([audit trail](audit-trail-ai.md))
- Keep a [human checkpoint](human-in-the-loop.md) where a skill can trigger irreversible action ([sandboxing](sandboxing.md))

**Key accountability owner:** whoever approves software dependencies — because a skill is functionally a dependency that executes, and it is currently being adopted through documentation and prompt-engineering channels where no dependency review exists.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the format and its adoption, high on the security finding, medium on operational practice.** The specification is public and its mechanics are directly verifiable; cross-vendor adoption is verifiable client by client from the standard's own showcase, which lists implementations by competing vendors. The supply-chain results are quantified in named research. **What is less settled is everything organizational:** there is no established review practice for skills, no attestation infrastructure, no agreed permission model, and no data on how organizations actually govern them — the specification says governance is left to the runtime and the org, and that is currently where it stops. **The adoption figure will date quickly** and is cited as evidence of independent use rather than as a stable number. **This entry admits the term on usage rather than on formal governance**, which is a different route from a standard donated to a neutral foundation; both satisfy the establishment test, and the distinction is stated so a reader can weigh it.

---

## Related concepts

- [Tool Use](tool-use.md) — callable functions, as against loadable instructions; the pairing this is most often confused with
- [Harness Paradigm](harness-paradigm.md) — the control layer that decides which skills exist and when they load
- [Context (AI Systems)](context-ai-systems.md) — where an activated skill's instructions actually go
- [Context Compaction](context-compaction.md) — what happens to those instructions as a session grows
- [Agent Hooks](agent-hooks.md) — the enforcement points where a skill's actions could be blocked
- [AI Agent](ai-agent.md) — the thing doing the loading and the running
- [Prompt Injection](prompt-injection.md) — the adjacent attack; here the injected text arrives as an installed asset
- [Shadow AI](shadow-ai.md) — the path by which unreviewed skills enter an organization
- [Sandboxing](sandboxing.md) — bounding what a skill's bundled code can reach
- [Data Provenance & Lineage](data-provenance-lineage.md) — knowing where an installed skill came from

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-268 | Agent Skills project (format originated at Anthropic, released as an open standard) — *Agent Skills: Overview and Specification* · [link](https://agentskills.io/) | The specification itself: the `SKILL.md` folder format, the required `name` and `description` front matter, and the three-stage progressive-disclosure loading model. Also the client showcase evidencing cross-vendor implementation. ⚠️ Maintained by the standard's own project — cite for what the format specifies and who implements it, never for how well it works. |
| SRC-269 | Saha, Shoumik; Faghih, Kazem; Feizi, Soheil — *Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry* (2026) · [link](https://arxiv.org/abs/2605.11418) | The security finding this entry's governance section rests on: because discovery and selection run on natural-language metadata, the description is the attack surface. Adversarial skills reached up to 86% pairwise win rate and 80% top-ten placement; description-only framing biased selection in 77.6% of paired trials; semantic evasion defeated blocking in 36.5–100% of cases. ⚠️ Preprint. |
| SRC-103 | Model Context Protocol project (Anthropic) — *What is the Model Context Protocol (MCP)?* (2024) · [link](https://modelcontextprotocol.io/docs/getting-started/intro) | The tool-connection layer this format is repeatedly confused with, and the basis for the instructions-versus-callable distinction. ⚠️ Vendor-originated specification. |
| SRC-069 | Anthropic — *Effective Context Engineering for AI Agents* (2025) · [link](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | The context-budget argument that makes progressive disclosure necessary rather than merely elegant. ⚠️ Vendor-authored. |
| SRC-071 | Osmani, Addy (O'Reilly Radar) — *Agent Harness Engineering* (2026) · [link](https://www.oreilly.com/radar/agent-harness-engineering/) | Situates loadable capability inside the harness layer — what the control layer offers the model, rather than a property of the model. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Treat skill installation as dependency installation: allowlist, pin versions, read the bundled scripts as code, and verify permission behavior in the client you actually run. |
| **Organizational** | A skill is functionally an executing dependency, currently adopted through documentation channels where no dependency review exists. The standard says governance is left to you — so if you do not impose it, nobody has. |
| **Client-facing** | Explains how an assistant can be given your organization's procedures without retraining, and what assurance that does and does not come with. |
| **LLM-native** | Instructions, not functions. Progressive disclosure keeps many skills affordable — and because selection runs on the description, the description is the attack surface. |

---

*Last updated: v1.0 · September 2026*
