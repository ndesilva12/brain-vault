# -*- coding: utf-8 -*-
"""Conform Sunjay's Partner Agreement and Greg's Strategic Adviser Agreement to the 2026-10-07 set.

SOURCE OF TRUTH: the two .docx files Norman sent 2026-10-07, copied to
scratchpad/sent-partner-adviser/. Patch build, every change asserted.
Output: out-partner-adviser-2026-10-07/

WHY — these two agreements are the PARENT documents for grants whose terms were settled
elsewhere today, and both had drifted out of sync with the paper that implements them:

  GREG'S ADVISER AGREEMENT was the worse of the two.
   • ⚠️ NUMBERING BUG — two sections were numbered 2.3 ("Vesting" and "Forfeiture / Repurchase"),
     so everything after it was off by one. Renumbered 2.3 Vesting / 2.4 Forfeiture / 2.5 Class A
     / 2.6 Tax / 2.7 No cash. Greg's RSPA Schedule A cites "Strategic Adviser Agreement §2.3" for
     the vesting schedule, which still resolves correctly because Vesting keeps 2.3.
   • EVERY economic term was still bracketed — [4]%, [24] months, [no cliff], [Effective Date /
     vesting commencement date], [Optional: acceleration ... confirm], [30] days' notice,
     [24] months non-circ, [Rule 701 / Reg D], [Venue / arbitration], [CEO / President] — while
     his RSPA, settled today, states all of them. The RSPA was the only document carrying real
     terms, and §8.2 makes both part of one agreement. Settled here to match exactly:
     4% / 166,667 shares / $0.001 / 24 months / no cliff / Effective Date / no acceleration /
     Rule 701 / Delaware Court of Chancery.
   • §2.5 TAX WAS BACKWARDS FOR HIM. It read like Ankur's ("consider filing"), but Greg's shares
     VEST, so 83(b) is critical, not optional. Rewritten to match his RSPA §5.1 — 30 days,
     statutory, non-extendable, and what missing it costs.
   • §7 NON-CIRC HAD NO CARVE-OUT, only a bracketed note saying one was needed so it would not
     impair Zero Gravity / 6th Sense. As drafted it would have barred him from his own existing
     relationships. Carve-out added, worded identically to Stockholders' Agreement §7.2 so the
     two cannot be read against each other (SHA §7.3 defers to this agreement, so this is the
     operative text).
   • Internal drafting notes removed: the "Working draft, 2026-08-15, for review with Loeb &
     Loeb and Sunjay" header (which also told Greg his paper is reviewed by Sunjay) and the
     four-item "For counsel before use" list at the end — all four items are now resolved.

  SUNJAY'S PARTNER AGREEMENT was sound. Four changes, all consequences of today's work:
   • §2.2 hardcoded a "[15]% Seed Round" and "~16.9%". The round is now an offering of UP TO
     $1.5M with no minimum, so a fixed post-Seed number cannot be stated as fact. Restated as an
     illustration, and 16.9% corrected to 16.875% to agree with his RSPA Schedule A.
   • §2.2 ended "must be confirmed against the actual Seed Round terms and cap table model
     before use" — a note to the drafter sitting in a counterparty document. Removed.
   • §3.1's "25% maximum" was ambiguous as to when it is measured. Left at 20% + 5% on the
     pre-Seed basis and made explicit that it is a ceiling on what may be GRANTED, not a
     percentage to be maintained after dilution. Without this, "maximum equity 25%" is arguable
     as a top-up right — i.e. anti-dilution by the back door, which §1.5(c), §2.5 and §3.6 all
     say he does not have.
   • §4.1 told him to consider an 83(b) "within thirty (30) days of each grant". Correct for the
     Base Shares, WRONG for Milestone Shares: those are fully vested on issuance under §3.6, so
     no 83(b) is applicable to them — the same reasoning that removed Ankur's 83(b) today. Split
     accordingly, and the Base Shares limb strengthened to match his RSPA §5.1.
   • §2.1 now states the share count (833,333) so the Partner Agreement, the RSPA and the cap
     table all carry the same number.

NOT CHANGED, DELIBERATELY:
  • Sunjay §1.7 (no cash compensation for 12 months). The parent raise is budgeted to pay him a
    salary, which §1.7 permits only by separate written agreement. That writing does not exist.
    Flagged for Norman, not patched — it is a business decision, not a drafting defect.
  • Greg §2.7 (no cash; paid consulting from 2027 under a separate Consulting Agreement). Greg
    agreed $4k/mo on Aug 30 2026 per the register, and the Consulting Agreement starts 1/1/27.
    Sept–Dec 2026 is therefore equity-only on this paper. Flagged, not patched.
  • Greg §6 IP ("works made for hire / assigned"). "Work made for hire" does not reach most
    independent-contractor work, but the assignment limb carries it. Cosmetic; left alone.
"""
import copy
import sys
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph

