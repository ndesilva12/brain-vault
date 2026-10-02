# -*- coding: utf-8 -*-
"""v8: US INDIVIDUAL accounts ranked by share velocity. Built top-down from the country,
not from the Making Cinderella target list.

WHAT WAS WRONG WITH v7 (and why this is a full rebuild, not a patch):
  1. SELECTION BIAS. The candidate pool started from MC targets and added to it, so the
     ranking could only ever reflect our own shortlist.
  2. SCORING BIAS. SHARE measured "shareability for our purposes" on a relative scale, so a
     niche account with a tight audience scored like a national one. Brandon Walker came out
     4th in the United States, which is absurd.

SHARE is now an ABSOLUTE scale — estimated shares/retweets on a typical well-performing post:
  10  >500k      Trump, Musk. A tier of their own; every post is a news event
   9  100-500k   Ye, MrBeast, Speed, Kai Cenat, top political accounts, Obama
   8  30-100k    Mega musicians, top creators, LeBron, Caitlin Clark
   7  10-30k     A-list actors, top athletes, major finance/tech accounts
   6  3-10k      Stephen A., McAfee, Portnoy, mid-tier creators
   5  1-3k       Niche sports media, Barstool personalities, hoops creators
   4  300-1k
   3  <300
VELOCITY = SHARE x Cadence (total shares distributed, not per-post).

SCOPE: individuals only. No aggregators, brands, leagues, or podcasts-as-properties —
so no Barstool, House of Highlights, NBA, Pardon My Take, Dude Perfect or Sidemen.
A podcast HOST as a person is in; the show as an entity is not.
US-based. Non-US-born athletes playing in US leagues are included and flagged, because
their share volume is substantially American. Non-US accounts (Ronaldo, Messi, KSI,
Khaby, McGregor, Adesanya, Peterson, Piers Morgan) are excluded.
⚠️ Avowed extremist accounts are omitted. That is an editorial call, stated so it is visible.
⚠️ NOT EXHAUSTIVE. This is an estimated top ~260, not every individual account in America.

In_MC_List is neutral metadata for cross-referencing. It does not touch the ranking.
"""
import csv, io, collections

