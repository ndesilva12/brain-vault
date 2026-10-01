# -*- coding: utf-8 -*-
"""v7: a US top-200 by SHARE VELOCITY, built independently of the MC target list.

⚠️ ESTIMATES. Share counts are not public on most platforms, so SHARE is modelled from the same
predictors as v6 (format, clip economy, emotional trigger, platform mix, participation, earned
media). VELOCITY = SHARE x Cadence.

⭐ THE FINDING: ranked by share velocity rather than followers, the top of America is dominated by
AGGREGATOR and NEWS accounts, not celebrities. Aggregators are PURCHASABLE MEDIA — a paid post, an
exclusive clip, a content partnership — not equity deals. For MC that is a far cheaper distribution
path than attaching a name.

TYPE: AGG aggregator/media brand · NEWS news/politics · IND individual · LEAGUE league/team · POD podcast
MC_FIT: Yes / Caution / No   (No = brand hazard for a school-facing docuseries)
US only — UK/global accounts (Sidemen, KSI, Beta Squad, Khaby, Ronaldo, Messi) excluded.
"""
import csv, io, collections

# (name, category, type, share, cadence, mc_fit, note)
A = [
("House of Highlights","Basketball","AGG",10,10,"Yes","⭐ Best distribution asset in US basketball. Buyable"),
("Bleacher Report","Sports","AGG",10,10,"Yes","⭐ Buyable. B/R Hoops sub-account also elite"),
("Overtime","Basketball","AGG",10,10,"Yes","⭐⭐ Built on youth/HS hoops — closest editorial fit to MC here"),
("Barstool Sports","Sports","AGG",10,10,"Caution","Adopting an underdog IS their model"),
("SportsCenter / ESPN","Sports","AGG",9,10,"Yes","Earned-media multiplier more than a share engine"),
("NBA","Basketball","LEAGUE",9,10,"Yes",""),
("NFL","Football","LEAGUE",9,10,"Yes",""),
("Hoop Central","Basketball","AGG",9,10,"Yes","Cheap, high volume"),
("Legion Hoops","Basketball","AGG",8,10,"Yes","Cheap"),
("Ballislife","Basketball","AGG",9,9,"Yes","⭐ Grassroots/HS hoops native"),
("SLAM","Basketball","AGG",9,9,"Yes","⭐ Culture authority in hoops"),
("Dime / Uproxx Sports","Basketball","AGG",8,9,"Yes",""),
("NBA Memes","Basketball","AGG",9,10,"Yes",""),
("Buckets","Basketball","AGG",8,10,"Yes",""),
("Overtime Elite","Basketball","AGG",8,9,"Yes",""),
("Field of 68","College hoops","AGG",8,9,"Yes","⭐⭐ College-basketball native. Small, perfect fit"),
("Jon Rothstein","College hoops","IND",7,10,"Yes","⭐ The college hoops newswire"),
("Stadium College Hoops","College hoops","AGG",7,9,"Yes",""),
("CBS Sports CBB","College hoops","AGG",7,9,"Yes",""),
("March Madness (NCAA)","College hoops","LEAGUE",8,8,"Yes","Seasonal, enormous in March"),
("Joe Lunardi / Bracketology","College hoops","IND",7,8,"Yes",""),
("WWE","Wrestling","LEAGUE",8,10,"Yes",""),
("UFC","Combat","LEAGUE",9,10,"Caution",""),
("Bleacher Report Gridiron","Football","AGG",9,10,"Yes",""),
("TheShadeRoom","Culture","AGG",10,10,"Caution","⭐ Enormous Black-culture reach; gossip tone"),
("PopCrave","Pop culture","AGG",10,10,"Yes","⭐ Highest quote-tweet rate in pop culture"),
("PopBase","Pop culture","AGG",10,10,"Yes",""),
("Pubity","Memes","AGG",10,10,"Caution","Scale without editorial control"),
("Daily Loud","Music/culture","AGG",10,10,"Caution",""),
("Worldstar (WSHH)","Culture","AGG",9,10,"No","Brand hazard for a school partner"),
("FearBuck","Memes","AGG",9,10,"Caution",""),
("9GAG","Memes","AGG",9,10,"Caution",""),
("Crazy Clips","Memes","AGG",9,10,"Caution",""),
("No Context Humans","Memes","AGG",9,9,"Caution",""),
("Dudes Posting Their Ws","Memes","AGG",9,9,"Caution",""),
("Complex","Culture","AGG",8,10,"Yes",""),
("Dexerto","Gaming","AGG",9,10,"Yes",""),
("Jake Lucky","Gaming news","IND",9,10,"Yes","⭐ Fast, high quote-tweet"),
("DramaAlert / Keemstar","Creator news","IND",8,9,"Caution",""),
("No Jumper","Music","AGG",8,9,"No",""),
("HotNewHipHop","Music","AGG",8,9,"Caution",""),
("XXL","Music","AGG",8,8,"Caution",""),
("Film Updates","Film","AGG",9,9,"Yes",""),
("DiscussingFilm","Film","AGG",9,9,"Yes",""),
("Netflix US","Platform","AGG",8,9,"Yes","⭐ Relevant as a BUYER, not a partner"),
("Betches","Lifestyle","AGG",8,9,"Yes",""),
("DeuxMoi","Gossip","AGG",8,8,"No",""),
("Unusual Whales","Finance","AGG",8,10,"Yes","⭐ Retail-investor audience — relevant to fan funding"),
("Chicks in the Office","Culture","POD",8,9,"Caution","Barstool"),
("Donald Trump","Politics","NEWS",10,10,"No","Highest share velocity in America. Unusable"),
("Elon Musk","Politics/tech","IND",10,10,"No","Possibly the most-retweeted account on earth"),
("Libs of TikTok","Politics","NEWS",9,10,"No",""),
("Catturd2","Politics","NEWS",9,10,"No",""),
("End Wokeness","Politics","NEWS",9,10,"No",""),
("Charlie Kirk","Politics","IND",9,10,"No",""),
("Benny Johnson","Politics","NEWS",9,10,"No",""),
("Collin Rugg","News","NEWS",9,10,"Caution","Straighter reporting than most of this cohort"),
("Mario Nawfal","News","NEWS",8,10,"Caution",""),
("Breaking911","News","NEWS",9,10,"Caution",""),
("MeidasTouch","Politics","NEWS",9,10,"No",""),
("Occupy Democrats","Politics","NEWS",9,10,"No",""),
("AOC","Politics","IND",9,9,"No",""),
("Disclose.tv","News","NEWS",8,10,"Caution",""),
("Zerohedge","Finance/news","NEWS",8,10,"Caution",""),
("The Spectator Index","News","NEWS",8,10,"Yes",""),
("Ian Miles Cheong","Politics","NEWS",8,10,"No",""),
("Wall Street Apes","Politics","NEWS",8,10,"No",""),
("Autism Capital","Culture/news","NEWS",8,10,"No",""),
("Dom Lucre","Politics","NEWS",8,10,"No",""),
("IShowSpeed","Mega creator","IND",10,10,"Caution","⭐ Most-clipped creator alive. Free third-party distribution"),
("Kai Cenat","Mega creator","IND",9,10,"Caution","⭐ Mafiathon convening"),
("Druski","Mega creator","IND",10,9,"Yes","⭐⭐ Content engineered to be reposted"),
("Sketch","Mega creator","IND",10,9,"Caution",""),
("Adin Ross","Mega creator","IND",8,10,"No","Brand hazard"),
("Plaqueboymax","Creator","IND",8,10,"Caution",""),
("Jynxzi","Creator","IND",8,10,"Yes",""),
("Tyler1","Creator","IND",7,10,"Caution",""),
("HasanAbi","Creator","IND",7,10,"No","Politically polarizing"),
("xQc","Mega creator","IND",6,10,"Caution",""),
("YourRAGE","Creator","IND",7,10,"Yes",""),
("Duke Dennis","Hoops creator","IND",8,9,"Yes","AMP"),
("Fanum","Creator","IND",7,9,"Yes","AMP"),
("Agent00","Creator","IND",7,9,"Yes","AMP"),
("MrBeast","Mega creator","IND",6,8,"Yes","Watched, not shared — YouTube share rate is weak"),
("Ryan Trahan","Creator","IND",7,7,"Yes",""),
("Airrack","Creator","IND",7,7,"Yes",""),
("Michelle Khare","Creator","IND",8,6,"Yes","⭐ Challenge format; MC-adjacent"),
("Mark Rober","Creator","IND",7,4,"Yes",""),
("Dude Perfect","Creator","IND",6,6,"Yes",""),
("Brittany Broski","Creator","IND",8,8,"Yes",""),
("Jake Shane","Creator","IND",8,8,"Yes",""),
("Drew Afualo","Creator","IND",8,8,"Caution",""),
("Trisha Paytas","Creator","IND",7,9,"No",""),
("Bobbi Althoff","Creator","IND",7,7,"Caution",""),
("Nara Smith","Lifestyle","IND",9,8,"Caution","⭐ Outrage-driven share rate"),
("Ballerina Farm","Lifestyle","IND",9,6,"Caution",""),
("Alix Earle","Lifestyle","IND",7,9,"Yes",""),
("Haley Kalil","Lifestyle","IND",7,9,"Caution",""),
("That Little Puff","Pets","IND",9,9,"Yes","Pure share format"),
("Caleb Simpson","Creator","IND",9,9,"Yes","⭐ Apartment-tour format; very high share"),
("Kareem Rahma / SubwayTakes","Creator","IND",10,8,"Yes","⭐⭐ One of the most-shared formats in America"),
("Keith Lee","Food","IND",10,8,"Yes","⭐⭐ Moves entire cities. Enormous civic share effect"),
("Nick DiGiovanni","Food","IND",8,8,"Yes","Harvard; New England tie"),
("Golden Balance","Food","IND",8,9,"Yes",""),
("Owen Han","Food","IND",8,9,"Yes",""),
("Tini Younger","Food","IND",8,8,"Yes",""),
("Joshua Weissman","Food","IND",7,7,"Yes",""),
("Logan Paul","Mega creator","IND",8,9,"Caution",""),
("Jake Paul","Mega creator","IND",8,9,"Caution","Built MVP — understands the model"),
("FaZe Rug","Mega creator","IND",6,8,"Yes",""),
("Nadeshot","Org builder","IND",6,8,"Yes","Built 100 Thieves by recruiting"),
("Valkyrae","Creator","IND",6,8,"Yes","100 Thieves co-owner"),
("Pokimane","Creator","IND",6,8,"Yes",""),
("Ninja","Creator","IND",6,8,"Yes",""),
("Markiplier","Creator","IND",6,6,"Yes",""),
("Ludwig","Creator","IND",7,8,"Yes","⭐ Produces live events"),
("Deestroying","Sports creator","IND",9,9,"Yes","⭐⭐ Lost NCAA eligibility over YouTube money — IS the NIL story"),
("Cam Wilder","Hoops creator","IND",9,9,"Yes","⭐⭐ Hoop Diaries = real-time team-season content"),
("Jesser","Hoops creator","IND",8,9,"Yes","2HYPE"),
("FlightReacts","Hoops creator","IND",8,9,"Yes",""),
("Tristan Jass","Hoops creator","IND",8,8,"Yes",""),
("Cash Nasty","Hoops creator","IND",8,8,"Yes","2HYPE"),
("ImDavisss","Hoops creator","IND",7,8,"Yes",""),
("Marcelas Howard","Hoops creator","IND",8,8,"Yes",""),
("The Professor","Hoops creator","IND",8,6,"Yes",""),
("Jordan Lawley","Hoops creator","IND",7,7,"Yes","Trainer; player access"),
("Kris London","Hoops creator","IND",7,7,"Yes","2HYPE"),
("Nick Briz","Hoops creator","IND",7,7,"Yes",""),
("Filayyyy","Hoops creator","IND",8,8,"Yes",""),
("Joe Rogan Experience","Podcast","POD",8,7,"Caution","Biggest gateway in podcasting"),
("Theo Von","Comedy","IND",9,9,"Yes","⭐ Clip format is elite right now"),
("Pat McAfee Show","Sports","POD",9,10,"Yes","⭐ ESPN platform + clip machine"),
("Stephen A. Smith","Sports","IND",9,9,"Yes",""),
("Shannon Sharpe / Nightcap","Sports","POD",9,9,"Caution","⭐ Most memeable reactions in sports"),
("Club Shay Shay","Podcast","POD",9,7,"Yes",""),
("Million Dollaz Worth of Game","Podcast","POD",8,8,"Caution","⭐⭐ Gillie + Wallo. North Philly natives"),
("Pardon My Take","Sports","POD",8,9,"Yes","Barstool"),
("New Heights (Kelce)","Sports","POD",8,7,"Yes","⭐ Jason Kelce = Philly"),
("Flagrant","Comedy","POD",8,8,"Caution","Schulz"),
("Andrew Schulz","Comedy","IND",8,8,"Caution",""),
("Kill Tony","Comedy","POD",8,8,"Caution",""),
("Matt Rife","Comedy","IND",8,8,"Caution",""),
("Bert Kreischer","Comedy","IND",8,8,"Yes","Very available"),
("Tom Segura / YMH","Comedy","POD",8,8,"Caution",""),
("Shane Gillis","Comedy","IND",8,7,"Caution","Philly-area roots"),
("Bobby Lee","Comedy","IND",7,7,"Caution",""),
("Call Her Daddy / Alex Cooper","Podcast","POD",7,8,"Yes","⭐ Built Unwell; women's sports credibility"),
("Smartless","Podcast","POD",6,6,"Yes",""),
("Lex Fridman","Podcast","POD",6,5,"Yes","MIT / Cambridge"),
("Big Cat (Dan Katz)","Sports","IND",8,9,"Yes",""),
("PFT Commenter","Sports","IND",8,9,"Yes","⭐ ~1M followers, top-30 velocity"),
("Brandon Walker","College hoops","IND",9,10,"Yes","⭐⭐ Barstool CBB. Obsessed with small-school hoops"),
("Trill Withers","College sports","IND",7,9,"Yes","Barstool"),
("Jack Mac","Sports","IND",7,9,"Yes","Barstool"),
("Spittin' Chiclets","Hockey","POD",7,8,"Yes","Ryan Whitney — Scituate MA"),
("Bussin' With The Boys","Football","POD",7,8,"Yes","Compton + Lewan"),
("Skip Bayless","Sports","IND",8,9,"Caution","Daily volume, declining relevance"),
("Colin Cowherd","Sports","IND",7,9,"Yes","Built The Volume"),
("Draymond Green","Sports","IND",8,8,"Caution","Active player"),
("Pat Beverley","Sports","IND",8,9,"Yes",""),
("Jalen Rose","Sports","IND",8,8,"Yes",""),
("Chad Johnson","Sports","IND",8,9,"Yes","Hyper-available"),
("Kirk Minihane","Sports","IND",7,9,"Caution","Massachusetts"),
("Caitlin Clark","Basketball","IND",9,7,"Yes","⭐ Tribal share rate is extraordinary"),
("Angel Reese","Basketball","IND",9,9,"Yes","⭐ Daily, hoops-native, culturally hot"),
("Livvy Dunne","Athlete-creator","IND",8,9,"Yes","⭐ NIL's defining face"),
("Flau'jae Johnson","Basketball","IND",8,9,"Yes","⭐⭐ Rapper + starting guard. Purpose-built fit"),
("Paige Bueckers","Basketball","IND",7,7,"Yes",""),
("JuJu Watkins","Basketball","IND",7,6,"Caution","Still enrolled — NIL complexity"),
("Hailey Van Lith","Basketball","IND",7,8,"Yes","Serial transfer — a story herself"),
("Cameron Brink","Basketball","IND",7,8,"Yes","Podcast host"),
("Shaquille O'Neal","Basketball","IND",7,8,"Yes","Famously says yes"),
("LeBron James","Basketball","IND",6,6,"Yes","Availability floor"),
("Stephen Curry","Basketball","IND",6,6,"Yes","Already attached (verbal)"),
("Ja Morant","Basketball","IND",7,7,"Caution","⭐ Murray State — literal mid-major Cinderella"),
("Anthony Edwards","Basketball","IND",7,6,"Yes","Best young personality"),
("Tyrese Haliburton","Basketball","IND",7,8,"Yes","Extremely online"),
("Victor Wembanyama","Basketball","IND",7,6,"Yes",""),
("Kevin Durant","Basketball","IND",6,9,"Caution","Boardroom + 35V"),
("Russell Westbrook","Basketball","IND",7,7,"Yes",""),
("Trae Young","Basketball","IND",7,7,"Yes",""),
("Jalen Brunson","Basketball","IND",6,7,"Yes","Villanova"),
("Marshawn Lynch","Football","IND",7,7,"Yes","Beloved, available"),
("Kendrick Lamar","Music","IND",6,3,"Yes","2024 beef drove record share volume"),
("Drake","Music","IND",6,6,"Caution",""),
("Taylor Swift","Music","IND",6,4,"Yes","Fandom shares intensely; zero availability"),
("Sexyy Red","Music","IND",7,9,"No",""),
("GloRilla","Music","IND",7,8,"Caution",""),
("Ice Spice","Music","IND",7,8,"Caution",""),
("Cardi B","Music","IND",7,8,"Caution",""),
("Nicki Minaj","Music","IND",7,8,"Caution",""),
("Travis Scott","Music","IND",6,6,"Caution",""),
("Bad Bunny","Music","IND",6,6,"Yes",""),
("Morgan Wallen","Music","IND",6,6,"Caution","Biggest country audience"),
("Jelly Roll","Music","IND",8,8,"Yes","⭐ Belmont target; underdog authenticity"),
("Post Malone","Music","IND",6,6,"Yes","North Texas"),
("Jack Harlow","Music","IND",6,6,"Yes","Louisville; hoops obsessive"),
("Lil Yachty","Music","IND",6,8,"Caution",""),
("Megan Thee Stallion","Music","IND",6,8,"Yes","Texas Southern alum"),
("DJ Khaled","Music","IND",6,9,"Yes","⭐ Assembling stars IS his art form"),
("Master P","Music","IND",7,7,"Yes","⭐ Has run programs and NIL ventures"),
("Quavo","Music","IND",6,7,"Yes","Celebrity-game regular"),
("2 Chainz","Music","IND",6,7,"Yes","Played college basketball"),
("Rick Ross","Music","IND",6,9,"Caution",""),
("Snoop Dogg","Music","IND",7,9,"Yes","⭐ Youth league founder; shows up"),
("Conor McGregor","Combat","IND",6,7,"No","Brand risk"),
("Sean O'Malley","Combat","IND",6,8,"Caution",""),
("Roman Reigns","Wrestling","IND",6,6,"Yes",""),
("Cody Rhodes","Wrestling","IND",6,7,"Yes",""),
("Rhea Ripley","Wrestling","IND",6,7,"Yes",""),
("Triple H","Wrestling","IND",6,7,"Yes","⭐ Runs WWE talent — he IS a network"),
("John Cena","Wrestling","IND",6,6,"Yes","UMass target"),
("Michael Rubin","Business","IND",6,8,"Yes","⭐⭐ Convening is his product. Low share, max connectivity"),
("Mark Cuban","Business","IND",6,9,"Yes","⭐⭐ Answers email himself"),
("Gary Vaynerchuk","Business","IND",6,10,"Yes","Gives intros away free"),
("Ryan Reynolds","Owner-operator","IND",6,7,"Yes","⭐⭐ THE proof case. May decline — owns it already"),
("Rob McElhenney","Owner-operator","IND",6,7,"Yes","⭐⭐ Philadelphia native. The accessible half"),
("Magic Johnson","Business","IND",7,8,"Yes","Understands the capital structure"),
("Dwyane Wade","Business","IND",6,8,"Yes","Produces; WNBA stake"),
("Carmelo Anthony","Business","IND",6,8,"Yes","Retired, available, daily voice"),
("Kevin Hart","Celebrity","IND",8,8,"Yes","⭐ Philly + Blue Coats co-owner"),
("Will Smith","Celebrity","IND",6,7,"Yes","West Philly"),
("Charles Barkley","Sports","IND",9,3,"Yes","⭐ TV clips shared hugely; tiny social"),
("Allen Iverson","Sports","IND",7,4,"Yes","⭐⭐ Philly deity. Low cadence"),
("Quinta Brunson","Creator-showrunner","IND",7,6,"Yes","⭐ West Philly; Abbott Elementary"),
("Lil Dicky","Creator-showrunner","IND",7,5,"Yes","YouTube viral -> Dave on FX. Philly suburb"),
("Gillie Da Kid","Podcast","IND",8,8,"Caution","⭐⭐ North Philly"),
("Wallo267","Podcast","IND",8,8,"Yes","⭐⭐ North Philly. Redemption brand = MC's own theme"),
]

