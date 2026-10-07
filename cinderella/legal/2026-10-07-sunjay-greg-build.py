# -*- coding: utf-8 -*-
"""Conform Sunjay's and Greg's RSPAs and Stockholders' Agreements to the 2026-10-07 set.

SOURCE OF TRUTH: the four .docx files Norman sent 2026-10-07 (copied to
scratchpad/sent-2026-10-07/). This is a PATCH build on those files, not a re-draft — every
change is a targeted replacement and each one is asserted to have fired, so a drifted source
string fails the build loudly instead of silently skipping a change.

WHY EACH CHANGE (full reasoning in 2026-10-07-sunjay-greg-review.md):

  A. SECURITIES EXEMPTION — resolved to Rule 701 primary / Section 4(a)(2) fallback, NOT
     Regulation D. Norman chose Reg D for ANKUR on 2026-10-07 for a reason that is specific to
     Ankur: Rule 701(c) excludes services rendered in connection with the offer or sale of
     securities in a capital-raising transaction, and Ankur's Adviser Agreement §1.1 defines his
     services as capital formation and investor meetings. Sunjay runs operations; Greg's Adviser
     Agreement §1.1 is "strategic guidance and network access" and §1.2 expressly makes him not
     an agent who may negotiate or sign. Neither is capital-raising, so Rule 701 is available to
     both — and it is the better exemption here because it needs no accredited-investor
     representation (Greg's status is unconfirmed) and no Form D for a par-value comp grant.
     Rule 701 requires the grant be made under a written compensation contract, so the clause
     now names that contract on its face. Rule 701 offerings do not integrate with Reg D.

  B. PRICE — the delivered drafts said the price was "to be set" and "confirm with counsel,"
     and Schedule A carried a bracketed "[FMV as determined by the Board]" note. A counterparty
     draft must not say your own price is unsettled. $0.001 is stated as the Board's good-faith
     FMV determination. ⚠️ REQUIRES the board resolution fixing $0.001 as FMV, dated on or
     before the Effective Date — still outstanding.

  C. 83(b) — INVERTS relative to Ankur. Ankur's shares are fully vested, so 83(b) is moot for
     him. Sunjay's and Greg's shares are substantially nonvested, so 83(b) is the whole
     ballgame, and the delivered language ("advised to consider filing") understates it. Now
     states the 30-day statutory deadline is non-extendable and what happens if it is missed.

  D. ANKUR DISCLOSURE REMOVED — both Schedule As read "Unlike the Company's arrangement with
     Ankur Jain, these Shares carry NO anti-dilution protection and NO top-up," and Greg's
     Acceleration line read "Compare Sunjay Mathews, who has both six-month severance
     acceleration and full single-trigger acceleration." These disclose another holder's
     preferential terms to a counterparty and hand them the argument for matching them. The
     substance is kept; the comparison is deleted.

  E. SEED SIZE DE-HARDCODED AS A REPRESENTATION, NOT DELETED — the post-Seed percentages
     (16.875% / 3.375%) are kept exactly as Norman sent them but marked illustrative and tied to
     a 15% round, so they do not become a representation if the round is resized.

  F. GREG'S BRACKETS SETTLED — [24] months confirmed as 24; vesting commencement confirmed as
     the Effective Date; acceleration stated as none. These were flagged "must be settled before
     execution" in the draft he was sent.

  G. STOCKHOLDERS' AGREEMENT CONFORMED — this is ONE agreement that every holder signs or joins,
     and the Ankur copy built 2026-10-07 now carries a firm D&O trigger in §2.6 and a new §2.7
     (no personal liability of the Investor Representative). Sunjay's and Greg's copies did not,
     which would put three different texts of the same agreement into execution. §2.7 says each
     Investor "by executing this Agreement or a joinder to it, acknowledges and agrees to this
     Section 2.7" — unenforceable against a holder who signed a copy that does not contain it.
     Sunjay is the Class A majority (833,333 of 1,166,667 pre-Seed), and §9.2 makes a Class A
     majority necessary to amend, so he in particular must be on the current text. Neither
     change touches any right of Sunjay's or Greg's — both run only to the Investor
     Representative. Text is character-identical to Ankur's copy by design.

NOT CHANGED, DELIBERATELY:
  • §2.4 Milestone grants ("the Company's written determination") — Ankur's copy was made
    objective and automatic. NOT propagated. Sunjay's Track B is board-attributed BY DESIGN per
    the Partner Agreement, and in any case his Schedule A grants no Milestone Shares here
    ("Milestone Shares are NOT granted by this Agreement"); Greg has no milestones at all. §2.4
    is inoperative in both documents. It matters when the Track A/B milestone RSPA is papered.
  • The "DRAFT — FOR DISCUSSION ONLY" banner on Greg's RSPA is left in place, and Sunjay's RSPA
    is NOT given one. Removing a not-legal-advice disclaimer from a document drafted without
    counsel is the wrong direction; the inconsistency is Norman's call.
  • Signature-block cosmetics (Sunjay's RSPA has no "By:" line; Greg's RSPA PURCHASER block is
    unfilled) — flagged, not patched; not worth the build risk.
"""
import copy
import sys
from pathlib import Path
from docx import Document

