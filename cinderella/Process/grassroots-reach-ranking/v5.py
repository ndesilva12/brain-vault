# -*- coding: utf-8 -*-
"""v5: adds CONNECTIVITY — the ability to bring OTHER big names into the effort.

Connectivity is NOT "has famous friends." It is the product of four things:

  1. CONVENING POWER — do others actually show up to what they host? (Rubin's July 4th party,
     Kai Cenat's Mafiathon, Druski's Coulda Been, Ludwig's events)
  2. RECRUITMENT TRACK RECORD — have they demonstrably pulled A-list names into a VENTURE,
     not just a photo? (Reynolds at Wrexham, Jake Paul at MVP, Nadeshot at 100 Thieves)
  3. STRUCTURAL POSITION — are they a hub by profession? (agents, owners, WWE's head of
     talent, podcast hosts who interview everyone, producers whose art form IS collaboration)
  4. ⭐ WILLINGNESS TO SPEND SOCIAL CAPITAL — the decisive variable. Michael Jordan knows
     everyone and will ask no one. Rubin will make the call today. This is what separates a
     9 from a 3 among equally famous people.

A fifth, cheap form: COLLECTIVE MEMBERSHIP. Signing one member of 2HYPE, AMP, Barstool or
Sidemen brings the crew at near-zero marginal cost. Those names carry a floor of 7.

Scale:
  10  Repeatedly assembles other A-list names into ventures AND spends capital to do it
  8-9 Genuine hub (convener, or interviews/produces everyone) with proven pulls
  6-7 Well connected inside a lane, or brings a crew via a collective
  4-5 Ordinary celebrity network; no track record of assembling anyone
  1-3 Isolated, reclusive, or all access is gatekept through reps

Two derived columns:
  Reach x Eng          — audience quality (unchanged from v4)
  Connector Leverage   — Connect x Avail. Can reach others X would actually do it. This is the
                         single number that answers Norman's question.
"""
import csv, io

ns = {}
exec(open("v4.py", encoding="utf-8").read().split("added = 0")[0], ns)
rows, old, NEW = ns["rows"], ns["old"], ns["NEW"]
seen = {r["Name"] for r in rows}
added = 0
for n, c, r, e, cad, h, av, tie, note in NEW:
    if n in seen:
        continue
    seen.add(n); added += 1
    rows.append(dict(Name=n, Category=c, Reach=r, Eng=e, Cad=cad, Hoop=h, Avail=av,
                     Tie=tie or "—", Scored="Jimmy est.", Notes=note))

