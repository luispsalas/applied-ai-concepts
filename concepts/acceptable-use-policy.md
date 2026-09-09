<!--meta
category: Observability & Governance
short: The rules about what a system may be used for — one set written by you, and one written by your provider that changes without asking you
aliases: [AUP, usage policy, acceptable use, usage policies, permitted use, prohibited use, terms of use, what are we allowed to use it for]
tags: [Data Governance, Regulatory, Ethics]
established: established
-->
# Acceptable Use Policy

> **Term status — Established.** A long-standing term of art in IT and telecommunications governance, applied to AI without redefinition.

## One-line essence
The document stating what a system may and may not be used for — and in AI there are always two of them, one you write and one your provider writes.

---

## Technical definition

An acceptable use policy states permitted and prohibited uses of a service, and the consequences of breaching them. The form predates AI by decades; what changes in an AI context is that **two policies are always in force at once, and only one of them is yours.**

**The provider's AUP is a constraint on your deployment that you do not control.** Every major model provider publishes one, prohibiting categories of use, and it binds you as a condition of access. **It is a living document, revised unilaterally**, so the boundary of what your product is permitted to do can move without any change on your side and without your involvement.

**That is the AI-specific governance fact and the reason this entry exists.** A conventional dependency changes behavior when you upgrade it. **A provider AUP changes what you are contractually allowed to do, at a time the provider chooses** — and a use that was permitted at launch may not be permitted at renewal. Nothing in your system reports this ([model version and update](model-version-update.md), [supply chain risk](supply-chain-risk-ai.md)).

**Your own AUP does different work: it converts principle into an enforceable statement about specific systems.** It is usually the first governance artifact an organization actually writes — earlier than a policy framework, an inventory or a risk process — because it answers the question employees are already asking ([AI governance](ai-governance.md)).

**Its characteristic failure is being written against tools rather than against uses.** A policy naming permitted products dates the moment someone adopts a new one, and it says nothing about the thing that actually matters — what data may go in, and what the output may be relied on for. **Policies written this way produce [shadow AI](shadow-ai.md) rather than preventing it**, because they answer a question nobody asked while leaving the real one open.

**An AUP is not a control.** It is a statement of intent that assigns responsibility. Whether behavior follows depends on awareness, on whether a compliant path exists, and on enforcement — and a policy with none of those is a document that transfers blame to individuals ([moral crumple zone](moral-crumple-zone.md)).

---

## Plain-language version

An acceptable use policy says what a system may and may not be used for. Nothing about that is new — every company has had one for its network for thirty years. What is different with AI is that **there are always two, and you only wrote one of them.**

**The one you did not write belongs to your model provider.** Every major provider publishes rules about what you may use their model for, and accepting them is a condition of access. Those rules are revised **when the provider decides**, not when you are ready. So the boundary of what your product is allowed to do can move without you changing a line of code, and without anyone telling your team.

That is worth sitting with, because it is unlike a normal dependency. When a library changes, your software behaves differently and your tests notice. When a provider's usage policy changes, **your software behaves identically and is now possibly non-compliant.** Nothing in your monitoring will tell you.

**The one you do write is usually the first AI governance document your organization produces** — before any framework or inventory — because employees are already using these tools and asking what they are allowed to do.

The most common way it fails is being written about **tools instead of uses**. A policy that lists approved products is out of date the week someone finds a new one, and it never answers the questions that actually matter: what information may I put in, and what may I rely on the answer for? **Policies like that tend to create unsanctioned use rather than prevent it**, because people with a real task and no permitted route will find another one.

Last thing, and it matters: **a policy is not a control.** It states intent and assigns responsibility. If nobody knows it exists, no compliant route is available, and nothing is enforced, then what it mostly does is move blame onto whoever gets caught.

---

## AI literacy notes

1. **Two policies always apply** — yours and your provider's.
2. **The provider's changes unilaterally**, and nothing in your system reports it.
3. **A permitted use can become prohibited** with no change on your side.
4. **Write about uses and data, not about named tools** — tool lists date immediately.
5. **It is usually the first governance artifact written**, and often the only one for a while.
6. **A policy is not a control**; without a compliant route it produces shadow AI.
7. **Prohibitions without alternatives push usage out of view** rather than stopping it.
8. **Enforcement, awareness and a permitted path** are what convert a policy into behavior.

---

## Governance notes

**Core question:** When our provider last changed its usage policy, would we have noticed — and is anything we do today still permitted under it?

