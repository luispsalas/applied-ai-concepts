#!/usr/bin/env python3
"""
Export the term tracker to CSV — the project's only irreplaceable artifact.

    export-tracker.py [outdir]        default: ./backups/

Why this exists: the repo has git history, a remote and a local clone. The
tracker is a single Google Sheet whose only recovery path is Google's own
version history, and it holds pertinence scores, term statuses, AISCE
cross-references and essences that exist nowhere else.

⚠️ THE OUTPUT IS NOT PUBLISHABLE. Column B ("AISCE References") contains real
AISCE content, which this repo's Critical Boundary forbids. `backups/` is
gitignored — keep it that way, and if you move the file, move it somewhere
private.

Credentials are read from ~/.config/gcp/ and are NEVER embedded here or in the
output. If the token has expired this refreshes it in place.
"""
import csv, json, sys, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

SHEET_ID = "1AaMFKmkGjKyV9FOfkpGqc51K9bd0-mm8D9j3mIMXyAA"
TAB = "AI Literacy Concepts"
TOKEN = Path.home() / ".config/gcp/sheets-token.json"


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
    print(f"wrote {out}")
    print(f"  {len(rows)} rows x {width} cols  ({out.stat().st_size:,} bytes), read-back verified")
    print(f"  header: {', '.join(rows[0])}")


if __name__ == "__main__":
    main()
