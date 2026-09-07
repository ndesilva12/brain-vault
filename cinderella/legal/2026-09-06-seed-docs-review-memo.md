**CONFIDENTIAL — QUESTIONS FOR COUNSEL**

# Seed Round Documents — Review Memo

_Reviewed 2026-09-06: **Side Letter Agreement (Series Seed Preferential Payments)** and
**Subscription Agreement for Common Stock**, both received from Loeb & Loeb in draft.
Nothing signed. Norman's raise: **$1.5M for 15%** (15 × $100K for 1% each)._

---

## ⭐ THE THREE THINGS TO FIX BEFORE ANYONE SIGNS

### 1. The Preferred Return is ambiguous — it reads as either 2x or 3x

Side Letter §1 creates a two-step waterfall:
- **first**, 50% of every distribution until Investors recover **100% of Unrecovered
  Investment Amount** (= 1x their money back);
- **second**, 10% of every distribution until Investors receive their **"Preferred Return."**

**"Preferred Return" is defined as 2 × Investment Amount.** The document never says whether the
1x already paid under step one *counts toward* that 2x.

**Why this is a real ambiguity and not pedantry:** the drafters clearly knew how to net out prior
payments — they did exactly that in *"Unrecovered Investment Amount"* ("...**less any aggregate
amounts previously distributed** ... pursuant to Section 1(a)"). They did **not** put equivalent
netting language in "Preferred Return." Under ordinary contract construction, that omission is
read as deliberate. An investor's counsel will argue the 2x is measured on its own, producing
**1x + 2x = 3x total**.

| Reading | Investor gets on $1.5M | Difference |
|---|---|---|
| 2x total (likely intent) | $3.0M | — |
| 3x total (defensible on the text) | $4.5M | **+$1.5M** |

**Fix:** state it in numbers, not labels — *"...until such Investor has received aggregate
payments under this Section 1 equal to two times (2x) its Investment Amount, inclusive of all
amounts received under Section 1(a)."*

### 2. It does not say whether Investors ALSO share in the remainder — a likely double-dip

The waterfall says a percentage of each distribution "shall be declared, paid or set aside **for
the Investors**." It is silent on what happens to the other 50%. The natural reading is that the
remaining 50% goes to **all** stockholders pro rata — **including the Investors' own 15%.**

On a $1M distribution that means: $500K preference **+ 15% of the remaining $500K ($75K) =
$575K**, on a 15% stake. That is participating-preferred economics, which may be what was
negotiated — **but nobody appears to have decided it.**

**Fix:** say expressly whether the Class A held by Investors participates in the residual, or
whether the preference is in lieu of pro rata participation until the Preferred Return is met.

### 3. ⚠️ The economics are in a side letter, not in the charter

This is the structural one. A Delaware corporation's dividend and liquidation rights **live in
the Certificate of Incorporation.** The A&R Charter (Contract Register 1.1) creates Class A
(1 vote) and Class B (10 votes, Norman only) — and, as far as the vault records, gives them
**ratable** economic rights. A contract among stockholders that redirects 50% of every dividend
away from that ratable split sits in tension with the instrument that actually governs
distributions.

**Two consequences worth raising with Brian directly:**
- **Enforceability.** Directors declaring a dividend act under the charter. A side letter binds
  the parties contractually but does not amend the charter.
- **Diligence risk at Series A.** A real institutional lead will run the charter against the cap
  table. Off-charter economics that don't reconcile is exactly the finding that stalls a round
  and forces a clean-up recap.

**Ask counsel:** should this be a **charter-level preferred class** rather than a side letter?
If the side letter is deliberate (speed, avoiding a charter amendment), get the reasoning in
writing.

---

## 🔴 DOCUMENT CONFLICT — two instruments doing the same job

**The vault already contains `legal/clean/Revenue_Share_Agreement.md`** — a drafted Revenue-Share
Right on *Gross Cash Revenue*, expressly "granted **in addition to, and independent of**, the
shares purchased under the Purchase Agreement ... as part of the same private placement."

Loeb's new Side Letter grants preferential payments on *distributions* to the same investors for
the same money.

**These are two different mechanisms for paying the same investor the same return. Executing both
pays them twice.** Likewise, the Contract Register lists a drafted **Stock Purchase Agreement**
(1.4) — the new **Subscription Agreement** appears to replace it.

**Before the close, confirm in writing which set governs:**

| Vault (drafted, "clean") | Loeb (new draft) | Which survives? |
|---|---|---|
| Stock Purchase Agreement (1.4) | Subscription Agreement | ❓ |
| Revenue-Share Agreement (1.5) | Side Letter — Preferential Payments | ❓ |
| Stockholders' Agreement (1.6) | *(no counterpart received)* | ❓ still needed? |
| Seed Term Sheet (1.3) | — | Does the new paper match what the term sheet promised investors? |

⚠️ **Check the new documents against the term sheet already shown to investors.** If anyone was
pitched the revenue-share structure and is now handed a preferential-payment side letter, that is
a changed deal and needs to be surfaced, not quietly swapped.

---

## Side Letter — further issues

**4. "Liquidation Event" catches the business model.** Limb (c) covers *"any sale, transfer or
other disposition of all or substantially all the assets."* **Cinderella Corp's only real asset
is the Format/Franchise IP, and licensing it is the entire business.** A large exclusive format
license to a streamer could be argued into this definition, triggering the full waterfall on an
ordinary-course transaction. Note the vault's own Revenue-Share draft anticipated this and named
IP disposition explicitly; Loeb's version neither carves it out nor addresses it.
**Fix:** carve out ordinary-course format licensing to SPVs and platform licensing.

**5. Limb (b) is triggered by Norman's own share sales.** It captures a sale of stock *by
stockholders* moving >50% of voting power. Norman holds **all** Class B at 10 votes/share, so
his voting power moves fast — a partial secondary by him could trip a Liquidation Event and the
waterfall. Confirm this is understood.

**6. Do SPV distributions flow through the waterfall?** The definition reaches the Company "and
its consolidated subsidiaries." Per the model, Cinderella holds **40%** of each SPV — likely not
consolidated. But SPV cash reaching the parent and then being distributed **is** caught. Confirm
the intended treatment of Management Services and franchise fees.

**7. The termination clause is circular.** §2 terminates when *"100% of the Preferential Payments
have been paid"* — but "Preferential Payments" is defined as *rights*, not a sum. Tie termination
to the Preferred Return figure instead.

**8. No buyout right.** The preference runs indefinitely with no mechanism for the Company to
retire it early. **Consider a call right** letting Cinderella extinguish it by paying the
Preferred Return — valuable if the company outperforms.

**9. Amendments require unanimity.** §5 requires "a written agreement executed by **all** parties."
With 15 investors, every future amendment needs all 15 signatures — and §6 requires all-party
consent to assign. **Change to Company + holders of a majority-in-interest.** This will otherwise
become a genuine operational problem within a year.

**10. Norman signs individually as "Class B Stockholder" but has no defined obligations.** The
recitals frame the preference as running "in relation to the holder of Class B Common Stock."
Being a party in his personal capacity without a stated role invites an argument that he is
personally on the hook for the preference. **Clarify he signs to acknowledge only — or remove him
as an individual party.**

---

## Subscription Agreement — further issues

**11. 🔴 The acceptance block is dated `1st day of January, 2025`** — hardcoded, ~20 months before
the investor's own September 2026 signature line. A template artifact, but it is on the Company's
execution block. **Replace with a blank.**

**12. Blanks that must be filled and reconciled:** price per Share (`$[____]`), number of Shares,
subscription amount, date. The per-share price must tie to the intended post-money cap table —
Norman 72 / Sunjay 20 / Ankur 4 / Greg 4 pre-Seed, with Ankur non-diluting through a 15% Seed
(per the Sunjay Partner Agreement §2.2).

**13. Exhibit A is a heading with nothing behind it.** The Certificate of Incorporation is
referenced as attached and incorporated into the terms — **it must actually be attached.**

**14. "Understands the risk factors" — but no risk factors are defined or attached.** The
Contract Register contemplates a risk-factors document. Investors are repping to something that
isn't in the package. **Attach it.** Non-reliance language does not cure a disclosure gap, and
anti-fraud liability under 10b-5 is not waivable.

**15. Template drift from a fund document.** The ERISA "benefit plan investors" 25% rep, the "No
Special Purpose Entity" clause, and especially *"any equity or other owners of the Investor share
in all the gains or losses of **all investments of the Company**"* are lifted from a private-fund
LP subscription agreement. Cinderella is an operating company, not a fund. Harmless legally, but
it reads as un-tailored to a sophisticated investor. Also *"at least 21 years old"* — capacity is
18. **Ask Loeb to tailor.**

**16. Zero Company representations.** The document is entirely one-directional — investor reps
only. **This favors Norman**, but expect sophisticated money (Ankur/Tabor especially) to require
at least due authorization, valid issuance, and a capitalization rep. Know it's coming; don't
volunteer it.

**17. No closing mechanics.** No minimum-raise condition, no escrow, no acceptance deadline. Each
subscription can be accepted independently — **good for a rolling close**, which suits the 15 ×
$100K structure. Flagging only so it's a choice rather than an accident. If Norman wants
all-or-nothing at $1.5M, that needs escrow language.

---

## ⚠️ 18. THE ONE TO RAISE WITH BRIAN FIRST — Reg D exemption and general solicitation

The Subscription Agreement has the Investor represent that **"neither the Company nor any person
acting on behalf of the Company offered to sell, or sold to the Investor, the Shares by means of
any form of general solicitation or general advertising."**

That representation places the offering under **Rule 506(b)**, which prohibits general
solicitation entirely.

**This needs an honest look at the actual outreach history.** The deck at
`cinderella.short.gy/deck` has circulated very widely — celebrities, agents, production
companies, athletic directors, cold outreach, and per-target variants (`/tb`, `/sas`). Much of
that is talent and partnership solicitation rather than securities offering, and that distinction
is exactly the point — **but it is a facts-and-circumstances test, and the volume is high.**

**Why it matters:** if general solicitation is later found to have occurred, the 506(b) exemption
fails, and investors may hold **rescission rights** — the ability to demand their money back.
Discovered at a Series A, that is a deal-stopper.

**Two questions for counsel:**
1. Given the outreach pattern, is **506(c)** the safer path? It permits general solicitation but
   requires **verified** accredited status (not the self-certification in §"Accredited Investor").
2. If staying at 506(b), what does Norman need to change **now** about how the deck circulates,
   and does a pre-existing-relationship analysis cover the current investor list?

**Do not paper over this by relying on the investor's representation.** The investor repping "no
general solicitation" does not create the exemption — the facts do.

---

## What is genuinely good here

- The **non-reliance** and **Access to Information** clauses are solid founder protection.
- **Irrevocable subscription** with Company-side discretion to accept is favorable.
- **No protective provisions, no board seat, no information rights, no pro rata rights** in these
  documents — Class A is 1 vote against Norman's 10-vote Class B. Control is well preserved.
- The **IPO lock-up** is capped at one year with a most-favored-nation floor. Fine.
- The preference is **non-accruing** — no interest ticking against the company over time.

---

## Recommended sequence

1. **Reconcile the two document sets** (Revenue-Share vs. Side Letter; Stock Purchase vs.
   Subscription) — nothing goes to an investor until it is clear which governs.
2. **Resolve 2x-vs-3x and the participation question** in the Side Letter text.
3. **Get counsel's written position on charter-level preferred vs. side letter.**
4. **Raise the 506(b)/506(c) question** with a candid account of how the deck has circulated.
5. Fix the January 2025 date, attach Exhibit A and the risk factors, fill the blanks.
6. Change the amendment threshold to majority-in-interest before there are 15 signatures to chase.
