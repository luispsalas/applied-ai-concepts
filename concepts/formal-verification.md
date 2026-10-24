<!--meta
category: Reliability & Quality
short: Proving a claim with software that checks every logical step. The result is as trustworthy as the statement that was proved and the checker that checked it
aliases: [proof assistant, theorem prover, interactive theorem proving, formal proof, machine-checked proof, Lean, autoformalization, proof kernel]
tags: [Evaluation, Safety]
established: established
-->
[Applied AI Concepts](../README.md) › [Reliability & Quality](../glossary/categories.md#reliability--quality) › Formal Verification

# Formal Verification

> **Term status — Established.** A recognized term of art, in independent use beyond any single originator.

## One-line essence
Proving a claim with software that checks every logical step. The result is as trustworthy as the statement that was proved and the checker that checked it.

---

## Technical definition

A formal proof is a proof checked all the way down to the foundations of mathematics and the rules of logic. Because that takes far too many steps to do by hand, it is done by software called a proof assistant. The idea is old: de Bruijn's Automath appeared in 1967 and Mizar in 1973, followed by systems such as Coq, Isabelle and HOL Light, and Lean in 2013 (Avigad et al., 2025).

**How it works in practice.** A person, or now an AI system, writes the statement of a theorem in the assistant's language, then writes instructions, called tactics, that build the proof step by step. The finished proof is *"checked for correctness by Lean's trusted kernel"*, a small core program whose only job is to confirm that every step follows. Large shared libraries make this practical; Lean's Mathlib held more than 80,000 definitions and 160,000 theorems in early 2025.

**Why it matters for AI.** A kernel check does not care who or what wrote the proof. That makes formal verification one of the few ways to accept an AI system's mathematical output without trusting the AI, and it has become central as models produce more mathematics. Turning an ordinary paper into a formal proof with AI, called autoformalization, became practical in 2026 according to Thomas Hales, a leading figure in the field.

**What a formal proof guarantees is narrower than it looks.** Three gaps remain, and each has a documented 2026 case.

**1. The statement can be wrong.** The kernel checks that the proof proves the statement as written, not that the statement means what you intended. Hales puts the rule plainly: *"Lean proofs should never be believed until they have been checked by the kernel. Additionally, a proof in Lean should not be accepted until a human audit is performed to ensure statement fidelity."* That audit asks whether the theorem and every definition it relies on are the ones you meant. He adds that it is generally much easier than checking the proof itself.

**2. The checker can be wrong.** A soundness bug is a bug in the kernel that lets a proof of a false statement through, and therefore a proof of anything. In the summer of 2026 several were found in Lean. One let a *"sorry-free 'disproof' of the Collatz conjecture, produced with AI assistance"* pass the kernel. Others were found by OpenAI's internal models, working with the Lean project, until *"the internal AI reported it could not find additional issues."* All were fixed. According to the project's postmortem they were *"only reachable through metaprogramming"*, so ordinary proofs were not affected. An independent kernel, nanoda, caught all of the ones OpenAI's model found, but the Collatz proof had also passed a week-old version of nanoda. The project's response is to ship several independent kernels and a mode that rechecks a proof with all of them. Its lead states the threat model directly: *"We consider AI-generated proofs a potential source of malicious proofs."* Hales notes that cross-checking with several kernels reduces doubt without removing it.

**3. Not everything is inside the kernel.** Some proofs rely on computations run outside the checker. One 2026 paper on an Erdős problem states that earlier large searches had been run, but *"those computations sit outside any proof kernel"*, and it then gave a smaller result checked end to end. A claim of formal verification is only as strong as the part that was actually checked.

**Correct is also not the same as credited.** When an OpenAI system produced a counterexample to an Erdős conjecture in 2026, a group of mathematicians published a short, human-verified version of the argument and noted that it relied on ideas that could be attributed, at least in retrospect, to earlier work. Checking that a result holds and checking where it came from are separate tasks, and only the first is done by a kernel.

---

## Plain-language version

Formal verification means having a computer check a proof completely, one tiny logical step at a time, so that nothing is taken on trust. Mathematicians use it to be certain a proof has no gaps, and it matters more now that AI systems produce proofs, because the checker does not need to trust whoever wrote the proof.

It is very strong, and it has three limits. The computer checks that the proof proves the statement it was given, so a person still has to confirm the statement says what they meant. The checker is itself software, and in 2026 several bugs in a popular one let false "proofs" through. They were found with the help of AI and fixed. And some proofs lean on calculations done outside the checker, which are only as reliable as the code that ran them.

So "formally verified" is a strong claim, but you still need to know what exactly was verified and by what.

---

## AI literacy notes

1. **The kernel checks the proof, not the meaning.** A correct proof of the wrong statement is still a correct proof.
2. **Statement fidelity needs a human.** Someone has to confirm the theorem and its definitions say what was intended, and that check is usually far smaller than checking the proof.
3. **The checker is software and can have bugs.** In 2026, kernel bugs let false proofs through until they were fixed; independent kernels caught them.
4. **Ask what was inside the kernel.** Computations run outside the checker are not verified by it.
5. **It suits AI-generated proofs well**, because the check does not depend on trusting the author. The project behind Lean treats AI-generated proofs as potentially malicious for exactly that reason.
6. **Verified is not the same as new or credited.** Whether a result is correct and whether it was already known are different questions.

---

## Governance notes

**Core question:** When something is described as formally verified, what exactly was the statement, which checker verified it, what was left outside the check, and who confirmed the statement means what was intended?

**Watch for:**
- "Formally verified" claims with no statement of what theorem or property was proved
- No human review of the formal statement and its definitions, so a proof of the wrong claim is accepted
- A single checker trusted absolutely, with no independent recheck for high-stakes results
- Computations run outside the proof kernel presented as part of the verified result
- AI-generated proofs accepted because they pass the checker, without the extra checks the checker's maintainers recommend for adversarial proofs
- Correctness taken to settle novelty or credit

**Practice:**
- **Record the exact statement, the checker and its version, and the axioms the proof uses**, alongside any claim that something is formally verified
- Have a person with domain knowledge audit the statement and definitions before the result is relied on
- For high-stakes results, recheck with independent kernels where they exist ([red teaming](red-teaming.md) is how the 2026 bugs were found)
- Treat AI-generated proofs as untrusted input: check them in the stricter way recommended for adversarial proofs, and keep a record of how they were checked ([audit trail](audit-trail-ai.md))
- Check prior work separately from correctness before claiming a result is new

**Key accountability owner:** whoever signs off a result as verified, because the machine check covers the proof and that person owns the statement, the checker choice and what was left outside.

*→ [Governance & Observability Notes](../notes/governance-and-observability.md): observability signals and the cross-cutting accountability checklist.*

---

## Confidence level

**High on the method and its limits.** How proof assistants work is documented by leading practitioners in the Notices of the American Mathematical Society, and the three limits described here are each stated by experts in the field. The 2026 soundness bugs are described from the Lean project's own postmortems, which are first-party accounts. **Less settled: how far autoformalization reaches**, which is moving quickly, and what share of AI-produced mathematics is ever formally checked, which no source cited here measures. The stopping point of the bug hunt, an AI reporting it found nothing more, is not evidence that no bugs remain.

---

## Related concepts

- [Verification](verification.md) — checking an output against something outside the system; formal verification is its strongest form
- [Evaluation (AI Systems)](evaluation.md) — measuring a system across many cases, where formal verification proves a single claim
- [Red Teaming](red-teaming.md) — the adversarial search that found the 2026 kernel bugs, partly with AI
- [Hallucination](hallucination.md) — the failure a kernel check rules out for the proof, though not for the statement
- [Automation Bias](automation-bias.md) — the risk of accepting "verified" without asking what was verified
- [Audit Trail (AI)](audit-trail-ai.md) — where the statement, checker and axioms of a verified claim should be recorded

---

## Sources

| ID | Source | Contribution to this entry |
|---|---|---|
| SRC-427 | Avigad, J.; Commelin, J.; Macbeth, H.; Topaz, A. — *Anatomy of a Formal Proof* (Notices of the American Mathematical Society 72(2), 2025) · [link](https://doi.org/10.1090/noti3114) | How a proof assistant works: tactics, the quoted trusted-kernel check, Mathlib's size in early 2025, and the lineage from Automath and Mizar to Lean. |
| SRC-424 | Hales, Thomas — *What mathematicians should know about the Lean Theorem Prover: questions of reliability and AI* (guest post on Terence Tao's blog, October 9, 2026) · [link](https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/) | The quoted kernel-and-human-audit rule, the definition of a soundness bug, the 2026 bugs from an expert's view, autoformalization becoming practical, and the limits of cross-checking. ⚠️ A blog post; cited as the author's stated view. |
| SRC-426 | de Moura, Leonardo (Lean FRO) — *Postmortem for Kernel Soundness Bug #14576* (August 2026) · [link](https://leodemoura.github.io/blog/2026-8-1-postmortem-for-kernel-soundness-bug-14576/) | The quoted Collatz case, the other bugs found with OpenAI's help, that all were caught by an independent kernel, and that they were only reachable through metaprogramming. ⚠️ First-party account. |
| SRC-425 | de Moura, Leonardo (Lean FRO) — *Postmortem for the Kernel Soundness Bug Hunt* (August 24, 2026) · [link](https://leodemoura.github.io/blog/2026-8-24-postmortem-for-the-kernel-soundness-bug-hunt/) | The bug hunt with OpenAI's internal models and its quoted stopping point, the quoted treatment of AI-generated proofs as potentially malicious, and the plan to ship several independent kernels. ⚠️ First-party account. |
| SRC-429 | Mian, I.; Siddique, S. — *A Kernel-Checked Exclusion Certificate for Erdős Problem 647* (2026) · [link](https://arxiv.org/abs/2608.17880) | The quoted distinction between computations outside the kernel and a result checked end to end. ⚠️ Preprint; cited as an illustration. |
| SRC-428 | Alon, N.; Bloom, T.F.; Gowers, W.T.; Litt, D.; Sawin, W.; Shankar, A.; Tsimerman, J.; Wang, V. et al. — *Remarks on the disproof of the unit distance conjecture* (2026) · [link](https://arxiv.org/abs/2605.20695) | A human-verified version of an AI-generated counterexample, with its reliance on earlier ideas acknowledged. ⚠️ Preprint. |

---

## Audience relevance

| Audience | Relevance |
|---|---|
| **Technical / Professional** | A kernel check verifies the proof; the statement, the checker version, the axioms and anything computed outside the kernel still need recording and review. |
| **Organizational** | "Formally verified" is a strong claim with a defined scope. Someone has to own the statement and sign off what was left outside the check. |
| **Client-facing** | Explains why a verified result can be trusted without trusting whoever, or whatever, produced it, and what that guarantee does not cover. |
| **LLM-native** | Kernel-checked proof is the strongest available check on model output, and it still depends on statement fidelity and a correct checker, as the 2026 soundness bugs showed. |

---

*Last updated: v1.0 · October 2026*
