# -*- coding: utf-8 -*-
"""Making Cinderella — grassroots reach ranking.
Built to Fried's thesis (2026-09-29): real-time daily engagement beats name recognition.
Follower figures are ESTIMATES as of ~mid-2026 and must be verified before external use.
Columns are independently sortable; COMPOSITE is a weighted blend."""
import csv, math

# name, category, reach_m (total est. followers, millions), eng (est. engagement %, 0-15),
# cadence (1-10 real-time daily posting), hoops (1-10 basketball authenticity),
# avail (1-10 likelihood of real on-the-ground commitment), school_tie, note
D = [
 # ── BASKETBALL-NATIVE CREATORS — the core of Fried's thesis ──
 ("Jesser (Jesse Riedel)","Hoops creator",16,7.5,9,10,9,"—","2HYPE. Daily basketball content; already on Fried's call list"),
 ("Cam Wilder","Hoops creator",4,8.5,9,10,10,"—","Hoop Diaries — literally makes real-time team-season content. Tightest format fit on the list"),
 ("Tristan Jass","Hoops creator",13,7.0,8,10,8,"—","Trick-shot/hoops native, global reach, young audience"),
 ("Duke Dennis","Hoops creator",9,8.0,9,9,8,"—","AMP. NBA2K/hoops roots, enormous Gen-Z pull"),
 ("Cash Nasty (CashNasty)","Hoops creator",7,7.0,8,10,8,"—","Basketball daily; 2HYPE orbit"),
 ("FlightReacts","Hoops creator",8,8.5,9,9,7,"—","Chaotic, extremely high engagement, pure hoops"),
 ("Filayyyy","Hoops creator",6,8.0,8,9,8,"—","Hoops content native"),
 ("Marcelas Howard","Hoops creator",2,7.0,8,10,9,"—","Basketball media creator, credible with players"),
 ("Kris London","Hoops creator",5,6.0,7,9,8,"—","2HYPE"),
 ("Jiedel","Hoops creator",3,6.5,7,9,8,"—","2HYPE"),
 ("Mopi","Hoops creator",3,6.5,7,9,8,"—","2HYPE"),
 ("ZackTTG","Hoops creator",3,6.0,7,9,8,"—","2HYPE"),
 ("The Professor (Grayson Boucher)","Hoops creator",8,6.0,6,10,8,"—","Streetball legend; authenticity very high"),
 ("Jordan Lawley","Hoops creator",2,6.0,7,10,9,"—","Trainer; deep player relationships"),
 ("Nick Briz","Hoops creator",2,6.5,7,9,8,"—","Hoops creator / Overtime orbit"),
 ("Mikey Williams","Player-creator",6,7.5,7,10,6,"—","Player with creator-scale following"),
 # ── BARSTOOL / GRASSROOTS SPORTS MEDIA — the dark-horse category ──
 ("Dave Portnoy","Sports media",5,9.0,10,7,8,"—","⭐ Barstool's entire model IS adopting an underdog in real time. Highest thesis fit of any non-hoops name"),
 ("Brandon Walker","Sports media",1,8.5,10,10,10,"—","⭐ Runs Barstool college basketball; publicly obsessed with small-school hoops. Perfect fit, tiny cost"),
 ("Big Cat (Dan Katz)","Sports media",2,7.5,9,7,7,"—","Pardon My Take — enormous daily sports audience"),
 ("PFT Commenter","Sports media",1,7.0,9,6,7,"—","PMT"),
 ("Trill Withers (Tyler)","Sports media",1,7.5,9,7,8,"—","Barstool college sports"),
 ("Jack Mac","Sports media",1,7.0,9,6,8,"—","Barstool"),
 ("Pat McAfee","Sports media",4,8.0,10,8,6,"—","ESPN daily show; authentic, huge, but heavily committed"),
 ("Shannon Sharpe","Sports media",4,7.5,9,8,6,"—","Nightcap — daily, culturally central"),
 ("Stephen A. Smith","Sports media",7,6.5,9,8,5,"St. Joseph's","Already a vault target; ESPN conflict analysis logged"),
 ("Draymond Green","Athlete media",7,7.0,8,10,5,"—","Daily podcast, active player"),
 ("Bill Simmons","Sports media",1,6.0,8,8,5,"Holy Cross","Vault pairing already"),
 ("Jomboy (Jimmy O'Brien)","Sports media",2,8.0,9,5,7,"—","Model for creator-built sports media; baseball-centric"),
 # ── MEGA CREATORS ──
 ("MrBeast (Jimmy Donaldson)","Mega creator",650,6.0,8,4,2,"—","Maximum reach, minimum availability. Would need to be his own idea"),
 ("IShowSpeed","Mega creator",75,11.0,10,7,5,"—","⭐ Extraordinary engagement + streams constantly. Global, chaotic, young"),
 ("Kai Cenat","Mega creator",40,10.0,10,6,5,"—","Twitch record-holder; AMP; unmatched live audience"),
 ("Jake Paul","Mega creator",65,6.5,9,6,8,"—","⭐ Already on Fried's call list. Has actually BUILT a sports business (MVP). Understands the model"),
 ("Logan Paul","Mega creator",75,6.0,9,5,7,"—","⭐ On Fried's list. WWE + Prime; proven brand builder"),
 ("KSI","Mega creator",45,6.5,8,5,6,"—","Prime co-founder, Sidemen"),
 ("Adin Ross","Mega creator",15,9.0,10,6,6,"—","Live-native, sports/betting adjacent"),
 ("Druski","Mega creator",16,9.5,9,7,8,"—","⭐ Coulda Been Records; culturally central, does sports content, young audience"),
 ("Sketch","Mega creator",8,9.0,9,6,7,"—","Viral, sports-adjacent, extremely high engagement"),
 ("xQc","Mega creator",15,7.0,10,3,4,"—","Live volume enormous, hoops fit weak"),
 ("Dude Perfect","Mega creator",75,6.0,6,7,6,"—","Family-brand sports stunts; org-scale"),
 ("Sidemen (collective)","Mega creator",40,6.5,7,4,5,"—","Collective; proven at building ventures"),
 ("Nadeshot (Matt Haag)","Org builder",5,6.0,8,5,9,"—","⭐ Built 100 Thieves from a following. Best living proof of the model"),
 ("FaZe Rug","Mega creator",30,6.0,8,5,6,"—","FaZe orbit"),
 # ── TIKTOK / LIFESTYLE NATIVE ──
 ("Livvy Dunne","Athlete-creator",15,7.5,9,6,7,"—","⭐ NIL's defining face. Thematically perfect — college athlete commercial value personified"),
 ("Alix Earle","Lifestyle",10,7.0,9,4,6,"—","Netflix series; young female audience; Miami"),
 ("Charli D'Amelio","Lifestyle",180,4.5,7,2,4,"—","Massive but weak sports tie"),
 ("Addison Rae","Lifestyle",100,4.0,6,2,3,"—","Weak fit"),
 ("Khaby Lame","Mega creator",190,5.0,7,2,3,"—","Global, no US sports tie"),
 ("Bryce Hall","Lifestyle",25,5.0,8,4,7,"—","Has done combat sports crossover"),
 ("Josh Richards","Lifestyle",40,4.5,7,3,6,"—","Investor-operator angle"),
 # ── ATHLETES WITH CREATOR-SCALE REACH ──
 ("Stephen Curry","Athlete",90,6.0,6,10,7,"Davidson","⚠️ ALREADY ATTACHED (verbal). Listed for comparison only"),
 ("Shaquille O'Neal","Athlete",45,6.5,8,10,8,"LSU","⭐ Famously says yes; DJ/appearance culture = on-the-ground willing"),
 ("Angel Reese","Athlete",10,8.0,9,10,7,"LSU","Young, daily, hoops-native, culturally hot"),
 ("Caitlin Clark","Athlete",6,8.5,7,10,5,"Iowa","Enormous cultural moment; availability low"),
 ("Sabrina Ionescu","Athlete",3,6.5,7,10,6,"Oregon","Vault 'Smoller lane'"),
 ("Serena Williams","Athlete",20,5.5,6,4,5,"—","Vault 'Smoller lane'; investor profile"),
 ("LeBron James","Athlete",210,5.0,6,10,2,"—","Reach ceiling, availability floor"),
 ("Paul George","Athlete",8,6.0,8,10,6,"Fresno State","Podcast — daily voice"),
 ("Josh Hart","Athlete",2,6.5,8,10,7,"Villanova","Roommates Show; Philly tie"),
 ("Pat Beverley","Athlete media",3,7.5,9,10,8,"Arkansas","Pat Bev Pod; loud, daily, hoops-deep"),
 ("Jalen Rose","Athlete media",2,6.0,8,10,7,"Michigan","Media-native"),
 # ── TRADITIONAL CELEBRITIES WITH REAL SOCIAL ──
 ("Dwayne Johnson","Celebrity",420,5.5,7,5,4,"Miami","Owns UFL — understands league-building. Availability low"),
 ("Kevin Hart","Celebrity",185,5.5,8,7,6,"St. Joseph's (regional)","⭐ Vault target; posts constantly; Philly"),
 ("Snoop Dogg","Celebrity",90,6.5,9,8,8,"Long Beach State","⭐ Youth football league founder; genuinely shows up; daily poster"),
 ("Drake","Celebrity",150,5.5,6,8,3,"—","Raptors ambassador; availability very low"),
 ("Jamie Foxx","Celebrity",25,5.0,6,7,7,"North Texas (regional)","⚠️ LIVE — Marcus King positive Sep 25"),
 ("Mark Wahlberg","Celebrity",25,5.0,7,5,6,"Northeastern (regional)","⚠️ Vault: Levinson previously killed it; CURRENT.md lists engaged"),
 ("Adam Sandler","Celebrity",15,5.0,4,8,5,"New Hampshire","⚠️ Engaged per CURRENT.md; low social cadence"),
 ("Theo Von","Comedian",12,8.0,9,4,8,"—","⭐ Daily-ish, relatable, Southern; strong grassroots energy"),
 ("Bert Kreischer","Comedian",8,7.0,8,4,8,"Florida State","Tour-native, very available"),
 ("Shane Gillis","Comedian",6,8.0,7,6,7,"Elon (weak tie)","Culturally hot; Philly-area roots"),
 ("Will Ferrell","Celebrity",15,4.5,4,6,5,"USC / UC Irvine","Low cadence"),
 ("Bill Murray","Celebrity",3,4.0,3,9,5,"Charleston / BC","Son Luke coaches BC; no social presence"),
 ("Michael Rubin","Owner-operator",2,6.0,8,7,7,"—","Fanatics; convenes everyone; not a reach play"),
 ("Ludacris","Celebrity",25,5.5,7,6,7,"Georgia State","Vault pairing"),
 ("Travis Scott","Celebrity",90,6.0,6,6,4,"Texas Southern","Vault pairing; availability low"),
 ("Jelly Roll","Musician",12,8.5,8,4,8,"Belmont (target)","⚠️ Belmont deck sent Sep 18. Underdog-story authenticity is exceptional"),
 ("Brad Paisley","Musician",5,5.0,5,3,7,"Belmont (target)","⚠️ Belmont deck sent Sep 18"),
 ("Luke Combs","Musician",12,6.5,6,4,6,"Appalachian St.","Vault pairing"),
 ("Eric Church","Musician",4,5.0,4,4,5,"Appalachian St.","Vault pairing"),
 ("Post Malone","Musician",50,6.0,6,5,5,"North Texas","Vault pairing"),
 ("Machine Gun Kelly","Musician",30,6.0,7,5,6,"Cleveland State","Underdog-city energy"),
 ("Jack Harlow","Musician",20,6.5,7,9,6,"Louisville","Genuine hoops obsessive"),
 ("Quavo","Musician",25,6.0,7,8,7,"—","Celebrity-game regular"),
 ("2 Chainz","Musician",15,6.0,7,8,7,"Alabama State","Played college basketball"),
 ("Master P","Musician",5,6.0,7,9,9,"—","⭐ Has actually run programs and NIL ventures; would absolutely engage"),
 ("Lil Yachty","Musician",20,6.5,8,6,7,"—","Very online"),
 ("Kai Trump","Creator",6,7.5,8,4,6,"Miami","Golf/NIL adjacent; young audience"),
 ("Nelly","Musician",10,5.5,6,7,7,"—","Owns stakes; available"),
 ("Marshawn Lynch","Athlete",6,7.0,7,5,8,"Cal","Beloved, authentic, very available"),
]

