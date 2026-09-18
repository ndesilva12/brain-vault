# -*- coding: utf-8 -*-
"""Side Letter Agreement (Revenue Share) — FINAL v2.
Loeb's 2026-09-18 final text, with the provisions Ankur's email asks for inserted.
Every insertion is marked NEW in the vault note; the surrounding text is Loeb's verbatim."""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = ("/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c/scratchpad/")
OUT = BASE + "Cinderella Corp - Side Letter Agreement Revenue Share FINAL v2.docx"

d = Document()
for s in d.sections:
    s.top_margin = s.bottom_margin = Inches(1.0)
    s.left_margin = s.right_margin = Inches(1.0)
st = d.styles["Normal"]
st.font.name = "Times New Roman"; st.font.size = Pt(11)
st.font.color.rgb = RGBColor(0, 0, 0)
st.paragraph_format.space_after = Pt(10)
st.paragraph_format.line_spacing = 1.08

N = [0]
def sec(title, body="", lead_only=False):
    N[0] += 1
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_before, pf.space_after = Pt(11), Pt(9)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(f"{N[0]}.  {title}"); r.bold = True
    if body:
        r2 = par.add_run("  " + body)
    return N[0]

def sub(text, indent=0.35):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.left_indent = Inches(indent); pf.space_after = Pt(9)
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    par.add_run(text)

def plain(text, **kw):
    par = d.add_paragraph(); pf = par.paragraph_format
    pf.space_after = Pt(kw.get("after", 10))
    pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = par.add_run(text); r.italic = kw.get("italic", False); r.bold = kw.get("bold", False)
    if kw.get("size"): r.font.size = Pt(kw["size"])
    if kw.get("center"): pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return par

def sig(label, extra=None):
    par = d.add_paragraph(); par.paragraph_format.space_before = Pt(16)
    par.paragraph_format.space_after = Pt(2); par.add_run("_" * 42)
    if label:
        q = d.add_paragraph(); q.paragraph_format.space_after = Pt(0); q.add_run(label)
    for e in (extra or []):
        q = d.add_paragraph(); q.paragraph_format.space_after = Pt(0); q.add_run(e)

plain("SIDE LETTER AGREEMENT", bold=True, center=True, size=13, after=14)

plain("This Side Letter Agreement (this “Agreement”) is made and entered into as of September "
      "__, 2026, by and among Cinderella Corp, a Delaware corporation (the “Company”) and the "
      "investors listed on the signature pages herein (each an “Investor” and collectively the "
      "“Investors”).")
plain("WHEREAS, concurrently with the execution of this Agreement, the Company and each Investor "
      "are entering into subscription agreements, dated as of the date hereof (the “Subscription "
      "Agreements”);")
plain("WHEREAS, as a condition to the Investors entry into the Subscription Agreements and "
      "purchase of Class A Common Stock, par value $0.001, of the Company (the “Shares”), and in "
      "lieu of certain other rights, privileges, and preferences, the Investors shall receive "
      "certain preferential payments based on the gross revenue of the Company, in relation to "
      "the holder of Class B Common Stock, par value $0.001, of the Company (the “Class B "
      "Stockholder”); and")
plain("WHEREAS, the parties herein wish to enter into this Agreement with respect to the "
      "preferential payments to confirm certain understandings.")
plain("NOW, THEREFORE, for good and valuable consideration, the parties agree as follows:")

# 1 — unchanged save the cross-reference to Termination (now Section 8)
sec("Acknowledgment and Agreement of Preferential Payments.",
    "Until this Agreement terminates in accordance with Section 8, the Investors shall be "
    "entitled to the below rights (collectively, the “Preferential Payments”) as follows:")
sub("(a)  first, fifty percent (50%) of all Gross Revenue received by the Company shall be paid "
    "to the Investors on a pro rata basis until the Investors have received aggregate "
    "Preferential Payments equal to one hundred percent (100%) of their respective Investment "
    "Amounts; and")
