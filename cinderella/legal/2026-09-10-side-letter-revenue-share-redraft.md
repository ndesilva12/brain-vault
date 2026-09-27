# Side Letter Agreement — Revenue-Share Redraft (proposed edits to Loeb's draft)

_Prepared 2026-09-10. **Decision: keep Loeb's Subscription Agreement and Side Letter** rather
than switching to the vault's four-document set — the cross-references between those four make
them heavier, and "drafted by Loeb & Loeb" carries assurance with investors that in-house drafts
do not. Loeb built their documents from scratch without ever seeing the vault drafts._

**What this file is:** the operative sections of Loeb's Side Letter, redrafted so the trigger is
**gross revenue into the parent** rather than **declared dividends and distributions**, per
Ankur's clarification. Boilerplate that does not change (Further Assurances, Assignment,
Governing Law, Counterparts, signature blocks) is not reproduced.

**Definitions and exclusions below are adapted from the vault's own
`legal/clean/Revenue_Share_Agreement.md`** — that language was already drafted for exactly this
structure, so this is not new drafting risk.

---

## Why this is not a find-and-replace

| # | What breaks when the trigger becomes revenue | Fix |
|---|---|---|
| 1 | **"Gross Revenue" is undefined.** Undefined, it captures the Seed proceeds themselves, future financings, pass-through money owed to SPVs/schools/athletes, and taxes collected for remittance. | New definition **with exclusions** |
| 2 | **No payment mechanic.** A dividend has a declaration date and an amount; revenue arrives continuously. Nothing says when payment is due. | New §3(a), **Payment Period** definition |
| 3 | **Nothing to verify against.** Investors can see a declared dividend; they cannot see revenue without statements. | New §3(b)–(c), reporting + audit |
| 4 | **Diversion risk appears.** Once payment turns on revenue, revenue can be routed through an SPV or affiliate. Investors will require this; it costs Norman nothing. | New §3(d), anti-avoidance |
| 5 | **A sale pays nothing.** Sale proceeds go to *stockholders*, not the Company — so they are not revenue, and the right would simply die at closing. | New §4, Liquidation Event acceleration |
| 6 | **No protection for Company cash.** 50% of *gross* runs ahead of salaries, legal and G&A. | New §3(e), deferral below a reserve floor |

---

## REPLACE Section 1 in full

> **1. Acknowledgment and Agreement of Preferential Payments.** Until this Agreement terminates
> in accordance with Section 5, the Investors shall be entitled to the below rights (collectively,
> the "**Preferential Payments**") as follows:
>
> &nbsp;&nbsp;(a) first, **fifty percent (50%) of all Gross Revenue received by the Company**
> shall be paid to the Investors on a pro rata basis until the Investors have received aggregate
> Preferential Payments equal to one hundred percent (100%) of their respective Investment
> Amounts; and
>
> &nbsp;&nbsp;(b) second and finally, **ten percent (10%) of all Gross Revenue received by the
> Company** shall be paid to the Investors on a pro rata basis until the Investors have received
> aggregate Preferential Payments equal to their respective Preferred Return.
>
> &nbsp;&nbsp;(c) Where Gross Revenue in a single Payment Period causes the threshold in Section
> 1(a) to be met, the portion of such Gross Revenue required to reach that threshold shall be
> applied at the rate set forth in Section 1(a) and the remainder of such Payment Period's Gross
> Revenue shall be applied at the rate set forth in Section 1(b).
>
> &nbsp;&nbsp;(d) The Preferential Payments are in addition to, and shall not be credited or
> offset against, any dividend, distribution or other amount payable to an Investor in respect of
> such Investor's Shares. Each Investor's equity interest in the Company is unaffected by this
> Agreement, and this Agreement confers no voting, governance, management or ownership rights.

⚠️ **§1(d) is the one term to confirm with Sunjay and Ankur before sending.** It says the revenue
share sits **on top of** the 15% equity, which is how the vault draft reads (§2.5) and how Ankur's
framing implies. It is **not** the same question Norman asked them on 2026-09-09 — that question
was about residual *distributions* under a distribution-preference model, which no longer exists.

## REPLACE Section 2 (Definitions)

**Delete** `"Unrecovered Investment Amount"` — no longer used, since §1(a) now measures against
aggregate Preferential Payments directly.

**Keep unchanged:** `"Investment Amount"`, `"Liquidation Event"`.

**Add:**

> "**Gross Revenue**" means all cash actually received by the Company from its business operations
> during a Payment Period, determined on a cash basis, including distributions and dividends
> received by the Company from any special purpose vehicle or other subsidiary or portfolio
> entity; management fees, franchise fees and administrative or service fees; sponsorship,
> marketing and brand-partnership revenue; content, media, documentary, live-event and
> distribution license fees; and format-licensing, merchandising and other intellectual-property
> royalties. **Gross Revenue expressly excludes:** (i) proceeds of any equity or debt financing,
> including the sale of the Shares and any subsequent capital raise, loan, note or credit
> facility; (ii) capital contributions to the Company; (iii) amounts received by the Company as
> agent, custodian or pass-through for the account of a third party, including amounts collected
> on behalf of any special purpose vehicle, institution, athlete or talent, that the Company is
> contractually obligated to remit, in each case to the extent so remitted; (iv) sales, use,
> excise, withholding and similar taxes collected for remittance to a governmental authority;
> (v) refunds, rebates, credits and chargebacks actually paid or credited to a payor, and amounts
> invoiced but not collected; (vi) proceeds from the sale or disposition of capital assets outside
> the ordinary course of business; (vii) insurance and litigation proceeds, other than
> business-interruption proceeds compensating for lost operating revenue; (viii) proceeds received
> in or in connection with a Liquidation Event; and (ix) interest income and other non-operating
> income.
>
> "**Payment Period**" means each calendar quarter, or portion thereof, during the term of this
> Agreement.

