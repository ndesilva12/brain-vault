# -*- coding: utf-8 -*-
import csv, io
old=list(csv.DictReader(open("grassroots.csv",encoding="utf-8")))
rows=[]
for r in old:
    rows.append(dict(Name=r["Name"],Category=r["Category"],Reach=r["Reach_M"],Eng=r["Engagement_Pct"],
        Cad=r["Cadence_1_10"],Hoop=r["Hoops_Auth_1_10"],Avail=r["Availability_1_10"],
        Tie=r["School_Tie"],Scored="Jimmy est.",Notes=r["Notes"]))
seen={r["Name"] for r in rows}

NEW=[
("Cristiano Ronaldo","Global athlete",1000),("Lionel Messi","Global athlete",700),
("Selena Gomez","Global celebrity",500),("Kylie Jenner","Global celebrity",450),
("Ariana Grande","Global celebrity",450),("Kim Kardashian","Global celebrity",420),
("Taylor Swift","Global celebrity",400),("Justin Bieber","Global celebrity",380),
("Beyonce","Global celebrity",350),("Neymar","Global athlete",300),
("Khloe Kardashian","Global celebrity",300),("Kendall Jenner","Global celebrity",290),
("Virat Kohli","Global athlete",280),("Jennifer Lopez","Global celebrity",280),
("Nicki Minaj","Musician",250),("Miley Cyrus","Global celebrity",250),
("Elon Musk","Other",230),("Katy Perry","Global celebrity",210),
("Rihanna","Global celebrity",200),("Barack Obama","Other",200),
("Zendaya","Global celebrity",190),("Cardi B","Musician",180),
("Kylian Mbappe","Global athlete",150),("Billie Eilish","Musician",130),
("Zach King","Creator",130),("Shakira","Global celebrity",130),
("Will Smith","Global celebrity",130),("PewDiePie","Creator",120),
("Vin Diesel","Global celebrity",110),("Bad Bunny","Musician",100),
("Bella Poarch","Creator",100),("David Beckham","Global athlete",90),
("Michelle Obama","Other",90),("The Weeknd","Musician",80),
("Mark Rober","Creator",70),("Ryan Reynolds","Owner-operator",70),
("Ninja","Creator",60),("Marshmello","Musician",60),
("Conor McGregor","Combat",60),("John Cena","Wrestling",60),
("Doja Cat","Musician",50),("Markiplier","Creator",45),
("Kevin Durant","NBA active",40),("Giannis Antetokounmpo","NBA active",40),
("Megan Thee Stallion","Musician",40),("DJ Khaled","Musician",40),
("Steve Harvey","Comedian",40),("Gary Vaynerchuk","Owner-operator",35),
("Michael Jordan","NBA retired",30),("Kendrick Lamar","Musician",30),
("Lil Baby","Musician",30),("James Harden","NBA active",30),
("Joe Rogan","Comedian",30),("Luka Doncic","NBA active",25),
("Kyrie Irving","NBA active",25),("Russell Westbrook","NBA active",25),
("Dwyane Wade","NBA retired",25),("Carmelo Anthony","NBA retired",25),
("Future","Musician",25),("21 Savage","Musician",25),
("Tyler, the Creator","Musician",25),("Offset","Musician",25),
("Ryan Trahan","Creator",25),("Matt Rife","Comedian",25),
("SZA","Musician",20),("Rick Ross","Musician",20),
("Steve Aoki","Musician",20),("Magic Johnson","NBA retired",20),
("Allen Iverson","NBA retired",20),("Pokimane","Creator",20),
("Jayson Tatum","NBA active",15),("Ja Morant","NBA active",15),
("Devin Booker","NBA active",15),("Jimmy Butler","NBA active",15),
("Roman Reigns","Wrestling",15),("Playboi Carti","Musician",15),
("Gunna","Musician",15),("Central Cee","Musician",15),
("Ice Spice","Musician",15),("Morgan Wallen","Musician",15),
("Simone Biles","Female athlete",15),("Jynxzi","Creator",15),
("Deestroying (Donald De La Haye)","Sports creator",12),
("Victor Wembanyama","NBA active",12),("Latto","Musician",12),
("Diplo","Musician",12),("Israel Adesanya","Combat",10),
("Zion Williamson","NBA active",10),("Trae Young","NBA active",10),
("Metro Boomin","Musician",10),("GloRilla","Musician",10),
("Sexyy Red","Musician",10),("Jay-Z","Musician",10),
("Dr. Dre","Musician",10),("Mark Cuban","Owner-operator",10),
("Triple H","Wrestling",10),("Andrew Schulz","Comedian",10),
("Ludwig","Creator",10),("Anthony Edwards","NBA active",8),
("Scottie Pippen","NBA retired",8),("Chad Johnson","Sports media",8),
("Rhea Ripley","Wrestling",8),("Zach Bryan","Musician",8),
("Bailey Zimmerman","Musician",8),("Tom Segura","Comedian",8),
("Jack Whitehall","Comedian",8),("Valkyrae","Creator",8),("Tyler1","Creator",8),
("Shai Gilgeous-Alexander","NBA active",5),("Tracy McGrady","NBA retired",5),
("Vince Carter","NBA retired",5),("Sean O'Malley","Combat",5),
("Flau'jae Johnson","Female athlete",5),("Caleb Pressley","Sports creator",5),
("HasanAbi","Creator",5),("YourRAGE","Creator",5),
("Naomi Osaka","Female athlete",6),("Jon Jones","Combat",6),
("Cody Rhodes","Wrestling",6),("Alex Cooper","Sports media",6),
("Agent00","Creator",6),("Fanum","Creator",6),("Plaqueboymax","Creator",6),
("Skip Bayless","Sports media",4),("Bobby Lee","Comedian",4),
("ImDavisss","Creator",4),("Jalen Brunson","NBA active",3),
("Tyrese Haliburton","NBA active",3),("Paige Bueckers","Female athlete",3),
("Cameron Brink","Female athlete",3),("Suni Lee","Female athlete",3),
("Bianca Belair","Wrestling",3),("Jey Uso","Wrestling",3),
("Shaboozey","Musician",3),("Rob McElhenney","Owner-operator",3),
("LSK (2HYPE)","Hoops creator",3),("JuJu Watkins","Female athlete",2),
("A'ja Wilson","Female athlete",2),("Hailey Van Lith","Female athlete",2),
("Sydney McLaughlin","Female athlete",2),("Charles Barkley","NBA retired",2),
("Baron Davis","NBA retired",2),("Colin Cowherd","Sports media",2),
("Will Compton","Sports creator",2),("Taylor Lewan","Sports creator",2),
("Michael Keaton","Celebrity",2),("Kamilla Cardoso","Female athlete",1),
("Larry Bird","NBA retired",1),
]
added=0
for n,c,r in NEW:
    if n in seen: continue
    seen.add(n); added+=1
    rows.append(dict(Name=n,Category=c,Reach=r,Eng="",Cad="",Hoop="",Avail="",
                     Tie="",Scored="UNSCORED — Norman",Notes=""))