SENT = Path("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c"
            "/scratchpad/sent-2026-10-07")
OUT = Path(__file__).parent / "out-sunjay-greg-2026-10-07"
OUT.mkdir(exist_ok=True)

FIRED = []


# ───────────────────────────── run-aware patch helpers ─────────────────────────────

def _set_span(para, i, j, new):
    """Put `new` in run i, blank runs i+1..j-1, preserving run i's formatting."""
    para.runs[i].text = new
    for k in range(i + 1, j):
        para.runs[k].text = ""


def sub(doc, old, new, *, label, where=None):
    """Replace the first occurrence of `old` across runs. Asserts exactly one paragraph hit."""
    hits = 0
    for para in doc.paragraphs:
        if old not in para.text:
            continue
        if where and where not in para.text:
            continue
        runs = para.runs
        # find the minimal consecutive run span whose concatenation contains `old`
        found = False
        for i in range(len(runs)):
            acc = ""
            for j in range(i, len(runs)):
                acc += runs[j].text
                if old in acc:
                    head, _, tail = acc.partition(old)
                    _set_span(para, i, j + 1, head + new + tail)
                    found = True
                    break
            if found:
                break
        assert found, f"{label}: text present in paragraph but not in any run span"
        hits += 1
        break
    assert hits == 1, f"{label}: expected 1 paragraph hit, got {hits}\n  looking for: {old[:110]!r}"
    FIRED.append(label)


def insert_after(doc, anchor_text, lead, body, *, label):
    """Clone the paragraph containing `anchor_text` and insert a new one after it."""
    src = None
    for para in doc.paragraphs:
        if anchor_text in para.text:
            src = para
            break
    assert src is not None, f"{label}: anchor not found: {anchor_text[:80]!r}"
    new_p = copy.deepcopy(src._p)
    src._p.addnext(new_p)
    from docx.text.paragraph import Paragraph
    np = Paragraph(new_p, src._parent)
    assert len(np.runs) >= 2, f"{label}: clone has {len(np.runs)} runs, need >= 2"
    np.runs[0].text = lead
    np.runs[1].text = body
    for r in np.runs[2:]:
        r.text = ""
    FIRED.append(label)
    return np


def insert_before_first(doc, lead, *, label):
    """Clone the first paragraph and insert a version note ahead of it."""
    first = doc.paragraphs[0]
    new_p = copy.deepcopy(first._p)
    first._p.addprevious(new_p)
    from docx.text.paragraph import Paragraph
    np = Paragraph(new_p, first._parent)
    assert np.runs, f"{label}: clone has no runs"
    np.runs[0].text = lead
    np.runs[0].bold = False
    np.runs[0].italic = True
    for r in np.runs[1:]:
        r.text = ""
    FIRED.append(label)
    return np


# ───────────────────────────── shared replacement text ─────────────────────────────

EXEMPTION = (
    "The Shares are issued as compensation for bona fide services, pursuant to Purchaser's "
    "separate written compensation agreement with the Company, in reliance on the exemption "
    "from registration provided by Rule 701 under the Securities Act of 1933, as amended, and, "
    "to the extent Rule 701 is unavailable, in reliance on Section 4(a)(2) thereof. The Shares "
    "have not been registered and may not be transferred absent registration or an available "
    "exemption."
)

ELECTION_83B = (
    "The Shares are substantially nonvested property within the meaning of Section 83 of the "
    "Internal Revenue Code. Purchaser is strongly advised to consult his own tax adviser and to "
    "consider filing an election under Section 83(b) of the Code with the Internal Revenue "
    "Service no later than thirty (30) days after the Effective Date. That thirty-day period is "
    "fixed by statute and cannot be extended by the Company or by the Internal Revenue Service "
    "for any reason, including reasonable cause. If no timely election is made, Purchaser will "
    "generally recognize ordinary income on each vesting date in an amount equal to the "
    "then-current fair market value of the Shares vesting on that date less the price paid for "
    "them, rather than at the Effective Date when that value is lowest. The election is "
    "Purchaser's sole responsibility; the Company makes no tax representation and has no "
    "obligation to file it on Purchaser's behalf. A form of election is attached as Schedule B."
)

