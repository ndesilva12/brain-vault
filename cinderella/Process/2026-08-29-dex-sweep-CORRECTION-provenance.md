# Dex Sweep — Correction & Provenance Audit
_2026-08-29. **Supersedes the headline finding in `2026-08-29-dex-notable-names-sweep.md`.**
Written after Norman challenged two claims. He was right on both._

---

## 1. THE HEADLINE FINDING WAS WRONG

I reported that **13 celebrities from the Making Cinderella shortlist are "already in your
contacts."** That framing does not survive an audit of where those records came from.

**12 of the 14 are Instagram follows with no phone, no email, and no relationship.**

| Name | Actually stored as |
|---|---|
| Adam Sandler | Instagram Contacts — no phone, no email |
| Paul "Triple H" Levesque | Instagram Contacts — no phone, no email |
| Paul Wight | Instagram Contacts — no phone, no email |
| Shawn Michaels | Instagram Contacts — no phone, no email |
| Bruno Mars | Instagram Contacts — no phone, no email |
| Darius Rucker | Instagram Contacts — no phone, no email |
| Eric Church | Instagram Contacts — no phone, no email |
| Kevin Hart | Instagram Contacts — no phone, no email |
| Walton Goggins | Instagram Contacts — no phone, no email |
| Bill Simmons | Instagram Contacts — no phone, no email |
| Shane Gillis | Instagram Contacts — no phone, no email |
| Jason Sudeikis | Instagram Contacts — no phone, no email |
| **Eli Thomas** | **Phone import — mobile AND email. REAL.** |
| **Sebastian Maniscalco** | **Phone import — mobile. REAL.** |

**How I know the Instagram group is a follow list, not a contact list.** It holds 127 records.
Roughly 20 of them are fraternity chapter accounts — `MIT Sigma Chi`, `Chi Phi at Boston
University`, `Northeastern Delt | ΔΤΔ`, `Phi Beta Epsilon`, `Pi Kappa Alpha`. Others are bare
handles: `courtsidedrip`, `billyred21`, `listid`, `Instagram user`, `con•nect•or`. A fraternity
chapter account is not a person Norman knows. This group is who he **follows**, synced into Dex.

**What this means:** the New Hampshire "fully connected school" claim was half wrong. The AD
(Ryan Colton, phone) and the head coach (Nathan Davis, phone + email) are real. Both celebrities
attached to that school — Sandler and Triple H — are Instagram follows. The school-side access is
genuine; the celebrity side is not.

**The two that survive are still worth acting on.** Eli Thomas at Happy Madison, with a live
mobile, remains the single best unused path to Sandler — and it is now the *only* Sandler path in
the database.

---

## 2. WHY SO MANY RECORDS SHOW ONLY A NAME

Norman's instinct was correct: he did not type thousands of names into his phone without contact
information. He didn't. Those records aren't from his phone.

**Where the 12,106 records come from:**

| Source group | Records | % of DB | Have a phone or email |
|---|---:|---:|---:|
| Mobile import (2026-08-29) | 8,108 | 67.0% | **78.4%** |
| Facebook Friends | 3,491 | 28.8% | **0.0%** |
| Instagram Contacts | 127 | 1.0% | **0.0%** |
| No group | 380 | 3.1% | 73.7% |

**3,618 records — 30% of the database — are social-graph syncs that carry a name and a profile
photo and nothing else.** That is the entire explanation for the "name only" phenomenon.

**Field fill rates across all 12,106 records:**
`full_name` 99.8% · `dex_email` 36.6% · `facebook` 29.1% · `dex_phone` 22.1% ·
`company` 18.3% · `job_title` 18.0% · `linkedin` 3.0% · `location` 2.6%

**My own sloppiness compounded this.** When I wrote "bare name," I meant *no job title, company,
or location* — the fields that let you identify who someone is. I let that read as *no contact
information at all*. Those are different claims and I should have separated them. Dwyane Wade
has a phone number in this database; what he lacks is a job title.

---

## 3. THE FILTER ERROR — I WRONGLY DISCARDED 3,014 REAL CONTACTS

I reported 12,106 → 8,650 "plausible people," implying ~3,456 junk records. That was wrong.

**What actually got dropped, and why:**

| Reason | Count | Was it right? |
|---|---:|---|
| Matched my business/junk word list | 3,047 | **Mostly WRONG — see below** |
| Single name only, no last name (`Vito`, `Whalen`, `Yumi`) | 375 | Right — unidentifiable |
| No name at all (blank) | 22 | Right |
| Too many non-letter characters | 10 | Right |
| Name under 4 characters | 2 | Right |

**The error:** my junk pattern began with `^track\b`. I assumed "Track…" meant call-tracking
noise. It does not — **it is a Dex prefix on real contact records.** There are 3,014 of them and
**100% have a phone number or an email address.**

Breaking those 3,014 down:
- **1,506** are a bare email address used as the name (`Track william.kilmer@c5capital.com`) — low value as names, but they are real addresses
- **1,142** duplicate a record I had already read under its clean name
- **366 are people I never saw at all**

**So the honest count of genuinely unusable records is roughly 440**, not 3,456 — main office
numbers, fax lines, voicemail entries, a printer, radio frequencies (`98.5`, `103.7`), and 22
blanks. Everything else was either a real person or a duplicate.

---

## 4. WHAT THE RECOVERED 366 CONTAIN

Names of consequence that the filter error hid, all reachable:

**The most important recovery — ⭐ BILL DUFFY.** Founder of BDA Sports and **Steve Nash's
longtime agent.** The vault's Santa Clara row reads *"Steve Nash (verified alum; via Unanimous /
WME→Bill Duffy / CTRL direct)."* Norman has Bill Duffy directly. That converts a three-hop
routing plan into a one-hop call. Kerry Keating (Santa Clara, phone) is the other half.

