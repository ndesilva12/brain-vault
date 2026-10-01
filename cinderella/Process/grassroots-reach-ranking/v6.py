# -*- coding: utf-8 -*-
"""v6: re-rank all 237 names on SHARING, per the specialist input that shares are the metric
that matters.

⚠️ HONESTY NOTE: share counts are not publicly observable for most platforms. Retweets are
public on X and TikTok displays shares, but Instagram sends and YouTube shares are
creator-only analytics. So SHARE below is an ESTIMATE from observable predictors, not
measured data. It is a model. Labelled as such everywhere it appears.

Predictors used, in order of weight:

1. FORMAT. Short vertical video and single-image/text posts get shared; long-form and
   livestreams structurally cannot be. ⭐ This is the single biggest reordering factor — you
   cannot share a six-hour stream, so stream-native creators collapse on own-share even with
   enormous live audiences.
2. CLIP ECONOMY. Third-party accounts reposting their moments. This RESCUES some streamers:
   Speed and Kai Cenat barely share their own content but thousands of clip accounts do it
   for them, which counts as distribution.
3. EMOTIONAL TRIGGER. Outrage, awe, humor and tribal identity get shared. Competence,
   lifestyle and aspiration do not.
4. PLATFORM MIX. X and TikTok are share-native; Reels moderate; YouTube long-form weak.
5. PARTICIPATION. Does the content invite duet / stitch / remix / quote-tweet.
6. EARNED MEDIA. Does a post become an article that then gets shared again.

Two columns:
  SHARE 1-10        — shareability of a single unit of their content
  SHARE VELOCITY    — SHARE x Cadence. Rate x volume = total distributed reach. A modest
                      account posting daily shareable content out-distributes a mega-account
                      posting weekly.
"""
import csv, io

ns = {}
exec(open("v5.py", encoding="utf-8").read().split("first = 15")[0], ns)
rows = ns["rows"]

