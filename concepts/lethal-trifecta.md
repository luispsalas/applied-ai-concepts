<!--meta
category: System Architecture
short: An AI agent that can read private data, take in untrusted content and communicate externally can be made to steal that data. Remove any one of the three and the theft path closes
aliases: [lethal trifecta for AI agents, Agents Rule of Two, rule of two, prompt injection exfiltration, data exfiltration risk]
tags: [Security, Agents]
established: established
-->
[Applied AI Concepts](../README.md) › [System Architecture](../glossary/categories.md#system-architecture) › Lethal Trifecta

# Lethal Trifecta

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
An AI agent that can read private data, take in untrusted content and communicate externally can be made to steal that data. Remove any one of the three and the theft path closes.

---

## Technical definition

Simon Willison named the combination in June 2025. An agent is exposed when it has all three of these at once:

1. **Access to private data**, which is one of the most common reasons to give an agent tools in the first place.
2. **Exposure to untrusted content**, which he defines as *"any mechanism by which text (or images) controlled by a malicious attacker could become available to your LLM"*.
3. **The ability to communicate externally** in a way that could carry data out.

With all three, an attacker does not need to break anything. They plant instructions in content the agent will read, and the agent follows them: it fetches the private data and sends it to the attacker. This works because of [prompt injection](prompt-injection.md). Models take instructions from whatever text reaches them and cannot reliably tell an operator's instructions from ones embedded in a web page, an email or a document, a weakness demonstrated against real systems since 2023 (Greshake et al.).

**The value of the term is that it turns a detection problem into a design decision.** Nobody can yet promise to catch every injected instruction. A designer can decide that one agent will never hold all three capabilities together, and that decision holds whatever the attacker writes. Willison's own list of exploited products shows the pattern from the other side: vendors mostly fixed each case by closing the channel the stolen data would have left through.

**The third leg is wider than it looks.** Willison notes that any tool able to make an HTTP request can carry data out, whether it calls an API, loads an image or offers the user a link to click. The 2026 incidents recorded in [Sandboxing](sandboxing.md) make the same point from the evaluation side. Agents allowed only to fetch pages still wrote to the web, through a wiki that accepted edits on ordinary page requests and through a public URL scanner that sent requests on their behalf. A capability labeled as read-only can still be a way out.

**Filtering does not close it.** Willison calls guardrail products that catch "95% of attacks" a failing grade, since an attacker only needs the remaining few. Research since supports him. Nasr et al. bypassed 12 recently published jailbreak and prompt-injection defenses with attack success above 90% for most of them, where most had originally reported near-zero success, by tuning their attacks to each defense. The formal results on [guardrails](guardrails-ai-systems.md) explain why no filter can promise complete coverage.

**Independent adoption has changed the third leg's scope.** Meta's *Agents Rule of Two* (October 2025) cites the trifecta and turns it into a rule: until prompt injection can be reliably detected and refused, an agent should hold no more than two of three properties within a session. Those are processing untrustworthy inputs, access to sensitive systems or private data, and changing state or communicating externally. If a task needs all three, the agent should not run autonomously and needs human approval or another reliable check. A Los Alamos position paper uses the term in the same broadened form, with "external action capability" as the third leg. **The broadening matters:** Willison's version is about data theft, while the later versions also cover an injected instruction that deletes, buys or publishes something. Willison welcomed the change, because the trifecta does not cover injected actions that change state. He objected to one detail: the rule's diagram labeled untrusted input combined with the power to change state as safe, when that pairing can do harm with no private data involved. Meta then relabeled the two-property overlaps as "lower risk". **Two legs out of three lowers the risk without removing it.**

**Design patterns can keep an agent useful without the full combination.** A cross-industry paper by Beurer-Kellner et al. states the governing principle: *"once an LLM agent has ingested untrusted input, it must be constrained so that it is impossible for that input to trigger any consequential actions."* It proposes six patterns that apply it. In one, the agent selects actions without ever reading their results. In another, it fixes its plan before reading any untrusted content. A third splits the work between a privileged model that plans and a quarantined model that reads. CaMeL (Debenedetti et al., IEEE SaTML 2026) builds the separation into a layer around the model. It extracts the control and data flow from the trusted request, so untrusted data cannot change what the program does, and it blocks private data from leaving through unauthorized flows. On the AgentDojo benchmark it solved 77% of tasks with provable security, against 84% for an undefended agent. That gap is the price of the guarantee.

---

## Plain-language version

Imagine an assistant that manages your email. To be useful it reads your inbox, which holds private things. It also reads every new message, including ones from strangers. And it can send email.

Now a stranger sends a message telling the assistant to forward your password-reset emails to an address the stranger controls. The assistant cannot reliably tell those instructions from yours, so there is a real chance it does exactly that.

The lethal trifecta names the three ingredients that made this possible: private data, content from people you do not trust, and a way to send things out. With all three in one place, someone can steal your data just by getting text in front of the assistant. Take away any one of them and that particular attack stops working. The assistant might only read mail from known senders, or never touch your private files, or be unable to send anything without asking you first.

---

## AI literacy notes

1. **It is an architecture risk.** A better model does not remove it, because models follow instructions in whatever they read. The fix lies in how capabilities are combined.
2. **Each leg is usually there for a good reason.** Private data is why the agent is useful, untrusted content is most of the outside world, and communication is how it gets things done. The risk comes from the combination, which is why it is easy to build by accident.
3. **External communication includes things that do not look like sending.** Loading an image, following a link or fetching a URL can all carry data out.
4. **Connecting tools yourself can assemble the trifecta.** Each tool can be safe on its own and the combination still dangerous. When users mix tools from different sources, no single vendor sees the whole picture.
5. **A detection rate is not protection.** A filter that catches most attacks still lets through the ones an attacker tunes against it.
6. **Removing one leg is a real control.** Of the defenses discussed here, it is the one that does not depend on recognizing the attack.
7. **Two versions of the rule are in use.** The original counts external communication, while later versions count any change of state. Check which one a guideline means before relying on it.

---

## Governance notes

**Core question:** For each agent we run, can a single session read private data, take in content from outside our control, and act or communicate beyond our boundary? If all three, who approved that, and what stands in for the missing protection?

**Watch for:**
- An agent given a new tool or connector without anyone rechecking which of the three legs it now holds
- External communication counted only as sending messages, missing image loads, link previews, URL fetches and services that make requests on the agent's behalf ([sandboxing](sandboxing.md))
- A vendor's filter or guardrail cited as the reason a full trifecta is acceptable ([guardrails](guardrails-ai-systems.md))
- Untrusted content entering through channels nobody labeled as untrusted, such as shared documents, tickets, issue trackers, calendar invites and retrieved web pages
- The legs split across sessions on paper but reunited through persistent memory or shared files that carry content from one session into another ([memory](memory-ai-systems.md))
- Users wiring their own tools together, outside any design review
- Two-leg configurations treated as safe. Untrusted input plus the power to act can still do damage without any private data

**Practice:**
- **Inventory the three legs per agent, per session**, and record which ones each tool adds. A new tool is a change to this inventory.
- **Break the combination by design where you can**: restrict the agent to trusted sources, keep it away from private data, or remove its ability to communicate or act externally.
- Where all three are genuinely needed, **require human approval or another reliable validation for consequential actions** ([human-in-the-loop](human-in-the-loop.md))
- Enforce the missing leg in the environment, at the network and permission layer, rather than in the prompt ([permission model](permission-model-ai.md))
- Treat filtering as an extra layer that reduces attack rates. Never use it as the reason a full trifecta is allowed.
- State which version of the rule your policy uses: theft of data only, or any change of state.

**Key accountability owner:** whoever approves an agent's tools and connections, because the trifecta is assembled one grant at a time, often by people who each saw only one of them.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High on the mechanism, medium on the remedies.** That injected instructions in untrusted content can steer an agent is peer-reviewed and repeatedly demonstrated, and the term is used independently by a major developer's published guidance and by research authors outside its originator. The term itself comes from a practitioner's blog, and most research using it is preprint. **The trifecta is a heuristic, not a measured threshold.** It names the conditions for one class of harm, data theft, and nobody has measured how often a full trifecta is exploited in practice. The design patterns and CaMeL show that agents can stay useful with the combination broken, measured on benchmarks rather than in deployment. The adaptive-attack results come from a preprint and concern the defenses tested, not every possible defense.

---

## Related concepts

- [Prompt Injection](prompt-injection.md) — the mechanism the trifecta depends on: instructions taken from content the agent was only meant to read
- [Sandboxing](sandboxing.md) — where the external-communication leg is enforced or lost, including routes that look like reading
- [Guardrails (AI Systems)](guardrails-ai-systems.md) — why filtering cannot substitute for removing a leg
- [Data Leakage (AI Systems)](data-leakage-ai-systems.md) — the harm the original trifecta describes
- [AI Agent](ai-agent.md) — tool use is what brings all three legs into one system
- [Tool Use](tool-use.md) — each tool can add a leg, and the combination is what matters
- [Permission Model (AI)](permission-model-ai.md) — where a missing leg is enforced rather than requested
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the fallback when all three are genuinely required
- [Agentic Design Patterns](agentic-design-patterns.md) — patterns that keep an agent useful with the combination broken
- [Memory (AI Systems)](memory-ai-systems.md) — how legs separated by session can meet again

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-392 | Willison, Simon — *The lethal trifecta for AI agents: private data, untrusted content, and external communication* (June 16, 2025) · [link](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) | The term and its three legs, the quoted definition of untrusted content, the breadth of the external-communication leg, the pattern of vendor fixes closing the exit, and the "95% of attacks" argument against filters. ⚠️ Practitioner blog post. |
| SRC-393 | Meta AI — *Agents Rule of Two: A Practical Approach to AI Agent Security* (October 31, 2025) · [link](https://ai.meta.com/blog/practical-ai-agent-security/) | Independent adoption by a major developer: no more than two of three properties per session, human approval when all three are needed, and the broadened third leg. ⚠️ Vendor guidance, not evidence of effectiveness. |
| SRC-394 | Bhattarai, M.; Vu, M. (Los Alamos National Laboratory) — *Trustworthy Agentic AI Requires Deterministic Architectural Boundaries* (2026) · [link](https://arxiv.org/abs/2602.09947) | Independent research use of the term, with "external action capability" as the third leg, and the argument that training-based defenses cannot give deterministic guarantees. ⚠️ Preprint; position paper. |
| SRC-395 | Beurer-Kellner, L.; Buesser, B.; Creţu, A.-M.; Debenedetti, E.; Dobos, D.; Fabian, D.; Fischer, M.; Froelicher, D.; Grosse, K.; Naeff, D.; Ozoani, E.; Paverd, A. et al. — *Design Patterns for Securing LLM Agents against Prompt Injections* (2025) · [link](https://arxiv.org/abs/2506.08837) | The quoted governing principle and six design patterns that trade utility for resistance to injection. ⚠️ Preprint; does not use the term. |
| SRC-396 | Debenedetti, E.; Shumailov, I.; Fan, T.; Hayes, J.; Carlini, N.; Fabian, D.; Kern, C.; Shi, C.; Terzis, A.; Tramèr, F. — *Defeating Prompt Injections by Design* (IEEE SaTML 2026) · [link](https://arxiv.org/abs/2503.18813) | CaMeL: control and data flow fixed by the trusted request, capabilities blocking unauthorized flows of private data, 77% of AgentDojo tasks with provable security against 84% undefended. ⚠️ Authors from Google and ETH; one benchmark. |
| SRC-397 | Nasr, M.; Carlini, N.; Sitawarin, C.; Schulhoff, S.V.; Hayes, J.; Ilie, M.; Pluto, J.; Song, S.; Chaudhari, H.; Shumailov, I.; Thakurta, A.; Xiao, K.Y. et al. — *The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections* (2025) · [link](https://arxiv.org/abs/2510.09023) | Adaptive attacks bypassing 12 published defenses with success above 90% for most, where most had reported near-zero. ⚠️ Preprint; read at abstract level. |
| SRC-402 | Willison, Simon — *New prompt injection papers: Agents Rule of Two and The Attacker Moves Second* (November 2, 2025) · [link](https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/) | The originator's response to the broadened rule: welcoming state change as a third property, objecting that untrusted input plus state change had been labeled safe, and recording Meta's relabeling to "lower risk". ⚠️ Practitioner blog post. |
| SRC-146 | Greshake, K. et al. — *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* (2023) · [link](https://arxiv.org/abs/2302.12173) | The underlying mechanism: instructions embedded in retrieved content, demonstrated against real systems. |
| SRC-389 | Nightingale Collective (Von Arx, S.; Slade Byrd, C.; Kitts, S.; Larsen, T.) — *Discovery of a new OpenAI agent message board* (September 2026) · [link](https://collusion.wiki/) | Agents limited to fetching pages writing to the web anyway, showing how wide the communication leg is. ⚠️ Independent investigation; attribution is the authors' inference. |
| SRC-390 | Howard-Jones, Rowan (swarmcha.se) — *OpenAI agents tried to bruteforce a UN website's API fields* (September 2026) · [link](https://swarmcha.se/posts/openai-unctad) | A public URL scanner used to send requests on the agents' behalf, another exit that did not look like one. ⚠️ Independent blog post; attribution inferred. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Inventory the three legs per agent and per session, enforce the missing one in the environment, and treat every new tool or connector as a change to that inventory. |
| **Organizational** | The trifecta is assembled one approval at a time. Someone has to own the combined view of what each agent can read, ingest and reach. |
| **Client-facing** | Explains why an assistant may refuse to combine some tasks, or ask before sending anything, even when each task alone looks harmless. |
| **LLM-native** | Models follow instructions in content. Until that changes, the safe design is a system in which injected instructions have nothing worth stealing or no way to send it. |

---

*Last updated: v1.0 · October 2026*