CONNECT = {
# 10 — the two genuine assemblers
"Michael Rubin":10,"Ryan Reynolds":10,
# 9 — hubs that convene and will spend the capital
"Mark Cuban":9,"Kai Cenat":9,"Druski":9,"DJ Khaled":9,"Snoop Dogg":9,"Jake Paul":9,
"Kevin Hart":9,"Jay-Z":9,"LeBron James":9,
# 8
"Joe Rogan":8,"Bill Simmons":8,"Triple H":8,"Gary Vaynerchuk":8,"Magic Johnson":8,
"Shaquille O'Neal":8,"Dave Portnoy":8,"Pat McAfee":8,"Alex Cooper":8,"IShowSpeed":8,
"MrBeast (Jimmy Donaldson)":8,"Stephen Curry":8,"Dwyane Wade":8,"Carmelo Anthony":8,
"Master P":8,"Ludwig":8,"Logan Paul":8,"KSI":8,"Sidemen (collective)":8,"Duke Dennis":8,
"Rob McElhenney":8,"Kevin Durant":8,"David Beckham":8,"Barack Obama":8,"Kim Kardashian":8,
# 7
"Jesser (Jesse Riedel)":7,"Cam Wilder":7,"Brandon Walker":7,"Cash Nasty (CashNasty)":7,
"Kris London":7,"Jiedel":7,"Mopi":7,"ZackTTG":7,"LSK (2HYPE)":7,"Nick Briz":7,
"Fanum":7,"Agent00":7,"Plaqueboymax":7,"Adin Ross":7,"Valkyrae":7,"FaZe Rug":7,
"Nadeshot (Matt Haag)":7,"Josh Richards":7,"Big Cat (Dan Katz)":7,"PFT Commenter":7,
"Jack Mac":7,"Trill Withers (Tyler)":7,"Caleb Pressley":7,"Will Compton":7,"Taylor Lewan":7,
"Shannon Sharpe":7,"Draymond Green":7,"Colin Cowherd":7,"Jomboy (Jimmy O'Brien)":7,
"Charles Barkley":7,"Jalen Brunson":7,"Josh Hart":7,"Baron Davis":7,"Serena Williams":7,
"Paige Bueckers":7,"Angel Reese":7,"Flau'jae Johnson":7,"Livvy Dunne":7,
"Theo Von":7,"Bert Kreischer":7,"Jelly Roll":7,"Post Malone":7,"Lil Yachty":7,
"Rick Ross":7,"Marshmello":7,"Tyler, the Creator":7,"Metro Boomin":7,"Diplo":7,
"Steve Aoki":7,"Drake":7,"Jamie Foxx":7,"Dwayne Johnson":7,"Jordan Lawley":7,
# 6
"FlightReacts":5,"Sketch":6,"Marcelas Howard":6,"The Professor (Grayson Boucher)":6,
"Tristan Jass":6,"Filayyyy":5,"Jynxzi":6,"Mark Rober":6,"Ryan Trahan":6,"Dude Perfect":6,
"Ninja":6,"Pokimane":6,"HasanAbi":6,"xQc":6,"YourRAGE":6,"ImDavisss":6,"Markiplier":5,
"Charli D'Amelio":6,"Alix Earle":6,"Kai Trump":6,"Bella Poarch":5,"Addison Rae":5,
"Bryce Hall":5,"Zach King":4,"Khaby Lame":4,"PewDiePie":4,
"Stephen A. Smith":7,"Jalen Rose":7,"Pat Beverley":6,"Paul George":6,"Skip Bayless":4,
"Chad Johnson":6,"Marshawn Lynch":6,"Deestroying (Donald De La Haye)":6,
"James Harden":6,"Russell Westbrook":6,"Jayson Tatum":6,"Devin Booker":6,"Jimmy Butler":6,
"Tyrese Haliburton":6,"Anthony Edwards":6,"Trae Young":6,"Allen Iverson":6,
"Vince Carter":6,"Tracy McGrady":6,"Caitlin Clark":6,"Sabrina Ionescu":6,"A'ja Wilson":6,
"JuJu Watkins":6,"Cameron Brink":6,"Naomi Osaka":6,"Mikey Williams":5,
"Giannis Antetokounmpo":5,"Luka Doncic":5,"Kyrie Irving":5,"Victor Wembanyama":5,
"Ja Morant":5,"Shai Gilgeous-Alexander":5,"Zion Williamson":4,"Scottie Pippen":5,
"Michael Jordan":3,"Larry Bird":2,
"John Cena":6,"Cody Rhodes":6,"Roman Reigns":5,"Rhea Ripley":5,"Bianca Belair":5,
"Jey Uso":5,"Conor McGregor":5,"Jon Jones":4,"Israel Adesanya":5,"Sean O'Malley":5,
"Tom Segura":6,"Bobby Lee":6,"Shane Gillis":6,"Andrew Schulz":6,"Matt Rife":5,
"Jack Whitehall":5,"Steve Harvey":6,"Adam Sandler":6,"Will Ferrell":6,"Mark Wahlberg":6,
"Will Smith":7,"Bill Murray":5,"Michael Keaton":3,"Vin Diesel":5,"Ludacris":6,"Nelly":6,
"Machine Gun Kelly":5,"Travis Scott":6,"Bad Bunny":6,"Jack Harlow":6,"Quavo":6,"Offset":6,
"2 Chainz":7,"Future":6,"21 Savage":5,"Lil Baby":6,"Gunna":5,"Playboi Carti":5,"Central Cee":5,
"Ice Spice":5,"Latto":5,"GloRilla":5,"Sexyy Red":5,"Megan Thee Stallion":6,"Cardi B":6,
"Nicki Minaj":6,"SZA":5,"Doja Cat":5,"Kendrick Lamar":5,"Dr. Dre":6,"The Weeknd":6,
"Morgan Wallen":6,"Zach Bryan":5,"Luke Combs":6,"Eric Church":5,"Brad Paisley":6,
"Bailey Zimmerman":5,"Shaboozey":5,"Beyonce":6,"Rihanna":6,"Jennifer Lopez":6,
"Selena Gomez":5,"Ariana Grande":5,"Justin Bieber":6,"Miley Cyrus":5,"Katy Perry":5,
"Billie Eilish":5,"Zendaya":5,"Taylor Swift":6,"Shakira":5,"Michelle Obama":6,
"Kylie Jenner":6,"Kendall Jenner":6,"Khloe Kardashian":5,"Elon Musk":5,
"Cristiano Ronaldo":6,"Lionel Messi":5,"Neymar":6,"Kylian Mbappe":5,"Virat Kohli":5,
"Tyler1":5,"Simone Biles":5,"Suni Lee":4,"Sydney McLaughlin":4,"Hailey Van Lith":5,
"Kamilla Cardoso":4,
}