MC = set("""IShowSpeed Druski Sketch Kai Cenat|Dave Portnoy|Pat McAfee|Brandon Walker|Theo Von
Deestroying|Angel Reese|Stephen A. Smith|Cam Wilder|Shannon Sharpe|Elon Musk|Adin Ross|Jynxzi
Plaqueboymax|Logan Paul|Jake Paul|Jesser|Livvy Dunne|Duke Dennis|FlightReacts|Chad Johnson
Flau'jae Johnson|Skip Bayless|Pat Beverley|Tyler1|HasanAbi|YourRAGE|Kevin Hart|Matt Rife
Tristan Jass|Jelly Roll|Andrew Schulz|Bert Kreischer|Cash Nasty|Draymond Green|Filayyyy
Caleb Pressley|Marcelas Howard|Jalen Rose|Caitlin Clark|Snoop Dogg|Alix Earle|Sexyy Red
Agent00|Fanum|Jomboy|Colin Cowherd|Gary Vaynerchuk|xQc|Joe Rogan|Tom Segura|Shane Gillis
Nicki Minaj|Cardi B|Shaquille O'Neal|Magic Johnson|Ice Spice|GloRilla|Ludwig|Kai Trump
Alex Cooper|ImDavisss|Tyrese Haliburton|Cameron Brink|Hailey Van Lith|Will Compton|Taylor Lewan
Bill Simmons|Kevin Durant|DJ Khaled|Rick Ross|Steve Aoki|Mark Cuban|Kyrie Irving|Russell Westbrook
Ryan Trahan|Ja Morant|Trae Young|Mikey Williams|Marshawn Lynch|Master P|Kris London|Bobby Lee
Paige Bueckers|Jordan Lawley|Nick Briz|The Professor|MrBeast|Ninja|Megan Thee Stallion|Lil Baby
Dwyane Wade|Carmelo Anthony|Offset|Lil Yachty|Pokimane|Latto|Diplo|Metro Boomin|Paul George
Valkyrae|Sean O'Malley|Josh Hart|Michael Rubin|Victor Wembanyama|Anthony Edwards|Jack Whitehall
JuJu Watkins|Dwayne Johnson|Charli D'Amelio|Zach King|Will Smith|Ryan Reynolds|Doja Cat
Josh Richards|Steve Harvey|Machine Gun Kelly|James Harden|Quavo|Ludacris|Mark Wahlberg|Future
Jack Harlow|2 Chainz|Jayson Tatum|Jimmy Butler|Gunna|Simone Biles|Triple H|Rhea Ripley
Bailey Zimmerman|Cody Rhodes|Sabrina Ionescu|Jalen Brunson|Suni Lee|Bianca Belair|Jey Uso
Rob McElhenney|A'ja Wilson|Baron Davis|Justin Bieber|LeBron James|Drake|Addison Rae|Bad Bunny
Bella Poarch|Stephen Curry|Travis Scott|Marshmello|John Cena|Post Malone|Markiplier
Giannis Antetokounmpo|Jamie Foxx|Luka Doncic|21 Savage|Serena Williams|Devin Booker|Roman Reigns
Morgan Wallen|Nelly|Scottie Pippen|Naomi Osaka|Jon Jones|Vince Carter|Shaboozey|Sydney McLaughlin
Zion Williamson|Kylie Jenner|Kim Kardashian|Khloe Kardashian|PewDiePie|Tyler, the Creator|SZA
Playboi Carti|Zach Bryan|Brad Paisley|Shai Gilgeous-Alexander|Tracy McGrady|Kamilla Cardoso
Selena Gomez|Kendall Jenner|Jennifer Lopez|Mark Rober|Allen Iverson|Charles Barkley|Ariana Grande
Miley Cyrus|Katy Perry|Billie Eilish|Vin Diesel|Taylor Swift|Rihanna|Barack Obama|The Weeknd
Adam Sandler|Will Ferrell|Eric Church|Zendaya|Beyonce|Michelle Obama|Kendrick Lamar|Dr. Dre
Bill Murray|Jay-Z|Michael Keaton|Michael Jordan|Larry Bird|Quinta Brunson|Lil Dicky|Gillie Da Kid
Wallo267|Nick DiGiovanni|Keith Lee|Kareem Rahma|Caleb Simpson|Nara Smith|Jake Shane
Brittany Broski|Drew Afualo|Trisha Paytas|Bobbi Althoff|Airrack|Michelle Khare|Lex Fridman
Jake Lucky|Jon Rothstein|Kirk Minihane|Jack Mac|Trill Withers|Big Cat|PFT Commenter|Nadeshot
FaZe Rug|Owen Han|Golden Balance|Tini Younger|Joshua Weissman|Ballerina Farm|Haley Kalil
Conor McGregor|Israel Adesanya|Khaby Lame|Cristiano Ronaldo|Lionel Messi|Neymar|Kylian Mbappe
Virat Kohli|David Beckham|KSI|Sidemen|Dude Perfect""".replace("\n", "|").split("|"))
MC = {m.strip() for m in MC if m.strip()}

