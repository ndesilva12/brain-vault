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
