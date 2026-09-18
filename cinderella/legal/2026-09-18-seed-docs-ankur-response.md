# Seed Docs v2 — Ankur's 2026-09-18 email, implemented in full

**Base documents (the ones Loeb settled on):**
Drive → Legal → **Seed Round › Final**
- `Cinderella Corp - Subscription Agreement Final` (`1vYhWtma6R--_GNOwBUShcPWU7iaQ52yh`)
- `Cinderella Corp - Side Letter Agreement Revenue Share Final` (`1ap_G8zQaeH6KNM-mC4Va8jK8IdVKOmdZ`)

> ⚠️ **Three side-letter files exist and they are NOT the same document.** Check the file id.
> - `1ap_G8zQ` — **settled, use this**. Liquidation formula correct.
> - `17XLRBuQ` (9/11, was in Final) — **older**. Liquidation formula broken; this is what Ankur
>   reviewed. Also contains two protections the settled version drops — see "Dropped by Loeb".
> - `1bI7bBTb`, `1D7DtFUep`, `1OTfe36k` — earlier drafts in the parent folder.

Generators: `2026-09-18-side-letter-v2-generator.py` · `2026-09-18-subscription-agreement-v2-generator.py`
Cross-references resolve by **section name**, so inserting a section cannot break them.

---

## Every item, and where it landed

| # | Ask | Status |
|---|---|---|
| 1 | Investor Rep indemnity + D&O | **Granted in full.** SL §5 |
| 2 | Return of undeployed capital at will | **Granted in full — sole discretion.** SL §6 |
| 3 | No adverse amendment without consent | **Granted in full.** SL §10(b) |
| 4 | Reconcile share class | Already Class A throughout. Confirmed expressly in Sub |
| 5 | Liquidation formula | **Already fixed by Loeb** in the settled version |
| 6 | Deferral blank | Filled — Minimum Reserve |
| 7 | Remove callable | Not present in either document. Nothing to do |
| 8 | Expense policy | **Granted.** SL §7 covenant + Exhibit A |
| 9 | Send full package | SHA + RSPAs ready; Sub now references and furnishes the SHA |

## §6 — exactly as Norman directed

- **"At any time, in the Investor Representative's sole discretion"** — no anniversary, no
  milestone, no vote of investors, the Board or the Company. Exercisable repeatedly.
- **Seed funds only.** "Undeployed Seed Capital" is *proceeds of the sale of the Shares* that are
  undeployed and legally available. It expressly **excludes Gross Revenue, the proceeds of any
  other financing, any dividend or distribution, and any other asset**, and is **capped at
  aggregate Investment Amounts** less prior returns.
- "Deployed" = expended **or contractually committed** under an executed agreement.
- Returns reduce Investment Amount dollar-for-dollar; Preferred Return recomputes; **Shares and
  ownership percentage are untouched**.
- 30 days to pay; anti-dissipation covenant in the interim.
- §6(c) tracks **Ankur's own proviso** — "legally available for return."

## Additions Ankur did not ask for, made because the above required them

- **Two risk factors in the Subscription Agreement**: "Return of Undeployed Capital" and "Reliance
  on the Investor Representative." A sole-discretion recall right that can strand the business
  plan is material and has to be disclosed to the other 14 investors. Do not remove these.
- **Subscription Agreement now names the Investor Representative** and has each investor
  acknowledge that his actions bind them — otherwise SL §5 binds people who never agreed to it.

## ✅ Dropped by Loeb between 9/11 and the settled version — both restored

Neither was an Ankur item; both protect Norman, both appeared in `17XLRBuQ`, and **both are now back in**:

1. ~~**§1(e) — no personal obligation of the Class B Stockholder.**~~ ✅ **RESTORED 2026-09-18**
   at Norman's direction. The signature block is also re-qualified to read *"CLASS B STOCKHOLDER
   (solely for purposes of Section 1(e))"* — the qualifier is half the protection and travels with
   the clause.
2. ✅ **RESTORED 2026-09-18.** Liquidation Event carve-out for format licensing. Without it,
   limb (c) of the definition — disposition of all or substantially all assets — could be argued
   to cover a major exclusive format license, accelerating the full 2x Preferred Return (up to
   $3M) at the moment of signing, while the license fee itself arrives over years. Sunjay's
   agreement already carries the identical carve-out, so the two documents are now consistent.

## Seed price and share count — FILLED 2026-09-18

**$2.025 per Share.** Not a choice — it is forced by the deal: Norman's 3,000,000 Class B shares,
the 72/20/4/4 pre-Seed split, 15% for $1,500,000, and a $10,000,000 post-money.

| Allocation | Shares | Price |
|---|---|---|
| One allocation (1.0%) | **49,383** | $100,000 |
| Full round (15 allocations, 15%) | **740,745** | $1,500,000 |

Post-Seed cap table:

| Holder | Shares | % |
|---|---|---|
| Norman (Class B) | 3,000,000 | 60.7499% |
| Sunjay | 833,333 | 16.8750% |
| Greg | 166,667 | 3.3750% |
| Ankur (after 30,864 top-up) | 197,531 | 4.0000% |
| Seed investors | 740,745 | 15.0001% |
| **Total** | **4,938,276** | 100% |

Class A issued 1,938,276 of 6,000,000 authorized; Class B stays 3,000,000 of 4,000,000.
**No charter amendment required.**

⚠️ **Rounding.** 49,383 x $2.025 = $100,000.57, so a $100,000 subscription is being accepted for
49,383 shares — a 57-cent concession per investor, $8.62 across the round. Immaterial, but it is
why the round totals 740,745 rather than the mathematically exact 740,740.74.

**Why the numbers are not round:** the founder block is 3,000,000. Had it been 6,075,000, the
price would be exactly $1.00 and an allocation exactly 100,000 shares — which is where the
`1,500,000 shares` figure in the superseded drafts came from. Getting there now needs a 2.025:1
split and a charter amendment (6,075,000 exceeds the 4,000,000 Class B authorized). **Not worth
it.** Nobody outside the stock ledger sees these numbers.

