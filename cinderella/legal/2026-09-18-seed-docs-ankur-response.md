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

## ⚠️ Dropped by Loeb between 9/11 and the settled version — consider restoring

Neither is an Ankur item; both protect Norman and both appeared in `17XLRBuQ`:

1. **§1(e) — no personal obligation of the Class B Stockholder.** *"The Class B Stockholder
   undertakes no personal obligation, and shall have no personal liability, in respect of the
   Preferential Payments."* Norman signs the Side Letter personally. Without this, his signature
   is unqualified.
2. **Liquidation Event carve-out for format licensing.** *"a Liquidation Event does not include
   the grant of a license of the Company's format or other intellectual property to any special
   purpose vehicle, production partner, distributor or other counterparty in the ordinary course."*
   Without it, an aggressive reading of limb (c) — disposition of substantially all assets — could
   treat a major format license as a Liquidation Event and accelerate the full 2× Preferred Return.

**Also still open:** price per share is `$[____]` in the Subscription Agreement. Per the cap table
that is **$2.025** for **740,741** shares. 409A/Board determination required first.
