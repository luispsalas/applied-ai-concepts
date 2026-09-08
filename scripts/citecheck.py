#!/usr/bin/env python3
"""
Citation-form diff — the only check that can catch a WRONG REFERENT.

    citecheck.py concepts/new-entry.md [more.md ...]   compare these against the corpus
    citecheck.py --all                                 every ID, every rendered form

Why this exists. Metadata comes from the source or the registry, never from
recall -- and that rule has been broken in every drafting batch so far. The
failures are not typos: SRC-153 (an InfoQ article) was cited for a generalization
paper, SRC-140 (an ISO technical report) for InstructGPT, SRC-063 (a vendor blog)
for an evaluation paper. Each was well-formed and pointed at a REAL but DIFFERENT
source, which is a misattribution to a named author -- the worst thing this corpus
can ship.

No structural check can catch that. A wrong-but-well-formed URL resolves, so the
link checker passes it; a real-but-wrong ID exists in the registry, so the ID gate
passes it; the schema is intact, so `build.py check` passes it. Comparing the
rendered form against how the SAME ID is written elsewhere is the only signal.

RANKING BY FREQUENCY IS THE POINT, and it is why this is a script rather than a
grep. Older IDs have several rendered forms in the corpus (SRC-039 has four,
SRC-141 three). Comparing against whichever sorts first alphabetically produced
two false positives in one batch -- and a false positive is how a check earns
being skimmed. The dominant form is the corpus's actual convention; that is what
a new citation should match.
"""
import re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROW_RE = re.compile(r"^\|\s*(SRC-\d+)\s*\|(.+?)\|", re.M)


def corpus_files():
    return sorted(list((ROOT / "concepts").glob("*.md")) + list((ROOT / "notes").glob("*.md")))


def forms(files):
    """-> {src_id: Counter(rendered form)} over the given files."""
    out = {}
    for f in files:
        for sid, form in ROW_RE.findall(f.read_text(encoding="utf-8")):
            out.setdefault(sid, Counter())[" ".join(form.split())] += 1
    return out


def main():
    args = [a for a in sys.argv[1:] if a != "--all"]
    every = "--all" in sys.argv[1:]
    targets = [Path(a) for a in args]
    for t in targets:
        if not t.exists():
            sys.exit(f"no such file: {t}")

    if every:
        allf = forms(corpus_files())
        drift = {s: c for s, c in allf.items() if len(c) > 1}
        print(f"== rendered-form drift: {len(drift)} of {len(allf)} IDs have more than one form ==")
        for sid, c in sorted(drift.items(), key=lambda kv: -len(kv[1])):
            print(f"\n{sid} — {len(c)} forms")
            for form, n in c.most_common():
                print(f"   {n:2d}x  {form[:150]}")
        return

    if not targets:
        sys.exit(__doc__.strip().splitlines()[2])

    baseline = forms([f for f in corpus_files() if f.resolve() not in {t.resolve() for t in targets}])
    new = forms(targets)

    problems = new_ids = matches = 0
    for sid in sorted(new):
        for form in new[sid]:
            if sid not in baseline:
                print(f"NEW      {sid}  (not cited elsewhere — verify against the registry)")
                new_ids += 1
                continue
            # The DOMINANT form is the corpus convention. Ties break toward the
            # longer form, which carries more verifiable detail.
            top, n = max(baseline[sid].items(), key=lambda kv: (kv[1], len(kv[0])))
            if form == top:
                matches += 1
                continue
            if form in baseline[sid]:
                print(f"variant  {sid}  matches a less common form "
                      f"({baseline[sid][form]}x vs {n}x dominant) — consider aligning")
                print(f"           yours: {form[:130]}")
                print(f"           domin: {top[:130]}")
                matches += 1
                continue
            problems += 1
            print(f"DIFFERS  {sid}")
            print(f"           yours: {form[:150]}")
            print(f"           domin: {top[:150]}  ({n}x)")
    print(f"\n{matches} match · {new_ids} new · {problems} differ"
          + ("" if not problems else "  <- verify each against the registry before publishing"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
