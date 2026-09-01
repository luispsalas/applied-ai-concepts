<!--meta
category: Reliability & Quality
short: Generation scales and verification does not — and the documented harm is fraud and intimate imagery, not mainly politics
aliases: [deepfake, AI-generated video, voice cloning, fake audio, manipulated media]
tags: [Security, Ethics, Regulatory]
-->
# Synthetic Media (Deepfakes)

## One-line essence
Convincing fabricated audio, image and video — and the practical problem that verifying what is real is now harder than producing what is not.

---

## Technical definition

AI-generated or AI-manipulated audiovisual content depicting people, events or objects in ways that did not occur. *Synthetic media* is the broad category; *deepfake* conventionally names the subset that depicts a real, identifiable person doing or saying something they did not.

**The structural problem is a cost asymmetry.** Producing convincing synthetic media has collapsed in cost — minutes, no expertise, commodity tools. Verifying whether a specific artifact is genuine has not: it requires provenance infrastructure, detection tooling, or investigative effort per item. **Generation scales; verification does not.** Every other difficulty here follows from that gap.

**What people can actually do, measured.** The most useful evidence is a 15,016-participant study comparing ordinary people against the leading detection model of its time. Three findings, and the third is the one usually missed:

- **Participants and the model were similarly accurate — while making different kinds of mistakes.** Humans were disrupted by manipulations targeting visual face processing that mostly did not affect the model.
- Combining them helped: *"participants with access to the model's prediction are more accurate than either alone."*
- **But *"inaccurate model predictions often decrease participants' accuracy."*** A wrong detector actively makes a human reviewer worse — [automation bias](automation-bias.md), measured directly in an authenticity task. Handing detection tooling to reviewers is not a safe default.

**Detection is the weakest available control**, and the [provenance](content-provenance-watermarking.md) entry's asymmetry applies with full force: a positive result is informative, a negative one is not. Detection generalizes poorly to generation methods it was not trained on, and the field is adversarial — improvements in detection inform generation.

**The harm is not primarily deception, and this is the part most treatments miss.** Documented harms concentrate in **non-consensual intimate imagery** and in fraud — voice-cloned social engineering against individuals and finance functions. A third harm needs no successful fake at all: the *liar's dividend*, where the existence of plausible synthetic media lets genuine evidence be dismissed as fabricated. **A defense built only around detecting fakes does not address that one.**

**Regulation has arrived on disclosure, not on generation.** EU AI Act Art. 50(4) requires deployers to disclose deepfakes, narrowed for artistic, creative and satirical work, alongside the Art. 50(2) machine-readable marking duty on providers.

---

## Plain-language version

Convincing fake audio, images and video are now cheap and easy to make. Checking whether a particular clip is real is not — it still takes tools, infrastructure or someone's time, one item at a time.

That imbalance is the whole problem. Making them got a thousand times easier; checking them did not.

People are not hopeless at spotting fakes — in a large study, ordinary participants did about as well as the best detection software of the time, and interestingly they made *different* mistakes, so together they were better than either alone. But there is a catch that matters enormously: when the software was wrong, it often made the humans wrong too. A confident bad answer is worse than no answer.

It is also worth being clear about where the actual harm lands. Public discussion focuses on political misinformation; the documented damage concentrates in fabricated intimate imagery of real people and in fraud — a cloned voice calling a finance team or a family member.

And there is a harm that needs no fake at all. Once everyone knows convincing fakes exist, anyone caught on genuine recording can call it fabricated. Detecting fakes does nothing about that.

---

## AI literacy notes

1. **Generation scales, verification does not.** That asymmetry is the concept. It will not be closed by better detection, because detection is per-item and generation is not.
2. **A negative detection means nothing.** No mark found, no detector hit — neither is evidence of authenticity. Only a positive result carries information.
3. **A wrong detector makes reviewers worse**, measurably. Detection tools handed to people without training in their failure modes can reduce accuracy rather than raise it.
4. **Humans and detectors fail differently**, which is why combining them helps — but only when the human can override, and only when they know the tool is fallible.
5. **The documented harm is intimate imagery and fraud**, not primarily political deception. Any response scoped only to misinformation misses where the damage actually falls.
6. **The liar's dividend needs no fake.** Plausible deniability for genuine evidence is a harm produced by the *existence* of the technology, and detection cannot address it.
7. **Provenance beats detection where you control the pipeline.** Proving what *is* real is more tractable than proving what is fake — which is why the infrastructure investment goes into signing authentic content, not into catching fabricated content.

---

## Governance notes

**Core question:** Where does your organization rely on audio or video being genuine — and what would happen if it were not?

**Watch for:**
- Voice or video used as an authentication or authorization factor, formally or informally — the "I recognized their voice" approval is the highest-value target and rarely a written control
- Payment, credential and access processes with no out-of-band verification step, where a convincing call is sufficient to act
- Detection tooling deployed to reviewers with no training in its failure modes, which the evidence says can make outcomes worse
- Absence of a mark read as authenticity in verification workflows
- Response scoped to misinformation only, leaving intimate-imagery and fraud harms unaddressed
- No plan for the liar's dividend — a genuine recording being dismissed as synthetic — which needs an evidentiary answer, not a detection one
- Executive and public-facing staff whose voice and likeness are abundantly available, with no acknowledgment that this is an exposure

