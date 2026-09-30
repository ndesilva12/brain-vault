# Grassroots Reach Ranking — generators

Ranked, self-scoring list of people with genuine grassroots-level reach, built for the
Boardwalk Pictures fan-engagement thread (call #2, 2026-09-23 / 09-30 follow-up).

## Live Google Sheets

| Version | Rows | Scored | Sheet |
|---|---|---|---|
| v1 | 89 | 89 | `1Rm6uP6_Q1U69fUEfjAJXLN6HNVRGkB04XiJ9jY_aH3Q` |
| v2 | 237 | 89 | `1RpHxfOOzL5CB-dCZFTAlwa2fGVbU-paGNLcjod7nrIc` |
| ⭐ **v3 — current** | **237** | **237** | `1XM_bKEE6ESkGtJtQNo_Jt4ReLx7oqWUQjI-I8rJoLys` |

v1 was biased toward names already in the vault and omitted global mega-following names
(Ronaldo, Messi) and — worst omission — **Ryan Reynolds and Rob McElhenney**, the literal
proof case for the whole format. v2 added 148 names with no pre-filtering for perceived fit
but left their judgment columns blank. **v3 fills them**, so all 237 names rank against each
other.

⚠️ **The Drive connector can only create sheets, not rewrite them** — so each pass is a new
link. Earlier versions are superseded, not live.

## How the sheet works

- **Weights live in `B6:B10`** and must total 1.00 (`B11` checks). Change a weight and every
  COMPOSITE and RANK recalculates.
- **`E11` / `F11` hold the column maxima** for Reach and Engagement; the per-row composite
  normalizes against them rather than recomputing `MAX()` 237 times.
- **COMPOSITE is blank-safe**: `COUNT($F:$I)<4` means a row with any unfilled judgment column
  stays blank instead of scoring artificially low. `RANK` ignores blanks.
- Formulas are **per-row, with absolute anchors** — deliberately not `ARRAYFORMULA`, so
  `Data → Sort range` cannot break them.
- **`Scored_By` reads `Jimmy est.` on all 237 rows in v3** — every number is an estimate, including
  the legacy 89. ⭐ **Norman does the actual ranking**; these values exist as *reference data* while
  he does it. Overwrite any cell and COMPOSITE + RANK recalculate immediately.
- ⚠️ **`Eng_Pct` is not a literal engagement percentage.** It is an engagement-INTENSITY score on
  the 0–11 band the v1 rows established (IShowSpeed 11 is the ceiling, ~6 is normal, ~4 is weak).
  The v3 scores were assigned to that same scale deliberately so composites stay comparable across
  both passes. Real engagement rates are far lower and inversely correlated with follower count —
  never quote this column as a percentage outside the vault.

⚠️ **Reach figures are rough estimates** of total cross-platform following in millions,
compiled 2026-09-30. Verify before any external use.

## Files

| File | Role |
|---|---|
| `grassroots.py` | v1 generator — the 89 scored names, with notes |
| `grassroots.csv` | v1 data extract, consumed by `v2.py` |
| `v2.py` | merges the 89 with 148 new names; holds the `NEW` list |
| `v3.py` | current generator — same 237 names, formulas shortened via the `E11`/`F11` maxima |
| `v3.csv` | the payload uploaded to the v2 sheet |

Regenerate with `python3 v3.py` from this directory (it execs `v2.py`, which reads
`grassroots.csv`). Guards assert 237 / 89 / 148 and abort on a mismatch.
