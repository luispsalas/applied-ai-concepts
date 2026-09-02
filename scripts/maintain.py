#!/usr/bin/env python3
"""
Periodic maintenance checks — the ones GENERATION DOES NOT MAKE UNNECESSARY.

    maintain.py offline    no network, no sheets. Safe to run any time.
    maintain.py links      + source URL liveness (network, slow, rate-limited)

Deliberately NOT here:
  * Anything `build.py check` already gates. That runs on every publish and
    covers schema, README/glossary sync, counts, link resolution, aliases,
    term status, confidence derivation, and tracker-export agreement.
    Duplicating it here would mean two places to update.
  * Anything the generator made impossible. Essence/version/count drift used to
    need checks; those fields are now derived, so the check would be dead code.

Everything below is REPORT-ONLY. None of it exits non-zero, because every one
of these needs a human call — see the precision note on the spelling check.
"""
import re, sys, json, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONCEPTS = ROOT / "concepts"
NOTES = ROOT / "notes"

# Publishers that return 4xx/5xx to automated clients while loading fine in a
# browser. Confirmed, not guessed. Without this list every audit re-raises them.
BOT_HOSTILE = ("oecd.org", "iso.org", "dl.acm.org", "doi.org", "sciencedirect.com",
               "link.springer.com", "estsjournal.org", "pubsonline.informs.org",
               "academic.oup.com", "nber.org", "jamanetwork.com",
               "mckinsey.com")   # HTTP/2 INTERNAL_ERROR to HEAD and GET; loads in a browser

# British variants. `programme`/`dialogue` need a boundary or they match
# "programmed" and "dialogue box"; that bug produced 3 of 14 hits on first run.
BRITISH = re.compile(r"\b\w*(behaviour|colour|flavour|favour|honour|labour|neighbour|"
                     r"rumour|humour|odour|vapour|centre|centred|fibre|litre|metre|theatre|"
                     r"calibre|sombre|spectre|catalogue|analogue|defence|offence|licence|"
                     r"pretence|practise|organise|organisa|recognise|recognisa|prioritise|"
                     r"summarise|utilise|optimise|minimise|maximise|specialise|normalise|"
                     r"standardise|categorise|characterise|emphasise|analyse|analysing|"
                     r"paralyse|modelling|modelled|labelling|labelled|travelling|cancelled|"
                     r"instalment|skilful|wilful|judgement|ageing|sceptic|cheque|storey|"
                     r"tyre|aluminium|manoeuvre|encyclopaedia)\w*\b", re.I)
BRITISH_WORD = re.compile(r"\bprogramme\b|\bgrey\b|\bfulfil\b|\benrol\b", re.I)


def _files():
    return sorted(list(CONCEPTS.glob("*.md")) + list(NOTES.glob("*.md")))


def spelling(report):
    """US-English sweep, EXCLUDING quotations and Sources tables.

    Precision matters more than recall here. The corpus quotes the EU AI Act,
    ISO and the OECD constantly, and all three write British English -- so a
    naive sweep returned 14 hits of which 1 was real. Faithfulness to a quoted
    source outranks house style, so quoted spans and Sources rows are skipped
    and the rest is REPORTED, never auto-corrected.
    """
    for f in _files():
        for n, line in enumerate(f.read_text().splitlines(), 1):
            if line.startswith("| SRC-"):          # Sources table row
                continue
            stripped = re.sub(r"\*?\"[^\"]*\"\*?", " ", line)   # quoted spans
            stripped = re.sub(r"\*[^*]+\*", " ", stripped)      # italicised titles/terms
            for rx in (BRITISH, BRITISH_WORD):
                for m in rx.finditer(stripped):
                    report.append(f"spelling  {f.name}:{n}  {m.group(0)}")


def source_links(report):
    """Every SRC-ID cited in an entry must carry a [link] in its Sources row."""
    for f in _files():
        m = re.search(r"^## Sources\s*\n(.*?)(?=^## |\Z)", f.read_text(), re.M | re.S)
        if not m:
            report.append(f"sources   {f.name}: no Sources section")
            continue
        for line in m.group(1).splitlines():
            hit = re.match(r"\| (SRC-\d+)", line)
            if hit and "[link](" not in line:
                report.append(f"sources   {f.name}: {hit.group(1)} has no [link]")


def orphan_sources(report):
    """SRC-IDs referenced in prose but absent from that entry's Sources table."""
    for f in _files():
        t = f.read_text()
        m = re.search(r"^## Sources\s*\n(.*?)(?=^## |\Z)", t, re.M | re.S)
        table = set(re.findall(r"SRC-\d+", m.group(1))) if m else set()
        body = t[:m.start()] if m else t
        for sid in sorted(set(re.findall(r"SRC-\d+", body))):
            if sid not in table:
                report.append(f"sources   {f.name}: {sid} cited in prose but not in the Sources table")


def collect_urls():
    urls = {}
    for f in _files():
        for sid, url in re.findall(r"\| (SRC-\d+) \|.*?\[link\]\((https?://[^)]+)\)", f.read_text()):
            urls.setdefault(url, set()).add(sid)
    return urls


def liveness(report):
    """HTTP-check every cited source URL. Slow; run rarely.

    Uses curl, NOT urllib: Python's urllib has no CA bundle in this environment
    and fails every https URL with CERTIFICATE_VERIFY_FAILED. The first version
    of this check did exactly that and reported 146 live sources as dead --
    the checker's own environment masquerading as a corpus defect. If this ever
    reports everything as broken, suspect the checker before the corpus.
    """
    import subprocess
    urls = collect_urls()
    skipped = 0
    print(f"  checking {len(urls)} distinct source URLs via curl...", file=sys.stderr)
    for url, sids in sorted(urls.items()):
        if any(h in url for h in BOT_HOSTILE):
            skipped += 1
            continue
        r = subprocess.run(
            ["curl", "-sSL", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "25",
             "-A", "Mozilla/5.0 (link-check)", "-I", url],
            capture_output=True, text=True)
        code = (r.stdout or "").strip()
        if code in ("403", "405", "429"):          # blocked or HEAD refused, not dead
            continue
        if code == "000":
            report.append(f"liveness  NO-RESPONSE {url}  ({', '.join(sorted(sids))})")
        elif not code.startswith(("2", "3")):
            report.append(f"liveness  {code} {url}  ({', '.join(sorted(sids))})")
    print(f"  ({skipped} skipped as known bot-hostile publishers)", file=sys.stderr)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "offline"
    report = []
    spelling(report)
    source_links(report)
    orphan_sources(report)
    if mode == "links":
        liveness(report)

    groups = {}
    for line in report:
        groups.setdefault(line.split()[0], []).append(line)
    for kind in sorted(groups):
        print(f"\n== {kind} ({len(groups[kind])}) ==")
        for line in groups[kind]:
            print("  " + line)
    if not report:
        print("clean — nothing to review")
    else:
        print(f"\n{len(report)} item(s) to REVIEW. None of these are automatic failures; "
              f"quoted material and source-faithful spellings are expected hits.")


if __name__ == "__main__":
    main()
