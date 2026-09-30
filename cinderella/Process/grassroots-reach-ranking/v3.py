# -*- coding: utf-8 -*-
# v3: same 237 names as v2, but formulas reference helper maxima cells (E11/F11)
# instead of recomputing MAX() inline on every row. Cuts payload ~45%.
import csv, io, runpy, sys

src = open("v2.py", encoding="utf-8").read()
ns = {}
exec(src.split("first=14")[0], ns)          # reuse the row list from v2.py verbatim
rows = ns["rows"]; old = ns["old"]; added = ns["added"]

first = 14; last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["MAKING CINDERELLA — GRASSROOTS REACH RANKING (v2)"])
w.writerow(["Unfiltered. Global mega-reach names included. Judgment columns left blank on the new rows for Norman to score."])
w.writerow(["Reach figures are ROUGH ESTIMATES of total cross-platform following (millions), compiled 2026-09-30, current to roughly mid-2026. VERIFY before external use."])
w.writerow(["COMPOSITE stays blank until Eng_Pct, Cadence, Hoops and Avail are all filled. Rank ignores blanks."])
w.writerow(["WEIGHTS — edit column B; everything below re-sorts", "", "(must total 1.00)"])
for lab, val in [("Reach (log-scaled)", 0.20), ("Engagement rate", 0.25), ("Cadence / real-time", 0.25),
                 ("Basketball authenticity", 0.15), ("Availability to commit", 0.15)]:
    w.writerow([lab, val])
w.writerow(["TOTAL", "=SUM(B6:B10)", "<- must read 1", "column maxima >",
            f"=MAX(E{first}:E{last})", f"=MAX(F{first}:F{last})"])
w.writerow([])
w.writerow(["Rank", "Name", "Category", "COMPOSITE", "Reach_M", "Eng_Pct", "Cadence_1_10",
            "Hoops_1_10", "Avail_1_10", "Reach x Eng", "School_Tie", "Scored_By", "Notes"])
for i, r in enumerate(rows):
    x = first + i
    comp = (f'=IF(COUNT($F{x}:$I{x})<4,"",LOG10($E{x}+1)/LOG10($E$11+1)*10*$B$6'
            f'+$F{x}/$F$11*10*$B$7+$G{x}*$B$8+$H{x}*$B$9+$I{x}*$B$10)')
    w.writerow([f'=IF($D{x}="","",RANK($D{x},$D${first}:$D${last}))', r["Name"], r["Category"],
                comp, r["Reach"], r["Eng"], r["Cad"], r["Hoop"], r["Avail"],
                f'=IF(COUNT($E{x}:$F{x})<2,"",$E{x}*$F{x}/100)', r["Tie"], r["Scored"], r["Notes"]])
t = buf.getvalue()
open("v3.csv", "w", encoding="utf-8").write(t)
assert len(rows) == 237 and added == 148 and len(old) == 89
print(f"total {len(rows)} | scored {len(old)} | new {added} | rows {first}-{last} | {len(t):,} bytes")
