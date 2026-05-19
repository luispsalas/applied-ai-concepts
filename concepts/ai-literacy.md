# AI Literacy

## One-line essence
The competencies required to engage with, use, and govern AI systems responsibly — at an individual, team, and organizational level.

---

## Technical definition

AI literacy is the ensemble of knowledge, skills, and critical capacities that allow individuals and organizations to engage with AI systems effectively and responsibly. It is not a single competency but a structured set of domains that operate at different levels of depth.

The OECD/EC AI Literacy Framework (2025) defines four domains:

1. **Engage with AI** — understanding what AI is and how it works at a conceptual level; recognizing AI-generated content; maintaining critical judgment when interacting with AI outputs
2. **Create with AI** — using AI tools effectively for tasks; prompting, iterating, and evaluating outputs; understanding the limits of model capability
3. **Manage with AI** — integrating AI into workflows and decision-making; understanding organizational implications; governance and accountability awareness
4. **Design AI** — technical and system-level competencies for those who build, configure, or deploy AI systems

Long & Magerko (2020) identified five competency clusters that map across these domains: understanding AI capabilities and limitations, understanding how AI learns, understanding the societal implications of AI, critically evaluating AI outputs, and designing or working with AI systems. These clusters have been foundational to AI literacy curriculum design.

At an organizational level, literacy operates at three tiers:
- **Awareness literacy** — sufficient understanding to use AI tools safely and recognize their limitations; required for all staff using AI tools
- **Operational literacy** — the competencies required to integrate AI into professional workflows, evaluate outputs, and make AI-assisted decisions; required for practitioners and knowledge workers
- **Governance literacy** — understanding of AI risk, accountability structures, regulatory context, and organizational control mechanisms; required for leaders, governance functions, and risk owners

AI literacy is the complement to technical capability: a technically capable AI system deployed without organizationally literate users produces unreliable outcomes. The gap between model capability and user understanding is where most organizational AI failures originate.

---

## Plain-language version

AI literacy is what people need to understand to work with AI well — not just to use the tools, but to use them correctly, to spot when they're wrong, and to understand what it means for the organization that they're using them at all.

It is not the same as knowing how to use a specific AI product. A person can use an AI tool fluently and still lack AI literacy — if they don't understand when to verify outputs, why confidence is not a reliability signal, or what governance questions their use of the tool raises.

Literacy is what makes AI adoption durable: when users understand the technology at a working level, the organization can set appropriate expectations, catch failures, and course-correct.

---

## AI literacy notes

AI literacy is the precondition that most organizations skip, and the failure point most organizations encounter. Deploying capable AI tools into an organization without a baseline literacy program is not technology adoption — it is risk transfer to users who do not know they are accepting it.

Three things practitioners need to understand:

1. **Literacy is tiered — and different roles need different tiers.** A customer service representative using an AI drafting tool needs awareness literacy: they need to know outputs require review, not the mechanics of transformer architecture. A data steward designing a knowledge base for a RAG system needs operational literacy. A Chief Risk Officer approving AI deployment needs governance literacy. One-size-fits-all literacy programs address none of these adequately.
2. **AI literacy changes what people do, not just what they know.** The test of literacy is behavioral: does a user verify AI outputs before using them in a consequential decision? Do they recognize hallucinated confidence? Do they know when to escalate a governance question? Literacy programs that produce knowledge without changing behavior have not produced literacy.
3. **The labor market is restructuring around AI competency — and the timeline is compressing.** Research on AI and labor market impact suggests that AI literacy is becoming a baseline employment competency, not a specialist credential. Organizations that do not build this capability are building an organizational deficit that will compound.

---

## Governance notes

**Core question:** Does your organization have a named owner for AI literacy — someone responsible for defining what different roles need to understand, assessing current capability gaps, and building the program to close them?