SENT = Path("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c"
            "/scratchpad/sent-partner-adviser")
OUT = Path(__file__).parent / "out-partner-adviser-2026-10-07"
OUT.mkdir(exist_ok=True)

FIRED = []


def sub(doc, old, new, *, label, where=None):
    hits = 0
    for para in doc.paragraphs:
        if old not in para.text or (where and where not in para.text):
            continue
        runs, found = para.runs, False
        for i in range(len(runs)):
            acc = ""
            for j in range(i, len(runs)):
                acc += runs[j].text
                if old in acc:
                    head, _, tail = acc.partition(old)
                    runs[i].text = head + new + tail
                    for k in range(i + 1, j + 1):
                        runs[k].text = ""
                    found = True
                    break
            if found:
                break
        assert found, f"{label}: text in paragraph but in no run span"
        hits += 1
        break
    assert hits == 1, f"{label}: expected 1 hit, got {hits}\n  needle: {old[:120]!r}"
    FIRED.append(label)


def find(doc, needle, *, label):
    for para in doc.paragraphs:
        if needle in para.text:
            return para
    raise AssertionError(f"{label}: not found: {needle[:90]!r}")


def drop(doc, needle, *, label):
    para = find(doc, needle, label=label)
    para._p.getparent().remove(para._p)
    FIRED.append(label)


def drop_from(doc, needle, *, label):
    """Delete the paragraph containing `needle` and every paragraph after it."""
    para = find(doc, needle, label=label)
    body = para._p.getparent()
    kids = list(body)
    n = 0
    for el in kids[kids.index(para._p):]:
        if el.tag.endswith('}p'):
            body.remove(el)
            n += 1
    FIRED.append(f"{label} ({n} paras)")


def insert_after(doc, anchor, lead, body, *, label):
    src = find(doc, anchor, label=label)
    new_p = copy.deepcopy(src._p)
    src._p.addnext(new_p)
    np = Paragraph(new_p, src._parent)
    assert np.runs, f"{label}: clone has no runs"
    if len(np.runs) == 1:
        np.runs[0]._r.addnext(copy.deepcopy(np.runs[0]._r))
    np.runs[0].text = lead
    np.runs[0].bold = True
    np.runs[1].text = body
    np.runs[1].bold = False
    for r in np.runs[2:]:
        r.text = ""
    FIRED.append(label)
    return np


# Both documents use STRAIGHT apostrophes throughout (verified: Greg 14 straight / 0 curly,
# Sunjay 47 straight / 0 curly), though Sunjay uses curly DOUBLE quotes. Replacement text must
# match each document's own convention or the needles miss and the inserted prose looks foreign.
Q = "'"


# ══════════════════════ GREG KRISTOF — STRATEGIC ADVISER AGREEMENT ══════════════════════

d = Document(SENT / "Greg_Kristof_Strategic_Adviser_Agreement.docx")

# ── internal drafting notes out ──
sub(d,
    "Working draft, 2026-08-15, for review with Loeb & Loeb and Sunjay before use. Not an offer "
    "of securities. Entity: Cinderella Corp., a Delaware corporation. Bracketed items [LIKE "
    "THIS] need confirmation. Confirm adviser" + Q + "s exact legal name (Greg Kristof per vault)._",
    "Revised 2026-10-07 — equity percentage, share count, purchase price, vesting term, "
    "acceleration, securities exemption, notice periods, non-circumvention carve-out and venue "
    "all settled; conformed to the Restricted Stock Purchase Agreement of even date. Entity: "
    "Cinderella Corp., a Delaware corporation.",
    label="G-adv header note")

drop_from(d, "For counsel before use", label="G-adv counsel checklist removed")

# ── §2.1 grant: share count and price stated ──
sub(d,
    "the Company will grant Adviser [4]% of the Company" + Q + "s Class A Common Stock",
    "the Company will grant Adviser four percent (4%) of the Company" + Q + "s Class A Common Stock",
    label="G-adv §2.1 — 4%")
sub(d,
    "in the Company" + Q + "s standard form. [Confirm exact share count once per-share price is set.]",
    "in the Company" + Q + "s standard form. The Shares are 166,667 shares of Class A Common Stock, "
    "being four percent (4%) of the pre-Seed fully-diluted total of 4,166,667 shares, at a "
    "purchase price of $0.001 per share, which the Board has determined in good faith to be the "
    "fair market value of a share of Class A Common Stock as of the Effective Date.",
    label="G-adv §2.1 — share count and price")

