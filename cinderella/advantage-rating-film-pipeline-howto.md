# Advantage Rating — Film Pipeline How-To (manual reproduce)

Plain-language notes for Norman. This is the DIY film → player tracks → court XY path we validated on a ~2.5 min Illinois–MSU broadcast cut. Full Advantage Rating rules are **not** in this sample yet.

## Where this ran

- **Jimmy's local Linux computer** ("my computer" / the Cursor box), **not** AWS/GCP GPU cloud.
- Device: **CPU only** (PyTorch CPU + YOLOv8n). No cloud GPU spend.
- Goal of the sample: prove ingest → detect/track → overlay → best-effort court XY, and document what fails on broadcast film.

## Stack

| Piece | Role |
|-------|------|
| Python venv (`.venv`) | Isolated deps under `/workspace/advantage-rating/.venv` |
| ffmpeg / yt-dlp | Download YT (or local) film and cut a 2–3 min clip |
| OpenCV (`cv2`) | Frames, resize, overlay draw, homography |
| PyTorch (CPU) | Backend for YOLO |
| Ultralytics YOLOv8n | Person detector (`yolov8n.pt`, COCO class 0 = person) |
| ByteTrack (+ `lap`) | Multi-object tracker (stable IDs across frames) |
| pandas / pyarrow | `tracks.csv` + `tracks.parquet` |

## Paths on Jimmy's computer

| What | Path |
|------|------|
| Sample clip | `/workspace/advantage-rating/sample/illini-msu-sample.mp4` |
| Tracking script (v1) | `/workspace/advantage-rating/sample-run/run_tracking.py` |
| v1 outputs | `/workspace/advantage-rating/sample-run/` |
| v2 outputs (tighter filters) | `/workspace/advantage-rating/sample-run-v2/` |
| Project venv | `/workspace/advantage-rating/.venv` |
| YOLO weights | `/workspace/yolov8n.pt` |

## What each program does (one line)

- **yt-dlp** — downloads YouTube (or other) game film to an MP4.
- **ffmpeg** — cuts a short window (e.g. 2–3 min) and can normalize resolution/fps.
- **YOLOv8n** — finds person boxes in each processed frame.
- **ByteTrack** — links boxes across frames into track IDs (needs the `lap` package).
- **OpenCV homography** — maps image foot-points → court feet (94×50) from a few painted keypoints.
- **`run_tracking.py`** — orchestrates detect → track → ROI/size filters → CSV/Parquet → overlay MP4 + JPEGs + metrics.
- **pandas/pyarrow** — store and analyze per-detection rows.

## End-to-end: reproduce manually someday

1. **Get film** — Prefer continuous high-sideline or basket-to-basket. Broadcast YT is OK for a smoke test; expect worse ID stability.
2. **Cut 2–3 minutes** — `ffmpeg -ss 00:10:00 -i game.mp4 -t 00:02:30 -c copy sample.mp4`
3. **Install deps once** — Python venv + `ultralytics`, `opencv-python-headless`, `pandas`, `pyarrow`, `lap`, `torch`, `torchvision`.
4. **Calibrate court** — Click ~4–6 paint/baseline keypoints; `cv2.findHomography` → `H.npy`. One static H does not survive big pans.
5. **Run tracking** — ~10 fps effective, resize ~960 wide, person-only, conf ≈ 0.5, CPU is fine for a short clip.
6. **Inspect** — Watch `overlay.mp4` and `frames/`; check unique ID count and short-track %.
7. **Interpret FAIL modes** — Broadcast pans + crowd = ID churn. Continuous fixed camera + jersey/team color ReID is the real path to Advantage Rating.

## Why broadcast YouTube fails ID stability

Half-court cuts, zooms, crowd/bench in frame, refs, and players leaving frame force ByteTrack to mint new IDs. Filters (court trapezoid, min box size, higher conf) help but do not fix appearance ReID. A fixed sideline camera is the right input for Advantage Rating v1.

## If doing full games later

- Optional cheap GPU (RunPod/Lambda/etc.) for full-game YOLO — not required for 2–3 min samples.
- Prefer your own film over network broadcast.
- Next software layer: team color / jersey ReID, per-possession or multi-pose homography, then the Advantage state machine (Step 0 spec).

## Related vault docs

- [advantage-rating-step0-spec.md](./advantage-rating-step0-spec.md)
- [advantage-rating-mvp-blueprint.md](./advantage-rating-mvp-blueprint.md)