seen, rows = set(), []
for t in A:
    if t[0] in seen:
        continue
    seen.add(t[0]); rows.append(t)
for n, cat, typ, s, c, fit, note in rows:
    assert 1 <= s <= 10 and 1 <= c <= 10, n
    assert fit in ("Yes", "Caution", "No"), n
    assert typ in ("AGG", "NEWS", "IND", "LEAGUE", "POD"), n

rows.sort(key=lambda t: (-(t[3]*t[4]), -t[3], t[0]))

first = 10
last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["US TOP ACCOUNTS BY SHARE VELOCITY — independent of the MC target list"])
w.writerow(["⚠️ ESTIMATES. Share counts are not public on most platforms. SHARE is modelled from format, clip economy, emotional trigger, platform mix, participation and earned media."])
w.writerow(["VELOCITY = SHARE x Cadence. Sorted descending. US accounts only — UK/global (Sidemen, KSI, Khaby, Ronaldo, Messi) excluded."])
w.writerow(["⭐ THE FINDING: ranked by share velocity rather than followers, the top is AGGREGATOR and NEWS accounts, not celebrities. Aggregators are PURCHASABLE MEDIA — a paid post or an exclusive clip, not an equity deal."])
w.writerow(["TYPE: AGG aggregator/media brand · NEWS news/politics · IND individual · LEAGUE league/team · POD podcast"])
w.writerow(["MC_FIT: Yes / Caution / No. 'No' = brand hazard for a school-facing docuseries. Several of the highest-velocity accounts in America are unusable for us."])
w.writerow([])
w.writerow(["Rank", "Account", "Category", "Type", "SHARE_1_10", "Cadence_1_10", "VELOCITY",
            "MC_FIT", "Note"])
for i, (n, cat, typ, s, c, fit, note) in enumerate(rows):
    x = first + i
    w.writerow([f"=RANK(G{x},G${first}:G${last})", n, cat, typ, s, c, f"=E{x}*F{x}", fit, note])
t = buf.getvalue()
open("v7-us200.csv", "w", encoding="utf-8").write(t)

print(f"{len(rows)} accounts | data rows {first}-{last} | {len(t):,} bytes\n")
print("by type:", dict(collections.Counter(r[2] for r in rows)))
print("by MC fit:", dict(collections.Counter(r[5] for r in rows)))
print("\n=== TOP 30 ===")
for i, (n, cat, typ, s, c, fit, note) in enumerate(rows[:30], 1):
    print(f"{i:3d} vel {s*c:3d}  {typ:6s} {fit:7s} {n}")
print("\n=== HIGHEST-VELOCITY 'Yes' AGGREGATORS / LEAGUES (buyable distribution) ===")
k = 0
for n, cat, typ, s, c, fit, note in rows:
    if fit == "Yes" and typ in ("AGG", "LEAGUE"):
        k += 1
        print(f"  vel {s*c:3d}  {n} — {note or cat}")
    if k >= 14:
        break