sub("(b)  second and finally, ten percent (10%) of all Gross Revenue received by the Company "
    "shall be paid to the Investors on a pro rata basis until the Investors have received "
    "aggregate Preferential Payments equal to their respective Preferred Return.")
sub("(c)  Where Gross Revenue in a single Payment Period causes the threshold set forth in "
    "Section 1(a) to be met, the portion of such Gross Revenue required to reach that threshold "
    "shall be applied at the rate set forth in Section 1(a) and the remainder of such Payment "
    "Period’s Gross Revenue shall be applied at the rate set forth in Section 1(b).")
sub("(d)  The Preferential Payments are in addition to, and shall not be credited or offset "
    "against, any dividend, distribution or other amount payable to an Investor in respect of "
    "such Investor’s Shares. Each Investor’s equity interest in the Company is unaffected by this "
    "Agreement, and this Agreement confers no voting, governance, management or ownership rights.")

sec("Definitions.", "As used in this Agreement:")
for t in [
 "“Gross Revenue” means all cash actually received by the Company from its business operations "
 "during a Payment Period, determined on a cash basis, including distributions and dividends "
 "received by the Company from any special purpose vehicle or other subsidiary or portfolio "
 "entity; management fees, franchise fees and administrative or service fees; sponsorship, "
 "marketing and brand-partnership revenue; content, media, documentary, live-event and "
 "distribution license fees; and format-licensing, merchandising and other intellectual-property "
 "royalties. Gross Revenue expressly excludes: (i) proceeds of any equity or debt financing, "
 "including the sale of the Shares and any subsequent capital raise, loan, note or credit "
 "facility; (ii) capital contributions to the Company; (iii) amounts received by the Company as "
 "agent, custodian or pass-through for the account of a third party, including amounts collected "
 "on behalf of any special purpose vehicle, institution, athlete or talent, that the Company is "
 "contractually obligated to remit, in each case to the extent so remitted; (iv) sales, use, "
 "excise, withholding and similar taxes collected for remittance to a governmental authority; "
 "(v) refunds, rebates, credits and chargebacks actually paid or credited to a payor, and amounts "
 "invoiced but not collected; (vi) proceeds from the sale or disposition of capital assets "
 "outside the ordinary course of business; (vii) insurance and litigation proceeds, other than "
 "business-interruption proceeds compensating for lost operating revenue; (viii) proceeds "
 "received in or in connection with a Liquidation Event; and (ix) interest income and other "
 "non-operating income.",
 "“Investment Amount” of an Investor means the amount of money paid by such Investor in exchange "
 "for such Investor’s receipt of its portion of the Shares.",
 "“Liquidation Event” means (a) the consummation of a share exchange, merger or consolidation of "
 "the Company with or into another entity or any other company reorganization, if, as a result of "
 "such share exchange, merger, consolidation or reorganization, more than 50% of the combined "
 "voting power of the continuing or surviving entity’s securities outstanding immediately after "
 "such share exchange, merger, consolidation or other reorganization is owned by persons who were "
 "not stockholders of the Company immediately prior to such merger, consolidation or other "
 "reorganization, (b) the sale of capital stock of the Company by stockholders of the Company "
 "(other than in a Public Offering) in a single transaction or series of related transactions if, "
 "as a result of such sale, more than 50% of the combined voting power of the Company’s capital "
 "stock outstanding immediately after such sale is owned by persons who were not stockholders of "
 "the Company immediately prior to such sale or (c) any sale, transfer or other disposition of "
 "all or substantially all the assets of the Company and its consolidated subsidiaries to an "
 "entity (other than a wholly owned subsidiary of the Company) of which more than 50% of the "
 "combined voting power of its outstanding securities is owned by persons who are not "
 "stockholders of the Company at the effective time of such sale, transfer or disposition.",
 "“Payment Period” means each calendar quarter, or portion thereof, during the term of this "
 "Agreement.",
 "“Preferred Return” means, with respect to any such Investor, an amount equal to the product of "
 "(x) two (2) and (y) the Investment Amount for such Investor. The Preferred Return is an "
 "aggregate amount. All Preferential Payments received by an Investor, whether pursuant to "
 "Section 1(a) or Section 1(b), shall count toward, and reduce the amount remaining payable to "
 "reach, such Investor’s Preferred Return, and in no event shall aggregate Preferential Payments "
 "to an Investor exceed such Investor’s Preferred Return.",
 # NEW definitions supporting Sections 5-7
 "“Investor Representative” means Ankur Jain, or such other person as may be designated from time "
 "to time by Investors holding a majority of the Shares then subject to this Agreement, in each "
 "case acting in the capacity described in Section 5.",
 "“Undeployed Capital” means, as of any date of determination, the Company’s unrestricted cash "
 "and cash equivalents, less (i) amounts contractually committed under agreements executed by the "
 "Company and then in effect, (ii) accrued and unpaid liabilities and accrued compensation, "
 "(iii) amounts reasonably reserved by the Board of Directors for liabilities and obligations "
 "reasonably expected to become due within the following one hundred eighty (180) days, and "
 "(iv) the Minimum Reserve. Undeployed Capital shall not include any amount the return of which "
 "would be impermissible under Section 6(c).",
 "“Minimum Reserve” means the greater of (x) two hundred fifty thousand dollars ($250,000) and "
 "(y) an amount equal to six (6) months of the Company’s budgeted operating expenses under the "
 "then-current operating budget approved by the Board of Directors.",
]:
    sub(t, indent=0.0)

