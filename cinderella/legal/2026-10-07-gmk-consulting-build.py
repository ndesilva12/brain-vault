# -*- coding: utf-8 -*-
"""Complete Greg Kristof's Consulting Agreement (GMK Sports Consulting, $4,000/month).

SOURCE OF TRUTH: GMK_Consulting_Agreement.docx sent by Norman 2026-10-07, copied to
scratchpad/sent-consulting/. Patch build, every change asserted.
Output: out-gmk-consulting-2026-10-07/

This is the SERVICE VENDOR agreement. It has nothing to do with Greg's equity, which sits in the
Strategic Adviser Agreement and the RSPA. §1.4 already keeps the two apart; that separation is
preserved throughout and is the reason §3.2 bars any equity, success fee or commission here.

TWO SECTIONS WERE EMPTY HEADINGS. In the vault markdown they read:
   §3.4 Invoicing  — "[Company pays automatically monthly / Consultant invoices monthly — confirm.]"
   §9.4 Indemnification / Limitation of Liability — "[Standard mutual — counsel to complete.]"
Both written. Choices made, since Norman asked for best judgement rather than perfection:
  • INVOICING: Consultant invoices monthly, net 30, with a disputed-portion mechanic and a W-9
    gate before first payment. Invoicing beats auto-pay for a vendor on a 1099 — it creates the
    record that supports the independent-contractor characterisation in §4, and auto-pay on a
    standing retainer is the thing that keeps paying after everyone has stopped paying attention.
  • INDEMNITY: mutual, for breach / gross negligence / willful misconduct, plus a one-way
    Consultant indemnity for his own taxes and for any claim that he or his personnel is really a
    Company employee — the actual exposure in a 1099 engagement. No consequential damages either
    way. Liability capped at 12 months of fees, with carve-outs for the indemnities,
    confidentiality, IP and non-circumvention, so the cap cannot swallow the clauses that matter.

OTHER UNFINISHED OR INCONSISTENT ITEMS, all fixed:
  • ⚠️ §8 NON-CIRCUMVENTION HAD NO RELATIONSHIP CARVE-OUT — the same defect found in his Strategic
    Adviser Agreement §7 earlier today. Left as-is it would contradict that agreement: one permits
    his Zero Gravity / 6th Sense relationships and the other forbids them, same counterparty, same
    restriction, two answers. Carve-out added, worded identically to Adviser Agreement §7 and to
    Stockholders' Agreement §7.2.
  • ⚠️ §1.5 NCAA AND RECRUITING COMPLIANCE — NEW, and the most important addition. Greg is being
    paid for a "basketball roster / NIL / coach / event network", and neither this agreement nor
    his Adviser Agreement said one word about NCAA limits. The project's whole compliance posture
    (cinderella/CLAUDE.md, "Norman's operational role") turns on nobody contacting unsigned
    prospects, nobody acting as an athlete agent for compensation, and nobody touching
    student-athlete compensation. A paid consultant whose value IS that network is exactly where
    that risk lands. Drafted from Norman's own standing rules, and it runs both ways — Greg agrees
    not to do these things, and the Company agrees not to direct him to.
  • §3.3 Expenses said only "reasonable, pre-approved". The October Expense & Travel Policy
    applies by its own terms to "contractors", and gates any single item over $500 on Ankur Jain's
    written approval. §3.3 now says so, so the two documents cannot diverge.
  • §2.2 "[30] days" → thirty (30) days.
  • §9.1 was the bare word "Delaware." → full governing-law, exclusive-jurisdiction and jury-waiver
    clause, matching Adviser Agreement §8.1, RSPA §9.1 and Stockholders' Agreement §9.1.
  • §1.3 named only "6th Sense"; the Adviser Agreement §1.3 names "Zero Gravity / 6th Sense".
    Aligned, so the carve-outs in both documents cover the same businesses.
  • Counterparty is GMK SPORTS CONSULTING, not "GMK Consulting". Renamed in the preamble and the
    signature block, and the signature block rebuilt for an entity (By / Name / Title) rather than
    an individual.
  • NEW §9.6 Notices, §9.7 Severability (with reformation of §8, matching Sunjay's §7.6), and
    §9.8 Authority — which carries a KEY-PERSON term: Greg performs personally and GMK may not
    substitute anyone without consent. The Company is buying Greg's network, not GMK's generic
    services, and nothing in the draft said so.
  • "Title: Founder / CEO" → "Founder & Chief Executive Officer", matching every other document.

FLAGGED, NOT CHANGED:
  ⚠️ The Effective Date stays JANUARY 1, 2027 as sent. Greg agreed $4k/month on Aug 30 2026, so
  Sept–Dec 2026 remains unpapered cash. Raised with Norman twice; it is a business decision, not a
  drafting defect, and moving the start date without being asked would change the deal.
"""
import copy
import sys
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph

SENT = Path("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c"
            "/scratchpad/sent-consulting")
OUT = Path(__file__).parent / "out-gmk-consulting-2026-10-07"
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


def find(doc, needle, *, label, startswith=False):
    for para in doc.paragraphs:
        t = para.text.strip()
        if (t.startswith(needle) if startswith else needle in para.text):
            return para
    raise AssertionError(f"{label}: not found: {needle[:90]!r}")


def append_body(doc, lead, body, *, label):
    """Append a non-bold run of `body` to the paragraph starting with `lead`.
    Used for the two sections that were delivered as bare headings."""
    para = find(doc, lead, label=label, startswith=True)
    base = para.runs[-1]
    r = copy.deepcopy(base._r)
    base._r.addnext(r)
    run = para.runs[-1]
    # the cloned run may inherit bold from the heading; the body must not be bold
    for rr in para.runs:
        if rr._r is r:
            rr.text = body
            rr.bold = False
            break
    FIRED.append(label)
    return para


def insert_after(doc, anchor, lead, body, *, label, startswith=False):
    src = find(doc, anchor, label=label, startswith=startswith)
    new_p = copy.deepcopy(src._p)
    src._p.addnext(new_p)
    np = Paragraph(new_p, src._parent)
    assert np.runs, f"{label}: clone has no runs"
    while len(np.runs) < 2:
        np.runs[0]._r.addnext(copy.deepcopy(np.runs[0]._r))
    np.runs[0].text = lead
    np.runs[0].bold = True
    np.runs[1].text = body
    np.runs[1].bold = False
    for r in np.runs[2:]:
        r.text = ""
    FIRED.append(label)
    return np


d = Document(SENT / "GMK_Consulting_Agreement.docx")

# ───────────────────────── counterparty name ─────────────────────────
sub(d, 'and GMK Consulting ("Consultant"), effective January 1, 2027',
    'and GMK Sports Consulting ("Consultant"), an entity controlled by Greg Kristof, effective '
    'January 1, 2027',
    label="preamble — GMK Sports Consulting")

# ───────────────────────── §1.3 align the named businesses ─────────────────────────
sub(d, "Consultant may continue his own businesses (including 6th Sense)",
    "Consultant may continue his own businesses (including Zero Gravity and 6th Sense)",
    label="§1.3 — name both businesses")

# ───────────────────────── §1.5 NCAA compliance (new) ─────────────────────────
insert_after(d, "1.4 ",
             "1.5  NCAA and recruiting compliance.  ",
             "Consultant acknowledges that the Company's business involves NCAA member "
             "institutions and their student-athletes, and agrees that in performing the services "
             "Consultant will not: (a) contact, recruit, evaluate or give any opinion on a "
             "specific prospective student-athlete who has not yet enrolled at, or signed a "
             "national letter of intent or equivalent binding commitment with, a school "
             "participating in a Company project; (b) act as, or hold himself out as, an athlete "
             "agent or representative of any student-athlete for compensation; (c) offer, promise, "
             "arrange or imply any name, image and likeness or other compensation to any "
             "prospective student-athlete as an inducement to enroll; or (d) participate in "
             "setting, pricing or negotiating any student-athlete's compensation. The services are "
             "limited to general strategic advice, industry and market context, and introductions "
             "to adults. Consultant will promptly raise with the Chief Executive Officer any "
             "request he believes may fall outside these limits, and the Company will not direct "
             "Consultant to act outside them. This Section survives termination.",
             label="§1.5 — NCAA compliance (new)", startswith=True)