first=14; last=first+len(rows)-1
buf=io.StringIO(); w=csv.writer(buf)
w.writerow(["MAKING CINDERELLA — GRASSROOTS REACH RANKING (v2)"])
w.writerow(["Unfiltered. Global mega-reach names included. Judgment columns left blank on new rows for Norman to score."])
w.writerow(["Reach figures are ROUGH ESTIMATES of total cross-platform following (millions), compiled 2026-09-30, current to roughly mid-2026. VERIFY before external use."])
w.writerow(["COMPOSITE stays blank until Eng_Pct, Cadence, Hoops and Avail are all filled. Rank ignores blanks."])
w.writerow(["WEIGHTS — edit column B; everything below re-sorts","","(must total 1.00)"])
for lab,val in [("Reach (log-scaled)",0.20),("Engagement rate",0.25),("Cadence / real-time",0.25),
                ("Basketball authenticity",0.15),("Availability to commit",0.15)]:
    w.writerow([lab,val])
w.writerow(["TOTAL","=SUM(B6:B10)","<- must read 1"])
w.writerow([])
w.writerow(["Rank","Name","Category","COMPOSITE","Reach_M","Eng_Pct","Cadence_1_10",
            "Hoops_1_10","Avail_1_10","Reach x Eng","School_Tie","Scored_By","Notes"])
for i,r in enumerate(rows):
    x=first+i
    comp=(f'=IF(OR($F{x}="",$G{x}="",$H{x}="",$I{x}=""),"",'
          f'LOG10($E{x}+1)/LOG10(MAX($E${first}:$E${last})+1)*10*$B$6'
          f'+$F{x}/MAX($F${first}:$F${last})*10*$B$7'
          f'+$G{x}*$B$8+$H{x}*$B$9+$I{x}*$B$10)')
    w.writerow([f'=IF($D{x}="","",RANK($D{x},$D${first}:$D${last}))', r["Name"], r["Category"],
        comp, r["Reach"], r["Eng"], r["Cad"], r["Hoop"], r["Avail"],
        f'=IF(OR($E{x}="",$F{x}=""),"",$E{x}*$F{x}/100)', r["Tie"], r["Scored"], r["Notes"]])
t=buf.getvalue(); open("v2.csv","w",encoding="utf-8").write(t)
print(f"total {len(rows)} names | previously scored {len(old)} | newly added {added}")
print(f"data rows {first}-{last} | payload {len(t):,} bytes")