sec("Payment; Reporting; Audit.")
sub("(a)  The Company shall pay amounts due under Section 1 within forty-five (45) days after the "
    "end of each Payment Period.")
sub("(b)  With each payment, the Company shall deliver a statement showing, for the Payment "
    "Period: Gross Revenue and its computation, the applicable rate, the amount paid, and "
    "cumulative Preferential Payments to date against the thresholds set forth in Sections 1(a) "
    "and 1(b).")
sub("(c)  The Company shall maintain books and records sufficient to verify Gross Revenue for "
    "three (3) years following each Payment Period. Once per calendar year, on thirty (30) days’ "
    "prior written notice, Investors holding a majority of the Shares then subject to this "
    "Agreement, or the Investor Representative on their behalf, may cause an independent "
    "certified public accountant to examine such records solely to verify the computation of "
    "Gross Revenue. The examining party shall bear the cost of such examination, except that if "
    "the examination discloses an underpayment exceeding five percent (5%) for the period "
    "examined, the Company shall bear the reasonable cost of the examination and pay the shortfall "
    "within thirty (30) days.")
sub("(d)  The Company shall not structure transactions with the principal purpose of diverting, "
    "deferring or re-characterizing Gross Revenue so as to avoid or reduce payments under this "
    "Agreement. Revenue arising from transactions with affiliates of the Company shall be included "
    "in Gross Revenue at arm’s-length fair value.")
sub("(e)  Deferral. The Company may defer any payment otherwise due under Section 1 to the extent "
    "the Board of Directors determines in good faith that making such payment would (i) leave the "
    "Company with unrestricted cash reserves of less than the Minimum Reserve, (ii) violate or "
    "breach any credit agreement, loan agreement, or other financing arrangement of the Company, "
    "(iii) violate the Board of Directors’ fiduciary duties to the Company, or (iv) otherwise "
    "violate applicable law. Any amount so deferred shall accrue and shall be paid promptly at "
    "such time as payment would no longer violate clauses (i) – (iv) above.")

sec("Liquidation Event.",
    "Upon the closing of a Liquidation Event, the Company (or its successor) shall pay to the "
    "Investors, at closing and on a pro rata basis, an amount equal to the excess of (a) the "
    "aggregate Preferred Return of all Investors over (b) aggregate Preferential Payments made "
    "through the closing date. Upon such payment, this Agreement shall terminate. For the "
    "avoidance of doubt, such payment is in addition to the consideration payable to the Investors "
    "in respect of their Shares.")

