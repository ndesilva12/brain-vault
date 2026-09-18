# -*- coding: utf-8 -*-
"""Expense & Travel Policy — Ankur's draft with four structural fixes."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = ("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c/"
       "scratchpad/Cinderella Corp - Expense and Travel Policy (REVISED).docx")
d = Document()
for s in d.sections:
    s.top_margin = s.bottom_margin = Inches(1.0); s.left_margin = s.right_margin = Inches(1.0)
st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
st.font.color.rgb = RGBColor(0,0,0); st.paragraph_format.space_after = Pt(8)
st.paragraph_format.line_spacing = 1.06

def p(t="", *, lead=None, indent=0.0, bold=False, italic=False, center=False,
      before=0, after=8, size=10.5):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    if indent: pf.left_indent = Inches(indent)
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
    if lead:
        r = par.add_run(lead); r.bold = True; r.font.size = Pt(size)
    if t:
        r = par.add_run(t); r.bold = bold; r.italic = italic; r.font.size = Pt(size)

def h(t, before=14, after=6):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    r = par.add_run(t); r.bold = True; r.font.size = Pt(11.5)

p("EXPENSE & TRAVEL POLICY", bold=True, center=True, size=13, after=3)
p("Cinderella Corp., a Delaware corporation", italic=True, center=True, size=10, after=14)

h("1.  Purpose and Scope", before=4)
p("This policy applies to all founders, employees, contractors, advisers and other persons "
  "seeking payment or reimbursement from Cinderella Corp. (the “Company”). Company-paid expenses "
  "must be reasonable, business-related, properly documented and consistent with this policy.")
p("This policy does not apply to any special purpose vehicle, project entity or other entity in "
  "which the Company holds an interest but which has its own governing agreement and other "
  "equity holders. Expenditure by any such entity is governed by that entity’s own operating "
  "agreement and budget.", lead="1.1  Entities not covered.  ")
p("This policy governs expenses and reimbursements. It does not apply to compensation, including "
  "salary, wages, bonuses, equity compensation or contractor fees, which are governed by the "
  "applicable individual agreements and by the Board of Directors.",
  lead="1.2  Compensation excluded.  ")
p("“Investor Representative” means the person then serving in that capacity under the Side Letter "
  "Agreement dated [____], 2026. Approvals required of the Investor Representative under this "
  "policy may be given by email.", lead="1.3  Definitions.  ")
p("“Approved Budget” means the Company’s then-current operating budget as approved by the Board "
  "of Directors. An expenditure is “within the Approved Budget” if it falls within a line item of "
  "the Approved Budget and does not cause that line item to be exceeded.", indent=0.0)

h("2.  Air Travel")
p("Until one hundred percent (100%) of Seed investor capital has been returned to investors, all "
  "Company-paid flights must be booked in coach/economy class.", indent=0.25)
p("Following the earlier of (a) return of 100% of Seed investor capital, (b) the closing of a "
  "Series A or later preferred financing, or (c) the closing of a definitive distribution "
  "agreement with a major streaming or distribution platform:", indent=0.25)
for t in ["scheduled flight time of 4 hours or less: coach/economy;",
          "more than 4 hours and up to 7 hours: premium economy;",
          "more than 7 hours: business class."]:
    p("•  " + t, indent=0.55, after=3)
p("Travelers may use personal cash, points or miles to upgrade above the permitted class at no "
  "cost to the Company.", indent=0.25, before=6)
p("Any exception to the permitted cabin class requires the prior written approval of the Investor "
  "Representative.", indent=0.25)

h("3.  Lodging")
p("Maximum lodging rate: $300 per night before taxes, except that in New York, San Francisco, Los "
  "Angeles, Boston, Chicago and Washington, D.C. the maximum is $450 per night before taxes. "
  "Where the U.S. General Services Administration publishes a higher per-diem lodging rate for "
  "the locality and dates of travel, that rate applies instead.", indent=0.25)
p("Any lodging above the applicable limit requires the prior written approval of the Investor "
  "Representative.", indent=0.25)
p("Personal extensions, room upgrades and other incremental personal costs are not reimbursable.",
  indent=0.25)

h("4.  Meals")
p("Breakfast up to $20, lunch up to $30, and dinner up to $50, with a maximum daily meal "
  "allowance of $100 per traveler.", indent=0.25)
p("The daily maximum does not apply to a documented business-development meal with one or more "
  "third parties, provided the expense report identifies the attendees and the business purpose. "
  "Such meals remain subject to Section 5.", indent=0.25)
p("If a meal is provided by a conference, hotel, sponsor, school, investor or other third party, "
  "the corresponding meal allowance is not reimbursable.", indent=0.25)
p("Alcohol and entertainment are not reimbursable unless they are part of a bona fide "
  "business-development expense and otherwise comply with this policy.", indent=0.25)

h("5.  Other Business Expenses")
p("Any single non-flight, non-lodging expense or commitment over five thousand dollars ($5,000) "
  "that is NOT within the Approved Budget requires the prior written approval of the Investor "
  "Representative. Expenditures within the Approved Budget do not require approval under this "
  "Section, regardless of amount.", indent=0.25)
p("A series of related expenditures to a single vendor within any ninety (90) day period is "
  "treated as a single expenditure for purposes of this Section.", indent=0.25)
p("This Section applies to entertainment, consultants, vendors, subscriptions, equipment, event "
  "costs, gifts, marketing and other business-development expenditures. It does not apply to "
  "fees of the Company’s outside legal counsel, accountants or other professional advisers "
  "engaged with Board approval, or to insurance premiums, taxes, statutory filing fees or other "
  "amounts the Company is legally obligated to pay.", indent=0.25)
p("Reasonable ground transportation, parking, tolls and similar travel expenses are reimbursable "
  "when incurred for Company business.", indent=0.25)

h("6.  Documentation and Reimbursement")
for t in ["Receipts or other reasonable supporting documentation are required for reimbursement.",
          "Expense reports should identify the business purpose and, for business-development "
          "meals or entertainment, the attendees.",
          "Reimbursement requests should be submitted within 30 days after the expense is "
          "incurred whenever practicable.",
          "Personal expenses are not reimbursable."]:
    p("•  " + t, indent=0.25, after=4)

h("7.  Exceptions and Amendments")
p("No person may approve his or her own exception to this policy.", indent=0.25)
p("Any exception requiring approval under this policy must be approved in advance by the Investor "
  "Representative. Approval or rejection shall be given within three (3) business days of a "
  "written request; a request not responded to within that period is deemed approved.",
  indent=0.25)
p("Until the earlier of the events described in Section 2, any material amendment to this policy "
  "requires the written approval of both the Chief Executive Officer and the Investor "
  "Representative.", indent=0.25)
p("This policy terminates automatically upon the earlier of the events described in Section 2, "
  "after which Company expenditure is governed by the Board of Directors.", indent=0.25)

p("Adopted:  ____________________", before=18)
d.save(OUT); print("wrote", OUT)
