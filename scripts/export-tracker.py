#!/usr/bin/env python3
"""
Export the term tracker to CSV — the project's only irreplaceable artifact.

    export-tracker.py [outdir]        default: ./backups/

Why this exists: the repo has git history, a remote and a local clone. The
tracker is a single Google Sheet whose only recovery path is Google's own
version history, and it holds pertinence scores, term statuses and essences
that exist nowhere else.

⚠️ THE OUTPUT IS NOT PUBLISHABLE. The backup carries internal pertinence
scores that the public projection deliberately omits. `backups/` is gitignored
— keep it that way, and if you move the file, move it somewhere private.

Credentials are read from ~/.config/gcp/ and are NEVER embedded here or in the
output. If the token has expired this refreshes it in place.
"""
import csv, json, re, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from entry_meta import stray_scripts  # noqa: E402

SHEET_ID = "1AaMFKmkGjKyV9FOfkpGqc51K9bd0-mm8D9j3mIMXyAA"
TAB = "AI Literacy Concepts"
# The source registry. Not exported here -- swept, because a stray character in
# a registry cell is invisible to `build.py check`: those cells reach the repo
# only by being retyped into an entry, so nothing else looks at them. v1.30 put
# `问题` in a risk-flags cell and it was found by an ad-hoc script, not a check.
REGISTRY_ID = "1utge8R0fRhIdc5fOLIJDSkCC5ul3pY65alreZRNRcP4"
REGISTRY_TAB = "Sources"
TOKEN = Path.home() / ".config/gcp/sheets-token.json"


def sweep_cells(rows, label):
    """Report stray scripts / invisible characters in fetched sheet cells."""
    hits = []
    for n, row in enumerate(rows, start=1):
        for ci, cell in enumerate(row):
            for ch, cp, name in stray_scripts(str(cell)):
                col = chr(65 + ci) if ci < 26 else f"col{ci+1}"
                hits.append(f"    {label} {col}{n}: {name} {ch!r} (U+{cp:04X})")
    seen, uniq = set(), []
    for h in hits:
        if h not in seen:
            seen.add(h); uniq.append(h)
    if uniq:
        print(f"  \u26a0\ufe0f  {len(uniq)} stray-character cell(s) in {label} — fix in the sheet:")
        print("\n".join(uniq[:25]))
        if len(uniq) > 25:
            print(f"    ... and {len(uniq)-25} more")
    else:
        print(f"  charset: {label} clean ({len(rows)} rows swept)")
    return uniq


# Markers that mean "a lookup RAN and found nothing" as against "no lookup is
# recorded". Deliberately prose-matched rather than tokenised: retrofitting a
# token into 300+ existing rows would cost more than it buys, and the failure
# direction is safe -- a note this misses falls into `no-record`, which is the
# bucket a human reads, never the bucket that says everything is fine.
_CHECKED_NEGATIVE = re.compile(
    r"none archived|no (?:wayback )?snapshot|not archived|unarchived|"
    r"checked \w+ (?:url )?forms", re.I)
# Markers that mean the lookup could not be completed -- rate limit, error,
# never run to conclusion. THIS IS NOT THE SAME AS 'no snapshot' and the whole
# point of the check is to keep the two apart.
_UNRESOLVED = re.compile(
    r"lookup not completed|could[- ]not[- ]determine|could not be determined|"
    r"not verified|429|rate[- ]limit", re.I)


def write_archive_state(reg):
    """Project ONE machine-readable line per source: is it archived, and if not,
    was that a completed check or an unfinished one?

    Only three short fields are projected. The registry's assessment prose
    (contribution, credibility, risk flags, version notes) stays INTERNAL --
    this repo is public, and those columns are not published today. Widening
    that would be a decision, not a side effect of adding a check.
    """
    hdr = {name: i for i, name in enumerate(reg[0])}
    # BOTH note columns are read. Found Sep 9 2026 by pointing this reader at the
    # registry for the first time: the "checked N forms, none archived" record lives in
    # RISK FLAGS on some rows and in VERSION/COMMIT on others, and nothing documents
    # which. Reading only one column classified every such row as `no-record`.
    need = ("ID", "Archive URL", "Version / Commit", "Risk Flags")
    missing = [n for n in need if n not in hdr]
    if missing:
        print(f"  \u26a0\ufe0f  registry archive export SKIPPED - no such column(s): {missing}")
        return
    out = ROOT / "scripts" / "registry-archive.tsv"
    lines = ["# Archive coverage projected from the Sources registry. GENERATED - do not edit.",
             "# id\tarchived\tcheck_state"]
    for r in reg[1:]:
        r = r + [""] * (len(hdr) - len(r))
        sid = str(r[hdr["ID"]]).strip()
        if not sid.startswith("SRC-"):
            continue
        archived = bool(str(r[hdr["Archive URL"]]).strip())
        note = str(r[hdr["Version / Commit"]]) + " " + str(r[hdr["Risk Flags"]])
        if archived:
            state = "archived"
        elif _CHECKED_NEGATIVE.search(note):
            # An explicit statement of the OUTCOME wins over an error code mentioned
            # in passing: a note may well say why a lookup succeeded DESPITE a 429.
            state = "absent"            # a lookup ran and there is genuinely nothing
        elif _UNRESOLVED.search(note):
            state = "unresolved"        # a lookup was attempted and did not conclude
        else:
            state = "no-record"         # nothing says a lookup ever happened
        lines.append(f"{sid}\t{'yes' if archived else 'no'}\t{state}")
    out.write_text("\n".join(lines) + "\n")
    print(f"  wrote {out.relative_to(ROOT)} ({len(lines)-2} sources)")