# ─────────── NEW SECTION 5 — Investor Representative (Ankur item 1) ───────────
sec("Investor Representative.")
sub("(a)  Appointment. Ankur Jain is hereby appointed as the Investor Representative. The Investor "
    "Representative is authorized to give and receive notices, consents, waivers, elections and "
    "directions under this Agreement on behalf of the Investors, and any such action taken by the "
    "Investor Representative shall bind all Investors. The Company shall be entitled to rely "
    "conclusively on any notice, consent, waiver, election or direction given by the Investor "
    "Representative without further inquiry, provided that the Investor Representative may not "
    "take any action that requires the consent of an individual Investor under Section 10.")
sub("(b)  Replacement. Investors holding a majority of the Shares then subject to this Agreement "
    "may replace the Investor Representative at any time upon written notice to the Company. The "
    "Investor Representative may resign upon written notice to the Company and the Investors.")
sub("(c)  Indemnification. The Company shall indemnify, defend and hold harmless the Investor "
    "Representative, and shall advance his reasonable attorneys’ fees and expenses, to the fullest "
    "extent permitted by applicable law, in respect of any claim, demand, action or proceeding "
    "arising out of or relating to his good-faith performance of the role of Investor "
    "Representative, including any claim brought by an Investor. No indemnification or advancement "
    "is available in respect of conduct constituting bad faith, willful misconduct, gross "
    "negligence, or a knowing and material breach of this Agreement, and advancement is "
    "conditioned upon delivery of an undertaking to repay amounts advanced if it is ultimately "
    "determined that the Investor Representative was not entitled to indemnification. This Section "
    "5(c) survives termination of this Agreement.")
sub("(d)  Insurance. The Company represents that, as of the date hereof, it does not maintain "
    "directors’ and officers’ liability insurance. The Company shall use commercially reasonable "
    "efforts to obtain such insurance within ninety (90) days following the date hereof and, once "
    "obtained, to name the Investor Representative as an insured person in his capacities as "
    "Investor Representative and as Board observer, and to provide the Investor Representative "
    "with the policy’s coverage limits and material terms upon request.")

# ─────────── NEW SECTION 6 — Return of Undeployed Capital (Ankur item 2) ───────────
sec("Return of Undeployed Capital.")
sub("(a)  Right to require return. At any time, and without regard to any anniversary of the date "
    "hereof or to the Company’s achievement of any operating milestone, the Investor "
    "Representative, acting upon the written direction of Investors holding a majority of the "
    "Shares then subject to this Agreement, may deliver written notice to the Company requiring "
    "the Company to return Undeployed Capital to the Investors on a pro rata basis in proportion "
    "to their respective Investment Amounts.")
sub("(b)  Mechanics. The Company shall pay the amount so required within sixty (60) days "
    "following its receipt of such notice, together with a statement showing the Company’s "
    "calculation of Undeployed Capital as of the notice date and as of the payment date, and the "
    "amount returned shall be the lesser of the two. The Company shall not, between the notice "
    "date and the payment date, commit or expend cash outside the ordinary course of business for "
    "the principal purpose of reducing Undeployed Capital.")
sub("(c)  Limitations. No return shall be made to the extent it would (i) render the Company "
    "unable to pay its debts as they become due in the ordinary course of business, (ii) be "
    "impermissible under Section 160 or Section 244 of the Delaware General Corporation Law or "
    "any other applicable law, (iii) violate or breach any credit agreement, loan agreement or "
    "other financing arrangement of the Company, or (iv) violate the Board of Directors’ fiduciary "
    "duties. Any amount not returned by reason of this Section 6(c) shall be returned promptly "
    "once the impediment no longer applies.")
