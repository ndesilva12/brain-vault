# Cinderella Corp — Financial Model & Franchise Mechanics
_Session: 2026-07-05_

Captures how the franchise functions economically, as encoded in the live
model. Source of truth is the Google Sheet, but this is the plain-English
spec so the logic survives outside the spreadsheet.

**Live model:** Google Sheet "Cinderella Corp Model"
(https://docs.google.com/spreadsheets/d/1mbYo2aQmMSXUaX1gYYSRfCnWvm4EaKFzlkv-qU6EO_U/edit).
Formula-driven — every tab recalculates off the **Assumptions** tab. Five
tabs: Summary · Per-School SPV (5-Yr) · Franchise Rollup · Parent Co P&L ·
Assumptions. ~58 named inputs; scenario dropdown (Base / Moderate / Reach).

---

## The two-layer structure

1. **Cinderella Corp (parent).** Holds all IP + franchise architecture.
   Raises **$1.5M for 15% equity** from 15 investors ($100K = 1%). Norman
   retains ~85% (pre further dilution). Parent funds operations only, not
   the teams.
2. **Per-season SPVs (one per school).** Each is its own entity, **5-year
   life**, responsible for its own obligations (incl. NIL). Single-tier:
   **every school uses the same archetype** — no anchor/standard split.

### What the parent earns from each SPV
- **40% equity** in the SPV → 40% of its net cash flow.
- **10% franchise fee** on SPV cost, one-time at close (= $1.5M on a $15M SPV).
- **2% annual management fee** on SPV cost (= $300K/yr) for the 5 years.

### SPV equity split (100%) — current
| Holder | % |
|---|---|
| Cinderella Corp (parent) | 40% |
| Lead talent / celebrity | 15% |
| Lead / presenting sponsor | 10% |
| Streaming partner | 5% |
| Basketball Operators (Norman) | 10% |
| Partnership Operators (Sunjay Mathews) | 10% |
| Strategic partner contingency | 10% |

**Norman's total per-SPV economics** = 85% × 40% (via parent) **+** 10%
direct (Basketball Operators) ≈ **44%** of SPV net.

---

## Revenue model (per school, per year)

- **Documentary licensing.** Platform pays $/doc-hour (prestige rate).
  EverWonder finances production and recoups **cost + 10%** from the
  streaming sale; the SPV keeps everything **above** that recoup. So the
  SPV's platform revenue is *net* of the EverWonder recoup.
- **Live game streaming** — per-game fee × games/year.
- **Sponsorships** — presenting sponsor + jersey patches + category
  sponsors. All step down after Year 1 (post-transformation).
- **School revenue share.** The SPV takes **80% of the school's incremental
  commercial revenue** (Year-1 commercial − baseline), **decaying 10%/yr**.
  The school keeps the other **20%**.

## Cost model (per school, per year)

- **NIL contracts** — the roster. Year 1 fully SPV-funded (~$12M).
  **See NIL self-funding mechanic below** for Years 2-5.
- **Live game production**, **marketing/legal/contingency** — annual.
- **Franchise fee** (Y1 only) and **management fee** (annual) — paid up to
  the parent; they're SPV expenses and parent income.
- **Documentary production** — $0 to the SPV (EverWonder finances it).

---

## NIL self-funding mechanic (the flywheel) — SPV-funded

The defining feature. After Year 1, the roster is meant to pay for itself
from the program's own commercial success:

- **Year 1:** SPV funds the full NIL (~$12M).
- **Years 2-5:** the **school's 20% revenue share** is redirected to fund
  that year's NIL, **capped at the Year-1 NIL amount**.
  - If the school's share **exceeds** the cap → school funds the full NIL
    and **keeps the excess**.
  - If it **falls short** → school contributes all of it and the **SPV
    covers the shortfall** (the SPV owns its obligations — this is NOT a
    parent-level cost).

**Decision (2026-07-05): the shortfall is funded by the SPV, not by
Cinderella Corp.** Rationale: each SPV is its own entity responsible for all
obligations related to its team. This keeps the parent off the hook and
consistent with the capitalization thesis (sponsors + streaming + PE fund
the SPV's NIL, not the parent).

**Reality check to defend in the deck:** at conservative revenue the
school's 20% share is small (e.g., Base: ~$3M share vs $12M NIL → ~$9M/yr
shortfall). The shortfall is the single biggest driver of returns. This is
exactly why NIL was always intended to be funded at the SPV level by the
sponsor/streaming/PE capital stack — **if the parent ever ate NIL
shortfalls, parent economics go underwater below aggressive revenue.**

---

## Franchise rollup (scaling)

- **Cohorts launch in successive seasons**; each cohort = `SchoolsPerCohort`
  schools; each school runs its full 5-year SPV. So cohort 3's tail (if 3
  cohorts) ends in season 7 → a staggered ramp of active schools, e.g. 3
  cohorts → **3, 6, 9, 9, 9, 6, 3** active per season.