# (name, category, share, cadence, note)
P = [
# ===== tier of their own =====
("Donald Trump","Politics",10,10,"⭐ Nothing in America is close. Every post is a news event"),
("Elon Musk","Business / politics",10,10,"⭐ Highest raw retweet volume on X most days"),
# ===== 9: national-event accounts =====
("Ye (Kanye West)","Music",9,6,"⚠️ Per-post share velocity may be 2nd only to Trump when active; erratic cadence"),
("IShowSpeed","Creator",9,10,"⭐ Clip economy — thousands of accounts repost him"),
("Kai Cenat","Creator",9,10,""),
("MrBeast","Creator",9,7,"Enormous, but YouTube share mechanics are weak"),
("Charlie Kirk","Politics",9,10,""),
("Barack Obama","Politics",9,3,"Huge per post, very low cadence"),
("Taylor Swift","Music",9,4,"Fandom shares intensely; posts rarely"),
("Candace Owens","Politics",9,9,""),
("Ben Shapiro","Politics",9,9,""),
("AOC","Politics",9,9,""),
("Matt Walsh","Politics",8,9,""),
("Tucker Carlson","Media / politics",9,7,""),
("Marjorie Taylor Greene","Politics",8,9,""),
("JD Vance","Politics",9,8,""),
("Bernie Sanders","Politics",8,8,""),
("Robert F. Kennedy Jr.","Politics",8,7,""),
("Gavin Newsom","Politics",7,8,""),
("Jasmine Crockett","Politics",7,7,""),
("Kamala Harris","Politics",8,6,""),
("Joe Biden","Politics",8,5,""),
("Tim Pool","Politics",7,9,""),
("Megyn Kelly","Media / politics",7,8,""),
("Dan Bongino","Politics",7,8,""),
("Jack Posobiec","Politics",6,9,""),
("Laura Loomer","Politics",6,9,""),
("Vivek Ramaswamy","Politics",6,8,""),
("Ted Cruz","Politics",6,8,""),
("Brian Tyler Cohen","Politics",6,10,""),
("Harry Sisson","Politics",5,10,""),
("Hakeem Jeffries","Politics",5,7,""),
("Nancy Pelosi","Politics",6,5,""),
("Hillary Clinton","Politics",6,5,""),
("Michelle Obama","Politics",7,3,""),
("Tulsi Gabbard","Politics",6,6,""),
("Marco Rubio","Politics",5,7,""),
("Nikki Haley","Politics",5,6,""),
("Josh Hawley","Politics",5,7,""),
# ===== music =====
("Drake","Music",9,6,""),
("Kendrick Lamar","Music",9,3,"2024 beef produced record single-post share volume"),
("Beyonce","Music",8,3,""),
("Rihanna","Music",8,4,""),
("Nicki Minaj","Music",8,8,""),
("Cardi B","Music",8,8,""),
("Sabrina Carpenter","Music",8,7,""),
("Bad Bunny","Music",8,6,""),
("Ariana Grande","Music",8,5,""),
("Billie Eilish","Music",8,5,""),
("SZA","Music",7,5,""),
("Travis Scott","Music",7,6,""),
("Doja Cat","Music",7,7,""),
("Olivia Rodrigo","Music",7,5,""),
("Chappell Roan","Music",7,5,""),
("Megan Thee Stallion","Music",7,8,""),
("Ice Spice","Music",6,8,""),
("Sexyy Red","Music",6,9,""),
("GloRilla","Music",6,8,""),
("Playboi Carti","Music",7,5,""),
("Future","Music",6,7,""),
("Lil Baby","Music",6,8,""),
("21 Savage","Music",6,6,""),
("Metro Boomin","Music",6,8,""),
("Lil Uzi Vert","Music",6,7,"North Philly"),
("Meek Mill","Music",6,8,"North Philly; Rubin's closest partner"),
("Morgan Wallen","Music",7,6,"Biggest audience in country"),
("Zach Bryan","Music",6,5,""),
("Post Malone","Music",7,6,""),
("Jelly Roll","Music",6,8,""),
("Shaboozey","Music",5,6,""),
("Benson Boone","Music",6,7,""),
("Teddy Swims","Music",5,7,""),
("Gracie Abrams","Music",5,6,""),
("Noah Kahan","Music",5,6,""),
("Tyler, the Creator","Music",6,5,""),
("Jack Harlow","Music",5,6,""),
("Lil Yachty","Music",5,8,""),
("Quavo","Music",5,7,""),
("Offset","Music",5,8,""),
("Rick Ross","Music",5,9,""),
("DJ Khaled","Music",5,9,""),
("2 Chainz","Music",4,7,""),
("Latto","Music",5,8,""),
("Machine Gun Kelly","Music",5,7,""),
("Steve Aoki","Music",4,9,""),
("Diplo","Music",4,8,""),
("Marshmello","Music",5,6,""),
("Snoop Dogg","Music",6,9,""),
("Jay-Z","Music",7,2,""),
("Dr. Dre","Music",5,3,""),
("Diddy","Music",8,2,"⚠️ Current share volume is legal-news driven, not content driven"),
("Master P","Music",4,7,""),
("Nelly","Music",4,6,""),
("Ludacris","Music",4,7,""),
("The Weeknd","Music",7,4,""),
("Justin Bieber","Celebrity",8,6,""),
("Selena Gomez","Celebrity",8,6,""),
("Miley Cyrus","Music",7,5,""),
("Katy Perry","Music",6,5,""),
("Jennifer Lopez","Celebrity",6,6,""),
("Eric Church","Music",4,4,""),
("Brad Paisley","Music",4,5,""),
("Bailey Zimmerman","Music",4,7,""),
("Gunna","Music",5,7,""),
# ===== creators =====
("Druski","Creator",8,9,"Content engineered to be reposted"),
("Sketch","Creator",8,9,""),
("Adin Ross","Creator",7,10,""),
("Jake Paul","Creator / boxer",8,9,""),
("Logan Paul","Creator",8,9,""),
("Tyler1","Creator",5,10,""),
("HasanAbi","Creator",6,10,""),
("xQc","Creator",6,10,"Canadian, US-based"),
("Jynxzi","Creator",6,10,""),
("Plaqueboymax","Creator",6,10,""),
("YourRAGE","Creator",5,10,""),
("Duke Dennis","Creator",6,9,"AMP"),
("Fanum","Creator",5,9,"AMP"),
("Agent00","Creator",5,9,"AMP"),
("DDG","Creator / music",6,8,""),
("Kai Trump","Creator",6,8,""),
("Trisha Paytas","Creator",6,9,""),
("Alix Earle","Creator",6,9,""),
("Charli D'Amelio","Creator",7,7,""),
("Dixie D'Amelio","Creator",6,6,""),
("Addison Rae","Creator",6,6,""),
("Bella Poarch","Creator",6,6,""),
("Zach King","Creator",7,7,""),
("Brittany Broski","Creator",6,8,""),
("Jake Shane","Creator",5,8,""),
("Drew Afualo","Creator",5,8,""),
("Bobbi Althoff","Creator",5,7,""),
("Nara Smith","Creator",6,8,"Outrage-driven share rate"),
("Ballerina Farm (Hannah Neeleman)","Creator",6,6,""),
("Keith Lee","Creator / food",7,8,"⭐ Moves entire cities"),
("Nick DiGiovanni","Creator / food",6,8,"Rhode Island; Harvard"),
("Kareem Rahma (SubwayTakes)","Creator",6,8,"⭐ One of the most-shared formats in America"),
("Caleb Simpson","Creator",6,9,""),
("Golden Balance","Creator / food",5,9,""),
("Owen Han","Creator / food",5,9,""),
("Tini Younger","Creator / food",5,8,""),
("Joshua Weissman","Creator / food",5,7,""),
("Emily Mariko","Creator",5,5,""),
("Haliey Welch","Creator",6,7,"⚠️ Viral spike rather than sustained velocity"),
("Jools Lebron","Creator",6,6,"⚠️ Viral spike"),
("Mark Rober","Creator",7,4,""),
("Ryan Trahan","Creator",6,7,""),
("Airrack","Creator",5,7,""),
("Michelle Khare","Creator",5,6,""),
("Ninja","Creator",6,8,""),
("Pokimane","Creator",5,8,""),
("Valkyrae","Creator",5,8,""),
("Markiplier","Creator",6,6,""),
("PewDiePie","Creator",6,5,"Swedish, largely retired"),
("FaZe Rug","Creator",5,8,""),
("Nadeshot","Creator / org",4,8,""),
("Josh Richards","Creator",5,7,""),
("Ludwig","Creator",5,8,""),
("Jake Lucky","Creator / news",6,10,""),
("Keemstar","Creator / news",5,9,""),
("Haley Kalil","Creator",5,9,""),
("Deestroying","Sports creator",5,9,"Lost NCAA eligibility over YouTube income"),
("Cam Wilder","Hoops creator",4,9,""),
("Jesser","Hoops creator",5,9,"2HYPE"),
("FlightReacts","Hoops creator",5,9,""),
("Tristan Jass","Hoops creator",5,8,""),
("Cash Nasty","Hoops creator",4,8,"2HYPE"),
("Kris London","Hoops creator",4,7,"2HYPE"),
("Marcelas Howard","Hoops creator",4,8,""),
("ImDavisss","Hoops creator",4,8,""),
("Filayyyy","Hoops creator",4,8,""),
("Jordan Lawley","Hoops creator",3,7,""),
("Nick Briz","Hoops creator",3,7,""),
("The Professor","Hoops creator",5,6,""),
# ===== athletes =====
("LeBron James","Basketball",8,6,""),
("Stephen Curry","Basketball",8,6,""),
("Caitlin Clark","Basketball",8,7,"⭐ Tribal share rate is extraordinary"),
("Shohei Ohtani","Baseball",8,4,"Japanese, US-based; enormous international share volume"),
("Travis Kelce","Football",8,7,""),
("Patrick Mahomes","Football",7,6,""),
("Deion Sanders","Coach",7,9,"⭐ Coach Prime posts are shared constantly"),
("Shedeur Sanders","Football",6,7,""),
("Angel Reese","Basketball",7,9,""),
("Shaquille O'Neal","Basketball",6,8,""),
("Kevin Durant","Basketball",6,9,""),
("Giannis Antetokounmpo","Basketball",7,6,"Greek, US-based"),
("Victor Wembanyama","Basketball",7,6,"French, US-based"),
("Luka Doncic","Basketball",7,6,"Slovenian, US-based"),
("Ja Morant","Basketball",6,7,""),
("Anthony Edwards","Basketball",6,6,""),
("Jayson Tatum","Basketball",6,7,""),
("Tyrese Haliburton","Basketball",5,8,""),
("Draymond Green","Basketball / media",6,8,""),
("Kyrie Irving","Basketball",6,7,""),
("Russell Westbrook","Basketball",5,7,""),
("James Harden","Basketball",5,7,""),
("Devin Booker","Basketball",5,6,""),
("Jimmy Butler","Basketball",5,7,""),
("Zion Williamson","Basketball",6,5,""),
("Trae Young","Basketball",5,7,""),
("Shai Gilgeous-Alexander","Basketball",6,5,"Canadian, US-based"),
("Jalen Brunson","Basketball",4,7,""),
("Josh Hart","Basketball",4,8,""),
("Paul George","Basketball",4,8,""),
("Bronny James","Basketball",6,5,""),
("Cooper Flagg","Basketball",6,5,""),
("Mikey Williams","Basketball",4,6,""),
("Michael Jordan","Basketball",7,2,""),
("Magic Johnson","Basketball / business",5,8,""),
("Allen Iverson","Basketball",5,4,""),
("Carmelo Anthony","Basketball / media",5,8,""),
("Dwyane Wade","Basketball / media",5,8,""),
("Scottie Pippen","Basketball",4,6,""),
("Vince Carter","Basketball",4,6,""),
("Tracy McGrady","Basketball",4,5,""),
("Baron Davis","Basketball",3,7,""),
("Larry Bird","Basketball",4,1,""),
("Paige Bueckers","Basketball",6,7,""),
("JuJu Watkins","Basketball",5,6,""),
("A'ja Wilson","Basketball",5,7,""),
("Napheesa Collier","Basketball",5,6,""),
("Sabrina Ionescu","Basketball",5,7,""),
("Cameron Brink","Basketball",5,8,""),
("Flau'jae Johnson","Basketball",5,9,""),
("Hailey Van Lith","Basketball",4,8,""),
("Kamilla Cardoso","Basketball",3,5,""),
("Lamar Jackson","Football",6,5,""),
("Josh Allen","Football",6,5,""),
("Saquon Barkley","Football",6,6,""),
("Micah Parsons","Football",6,8,""),
("Tyreek Hill","Football",6,7,""),
("Jason Kelce","Football / media",6,6,"Philadelphia"),
("Tom Brady","Football / media",7,6,""),
("Marshawn Lynch","Football",5,7,""),
("Chad Johnson","Football / media",5,9,""),
("Aaron Judge","Baseball",5,4,""),
("Juan Soto","Baseball",5,5,""),
("Serena Williams","Tennis",7,6,""),
("Coco Gauff","Tennis",5,6,""),
("Naomi Osaka","Tennis",5,6,"Japanese, US-based"),
("Simone Biles","Gymnastics",7,7,""),
("Suni Lee","Gymnastics",4,7,""),
("Sha'Carri Richardson","Track",6,7,""),
("Noah Lyles","Track",5,7,""),
("Sydney McLaughlin","Track",4,6,""),
("Ilona Maher","Rugby / creator",6,8,"⭐ One of the fastest-rising share engines in US sport"),
("Livvy Dunne","Gymnastics / creator",6,9,""),
("Tiger Woods","Golf",7,3,""),
("Scottie Scheffler","Golf",4,4,""),
("Bryson DeChambeau","Golf",6,7,""),
("Jon Jones","MMA",6,6,""),
("Sean O'Malley","MMA",5,8,""),
("Dustin Poirier","MMA",5,6,""),
("Ryan Garcia","Boxing",6,9,""),
("Gervonta Davis","Boxing",5,7,""),
("Terence Crawford","Boxing",4,6,""),
("John Cena","Wrestling",6,6,""),
("Roman Reigns","Wrestling",6,6,""),
("Triple H","Wrestling",5,7,""),
("Cody Rhodes","Wrestling",5,7,""),
("Rhea Ripley","Wrestling",5,7,""),
("Jey Uso","Wrestling",5,7,""),
("Bianca Belair","Wrestling",4,7,""),
# ===== media / commentary =====
("Dave Portnoy","Media / business",6,10,""),
("Pat McAfee","Sports media",6,10,""),
("Stephen A. Smith","Sports media",6,9,""),
("Shannon Sharpe","Sports media",6,9,""),
("Skip Bayless","Sports media",5,9,""),
("Colin Cowherd","Sports media",5,9,""),
("Bill Simmons","Sports media",5,8,""),
("Charles Barkley","Sports media",6,3,"Real channel is live TV, not social"),
("Jalen Rose","Sports media",4,8,""),
("Pat Beverley","Sports media",5,9,""),
("Jomboy","Sports media",5,9,""),
("Brandon Walker","Sports media",5,10,"⚠️ Was 4th in the prior build. Honest placement is here"),
("Big Cat (Dan Katz)","Sports media",5,9,""),
("PFT Commenter","Sports media",5,9,""),
("Jack Mac","Sports media",4,9,""),
("Trill Withers","Sports media",4,9,""),
("Caleb Pressley","Sports creator",6,8,""),
("Will Compton","Sports creator",5,8,""),
("Taylor Lewan","Sports creator",5,8,""),
("Ryan Whitney","Sports creator",5,8,"Scituate MA"),
("Kirk Minihane","Sports media",4,9,"Massachusetts"),
("Jon Rothstein","College hoops media",4,10,""),
("Joe Lunardi","College hoops media",4,8,""),
("Don Lemon","Media",5,8,""),
# ===== comedy / podcast hosts =====
("Joe Rogan","Podcast",8,7,""),
("Theo Von","Comedy",7,9,""),
("Andrew Schulz","Comedy",6,8,""),
("Shane Gillis","Comedy",6,7,"Philly-area roots"),
("Matt Rife","Comedy",6,8,""),
("Tom Segura","Comedy",6,8,""),
("Bert Kreischer","Comedy",5,8,""),
("Bobby Lee","Comedy",5,7,""),
("Alex Cooper","Podcast",6,8,"Bucks County PA; Boston University"),
("Gillie Da Kid","Podcast",5,8,"North Philly"),
("Wallo267","Podcast",5,8,"North Philly"),
("Lex Fridman","Podcast",5,5,"MIT / Cambridge"),
("Steve Harvey","Media",5,7,""),
("Jack Whitehall","Comedy",4,6,"British"),
# ===== business / finance / tech =====
("Mark Cuban","Business",7,9,""),
("Bill Ackman","Finance",7,9,"⭐ Very high retweet velocity on X"),
("Michael Saylor","Finance",6,9,""),
("Sam Altman","Tech",7,6,""),
("Mark Zuckerberg","Tech",7,5,""),
("Jeff Bezos","Tech",7,4,""),
("Jensen Huang","Tech",6,3,""),
("Cathie Wood","Finance",5,7,""),
("Chamath Palihapitiya","Finance",5,7,""),
("Naval Ravikant","Tech",6,5,""),
("Gary Vaynerchuk","Business",5,10,""),
("Michael Rubin","Business",5,8,"Convening, not sharing, is his asset"),
# ===== actors / entertainment =====
("Dwayne Johnson","Celebrity",8,7,""),
("Kevin Hart","Celebrity",7,8,"Philadelphia"),
("Will Smith","Celebrity",7,7,"West Philadelphia"),
("Ryan Reynolds","Celebrity",7,7,"Canadian, US-based"),
("Zendaya","Celebrity",8,4,""),
("Timothee Chalamet","Celebrity",7,4,""),
("Sydney Sweeney","Celebrity",7,6,""),
("Jenna Ortega","Celebrity",7,5,""),
("Millie Bobby Brown","Celebrity",7,6,"British, US-based"),
("Pedro Pascal","Celebrity",6,5,""),
("Glen Powell","Celebrity",6,6,""),
("Kim Kardashian","Celebrity",8,7,""),
("Kylie Jenner","Celebrity",8,7,""),
("Kendall Jenner","Celebrity",7,6,""),
("Khloe Kardashian","Celebrity",7,7,""),
("Kris Jenner","Celebrity",6,6,""),
("Hailey Bieber","Celebrity",7,7,""),
("Adam Sandler","Celebrity",6,4,""),
("Will Ferrell","Celebrity",5,4,""),
("Mark Wahlberg","Celebrity",5,7,""),
("Vin Diesel","Celebrity",5,5,""),
("Bill Murray","Celebrity",4,3,""),
("Michael Keaton","Celebrity",3,3,""),
("Jamie Foxx","Celebrity",5,6,""),
("Rob McElhenney","Celebrity",5,7,"Philadelphia native"),
("Quinta Brunson","Celebrity",5,6,"West Philadelphia"),
("Lil Dicky","Celebrity",5,5,"Philly suburb"),
("Tina Fey","Celebrity",5,4,"Upper Darby PA"),
("Conan O'Brien","Celebrity",6,5,"Brookline MA"),
("John Krasinski","Celebrity",6,4,"Newton MA"),
("Bill Burr","Comedy",5,6,"Canton MA"),
("Mindy Kaling","Celebrity",5,5,"Cambridge MA"),
("Meghan Trainor","Music",5,7,"Nantucket MA"),
("SteveWillDoIt","Creator",6,7,"Danbury CT"),
("Sarah Silverman","Comedy",5,6,"NH"),
("Seth Meyers","Comedy",6,6,"Bedford NH"),
("Dana White","Business",6,8,"Boston-adopted"),
("Rob Gronkowski","Football",6,6,"Patriots"),
("Julian Edelman","Football / media",5,6,"Patriots"),
("Jaylen Brown","Basketball",5,7,"Celtics"),
("Kevin Garnett","Basketball / media",5,7,"Celtics"),
("Amy Poehler","Celebrity",5,4,"BC '93"),
("Steve Carell","Celebrity",5,3,"Acton MA"),
("Elizabeth Banks","Celebrity",5,5,"Pittsfield MA"),
("Aly Raisman","Gymnastics",4,5,"Needham MA"),
("Seth MacFarlane","Celebrity",5,5,"Kent CT"),
("Questlove","Music",4,7,"Philadelphia"),
("M. Night Shyamalan","Celebrity",5,4,"Philadelphia"),
("P!nk","Music",6,5,"Doylestown PA"),
("Bam Margera","Creator",5,7,"West Chester PA"),
("DJ Jazzy Jeff","Music",3,6,"West Philadelphia"),
("Tierra Whack","Music",3,6,"Philadelphia"),
("Armani White","Music",3,7,"West Philadelphia"),
("Fridayy","Music",3,6,"Philadelphia"),
("2Rare","Music",3,7,"Philadelphia"),
("Philly Boy Jay","Creator",3,6,"Philadelphia"),
("Rich Rebuilds","Creator",4,6,"Massachusetts"),
("Brianna Chickenfry","Creator",5,8,"Massachusetts"),
("Jerry Thornton","Sports media",3,8,"Boston"),
("Jenna Marbles","Creator",5,2,"BU; retired 2020"),
("Casey Neistat","Creator",5,5,"Gales Ferry CT"),
("Dixie Chicks / n-a","Music",1,1,"placeholder-removed"),
]