**Replace:**

> "**Preferred Return**" means, with respect to any such Investor, an amount equal to the product
> of (x) two (2) and (y) the Investment Amount for such Investor. **The Preferred Return is an
> aggregate amount. All Preferential Payments received by an Investor, whether pursuant to Section
> 1(a) or Section 1(b), shall count toward, and reduce the amount remaining payable to reach, such
> Investor's Preferred Return, and in no event shall aggregate Preferential Payments to an
> Investor exceed such Investor's Preferred Return.**

## INSERT new Section 3

> **3. Payment; Reporting; Audit.**
>
> &nbsp;&nbsp;(a) The Company shall pay amounts due under Section 1 within forty-five (45) days
> after the end of each Payment Period.
>
> &nbsp;&nbsp;(b) With each payment, the Company shall deliver a statement showing, for the
> Payment Period: Gross Revenue and its computation, the applicable rate, the amount paid, and
> cumulative Preferential Payments to date against the thresholds in Sections 1(a) and 1(b).
>
> &nbsp;&nbsp;(c) The Company shall maintain books and records sufficient to verify Gross Revenue
> for three (3) years following each Payment Period. Once per calendar year, on thirty (30) days'
> prior written notice, Investors holding a majority of the Shares then subject to this Agreement
> may cause an independent certified public accountant to examine such records solely to verify
> the computation of Gross Revenue. The examining party shall bear the cost of such examination,
> except that if the examination discloses an underpayment exceeding five percent (5%) for the
> period examined, the Company shall bear the reasonable cost of the examination and pay the
> shortfall within thirty (30) days.
>
> &nbsp;&nbsp;(d) The Company shall not structure transactions with the principal purpose of
> diverting, deferring or re-characterizing Gross Revenue so as to avoid or reduce payments under
> this Agreement. Revenue arising from transactions with affiliates of the Company shall be
> included in Gross Revenue at arm's-length fair value.
>
> &nbsp;&nbsp;(e) **Deferral.** The Company may defer any payment otherwise due under Section 1 to
> the extent the Board of Directors determines in good faith that making such payment would leave
> the Company with unrestricted cash reserves of less than **[$________]**. Any amount so deferred
> shall accrue and be paid promptly once payment would no longer reduce reserves below such
> amount.

## INSERT new Section 4

> **4. Liquidation Event.** Upon the closing of a Liquidation Event, the Company (or its
> successor) shall pay to the Investors, at closing and on a pro rata basis, an amount equal to
> the excess of (a) the aggregate Preferred Return of all Investors over (b) aggregate
> Preferential Payments made through the closing date. Upon such payment, this Agreement shall
> terminate. For the avoidance of doubt, such payment is in addition to the consideration payable
> to the Investors in respect of their Shares.

## REPLACE Termination (now Section 5)

> **5. Termination.** This Agreement shall automatically terminate upon the earliest of (i) the
> date on which the Investors have received aggregate Preferential Payments equal to their
> respective Preferred Returns, (ii) payment in full pursuant to Section 4, and (iii) the mutual
> agreement of the parties hereto.

## REPLACE Amendment and Modification (now Section 7)

> **7. Amendment and Modification.** This Agreement may not be amended, modified, or supplemented
> except by a written agreement executed by the Company and Investors holding a majority of the
> Shares then subject to this Agreement, and any such amendment shall bind all Investors.

---

## Renumbering and cross-references

Inserting two sections pushes everything down by two:

| Was | Becomes |
|---|---|
| 3. Termination | **5.** Termination |
| 4. Further Assurances | **6.** Further Assurances |
| 5. Amendment and Modification | **7.** Amendment and Modification |
| 6. Assignment | **8.** Assignment |
| 7. Governing Law | **9.** Governing Law |
| 8. Counterparts | **10.** Counterparts |

⚠️ **Pre-existing cross-reference error in Loeb's draft — flag it to them.** Section 1 opens
*"Until this Agreement terminates in accordance with **Section 2**"* — but Section 2 is
Definitions; Termination is Section 3. **In the redraft it must point to Section 5.**

⚠️ Also update the second recital: it currently says Investors receive *"certain dividend,
distribution, liquidation and other preferential payments."* Should read *"certain preferential
payments based on the Company's gross revenue,"* so the recital matches the operative section.

---

## Still outstanding on the Subscription Agreement (unchanged by this redraft)

1. 🔴 Acceptance block hardcoded **"1st day of January, 2025"** — replace with a blank.
2. Price per Share, share count and date are blank.
3. **Exhibit A (Certificate of Incorporation) is a heading with nothing attached.**
4. Investors rep they understand "the risk factors" — none are defined or attached.
5. Fund-template drift: ERISA "benefit plan investors," "all investments of the Company,"
   "at least 21 years old."
6. ⚠️ **Rule 506(b) general-solicitation exposure** given how widely the deck has circulated —
   the single most important question to put to Brian. See
   `2026-09-06-seed-docs-review-memo.md` §18.