**⭐ David Preschlack (NBCUniversal)** — President of NBC Sports. A buyer, and one not currently
on the buyer map in `2026-08-28-partner-buyer-landscape-and-network-map.md`. Also recovered:
**Princell Hair** and **Danielle Dancy**, both NBCUniversal.

**NBA front office — a serious tier:**
Koby Altman (President of Basketball Ops, Cleveland) · Tim Connelly (President of Basketball Ops,
Minnesota) · Austin Ainge (President of Basketball Ops, Utah) · Ryan McDonough (former GM,
Phoenix) · Ben Tenzer (EVP Basketball Ops, Denver) · Dan Padover (2x WNBA Executive of the Year) ·
Stu Lash · Chris Alpert · Brett Brown (former Head Coach, Philadelphia) · **Monty Williams**
(NBA Coach of the Year) · David Benner (Indiana Pacers)

**⭐ Chris Brickley** — the celebrity NBA trainer (Durant, Carmelo, JR Smith). His gym is the
single densest celebrity-athlete crossover room in New York. Direct talent-access value.
Also: **Damon Jones** (former NBA player, longtime LeBron associate), **Michael Conley Sr.**
(Olympic gold medalist and agent), JaKarr Sampson, Mitch Butler, Victor Rudd.

**Capital and media:**
Jon Steinberg (founder of Cheddar; former President of BuzzFeed) · David Hornik (Lobby Capital,
formerly August Capital) · Ben duPont (venture) · Skip Fleshman · Etan Butler (Dalton Capital) ·
Michael Duda (Bullish) · Breanden Beneschott (co-founder, Toptal) · Joseph R. Paolino Jr.
(former Mayor of Providence; developer) · Richard Baccari II (developer) · Michael Woodruff
(Partner, Faegre Drinker) · Marc Trachtenberg · Tyneeha Rivers

---

## 5. WHAT SURVIVES THE AUDIT — AND IS STRONGER THAN I FRAMED IT

The celebrity headline collapsed. **The basketball network did not.** Nearly every name in the
athlete and front-office lanes is reachable by phone or email:

**Players with a live phone number:** Dwyane Wade · Devin Harris · Deron Williams · Carlos
Boozer · Antoine Walker · Caron Butler · Channing Frye · Corey Maggette · Dee Brown · Jason
Terry · Josh Howard · Leandro Barbosa · Sam Cassell · TJ McConnell · Xavier Henry · Patrick
Ewing Jr. · Omar Cook · Andre Ingram · Marqus Blakely · Matt Bullard · Nolan Smith
**Phone + email:** Allan Houston · Nick Van Exel · Kevin Gamble · Malcolm Lee · Earl Watson ·
Mike Batiste · Rahlir Hollis-Jefferson · D.J. Seeley
**Email:** Baron Davis · B.J. Armstrong · Brian Scalabrine · Omar Wilkes · Vittorio Gallinari

**Front office, reachable:** Sam Hinkie (phone) · Mike Zarren (phone + email) · Leon Rose
(email) · Joe Dumars (phone) · Jon Horst (phone + email) · Tommy Sheppard · Justin Zanik · Rob
Hennigan · Milt Newton · Jonnie West · Mark Daigneault · Kevin Young · Nate Bjorkgren ·
Jay Larranaga · Mike Gansey · Ben Falk · Dave Lewin · Gianluca Pascucci

**Priority targets that held up:** Rich Kleiman (email) · Geoff Chow (email) · Rob DeAngelis
(email) · Corey Smyth (email) · Darren Prince (phone + email) · Eric Newman (phone) · Connor
Schell (phone) · Steve Pagliuca (phone) · Arn Tellem (email) · Tim Grover (email) · Mark
Bartelstein (email) · Sam Goldfedder (phone) · Chris Clunie (phone) · Billy Lange (phone +
email) · Ryan Colton (phone) · Nathan Davis (phone + email) · Kerry Keating (phone)

**Priority targets that fell out (social-follow only, no contact info):**
Ari Emanuel (Instagram) · Jonny Shipes (Instagram) · Will Dawkins (Facebook) ·
Todd Dos Reis (Facebook)

**Other marquee names that are real and reachable:** Chamath Palihapitiya (email) · Vivek
Ramaswamy (phone + email) · Bud Selig (phone) · Dana Perino (phone) · Tony Romo (phone) ·
Gary Vaynerchuk (phone) · Ken Jeong (phone) · Aaron Paul (phone) · Karyn Parsons (phone) ·
Josh Altman (phone + email) · Tarek El Moussa (phone) · Dane DiLiegro (phone + email) ·
Shane Douglas (phone + email) · Peter Billingsley (phone) · Patrick Bet-David (phone)

**Marquee names that are social-follow only:** Tom Brady (FB) · Mike Tyson (FB) · Kyrie Irving
(IG) · Lori Greiner (IG) · Patton Oswalt (IG) · Denis Leary (IG) · Jason Alexander (IG) ·
Taylor Schilling (FB) · Gary Brecka (IG) · Dean Graziosi (IG) · Will Bynum (FB) ·
Terence Stansbury (FB) · Jerome Randle (FB) · Jordan McRae (FB)

---

## 6. THE RULE THIS ESTABLISHES

**Provenance is a required field on every future contact sweep.** A name in this database means
one of three very different things:

1. **Phone import with a number or address** — a real contact, worth an outreach decision
2. **Facebook Friends / Instagram Contacts with nothing else** — a follow or a loose social
   connection. Not a path to anyone.
3. **Phone import with no number or address** — a name-only remnant; treat as unidentifiable

Never again report a name-match as network access without saying which of the three it is.
