# Sunjay's Partner Agreement & Greg's Strategic Adviser Agreement — review

**Date:** 2026-10-07
**Reviewed:** the two `.docx` files Norman sent 2026-10-07. Logged as versions of record in
`current-versions-2026-10-07/`.
**Build:** `2026-10-07-partner-adviser-build.py` → `out-partner-adviser-2026-10-07/`
(21 patches, each asserted; all checks pass)

Both are the **parent** documents for grants whose terms got settled elsewhere today, and both had
drifted out of sync with the paper that implements them.

---

## Greg's Adviser Agreement was the problem. Three real defects.

### 1. ⚠️ Two sections were both numbered 2.3

`2.3 Vesting` and `2.3 Forfeiture / Repurchase` — then 2.4, 2.5, 2.6 continued from the second
one. So Article 2 had a duplicate number and everything after it was off by one.

Renumbered: **2.3 Vesting · 2.4 Forfeiture · 2.5 Class A only · 2.6 Tax / 83(b) · 2.7 No cash.**
Vesting deliberately keeps 2.3, because Greg's RSPA Schedule A cites "Strategic Adviser Agreement
§2.3" for the vesting schedule — that citation still resolves correctly.

### 2. Every economic term was still bracketed, while his RSPA states real ones

§8.2 makes the Adviser Agreement and the RSPA one agreement. The RSPA, settled this morning, says
4% / 166,667 shares / $0.001 / 24 months / no cliff / no acceleration. The Adviser Agreement
still said:

| Was | Now |
|---|---|
| `[4]%` of Class A | **four percent (4%)**, and §2.1 now states **166,667 shares at $0.001**, Board-determined FMV |
| `[4]%` → `[3.4]%` after a `[15]%` round | **3.375%** (166,667 of 4,938,272), marked an illustration |
| monthly over `[24]` months | **24 installments of 6,944** (final 6,955), mechanics restated in full |
| from `[Effective Date / vesting commencement date]` | **the Effective Date** |
| `[no cliff]` | **no cliff** |
| `[Optional: acceleration … confirm]` | **no acceleration**, stated affirmatively |
| `[30]` days' notice | **thirty (30) days** |
| `[24]` months non-circ tail | **twenty-four (24) months** |
| `[Rule 701 / Reg D]` | **Rule 701, §4(a)(2) fallback** — matches the RSPA |
| `[Venue / arbitration — confirm]` | **Delaware Court of Chancery, exclusive** — matches RSPA §9.1 and SHA §9.1 |
| `Title: [CEO / President]` | **Founder & Chief Executive Officer** |

### 3. §2.6 tax was backwards for him

It carried the same language as Ankur's — *"advised to consider filing an 83(b) election."*

**Ankur's shares are fully vested, so 83(b) is moot for him. Greg's shares vest over 24 months, so
83(b) is the whole ballgame.** The casual phrasing was imported from the wrong person.

Rewritten to match Greg's RSPA §5.1: the Shares are substantially nonvested property, the 30-day
window is statutory and non-extendable, and if he misses it he pays ordinary income on each
monthly tranche at that month's value instead of on $167 once.

### 4. §7 non-circumvention had no carve-out — only a note saying it needed one

As sent, §7 barred Greg from circumventing the Company "with respect to schools, celebrities,
capital partners, sponsors, or other counterparties introduced through or in connection with the
Company," followed by:

> *"[Confirm scope so it doesn't impair his existing Zero Gravity relationships — carve out
> pre-existing relationships.]"*

The note identified the problem and then left it in the document. As drafted it would have
restricted Greg from his own existing business relationships — the thing §1.3 expressly permits him
to keep running.

**Carve-out added, worded identically to Stockholders' Agreement §7.2** so the two cannot be read
against each other. This matters structurally: SHA §7.3 says that where a stockholder's separate
agreement contains a non-circumvention provision, *that* provision governs — so this is the
operative text, and it had to be right.

### 5. Internal notes removed

The header read *"Working draft, 2026-08-15, for review with Loeb & Loeb **and Sunjay** before
use"* — which tells Greg his paper is vetted by Sunjay. And the document ended with a four-item
"For counsel before use" checklist. All four items are now resolved, so both are gone.

---

## Sunjay's Partner Agreement was sound. Four changes, all knock-ons from today.

### §2.2 — the seed is no longer a fixed quantity

It hardcoded *"assuming a `[15]%` Seed Round"* and *"Partner's approximate post-Seed position
would be ~16.9%."* The Subscription Agreement now offers **up to $1.5M with no minimum**, so a
fixed post-Seed number can't be stated as fact. Restated as an illustration tied to a full raise,
and **~16.9% corrected to 16.875%** to agree with his RSPA Schedule A.

### §2.2 — a drafter's note was sitting in a counterparty document

> *"This figure is illustrative only and must be confirmed against the actual Seed Round terms and
> cap table model before use."*

Removed. (Same class of problem as the Ankur/Sunjay comparisons found in the RSPAs earlier today.)

### ⭐ §3.1 — "25% maximum" was arguable as a top-up right

It read: *"bringing Partner's maximum equity to twenty-five percent (25%)."*

