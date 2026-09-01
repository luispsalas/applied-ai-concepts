#!/usr/bin/env python3
"""
Generate and check the wiki's derived artifacts.

    build.py check     report every inconsistency, change nothing (exit 1 if any)
    build.py write     regenerate glossary + search-index.json, sync README rows
    build.py report    reverse index for Wiki-Sources col L, and the gap report

Design notes worth keeping:

* README row ORDER inside a category is hand-curated and pedagogical (LLMs
  before SLMs before Local LLMs). The generator syncs row CONTENT in place and
  appends new entries at the end of their category. It never reorders.
* The glossary is alphabetical and fully derived, so it is regenerated whole.
* `check` is the mode that runs on every publish. `write` is only for when
  check reports a fixable difference.
"""
import json, re, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from entry_meta import load, ROOT  # noqa: E402

README = ROOT / "README.md"
GLOSSARY = ROOT / "glossary" / "index.md"
INDEX = ROOT / "search-index.json"
SEARCH = ROOT / "search.html"
TEMPLATE = ROOT / "scripts" / "search-template.html"
CONCEPTS = ROOT / "concepts"

ROW_RE = re.compile(r"^\|\s*\[([^\]]+)\]\(concepts/([a-z0-9-]+)\.md\)\s*\|\s*(.*?)\s*\|\s*✅\s*(v[\d.]+)\s*\|\s*$")
SECTION_RE = re.compile(r"^### (.+)$")
COUNT_RE = re.compile(r"(\*\*Phase 2 \(current\)[^*]*\*\*\s*)(\d+)( concepts)")


# ---------- README parsing ----------

def read_readme_rows():
    """-> {slug: (term, short, version, line_no)}, and {category: [slug,...]} in file order."""
    lines = README.read_text().splitlines()
    rows, order, cat = {}, defaultdict(list), None
    for i, line in enumerate(lines):
        m = SECTION_RE.match(line)
        if m:
            cat = m.group(1).strip()
            continue
        m = ROW_RE.match(line)
        if m and cat:
            rows[m.group(2)] = (m.group(1), m.group(3), m.group(4), i)
            order[cat].append(m.group(2))
    return lines, rows, order


# ---------- checks ----------

def check(entries):
    problems = []
    by_slug = {e["slug"]: e for e in entries}
    lines, rrows, rorder = read_readme_rows()

    # 1. schema completeness
    for e in entries:
        miss = [k for k in ("term", "essence", "version") if not e.get(k)]
        if miss:
            problems.append(f"derivation: {e['slug']} missing {', '.join(miss)}")
        if not e.get("authored"):
            problems.append(f"schema: {e['slug']} has no <!--meta block")
        for k in ("category", "short", "aliases"):
            if not e.get(k):
                problems.append(f"schema: {e['slug']} missing authored field '{k}'")

    # 2. README round-trip (term, category, short, version)
    for slug, (term, short, ver, _) in rrows.items():
        e = by_slug.get(slug)
        if not e:
            problems.append(f"readme: row for {slug} but no such entry")
            continue
        if e["term"] != term:
            problems.append(f"readme term: {slug} H1='{e['term']}' README='{term}'")
        if e.get("short") != short:
            problems.append(f"readme short: {slug} differs from meta block")
        if e["version"] != ver:
            problems.append(f"readme version: {slug} entry={e['version']} README={ver}")
    for slug in by_slug.keys() - rrows.keys():
        problems.append(f"readme: {slug} published but absent from README")
    for cat, slugs in rorder.items():
        for slug in slugs:
            e = by_slug.get(slug)
            if e and e.get("category") and e["category"] != cat:
                problems.append(f"readme category: {slug} meta='{e['category']}' README section='{cat}'")

    # 3. glossary
    want = "\n".join(glossary_rows(entries))
    have = "\n".join(l for l in GLOSSARY.read_text().splitlines() if l.startswith("| ["))
    if want != have:
        problems.append("glossary: out of sync with entries (run `build.py write`)")

    # 4. counts
    m = COUNT_RE.search(README.read_text())
    if not m:
        problems.append("readme: concept-count line not found")
    elif int(m.group(2)) != len(entries):
        problems.append(f"readme count: says {m.group(2)}, corpus has {len(entries)}")

    # 5. links + anchor-text mislinks
    problems += link_problems(entries, by_slug)

    # 6. alias rules
    problems += alias_problems(entries)
    return problems