PRICE_SCHED = (
    "$0.001, being the fair market value of a share of Class A Common Stock as determined in "
    "good faith by the Board of Directors as of the Effective Date"
)

DILUTION = (
    "Measured PRE-Seed. These Shares carry NO anti-dilution protection and NO top-up right. "
    "They are diluted by the Seed Round and by every subsequent issuance on an ordinary "
    "pro-rata basis."
)

# character-identical to the Ankur copy built 2026-10-07 — this is one agreement
SHA_26_TAIL = (
    "The Company shall obtain directors' and officers' liability insurance on or before the "
    "closing of the Seed Round and shall cause the Investor Representative to be covered under "
    "that policy in his capacities as Board observer or director and as Investor "
    "Representative. The Company represents that, as of the date hereof, it does not maintain "
    "such insurance."
)
SHA_27_LEAD = "2.7  No personal liability of the Investor Representative.  "
SHA_27_BODY = (
    "The Investor Representative shall have no personal liability to any Investor for any "
    "action taken, or omitted to be taken, by him in good faith in his capacity as Investor "
    "Representative, except to the extent such action or omission constitutes fraud, bad faith, "
    "willful misconduct or gross negligence. The Investor Representative is not a fiduciary of, "
    "and owes no fiduciary duty to, any Investor, and may have interests that differ from those "
    "of any Investor. Each Investor, by executing this Agreement or a joinder to it, "
    "acknowledges and agrees to this Section 2.7. Nothing in this Section creates any liability "
    "or duty that would not otherwise exist, and nothing in this Section limits the "
    "indemnification provided under Section 2.6. This Section 2.7 survives termination of this "
    "Agreement."
)


# ═══════════════════════════════ RSPA — SUNJAY MATHEWS ═══════════════════════════════

d = Document(SENT / "Cinderella_Corp_-_RSPA_-_Sunjay_Mathews.docx")

sub(d,
    "Purchase price per Share to be set at fair market value as determined in good faith by "
    "the Board — confirm with counsel before execution.",
    "The purchase price of $0.001 per Share is the fair market value of a share of Class A "
    "Common Stock as determined in good faith by the Board of Directors as of the Effective "
    "Date.",
    label="S-header-price")

sub(d,
    "The Shares are issued pursuant to the exemption from registration provided by "
    "[Rule 701 / Regulation D] under the Securities Act of 1933, as amended. The Shares have "
    "not been registered and may not be transferred absent registration or an available "
    "exemption.",
    EXEMPTION, label="S-1.3-exemption")

sub(d,
    "Purchaser is strongly advised to consult his or her own tax adviser and to consider "
    "filing an election under Section 83(b) of the Internal Revenue Code within thirty (30) "
    "days of the Effective Date. The election is Purchaser's sole responsibility; the Company "
    "makes no tax representation and has no obligation to file it on Purchaser's behalf. A form "
    "of election is attached as Schedule B.".replace("'", "’"),
    ELECTION_83B.replace("'", "’"), label="S-5.1-83b")

sub(d, "$0.001  [FMV as determined by the Board]", PRICE_SCHED,
    label="S-schedA-price", where="Purchase price per Share")

sub(d,
    "20.000% of the fully-diluted capitalization immediately prior to the Seed Round "
    "(pre-Seed fully-diluted total: 4,166,667 shares); approximately 16.875% immediately "
    "following the Seed Round",
    "20.000% of the fully-diluted capitalization immediately prior to the Seed Round "
    "(pre-Seed fully-diluted total: 4,166,667 shares). Following a Seed Round sold for fifteen "
    "percent (15%) of the post-money fully-diluted capitalization, this position would "
    "represent approximately 16.875%; that figure is illustrative only, and the actual "
    "post-Seed percentage depends on the final size, price and structure of the Seed Round",
    label="S-schedA-pct")

sub(d,
    "Measured PRE-Seed. Unlike the Company's arrangement with Ankur Jain, these Shares carry "
    "NO anti-dilution protection and NO top-up. They are diluted by the Seed Round and by "
    "every subsequent issuance on an ordinary pro-rata basis.".replace("'", "’"),
    DILUTION, label="S-schedA-dilution")

insert_before_first(d, "Revised 2026-10-07 — securities exemption, purchase price and "
                       "83(b) language settled; supersedes the 2026-09-18 copy.",
                    label="S-version-note")
d.save(OUT / "Cinderella_Corp_-_RSPA_-_Sunjay_Mathews.docx")