W = {"reach":0.20,"eng":0.25,"cadence":0.25,"hoops":0.15,"avail":0.15}
mx_e = max(r[3] for r in D)
rows=[]
for name,cat,reach,eng,cad,hoop,avail,tie,note in D:
    r_s = math.log10(reach+1)/math.log10(651)*10          # log-scaled so mega names don't swamp
    e_s = eng/mx_e*10
    comp = (r_s*W["reach"] + e_s*W["eng"] + cad*W["cadence"]
            + hoop*W["hoops"] + avail*W["avail"])
    rows.append(dict(Name=name, Category=cat, Composite=round(comp,2),
        Reach_M=reach, Reach_Score=round(r_s,2), Engagement_Pct=eng,
        Engagement_Score=round(e_s,2), Cadence_1_10=cad, Hoops_Auth_1_10=hoop,
        Availability_1_10=avail, Reach_x_Eng_M=round(reach*eng/100,2),
        School_Tie=tie, Notes=note))
rows.sort(key=lambda r:-r["Composite"])
for i,r in enumerate(rows,1): r["Rank"]=i

cols=["Rank","Name","Category","Composite","Reach_M","Reach_Score","Engagement_Pct",
      "Engagement_Score","Cadence_1_10","Hoops_Auth_1_10","Availability_1_10",
      "Reach_x_Eng_M","School_Tie","Notes"]
out="/tmp/claude-0/-home-user-brain-vault/cdeb7b3c-9b38-5f86-b0fa-23ce6e519c4c/scratchpad/grassroots.csv"
with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow({c:r[c] for c in cols})
print(f"{len(rows)} names -> {out}\n")
print(f"{'#':>3} {'NAME':34}{'CAT':16}{'CMP':>5}{'REACH':>7}{'ENG%':>6}{'CAD':>4}{'HOOP':>5}{'AVL':>4}")
for r in rows[:30]:
    print(f"{r['Rank']:>3} {r['Name'][:33]:34}{r['Category'][:15]:16}{r['Composite']:>5}"
          f"{r['Reach_M']:>7}{r['Engagement_Pct']:>6}{r['Cadence_1_10']:>4}"
          f"{r['Hoops_Auth_1_10']:>5}{r['Availability_1_10']:>4}")