def link_problems(entries, by_slug):
    """Broken links, plus two anchor-text checks with deliberately different strictness.

    Related-concepts bullets follow an exact-title convention, so a mismatch there
    is a hard failure. Inline prose links are legitimately paraphrased ("[tools]",
    "[human approval]"), so flagging every loose anchor is pure noise — the useful
    signal is narrower: an anchor that matches some OTHER entry and not the target.
    That is what a stale link looks like after the real target gets published, and
    it is invisible to a broken-link check because the old target still resolves.
    """
    out = []
    norm = lambda x: set(re.sub(r"[^a-z0-9]+", " ", x.lower()).split())
    titles = {e["slug"]: e["term"] for e in entries}
    words = {e["slug"]: norm(e["term"]) | set().union(*[norm(a) for a in (e.get("aliases") or [])] or [set()])
             for e in entries}
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts or p.name == "CONTEXT.md":
            continue
        for line in p.read_text().splitlines():
            bullet = line.lstrip().startswith("- [")
            for m in re.finditer(r"\[([^\]]+)\]\(([^)]+\.md)\)", line):
                anchor, target = m.group(1), m.group(2).split("#")[0]
                if not (p.parent / target).exists():
                    out.append(f"broken link: {p.relative_to(ROOT)} -> {target}")
                    continue
                slug = Path(target).stem
                if slug not in titles:
                    continue
                a, t = norm(anchor), norm(titles[slug])
                if bullet and not (a & t):
                    out.append(f"mislink (related-concepts): {p.relative_to(ROOT)} "
                               f"[{anchor}] -> {slug} ('{titles[slug]}')")
    return out


def inline_anchor_review(entries):
    """Inline anchors sharing no words with their target — a REVIEW list, not a check.

    Tried as a hard check first and it scored 1 true positive against 18 false ones,
    because inline prose legitimately paraphrases ("[tools]", "[human approval]").
    The one real find — [shadow] -> ai-governance, written before shadow-ai.md
    existed — came from reading the list, not from the rule. So the rule earns a
    place in `report`, skimmed after a publish, and not a place in the gate.
    """
    norm = lambda x: set(re.sub(r"[^a-z0-9]+", " ", x.lower()).split())
    titles = {e["slug"]: e["term"] for e in entries}
    out = []
    for p in sorted(ROOT.rglob("*.md")):
        if ".git" in p.parts or p.name == "CONTEXT.md":
            continue
        for line in p.read_text().splitlines():
            if line.lstrip().startswith("- ["):
                continue
            for m in re.finditer(r"\[([^\]]+)\]\(([^)]+\.md)\)", line):
                slug = Path(m.group(2).split("#")[0]).stem
                if slug in titles and not (norm(m.group(1)) & norm(titles[slug])):
                    out.append(f"  {p.relative_to(ROOT)}: [{m.group(1)}] -> {slug}")
    return out


def alias_problems(entries):
    out = []
    norm = lambda x: re.sub(r"[^a-z0-9]+", " ", x.lower()).strip()
    titles = {norm(e["term"]): e["slug"] for e in entries}
    seen = defaultdict(list)
    for e in entries:
        for a in e.get("aliases") or []:
            n = norm(a)
            seen[n].append(e["slug"])
            owner = titles.get(n)
            if owner and owner != e["slug"]:
                out.append(f"alias collision: {e['slug']} '{a}' is the title of {owner}")
            if n == norm(e["term"]):
                out.append(f"alias restates title: {e['slug']} '{a}'")
    for n, slugs in seen.items():
        if len(slugs) > 1:
            out.append(f"alias shared: '{n}' -> {', '.join(slugs)}")
    return out


# ---------- generation ----------

def glossary_rows(entries):
    return [f"| [{e['term']}](../concepts/{e['slug']}.md) | {e['essence'].rstrip('.')} |"
            for e in sorted(entries, key=lambda e: e["term"].lower())]


