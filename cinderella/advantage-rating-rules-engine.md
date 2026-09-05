# Advantage Rating — Rules Engine Spec (locked)

**Status:** Locked from Norman interview 2026-09-05 (+ clarifications same day).  
**Supersedes:** scoring-region default of ≤18 ft in older Step 0 drafts.  
**Sources:** Genius Sports Advantage Rating Model Summary deck + Norman decisions.  
**Downstream:** Google Sheet of YouTube links + scope (deferred until trial accuracy is OK).

## Plain definition
An **advantage** is a stretch where the **player with the ball** has compromised the defense. Off-ball players do **not** create advantages. It can start and end multiple times in one possession. Only **used** advantages count; if the defense **recovers** first, that advantage is **null**.

## Court / scoring region
- Court: NCAA/NBA **94 × 50 ft**; player foot XY in court feet.
- **Scoring region = inside the 3-point line** (locked).

## Ball-handler (hard gate)
- Create rules apply **only** to the current **ball-handler**.
- Creator = ball-handler at advantage start.
- If ball-handler is unknown, do **not** start an advantage.

## START (OR — any one, ball-handler only)
1. **15 ft auto-create:** Ball-handler within **15.0 ft** of the target rim.
2. **Second defender:** Ball-handler **inside the 3** AND at least **two defenders within ~6 ft** of the ball-handler.
3. **Closer to rim:** Ball-handler **inside the 3** AND closer to the rim than the nearest defender.

## END (OR)
1. **Recover:** Create conditions (1–3) are all false for **~1.0 second continuously** → advantage is **null**.
2. **Used:** Possession ends via **FGA**, **shooting foul**, or **turnover**.

## Credit (who)
- **Only the creator** (ball-handler who started it).

## Points (how much)
`credit = shot_point_value × (quality / 100)`

- **Shot point value:** 2 or 3 (or foul as 2/3).
- **Quality 0–100:** (1) distance to nearest defender, (2) small bump earlier in shot clock.
- **Misses still get** quality×points (expected points).
- **Shooting foul:** same as shot.
- **Turnover:** **0 points**, but still **used** (not null).

## Headline rating (locked)
**Advantage Rating = total creator credits ÷ number of used advantages** (points per advantage).

Applies to a player or a team (team = that team’s total creator credits ÷ that team’s used advantages). Also keep raw totals for transparency.

## Aggregations (sheet scopes — later)
| Scope | Output |
|-------|--------|
| One player | That player’s PPA (+ totals) |
| Every player on a team | Per-player PPA |
| Team total | Team PPA |
| Full game both teams | Per-player + both team PPAs |

## Non-goals for v1 engine
- Deck credit types 2–5 (finisher / swing chains)
- And-1 / technicals as separate types
- Perfect roster names (use best tracking IDs)

## Decision log
- 2026-09-05: Scoring region = inside 3pt; keep all three create rules.
- 2026-09-05: End = recover OR use; recover-before-use = null; recover ≈ 1s.
- 2026-09-05: Second defender = ≥2 defenders within ~6 ft.
- 2026-09-05: Credit = creator only; EP = quality×points even on miss; SF same; TO = 0 but used.
- 2026-09-05: Headline = **credits ÷ used advantages** (PPA).
- 2026-09-05: **Ball-handler only** — off-ball cannot create.