# ── §2.2 dilution illustration: seed no longer a fixed quantity ──
sub(d,
    "For illustration only, a [4]% pre-Seed position becomes approximately [3.4]% following a "
    "[15]% Seed Round.",
    "The Seed Round is an offering of up to $1,500,000 of Class A Common Stock at $2.025 per "
    "share, with no minimum aggregate raise, and may close for less than the full amount; "
    "Adviser" + Q + "s post-Seed percentage therefore cannot be fixed in advance. For illustration "
    "only, were the full amount sold, a 4% pre-Seed position would become approximately 3.375% "
    "(166,667 shares of a 4,938,272-share fully-diluted total). That figure is an illustration "
    "only and the actual percentage depends on the final size of the Seed Round.",
    label="G-adv §2.2 — seed illustration")

# ── §2.3 vesting: all brackets settled ──
sub(d,
    "The Shares vest monthly over [24] months from the [Effective Date / vesting commencement "
    "date], [no cliff], subject to Adviser" + Q + "s continued service under this Agreement. "
    "[Optional: acceleration on a change of control — single-trigger / double-trigger — confirm.]",
    "The Shares vest in twenty-four (24) equal monthly installments of 6,944 Shares (the final "
    "installment 6,955 Shares) from the Effective Date, with no cliff, the first installment "
    "vesting on the last day of the first full calendar month following the Effective Date and "
    "each subsequent installment on the last day of each full calendar month thereafter, in each "
    "case subject to Adviser" + Q + "s continued service under this Agreement. No installment vests "
    "in respect of a partial calendar month. No acceleration of vesting applies, whether on "
    "termination of service or on a change of control.",
    label="G-adv §2.3 — vesting settled")

# ── renumber the duplicate 2.3 and everything after it ──
for old, new, lbl in (
    ("2.3 Forfeiture / Repurchase.", "2.4 Forfeiture / Repurchase.", "G-adv renumber → 2.4"),
    ("2.4 Class A only.", "2.5 Class A only.", "G-adv renumber → 2.5"),
    ("2.5 Tax / 83(b).", "2.6 Tax / 83(b).", "G-adv renumber → 2.6"),
    ("2.6 No cash.", "2.7 No cash.", "G-adv renumber → 2.7"),
):
    sub(d, old, new, label=lbl)

# ── tax: 83(b) is critical for Greg, not optional ──
sub(d,
    "Adviser is advised to consult his own tax adviser and to consider filing an 83(b) election "
    "within 30 days of grant. The Company makes no tax representation. [Confirm FMV / 409A "
    "support and the Rule 701 / Reg D exemption for the issuance — counsel.]",
    "The Shares are substantially nonvested property within the meaning of Section 83 of the "
    "Internal Revenue Code. Adviser is strongly advised to consult his own tax adviser and to "
    "consider filing an election under Section 83(b) of the Code with the Internal Revenue "
    "Service no later than thirty (30) days after the Effective Date. That thirty-day period is "
    "fixed by statute and cannot be extended by the Company or by the Internal Revenue Service "
    "for any reason. If no timely election is made, Adviser will generally recognize ordinary "
    "income on each vesting date equal to the then-current fair market value of the Shares "
    "vesting on that date less the price paid for them, rather than at the Effective Date when "
    "that value is lowest. The election is Adviser" + Q + "s sole responsibility and the Company has "
    "no obligation to file it on his behalf. The Shares are issued as compensation for bona fide "
    "services under this Agreement in reliance on the exemption from registration provided by "
    "Rule 701 under the Securities Act of 1933, as amended, and, to the extent Rule 701 is "
    "unavailable, in reliance on Section 4(a)(2) thereof. The Company makes no tax "
    "representation.",
    label="G-adv §2.6 — 83(b) and exemption")

# ── §4.2 notice period ──
sub(d, "Either party may terminate on [30] days" + Q + " written notice",
    "Either party may terminate on thirty (30) days" + Q + " written notice",
    label="G-adv §4.2 — 30 days")

# ── §7 non-circumvention: real carve-out, matching Stockholders' Agreement §7.2 ──
sub(d,
    "during the term and for [24] months after",
    "during the term and for twenty-four (24) months after",
    label="G-adv §7 — 24 months")