# ═══════════════════════════════ RSPA — GREG KRISTOF ═══════════════════════════════

d = Document(SENT / "Cinderella_Corp_-_RSPA_-_Greg_Kristof.docx")

sub(d,
    "The vesting term and any acceleration remain bracketed in the Strategic Adviser Agreement "
    "and must be settled before execution. Purchase price per Share to be set at fair market "
    "value as determined in good faith by the Board — confirm with counsel.",
    "The purchase price of $0.001 per Share is the fair market value of a share of Class A "
    "Common Stock as determined in good faith by the Board of Directors as of the Effective "
    "Date. The vesting term is twenty-four (24) months with no cliff and no acceleration, as "
    "restated in Schedule A; the Strategic Adviser Agreement is to be conformed to match.",
    label="G-header")

sub(d, "at a purchase price of $[____] per Share", "at a purchase price of $0.001 per Share",
    label="G-1.1-price")

sub(d,
    "The Shares are issued pursuant to the exemption from registration provided by "
    "[Rule 701 / Regulation D] under the Securities Act of 1933, as amended. The Shares have "
    "not been registered and may not be transferred absent registration or an available "
    "exemption.",
    EXEMPTION, label="G-1.3-exemption")

sub(d,
    "Purchaser is strongly advised to consult his or her own tax adviser and to consider "
    "filing an election under Section 83(b) of the Internal Revenue Code within thirty (30) "
    "days of the Effective Date. The election is Purchaser's sole responsibility; the Company "
    "makes no tax representation and has no obligation to file it on Purchaser's behalf. A form "
    "of election is attached as Schedule B.".replace("'", "’"),
    ELECTION_83B.replace("'", "’"), label="G-5.1-83b")

sub(d, "$______________  [FMV as determined by the Board]", PRICE_SCHED,
    label="G-schedA-price", where="Purchase price per Share")

sub(d,
    "4.000% of the fully-diluted capitalization immediately prior to the Seed Round "
    "(pre-Seed fully-diluted total: 4,166,667 shares); approximately 3.375% immediately "
    "following the Seed Round",
    "4.000% of the fully-diluted capitalization immediately prior to the Seed Round "
    "(pre-Seed fully-diluted total: 4,166,667 shares). Following a Seed Round sold for fifteen "
    "percent (15%) of the post-money fully-diluted capitalization, this position would "
    "represent approximately 3.375%; that figure is illustrative only, and the actual post-Seed "
    "percentage depends on the final size, price and structure of the Seed Round",
    label="G-schedA-pct")

sub(d, "______________  [Effective Date — confirm]", "Effective Date",
    label="G-schedA-vcd", where="Vesting commencement date")

sub(d,
    "Monthly over [24] months from the vesting commencement date, no cliff, subject to "
    "continuous service — [24] equal monthly installments of 6,944 Shares (the final "
    "installment 6,955 Shares). TERM STILL BRACKETED IN THE ADVISER AGREEMENT; confirm the "
    "number of months and restate this schedule before execution.",
    "Twenty-four (24) equal monthly installments of 6,944 Shares (the final installment 6,955 "
    "Shares), no cliff, the first on the last day of the first full calendar month following "
    "the vesting commencement date and each subsequent installment on the last day of each full "
    "calendar month thereafter, subject to continuous service. No installment vests for a "
    "partial calendar month.",
    label="G-schedA-vesting")

sub(d,
    "[None provided. The Strategic Adviser Agreement leaves change-of-control acceleration "
    "open as an optional, unresolved item. Compare Sunjay Mathews, who has both six-month "
    "severance acceleration and full single-trigger acceleration on a Change of Control.]",
    "None. No vesting acceleration applies on termination of service or on a Change of Control. "
    "Unvested Shares remain subject to Article 3.",
    label="G-schedA-accel")

sub(d,
    "Measured PRE-Seed. Unlike the Company's arrangement with Ankur Jain, these Shares carry "
    "NO anti-dilution protection and NO top-up. They are diluted by the Seed Round and by "
    "every subsequent issuance on an ordinary pro-rata basis.".replace("'", "’"),
    DILUTION, label="G-schedA-dilution")

insert_before_first(d, "Revised 2026-10-07 — securities exemption, purchase price, vesting "
                       "term, acceleration and 83(b) language settled; supersedes the "
                       "2026-09-18 copy.",
                    label="G-version-note")
d.save(OUT / "Cinderella_Corp_-_RSPA_-_Greg_Kristof.docx")


# ════════════════════════ STOCKHOLDERS' AGREEMENTS — BOTH ════════════════════════