- **Total schools = SchoolsPerCohort × NumCohorts.**
- The rollup is now **generalized to flex with `Number of cohorts`** (was
  hardcoded to 3). Each season sums a rolling window of overlapping cohorts
  via `SUMPRODUCT`. Layout frame = 7 season columns (supports up to 3
  cohorts); N cohorts needs N+4 columns.

### How scale affects investor MOIC
With a **fixed** raise ($1.5M/15%) and **fixed** parent operating budget,
**MOIC rises with total schools** — each school adds franchise fees + mgmt
fees + 40% of its net, at no extra parent cost. Verified: 1 / 2 / 3 cohorts
→ **12x / 24.5x / 37x** (Moderate). MOIC would only *fall* with scale if the
parent took on a per-cohort cost (e.g., if it funded NIL shortfalls — which
we've decided it does **not**).

---

## Parent economics & investor return

- **Parent income** = franchise fees + management fees + 40% of franchise
  net CF, across the operating seasons.
- **Parent expenses** = Year-0 raise deployment + annual run-rate (~$970K:
  founder salary, basketball ops, partnership ops, payroll load, legal,
  plus a one-time closing bonus).
- **Distributable** = net parent income over the operating years.
- **Investor pool = 15% of distributable**; per-$100K return = pool ÷ 15;
  **MOIC = return ÷ $100K.**

**Representative outputs** (Moderate, 3 cohorts / 9 schools): distributable
~$370M, MOIC ~37x. Scenario spread at 3 cohorts ≈ **17x (Base) / 37x
(Moderate) / 66x (Reach)**. These move with every assumption and are being
actively revised — treat as directional, not final.

---

## Current assumption set (as of 2026-07-05)

- Raise $1.5M / 15% / 15 investors; Norman ~85% of parent.
- SPV cost $15M; franchise fee 10%; mgmt fee 2%; SPV life 5 yrs.
- Rev share 80%; decay 10%; school baseline $3M.
- School Y1 commercial revenue: **$18M / $28M / $38M** (Base/Mod/Reach).
- NIL Year 1 $12M; Years 2-5 → self-funding mechanic (SPV shortfall).
- Live game production $500K; marketing/legal/contingency $650K.
- Doc hours Y1 = 5, Y2-5 = 1; production $600K/hr.
- Parent run-rate ~$970K/yr; closing bonus $100K (one-time).
- Schools per cohort 3; number of cohorts flexes.

---

## Open items / to build

1. **Wire the NIL self-funding mechanic into the sheet** (SPV-funded):
   Per-School helper rows compute school's 20% share → school-funded NIL
   (prior year, capped at Y1 NIL) → SPV shortfall; then set Per-School NIL
   expense Years 2-5 = the shortfall. Instructions drafted; not yet in the
   live sheet.
2. **Franchise rollup generalization** — formulas drafted & verified;
   paste into the live tab (or copy the reference tab).
3. **Downside/cost stress** — even Base prints a high MOIC; the model needs
   a conservative case that flexes NIL cost and a "% of SPV cash actually
   distributed" haircut, so returns reflect execution risk, not just soft
   revenue.
4. Decide whether `Number of cohorts` or `Schools per cohort` is the primary
   scaling lever for the deck narrative (both now work).