sub(d,
    "nor solicit Company personnel. [Confirm scope so it doesn" + Q + "t impair his existing Zero "
    "Gravity relationships — carve out pre-existing relationships.]",
    "nor solicit Company personnel. Nothing in this Section restricts Adviser from initiating, "
    "continuing or maintaining any personal or professional relationship with any person or "
    "entity, whenever and however that relationship arose, including any relationship arising "
    "through Zero Gravity, 6th Sense or any other business of Adviser permitted under "
    "Section 1.3. Adviser" + Q + "s obligations under Sections 5 and 6 continue to apply to Company "
    "confidential information and intellectual property in any such communication.",
    label="G-adv §7 — relationship carve-out")

# ── §8.1 venue ──
sub(d, "Governing Law. Delaware. [Venue / arbitration — confirm.]",
    "Governing law; jurisdiction. This Agreement is governed by the laws of the State of "
    "Delaware, without regard to its conflicts of laws principles. The Court of Chancery of the "
    "State of Delaware has exclusive jurisdiction over any dispute arising out of or relating to "
    "this Agreement (or, if that court lacks subject-matter jurisdiction, the federal or state "
    "courts located in the State of Delaware).",
    label="G-adv §8.1 — venue")

sub(d, "Title: [CEO / President]", "Title: Founder & Chief Executive Officer",
    label="G-adv signature title")

d.save(OUT / "Greg_Kristof_Strategic_Adviser_Agreement.docx")


# ══════════════════════════ SUNJAY MATHEWS — PARTNER AGREEMENT ══════════════════════════

d = Document(SENT / "Sunjay_Mathews_Partner_Agreement.docx")

sub(d,
    "equal to twenty percent (20%) of the Company (the “Base Shares”), measured on the "
    "fully-diluted capitalization of the Company immediately PRIOR to the Seed Round (i.e., "
    "pre-money / pre-Seed).",
    "equal to twenty percent (20%) of the Company (the “Base Shares”), measured on the "
    "fully-diluted capitalization of the Company immediately PRIOR to the Seed Round (i.e., "
    "pre-money / pre-Seed). The Base Shares are 833,333 shares of Class A Common Stock, being "
    "twenty percent (20%) of the pre-Seed fully-diluted total of 4,166,667 shares, issued under "
    "the Restricted Stock Purchase Agreement of even date.",
    label="S-partner §2.1 — share count")

sub(d,
    "and assuming a [15]% Seed Round in which Ankur Jain" + Q + "s position does not dilute (per the "
    "Company" + Q + "s separate arrangement with him), Norman, Partner, and Greg collectively absorb "
    "more than 15% dilution to hold Ankur flat and still deliver 15% to the Seed investors. On "
    "that assumption, Partner" + Q + "s approximate post-Seed position would be ~16.9% (not the ~17% a "
    "simple pro-rata calculation would suggest). This figure is illustrative only and must be "
    "confirmed against the actual Seed Round terms and cap table model before use.",
    "and assuming a Seed Round sold for fifteen percent (15%) of the post-money fully-diluted "
    "capitalization in which Ankur Jain" + Q + "s position does not dilute (per the Company" + Q + "s "
    "separate arrangement with him), Norman, Partner and Greg collectively absorb more than 15% "
    "dilution to hold Ankur flat and still deliver 15% to the Seed investors. On that assumption "
    "Partner" + Q + "s post-Seed position would be 16.875% (not the ~17% a simple pro-rata "
    "calculation would suggest) — 833,333 shares of a 4,938,272-share fully-diluted total. The "
    "Seed Round is an offering of up to $1,500,000 of Class A Common Stock at $2.025 per share "
    "with no minimum aggregate raise, and may close for less than the full amount, so that figure "
    "is an illustration only and Partner" + Q + "s actual post-Seed percentage depends on the final "
    "size of the Seed Round.",
    label="S-partner §2.2 — seed illustration")

sub(d,
    "bringing Partner" + Q + "s maximum equity to twenty-five percent (25%), by achieving Track A "
    "and/or Track B below.",
    "bringing the maximum equity grantable to Partner under this Agreement to twenty-five "
    "percent (25%) measured on the same pre-Seed basis as Section 2.1, by achieving Track A "
    "and/or Track B below. That twenty-five percent (25%) is a ceiling on what may be granted "
    "and is not a percentage to be maintained: consistent with Sections 1.5(c), 2.5 and 3.6, "
    "Partner has no anti-dilution protection and no right to any top-up, and his actual holding "
    "after the Seed Round or any subsequent issuance will be lower.",
    label="S-partner §3.1 — 25% is a ceiling, not a floor")