# ───────────────────────── §2.2 notice period ─────────────────────────
sub(d, "terminated by either party on [30] days' written notice",
    "terminated by either party on thirty (30) days' written notice",
    label="§2.2 — 30 days")

# ───────────────────────── §3.3 tie expenses to the policy ─────────────────────────
sub(d, "business expenses on submission of receipts.",
    "business expenses on submission of receipts. Reimbursement is governed by the Company's "
    "Expense & Travel Policy then in effect, which applies by its terms to contractors and a copy "
    "of which has been provided to Consultant. Under that policy, any single non-flight, "
    "non-lodging expense or commitment over five hundred dollars ($500) requires prior written "
    "approval by email before it is incurred.",
    label="§3.3 — expenses governed by the policy")

# ───────────────────────── §3.4 Invoicing (was an empty heading) ─────────────────────────
append_body(d, "3.4",
            "  Consultant will submit an invoice to the Company on or about the first business day "
            "of each month for that month's retainer, together with any reimbursable expenses "
            "incurred in the preceding month and the supporting receipts. The Company will pay "
            "each undisputed invoice within thirty (30) days of receipt. Where the Company "
            "disputes any portion of an invoice, it will pay the undisputed portion when due and "
            "notify Consultant of the disputed portion within ten (10) business days of receipt, "
            "and the parties will resolve it in good faith. The Company has no obligation to make "
            "any payment under this Agreement until Consultant has delivered a completed IRS Form "
            "W-9. Invoices must be submitted within ninety (90) days after the end of the month to "
            "which they relate.",
            label="§3.4 — Invoicing (was empty)")

# ───────────────────────── §8 relationship carve-out ─────────────────────────
sub(d, "nor solicit Company personnel.",
    "nor solicit Company personnel. Nothing in this Section restricts Consultant from "
    "initiating, continuing or maintaining any personal or professional relationship with any "
    "person or entity, whenever and however that relationship arose, including any relationship "
    "arising through Zero Gravity, 6th Sense or any other business of Consultant permitted under "
    "Section 1.3. Consultant's obligations under Sections 6 and 7 continue to apply to Company "
    "confidential information and intellectual property in any such communication.",
    label="§8 — relationship carve-out")

# ───────────────────────── §9.1 governing law ─────────────────────────
sub(d, "Governing Law.",
    "Governing law; jurisdiction; jury waiver.",
    label="§9.1 heading")
sub(d, " Delaware. ",
    " This Agreement is governed by and construed in accordance with the laws of the State of "
    "Delaware, without regard to its conflicts of laws principles. The Court of Chancery of the "
    "State of Delaware has exclusive jurisdiction over any dispute arising out of or relating to "
    "this Agreement (or, if that court lacks subject-matter jurisdiction, the federal or state "
    "courts located in the State of Delaware). TO THE FULLEST EXTENT PERMITTED BY LAW, EACH PARTY "
    "WAIVES ANY RIGHT TO TRIAL BY JURY. ",
    label="§9.1 — governing law body")

