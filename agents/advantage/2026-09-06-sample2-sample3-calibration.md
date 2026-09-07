# 2026-09-06 — Sample2/Sample3 calibration status

## Locked rules (Norman, unchanged)
- Ball-handler only can create
- Scoring region = inside the 3
- Create OR: ≤15 ft rim · OR ≥2 defenders within ~6 ft inside 3 · OR closer-to-rim than nearest D inside 3
- Unused recover ~1s = creation credit only (not in PPA divisor)
- Self-use = actual points (no quality mult)
- Pass-off = (2|3) × (quality/100)
- Rating = rating_points ÷ used advantages
- Live sideline / elevated-sideline only; camera-angle≈replay → ignore

## Film windows (YT `Or0nrNcjQvU`)
| Sample | YT window | Role |
|--------|-----------|------|
| sample1 | 10:00–12:30 | Norman gold + Events / Events_v4 |
| sample2 | 25:00–27:30 | Hand-scored after cold run; training set |
| sample3 | 35:00–37:30 | Cold transfer test — **failed Norman review** |

Sheets: Events workbook `14r-JLuB6G8YpUPtt0gy-0q3FKNv_EzLpoonwmNCXxo0` (tabs include Events, Events_v4, Events_sample2_cold, Events_sample2_pass6, Events_sample3_cold).

## Sample2 path (organic passes)
- Cold under-fired (2 events) → live-gate starved
- Passes 1–6 toward Norman gold (5 REAL + 2 NOTHING FPs)
- **Pass6** hit recall 5/5 and SF→1 / pass-off 2.7 on sample2
- Prematurely copied to `rules-engine-v4-locked/` and sheet `Events_sample2_pass6`

## Failure: sample3 + overfitting
Norman: sample3 output “not even close” / nonsensical.

**Root cause:** pass6/locked engine hard-coded **clip-time** hacks tuned to sample2 gold clocks, e.g.:
- HQ pass-off 2.7 only if `t_start ∈ [120, 136]`
- Early paint_catch persist for `t < 40`
- Late paint_catch / prox15 cuts at `t ≥ 125`
- Merge guards shaped around sample2 windows [16–18] vs [19–21]

Those are not general rules. Sample2 5/5 was not transferable. Locking pass6 was a mistake.

## Stack (box)
- Tracking: Roboflow RF-DETR `basketball-player-detection-3-ycjdo/13` + BoT-SORT (`sample*-run-v5b/`)
- Engine: Python `advantage_rules_v4*.py` in `.venv/`
- Prefer organic detection over gold inject/snap/anchors
- Check-in after every 1–2 engine passes; no unlimited chase

## Next (agreed direction)
1. **Decontaminate** engine — strip time-anchored sample2 hacks; keep general create/use/live-gate/SF heuristics only
2. Re-run **sample3 cold** on decontaminated eng (expect uglier, more honest output)
3. Norman hand-scores that before more tuning
4. Do **not** treat `rules-engine-v4-locked` (=pass6) as production baseline until it generalizes

## Paths (box)
- Work: `/workspace/advantage-rating/`
- Sample2 gold JSON: `norman_gold_events_sample2.json`
- Pass6 / false lock: `rules-engine-v4-sample2-pass6/`, `rules-engine-v4-locked/`
- Sample3 cold (rejected): `rules-engine-v4-sample3-cold/`, clip `sample3/`