NOTE_ADD = {
"Michael Rubin":"⭐⭐ THE most connected person in sports. Convening IS his product — the July 4th party alone puts 30 A-list names in one room. Reach is irrelevant; treat him as a distribution channel for names",
"Ryan Reynolds":"⭐⭐ Builds cap tables out of famous friends — Wrexham, Aviation, Mint. Exactly the skill MC needs. ⚠️ Also the reason he may decline: he already owns this format",
"Mark Cuban":"⭐⭐ Shark Tank alumni + NBA owners + founders, and he answers email himself",
"Kai Cenat":"⭐⭐ Mafiathon proved he can summon anyone — Hart, Nicki, Durant all appeared. Extraordinary convening for a 23-year-old",
"DJ Khaled":"⭐ His entire art form IS assembling other stars. Under-rated as a connector",
"Druski":"⭐ Coulda Been is a talent-assembly machine. Currently the connective tissue between rap, comedy and sports",
"Jake Paul":"⭐ MVP proves he assembles names into a VENTURE, not just a video",
"Triple H":"⭐ Runs WWE talent — he is not connected to a network, he IS one",
"Bill Simmons":"⭐ The Ringer is a network. Can put anyone in sports or Hollywood on a mic",
"Joe Rogan":"⭐ The single biggest gateway in podcasting; an appearance moves other bookings",
"Jay-Z":"⭐ Roc Nation is literally a network business — athletes and musicians on tap. ⚠️ Access is the whole problem",
"LeBron James":"⭐ SpringHill can move any athlete and most of Hollywood. ⚠️ Builds his own things first",
"Michael Jordan":"⚠️ Maximum authority, near-zero connective willingness. Knows everyone, asks no one",
"Larry Bird":"⚠️ The original Cinderella, and the least networked name on the list",
"Alex Cooper":"⭐ Unwell signs other creators — she has built a network, not just an audience",
"Gary Vaynerchuk":"⭐ Enormous rolodex and gives intros away for free",
"Ludwig":"⭐ Has produced events that pulled in dozens of creators — an operator with a rolodex",
"Nadeshot (Matt Haag)":"⭐ Built 100 Thieves by RECRUITING creators. Closest analog to what we need done",
"Kevin Durant":"⭐ Boardroom + 35V — he invests in sports ventures and knows every athlete",
"Allen Iverson":"⚠️ Model under-rates him. For a St. Joe's build, Philly access is worth more than the score says",
"Charles Barkley":"⭐ Inside the NBA means everyone takes his call. Social reach understates him badly",
}