# ───────────────────── §9.4 Indemnification / LoL (was an empty heading) ─────────────────────
append_body(d, "9.4",
            " Each party will indemnify, defend and hold harmless the other, and the other's "
            "officers, directors, employees and agents, from and against any third-party claim, "
            "and any resulting loss, liability, damage, cost and reasonable attorneys' fees, to "
            "the extent arising out of the indemnifying party's breach of this Agreement, gross "
            "negligence or willful misconduct. Consultant will further indemnify the Company "
            "against any claim arising out of Consultant's failure to pay taxes on amounts "
            "received under this Agreement, or out of any assertion that Consultant or any of "
            "Consultant's personnel is an employee of the Company. Neither party is liable to the "
            "other for indirect, incidental, special, consequential, exemplary or punitive "
            "damages, or for lost profits, however caused. Except for a party's indemnification "
            "obligations under this Section, a breach of Section 6 (Confidentiality) or Section 7 "
            "(Intellectual Property), and Consultant's obligations under Section 8 "
            "(Non-Circumvention / Non-Solicitation), each party's aggregate liability under this "
            "Agreement is limited to the total fees paid or payable to Consultant under this "
            "Agreement in the twelve (12) months preceding the event giving rise to the claim.",
            label="§9.4 — Indemnification / LoL (was empty)")

# ───────────────────────── new §§9.6 – 9.8 ─────────────────────────
anchor = "9.5 "
for lead, body, lbl in (
    ("9.6  Notices.  ",
     "All notices under this Agreement must be in writing and delivered by hand, by nationally "
     "recognized overnight courier, or by email, in each case to the address set forth on the "
     "signature page (or such other address as a party designates by notice). Notice is deemed "
     "given on delivery if by hand, one business day after deposit if by courier, and on "
     "transmission if by email provided no bounce or error notice is received.",
     "§9.6 — Notices (new)"),
    ("9.7  Severability; reformation.  ",
     "If any provision of this Agreement is held invalid or unenforceable, that provision is "
     "ineffective only to the extent of such invalidity or unenforceability and the remainder "
     "continues in full force. If any restriction in Section 8 is held unenforceable because of "
     "its duration, geographic scope or subject matter, the parties intend that the court reduce "
     "that restriction to the maximum duration, scope or subject matter that is enforceable and "
     "enforce it as so reduced.",
     "§9.7 — Severability (new)"),
    ("9.8  Authority; key person.  ",
     "Consultant represents that it is duly organized and in good standing, and that the person "
     "signing below is authorized to bind it. The Company is engaging Consultant for Greg "
     "Kristof's personal expertise, judgement and relationships; Greg Kristof will perform the "
     "services personally, and Consultant may not subcontract or substitute any other individual "
     "without the Company's prior written consent.",
     "§9.8 — Authority / key person (new)"),
):
    insert_after(d, anchor, lead, body, label=lbl, startswith=True)
    anchor = lead.strip().split()[0] + " "

# ───────────────────────── signature block ─────────────────────────
sub(d, "Title: Founder / CEO", "Title: Founder & Chief Executive Officer",
    label="signature — CEO title")
# The counterparty is an entity, so the block needs By / Name / Title rather than one name line.
# ⚠️ "\n" inside a run does NOT render as a line break in Word, so each line is its own paragraph,
# cloned from the existing one to keep the signature-block formatting.
sub(d, "CONSULTANT: _________________________", "CONSULTANT: GMK SPORTS CONSULTING",
    label="signature — consultant is the entity")
# ⚠️ Hold a reference to the consultant's paragraph rather than re-finding it by text: the
# Company's block has its own "By: ____" line earlier in the document, so a text anchor matches
# that one and the entity lines land under Cinderella Corp instead of GMK.
_cons = find(d, "GMK Consulting, Greg Kristof", label="signature — By line")
_cons.runs[0].text = "By: _________________________"
for _r in _cons.runs[1:]:
    _r.text = ""
FIRED.append("signature — By line")
for _line, _lbl in (
    ("Name: Greg Kristof", "signature — Name"),
    ("Title: _________________________", "signature — Title"),
    ("Address for notices: _______________________________", "signature — Address"),
    ("Email: _________________________", "signature — Email"),
):
    _new = copy.deepcopy(_cons._p)
    _cons._p.addnext(_new)
    _np = Paragraph(_new, _cons._parent)
    _np.runs[0].text = _line
    for _r in _np.runs[1:]:
        _r.text = ""
    FIRED.append(_lbl)
    _cons = _np