def fetch(url, token=None, data=None):
    """curl, not urllib: urllib has no CA bundle in this environment and fails
    every https call with CERTIFICATE_VERIFY_FAILED."""
    import subprocess
    cmd = ["curl", "-sS", "--max-time", "60", url]
    if token:
        cmd += ["-H", f"Authorization: Bearer {token}"]
    if data:
        cmd += ["-X", "POST", "-d", data]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"curl failed: {r.stderr.strip()}")
    return json.loads(r.stdout)


def main():
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "backups"
    outdir.mkdir(parents=True, exist_ok=True)

    d = json.loads(TOKEN.read_text())
    tok = fetch(d["token_uri"], data=urllib.parse.urlencode({
        "client_id": d["client_id"], "client_secret": d["client_secret"],
        "refresh_token": d["refresh_token"], "grant_type": "refresh_token"}))
    if "access_token" not in tok:
        sys.exit(f"token refresh failed: {tok}")

    rng = urllib.parse.quote(f"{TAB}!A1:Z1000")
    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{rng}"
           f"?majorDimension=ROWS&valueRenderOption=UNFORMATTED_VALUE")
    data = fetch(url, token=tok["access_token"])
    rows = data.get("values", [])
    if not rows:
        sys.exit("no rows returned — refusing to write an empty backup")

    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    out = outdir / f"tracker-{stamp}.csv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows(rows)

    # Read back and verify, rather than trusting the write.
    back = list(csv.reader(out.open(encoding="utf-8")))
    assert len(back) == len(rows), f"row count mismatch: wrote {len(rows)}, read {len(back)}"
    assert back[0] == rows[0], "header mismatch on read-back"
    # Also regenerate the PUBLIC projection the register is built from.
    # Same source, two derived artifacts, so neither is hand-maintained.
    # Columns are looked up BY HEADER NAME, never by position, so the sheet's
    # layout can change without touching this script. Only the four columns
    # named below are projected; anything else in the sheet stays internal.
    hdr = {name: i for i, name in enumerate(rows[0])}
    tsv = ROOT / "scripts" / "tracker-export.tsv"
    lines = ["# Term register export from the tracker sheet. GENERATED by export-tracker.py — do not edit.",
             "# term\tpublished\tstatus\tnote\tflag"]
    # One row per term, ALWAYS. A tab splits a column and a NEWLINE splits a row, so any
    # cell containing either silently forges extra terms downstream. This bit only stripped
    # tabs until Sep 2026, when a multi-paragraph status note turned 133 terms into 141
    # phantom rows with empty statuses -- caught by build.py check, not by this script.
    # Collapsing all whitespace is also what the register needs: its notes render inside a
    # markdown table cell, which cannot contain a raw newline either.
    def flat(s):
        return " ".join(s.split())

    for r in rows[1:]:
        term = flat(r[hdr["Term"]])
        if not term:
            continue
        # `published` collapses the flag to a boolean, which is what the register needs.
        # The RAW flag is projected alongside it because the collapse hides a real
        # distinction: `TBD` (queued) and `N/A` (will not be published) both read as "no",
        # so a fold left as TBD was undetectable from the repo until this column existed.
        lines.append("\t".join([term,
                                "yes" if r[hdr["On Github Flag"]].strip() == "X" else "no",
                                flat(r[hdr["Term Status"]]) or "unassessed",
                                flat(r[hdr["Term Status Note"]]),
                                flat(r[hdr["On Github Flag"]]) or "(blank)"]))
    tsv.write_text("\n".join(lines) + "\n")
    print(f"wrote {tsv.relative_to(ROOT)} ({len(lines)-2} terms)")

    print(f"wrote {out}")
    print(f"  {len(rows)} rows x {width} cols  ({out.stat().st_size:,} bytes), read-back verified")
    print(f"  header: {', '.join(rows[0])}")

    # Sweep both sheets for stray scripts. The tracker's notes render verbatim
    # into the public register, so those also get caught by `build.py check`;
    # the registry has no such downstream reader and is only covered here.
    sweep_cells(rows, "tracker")
    rng = urllib.parse.quote(f"{REGISTRY_TAB}!A1:P400")
    reg = fetch(f"https://sheets.googleapis.com/v4/spreadsheets/{REGISTRY_ID}/values/{rng}"
                f"?majorDimension=ROWS", token=tok["access_token"]).get("values", [])
    if reg:
        sweep_cells(reg, "registry")
        write_archive_state(reg)
    else:
        print("  \u26a0\ufe0f  registry returned no rows — sweep did NOT run")


if __name__ == "__main__":
    main()