SHARE = {
# 10 — engineered to be reposted; the content IS the share
"Druski":10,"Sketch":10,"IShowSpeed":10,
# 9
"Kai Cenat":9,"Theo Von":9,"Shannon Sharpe":9,"Dave Portnoy":9,"Cam Wilder":9,
"Caitlin Clark":9,"Angel Reese":9,"Deestroying (Donald De La Haye)":9,"Brandon Walker":9,
"Charles Barkley":9,"Stephen A. Smith":9,"Pat McAfee":9,
# 8
"FlightReacts":8,"Jesser (Jesse Riedel)":8,"Tristan Jass":8,"Duke Dennis":8,"Filayyyy":8,
"Cash Nasty (CashNasty)":8,"Marcelas Howard":8,"The Professor (Grayson Boucher)":8,
"Jake Paul":8,"Logan Paul":8,"Adin Ross":8,"Plaqueboymax":8,"Jynxzi":8,
"Draymond Green":8,"Pat Beverley":8,"Jalen Rose":8,"Big Cat (Dan Katz)":8,"PFT Commenter":8,
"Flau'jae Johnson":8,"Livvy Dunne":8,"Kevin Hart":8,"Andrew Schulz":8,"Shane Gillis":8,
"Bert Kreischer":8,"Tom Segura":8,"Matt Rife":8,"Joe Rogan":8,"Skip Bayless":8,
"Chad Johnson":8,"Caleb Pressley":8,"Jelly Roll":8,"Elon Musk":8,"Gillie Da Kid":8,
"Wallo267":8,
# 7
"Kris London":7,"Jiedel":7,"Mopi":7,"ZackTTG":7,"LSK (2HYPE)":7,"Nick Briz":7,
"Jordan Lawley":7,"ImDavisss":7,"Agent00":7,"Fanum":7,"YourRAGE":7,"Tyler1":7,
"Jack Mac":7,"Trill Withers (Tyler)":7,"Jomboy (Jimmy O'Brien)":7,"Colin Cowherd":7,
"Will Compton":7,"Taylor Lewan":7,"Bill Simmons":7,"Kirk Minihane":7,
"Snoop Dogg":7,"Shaquille O'Neal":7,"Master P":7,"Allen Iverson":7,"Magic Johnson":7,
"Ja Morant":7,"Anthony Edwards":7,"Tyrese Haliburton":7,"Victor Wembanyama":7,
"Kyrie Irving":7,"Russell Westbrook":7,"Trae Young":7,"Zion Williamson":7,
"Paige Bueckers":7,"JuJu Watkins":7,"Hailey Van Lith":7,"Cameron Brink":7,
"Sexyy Red":7,"GloRilla":7,"Cardi B":7,"Nicki Minaj":7,"Ice Spice":7,
"Bobby Lee":7,"Jack Whitehall":7,"Alex Cooper":7,"Ludwig":7,"HasanAbi":7,
"Mikey Williams":7,"Kai Trump":7,"Alix Earle":7,"Bryce Hall":7,"Mark Rober":7,
"Ryan Trahan":7,"Dude Perfect":7,"Marshawn Lynch":7,"Bam Margera":7,
# 6
"xQc":6,"Valkyrae":6,"Pokimane":6,"Ninja":6,"Markiplier":6,"FaZe Rug":6,"Sidemen (collective)":6,
"KSI":6,"MrBeast (Jimmy Donaldson)":6,"Nadeshot (Matt Haag)":6,"Josh Richards":6,
"Charli D'Amelio":6,"Bella Poarch":6,"Zach King":6,"Khaby Lame":6,"PewDiePie":6,
"Jayson Tatum":6,"Devin Booker":6,"Jimmy Butler":6,"James Harden":6,"Giannis Antetokounmpo":6,
"Luka Doncic":6,"Shai Gilgeous-Alexander":6,"Jalen Brunson":6,"Josh Hart":6,"Paul George":6,
"Kevin Durant":6,"Carmelo Anthony":6,"Dwyane Wade":6,"Scottie Pippen":6,"Tracy McGrady":6,
"Vince Carter":6,"Baron Davis":6,"A'ja Wilson":6,"Kamilla Cardoso":6,"Sabrina Ionescu":6,
"Simone Biles":6,"Naomi Osaka":6,"Serena Williams":6,"Suni Lee":6,"Sydney McLaughlin":6,
"Conor McGregor":6,"Jon Jones":6,"Israel Adesanya":6,"Sean O'Malley":6,
"Roman Reigns":6,"Cody Rhodes":6,"Rhea Ripley":6,"Bianca Belair":6,"Jey Uso":6,"Triple H":6,
"John Cena":6,"Steve Harvey":6,"Will Ferrell":6,"Adam Sandler":6,"Bill Murray":6,
"Michael Rubin":6,"Mark Cuban":6,"Gary Vaynerchuk":6,"Rob McElhenney":6,"Ryan Reynolds":6,
"Lil Yachty":6,"Jack Harlow":6,"2 Chainz":6,"Quavo":6,"Offset":6,"Rick Ross":6,
"Megan Thee Stallion":6,"Latto":6,"DJ Khaled":6,"Lil Baby":6,"Gunna":6,"Playboi Carti":6,
"Central Cee":6,"21 Savage":6,"Future":6,"Metro Boomin":6,"Shaboozey":6,"Morgan Wallen":6,
"Machine Gun Kelly":6,"Travis Scott":6,"Bad Bunny":6,"Tyler, the Creator":6,"Doja Cat":6,
"SZA":6,"Jamie Foxx":6,"Ludacris":6,"Nelly":6,"Post Malone":6,"Luke Combs":6,
"Zach Bryan":6,"Bailey Zimmerman":6,"Brad Paisley":6,"Eric Church":6,"Jay-Z":6,
"Taylor Swift":6,"Justin Bieber":6,"Cristiano Ronaldo":6,"Neymar":6,"Kylian Mbappe":6,
"Lionel Messi":6,"Virat Kohli":6,"David Beckham":6,"Barack Obama":6,"Michelle Obama":6,
"Drake":6,"LeBron James":6,"Stephen Curry":6,"Steve Aoki":6,"Diplo":6,"Marshmello":6,
"Dr. Dre":6,"Kendrick Lamar":6,"The Weeknd":6,"Rihanna":6,"Beyonce":6,"Will Smith":6,
"Dwayne Johnson":6,"Mark Wahlberg":6,"Addison Rae":6,"Josh Hart ":6,
# 5 and below — polished, aspirational or inert; shared rarely relative to size
"Kylie Jenner":5,"Kendall Jenner":5,"Khloe Kardashian":5,"Kim Kardashian":5,
"Selena Gomez":5,"Ariana Grande":5,"Miley Cyrus":5,"Katy Perry":5,"Billie Eilish":5,
"Zendaya":5,"Shakira":5,"Jennifer Lopez":5,"Vin Diesel":5,"Michael Keaton":4,
"Michael Jordan":4,"Larry Bird":4,
}

