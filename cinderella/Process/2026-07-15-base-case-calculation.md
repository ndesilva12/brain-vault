# Base-Case Calculation — Revenue Buckets & Rev-Share Mechanic
_Session: 2026-07-15 · synthesis of the four archetype builds
(2026-07-14-mbb-revenue-archetype-builds.md) into the model's inputs._

The reconciliation that replaces the inflated "$24M 80% share" with a
comps-grounded, additive-clean number defensible line-by-line to Ankur.

---

## The locked mechanic (2026-07-15)

Three separate money streams. Do not blend them.

1. **Bucket 1 — the school's own commercial revenue** (everything the school
   sells itself: gate, concessions, its own sponsors/MMR, apparel, licensing,
   school media/streaming, camps, guarantees).
   - Compute the **matured Bucket 1 total.**
   - **School keeps the BASELINE 100%** (what they always made pre-MC).
   - **Everything above baseline splits 80/20** — **SPV 80%, school 20%.**
   - **Net to the school = baseline + 20% of the growth.** The school can only
     come out ahead — this is what makes the deal signable to an AD.

2. **Bucket 2 — SPV-procured streams** (national / Netflix-grade presenting
   sponsor + premium patch, streaming/series license fee, live-game rights on
   school-owned neutral/non-conf games, monetized content engine, format +
   international windows). **100% to the SPV, directly. Never touches the
   school's books.** Not part of the rev-share.

3. **Structural (conf media, NCAA units, broad-based):** school keeps 100%.
   Units *explode* with a deep tournament run (SDSU generated ~$2.7M off one
   run) — real money that stays home and helps sell the deal.

4. **Donor (C\*):** separate track — **conversion** (would-be donors → SPV
   investors, primary) + **incremental 50/50** on the giving uplift MC creates.
   Baseline + general/athletics giving stay out. (See taxonomy + compliance note.)

**Base = match the comps' Bucket 1 (~$9M matured). Reach = outperform (~$12M).**

---

## Base-case build — representative Davidson-type school

Bucket 1, matured (anchored to the four comps' ~$8–10M ex-donor PCR ceiling):

| Bucket 1 line (school-sold) | Base | Reach |
|---|---:|---:|
| Ticketing | 3.8 | 5.0 |
| Concessions/parking/novelty | 0.5 | 0.7 |
| Sponsorship/MMR (school's own, regional) | 1.8 | 2.4 |
| School media/streaming | 0.3 | 0.4 |
| Licensing/merch | 0.9 | 1.3 |
| Apparel | 0.6 | 0.8 |
| Guarantee/neutral/MTE/tourney | 0.7 | 1.0 |
| Camps/rentals | 0.3 | 0.4 |
| **Bucket 1 total** | **~8.9** | **~12.0** |

Rev-share result (baseline kept 100%, increment split 80/20):

| | Baseline (school 100%) | Base matured | Reach matured |
|---|---:|---:|---:|
| Bucket 1 total | ~3.0 | ~8.9 | ~12.0 |
| Increment over baseline | — | 5.9 | 9.0 |
| **SPV 80% of increment** | — | **~$4.7M** | **~$7.2M** |
| School 20% of increment | — | ~$1.2M | ~$1.8M |
| **School total take** | 3.0 | **~$4.2M** | **~$4.8M** |

**Baseline is the key per-school knob.** ~$3.0M is a Davidson-type; a true
low-tier D1 target may baseline lower (~$1.5–2.5M), which *widens* the increment
the SPV shares in. Set per target school.

---

## Time shape — two opposite curves

- **Bucket 1 (organic) ramps UP.** A program matures into its gate/sponsor/
  licensing ceiling over 3–4 years. Model Year 1 ≈ 55–65% of matured; full by ~Y3.
  - Y1 base: Bucket 1 ≈ $5.5M → increment ~$2.5M → **SPV ~$2.0M**; ramps to ~$4.7M.
- **Bucket 2 (Netflix/hype) peaks EARLY, decays.** Series attention + launch-
  sponsor premium are hottest in Season 1. **This is the line the 10% decay
  fits** — not Bucket 1.

Blending them into one decaying curve (the old model) hid this. Keep them separate.

---

## Model reconciliation — the fix to the double-count

- **Old input:** "Year-1 80% share = $24M" → implied ~$30M shared commercial,
  ~5× what the four real comps prove exists (~$9M matured pie).
- **New input:** `Bucket1_matured` ≈ $8.9M base / $12.0M reach; `Bucket1_baseline`
  ≈ $3.0M (per-school knob); rev-share = **80% of (Bucket1 − baseline)**, ramping
  up over the clock. Matured SPV Bucket 1 ≈ **$4.7M/yr base.**
- The large additive money moves to **Bucket 2 (100% SPV)** — contract revenue,
  easier to underwrite than demand elasticity — built as separate SPV lines.

---

## Next passes
1. **Bucket 2 build** — streaming/series license, national presenting sponsor +
   patch, live-game rights, content engine, format/intl — at base/moderate/reach.
2. **Donor track** — conversion + incremental 50/50, sized off the relevance halo.
3. **School-side P&L** — prove cost-relief (SPV funds ~$9–13M NIL/roster) + kept
   structural/donor > the 80% commercial give-up. The slide that signs the LOI.
4. **Port to the model** — set `SchoolY1Commercial`/baseline/ramp; wire Bucket 2 +
   donor as separate SPV lines; fix the base commercial double-count for good.
