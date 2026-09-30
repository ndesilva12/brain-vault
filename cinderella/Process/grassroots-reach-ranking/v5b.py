# -*- coding: utf-8 -*-
"""v5b: compact CONNECTIVITY sheet.

v5.py builds the full 237-row merged sheet (reach + engagement + cadence + hoops + avail +
connect), but that payload is ~87KB and too large to upload in one call. This emits just the
connectivity layer, pre-sorted by Connector Leverage, so it is useful standalone AND can be
pasted into the master sheet as columns.

Rows are sorted DESC by Connector Leverage (Connect x Avail) — the number that answers
"who can bring other big names in AND would actually do it."
"""
import csv, io

ns = {}
exec(open("v5.py", encoding="utf-8").read().split("first = 15")[0], ns)
rows = ns["rows"]

for r in rows:
    r["Lev"] = r["Connect"] * float(r["Avail"])
rows.sort(key=lambda r: (-r["Lev"], -r["Connect"], -float(r["Reach"])))

# keep notes only where they carry connectivity signal
KEEP = set(ns["NOTE_ADD"])
first = 12
last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["MAKING CINDERELLA — CONNECTIVITY (v1)"])
w.writerow(["Who can bring OTHER big names into the effort. Companion to the Reach Ranking sheet — paste columns D-F in there to fold connectivity into that composite."])
w.writerow(["⚠️ ESTIMATES. CONNECT is 1-10: convening power x recruitment track record x structural position x WILLINGNESS TO SPEND SOCIAL CAPITAL."])
w.writerow(["That last factor decides it. Michael Jordan knows everyone and will ask no one (3). Michael Rubin will make the call today (10)."])
w.writerow(["⭐ SORTED BY LEVERAGE = CONNECT x AVAIL. Sort by CONNECT alone to see raw network; by LEVERAGE to see who is actually gettable."])
w.writerow(["Collective members (2HYPE, AMP, Barstool, Sidemen) carry a floor of 7 — signing one brings the crew at near-zero marginal cost."])
w.writerow([])
w.writerow(["SCALE", "10", "Repeatedly assembles A-list names into ventures AND spends capital doing it"])
w.writerow(["", "8-9", "Genuine hub — convener, or produces/interviews everyone — with proven pulls"])
w.writerow(["", "6-7", "Well connected inside a lane, or brings a crew via a collective"])
w.writerow(["", "4-5", "Ordinary celebrity network; no track record of assembling anyone"])
w.writerow(["", "1-3", "Isolated or reclusive; all access gatekept through reps"])
w.writerow([])
w.writerow(["Rank", "Name", "Category", "CONNECT_1_10", "Avail_1_10", "LEVERAGE",
            "Reach_M", "School_Tie", "Why"])
for i, r in enumerate(rows):
    x = 15 + i  # 13 rows of header block, header row at 14, data starts at 15
    # every row is scored, so the blank-guards from earlier versions are dead weight —
    # dropping them roughly halves the upload payload
    w.writerow([f'=RANK(F{x},F$15:F${14+len(rows)})',
                r["Name"], r["Category"], r["Connect"], r["Avail"],
                f'=D{x}*E{x}',
                r["Reach"], r["Tie"], ns["NOTE_ADD"].get(r["Name"], "")])
t = buf.getvalue()
open("v5b.csv", "w", encoding="utf-8").write(t)
print(f"rows {len(rows)} | data 15-{14+len(rows)} | {len(t):,} bytes")
print("top 12 by leverage:")
for r in rows[:12]:
    print(f"  lev {int(r['Lev']):3d}  conn {r['Connect']:2d}  avail {int(float(r['Avail'])):2d}  {r['Name']}")
