# Execution copies — hand-finalised, not generated

⚠️ **No build script writes to this folder.** Files here are versions Norman finalised by hand;
they **supersede** the generated equivalents in `out-2026-10-07-final/`, and a rebuild of the
generator chain will not touch them.

| File | Supersedes | Why |
|---|---|---|
| `Cinderella_Corp_-_Subscription_Agreement_Final.docx` | `out-2026-10-07-final/Cinderella_Corp_-_Subscription_Agreement_Final.docx` | Norman's formatting and spacing pass, 2026-10-07 |

**Diff against the generated version — three changes, none substantive:**
1. The generated version-note line at the top removed.
2. Investor signature date `20[__]` → `2026`.
3. The ACCEPTANCE block split into separate paragraphs (`CINDERELLA CORP`, `By: ___`) instead of
   one run-on paragraph.

Every operative provision is identical, verified paragraph-by-paragraph: the Offering clause, the
removal of the $100,000 / 15-allocation language, the Exhibit A cover and the Investor
Representative acknowledgment all carry over unchanged.

**The execution PDF is built from THIS file**, by `../2026-10-07-subscription-execution-pdf.py`.

## Page breaks

`Cinderella_Corp_-_Subscription_Agreement_Final_page-breaks.docx` — **optional.** Identical text to
Norman's copy, with the **35 consecutive empty spacer paragraphs** that pushed EXHIBIT A and
EXHIBIT B onto new pages replaced by **two real Word page breaks**.

⚠️ Why it matters: hand-pagination with empty paragraphs holds only until something above it
reflows. It also caused a **blank page** in the first execution PDF — the spacers overflowed past
the end of the Exhibit A page once a real break was applied. The renderer now drops a run of blank
paragraphs sitting immediately before a forced break, and the build asserts there are no blank
pages anywhere in the output.

Take it or leave it — Norman's original is untouched and the PDF is correct either way.

⚠️ **Do not send `out-2026-10-07-final/Cinderella_Corp_-_Subscription_Agreement_Final.docx`.** That
is the generated copy and is now superseded by this folder.

## Typesetting

The execution PDF is typeset by `../legal_pdf.py`, not rendered one-paragraph-to-one-line. The
.docx carries almost no formatting — no styles, no heading levels, a bold run here and there — so
the structure is recovered from the text itself and set properly:

- **Liberation Serif** (metric-compatible with Times New Roman) at 11pt, justified, 1.42 leading
- Centred letterspaced title under a rule
- **Hanging indents** on the numbered clauses, so the number sits in the margin and the text block
  aligns — 1. through 20. and the 22 risk factors
- **Bold run-in headings**, detected by shape (a short title-case phrase ending in a period), since
  most are not bold in the source
- Signature blocks as a **rule with a small-caps label beneath**, instead of `______ Print Name`
  jammed onto one line
- Exhibit covers centred and letterspaced with a rule, and a narrowed descriptive block
- Widow/orphan control, and a footer rule with **"Page N of M"** on every page

⚠️ **The three filed charter scans are deliberately left unstamped** — nothing is printed over a
document filed with the State of Delaware. Numbering stays continuous with the physical document,
so Exhibit B reads "Page 12 of 13".

Two repairs `legal_pdf.py` makes to the source, both asserted by the build:
1. **Paragraphs split mid-sentence are rejoined** (clauses 1 and 9 break in the middle of a
   sentence in the .docx), as is the all-caps acknowledgment that is hard-wrapped across two.
2. **Runs of empty spacer paragraphs are dropped before a forced page break**, which is what
   produced a blank page in the first execution PDF.

`legal_pdf.py` is reusable for the rest of the contract set — it needs the document's own exhibit
names passed as `break_before`.