for r in rows:
    r["Connect"] = CONNECT.get(r["Name"])
    assert r["Connect"] is not None, f"no connectivity score for {r['Name']}"
    if r["Name"] in NOTE_ADD:
        r["Notes"] = NOTE_ADD[r["Name"]]

# 2HYPE / AMP / Barstool / Sidemen members must never score below the collective floor
COLLECTIVE_FLOOR = ["Jesser (Jesse Riedel)","Cash Nasty (CashNasty)","Kris London","Jiedel",
                    "Mopi","ZackTTG","LSK (2HYPE)","Duke Dennis","Fanum","Agent00",
                    "Big Cat (Dan Katz)","PFT Commenter","Jack Mac","Brandon Walker",
                    "Trill Withers (Tyler)","Caleb Pressley","Sidemen (collective)","KSI"]
for r in rows:
    if r["Name"] in COLLECTIVE_FLOOR:
        assert r["Connect"] >= 7, f"{r['Name']} below collective floor"
for r in rows:
    assert 1 <= r["Connect"] <= 10, r["Name"]

first = 15; last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["MAKING CINDERELLA — GRASSROOTS REACH + CONNECTIVITY RANKING (v4)"])
w.writerow(["237 names. Adds CONNECT — the ability to bring OTHER big names in. Weighted equal-highest, because a connector is worth more than a standalone name."])
w.writerow(["⚠️ EVERY NUMBER IS AN ESTIMATE. Reach is rough cross-platform following in millions. Eng_Pct is an intensity score on a 0-11 band, NOT a literal percentage. Compiled 2026-09-30."])
w.writerow(["CONNECT 1-10 = convening power x recruitment track record x structural position x WILLINGNESS TO SPEND SOCIAL CAPITAL. That last factor is why Jordan is a 3 and Rubin is a 10."])
w.writerow(["WEIGHTS — edit column B; everything below re-sorts", "", "(must total 1.00)"])
for lab, val in [("Reach (log-scaled)", 0.15), ("Engagement rate", 0.20), ("Cadence / real-time", 0.20),
                 ("Basketball authenticity", 0.10), ("Availability to commit", 0.15),
                 ("⭐ Connectivity", 0.20)]:
    w.writerow([lab, val])
w.writerow(["TOTAL", "=SUM(B6:B11)", "<- must read 1", "column maxima >",
            f"=MAX(E{first}:E{last})", f"=MAX(F{first}:F{last})"])
w.writerow([])
w.writerow(["Rank", "Name", "Category", "COMPOSITE", "Reach_M", "Eng_Pct", "Cadence_1_10",
            "Hoops_1_10", "Avail_1_10", "CONNECT_1_10", "Reach x Eng", "Connector Leverage",
            "School_Tie", "Scored_By", "Notes"])
for i, r in enumerate(rows):
    x = first + i
    comp = (f'=IF(COUNT($F{x}:$J{x})<5,"",LOG10($E{x}+1)/LOG10($E$12+1)*10*$B$6'
            f'+$F{x}/$F$12*10*$B$7+$G{x}*$B$8+$H{x}*$B$9+$I{x}*$B$10+$J{x}*$B$11)')
    w.writerow([f'=IF($D{x}="","",RANK($D{x},$D${first}:$D${last}))', r["Name"], r["Category"],
                comp, r["Reach"], r["Eng"], r["Cad"], r["Hoop"], r["Avail"], r["Connect"],
                f'=IF(COUNT($E{x}:$F{x})<2,"",$E{x}*$F{x}/100)',
                f'=IF(COUNT($I{x}:$J{x})<2,"",$I{x}*$J{x})',
                r["Tie"], r["Scored"], r["Notes"]])
t = buf.getvalue()
open("v5.csv", "w", encoding="utf-8").write(t)
assert len(rows) == 237 and added == 148
print(f"total {len(rows)} | rows {first}-{last} | {len(t):,} bytes")
