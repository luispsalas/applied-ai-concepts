#!/usr/bin/env python3
"""
Citation-form diff — the only check that can catch a WRONG REFERENT.

    citecheck.py concepts/new-entry.md [more.md ...]   compare these against the corpus
    citecheck.py --all                                 every ID, every rendered form
    citecheck.py --all --substantive                   only drift that could hide a different document

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


URL_RE = re.compile(r"\[link\]\((.*?)\)")
TITLE_RE = re.compile(r"\*(.+?)\*")


def _norm_title(t):
    """Fold the differences that are typographic rather than referential."""
    t = t.lower()
    for a, b in [("\u2011", "-"), ("\u2010", "-"), ("\u2013", "-"), ("\u2014", "-"),
                 ("\u2026", "..."), ("\u2018", "'"), ("\u2019", "'"),
                 ("\u201c", '"'), ("\u201d", '"'), ("&", "and")]:
        t = t.replace(a, b)
    t = re.sub(r"[\s]+", " ", t)
    return t.strip(" .,:;-\u2014")


def _norm_url(u):
    if not u:
        return None
    return re.sub(r"^https?://(www\.)?", "", u).rstrip("/")


def same_referent(a, b):
    """Do two rendered forms point at the same document?

    THE URL IS THE DISCRIMINATOR, and title is deliberately ignored when both
    forms carry a link. Two citations sharing a URL cite the same document
    however differently they name it -- "AI Risk Management Framework" and
    "Artificial Intelligence Risk Management Framework (AI RMF 1.0)" are one
    NIST page, and "EU AI Act, Article 13" and "EU Artificial Intelligence Act,
    Article 13: Transparency and provision of information to deployers" are one
    article. Those are naming inconsistencies; this filter exists to find
    something else.

    Calibrated by measurement rather than taste. Treating any title difference as
    substantive flagged 26 of 94 drifted IDs; allowing prefix-truncation brought
    it to 13; keying on URL gives 1 -- and the two real defects found this way
    (a preprint cited over the published paper, a superseded review draft cited
    over the final edition) were BOTH URL differences. A filter that reports a
    quarter of the corpus is one nobody reads.

    Title still decides when a form carries no link at all.
    """
    (ua, ta), (ub, tb) = a, b
    if ua or ub:
        return _norm_url(ua) == _norm_url(ub)
    if ta is None or tb is None:
        return True
    ta, tb = _norm_title(ta), _norm_title(tb)
    return ta == tb or ta.startswith(tb) or tb.startswith(ta)


def referent(form):
    """-> (url, title) for a rendered citation form. Compare with same_referent."""
    u = URL_RE.search(form)
    t = TITLE_RE.search(form)
    return (u.group(1) if u else None, t.group(1) if t else None)


def refs_disagree(forms_iter):
    """True if any two forms point at documents that are not clearly the same."""
    refs = [referent(f) for f in forms_iter]
    return any(not same_referent(refs[0], r) for r in refs[1:]) or \
           any(not same_referent(x, y) for i, x in enumerate(refs) for y in refs[i + 1:])


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    every = "--all" in sys.argv[1:]
    targets = [Path(a) for a in args]
    for t in targets:
        if not t.exists():
            sys.exit(f"no such file: {t}")

    if every:
        substantive_only = "--substantive" in sys.argv[1:]
        allf = forms(corpus_files())
        drift = {s: c for s, c in allf.items() if len(c) > 1}
        shown = {s: c for s, c in drift.items()
                 if not substantive_only or refs_disagree(c)}
        if substantive_only:
            print(f"== SUBSTANTIVE drift: {len(shown)} of {len(drift)} drifted IDs point at a "
                  f"DIFFERENT URL ({len(allf)} IDs total) ==")
            print("   The rest differ only in how the same document is named or attributed — "
                  "author lists, subtitles, abbreviations — and are left alone deliberately.\n")
            if not shown:
                print("   none — every drifted ID resolves to one document")
        else:
            print(f"== rendered-form drift: {len(drift)} of {len(allf)} IDs have more than one form ==")
        for sid, c in sorted(shown.items(), key=lambda kv: -len(kv[1])):
            mark = "  <- points at a DIFFERENT document" if refs_disagree(c) else ""
            print(f"\n{sid} — {len(c)} forms{mark}")
            for form, n in c.most_common():
                print(f"   {n:2d}x  {form[:150]}")
        sys.exit(1 if (substantive_only and shown) else 0)

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
