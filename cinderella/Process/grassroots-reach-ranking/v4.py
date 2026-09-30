# -*- coding: utf-8 -*-
"""v4: fills Eng_Pct / Cadence / Hoops / Avail for the 148 names added in v2.

Scale is inherited from the v1 rows so the composite stays comparable — Eng_Pct is an
engagement-INTENSITY score on the same 0-11 band Jimmy used (IShowSpeed 11 is the ceiling,
~6 is normal, ~4 is weak), not a literal engagement percentage. Cadence / Hoops / Avail
are 1-10. All 237 rows are now scored; Scored_By stays 'Jimmy est.' throughout because
every number in the sheet is an estimate.
"""
import csv, io

old = list(csv.DictReader(open("grassroots.csv", encoding="utf-8")))
rows = [dict(Name=r["Name"], Category=r["Category"], Reach=r["Reach_M"], Eng=r["Engagement_Pct"],
             Cad=r["Cadence_1_10"], Hoop=r["Hoops_Auth_1_10"], Avail=r["Availability_1_10"],
             Tie=r["School_Tie"], Scored="Jimmy est.", Notes=r["Notes"]) for r in old]
seen = {r["Name"] for r in rows}

# name: (reach_M, category, eng, cadence, hoops, avail, school_tie, note)
NEW = [
("Cristiano Ronaldo","Global athlete",1000,4.0,7,1,1,"","Largest following on earth and almost none of it is addressable for us. No hoops, no availability"),
("Lionel Messi","Global athlete",700,4.0,5,1,1,"",""),
("Selena Gomez","Global celebrity",500,4.0,6,1,2,"",""),
("Kylie Jenner","Global celebrity",450,4.0,7,1,2,"",""),
("Ariana Grande","Global celebrity",450,4.0,5,1,2,"",""),
("Kim Kardashian","Global celebrity",420,4.0,7,3,2,"","Courtside presence, no basketball substance"),
("Taylor Swift","Global celebrity",400,5.0,4,2,1,"","The NFL halo proves the mechanism works. Availability is effectively zero"),
("Justin Bieber","Global celebrity",380,4.5,6,7,3,"","Genuine hoops fan who actually plays — better fit than the reach alone suggests"),
("Beyonce","Global celebrity",350,4.5,3,3,1,"LIU (vault)","Vault pairing via Jay-Z. Realistically unreachable"),
("Neymar","Global athlete",300,4.5,8,1,2,"",""),
("Khloe Kardashian","Global celebrity",300,3.5,7,3,3,"",""),
("Kendall Jenner","Global celebrity",290,3.5,6,4,2,"",""),
("Virat Kohli","Global athlete",280,4.5,6,1,1,"",""),
("Jennifer Lopez","Global celebrity",280,3.5,6,1,2,"",""),
("Nicki Minaj","Musician",250,5.0,8,2,3,"",""),
("Miley Cyrus","Global celebrity",250,4.0,5,1,2,"",""),
("Elon Musk","Other",230,6.5,10,1,2,"","⚠️ Posts constantly, zero hoops, and a political liability that would define the show"),
("Katy Perry","Global celebrity",210,3.5,5,1,3,"",""),
("Rihanna","Global celebrity",200,4.5,4,5,2,"","Famously courtside; no availability"),
("Barack Obama","Other",200,5.5,4,10,2,"UIC / DePaul (vault)","⭐ Real hoops obsessive and already a vault pairing. Availability is the whole problem"),
("Zendaya","Global celebrity",190,4.0,4,2,2,"",""),
("Cardi B","Musician",180,5.0,8,2,4,"",""),
("Kylian Mbappe","Global athlete",150,4.5,7,2,2,"",""),
("Billie Eilish","Musician",130,4.5,5,1,2,"",""),
("Zach King","Creator",130,4.0,7,1,5,"",""),
("Shakira","Global celebrity",130,3.5,5,1,2,"",""),
("Will Smith","Global celebrity",130,5.0,7,6,4,"St. Joseph's (vault, Philly)","⭐ Vault Season-1 option. Philly native, posts heavily, reputation rehab motive cuts both ways"),
("PewDiePie","Creator",120,4.0,5,1,3,"","Largely retired from the grind. Reach is legacy"),
("Vin Diesel","Global celebrity",110,3.5,5,1,3,"",""),
("Bad Bunny","Musician",100,5.0,6,6,3,"","Real NBA presence and cultural heat; availability low"),
("Bella Poarch","Creator",100,4.0,6,1,5,"",""),
("David Beckham","Global athlete",90,4.0,6,2,3,"","Owns Inter Miami — understands the model better than almost anyone on the list"),
("Michelle Obama","Other",90,5.0,3,6,2,"DePaul (vault)",""),
("The Weeknd","Musician",80,4.0,4,4,2,"",""),
("Mark Rober","Creator",70,6.0,4,2,6,"","⭐ Best pure storyteller among the big creators. Low cadence, high craft, would likely engage"),
("Ryan Reynolds","Owner-operator",70,6.5,7,4,5,"","⭐⭐ THE proof case. ⚠️ Also the reason he may decline — he already owns the Wrexham version of this"),
("Ninja","Creator",60,4.5,8,2,6,"",""),
("Marshmello","Musician",60,4.0,6,3,5,"",""),
("Conor McGregor","Combat",60,5.5,7,1,3,"","⚠️ Brand risk"),
("John Cena","Wrestling",60,4.5,6,4,5,"UMass (vault)","Vault pairing; actual alma mater is Springfield College (D3)"),
("Doja Cat","Musician",50,5.0,7,1,3,"",""),
("Markiplier","Creator",45,5.5,6,1,4,"",""),
("Kevin Durant","NBA active",40,6.0,9,10,4,"Texas","⭐ Genuinely online, argues with fans daily, and actively invests in sports ventures"),
("Giannis Antetokounmpo","NBA active",40,6.0,6,10,4,"",""),
("Megan Thee Stallion","Musician",40,5.5,8,4,4,"","Texas Southern alum — a vault school"),
("DJ Khaled","Musician",40,4.5,9,5,6,"","Posts constantly and physically shows up to everything"),
("Steve Harvey","Comedian",40,4.5,7,3,5,"Kent State (vault)",""),
("Gary Vaynerchuk","Owner-operator",35,6.0,10,4,7,"","⭐ Relentless poster who says yes to business-building content. Not a hoops name"),
("Michael Jordan","NBA retired",30,5.0,2,10,1,"North Carolina","Maximum authority, no social presence, no availability"),
("Kendrick Lamar","Musician",30,6.0,3,4,2,"",""),
("Lil Baby","Musician",30,5.0,8,6,5,"",""),
("James Harden","NBA active",30,5.5,7,10,5,"Arizona State",""),
("Joe Rogan","Comedian",30,6.5,7,3,4,"UMass Boston (vault D3)","Vault D3 track. Enormous male audience, weak hoops"),
("Luka Doncic","NBA active",25,6.0,6,10,3,"",""),
("Kyrie Irving","NBA active",25,6.0,7,10,4,"Duke","⚠️ Unpredictable partner"),
("Russell Westbrook","NBA active",25,5.5,7,10,5,"UCLA",""),
("Dwyane Wade","NBA retired",25,5.5,8,10,6,"Marquette","⭐ Media-native, produces, owns a WNBA stake — speaks our language"),
("Carmelo Anthony","NBA retired",25,5.5,8,10,7,"Syracuse / Baltimore (vault D3)","⭐ 7PM in Brooklyn gives him a daily voice; retired and genuinely available"),
("Future","Musician",25,5.0,7,4,3,"",""),
("21 Savage","Musician",25,5.0,6,4,4,"",""),
("Tyler, the Creator","Musician",25,5.5,5,3,3,"",""),
("Offset","Musician",25,5.0,8,5,5,"",""),
("Ryan Trahan","Creator",25,7.0,7,2,7,"","⭐ Long-form documentary instinct and very high engagement. Would likely say yes"),
("Matt Rife","Comedian",25,6.5,8,3,6,"",""),
("SZA","Musician",20,5.5,5,3,3,"",""),
("Rick Ross","Musician",20,5.0,9,4,6,"",""),
("Steve Aoki","Musician",20,4.5,9,4,7,"","Tours constantly — genuinely available"),
("Magic Johnson","NBA retired",20,5.5,8,10,6,"Michigan State","⭐ Owner-operator who posts daily and understands the capital structure instinctively"),
("Allen Iverson","NBA retired",20,6.0,4,10,6,"Georgetown / Philly","⭐⭐ Philly deity — the single most potent name for a St. Joseph's build. Low cadence"),
("Pokimane","Creator",20,5.5,8,1,6,"",""),
("Jayson Tatum","NBA active",15,6.0,7,10,4,"Duke / Saint Louis (vault)","Vault pairing at Saint Louis — his hometown"),
("Ja Morant","NBA active",15,6.5,7,10,4,"Murray State","⭐ The literal mid-major Cinderella — OVC to #2 pick. ⚠️ Off-court risk is real"),
("Devin Booker","NBA active",15,6.0,6,10,4,"Kentucky",""),
("Jimmy Butler","NBA active",15,6.0,7,10,5,"Marquette / Tyler JC","Junior-college-to-NBA underdog arc fits the thesis"),
("Roman Reigns","Wrestling",15,5.5,6,3,4,"",""),
("Playboi Carti","Musician",15,5.5,5,3,3,"",""),
("Gunna","Musician",15,5.5,7,4,5,"",""),
("Central Cee","Musician",15,5.5,7,3,4,"",""),
("Ice Spice","Musician",15,5.5,8,3,5,"",""),
("Morgan Wallen","Musician",15,6.0,6,3,4,"","Biggest audience in country music; ⚠️ brand risk"),
("Simone Biles","Female athlete",15,6.0,7,3,4,"",""),
("Jynxzi","Creator",15,8.5,10,5,8,"","⭐ Streams daily to an enormous young audience and does sports content. High fit, low cost"),
("Deestroying (Donald De La Haye)","Sports creator",12,7.5,9,4,8,"UCF","⭐⭐ Lost NCAA eligibility over YouTube income — he IS the NIL story. Thematically perfect"),
("Victor Wembanyama","NBA active",12,6.5,6,10,3,"",""),
("Latto","Musician",12,5.5,8,4,5,"",""),
("Diplo","Musician",12,5.0,8,3,6,"",""),
("Israel Adesanya","Combat",10,6.0,7,2,5,"",""),
("Zion Williamson","NBA active",10,6.0,5,10,3,"Duke",""),
("Trae Young","NBA active",10,6.0,7,10,4,"Oklahoma",""),
("Metro Boomin","Musician",10,5.5,8,5,5,"",""),
("GloRilla","Musician",10,6.0,8,4,5,"",""),
("Sexyy Red","Musician",10,6.5,9,4,6,"",""),
("Jay-Z","Musician",10,5.0,2,8,2,"LIU (vault)","Roc Nation Sports means he understands the structure. No access, no cadence"),
("Dr. Dre","Musician",10,4.5,3,3,2,"",""),
("Mark Cuban","Owner-operator",10,6.5,9,10,6,"Indiana","⭐⭐ Sold the Mavs, extremely online, funds unconventional sports ideas. Would take the call"),
("Triple H","Wrestling",10,5.5,7,3,5,"New Hampshire (vault)",""),
("Andrew Schulz","Comedian",10,7.0,8,5,6,"","Flagship-podcast reach with a young male audience"),
("Ludwig","Creator",10,6.5,8,3,7,"","⭐ Has actually produced live events (Chess Boxing, Mogul Money) — operator, not just a face"),
("Anthony Edwards","NBA active",8,6.5,6,10,4,"Georgia","Best personality among young stars"),
("Scottie Pippen","NBA retired",8,5.0,6,10,8,"Central Arkansas (vault)","⭐⭐ Vault pairing at his OWN alma mater — NAIA walk-on to the NBA. Available and on-thesis"),
("Chad Johnson","Sports media",8,6.5,9,3,8,"Oregon State","⭐ Hyper-online, hyper-available, loves a stunt"),
("Rhea Ripley","Wrestling",8,6.5,7,2,5,"",""),
("Zach Bryan","Musician",8,6.5,5,3,4,"",""),
("Bailey Zimmerman","Musician",8,6.0,7,3,6,"",""),
("Tom Segura","Comedian",8,6.0,7,3,6,"",""),
("Jack Whitehall","Comedian",8,5.5,6,2,5,"",""),
("Valkyrae","Creator",8,6.0,8,1,6,"",""),
("Tyler1","Creator",8,7.5,10,2,6,"","Extreme cadence and engagement; no hoops"),
("Shai Gilgeous-Alexander","NBA active",5,6.0,5,10,3,"Kentucky",""),
("Tracy McGrady","NBA retired",5,5.0,5,10,7,"","Available and credible"),
("Vince Carter","NBA retired",5,5.0,6,10,7,"North Carolina","⭐ ESPN analyst now — media-native, available, universally liked"),
("Sean O'Malley","Combat",5,6.5,8,2,6,"",""),
("Flau'jae Johnson","Female athlete",5,7.5,9,10,7,"LSU","⭐⭐ Rapper and starting guard, NIL-native, posts daily. Closest thing to a purpose-built fit"),
("Caleb Pressley","Sports creator",5,7.5,8,6,8,"North Carolina","⭐ Barstool, ex-UNC QB, Sundae Conversation. Ideal on-camera presence for this format"),
("HasanAbi","Creator",5,7.0,10,2,6,"","⚠️ Politically polarizing"),
("YourRAGE","Creator",5,7.5,10,6,7,"","Streams constantly; real hoops interest"),
("Naomi Osaka","Female athlete",6,5.5,6,4,4,"",""),
("Jon Jones","Combat",6,6.0,6,2,4,"","⚠️ Brand risk"),
("Cody Rhodes","Wrestling",6,6.0,7,2,5,"",""),
("Alex Cooper","Sports media",6,7.0,8,5,5,"Boston University","⭐ Built Unwell from a podcast — proof a following converts into a company. Women's-sports credibility"),
("Agent00","Creator",6,7.5,9,8,8,"","AMP; genuine hoops content"),
("Fanum","Creator",6,7.5,9,6,8,"","AMP"),
("Plaqueboymax","Creator",6,8.0,10,5,8,"","⭐ One of the highest live-cadence creators right now"),
("Skip Bayless","Sports media",4,5.5,9,8,7,"","Daily volume, declining relevance"),
("Bobby Lee","Comedian",4,6.0,7,2,6,"",""),
("ImDavisss","Creator",4,7.0,8,9,8,"","Hoops creator — cheap, willing, on-format"),
("Jalen Brunson","NBA active",3,6.0,7,10,5,"Villanova","Roommates Show with Josh Hart — already a media pair on this list"),
("Tyrese Haliburton","NBA active",3,6.5,8,10,5,"Iowa State","⭐ Extremely online and enjoys being a character"),
("Paige Bueckers","Female athlete",3,7.0,7,10,5,"UConn",""),
("Cameron Brink","Female athlete",3,7.0,8,10,6,"Stanford","Podcast host — media-native"),
("Suni Lee","Female athlete",3,6.5,7,2,5,"Auburn",""),
("Bianca Belair","Wrestling",3,6.5,7,3,5,"",""),
("Jey Uso","Wrestling",3,6.5,7,3,5,"",""),
("Shaboozey","Musician",3,6.5,6,3,6,"",""),
("Rob McElhenney","Owner-operator",3,6.5,7,4,6,"","⭐⭐ The other half of the proof case. Lower reach than Reynolds, likely far more accessible"),
("LSK (2HYPE)","Hoops creator",3,6.5,7,9,8,"",""),
("JuJu Watkins","Female athlete",2,7.0,6,10,4,"USC (vault)","⚠️ Still an enrolled athlete — NIL complexity cuts both ways"),
("A'ja Wilson","Female athlete",2,6.5,7,10,6,"South Carolina (vault)",""),
("Hailey Van Lith","Female athlete",2,7.0,8,10,6,"","Serial transfer — a story in herself"),
("Sydney McLaughlin","Female athlete",2,6.0,6,2,5,"",""),
("Charles Barkley","NBA retired",2,5.5,3,10,6,"St. Joseph's (vault, Philly)","⭐ Vault Season-1 option. Social reach understates him badly — his real channel is live TV"),
("Baron Davis","NBA retired",2,5.5,7,10,8,"UCLA","⭐ Already a media and investing operator. Very available"),
("Colin Cowherd","Sports media",2,5.0,9,7,6,"",""),
("Will Compton","Sports creator",2,6.5,8,4,8,"Nebraska","Bussin' With The Boys — available and format-friendly"),
("Taylor Lewan","Sports creator",2,6.5,8,4,8,"Michigan","Bussin' With The Boys"),
("Michael Keaton","Celebrity",2,4.0,3,4,4,"Kent State (vault)",""),
("Kamilla Cardoso","Female athlete",1,6.0,5,10,6,"South Carolina",""),
("Larry Bird","NBA retired",1,4.5,1,10,3,"Indiana State (vault)","⭐ The original Cinderella — 1979 Indiana State. ⚠️ Famously private, no social, rarely says yes"),
]