sub("(d)  Effect. A return of capital under this Section 6 is a return of capital only. It reduces "
    "each Investor’s Investment Amount dollar-for-dollar, with such Investor’s Preferred Return "
    "recomputed accordingly, and does not cancel, reduce or otherwise affect any Investor’s Shares "
    "or percentage ownership of the Company.")

# ─────────── NEW SECTION 7 — Protective Provisions (Term Sheet gap) ───────────
sec("Protective Provisions.",
    "So long as any portion of the Preferred Return remains unpaid, the Company shall not, without "
    "the prior written consent of the Investor Representative acting upon the written direction of "
    "Investors holding a majority of the Shares then subject to this Agreement:")
sub("(a)  issue or incur any security, instrument or obligation that is senior in payment priority "
    "to the Preferential Payments, other than indebtedness for borrowed money incurred in the "
    "ordinary course of business and trade payables; or")
sub("(b)  amend the Company’s Certificate of Incorporation or bylaws in a manner that "
    "disproportionately and adversely affects the Investors, in their capacity as such, relative "
    "to other holders of Class A Common Stock.")

sec("Termination.",
    "This Agreement shall automatically terminate upon the earliest of (i) the date on which the "
    "Investors have received aggregate Preferential Payments equal to their respective Preferred "
    "Returns, (ii) payment in full pursuant to Section 4, and (iii) the mutual agreement of the "
    "parties hereto. Sections 5(c), 12 and 13 survive termination.")

sec("Further Assurances.",
    "The parties hereto shall execute and deliver such other documents, certificates, agreements "
    "and other writings and take such other actions as may be necessary or desirable in order to "
    "consummate or implement expeditiously the transactions contemplated by this Agreement.")

# ─────────── SECTION 10 — Amendment, revised (Ankur item 3) ───────────
sec("Amendment and Modification.")
sub("(a)  Except as provided in Section 10(b), this Agreement may not be amended, modified, or "
    "supplemented except by a written agreement executed by the Company and Investors holding a "
    "majority of the Shares then subject to this Agreement, and any such amendment shall bind all "
    "Investors.")
sub("(b)  Notwithstanding Section 10(a), no amendment, modification, waiver or supplement shall be "
    "effective as against any Investor without that Investor’s prior written consent if it would "
    "(i) reduce, delay, subordinate or otherwise adversely affect such Investor’s Preferential "
    "Payments, Preferred Return, Investment Amount, or the priority or timing of payments to such "
    "Investor; (ii) adversely affect such Investor’s rights under Section 6; or (iii) affect such "
    "Investor in a manner that is disproportionate and adverse relative to the other Investors. "
    "This Section 10(b) may not itself be amended without the written consent of each Investor.")

sec("Assignment.",
    "The rights and obligations arising under this Agreement may not be assigned by any party "
    "without the written consent of the other parties.")
sec("Governing Law.",
    "This Agreement shall be governed by and construed in accordance with the laws of the State of "
    "Delaware, without regard to its conflicts of laws principles.")
sec("Counterparts.",
    "This Agreement may be executed simultaneously in one or more counterparts, and by the parties "
    "hereto in separate counterparts, each of which when executed will be deemed an original, but "
    "all of which taken together will constitute one and the same instrument.")

plain("[Remainder of page intentionally left blank]", italic=True, center=True, after=14)
d.add_page_break()
plain("IN WITNESS WHEREOF, the parties hereto have executed this Side Letter Agreement as of the "
      "date first above written.", after=14)
plain("INVESTORS:", bold=True, after=0)
sig("By:", ["Name:", "Title:"])
plain("INVESTOR REPRESENTATIVE:", bold=True, after=0)
sig("Ankur Jain", [])
plain("CLASS B STOCKHOLDER:", bold=True, after=0)
sig("Norman de Silva", [])
plain("COMPANY:", bold=True, after=0)
plain("CINDERELLA CORP", after=0)
sig("By:", ["Name: Norman de Silva", "Title: President & Founder"])

d.save(OUT)
print("wrote", OUT)
