# Advantage Rating — one-game MVP blueprint

**Status:** parked for later (saved 2026-09-05). Do not build until Norman approves.
**Related:** Drive deck [Advantage Rating - Model Summary](https://docs.google.com/presentation/d/10Lvu7xI1jaKYUHox18ifkFqOqD4NwT_qgmqm96tIJRk/edit) (Feb 25, 2025, for Genius Sports).

## Goal
From raw game film → one game of Advantage Rating outputs (events + points-per-advantage + create/use credit), good enough to validate the model. Not a league product.

## Strategy
Own the stack. Commercial upload tools (Kore, League Lens, etc.) are useful for box scores; they will not reliably implement Advantage Rating. Pipeline: film → court XY → Advantage Rating state machine on top.

## Input assumptions (v1)
- One full game, preferably **one continuous angle** (high sideline or basket-to-basket). Broadcast pans/cuts work but need more QA.
- Roster (jersey → name) + final box for sanity checks.
- Shot clock optional for v1.
- Scoring region defined in feet on a standard 94×50 court.

## Pipeline
```
Raw MP4(s)
  → ingest + cut dead time
  → YOLO detect players + ball
  → ByteTrack IDs
  → court keypoints → homography → (x_ft, y_ft) per ID / frame
  → jersey OCR / manual roster glue
  → possession segmentation
  → Advantage Rating engine (3 create rules + kill/use + credit chains 1–5)
  → CSV/JSON + QA overlay clips
```

## Phases / cost / time

| Step | What | Tools | $ (est.) | Calendar | Eng. time |
|------|------|-------|----------|----------|-----------|
| 0 Spec lock | Operationalize scoring region, 15 ft, 2nd defender, null-if-recovered | Doc | $0 | 0.5 day | 2–3 hrs |
| 1 Ingest | Normalize 1080p, split quarters, drop dead ball | ffmpeg, Drive | $0–5 | 0.5 day | 2–4 hrs |
| 2 Calibrate | Paint/baselines/baskets → H matrix | OpenCV + light UI | $0 | 0.5–1 day | 4–8 hrs |
| 3 Detect + track | Players + ball every frame | YOLOv8/v11 + ByteTrack | GPU **$15–60** | 1–2 days | 8–16 hrs |
| 4 Identity | Track ID → jersey → roster | OCR + manual fix | $0–10 | 1 day | 4–10 hrs |
| 5 Possession + events | Ball handler, FGA/TO/foul (hybrid CV + light tags) | Custom; optional Hudl Assist | $0 or ~$40–100 | 1–2 days | 8–14 hrs |
| 6 Advantage engine | State machine on XY stream (product IP) | Custom Python | $0 | 1–2 days | 10–16 hrs |
| 7 Output + QA | Tables + ~15 stamped clips; tune thresholds | pandas, overlays | GPU $5–15 | 1 day | 6–10 hrs |

**Cash for one game (DIY):** ~$20–90 compute (+ optional ~$55 Kore as parallel XY sanity check).
**Calendar:** ~1.5–3 weeks part-time, or ~5–8 focused days.
**Biggest risk:** ID swaps + pans breaking homography — not the Advantage math.

## Deliverables (game #1)
1. `advantage_events.csv` — start/end, creator, user(s), type 1–5, used/null, points, shot clock if available
2. `player_advantage_summary.csv` — created, used, PPA, null rate
3. `tracking.parquet` — frame-level XY (re-run rules without re-tracking)
4. QA pack — ~15 overlay clips
5. Method note — thresholds used

## Out of scope for v1
Multi-cam fusion, Hawk-Eye/Genius feeds, live in-game, perfect jersey OCR, coach UI before numbers look right on film.

## Next step when unpaused
Approve blueprint → Step 0 + **2–3 min sample clip** test (homography + tracks) → then full game GPU.

## Film-layer vendors (context only; not the core)
Kore, League Lens, Paloa, HoopIQ, Mixpeek, Anysports — upload film products. Prefer DIY XY for Advantage Rating; optionally compare one Kore match for sanity.
