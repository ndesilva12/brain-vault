# Advantage Rating — Rules Engine Spec (locked)

**Status:** Revised 2026-09-05 after Norman hand-review of ILL–MSU sample events.  
**Sources:** Genius Sports deck + Norman interview + Events sheet annotations.

## Plain definition
An **advantage** is a stretch where the **ball-handler** has compromised the defense. Off-ball players do not create. Advantages can start/end multiple times in a possession.

## Film gate (hard)
Score **only live game action** from the **sideline / elevated sideline** camera.  
If the **camera angle changes**, treat as **replay / non-live** → **do not log** advantages.  
(Broadcast cutaways and replays caused most false positives on the ILL–MSU sample.)

## Scoring region
**Inside the 3-point line.**

## START (OR — ball-handler only)
1. Within **15 ft** of rim.  
2. Inside the 3 AND ≥2 defenders within **~6 ft**.  
3. Inside the 3 AND closer to rim than nearest defender.  

Multiple create reasons in the same continuous advantage = **one creation** (do not split duplicates).

## END
1. **Recover:** create conditions false for **~1.0 s continuous**.  
2. **Used:** FGA, shooting foul, or turnover (by anyone on that advantage chain as defined below).

## Two ledgers (do not mix)

### A) Raw creation ability
Every valid create (including ones that **never get used**) increments **creations**.  
Unused creates: **creation credit only** — **$0** toward Advantage Rating.

### B) Advantage Rating (headline)
Only **used** advantages contribute points to the rating.  
**Divisor = number of used advantages** (not total creations).

`Rating = rating_points ÷ used_advantages`

## How rating_points are computed on a USED advantage

### Case 1 — Creator uses it themselves
(shot, shooting foul, or turnover by the creator)

Use **actual scored points**: **3 / 2 / 1 / 0**  
- Include free throws made from that shooting foul.  
- Turnover → **0**.  
- **Do not** apply shot-quality scaling in this case.

### Case 2 — Creator passes; teammate **immediately** uses
Use **expected points**:  
`rating_points = (2 or 3) × (quality / 100)`  
Quality 0–100 from nearest-defender distance + small early shot-clock bump.  
Misses still get EP in this pass-off case.

### Case 3 — Created but never used (recover / dead)
- Counts in **creations**  
- **$0** rating_points; **excluded** from used_advantages divisor

## Credit identity
Creator = ball-handler at create. Roster jersey preferred over anonymous track IDs.

## Team rollup
Same formulas at team level: team rating_points ÷ team used_advantages; also report raw creations.

## ILL–MSU sample lessons (2026-09-05)
- Majority of auto events were **replay / non-gameplay** after camera cuts.  
- Many false creates: wrong BH, not actually ≤15 ft / closer-to-rim.  
- Duplicate splits of one real advantage.  
- Quality sometimes too high on poor shots.

## Decision log
- 2026-09-05: Inside 3; create OR×3; BH-only; recover ~1s.  
- 2026-09-05: **Creation ≠ rating**; unused create ≠ divisor.  
- 2026-09-05: Self-use = **actual points**; pass-then-use = **quality×points**.  
- 2026-09-05: **Live sideline cam only**; ignore angle-change replays.
