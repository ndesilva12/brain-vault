# -*- coding: utf-8 -*-
"""Typeset contract .docx files to execution-quality PDFs via legal_pdf.

The Subscription Agreement has its own build (2026-10-07-subscription-execution-pdf.py) because
it also splices in the filed Delaware charter. Everything else goes through here.

Output: out-pdf-2026-10-07/
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
import legal_pdf as lpdf

OUT = HERE / "out-pdf-2026-10-07"
OUT.mkdir(exist_ok=True)

DOCS = [
    dict(src=HERE / "out-2026-10-07-final" / "Cinderella_Corp_-_Side_Letter_Agreement_Revenue_Share_Final.docx",
         out="Cinderella_Corp_-_Side_Letter_Agreement_Revenue_Share.pdf",
         label="Cinderella Corp. — Side Letter Agreement",
         title="Cinderella Corp. — Side Letter Agreement",
         breaks=("EXHIBIT A",),
         # the exhibit is the Expense & Travel Policy, which must survive intact
         expect=("over $500 requires Ankur Jain", "Maximum lodging rate: $300 per night",
                 "6. Documentation and Reimbursement", "Ankur Jain", "Norman de Silva"),
         forbid=("New York, San Francisco", "five thousand dollars ($5,000)")),
]


def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    assert r.returncode == 0, f"{cmd[0]} failed:\n{r.stdout}\n{r.stderr}"
    return r.stdout


def pages(pdf):
    return int(re.search(r"^Pages:\s+(\d+)", run("pdfinfo", str(pdf)), re.M).group(1))


def flat(s):
    return re.sub(r"\s+", " ", s)


bad = 0
for d in DOCS:
    assert d["src"].exists(), f"missing source: {d['src']}"
    final = OUT / d["out"]
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        body = td / "body.pdf"
        lpdf.convert(d["src"], body, break_before=d["breaks"], title=d["title"], workdir=td)
        lpdf.stamp_footers(body, final, label=d["label"], skip_pages=(), workdir=td)

    n = pages(final)
    text = flat(run("pdftotext", "-layout", str(final), "-"))
    print(f"\n{d['out']}  ({n} pages)")

    checks = []
    for needle in d["expect"]:
        checks.append((f"has {needle[:46]!r}", needle in text))
    for needle in d["forbid"]:
        checks.append((f"no  {needle[:46]!r}", needle not in text))

    # every numbered clause must actually render — the hanging-indent CSS silently dropped them
    # once (an inline-block + negative text-indent put them outside the painted area), and the
    # numbers stayed in the HTML so nothing caught it
    raw = run("pdftotext", "-layout", str(final), "-")
    nums = set(int(m.group(1)) for m in re.finditer(r"^\s*(\d{1,2})\.\s+[A-Z]", raw, re.M))
    checks.append((f"clause numbers render (found {sorted(nums)[:14]}…)",
                   {1, 2, 3, 7, 8, 11, 12, 13} <= nums))
    # signature parties each present once
    for party in ("INVESTOR:", "INVESTOR REPRESENTATIVE:", "CLASS B STOCKHOLDER:", "COMPANY:"):
        checks.append((f"signature party {party}", party in text))
    checks.append(("no collapsed signature line (rule followed by By:/Name:/Title:)",
                   not re.search(r"_{6,}\s*By:\s*Name:", raw)))
    checks.append(("signature heading is singular INVESTOR", "INVESTORS:" not in text))
    checks.append(("page numbers stamped", f"Page {n} of {n}" in text))
    blanks = [i for i in range(1, n + 1)
              if not flat(run("pdftotext", "-f", str(i), "-l", str(i), str(final), "-")).strip()]
    checks.append((f"no blank pages (checked all {n})", not blanks))

    for label, ok in checks:
        bad += not ok
        print(f"  {'OK  ' if ok else 'FAIL'} {label}")

print(f"\n{'ALL CHECKS PASSED' if not bad else f'{bad} CHECK(S) FAILED'}")
sys.exit(1 if bad else 0)