d.save(OUT / "GMK_Sports_Consulting_Agreement.docx")


# ════════════════════════════════ VERIFICATION ════════════════════════════════

print(f"{len(FIRED)} changes applied:")
for f in FIRED:
    print("  ✓", f)

t = "\n".join(p.text for p in Document(OUT / "GMK_Sports_Consulting_Agreement.docx").paragraphs)
checks = [
    # nothing unfinished left
    ("[30]", False),
    ("[Company pays automatically", False),
    ("[Standard mutual", False),
    ("GMK Consulting", False),
    ("Title: Founder / CEO", False),
    # the two empty headings are now written
    ("Consultant will submit an invoice to the Company", True),
    ("completed IRS Form W-9", True),
    ("pay each undisputed invoice within thirty (30) days", True),
    ("Each party will indemnify, defend and hold harmless the other", True),
    ("is an employee of the Company", True),
    ("limited to the total fees paid or payable to Consultant", True),
    ("indirect, incidental, special, consequential", True),
    # new and corrected
    ("GMK Sports Consulting", True),
    ("CONSULTANT: GMK SPORTS CONSULTING", True),
    ("Name: Greg Kristof", True),
]
# the four entity lines must sit between the consultant heading and its Date line,
# not under Cinderella Corp's signature block
_ps = [p.text.strip() for p in Document(OUT / "GMK_Sports_Consulting_Agreement.docx").paragraphs]
_i = _ps.index("CONSULTANT: GMK SPORTS CONSULTING")
_block = [x for x in _ps[_i:_i + 7] if x]
_want = ["CONSULTANT: GMK SPORTS CONSULTING", "By: _________________________",
         "Name: Greg Kristof", "Title: _________________________",
         "Address for notices: _______________________________",
         "Email: _________________________", "Date: ______"]
_sig_ok = _block == _want
_norman = _ps.index("Name: Norman C. de Silva")
_sig_ok = _sig_ok and _norman < _i          # Company block stays above, unpolluted
checks += [
    ("\\n", False),
    ("1.5  NCAA and recruiting compliance.", True),
    ("athlete agent or representative of any student-athlete for compensation", True),
    ("the Company will not direct Consultant to act outside them", True),
    ("whenever and however that relationship arose", True),
    ("Zero Gravity and 6th Sense", True),
    ("over five hundred dollars ($500) requires prior written approval", True),
    ("WAIVES ANY RIGHT TO TRIAL BY JURY", True),
    ("Court of Chancery of the State of Delaware", True),
    ("9.6  Notices.", True),
    ("9.7  Severability; reformation.", True),
    ("9.8  Authority; key person.", True),
    ("Greg Kristof will perform the services personally", True),
    ("Founder & Chief Executive Officer", True),
    # the equity separation must survive untouched
    ("no equity is granted here", True),
    ("$4,000 per month", True),
    ("January 1, 2027", True),
]
print("\nverification:")
bad = 0
for needle, want in checks:
    ok = (needle in t) is want
    bad += not ok
    print(f"  {'OK  ' if ok else 'FAIL'} {'has' if want else 'no ':<3} {needle[:62]!r}")

# no duplicate section numbers
import re
leads = [m.group(1) for p in Document(OUT / "GMK_Sports_Consulting_Agreement.docx").paragraphs
         if (m := re.match(r"^(\d+\.\d+)\s", p.text.strip()))]
dupes = {x for x in leads if leads.count(x) > 1}
bad += len(dupes)
print(f"  {'OK  ' if not dupes else 'FAIL'} no duplicate section numbers "
      f"({len(leads)} numbered: {', '.join(leads)})")

bad += not _sig_ok
print(f"  {'OK  ' if _sig_ok else 'FAIL'} consultant signature block is the entity form, in order\n       {_block}")

print(f"\n{'ALL CHECKS PASSED' if not bad else f'{bad} CHECK(S) FAILED'}")
sys.exit(1 if bad else 0)