**Watch for:**
- AI deployment outpacing AI literacy: tools in production before users have the competencies to use them responsibly. The gap appears as unrealistic expectations, poor output verification, and unrecognized governance exposure.
- Literacy treated as a one-time training event rather than a capability that must be maintained and updated as AI systems evolve. A literacy program designed for 2023 models does not address agentic AI, multimodal systems, or the governance requirements of 2026 deployment contexts.
- Governance literacy concentrated only at the technical layer: IT and data teams understand AI risk; leadership and business functions do not. Governance decisions made by literacy-deficient stakeholders produce governance gaps that technical controls cannot close.

**Practice:**
- Define minimum literacy requirements by role tier: what every employee using AI tools must understand, what practitioners integrating AI into workflows must understand, and what leaders approving AI deployment must understand.
- Treat literacy as a continuous program: update content as models, tools, and regulatory requirements evolve; assess baseline literacy before major AI deployments; measure behavioral outcomes, not completion rates.

**Key accountability owner:** AI literacy owner — the role (individual or function) responsible for defining organizational literacy requirements, designing and delivering programs, and maintaining the capability as AI systems and regulatory context evolve.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Established, developing.** The foundational competency clusters (Long & Magerko, 2020) are stable and widely cited. The OECD/EC framework (2025) provides current institutional consensus on domain structure. Organizational literacy tiers and labor market implications are active research areas. Specific curriculum standards and assessment methodologies are nascent.

---

## Related concepts

- [Hallucination](hallucination.md) — understanding hallucination is the highest-impact single literacy concept for non-technical users; it changes how outputs are used
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — HITL design only functions if the humans in the loop have sufficient literacy to exercise meaningful judgment
- [AI Governance](ai-governance.md) — governance frameworks require literacy to be operational; ungoverned AI and literacy-deficient AI often co-occur
- [Context Engineering](context-engineering.md) — operational literacy includes the ability to frame requests effectively and understand how context shapes outputs
- [Observability](observability.md) — governance literacy includes understanding what should be monitored, why, and what the signals mean
- [Persistent Synthesis](persistent-synthesis.md) — the synthesis model this wiki is built on is itself a literacy practice: compiling understanding rather than accumulating information

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-067 | OECD/European Commission — *AI Literacy Framework* (May 2025) · [link](https://www.oecd.org/en/publications/oecd-ec-ai-literacy-framework_3440f3db-en.html) | Four-domain framework (Engage/Create/Manage/Design); institutional definition of AI literacy competencies; policy and curriculum foundation. Joint OECD/EC publication — authoritative institutional source. |
| SRC-068 | Long, D. & Magerko, B. — *What is AI Literacy? Competencies and Design Considerations* (CHI 2020) · [link](https://dl.acm.org/doi/10.1145/3313831.3376727) | Foundational competency cluster taxonomy (capabilities, learning, societal implications, critical evaluation, design); widely cited baseline for AI literacy curriculum design. Peer-reviewed. |
| SRC-056 | Anthropic — *The Impact of AI on the Labor Market* (2025) · [link](https://www.anthropic.com/research/impact-ai-labor-market) | AI literacy as an emerging baseline employment competency; structural shift in labor market requirements; organizational implications of literacy deficits at workforce scale. Vendor-produced — use as background reference for labor market framing; not cited as an independent authority. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Relevant in two directions: as a concept to understand (what does literacy mean, who needs what), and as a design constraint (systems must be designed for the literacy level of their actual users). |
| **Organizational** | The entry most directly addressed to organizational leaders. AI adoption without literacy planning produces predictable failures. Literacy ownership is a governance question with a named answer. |
| **Client-facing** | Foundational for any client conversation about AI readiness. "Is your organization AI-ready?" is a literacy question as much as a technology question. |
| **LLM-native** | Provides the framing for why concepts in this wiki are structured the way they are — each entry is designed to build a specific tier of literacy for a specific audience. |

---

*Last updated: v1.0 · May 2026*