for who, fname in (("Sunjay Mathews", "Cinderella_Corp_-_Stockholders_Agreement_-_Sunjay_Mathews.docx"),
                   ("Greg Kristof", "Cinderella_Corp_-_Stockholders_Agreement_-_Greg_Kristof.docx")):
    tag = who.split()[0][0]
    d = Document(SENT / fname)

    sub(d,
        "The Company will use commercially reasonable efforts to include the Investor "
        "Representative under its directors' and officers' liability insurance in his "
        "capacities as Board observer or director and as Investor "
        "Representative.".replace("'", "’"),
        SHA_26_TAIL.replace("'", "’"), label=f"{tag}SHA-2.6-dando")

    insert_after(d, "2.6  Indemnification of the Investor Representative.",
                 SHA_27_LEAD, SHA_27_BODY.replace("'", "’"),
                 label=f"{tag}SHA-2.7-insert")

    insert_before_first(d, "Conformed 2026-10-07 — Sections 2.6 and 2.7 brought into line "
                           "with the single current text of this Agreement; supersedes the "
                           "2026-09-18 copy.",
                        label=f"{tag}SHA-version-note")
    d.save(OUT / fname)


# ═════════════════════════════════ VERIFICATION ═════════════════════════════════

print(f"{len(FIRED)} changes applied:")
for f in FIRED:
    print("  ✓", f)

print("\nverification:")
checks = {
    "Cinderella_Corp_-_RSPA_-_Sunjay_Mathews.docx": [
        ("Rule 701 under the Securities Act", True),
        ("[Rule 701 / Regulation D]", False),
        ("cannot be extended by the Company", True),
        ("[FMV as determined by the Board]", False),
        ("Ankur Jain", False),
        ("confirm with counsel", False),
        ("illustrative only", True),
        ("833,333 shares of Class A Common Stock", True),
    ],
    "Cinderella_Corp_-_RSPA_-_Greg_Kristof.docx": [
        ("Rule 701 under the Securities Act", True),
        ("[Rule 701 / Regulation D]", False),
        ("$[____]", False),
        ("[FMV as determined by the Board]", False),
        ("Ankur Jain", False),
        ("Sunjay Mathews", False),
        ("TERM STILL BRACKETED", False),
        ("[24]", False),
        ("Twenty-four (24) equal monthly installments", True),
        ("166,667 shares of Class A Common Stock", True),
    ],
    "Cinderella_Corp_-_Stockholders_Agreement_-_Sunjay_Mathews.docx": [
        ("2.7  No personal liability of the Investor Representative.", True),
        ("shall obtain directors’ and officers’ liability insurance", True),
        ("commercially reasonable efforts to include the Investor", False),
        ("Sunjay Mathews", True),
    ],
    "Cinderella_Corp_-_Stockholders_Agreement_-_Greg_Kristof.docx": [
        ("2.7  No personal liability of the Investor Representative.", True),
        ("shall obtain directors’ and officers’ liability insurance", True),
        ("commercially reasonable efforts to include the Investor", False),
    ],
}
bad = 0
for fname, cs in checks.items():
    t = "\n".join(p.text for p in Document(OUT / fname).paragraphs)
    for needle, want in cs:
        got = needle in t
        ok = got is want
        if not ok:
            bad += 1
        print(f"  {'OK  ' if ok else 'FAIL'} {fname[22:48]:<28} "
              f"{'has' if want else 'no ':<3} {needle[:52]!r}")

# the two Stockholders' Agreements must be character-identical apart from the signature block
sa = [p.text for p in Document(OUT / "Cinderella_Corp_-_Stockholders_Agreement_-_Sunjay_Mathews.docx").paragraphs]
ga = [p.text for p in Document(OUT / "Cinderella_Corp_-_Stockholders_Agreement_-_Greg_Kristof.docx").paragraphs]
body_s = [x for x in sa[:44] if x.strip()]
body_g = [x for x in ga[:44] if x.strip()]
diffs = [(i, a, b) for i, (a, b) in enumerate(zip(body_s, body_g)) if a != b]
operative = [d for d in diffs if "2026 (the" not in d[1]]
print(f"\n  {'OK  ' if not operative else 'FAIL'} SHA bodies identical apart from the date blank "
      f"({len(diffs)} diff(s), {len(operative)} operative)")
for i, a, b in operative:
    print(f"       para {i}: {a[:90]!r}\n              vs {b[:90]!r}")
bad += len(operative)

print(f"\n{'ALL CHECKS PASSED' if not bad else f'{bad} CHECK(S) FAILED'}")
sys.exit(1 if bad else 0)
