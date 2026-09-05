# Advantage Rating — Step 0 operational spec

**Status:** locked for MVP sample (2026-09-05), pending Norman confirm on scoring-region geometry.
**Sources:** [Advantage Rating - Model Summary](https://docs.google.com/presentation/d/10Lvu7xI1jaKYUHox18ifkFqOqD4NwT_qgmqm96tIJRk/edit) (Feb 25, 2025, Genius Sports); vault MVP blueprint.
**Not authoritative:** Drive `advantage_rating_files.zip` (Feb 2026 prototype) — simplified closer-to-basket than defender only; missing 15 ft auto-create, scoring region, second-defender engage, credit types 1–5, and points-per-advantage. Treat as XY/pipeline reference only.

## Court frame
- Standard NCAA/NBA court: **94 ft × 50 ft**.
- Coordinates: basket at `(0, 25)` for the active half (or dual baskets at `x=0` and `x=94`, y midline `25`). Foot position = player XY.
- Homography maps image feet → court feet before any rule fires.

## Definition
An **advantage** is a time period where the defense is compromised: offense has the ball with a more favorable court position than the defense.

Advantages can begin/end **multiple times** (or never) inside one possession.

## Create rules (OR — any one starts an advantage)
While offensive player **P** has physical possession:

1. **Proximity auto-create:** P is within **15.0 ft** of the target rim center. *(Automatic.)*
2. **Second-defender engage:** P engages a **second defender** while at or inside the **scoring region**.
3. **Closer-to-rim in scoring region:** P is **closer to the rim** than the nearest defender **and** P is inside the scoring region.

### Scoring region (v1 proposal — confirm)
Deck names scoring region but does not publish exact feet. **v1 default for code:**
- Any offensive XY with **distance(rim) ≤ 18 ft** (approx. lane + short midrange).

**Open question for Norman:** exact polygon (paint only? 3pt arc? custom drawing from deck diagrams). Until answered, MVP uses **distance(rim) ≤ 18 ft**.

### Second defender (v1 operational)
- Defenders ranked by distance to **P** (not to rim).
- Engaging a second defender = at least **two** defenders within **6.0 ft** of P, OR one within **3.0 ft** and a second within **8.0 ft** while P is driving/attacking (velocity toward rim > threshold).
- v1 sample clip will flag frames; thresholds tune after QA.

## Kill / end rules (OR)
An active advantage **ends** when either:

1. **Defense recovers:** create conditions no longer true for a sustained **N = 8 frames** (~0.27s @ 30fps); or
2. **Advantage used:** possession ends via **FGA, shooting foul, or turnover**.

If the defense recovers **before** a terminal event → advantage is **null** (does **not** count toward rating).

If the advantage leads to end of possession → count **points rendered** (0–3) toward **points per advantage**.

## Credit chain types (deck 1–5)
| Type | Pattern |
|------|---------|
| 1 | A creates and uses |
| 2 | A creates; B uses (catch & shoot / finish / lob) |
| 3 | A creates; B inherits and re-creates/re-engages before using |
| 4 | A creates; B continues; C uses (one-more / swing / extra pass) |
| 5 | A creates; B re-creates; C inherits and uses |

## Metrics
- Was advantage created? / Who created?
- Recovered vs used
- If used: shot quality (v1: 2pt/3pt by XY), shot clock if available, who used, points
- Points per advantage (and per 100 advantages)
- Null advantages excluded from rating as deck specifies

## Sample-clip test scope
Prove film layer (not full Advantage engine yet):
1. Ingest 2–3 min clip
2. YOLO players + ByteTrack
3. Court keypoints → homography → (x_ft, y_ft)
4. Overlay: tracks + rim + 15 ft circle + scoring region
5. Manual 10-frame spot-check

**Pass criteria:** stable IDs for ≥70% of clip without catastrophic swaps; XY within ~2 ft on painted landmarks after calibration.

## Film source
- Sample: YouTube Illinois vs Michigan State (Jan 25, 2026) full replay `Or0nrNcjQvU`; cut ~10:00–12:30 for tracking test.

## Decision log
- 2026-09-05: Norman approved Step 0 + sample-clip test.
- Scoring region geometry: **proposed 18 ft radius** until Norman overrides.
- 2026-09-05: Chose Illinois–MSU YT full replay as sample film.
