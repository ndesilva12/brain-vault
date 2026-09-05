# Advantage Rating — Rules Engine Spec (locked)

**Status:** Locked from Norman interview 2026-09-05 (America/New_York).  
**Supersedes:** scoring-region default of ≤18 ft in Step 0.  
**Sources:** Genius Sports Advantage Rating Model Summary deck + Norman decisions below.  
**Downstream:** Google Sheet of YouTube links + scope (player / team roster / team total / full game).

## Plain definition
An **advantage** is a stretch where the offense has the ball and the defense is compromised. It can start and end multiple times in one possession. Only **used** advantages count; if the defense **recovers** first, that advantage is **null**.

## Court / scoring region
- Court: NCAA/NBA **94 × 50 ft**; player foot XY in court feet.
- **Scoring region = inside the 3-point line** (locked).

## START (OR — any one, while offense has possession)
1. **15 ft auto-create:** Ball-handler within **15.0 ft** of the target rim.
2. **Second defender:** Ball-handler **inside the 3** AND at least **two defenders within ~6 ft** of the ball-handler.
3. **Closer to rim:** Ball-handler **inside the 3** AND closer to the rim than the nearest defender.

## END (OR)
1. **Recover:** Create conditions (1–3) are all false for **~1.0 second continuously** → advantage is **null** (does not count).
2. **Used:** Possession ends via **FGA**, **shooting foul**, or **turnover**.

## Credit (who)
- **Only the creator** gets credit (not finisher / multi-pass chain types for this product version).

## Points (how much)
Creator credit is **expected-points style**:

`credit = shot_point_value × (quality / 100)`

- **Shot point value:** 2 or 3 from shot location (or foul as 2/3).
- **Quality 0–100** from objective factors only:
  1. Distance to nearest defender (more open → higher)
  2. Small bump earlier in the shot clock
- **Misses still get** `quality × points` (not zero).
- **Shooting foul:** same formula as a shot (2 or 3 × quality/100).
- **Turnover:** **0 points**, but still **used** (counts in denominator / event list; not null).

Exact quality curve (mapping defender-ft + clock → 0–100) is an implementation detail; keep monotonic: farther defender and earlier clock → higher quality.

## Aggregations (sheet scopes)
| Scope | Output |
|-------|--------|
| One player | That player’s sum of creator credits (used advantages only) |
| Every player on a team | Per-player creator sums for that roster |
| Team total | **Sum** of each player’s creator expected-points on that team |
| Full game both teams | Per-player + both team totals |

Optional rate metrics later: points per advantage, per 100 possessions — not required to start coding.

## Non-goals for v1 engine
- Deck credit types 2–5 (finisher / swing chains)
- And-1 / technical free throws as separate point types
- Perfect jersey OCR / true roster ID (use best available identity from tracking)

## Implementation order
1. Apply rules on tracked XY + ball-handler + team labels on sample clip wide stretches.
2. Spot-check create/kill vs film.
3. Quality function v1 from defender distance + shot clock.
4. Sheet intake: YouTube URL + scope → run → write results.

## Decision log
- 2026-09-05: Scoring region = inside 3pt.
- 2026-09-05: Keep all three create rules.
- 2026-09-05: End = recover OR use; recover-before-use = null.
- 2026-09-05: Second defender = ≥2 defenders within ~6 ft.
- 2026-09-05: Credit = creator only; EP = quality×points even on miss; SF same; TO = 0 but used.
- 2026-09-05: Team = sum of player creator credits.
- 2026-09-05: Recover window ≈ 1 second continuous.