Twenty-five percent **of what, measured when?** His base 20% is pre-Seed and becomes 16.875%
post-Seed. If "maximum equity 25%" is read as a position he's entitled to reach, then every
dilution event creates a shortfall he can claim back — **which is anti-dilution protection by the
back door.** §1.5(c) says he has no anti-dilution right of any kind, §2.5 says the Base Shares take
ordinary pro-rata dilution, and §3.6 says the same of Milestone Shares. §3.1 was the one sentence
that cut the other way.

Now explicit: 25% is **a ceiling on what may be granted**, measured on the same pre-Seed basis as
§2.1, and **not a percentage to be maintained** — with the cross-references to §§1.5(c), 2.5 and 3.6
written in. No economics changed; the ambiguity is closed in Norman's favour.

### §4.1 — 83(b) was wrong as to Milestone Shares

It said *"consider filing an 83(b) election within thirty (30) days of **each grant**."*

Correct for the Base Shares. **Wrong for Milestone Shares** — those are fully vested on issuance
under §3.6, so they aren't substantially nonvested property and no 83(b) election is applicable to
them. (Exactly the reasoning that removed Ankur's 83(b) today.) Telling Sunjay to file one for a
Milestone grant would have him file a pointless election; worse, it muddies whether the Base Shares
election — the one that actually matters — was properly made.

Split: Base Shares get the full strengthened warning (30 days, statutory, non-extendable, cost of
missing it); Milestone Shares get a plain statement that no election applies and that issuance is
itself a taxable event at the then-current FMV.

### §2.1 — share count added

Now states **833,333 shares**, so the Partner Agreement, the RSPA and the cap table all carry the
same number. Added for the same reason Ankur asked for a reconciliation.

---

## Flagged for you, not patched — both are business decisions

**1. Sunjay's §1.7 bars cash compensation for 12 months.** *"Partner will receive no cash
compensation, salary, bonus, benefits or other remuneration … during the first twelve (12) months
of the term,"* and any later comp must be *"determined and agreed separately in writing."*

**The parent-co budget funds a Sunjay salary.** If the raise closes and he starts drawing one inside
the first 12 months, §1.7 is breached unless that separate writing exists. It does not. Either
amend §1.7 or paper the salary separately when the round closes — but don't just start paying him.

**2. Greg is equity-only from September to December 2026.** He agreed $4k/month on Aug 30 per the
register. §2.7 says no cash is payable under the Adviser Agreement, and the separate Consulting
Agreement (Register 1.10) starts **1/1/27**. So there are roughly four months of work with no paper
behind the cash. Either start the Consulting Agreement earlier or put the interim months in writing.

---

## Checked, no change needed

- **Sunjay's Recitals A–D** (origination, the April 28 2026 Partner Start Date, the
  no-founder-claim acknowledgment, and §D making them contractual facts rather than preamble) —
  strong, and the most valuable part of the document. Untouched.
- **§1.2 / §1.3 / §1.6** (no founder claim, licensed title, sole spokesperson) with survival and
  injunctive relief in §1.6(f). Untouched.
- **§5.3 waiver of creation and credit claims**, including the "Created by Norman C. de Silva"
  first-position requirement and the moral-rights waiver. Untouched.
- **§6.2 Cause**, including (d) reputational harm. Broad, which is the intent. Untouched.
- **§5.4(c)** already carries the relationships carve-out that Greg's §7 was missing — which is how
  the gap in Greg's document was visible at all.
- **Track A and Track B** mechanics, the Outside Date of Dec 31 2029, the all-or-nothing rule, the
  12-month sustained-performance clawback on Track A, and Track B's Season-2-or-later restriction.
  Untouched. **Track B stays board-attributed by design** — the same reason Ankur's milestone fix
  was not propagated to Sunjay.
- **Greg §6 IP** — "works made for hire **and/or** assigned." Work-made-for-hire doesn't reach most
  independent-contractor output, but the assignment limb carries it. Cosmetic; left alone.
- **Greg §2.5 Class A only** — correct, and consistent with SHA §1.3.

---

## Open items

Carried forward unchanged, plus one new:

1. ⚠️ **Board resolution fixing $0.001 as FMV** — now asserted in *five* documents (four RSPAs and
   Greg's Adviser Agreement §2.1). Still doesn't exist. Blocking.
2. ⚠️ **83(b) elections prepared before countersignature** for Sunjay and Greg.
3. ⚠️ **The filed Certificate of Incorporation** into Subscription Agreement Exhibit A.
4. **NEW — Sunjay's salary needs its own writing** before any cash moves (§1.7).
5. **NEW — Greg's Sept–Dec 2026 cash needs paper** (§2.7 vs the 1/1/27 Consulting Agreement).
6. **Decide Greg's acceleration** — currently none, in both his RSPA and now his Adviser Agreement.
7. Loeb, one email: Rule 701(c) carve-out for Ankur; Rule 701 availability for Sunjay and Greg;
   FMV/409A support for $0.001; spousal consents.
8. Still open on Ankur's side: the **Tabor OBA Approval** (§0 condition precedent to his entire
   agreement) and the two capital-return asks.