**Watch for:**
- No one assigned to track provider usage-policy changes ([supply chain risk](supply-chain-risk-ai.md))
- An internal AUP naming specific tools, already out of date ([shadow AI](shadow-ai.md))
- Prohibitions with no sanctioned alternative for the underlying need
- A policy nobody has read since onboarding, cited after an incident to locate fault ([moral crumple zone](moral-crumple-zone.md))
- Silence on the two questions people actually have: what data may go in, what may the output be used for
- Provider terms accepted at signup and never re-read at renewal or expansion
- No route to ask whether a novel use is permitted, so people decide alone
- Policy scope covering approved deployments but not the model access individuals already have

**Practice:**
- **Assign ownership for monitoring provider usage-policy changes**, and re-read them at renewal — this is the control that does not exist in most organizations
- **Write about data classes and use categories, not product names**, so the policy survives the next tool
- Answer the two live questions explicitly: what may go in, and what may the output be relied on for
- **Provide a sanctioned route for every prohibition** — a ban without an alternative relocates the behavior ([shadow AI](shadow-ai.md))
- Give people a way to ask about an unlisted use, and record the answers so precedent accumulates
- Map your own AUP against provider constraints, so you never permit internally what your supplier prohibits
- Treat the policy as one layer among several rather than as the control itself ([guardrails](guardrails-ai-systems.md), [permission model](permission-model-ai.md))

**Key accountability owner:** whoever owns the vendor relationship — because the provider's AUP is the half of this that changes without notice, and the half nobody is usually watching.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanics, and this entry is deliberately light on evidence about effect.** That providers publish usage policies, bind access to them, and revise them unilaterally is directly verifiable from the policies themselves, which are cited here. **The claims about how internal policies fail — tool lists dating, prohibitions producing shadow AI, policies functioning as blame allocation — are reasoned from the corpus's own entries and from general organizational practice, not measured.** They are stated as failure modes to watch for rather than as findings. **No source here establishes that any AUP formulation changes behavior**, and the entry's strongest claim is structural rather than empirical: a policy without awareness, a permitted route, or enforcement assigns responsibility without altering what people do.

---

## Related concepts

- [AI Governance](ai-governance.md) — the framework an AUP is usually the first piece of
- [Shadow AI](shadow-ai.md) — what prohibitions without alternatives produce
- [Compliance (AI Systems)](compliance-ai-systems.md) — where policy meets external obligation
- [Supply Chain Risk (AI)](supply-chain-risk-ai.md) — the provider-side terms you inherit and do not control
- [Model Version & Update](model-version-update.md) — the other thing a provider changes without asking
- [Permission Model (AI)](permission-model-ai.md) — the technical control a policy cannot substitute for
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — enforcement that does not rely on people reading a document
- [Moral Crumple Zone](moral-crumple-zone.md) — what a policy becomes when it is only cited after incidents
- [AI Literacy](ai-literacy.md) — the awareness a policy depends on to function
- [Data Minimization](data-minimization.md) — the substance behind "what data may go in"

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-313 | Anthropic — *Usage Policy* · [link](https://www.anthropic.com/legal/aup) | A live provider acceptable use policy: the categories of prohibited use, and the fact that acceptance is a condition of access. Cited as **evidence that the artifact exists and binds deployers**, not for the merits of any particular restriction. ⚠️ Vendor document and a **living one** — it is revised unilaterally, which is precisely this entry's point, and makes it a source with high decay by design. |
| SRC-314 | OpenAI — *Usage Policies* · [link](https://openai.com/policies/usage-policies/) | A second provider's policy, establishing that this is a **structural feature of the market rather than one company's practice** — every deployer operates under terms they did not write. ⚠️ Vendor document, living, revised without notice to deployers. Returns 403 to automated clients; consult the archived snapshot or a browser. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | The Govern function under which acceptable-use policy sits as an organizational control — establishing it as a recognized governance artifact rather than an informal document. |
| SRC-129 | European Parliament / Council of the EU — *EU Artificial Intelligence Act (Regulation (EU) 2024/1689)* · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The regulatory backdrop that makes intended purpose a legally operative concept — a use restriction is not only contractual, and changing a system's intended purpose has consequences under Article 25. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Your provider's usage policy can change what you are permitted to do with no change to your code and no signal in your monitoring. |
| **Organizational** | Assign someone to watch provider policy changes and re-read terms at renewal. Write about data and uses, never about named tools. |
| **Client-facing** | Explains what an organization has actually committed to, and what it cannot promise because a supplier controls it. |
| **LLM-native** | Every prohibition needs a sanctioned route for the same need, or it relocates the behavior instead of stopping it. |

---

*Last updated: v1.0 · September 2026*
