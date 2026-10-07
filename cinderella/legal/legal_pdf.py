# -*- coding: utf-8 -*-
"""Typeset a flat .docx contract as a properly formatted legal PDF.

WHY: the Subscription Agreement .docx carries almost no formatting — no styles, no heading levels,
no indents, a bold run here and there. Rendering it one-paragraph-to-one-<p> produced a wall of
text that reads as amateur. The structure IS in the document, just implicitly: numbered clauses
("1. Formation; Authority. …"), run-in headings ("Side Letter Agreement. …"), exhibit covers, an
all-caps acknowledgment, and signature rules. This module recovers that structure and sets it the
way a law firm would.

WHAT IT PRODUCES
  • Liberation Serif (metric-compatible with Times New Roman) at 11pt, justified, 1.42 leading
  • A centred, letterspaced title under a rule
  • Numbered clauses with real HANGING INDENTS — the number sits in the margin and the text block
    aligns, instead of the number being swallowed into the paragraph
  • Bold run-in headings on both numbered clauses and named paragraphs
  • Exhibit cover pages: centred, letterspaced, with a rule and a narrowed descriptive block
  • Signature blocks rendered as a rule with a small-caps label beneath, not "______ Print Name"
    jammed onto one line
  • Widow/orphan control, and headings that cannot be stranded at the foot of a page
  • A footer rule and "Page N of M" stamped on every page of the agreement

TWO REPAIRS IT MAKES TO THE SOURCE
  1. Paragraphs split mid-sentence are rejoined. The .docx breaks clause 1 and clause 9 in the
     middle of a sentence ("…to enter into this Subscription" / "Agreement, to carry out…"),
     which would otherwise render as two paragraphs in the middle of a sentence.
  2. Runs of empty spacer paragraphs used to hand-paginate in Word are dropped before a forced
     page break; they otherwise overflow onto a blank page.

LIMITS: this is tuned to the Cinderella contract set, not a general .docx converter. It ignores
images, headers/footers, numbering fields and styles. Page numbering needs pypdf, which in this
container must be imported with `cryptography` blocked — see `_import_pypdf`.
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from docx import Document

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    "/usr/bin/chromium",
    "/usr/bin/google-chrome",
]


def _chrome():
    c = next((x for x in CHROME_CANDIDATES if Path(x).exists()), None)
    assert c, f"no chromium found; tried {CHROME_CANDIDATES}"
    return c


def _import_pypdf():
    """pypdf's import pulls in `cryptography`, whose rust binding panics in this container
    (pyo3_runtime.PanicException, not an ImportError, so pypdf's own try/except cannot catch it).
    Block the module first; pypdf then falls back to its pure-python provider, which is all we
    need since nothing here is encrypted."""
    for name in [n for n in sys.modules if n.startswith("cryptography")]:
        del sys.modules[name]

    class _Blocker:
        def find_module(self, fullname, path=None):
            return self if fullname.split(".")[0] == "cryptography" else None

        def load_module(self, fullname):
            raise ImportError("blocked: rust binding panics in this container")

    if not any(type(f).__name__ == "_Blocker" for f in sys.meta_path):
        sys.meta_path.insert(0, _Blocker())
    import pypdf
    return pypdf


# ────────────────────────────── structure recovery ──────────────────────────────

LETTERED = re.compile(r"^\((?P<l>[a-z]{1,2})\)\s+(?P<rest>.*)$", re.S)
DEFINED = re.compile(r"^[\u201c\"](?P<term>[^\u201d\"]{2,60})[\u201d\"]\s+(?P<rest>means\b.*)$", re.S)
BULLET = re.compile(r"^([\u2022\u25e6])\s+(.*)$", re.S)
RECITAL = re.compile(r"^(WHEREAS|NOW, THEREFORE)\b[,]?\s*(.*)$", re.S)
PARTY_HEAD = re.compile(r"^([A-Z][A-Z &/]{2,45}:?)\s*(\(.*\))?:?\s*$")
SIG_MANGLED = re.compile(r"^(?P<pre>[A-Z][A-Za-z .,&]*?)?\s*_{6,}\s*(?P<post>.*)$")
NUMBERED = re.compile(r"^(\d{1,2})\.\s+(.{2,90}?\.)(?:\s+(.*))?$", re.S)
RUN_IN = re.compile(r"^([A-Z][A-Za-z’'()\- ]{2,60}(?:;\s*[a-z][A-Za-z ]{2,30})?\.)\s+(.*)$", re.S)
SIG_RULE = re.compile(r"^(_{6,})\s*(.*)$")
FIELD = re.compile(r"^([A-Z][A-Za-z .,/]{2,40}:)\s*(.*)$")


def _looks_like_heading(lead):
    """A run-in heading is a short title-case phrase, e.g. "Side Letter Agreement."

    Needed because most run-in headings in this document set are NOT bold in the source — only
    the ones added by a build are. Requiring mostly-capitalised words of a handful keeps ordinary
    sentences ("The Investor hereby represents and warrants…") from being promoted to headings.
    """
    words = [w for w in lead.rstrip(".").replace(";", " ").split() if w]
    if not (1 <= len(words) <= 5) or len(lead) > 48:
        return False
    caps = sum(1 for w in words if w[:1].isupper())
    return caps >= max(2, len(words) - 1)


def classify(text, *, bold_lead):
    """Return (kind, payload). Order matters — the most specific pattern wins."""
    t = text.strip()
    if not t:
        return "blank", None
    if t in ("EXHIBIT A", "EXHIBIT B"):
        return "exhibit", t
    if t in ("CERTIFICATE OF INCORPORATION", "RISK FACTORS"):
        return "exhibit_sub", t
    if t == "SUBSCRIPTION AGREEMENT":
        return "title", t
    if t.startswith("ACCEPTANCE"):
        return "acceptance", t[len("ACCEPTANCE"):].strip()
    if t.startswith("IN WITNESS WHEREOF"):
        return "witness", t
    if t == t.upper() and len(t) > 25 and not SIG_RULE.match(t):
        return "caps", t
    m = SIG_RULE.match(t)
    if m:
        return "sigline", (m.group(2).strip(),)
    if t.startswith("[Remainder of page"):
        return "blankline", t
    m = BULLET.match(t)
    if m:
        return "bullet", (m.group(1), m.group(2))
    m = RECITAL.match(t)
    if m:
        return "recital", (m.group(1), m.group(2))
    m = DEFINED.match(t)
    if m:
        return "defined", (m.group("term"), m.group("rest"))
    m = NUMBERED.match(t)
    if m and bold_lead:
        return "clause", (m.group(1), m.group(2), m.group(3) or "")
    m = LETTERED.match(t)
    if m:
        rest = m.group("rest")
        h = RUN_IN.match(rest)
        if h and (bold_lead or _looks_like_heading(h.group(1))):
            return "lettered", (m.group("l"), h.group(1), h.group(2))
        return "lettered", (m.group("l"), None, rest)
    m = FIELD.match(t)
    if m and "_" in t:
        return "field", (m.group(1), m.group(2))
    m = RUN_IN.match(t)
    if m and (bold_lead or _looks_like_heading(m.group(1))):
        return "runin", (m.group(1), m.group(2))
    return "body", t


LABEL_LINE = re.compile(r"^(By|Name|Title|Date|Email|Address|Signature|Print Name|Subscription "
                        r"Amount|Number of Shares|Tax Identification|Mailing Address)\b\s*:?", re.I)


def _continues(prev_text, cur_text):
    """True when the .docx split one sentence across two paragraphs.

    ⚠️ Deliberately conservative. An earlier version merged any paragraph that followed one not
    ending in punctuation, which glued the whole company signature block into a single line
    ("CINDERELLA CORP By: ____ Name: Norman de Silva Title: …"). A real mid-sentence split only
    happens after a FULL line of text, so require the previous paragraph to be long, and never
    absorb a label line, an all-caps party name, a numbered clause or a signature rule.
    """
    if not prev_text or not cur_text:
        return False
    if prev_text.rstrip()[-1:] in ".:;!?”\"_":
        return False
    if LABEL_LINE.match(cur_text) or SIG_RULE.match(cur_text) or NUMBERED.match(cur_text):
        return False

    both_caps = prev_text == prev_text.upper() and cur_text == cur_text.upper()
    if both_caps:
        # An all-caps acknowledgment hard-wrapped across two paragraphs ("BY EXECUTING THE
        # SIGNATURE PAGE … THE" / "INVESTOR AGREES TO BE BOUND BY THE FOREGOING.") rejoins even
        # though the first line is under the length threshold below — it is a wrapped line, not a
        # party name, because a party name would not be followed by more capitals.
        return len(prev_text) > 30
    if prev_text == prev_text.upper() or cur_text == cur_text.upper():
        return False                              # party name, heading, or caps block boundary
    if len(prev_text) < 70:                       # short line = deliberate, not a wrap
        return False
    return cur_text[:1].isalpha()


# ───────────────────────── signature blocks ─────────────────────────

SIG_START = re.compile(r"^IN WITNESS WHEREOF\b")
FIELD_VAL = re.compile(r"^(By|Name|Title|Date|Email|Address)\s*:\s*(.*)$", re.I)


def parse_signatures(lines):
    """Turn the collapsed signature lines in the .docx into structured blocks.

    ⚠️ THIS IS THE REASON THE SIGNATURE PAGE LOOKED BROKEN. In the source, a whole signature
    block is squashed onto one paragraph:

        "__________________________________________ By: Name: Title:"
        "__________________________________________ Ankur Jain"
        "CINDERELLA CORP __________________________________________ By:"

    Rendered literally that is a rule with three labels trailing off it. Each of those lines is
    really a party name, a signature rule and a set of fields stacked vertically. This splits them
    back apart and returns blocks of:
        {"party": str|None, "entity": str|None, "note": str|None,
         "fields": [(label, value)] , "name_under": str|None}
    An entity signs through By / Name / Title; an individual signs over a printed name.
    """
    blocks, cur = [], None

    def flush():
        nonlocal cur
        if cur and (cur["entity"] or cur["fields"] or cur["name_under"] or cur["party"]):
            blocks.append(cur)
        cur = None

    for ln in lines:
        ln = ln.strip()
        if not ln:
            continue
        # a party heading: ALL CAPS, optionally with a parenthetical scope note
        m = re.match(r"^([A-Z][A-Z &/]{2,45}):?\s*(\(.*\))?:?\s*$", ln)
        if m and "_" not in ln:
            flush()
            cur = {"party": m.group(1).rstrip(":"), "entity": None, "note": m.group(2),
                   "fields": [], "name_under": None}
            continue
        m = re.match(r"^([A-Z][A-Z &/]{2,45}):?\s*\((?P<note>[^)]*)\):?\s*$", ln)
        if m:
            flush()
            cur = {"party": m.group(1).rstrip(":"), "entity": None,
                   "note": "(" + m.group("note") + ")", "fields": [], "name_under": None}
            continue
        if cur is None:
            cur = {"party": None, "entity": None, "note": None, "fields": [], "name_under": None}

        if "_____" in ln:
            pre, _, post = ln.partition("_")
            post = post.lstrip("_").strip()
            pre = pre.strip()
            if pre:
                cur["entity"] = pre
            labels = re.findall(r"(By|Name|Title|Date)\s*:", post)
            if labels:
                for lab in labels:
                    cur["fields"].append((lab, ""))
            elif post:
                cur["name_under"] = post
            if not labels and not post:
                cur["name_under"] = cur["name_under"] or ""
            continue

        m = FIELD_VAL.match(ln)
        if m:
            lab, val = m.group(1).title(), m.group(2).strip()
            for i, (l, v) in enumerate(cur["fields"]):
                if l.lower() == lab.lower() and not v:
                    cur["fields"][i] = (l, val)
                    break
            else:
                cur["fields"].append((lab, val))
            continue
        # a bare entity name line, e.g. "[ENTITY NAME]"
        if cur["entity"] is None and not cur["fields"]:
            cur["entity"] = ln
        else:
            cur["fields"].append(("", ln))
    flush()
    return blocks


def read_blocks(docx_path, *, break_before=()):
    """Paragraphs -> classified blocks, with continuations rejoined and spacer runs dropped."""
    doc = Document(docx_path)
    raw = []
    for p in doc.paragraphs:
        raw.append((p.text.strip(), any(r.bold for r in p.runs)))

    # rejoin mid-sentence splits
    joined = []
    for text, bold in raw:
        if joined and text and _continues(joined[-1][0], text):
            joined[-1] = (joined[-1][0] + " " + text, joined[-1][1])
        else:
            joined.append((text, bold))

    # Everything from "IN WITNESS WHEREOF" to the first exhibit is the signature region and is
    # parsed as a unit — its lines are collapsed in the source and only make sense together.
    sig_from = sig_to = None
    for i, (text, _b) in enumerate(joined):
        if sig_from is None and SIG_START.match(text):
            sig_from = i          # include the IN WITNESS line so it stays with the signatures
        elif sig_from is not None and text.startswith("EXHIBIT"):
            sig_to = i
            break
    if sig_from is not None and sig_to is None:
        sig_to = len(joined)

    blocks, pending = [], 0
    for idx, (text, bold) in enumerate(joined):
        if sig_from is not None and sig_from <= idx < sig_to:
            if idx == sig_from:
                blocks.append(("witness_page", joined[sig_from][0], False))
                sigs = parse_signatures([x for x, _ in joined[sig_from + 1:sig_to]])
                blocks.append(("signatures", sigs, False))
            continue
        if not text:
            pending += 1
            continue
        kind, payload = classify(text, bold_lead=bold)
        brk = any(text.startswith(pfx) for pfx in break_before)
        if not brk and pending:
            blocks.append(("gap", min(pending, 2)))
        pending = 0
        blocks.append((kind, payload) if kind != "exhibit" else ("exhibit", payload))
        if brk:
            blocks[-1] = (blocks[-1][0], blocks[-1][1], True)
    return [b if len(b) == 3 else (b[0], b[1], False) for b in blocks]


# ─────────────────────────────────── styling ───────────────────────────────────

CSS = """
@page { size: Letter; margin: 1.05in 1.1in 1.0in 1.1in; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "Liberation Serif", "Times New Roman", Times, serif;
       font-size: 11pt; line-height: 1.42; color: #000; margin: 0;
       text-align: justify; hyphens: none; }

p { margin: 0 0 9pt 0; orphans: 3; widows: 3; }

/* title */
.title { text-align: center; margin: 0 0 2pt 0; font-size: 15.5pt; font-weight: 700;
         letter-spacing: .14em; text-transform: uppercase; }
.title-rule { border: 0; border-top: 1.1pt solid #000; width: 46%; margin: 9pt auto 20pt auto; }

/* numbered clause with a hanging indent */
.clause { padding-left: 0.42in; text-indent: -0.42in; margin-bottom: 9pt; }
/* ⚠️ Do NOT make .n an inline-block: combined with the negative text-indent that creates the
   hanging indent, Chromium shifts it outside the painted area and the number disappears from the
   rendered PDF (it stays in the HTML and the text layer, so it is invisible in diffs). Plain
   inline text with two non-breaking spaces is what works. */
.clause .n { font-weight: 700; }
.clause .h { font-weight: 700; }

/* named run-in heading */
.runin .h { font-weight: 700; }

/* lead-in line before a numbered list */
.leadin { margin-bottom: 11pt; }

/* all-caps acknowledgment */
.caps { text-align: center; font-weight: 700; letter-spacing: .035em; font-size: 10.5pt;
        margin: 16pt auto 14pt auto; width: 86%; line-height: 1.5; text-align: center; }

/* signature matter */
.witness { margin: 18pt 0 16pt 0; text-align: left; }
.sig { margin: 0 0 15pt 0; page-break-inside: avoid; text-align: left; }
.sig .rule { border-bottom: 0.9pt solid #000; height: 0; width: 4.0in; margin-bottom: 3pt; }
.sig .lbl { font-size: 8.6pt; letter-spacing: .09em; text-transform: uppercase; color: #000; }
.field { margin: 0 0 10pt 0; text-align: left; }
.field .k { font-weight: 700; }
.field .note { display: block; font-size: 9.2pt; line-height: 1.38; margin-top: 4pt;
               text-align: justify; }
.acceptance { margin-top: 22pt; }
.acceptance .h { font-weight: 700; letter-spacing: .1em; text-transform: uppercase;
                 display: block; margin-bottom: 8pt; }
.party { font-weight: 700; letter-spacing: .06em; margin: 0 0 6pt 0; text-align: left; }

/* exhibits */
.pb { page-break-before: always; }
.exhibit { text-align: center; font-weight: 700; font-size: 14pt; letter-spacing: .22em;
           margin: 1.1in 0 0 0; }
.exhibit-rule { border: 0; border-top: 0.9pt solid #000; width: 28%; margin: 12pt auto 12pt auto; }
.exhibit-sub { text-align: center; font-weight: 700; font-size: 11.5pt; letter-spacing: .1em;
               margin: 0 0 20pt 0; }
.exhibit-note { width: 78%; margin: 0 auto; text-align: center; font-size: 10.5pt;
                line-height: 1.5; }
.gap1 { height: 5pt; } .gap2 { height: 11pt; }

/* lettered sub-clause, one level in from a numbered clause */
.lettered { padding-left: 0.72in; text-indent: -0.30in; margin-bottom: 8pt; }
.lettered .l { font-weight: 400; }
.lettered .h { font-weight: 700; }

/* defined term */
.defined { padding-left: 0.32in; text-indent: -0.32in; margin-bottom: 8pt; }
.defined .t { font-weight: 700; }

/* recitals */
.recital { margin-bottom: 8pt; }
.recital .w { font-variant: small-caps; letter-spacing: .04em; font-weight: 700; }

/* bullets inside an exhibit */
.b1 { padding-left: 0.42in; text-indent: -0.17in; margin-bottom: 4pt; text-align: left; }
.b2 { padding-left: 0.74in; text-indent: -0.17in; margin-bottom: 3pt; text-align: left; }

/* "[Remainder of page intentionally left blank]" */
.blankline { text-align: center; font-style: italic; font-size: 10pt; margin: 22pt 0 0 0; }

/* ── signature page ── */
.sigs { page-break-inside: auto; }
.sigblock { page-break-inside: avoid; margin: 0 0 30pt 0; text-align: left; width: 4.6in; }
.sigblock .pty { font-weight: 700; letter-spacing: .1em; font-size: 9.5pt;
                 text-transform: uppercase; margin-bottom: 2pt; }
.sigblock .note { font-size: 9pt; font-style: italic; margin-bottom: 9pt; line-height: 1.3; }
.sigblock .ent { font-weight: 700; letter-spacing: .05em; margin: 7pt 0 13pt 0; }
/* a bracketed placeholder entity becomes a blank for the signer, sized to match the field rules
   below it (0.52in label column + 3.9in rule) so the block reads as one stack */
.sigblock .entrule { border-bottom: 0.9pt solid #000; height: 0; width: 4.42in;
                     margin: 10pt 0 15pt 0; }
.sigblock .srule { border-bottom: 0.9pt solid #000; height: 0; width: 100%;
                   margin-top: 24pt; margin-bottom: 3pt; }
.sigblock .nm { font-size: 10pt; margin-bottom: 0; }
.sigblock .row { display: block; margin-bottom: 11pt; }
.sigblock .row .k { display: inline-block; width: 0.52in; font-size: 10pt; }
.sigblock .row .v { display: inline-block; width: 3.9in; border-bottom: 0.9pt solid #000;
                    font-size: 10.5pt; }
.sigblock .row .vf { display: inline-block; width: 3.9in; font-size: 10.5pt; }
"""


def to_html(docx_path, *, break_before=(), title="Agreement"):
    blocks = read_blocks(docx_path, break_before=break_before)
    out = []
    e = html.escape
    pending_exhibit_note = False

    for kind, payload, brk in blocks:
        pb = " pb" if brk else ""
        if kind == "blank":
            continue
        if kind == "gap":
            out.append(f'<div class="gap{payload}"></div>')
        elif kind == "title":
            out.append(f'<p class="title{pb}">{e(payload)}</p><hr class="title-rule">')
        elif kind == "exhibit":
            out.append(f'<p class="exhibit{pb}">{e(payload)}</p><hr class="exhibit-rule">')
            pending_exhibit_note = True
        elif kind == "exhibit_sub":
            out.append(f'<p class="exhibit-sub">{e(payload)}</p>')
        elif kind == "clause":
            n, head, rest = payload
            out.append(f'<p class="clause{pb}"><span class="n">{e(n)}.</span>&nbsp;&nbsp;'
                       f'<span class="h">{e(head)}</span> {e(rest)}</p>')
        elif kind == "runin":
            head, rest = payload
            out.append(f'<p class="runin{pb}"><span class="h">{e(head)}</span> {e(rest)}</p>')
        elif kind == "lettered":
            lab, head, rest = payload
            h = f'<span class="h">{e(head)}</span> ' if head else ""
            out.append(f'<p class="lettered{pb}"><span class="l">({e(lab)})</span>&nbsp;&nbsp;'
                       f'{h}{e(rest)}</p>')
        elif kind == "defined":
            term, rest = payload
            out.append(f'<p class="defined{pb}"><span class="t">\u201c{e(term)}\u201d</span> '
                       f'{e(rest)}</p>')
        elif kind == "recital":
            word, rest = payload
            sep = ", " if word.startswith("NOW") else ", "
            out.append(f'<p class="recital{pb}"><span class="w">{e(word)}</span>{sep}{e(rest)}</p>')
        elif kind == "bullet":
            mark, text = payload
            cls = "b1" if mark == "\u2022" else "b2"
            glyph = "\u2022" if mark == "\u2022" else "\u25e6"
            out.append(f'<p class="{cls}{pb}">{glyph}&nbsp;&nbsp;{e(text)}</p>')
        elif kind == "blankline":
            out.append(f'<p class="blankline{pb}">{e(payload)}</p>')
        elif kind == "witness_page":
            out.append(f'<p class="witness pb">{e(payload)}</p>')
        elif kind == "signatures":
            out.append('<div class="sigs">')
            for s in payload:
                out.append('<div class="sigblock">')
                if s["party"]:
                    out.append(f'<div class="pty">{e(s["party"].strip())}:</div>')
                if s["note"]:
                    out.append(f'<div class="note">{e(s["note"])}</div>')
                if s["entity"]:
                    # A bracketed placeholder ("[ENTITY NAME]") is something the signer fills in,
                    # so set it as a blank rule like the fields below it rather than printing the
                    # placeholder text. A real party name ("CINDERELLA CORP") still prints.
                    if re.fullmatch(r"\[.*\]", s["entity"].strip()):
                        out.append('<div class="entrule"></div>')
                    else:
                        out.append(f'<div class="ent">{e(s["entity"])}</div>')
                if s["fields"]:
                    for lab, val in s["fields"]:
                        if not lab:
                            out.append(f'<div class="nm">{e(val)}</div>')
                            continue
                        cls = "vf" if val else "v"
                        out.append(f'<div class="row"><span class="k">{e(lab)}:</span>'
                                   f'<span class="{cls}">{"&nbsp;" + e(val) if val else "&nbsp;"}'
                                   f'</span></div>')
                else:
                    out.append('<div class="srule"></div>')
                    out.append(f'<div class="nm">{e(s["name_under"] or "")}</div>')
                out.append('</div>')
            out.append('</div>')
        elif kind == "caps":
            out.append(f'<p class="caps{pb}">{e(payload)}</p>')
        elif kind == "witness":
            out.append(f'<p class="witness{pb}">{e(payload)}</p>')
        elif kind == "sigline":
            lbl = payload[0]
            out.append(f'<div class="sig{pb}"><div class="rule"></div>'
                       f'<div class="lbl">{e(lbl)}</div></div>')
        elif kind == "field":
            k, v = payload
            # a long trailing explanation is set smaller, under the field
            m = re.match(r"^(\$?_{4,}|\S*_{4,}\S*)\s*(.*)$", v)
            if m and m.group(2):
                out.append(f'<p class="field{pb}"><span class="k">{e(k)}</span> {e(m.group(1))}'
                           f'<span class="note">{e(m.group(2))}</span></p>')
            else:
                out.append(f'<p class="field{pb}"><span class="k">{e(k)}</span> {e(v)}</p>')
        elif kind == "acceptance":
            out.append(f'<p class="acceptance{pb}"><span class="h">Acceptance</span>'
                       f'{e(payload)}</p>')
        else:
            cls = "exhibit-note" if pending_exhibit_note else "body"
            if pending_exhibit_note:
                pending_exhibit_note = False
            if payload.endswith("as follows:"):
                cls = "leadin"
            if re.match(r"^(CINDERELLA CORP|COMPANY:|CONSULTANT:|INVESTOR:)", payload):
                cls = "party"
            out.append(f'<p class="{cls}{pb}">{e(payload)}</p>')

    return (f"<!doctype html><html><head><meta charset='utf-8'><title>{e(title)}</title>"
            f"<style>{CSS}</style></head><body>" + "".join(out) + "</body></html>")


# ─────────────────────────────── render + paginate ───────────────────────────────

def _render(html_text, pdf_path, workdir):
    f = Path(workdir) / (Path(pdf_path).stem + ".html")
    f.write_text(html_text, encoding="utf-8")
    r = subprocess.run([_chrome(), "--headless", "--no-sandbox", "--disable-gpu",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
                        f"file://{f.resolve()}"],
                       capture_output=True, text=True, timeout=300)
    assert Path(pdf_path).exists(), f"chromium produced no PDF:\n{r.stdout}\n{r.stderr}"
    return Path(pdf_path)


FOOTER_CSS = """
@page { size: Letter; margin: 0; }
body { margin: 0; font-family: "Liberation Serif", Times, serif; }
.pg { position: relative; width: 8.5in; height: 11in; page-break-after: always; }
.ft { position: absolute; left: 1.1in; right: 1.1in; bottom: 0.62in; text-align: center;
      font-size: 8.8pt; letter-spacing: .06em; color: #000;
      border-top: 0.6pt solid #000; padding-top: 5pt; }
.ft .l { float: left; letter-spacing: .09em; text-transform: uppercase; font-size: 8pt; }
.ft .r { float: right; }
"""


def stamp_footers(pdf_path, out_path, *, label, skip_pages=(), workdir=None):
    """Overlay a footer rule, a document label and 'Page N of M' on every page except skip_pages.

    skip_pages is 1-based. Filed exhibit scans are skipped so nothing is printed over a document
    that was filed with the state."""
    pypdf = _import_pypdf()
    reader = pypdf.PdfReader(str(pdf_path))
    total = len(reader.pages)
    workdir = Path(workdir or Path(out_path).parent)

    pages_html = []
    for i in range(1, total + 1):
        inner = "" if i in skip_pages else (
            f'<div class="ft"><span class="l">{html.escape(label)}</span>'
            f'<span class="r">Page {i} of {total}</span>'
            f'&nbsp;</div>')
        pages_html.append(f'<div class="pg">{inner}</div>')
    overlay_pdf = workdir / "footers.pdf"
    _render(f"<!doctype html><html><head><meta charset='utf-8'><style>{FOOTER_CSS}</style>"
            f"</head><body>{''.join(pages_html)}</body></html>", overlay_pdf, workdir)

    ov = pypdf.PdfReader(str(overlay_pdf))
    assert len(ov.pages) >= total, f"footer overlay has {len(ov.pages)} pages, need {total}"
    writer = pypdf.PdfWriter()
    for i, page in enumerate(reader.pages):
        if (i + 1) not in skip_pages:
            page.merge_page(ov.pages[i])
        writer.add_page(page)
    with open(out_path, "wb") as fh:
        writer.write(fh)
    return Path(out_path)


def convert(docx_path, pdf_path, *, break_before=(), title=None, workdir=None):
    workdir = Path(workdir or Path(pdf_path).parent)
    workdir.mkdir(parents=True, exist_ok=True)
    doc_title = title or Path(docx_path).stem
    return _render(to_html(docx_path, break_before=break_before, title=doc_title),
                   pdf_path, workdir)


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as td:
        convert(sys.argv[1], sys.argv[2], break_before=("EXHIBIT A", "EXHIBIT B"), workdir=td)
    print("wrote", sys.argv[2])
