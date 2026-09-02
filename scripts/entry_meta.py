#!/usr/bin/env python3
"""
Entry metadata: derive what can be derived, parse only what must be authored.

Schema v1 — see CONTEXT.md "Entry metadata schema".

Four fields are DERIVED from the file and can never drift:
    slug     <- filename
    term     <- H1
    essence  <- line after "## One-line essence"
    version  <- footer "*Last updated: vX.Y - Month Year*"
Two more are derived for the generator's own checks:
    related  <- ](*.md) targets under "## Related concepts"
    sources  <- SRC-IDs anywhere in the file

Three fields are AUTHORED, in an HTML comment at the top of the file, because
they cannot be recovered from the prose:
    category   the README section the entry belongs to
    tags       topical facet, orthogonal to category (a term has one category, several topics)
    short      the README table form (~110 chars), distinct from `essence`
    aliases    what someone would type who does not know the title

Usage:
    entry_meta.py check    report which entries lack an authored block
    entry_meta.py dump     emit the full index as JSON on stdout
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"

META_RE = re.compile(r"\A<!--meta\s*\n(.*?)\n-->", re.S)
ESSENCE_RE = re.compile(r"^## One-line essence\s*\n(.+?)\s*$", re.M)
VERSION_RE = re.compile(r"^\*Last updated:\s*(v[\d.]+)\s*·\s*(.+?)\*\s*$", re.M)
CONF_RE = re.compile(r"^## Confidence level\s*\n+\*\*(.+?)\*\*", re.M | re.S)
# Longest-first: "medium-high" must win before "medium" or "high" can match inside it.
RATINGS = ("medium-high", "low-medium", "high", "medium", "low")

def derive_confidence(text):
    """The headline rating, DERIVED from the prose so it cannot drift from it.

    Two ratings in one statement ("High on the mechanism, low on effectiveness in
    the wild") is a *split* assessment, and saying so is the point -- flattening it
    to its first word would report an entry as confident about the half it is not.
    """
    m = CONF_RE.search(text)
    if not m:
        return None
    head = m.group(1).lower()
    if head.startswith("split"):
        return "split"
    found, seen = [], head
    for r in RATINGS:
        if re.search(rf"\b{r}\b", seen):
            found.append(r)
            seen = seen.replace(r, " ")
    if not found:
        return None
    return "split" if len(found) > 1 else found[0]


RELATED_RE = re.compile(r"^## Related concepts\s*\n(.*?)(?=\n---|\n## )", re.S | re.M)
LINK_RE = re.compile(r"\]\(([a-z0-9-]+)\.md\)")
SRC_RE = re.compile(r"SRC-\d{3}")


def parse_meta(block):
    """Three keys, one list. Deliberately not YAML — no dependency, no ambiguity."""
    out = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if k in ("aliases", "tags"):
            v = v.strip("[]")
            out[k] = [a.strip() for a in v.split(",") if a.strip()]
        else:
            out[k] = v
    return out


def read_entry(path):
    text = path.read_text()
    e = {"slug": path.stem, "path": f"concepts/{path.name}"}

    first = text.lstrip().splitlines()[0] if text.strip() else ""
    m = META_RE.match(text)
    if m:
        e.update(parse_meta(m.group(1)))
        body = text[m.end():]
        first = body.lstrip().splitlines()[0] if body.strip() else ""
    e["authored"] = bool(m)

    e["term"] = first.lstrip("# ").strip() if first.startswith("#") else None
    e["confidence"] = derive_confidence(text)
    me = ESSENCE_RE.search(text)
    e["essence"] = me.group(1).strip() if me else None
    mv = VERSION_RE.search(text)
    e["version"], e["updated"] = (mv.group(1), mv.group(2)) if mv else (None, None)
    mr = RELATED_RE.search(text)
    e["related"] = sorted(set(LINK_RE.findall(mr.group(1)))) if mr else []
    e["sources"] = sorted(set(SRC_RE.findall(text)))
    return e


def load():
    return [read_entry(p) for p in sorted(CONCEPTS.glob("*.md"))]


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    entries = load()

    if cmd == "dump":
        print(json.dumps({"count": len(entries), "entries": entries}, indent=2, ensure_ascii=False))
        return 0

    # check: derivation must be total; authoring is allowed to be incomplete during rollout
    bad = [e for e in entries if not (e["term"] and e["essence"] and e["version"])]
    todo = [e for e in entries if not e["authored"]]
    print(f"entries: {len(entries)}")
    print(f"derived cleanly (term + essence + version): {len(entries) - len(bad)}/{len(entries)}")
    for e in bad:
        miss = [k for k in ("term", "essence", "version") if not e[k]]
        print(f"  DERIVATION FAILED {e['slug']}: missing {', '.join(miss)}")
    print(f"authored meta block present: {len(entries) - len(todo)}/{len(entries)}")
    if todo:
        print(f"  awaiting authoring: {len(todo)} (retrofit backlog)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
