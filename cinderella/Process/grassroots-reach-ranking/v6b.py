# -*- coding: utf-8 -*-
"""v6b: compact upload CSV for the MC 237 ranked by SHARE VELOCITY."""
import csv, io
ns = {}
exec(open("v6.py", encoding="utf-8").read().split("# write the vault CSV")[0], ns)
rows = ns["rows"]
rows.sort(key=lambda r: (-r["Vel"], -r["Share"], -float(r["Reach"])))
first = 9
last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["MAKING CINDERELLA — GRASSROOTS TARGETS RANKED BY SHARE VELOCITY (v5)"])
w.writerow(["Re-ranked on SHARING. Shares are the only metric that produces NEW audience — likes and comments come from people who already follow you; a share lands in a stranger's feed."])
w.writerow(["⚠️ SHARE IS A MODEL, NOT MEASURED DATA. Retweets are public on X and TikTok shows shares, but Instagram sends and YouTube shares are creator-only analytics. SHARE is estimated from format, clip economy, emotional trigger, platform mix, participation and earned media."])
w.writerow(["VELOCITY = SHARE x Cadence. Rate x volume = total distributed reach: a modest account posting daily shareable content out-distributes a mega-account posting weekly."])
w.writerow(["⭐ Reach is now nearly irrelevant. Brandon Walker at 1M ties Kai Cenat at 40M. Share-weighting collapses the price/performance gap — distribution is buyable far cheaper than the reach list implied."])
w.writerow(["⚠️ Connect and Avail are carried over for cross-reference. The best CONNECTORS are the worst SHARERS (Curry, Rubin, Reynolds, Iverson) — connector, share engine and celebrity lead are three different jobs needing three different casts."])
w.writerow([])
w.writerow(["Rank","Name","Category","SHARE_1_10","Cadence_1_10","VELOCITY","Reach_M",
            "Connect_1_10","Avail_1_10","Hoops_1_10","School_Tie","Notes"])
for i, r in enumerate(rows):
    x = first + i
    w.writerow([f"=RANK(F{x},F${first}:F${last})", r["Name"], r["Category"], r["Share"], r["Cad"],
                f"=D{x}*E{x}", r["Reach"], r["Connect"], r["Avail"], r["Hoop"], r["Tie"],
                (r["Notes"] if r["Notes"][:1] in ("\u2b50","\u26a0") else "")])
t = buf.getvalue()
open("v6b.csv","w",encoding="utf-8").write(t)
print(f"rows {len(rows)} | data {first}-{last} | {len(t):,} bytes")