P = [t for t in P if t[0] != "Dixie Chicks / n-a"]
seen, rows = set(), []
for t in P:
    if t[0] in seen:
        continue
    seen.add(t[0]); rows.append(t)
for n, c, s, cad, note in rows:
    assert 1 <= s <= 10 and 1 <= cad <= 10, n

# ⭐ THE FIX over the first attempt: SHARE is a LOG scale (each step ~3x) and cadence is
# LINEAR, so multiplying the two indexes compressed a ~250x real gap between Trump and a
# niche account into 2x. Convert both to absolute units and multiply those instead.
SHARES_PER_POST = {10:750_000, 9:250_000, 8:55_000, 7:18_000, 6:6_000, 5:1_800, 4:600, 3:200}
POSTS_PER_DAY   = {10:8, 9:4, 8:2, 7:1, 6:0.5, 5:0.3, 4:0.15, 3:0.07, 2:0.03, 1:0.01}
def daily(s_idx, c_idx):
    return SHARES_PER_POST[s_idx] * POSTS_PER_DAY[c_idx]
rows.sort(key=lambda t: (-daily(t[2], t[3]), -t[2], t[0]))

first = 14                      # 12 header lines + 1 blank + 1 column header
last = first + len(rows) - 1
buf = io.StringIO(); w = csv.writer(buf)
w.writerow(["US INDIVIDUAL ACCOUNTS RANKED BY SHARE VELOCITY"])
w.writerow(["Built top-down from the country. NOT filtered or scored for Making Cinderella — the prior version was, and that was the error."])
w.writerow(["⚠️ ESTIMATES. Share counts are not public on most platforms. SHARE is an ABSOLUTE scale: estimated shares/retweets on a typical well-performing post."])
w.writerow(["SHARE  10 = >500k (Trump, Musk) · 9 = 100-500k · 8 = 30-100k · 7 = 10-30k · 6 = 3-10k · 5 = 1-3k · 4 = 300-1k · 3 = <300"])
w.writerow(["⭐ EST_SHARES_PER_DAY is the ranking metric = (est. shares per post) x (est. posts per day)."])
w.writerow(["⚠️ Multiplying the 1-10 indexes together was WRONG and produced the previous bad ranking: SHARE is logarithmic and cadence is linear, so a ~250x real gap between Trump and a niche account compressed into 2x. Hence absolute units."])
w.writerow(["Conversion — SHARE: 10=750k 9=250k 8=55k 7=18k 6=6k 5=1.8k 4=600 3=200 shares/post. Cadence: 10=8 9=4 8=2 7=1 6=0.5 5=0.3 4=0.15 3=0.07 2=0.03 1=0.01 posts/day."])
w.writerow(["SCOPE: individuals only. No aggregators, brands, leagues or podcast properties — no Barstool, House of Highlights, NBA, Pardon My Take, Dude Perfect, Sidemen. A podcast HOST is in; the show is not."])
w.writerow(["US-based. Non-US-born athletes in US leagues are included and flagged (Ohtani, Giannis, Wembanyama, Doncic, SGA). Fully non-US accounts excluded (Ronaldo, Messi, KSI, Khaby, McGregor, Adesanya, Peterson)."])
w.writerow(["⚠️ Avowed extremist accounts are omitted — an editorial call, stated so it is visible. ⚠️ NOT EXHAUSTIVE: an estimated top ~370, not every individual account in America."])
w.writerow(["In_MC_List is neutral cross-reference metadata only. It does NOT affect the ranking."])
w.writerow(["Overwrite any SHARE or Cadence cell to substitute your own judgment; the per-post / per-day columns are lookups you can also overwrite, and Rank recalculates."])
w.writerow([])
w.writerow(["Rank", "Name", "Category", "SHARE_1_10", "Cadence_1_10", "Est_Shares_Per_Post",
            "Est_Posts_Per_Day", "EST_SHARES_PER_DAY", "In_MC_List", "Note"])
