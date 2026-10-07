# -*- coding: utf-8 -*-
"""Build the Subscription Agreement EXECUTION PDF with the Delaware charter bound in as Exhibit A.

Ankur, 2026-10-07: "The Subscription Agreement says the Certificate of Incorporation follows as
Exhibit A, but the actual charter isn't appended."

The charter is two filed Delaware PDFs (scans, no text layer), so it cannot be rebuilt as .docx
text — it has to be bound in as pages. This script:
  1. converts out-2026-10-07-final/…Subscription_Agreement_Final.docx to PDF (LibreOffice),
  2. finds the page carrying the Exhibit A cover ("CERTIFICATE OF INCORPORATION … follows this
     page"),
  3. splices the two charter PDFs in DIRECTLY AFTER that page — not at the end of the file.

⚠️ Why the splice position matters: Exhibit A sits BEFORE Exhibit B (Risk Factors) in the
document, and its cover page says the charter "follows this page". Appending the charter to the
end of the PDF would put it after the risk factors and make the cover page's own cross-reference
false. pdfunite alone cannot do this; the document is separated into pages and reassembled.

SOURCE DOCUMENTS (both verified against the Subscription Agreement's representations):
  01-certificate.pdf — Certificate of Incorporation, filed 04/13/2026, File No. 10581972, 1 page,
     US Letter. Article FOURTH: 10,000,000 shares at $0.001 par.
  02-amendment.pdf  — Certificate of Amendment, filed 08/12/2026, 2 pages, A4. Amends Article
     FOURTH in its entirety: 6,000,000 Class A + 4,000,000 Class B, $0.001 par, no preferred;
     Class A one vote, Class B ten votes; automatic conversion of Class B on any transfer other
     than a Permitted Transfer; adds Article SIXTH (limitation of director liability) and Article
     SEVENTH (indemnification).

  These tie out exactly to Subscription Agreement "Governing Corporate Documents" (two classes of
  common, no preferred), Stockholders' Agreement §1.1 (6,000,000 / 4,000,000 / $0.001), §1.2
  (1 vote / 10 votes) and §1.4 (automatic conversion). SHA §3.2 defers Class B Permitted Transfers
  to the Certificate, and the Certificate defines them — consistent, no gap.

  ⭐ Article SEVENTH matters beyond the exhibit: the charter already requires the Corporation to
  indemnify and advance expenses to directors and officers to the fullest extent permitted by the
  DGCL, which independently supports Stockholders' Agreement §2.6 (indemnification of the Investor
  Representative) and sits alongside the D&O policy Norman agreed to bind at Seed close.

  ⚠️ Page sizes differ (Letter vs A4). Deliberately not normalised — these are filed originals and
  rescaling a filed charter is worse than a page-size change mid-exhibit.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import docx_to_pdf as d2p

HERE = Path(__file__).parent
SRC_DOCX = HERE / "out-2026-10-07-final" / "Cinderella_Corp_-_Subscription_Agreement_Final.docx"
CHARTER = Path("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c"
               "/scratchpad/charter")
OUT = HERE / "out-2026-10-07-final"
FINAL = OUT / "Cinderella_Corp_-_Subscription_Agreement_EXECUTION_with_Exhibit_A.pdf"

for p in (SRC_DOCX, CHARTER / "01-certificate.pdf", CHARTER / "02-amendment.pdf"):
    assert p.exists(), f"missing input: {p}"


def run(*cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    assert r.returncode == 0, f"{cmd[0]} failed:\n{r.stdout}\n{r.stderr}"
    return r.stdout


def pages(pdf):
    out = run("pdfinfo", str(pdf))
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


with tempfile.TemporaryDirectory() as td:
    td = Path(td)

    # ── 1. docx -> pdf ──────────────────────────────────────────────────────────
    # ⚠️ NOT LibreOffice: it is installed but cannot open any .docx in this container
    # ("Error: source file could not be loaded", even for a one-line python-docx file), so the
    # install is broken rather than our documents. docx_to_pdf renders via Chromium instead.
    body = td / "body.pdf"
    d2p.convert(SRC_DOCX, body, break_before=("EXHIBIT A", "EXHIBIT B"), workdir=td)
    n_body = pages(body)

    # ── 2. locate the Exhibit A cover page ──────────────────────────────────────
    cover = None
    for i in range(1, n_body + 1):
        txt = run("pdftotext", "-f", str(i), "-l", str(i), "-layout", str(body), "-")
        if "CERTIFICATE OF INCORPORATION" in txt and "follows this page" in txt:
            cover = i
            break
    assert cover, ("could not find the Exhibit A cover page ('CERTIFICATE OF INCORPORATION' + "
                   "'follows this page') in the converted PDF")

    # the charter must not land after Exhibit B — confirm Exhibit B is still ahead of us
    tail = run("pdftotext", "-f", str(cover), "-l", str(n_body), str(body), "-")
    assert "RISK FACTORS" in tail.upper(), \
        "Exhibit B (Risk Factors) not found after the Exhibit A cover — check document order"

    # ── 3. split, splice, reassemble ────────────────────────────────────────────
    parts = td / "parts"
    parts.mkdir()
    run("pdfseparate", "-f", "1", "-l", str(n_body), str(body), str(parts / "p-%04d.pdf"))

    order = [parts / f"p-{i:04d}.pdf" for i in range(1, cover + 1)]
    order += [CHARTER / "01-certificate.pdf", CHARTER / "02-amendment.pdf"]
    order += [parts / f"p-{i:04d}.pdf" for i in range(cover + 1, n_body + 1)]
    for p in order:
        assert p.exists(), f"missing page file {p}"

    merged = td / "merged.pdf"
    run("pdfunite", *[str(p) for p in order], str(merged))

    n_charter = pages(CHARTER / "01-certificate.pdf") + pages(CHARTER / "02-amendment.pdf")
    assert pages(merged) == n_body + n_charter, \
        f"page count {pages(merged)} != {n_body} + {n_charter}"

    shutil.copy(merged, FINAL)

# ─────────────────────────────── verification ───────────────────────────────

n = pages(FINAL)
print(f"wrote {FINAL.name}")
print(f"  {n_body} agreement pages + {n_charter} charter pages = {n}")
print(f"  Exhibit A cover on page {cover}; charter spliced in as pages {cover+1}–{cover+n_charter}")

checks = []
# the charter pages are scans with no text layer, so verify by page count and by what surrounds them
def flat(s):
    return re.sub(r"\s+", " ", s)

after = flat(run("pdftotext", "-f", str(cover + n_charter + 1), "-l", str(n), FINAL, "-")).upper()
checks.append(("Exhibit B still follows the charter", "RISK FACTORS" in after))
before = flat(run("pdftotext", "-f", "1", "-l", str(cover), FINAL, "-"))
checks.append(("Exhibit A cover precedes the charter", "follows this page" in before))
checks.append(("offering clause present", "no minimum aggregate amount that must be subscribed" in before))
checks.append(("Exhibit A cover text present",
               "Certificate of Incorporation of Cinderella Corp." in before))
checks.append(("no stale allocation block", "A minimum allocation is $100,000" not in before))
checks.append(("no stale 15-allocation language", "15 such allocations" not in before))
checks.append(("charter pages carry no text layer (scans, as expected)",
               run("pdftotext", "-f", str(cover + 1), "-l", str(cover + n_charter),
                   FINAL, "-").strip() == ""))

print("\nverification:")
bad = 0
for label, ok in checks:
    bad += not ok
    print(f"  {'OK  ' if ok else 'FAIL'} {label}")
print(f"\n{'ALL CHECKS PASSED' if not bad else f'{bad} CHECK(S) FAILED'}")
sys.exit(1 if bad else 0)