**Practice:**
- **Remove voice and video from the trust path for anything consequential.** Out-of-band confirmation on a known channel, callback to a stored number, or a second approver — this is the single highest-value control and it is procedural, not technical
- Train the specific scenario, particularly for finance and executive-support functions; awareness of "deepfakes exist" does not transfer to recognizing an urgent call
- Where detection is used, train the failure modes with it, and ensure the human can override — a tool presented as authoritative degrades the reviewer
- Invest in [provenance](content-provenance-watermarking.md) for content you originate: signing what is real is more tractable than detecting what is not
- Assign the Art. 50(4) deployer disclosure duty to a named owner
- Have an evidentiary answer ready for the liar's dividend — chain of custody, signed originals, corroboration — since detection does not address it
- Include synthetic-media incidents in [incident](ai-incident-reporting.md) response with a defined path, rather than improvising during one

**Key accountability owner:** security and fraud prevention for the authentication exposure — which is where the measurable harm concentrates — with communications owning the response to fabricated content about the organization. **Not the AI team**, which owns neither the trust path nor the response.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md) — observability signals and cross-cutting accountability checklist.*

---

## Confidence level

**Medium-High.** The cost asymmetry is structural and uncontested, the human-detection evidence is peer-reviewed with a large sample, and the automation-bias finding is directly measured. **The dating problem is severe and stated deliberately:** that study's accuracy parity describes 2021-era video deepfakes and one detection model, and generation has advanced substantially — **do not quote the parity as current.** What transfers is the complementary-errors structure and the automation-bias result. Detection effectiveness in the wild is not well measured publicly, and prevalence figures circulate widely from vendor sources measuring salience; this entry cites none.

---

## Related concepts

- [Content Provenance & Watermarking (C2PA)](content-provenance-watermarking.md) — the infrastructure answer, and where the positive/negative asymmetry is set out
- [Verification](verification.md) — the practice this makes structurally harder, and the cost side of the asymmetry
- [Automation Bias](automation-bias.md) — why a wrong detector makes a reviewer worse
- [AI Disclosure (Attribution)](ai-disclosure-attribution.md) — the deployer duty under Art. 50(4)
- [Multimodal AI](multimodal-ai.md) — the capability that made cross-modal generation practical
- [Privacy (AI Systems)](privacy-ai-systems.md) — likeness and voice as personal data
- [Copyright & AI Output](copyright-ai-output.md) — the adjacent rights questions around likeness and voice
- [AI Incident (Reporting)](ai-incident-reporting.md) — where synthetic-media incidents get recorded and escalated
- [Human-in-the-Loop (HITL)](human-in-the-loop.md) — the reviewer whose accuracy a bad detector degrades
- [Permission Model (AI)](permission-model-ai.md) — out-of-band confirmation as an authorization control
- [AI Literacy](ai-literacy.md) — reading a negative detection correctly is a literacy skill, not a technical one
- [Anthropomorphism (AI)](anthropomorphism-ai.md) — a familiar voice is a trust signal that no longer carries information

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-210 | Groh, M.; Epstein, Z.; Firestone, C.; Picard, R. — *Deepfake detection by human crowds, machines, and machine-informed crowds* (PNAS 119(1), 2022) · [link](https://doi.org/10.1073/pnas.2110013119) | The measured baseline across 15,016 participants: comparable accuracy with complementary errors, a benefit from combination, and the finding that inaccurate model predictions often decrease human accuracy. ⚠️ 2021-era deepfakes; parity should not be quoted as current. |
| SRC-204 | European Parliament / Council of the EU — *EU AI Act, Article 50: Transparency obligations* (2024) · [link](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689) | The deployer duty to disclose deepfakes, its artistic/creative/satirical narrowing, and the provider marking duty alongside it. |
| SRC-205 | Coalition for Content Provenance and Authenticity — *C2PA Technical Specification v2.4* (2026) · [link](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html) | The provenance approach — proving what is real rather than detecting what is fake — with the spec's own statement that validation is not truthfulness. |
| SRC-174 | Goddard, K.; Roudsari, A.; Wyatt, J.C. — *Automation bias: a systematic review* (JAMIA, 2012) · [link](https://doi.org/10.1136/amiajnl-2011-000089) | The prior literature explaining why a confident wrong tool degrades human judgment rather than being ignored. |
| SRC-164 | McGregor, S. (XPRIZE Foundation / Partnership on AI / Syntiant) — *Preventing Repeated Real World AI Failures by Cataloging Incidents* (AAAI, 2021) · [link](https://ojs.aaai.org/index.php/AAAI/article/view/17817) | Cataloged harm as the alternative to projected harm — what has actually happened, rather than what is feared. |
| SRC-001 | NIST — *AI Risk Management Framework* · [link](https://www.nist.gov/itl/ai-risk-management-framework) | Places authenticity risk inside a measurable lifecycle rather than treating detection tooling as a control. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | Detection is the weakest control available. Invest in signing content you originate, and never present a detector to a reviewer as authoritative. |
| **Organizational** | The highest-value control is procedural: remove voice and video from the trust path for consequential actions, and require out-of-band confirmation. This belongs to fraud prevention, not the AI team. |
| **Client-facing** | Explains why "I recognized their voice" is no longer a control, and why verification processes now require a second channel. |
| **LLM-native** | Generation scales and verification does not — a gap detection cannot close. And the liar's dividend is a harm that requires no successful fake at all. |

---

*Last updated: v1.0 · August 2026*