def write(entries):
    changed = []
    by_slug = {e["slug"]: e for e in entries}

    # glossary — fully regenerated (alphabetical, derived)
    head = ["# Glossary", "", "Quick-reference index of all concepts. Follow links for full entries.",
            "", "---", "", "| Term | One-line essence |", "|---|---|"]
    new_gloss = "\n".join(head + glossary_rows(entries)) + "\n"
    if GLOSSARY.read_text() != new_gloss:
        GLOSSARY.write_text(new_gloss)
        changed.append(f"glossary/index.md ({len(entries)} rows)")

    # README — sync row content in place, append new rows at end of their category
    lines, rrows, rorder = read_readme_rows()
    edits = 0
    for slug, (term, short, ver, i) in rrows.items():
        e = by_slug.get(slug)
        if not e:
            continue
        want = f"| [{e['term']}](concepts/{slug}.md) | {e['short']} | ✅ {e['version']} |"
        if lines[i] != want:
            lines[i] = want
            edits += 1
    missing = [s for s in by_slug if s not in rrows]
    for slug in missing:
        e = by_slug[slug]
        idxs = [i for s in rorder.get(e["category"], []) for (_, _, _, i) in [rrows[s]]]
        if not idxs:
            changed.append(f"!! {slug}: category '{e['category']}' has no README section — add by hand")
            continue
        row = f"| [{e['term']}](concepts/{slug}.md) | {e['short']} | ✅ {e['version']} |"
        lines.insert(max(idxs) + 1, row)
        lines, rrows, rorder = _reparse(lines)
        edits += 1
    text = "\n".join(lines) + "\n"
    text = COUNT_RE.sub(lambda m: f"{m.group(1)}{len(entries)}{m.group(3)}", text)
    if text != README.read_text():
        README.write_text(text)
        changed.append(f"README.md ({edits} row(s) synced, count -> {len(entries)})")

    # search index
    payload = {"schema": 1, "count": len(entries),
               "entries": [{k: e[k] for k in ("slug", "term", "category", "essence", "short",
                                              "aliases", "version", "updated", "related",
                                              "sources", "path")} for e in
                           sorted(entries, key=lambda e: e["term"].lower())]}
    new_idx = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    if not INDEX.exists() or INDEX.read_text() != new_idx:
        INDEX.write_text(new_idx)
        changed.append(f"search-index.json ({len(entries)} entries, "
                       f"{sum(len(e['aliases']) for e in entries)} aliases)")

    # search.html — index INLINED, not fetched. GitHub Pages is not enabled on this
    # repo, so the page has to work when opened from a clone over file://, where
    # fetch() is blocked by CORS. Inlining costs a duplicate copy of generated data,
    # which cannot drift because this function writes both.
    if TEMPLATE.exists():
        page = (TEMPLATE.read_text()
                .replace("__INDEX__", json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
                .replace("__COUNT__", str(len(entries)))
                .replace("__ALIASES__", str(sum(len(e["aliases"]) for e in entries))))
        if not SEARCH.exists() or SEARCH.read_text() != page:
            SEARCH.write_text(page)
            changed.append(f"search.html ({len(page)//1024} KB, self-contained)")
    return changed


def _reparse(lines):
    README.write_text("\n".join(lines) + "\n")
    return read_readme_rows()


# ---------- reports ----------

def report(entries):
    # reverse index for Wiki-Sources col L
    rev = defaultdict(list)
    for e in entries:
        for s in e["sources"]:
            rev[s].append(e["slug"])
    print("== Wiki-Sources reverse index (col L) ==")
    for src in sorted(rev):
        print(f"{src}\t{' · '.join(sorted(rev[src]))}")

    rev_review = inline_anchor_review(entries)
    print(f"\n== Inline anchors to eyeball ({len(rev_review)}) — paraphrase is fine, a wrong target is not ==")
    print("\n".join(rev_review) if rev_review else "  none")

    # gap report: unpublished candidate terms ranked by unlinked plain-text mentions
    tracker = ROOT / "scripts" / "tracker-terms.txt"
    print("\n== Gap report ==")
    if not tracker.exists():
        print(f"(skipped — no {tracker.relative_to(ROOT)}; one candidate term per line)")
        return
    published = {e["term"] for e in entries}
    corpus = {p: p.read_text() for p in CONCEPTS.glob("*.md")}
    corpus.update({p: p.read_text() for p in (ROOT / "notes").glob("*.md")})
    scored = []
    for term in (t.strip() for t in tracker.read_text().splitlines() if t.strip()):
        if term in published:
            continue
        n = sum(1 for text in corpus.values()
                for line in text.splitlines()
                if term in line and "](" not in line)
        scored.append((n, term))
    for n, term in sorted(scored, reverse=True):
        print(f"{n:3d}  {term}")
    flat = Counter(n for n, _ in scored)
    top = max(flat) if flat else 0
    print(f"\n{len(scored)} unpublished · top score {top} · "
          f"{flat.get(top,0)} tied at top"
          f"{'  <- tiebreak is FLAT, fall back to curation criteria' if flat.get(top,0) > 2 else ''}")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    entries = load()
    if cmd == "check":
        problems = check(entries)
        if problems:
            print(f"{len(problems)} problem(s):")
            for p in problems:
                print(f"  {p}")
            return 1
        print(f"clean — {len(entries)} entries, "
              f"{sum(len(e['aliases']) for e in entries)} aliases, "
              f"README + glossary + counts + links + aliases all consistent")
        return 0
    if cmd == "write":
        changed = write(entries)
        print("\n".join(f"wrote {c}" for c in changed) if changed else "nothing to write")
        return 0
    if cmd == "report":
        report(entries)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
