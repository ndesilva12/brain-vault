# -*- coding: utf-8 -*-
"""Ankur Jain Strategic Adviser Agreement — revised per the 2026-09-18 exchange."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = ("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c/"
       "scratchpad/Ankur Jain Strategic Adviser Agreement (REVISED).docx")

d = Document()
for s in d.sections:
    s.top_margin = s.bottom_margin = Inches(1.0)
    s.left_margin = s.right_margin = Inches(1.0)
st = d.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(10.5)
st.font.color.rgb = RGBColor(0, 0, 0)
st.paragraph_format.space_after = Pt(9)
st.paragraph_format.line_spacing = 1.06


def p(text="", *, lead=None, indent=0.0, center=False, italic=False, bold=False,
      before=0, after=9, size=10.5, justify=True):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    if indent: pf.left_indent = Inches(indent)
    if center: par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif justify: par.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if lead:
        r = par.add_run(lead); r.bold = True; r.font.size = Pt(size)
    if text:
        r = par.add_run(text); r.italic = italic; r.bold = bold; r.font.size = Pt(size)
    return par


def head(t, size=11.5, before=15, after=7):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(before), Pt(after)
    r = par.add_run(t); r.bold = True; r.font.size = Pt(size)


def sig(label, extra=None):
    par = d.add_paragraph(); par.paragraph_format.space_before = Pt(15)
    par.paragraph_format.space_after = Pt(2); par.add_run("_" * 44)
    if label:
        q = d.add_paragraph(); q.paragraph_format.space_after = Pt(0); q.add_run(label)
    for e in (extra or []):
        q = d.add_paragraph(); q.paragraph_format.space_after = Pt(0); q.add_run(e)


p("DRAFT — FOR DISCUSSION ONLY — NOT LEGAL ADVICE", bold=True, center=True, size=9,
  after=12, justify=False)
par = d.add_paragraph(); par.alignment = WD_ALIGN_PARAGRAPH.CENTER
par.paragraph_format.space_after = Pt(14)
r = par.add_run("STRATEGIC ADVISER AGREEMENT"); r.bold = True; r.font.size = Pt(13)

p("This Strategic Adviser Agreement (this “Agreement”) is entered into as of [____], 2026 "
  "(the “Effective Date”) by and between Cinderella Corp., a Delaware corporation (the "
  "“Company”), and Ankur Jain (“Adviser”).")

head("0.  CONDITION PRECEDENT — OUTSIDE BUSINESS ACTIVITY (OBA) APPROVAL")
p("Notwithstanding anything else, no title, services, fundraising participation, investor "
  "meetings, use of Adviser’s name, distributor outreach, or board activity under this "
  "Agreement is authorized or effective until Adviser has obtained and delivered written "
  "outside-business-activity approval from Tabor Asset Management (“OBA Approval”).",
  lead="0.1  Tabor approval.  ")
p("OBA Approval must remain in effect. If it is withdrawn, limited, or conditioned, the affected "
  "activities are suspended until restored; the Company may suspend or terminate under Section "
  "10. Adviser will operate at all times within the scope of his OBA Approval.",
  lead="0.2  Continuing condition.  ")

head("1.  SERVICES AND ROLE")
p("Adviser serves as a non-exclusive Strategic Adviser, providing: (a) advice on financial "
  "structure, valuation, and capital formation; (b) strategic review and approval of the "
  "Company’s financial materials as set forth in Sections 1.2 and 1.3; (c) participation in "
  "PE/investor and distributor meetings (subject to OBA Approval and Section 1.5); and "
  "(d) introductions across his network.", lead="1.1  Role.  ")

p("The Company will not distribute externally any financial materials — including models, "
  "investor financial decks, the assumptions underlying them, and the presentation of financial "
  "information — without Adviser’s strategic review and approval, not to be unreasonably "
  "withheld, conditioned or delayed.",
  lead="1.2  Financial materials — approval.  ")

p("Adviser’s strategic review and approval under Section 1.2 extends to the Company’s "
  "valuation analysis, proposed financing structure and proposed investor terms as presented in "
  "materials furnished to prospective investors, and the Company will consult Adviser in good "
  "faith and in advance on each of them before going to market on any financing. Approval under "
  "Section 1.2 and this Section is deemed given where Adviser has participated in the preparation "
  "of the relevant materials, or has been furnished with them and has not objected in writing "
  "within five (5) business days. Nothing in this Section is intended to alter the allocation of "
  "authority under the Delaware General Corporation Law, the Company’s Certificate of "
  "Incorporation or its Bylaws, under which the issuance of securities, the consideration for "
  "which they are issued, and the acceptance of any subscription remain matters for determination "
  "by the Board.", lead="1.3  Valuation, financing structure and investor terms.  ")

p("The Company will retain, at its own expense, a qualified certified public accounting firm to "
  "review the accounting, financial statements, and underlying financial accuracy of the "
  "Company’s investor materials. The firm will be selected by Adviser, within an annual "
  "budget agreed by the Company and Adviser. "
  "For the avoidance of doubt, Adviser does not act as, and has no duties of, a chief financial "
  "officer, controller, certified public accountant or accounting professional; Adviser does not "
  "prepare, audit, review or certify the Company’s accounting records, financial statements "
  "or the accounting accuracy of any financial model or investor material, and has no liability "
  "for any of them. Responsibility for the accounting accuracy of the Company’s financial "
  "statements and investor materials rests with the Company and that firm.",
  lead="1.4  Accounting firm; no accounting role.  ")

p("Adviser is not an officer, director, employee, or agent, has no authority to bind the Company, "
  "will not execute or sign agreements on its behalf, and is not engaged as a broker, finder, or "
  "placement agent; no compensation under this Agreement is contingent on the sale of securities "
  "or on the size or closing of any financing.", lead="1.5  Limits; no broker.  ")
p("Adviser may continue Tabor and his other activities, subject to OBA Approval and Sections 6–8.",
  lead="1.6  Non-exclusive.  ")

head("2.  COMPENSATION — EQUITY ONLY; NO CASH")
p("The Company will grant Adviser restricted Class A Common Stock equal to four percent (4%) of "
  "the Company (the “Role Shares”), measured per Section 2.5, which shall be fully "
  "vested as of the Effective Date and not subject to any repurchase option for unvested shares. "
  "The Role Shares compensate the advisory role and are not contingent on any financing.",
  lead="2.1  Role Equity — 4%, fully vested.  ")

p("The Company will additionally grant restricted Class A Common Stock upon achievement, during "
  "OBA-approved activity, of the milestones below with respect to a Qualifying Platform. A "
  "“Qualifying Platform” means Netflix, Apple, Amazon Prime Video, HBO/Max (Warner "
  "Bros. Discovery), Disney/Hulu/ESPN (The Walt Disney Company), Paramount, "
  "NBCUniversal/Peacock, or another comparable "
  "major streaming or distribution platform approved by the Board, in each case where the "
  "relationship is directly attributable to Adviser’s introduction.",
  lead="2.2  Distribution Milestone Equity — up to 5%.  ")

p("(a)  Platform tiers. The milestone equity available with respect to each Qualifying "
  "Platform, by tranche, is set forth below. The “Total” column is the maximum earnable with "
  "respect to that platform; the tranche columns correspond to clauses (i), (ii) and (iii) of "
  "Section 2.2(b).", indent=0.3, after=5)

tbl = d.add_table(rows=6, cols=5); tbl.style = "Table Grid"
rows = [("Qualifying Platform", "Meeting (25%)", "Term sheet (25%)", "Definitive (50%)", "Total"),
        ("Netflix", "1.25%", "1.25%", "2.50%", "5.00%"),
        ("Apple", "0.875%", "0.875%", "1.75%", "3.50%"),
        ("Amazon Prime Video", "0.875%", "0.875%", "1.75%", "3.50%"),
        ("Disney / Hulu / ESPN", "0.875%", "0.875%", "1.75%", "3.50%"),
        ("All other Qualifying Platforms", "0.25%", "0.25%", "0.50%", "1.00%")]
for i, row in enumerate(rows):
    for j, val in enumerate(row):
        c = tbl.cell(i, j); c.text = ""
        rr = c.paragraphs[0].add_run(val)
        rr.bold = (i == 0); rr.font.size = Pt(9.5); rr.font.name = "Calibri"

p("", after=4)
p("(b)  Milestones. For each Qualifying Platform: (i) the first tranche vests upon a "
  "senior-level meeting with that platform, directly resulting from Adviser’s introduction; "
  "(ii) the second tranche vests upon a qualifying term sheet from that platform; and "
  "(iii) the third tranche vests upon a definitive rights agreement with that platform together "
  "with receipt by the Company of the initial guaranteed payment.", indent=0.3)

p("(c)  Aggregate cap. Milestone equity may be earned with respect to more than one Qualifying "
  "Platform, provided that aggregate milestone equity granted under this Section 2.2 shall not "
  "exceed five percent (5%) of the Company.", indent=0.3)

p("(d)  Attribution. Adviser shall give the Company written notice identifying each introduction "
  "at the time it is made. A milestone is attributable to Adviser only where such notice was "
  "given, or where the Company otherwise confirms attribution in writing.", indent=0.3)

p("If Adviser introduces or materially advances a relationship with a Qualifying Platform during "
  "the term, Adviser remains eligible for the corresponding milestone equity if the applicable "
  "term sheet or definitive agreement is completed within twelve (12) months after termination of "
  "this Agreement, provided Adviser was not terminated for material breach or loss of OBA "
  "Approval.", lead="2.3  Tail — 12 months.  ")

p("Adviser’s equity is measured on the fully-diluted capitalization immediately after "
  "completion of the Seed Round (the $1,500,000 / 15% raise), so the Seed Round does not dilute "
  "Adviser. After the Seed Round is complete, Adviser’s shares are subject to ordinary, "
  "pro-rata dilution on the same basis as the Founder on all subsequent issuances — no further "
  "anti-dilution protection. This post-Seed measurement is specific to Adviser and is not a "
  "precedent for any other grant.", lead="2.4  Anti-dilution — Seed Round only.  ")
p("All shares are Class A Common (1 vote per share); Adviser does not receive Class B or any "
  "super-voting stock, which is held solely by Norman C. de Silva.", lead="2.5  Class A only.  ")
p("Issued as restricted stock under the Company’s Restricted Stock Purchase Agreement and "
  "subject to the Stockholders’ Agreement; Adviser is advised to consider an 83(b) election "
  "within thirty (30) days of each grant.", lead="2.6  Mechanics; tax.  ")
p("No cash fees, salary, or bonus are payable.", lead="2.7  No cash.  ")

head("3.  GOVERNANCE AND INFORMATION")
p("Adviser may attend all meetings of the Board in a non-voting observer capacity and shall "
  "receive copies of all materials provided to directors, at the same time they are provided. The "
  "Company may exclude the observer from any portion of a meeting, and withhold any material, "
  "where the Board determines in good faith that doing so is necessary to preserve "
  "attorney-client privilege, to address an actual or potential conflict of interest involving "
  "Adviser, or to protect highly confidential information.", lead="3.1  Board observer.  ")
p("Upon the appointment or election of any additional director — that is, at such time as any "
  "person other than the Founder becomes a director of the Company — Adviser shall automatically "
  "and concurrently be appointed to the Board as a director, without further action or discretion "
  "on the part of the Company or the Founder. Adviser may decline the seat and elect to continue "
  "as an observer under Section 3.1, in which case the right to take the seat continues and may "
  "be exercised at any later time on written notice.",
  lead="3.2  Automatic Board seat on Board expansion.  ")
p("Annual and quarterly financial statements, the annual budget, and material financing updates.",
  lead="3.3  Information rights.  ")
p("Reasonable, pre-approved expenses reimbursed on receipts, per Company expense policy.",
  lead="3.4  Expense reimbursement.  ")

head("4.  INDEMNIFICATION AND INSURANCE")
p("The Company will indemnify, defend and hold harmless Adviser, and advance his reasonable "
  "expenses, to the fullest extent permitted by Delaware law, in respect of his authorized "
  "services, his Board observer or director role, and his role as Investor Representative, "
  "including any claim brought by an investor in respect of good-faith actions taken as Investor "
  "Representative.", lead="4.1  Indemnification.  ")
p("No indemnity is available for bad faith, willful misconduct, gross negligence, or breach of "
  "this Agreement, and advancement is conditioned on an undertaking to repay amounts advanced if "
  "it is ultimately determined that Adviser was not entitled to indemnification.",
  lead="4.2  Exclusions.  ")
p("The Company will use commercially reasonable efforts to include Adviser under its "
  "directors’ and officers’ liability insurance expressly in his capacities as Board "
  "observer or director and as Investor Representative.", lead="4.3  D&O insurance.  ")

head("5.  NAME, IMAGE, AND LIKENESS")
p("The Company may use Adviser’s name, image, and biography only with his prior approval and "
  "within OBA limits; approvals for a given use, once given, extend to substantially similar uses.")

head("6.  CONFIDENTIALITY")
p("Adviser will hold all non-public Company information in confidence and use it only for the "
  "Company’s benefit. This obligation does not apply to information that is or becomes "
  "public other than through Adviser’s breach, or that Adviser is required to disclose by "
  "law, provided he gives the Company prompt notice where lawful to do so.")

head("7.  INTELLECTUAL PROPERTY")
p("Work product Adviser creates for or delivers to the Company is assigned to the Company. "
  "Adviser’s pre-existing and independent business IP, including Tabor’s, remains his.")

head("8.  NON-CIRCUMVENTION")
p("A “Restricted Project” means any business, venture, production or project that "
  "(i) pairs one or more celebrities, public figures, athletes or prominent alumni with one or "
  "more collegiate athletic programs for the purpose of financing, capitalizing or materially "
  "supporting that program and producing, licensing or distributing documentary or similar "
  "audiovisual content concerning it, or (ii) is otherwise substantially similar to the "
  "Company’s Making Cinderella format.", lead="8.1  Restricted Project.  ")
p("During the term and for twelve (12) months thereafter, Adviser will not, using the "
  "Company’s confidential information or an opportunity originated by the Company, "
  "circumvent the Company with respect to any Restricted Project, nor solicit Company personnel.",
  lead="8.2  Restriction.  ")
p("Nothing in this Agreement restricts Adviser from initiating, continuing or maintaining any "
  "relationship with any person or entity, whenever and however that relationship arose. For the "
  "avoidance of doubt, Section 8.2 does not apply to: (a) people and organizations Adviser knew "
  "or had relationships with prior to his involvement with the Company; (b) Tabor-related "
  "activity; (c) relationships independently developed outside the Company; (d) Adviser’s "
  "existing investments and business activities; or (e) parties who approach Adviser "
  "independently without use of the Company’s confidential information.",
  lead="8.3  Relationships expressly unrestricted.  ")

head("9.  INDEPENDENT CONTRACTOR")
p("Independent contractor; responsible for his own taxes; no employee benefits; no partnership or "
  "employment relationship created.")

head("10.  TERM AND TERMINATION")
p("From the Effective Date until terminated.", lead="10.1  Term.  ")
p("Either party may terminate on thirty (30) days’ notice, or immediately for material "
  "breach or loss of OBA Approval. On termination: the Role Shares, being fully vested, are "
  "retained; unearned milestone equity is forfeited, subject to Section 2.3; and all shares "
  "remain subject to the Stockholders’ Agreement. Sections 4 and 6–8 survive.",
  lead="10.2  Termination.  ")

head("11.  GENERAL")
p("Delaware law governs, without regard to conflicts of law principles; the Court of Chancery of "
  "the State of Delaware has exclusive jurisdiction. This Agreement, together with the Restricted "
  "Stock Purchase Agreement and the Stockholders’ Agreement, constitutes the entire "
  "agreement as to its subject matter. Amendments in writing signed by both parties. Adviser may "
  "not assign. Counterparts and electronic signature permitted. If any provision is held "
  "unenforceable, the remainder continues in full force.")

p("[Remainder of page intentionally left blank]", center=True, italic=True, before=14, after=14,
  justify=False)
d.add_page_break()
p("IN WITNESS WHEREOF, the parties have executed this Strategic Adviser Agreement as of the date "
  "first above written.", after=16)
p("COMPANY:", bold=True, after=0, justify=False)
p("CINDERELLA CORP.", before=8, after=0, justify=False)
sig("By:", ["Name:  Norman C. de Silva", "Title:  Founder & Chief Executive Officer",
            "Date:  ______________"])
p("ADVISER:", bold=True, before=20, after=0, justify=False)
sig("Ankur Jain", ["Date:  ______________",
                   "Address for notices:  ______________________________",
                   "Email:  ______________________"])

d.save(OUT)
print("wrote", OUT)