missing = [r["Name"] for r in rows if r["Name"] not in SHARE]
assert not missing, f"no SHARE score for: {missing}"

for r in rows:
    r["Share"] = SHARE[r["Name"]]
    r["Vel"] = r["Share"] * float(r["Cad"])
    assert 1 <= r["Share"] <= 10, r["Name"]

# write the vault CSV
rows_sorted = sorted(rows, key=lambda r: (-r["Vel"], -r["Share"], -float(r["Reach"])))
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["Rank", "Name", "Category", "SHARE_1_10", "Cadence_1_10", "SHARE_VELOCITY",
            "Reach_M", "Connect_1_10", "Avail_1_10", "School_Tie"])
for i, r in enumerate(rows_sorted, 1):
    w.writerow([i, r["Name"], r["Category"], r["Share"], r["Cad"], int(r["Vel"]),
                r["Reach"], r["Connect"], r["Avail"], r["Tie"]])
open("v6-shares.csv", "w", encoding="utf-8").write(buf.getvalue())

print(f"{len(rows)} scored\n")
print("=== TOP 40 BY SHARE VELOCITY (share x cadence) ===")
for i, r in enumerate(rows_sorted[:40], 1):
    print(f"{i:3d} vel {int(r['Vel']):3d}  share {r['Share']:2d}  cad {int(float(r['Cad'])):2d}  "
          f"reach {str(r['Reach']):>4}M  {r['Name']}")

# biggest movers against the old reach-weighted composite
import math
W = dict(reach=.15, eng=.20, cad=.20, hoop=.10, avail=.15, conn=.20)
mR = max(float(r["Reach"]) for r in rows); mE = max(float(r["Eng"]) for r in rows)
for r in rows:
    r["Old"] = (math.log10(float(r["Reach"])+1)/math.log10(mR+1)*10*W["reach"]
                + float(r["Eng"])/mE*10*W["eng"] + float(r["Cad"])*W["cad"]
                + float(r["Hoop"])*W["hoop"] + float(r["Avail"])*W["avail"]
                + r["Connect"]*W["conn"])
old_rank = {r["Name"]: i for i, r in enumerate(sorted(rows, key=lambda z: -z["Old"]), 1)}
new_rank = {r["Name"]: i for i, r in enumerate(rows_sorted, 1)}
delta = sorted(rows, key=lambda r: old_rank[r["Name"]] - new_rank[r["Name"]])
print("\n=== BIGGEST FALLERS (old rank -> new) ===")
for r in delta[:12]:
    print(f"  {old_rank[r['Name']]:3d} -> {new_rank[r['Name']]:3d}  {r['Name']}")
print("\n=== BIGGEST RISERS ===")
for r in delta[-12:][::-1]:
    print(f"  {old_rank[r['Name']]:3d} -> {new_rank[r['Name']]:3d}  {r['Name']}")