for i, (n, c, sh, cad, note) in enumerate(rows):
    x = first + i
    w.writerow([f"=RANK(H{x},H${first}:H${last})", n, c, sh, cad,
                SHARES_PER_POST[sh], POSTS_PER_DAY[cad], f"=F{x}*G{x}",
                "Yes" if n in MC else "", note])
t = buf.getvalue()
open("v8-us-individuals.csv", "w", encoding="utf-8").write(t)

print(f"{len(rows)} individuals | data rows {first}-{last} | {len(t):,} bytes")
print(f"in MC list: {sum(1 for r in rows if r[0] in MC)} of {len(rows)}\n")
print("=== TOP 25 ===")
for i, (n, c, sh, cad, note) in enumerate(rows[:25], 1):
    print(f"{i:3d} {daily(sh,cad):>10,.0f}/day  {n}  [{c}]")
print()
for name in ("Caitlin Clark","Dave Portnoy","Stephen A. Smith","Brandon Walker",
             "Ryan Reynolds","Michael Rubin","Cam Wilder","Larry Bird"):
    k=[i for i,r in enumerate(rows,1) if r[0]==name][0]
    r=[r for r in rows if r[0]==name][0]
    print(f"  #{k:3d}  {daily(r[2],r[3]):>9,.0f}/day  {name}")