added = 0
for n, c, r, e, cad, h, av, tie, note in NEW:
    if n in seen:
        continue
    seen.add(n); added += 1
    rows.append(dict(Name=n, Category=c, Reach=r, Eng=e, Cad=cad, Hoop=h, Avail=av,
                     Tie=tie or "—", Scored="Jimmy est.", Notes=note))

# every row must now be fully scored, or the composite silently blanks
for r in rows:
    for k in ("Reach", "Eng", "Cad", "Hoop", "Avail"):
        assert str(r[k]).strip() != "", f"{r['Name']} missing {k}"
    assert 1 <= float(r["Eng"]) <= 11, r["Name"]
    for k in ("Cad", "Hoop", "Avail"):
        assert 1 <= float(r[k]) <= 10, (r["Name"], k)

first = 14; last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["MAKING CINDERELLA — GRASSROOTS REACH RANKING (v3)"])
w.writerow(["Unfiltered, and now fully scored — all 237 names carry Reach, Engagement, Cadence, Hoops and Availability."])
w.writerow(["⚠️ EVERY NUMBER IS AN ESTIMATE. Reach is rough cross-platform following in millions; Eng_Pct is an engagement-INTENSITY score on a 0-11 band, not a literal percentage. Compiled 2026-09-30. Verify before external use."])
w.writerow(["Overwrite any cell to substitute your own judgment — COMPOSITE and Rank recalculate immediately."])
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
open("v4.csv", "w", encoding="utf-8").write(t)
assert len(rows) == 237 and added == 148 and len(old) == 89
print(f"total {len(rows)} | legacy {len(old)} | newly scored {added} | rows {first}-{last} | {len(t):,} bytes")
