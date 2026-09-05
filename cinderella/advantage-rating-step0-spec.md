# Advantage Rating — Step 0 operational spec

**Status:** film layer complete enough for rules work; **rules engine locked in** [advantage-rating-rules-engine.md](./advantage-rating-rules-engine.md) (Norman interview 2026-09-05).
**Sources:** [Advantage Rating - Model Summary](https://docs.google.com/presentation/d/10Lvu7xI1jaKYUHox18ifkFqOqD4NwT_qgmqm96tIJRk/edit) (Feb 25, 2025, Genius Sports); vault MVP blueprint.
**Not authoritative:** Drive `advantage_rating_files.zip` — simplified closer-to-basket only.

## Court frame
- Standard NCAA/NBA court: **94 ft × 50 ft**.
- Foot position = player XY after homography.

## Definition
An **advantage** is a time period where the defense is compromised while offense has the ball. Can begin/end multiple times inside one possession.

## Create rules (OR) — locked
While offensive player **P** has possession:
1. **Proximity:** P within **15.0 ft** of target rim.
2. **Second defender:** P **inside the 3-point line** AND ≥2 defenders within **~6 ft** of P.
3. **Closer-to-rim:** P **inside the 3-point line** AND closer to rim than nearest defender.

### Scoring region — locked
**Inside the 3-point line** (not ≤18 ft).

## Kill / end — locked
1. **Recover:** create conditions false for **~1.0 s continuously** → **null**.
2. **Used:** FGA, shooting foul, or turnover.

## Credit & points — locked
- Credit **creator only**.
- `credit = (2 or 3) × (quality/100)`; quality from nearest-defender distance + early shot-clock bump; **misses still count** (EP).
- Shooting foul: same as shot; turnover: 0 points but used.
- Team rating = **sum** of player creator credits.

See full spec: [advantage-rating-rules-engine.md](./advantage-rating-rules-engine.md).

## Film / tracking note (2026-09-05)
Broadcast Illini–MSU sample: Roboflow RF-DETR + BoT-SORT + appearance gallery. Tracking is fuel for rules; unique-ID metrics are directional. Details in film pipeline howto.