sub(d,
    "Partner is strongly advised to consult his own tax adviser and to consider filing an 83(b) "
    "election within thirty (30) days of each grant. The Company makes no tax representation.",
    "The Base Shares are substantially nonvested property within the meaning of Section 83 of "
    "the Internal Revenue Code. Partner is strongly advised to consult his own tax adviser and "
    "to consider filing an election under Section 83(b) of the Code with the Internal Revenue "
    "Service no later than thirty (30) days after the Effective Date. That thirty-day period is "
    "fixed by statute and cannot be extended by the Company or by the Internal Revenue Service "
    "for any reason. If no timely election is made, Partner will generally recognize ordinary "
    "income on each vesting date under Section 2.3(b) equal to the then-current fair market "
    "value of the Base Shares vesting on that date less the price paid for them, rather than at "
    "the Effective Date when that value is lowest. The election is Partner" + Q + "s sole "
    "responsibility and the Company has no obligation to file it on his behalf. Milestone Shares "
    "are fully vested on issuance under Section 3.6 and are accordingly not substantially "
    "nonvested property, so no election under Section 83(b) is applicable to them — their "
    "issuance is itself a taxable event measured at the fair market value on the issuance date. "
    "The Company makes no tax representation.",
    label="S-partner §4.1 — 83(b) split Base vs Milestone")

insert_after(d, "7.9  Independent counsel.",
             "7.10  Version.  ",
             "This Agreement is the 2026-10-07 revision, conforming Sections 2.1, 2.2, 3.1 and "
             "4.1 to the Restricted Stock Purchase Agreement of even date and to the final terms "
             "of the Seed Round offering. It supersedes all earlier drafts.",
             label="S-partner version note")

d.save(OUT / "Sunjay_Mathews_Partner_Agreement.docx")


# ════════════════════════════════ VERIFICATION ════════════════════════════════

print(f"{len(FIRED)} changes applied:")
for f in FIRED:
    print("  ✓", f)

checks = {
    "Greg_Kristof_Strategic_Adviser_Agreement.docx": [
        ("[4]%", False), ("[24]", False), ("[no cliff]", False), ("[30]", False),
        ("[Rule 701 / Reg D]", False), ("[Optional: acceleration", False),
        ("[Venue / arbitration", False), ("[CEO / President]", False),
        ("[Confirm", False), ("For counsel before use", False),
        ("Working draft, 2026-08-15", False),
        ("2.3 Vesting.", True), ("2.4 Forfeiture / Repurchase.", True),
        ("2.5 Class A only.", True), ("2.6 Tax / 83(b).", True), ("2.7 No cash.", True),
        ("166,667 shares of Class A Common Stock", True),
        ("Rule 701 under the Securities Act", True),
        ("cannot be extended by the Company", True),
        ("No acceleration of vesting applies", True),
        ("whenever and however that relationship arose", True),
        ("Court of Chancery of the State of Delaware", True),
        ("Founder & Chief Executive Officer", True),
    ],
    "Sunjay_Mathews_Partner_Agreement.docx": [
        ("[15]%", False),
        ("~16.9%", False),
        ("must be confirmed against the actual Seed Round terms", False),
        ("within thirty (30) days of each grant", False),
        ("833,333 shares of Class A Common Stock", True),
        ("16.875%", True),
        ("is a ceiling on what may be granted", True),
        ("no election under Section 83(b) is applicable to them", True),
        ("up to $1,500,000 of Class A Common Stock at $2.025 per share", True),
        ("7.10  Version.", True),
    ],
}
print("\nverification:")
bad = 0
for fname, cs in checks.items():
    t = "\n".join(p.text for p in Document(OUT / fname).paragraphs)
    for needle, want in cs:
        ok = (needle in t) is want
        bad += not ok
        print(f"  {'OK  ' if ok else 'FAIL'} {fname[:26]:<28} {'has' if want else 'no ':<3} {needle[:48]!r}")

# no section number may appear twice as a lead in Greg's agreement
import re
leads = [m.group(1) for p in Document(OUT / "Greg_Kristof_Strategic_Adviser_Agreement.docx").paragraphs
         if (m := re.match(r"^(\d+\.\d+)\s", p.text.strip()))]
dupes = {x for x in leads if leads.count(x) > 1}
bad += len(dupes)
print(f"  {'OK  ' if not dupes else 'FAIL'} Greg: no duplicate section numbers "
      f"({len(leads)} numbered sections{', dupes: ' + str(sorted(dupes)) if dupes else ''})")

print(f"\n{'ALL CHECKS PASSED' if not bad else f'{bad} CHECK(S) FAILED'}")
sys.exit(1 if bad else 0)
