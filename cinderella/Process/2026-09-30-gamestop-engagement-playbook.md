# Manufacturing the "GameStop" effect — playbook

_2026-09-30. Fried's pitch (call #2) was that MC should build **real-time collective energy** rather
than borrow a celebrity's name. This is the menu for doing that, split by whether it takes money
from fans. Companion to `legal/2026-09-30-fan-funded-spv-securities-analysis.md`._

---

## First — the real constraints on a tradeable token, ranked

Disclosure is **one** constraint, not the main one:

| Rank | Constraint | Detail |
|---|---|---|
| **1** | ⚠️ **Cost and time** | Reg A+ Tier 2 is **$100–300K and 4–8 months**, with an unpredictable SEC comment cycle. Against a **$1.5M** seed that is 7–20% of the raise. **This is the binding constraint, not disclosure** |
| **2** | ⚠️ **Section 12(a)(2) liability** | Reg A+ exposes officers and directors personally for material misstatements — on a speculative venture with **no operating history**. Real exposure, not paperwork |
| **3** | **Form 1-A material-contract exhibits** | The school agreement and talent deals become public. **School and talent consent-dependent.** Reg CF's Form C does **not** require this |
| **4** | **Audited financials of a shell** | A newly formed SPV with no revenue is auditable but thin, and "no operating history" is itself a disclosure item |
| **5** | **Perpetual reporting** | Form 1-K annual and 1-SA semi-annual, forever |
| **6** | **Season timing** | Qualification must start roughly a year before the season it funds |

## Is a tradeable tokenised SPV stake legally OK? Yes — with four pieces in place

Not a grey area. A known path with known vendors.

1. **An exempt or qualified offering** — **Reg A+ Tier 2** for free tradability (Reg CF locks resale
   for 12 months).
2. **A registered transfer agent** maintaining the holder record — Securitize is both.
3. **A registered broker-dealer + ATS** as the trading venue — **Securitize, tZERO, INX, Texture
   Capital.** ⚠️ **Minting on a public chain and letting people trade on an open NFT marketplace is
   operating an unregistered exchange. That is the line.**
4. **KYC/AML onboarding** of every holder.

⭐ **Architecture point: put the token on a FEEDER, never on the SPV itself.** The tradeable token
represents an interest in a feeder vehicle that holds **one** SPV stake. Otherwise a freely traded
cap table collides with the school's approval rights, the talent's approval rights, the drag-along,
and NCAA questions about who controls the payor. **With a feeder, the SPV cap table never moves.**

---

## A. NO money from fans

### ⭐⭐ A1. The Adoption Draft — the single best idea here

Before the season, **let the internet vote on which school gets the investment.** Eight candidate
programs, bracket format, multi-week.

Why it is the strongest play on the list:
- **Free, and it is mass audience acquisition** — eight fanbases mobilise themselves.
- **It inverts the sales problem.** Instead of Norman persuading schools, schools' fanbases campaign
  to be chosen. ADs stop being gatekeepers and become applicants.
- **The winner arrives with a mandate**, which is the emotional core of the Wrexham story.
- ⭐ **It is episode one.** The selection becomes the show's opening arc rather than backstory.
- It is the cleanest possible answer to HBO's Bentley Weiner brief — *"what does it interrogate?"*

⚠️ Run it on schools that have **already signed LOIs** so no outcome is a false promise. We have
four: Davidson, St. Joseph's, Belmont, Merrimack.

### A2. Bounded fan governance
Real votes with visible outcomes, none touching competition: **walk-out song · alternate jersey ·
which charity gets game proceeds · the non-conference guarantee-game opponent · warm-up shirt
slogan.** Never minutes, lineups or roster decisions — that is coaching, and NCAA institutional
control depends on it staying that way.

### A3. Open books as content
A **live public dashboard**: roster budget committed vs. spent, sponsor count, revenue to date,
tickets sold, NIL deployed. **GameStop energy came partly from watching a number move.** Transparency
is cheap content and it is differentiating — nobody in college sports does this.

### A4. Name the villain
GameStop needed short sellers. Our thesis already has an antagonist —
**"capital going to a school the system never let win."** Make it explicit: the blue bloods, the
cap, the programs that say this shouldn't be allowed. A movement needs an opponent.

### A5. Numbered free membership
Free signup, permanently numbered. **"Member #1,847."** Costs nothing, creates identity and
hierarchy, and rewards being early — the same mechanic as an early Bitcoin address or a Wrexham
season-ticket number.

### A6. The fan content pipeline
Best fan edit airs **in the show.** Creates an unpaid marketing army competing for a slot, and
supplies the production with free material.

### A7. Witnessed decisions
Norman makes real basketball decisions **on camera with chat present.** Not fan-controlled — fan-
witnessed. That distinction is what makes Twitch work and it keeps institutional control clean.

### A8. Earned tiers
Status unlocked by engagement — watching, sharing, attending — never purchased. Gamified standing
with zero transaction.

---

## B. MONEY from fans, still NO securities law

The rule: **sell a product or a perk, never a return.**

### ⭐⭐ B1. Rewards-based crowdfunding — the best money answer
**Kickstarter/Indiegogo model.** Backers get a product or experience, not a share of profits, so it
is **not a securities offering.** Well-trodden, and seven-figure campaigns are routine.

Fund **specific line items**, which is far more compelling than "fund the team":
the charter flight for the conference tournament · the video board · the shooting machine · the
team's pregame meal for a named road game · the alternate uniforms fans voted on.

Every backer gets a receipt saying **exactly what their money bought.** That is the GameStop
feeling — collective action with a visible, attributable result — with no SEC involvement at all.

### B2. Buy a piece of the building
Name on a floorboard, a seatback, a banner, the tunnel. **$100–$1,000.** Physical, permanent,
photographable, and schools already sell exactly this so the compliance path is known.

### B3. Merch where the margin is the story
Fans buy the jersey; the SPV's cut funds the roster, with a **public counter**: *"this drop funded
$318,000 of the roster."* A purchase, not an investment.

### B4. Named micro-sponsorships
**$500 buys your name on the broadcast** for one road trip. This is **advertising inventory** — the
same thing we sell a brand, sold in small units. Not equity, and it reinforces the FMV architecture
in `2026-09-13-nil-sponsor-architecture-and-pcsa.md`.

### B5. All-access subscription
A paid tier above the show: raw footage, film sessions, **Norman's actual scouting notes**, practice
streams. Recurring revenue, and it monetises material the production generates anyway.

### B6. Auctioned scarcity
Sit on the bench · ride the bus · sit in the film room · shoot at halftime. High-ticket, genuinely
scarce, **and each one is itself content.**

### B7. Priority rights
Presale windows, playoff ticket priority, travel packages. High margin, and if the team wins these
become very valuable — which produces the *feeling* of upside **without conveying any.**

### ❌ Do not
A revenue share, a profit share, or anything described as a "bond." Those are securities. If real
economics are wanted, use §A of the legal memo properly rather than dressing a security as a perk.

---

## ⭐ The ladder — how they compose

| Tier | Size | Instrument | Legal load |
|---|---|---|---|
| **Free** | Millions | Numbered membership, votes, dashboard | **None** |
| **Small $** | Tens of thousands | Rewards crowdfunding, merch, floorboards | **None** |
| **Real $** | Thousands | Reg CF (~$5M, 12-mo lock) | Moderate |
| **Tradeable** | Hundreds | Reg A+ token on a registered ATS | **Heavy** |

⭐ **Build bottom-up.** The free and rewards tiers cost nothing legally and deliver the thing that
actually matters — **audience**. They also *prove demand*, which is the only honest basis for
spending $200K on a Reg A+ qualification later. **Do not start at the top of the ladder.**

---
---

# ADDENDUM 2026-09-30 — Norman's follow-ups

## Where the $100–300K comes from, and the correction he is owed

Reg A+ Tier 2 components: securities counsel drafting Form 1-A **$50–150K** · PCAOB-standard audited
financials **$15–50K** · EDGAR/financial printer **$5–15K** · transfer agent setup **$5–15K/yr** ·
platform or broker-dealer fee often **3–7% of the raise** · then **$30–75K/yr** ongoing for the
1-K/1-SA and annual audit.

⚠️ **Norman is right that the SPV, not the $1.5M parent raise, is where token equity would sit.**
**But the fees land before the raise closes, and the SPV has no cash until it does.** So the money
comes from the parent's $1.5M or from a capital partner. **That chicken-and-egg is the real
constraint — not the percentage arithmetic I used.**

## Reg CF vs. Reg D for non-accredited fans

| | **Reg CF** ⭐ | **506(b)** | **Rule 504** |
|---|---|---|---|
| Cap / 12 mo | **~$5M per issuer** | Unlimited | $10M |
| Non-accredited | **Unlimited number** | **Max 35** | Yes |
| Advertise? | ✅ **Yes**, via the portal | ❌ **No general solicitation — fatal for a fan campaign** | Yes |
| Disclosure | Form C + C-AR annual | Reg A-level to non-accredited (Rule 502(b)) | Varies |
| Financials | ≤$124k officer-certified · $124k–$1.235M **CPA-reviewed** · above **audited** (first-timers may use reviewed) | — | — |
| Resale | ⚠️ **12-month lock** | Restricted | Restricted |
| Blue sky | Preempted | Preempted | ❌ **Not preempted — register state by state** |
| Cost / time | **$15–50K, 2–4 months** | Low | Impractical |
| Per-investor limits | Both income and net worth <$124k → greater of $2,500 or 5% of the lesser. Both ≥$124k → 10% of the lesser, capped $124k. Accredited unlimited | — | — |

**Verdict: Reg CF is the right tool. 506(b) is useless here — 35 people and no advertising. Rule 504
dies on blue sky.** Must run through a registered funding portal (Wefunder, StartEngine, Republic,
Netcapital); self-hosting is not permitted.

## ✅ Can fans realistically trade on Securitize / tZERO / INX? Norman's skepticism is correct

**Technically yes. Culturally no.**

Account opening, KYC, suitability checks, brokerage-style UX, and **thin liquidity** — most tokenised
securities on ATSs barely trade. Securitize is largely institutional; tZERO volume has been modest.

⭐ **GameStop happened because of Robinhood's frictionless UX plus Reddit. An ATS has neither.**
Do not expect a regulated ATS to produce a social phenomenon. It will not.

## ⭐⭐ "Why not a crypto token?" — the actual answer

**You can. It depends entirely on what the token represents, and there are two completely different
paths.**

| | **(a) Token = economic stake** | **(b) Token = membership / access / voting, no economics** |
|---|---|---|
| Security? | **Yes** | **No** |
| Offering | Reg CF or Reg A+ required | None |
| Venue | Registered ATS only | ⭐ **Any chain, any wallet, OpenSea** |
| KYC | Required | Not required |
| UX | Brokerage | ⭐ **Full crypto UX** |

**(b) is what Norman actually wants for engagement, and it is unconstrained.**

### ⚠️ But *Stoner Cats* is the precedent to respect — it is nearly our exact fact pattern

The SEC charged **Stoner Cats** as an unregistered securities offering: **NFTs sold to fund an
animated series, with holders getting access to it.** Also **Impact Theory** — NFTs marketed as
"we're building the next Disney, these will be worth more."

**So the line is marketing, not technology:**
- ❌ Do **not** sell the token as a way to **fund** the team or the show.
- ❌ Do **not** tie its value to the project's performance, or promise to drive its price.
- ✅ Sell it as **access, identity and community** — a season ticket or fan-club card, not a stake.
- ✅ **Free or nominal mint** is far safer than a fundraise.

⭐ **The clean resolution: separate the token from the money.**
**Token = engagement (free/cheap, access-only, full crypto UX). Money = rewards commerce (§B).**
Combining them is what created Stoner Cats.

## ⭐ Fan ranking — how to rank and reward engagement

**Points from verifiable actions**, weighted by cost to the fan:
ticket scan at a home game **50** · road game **150** · watch-party check-in **30** · watched minutes
**1/10 min** · share with attributed click **5** · referral who signs up **100** · vote cast **10** ·
UGC submitted **25** · UGC used in the show **500** · merch purchase **1/$1** · consecutive-game
streak **multiplier**.

**Tiers, with scarcity concentrated at the top:**

| Tier | Size | Reward |
|---|---|---|
| Member | Millions | Numbered ID, votes, dashboard |
| Sixth Man | ~100k | Early ticket window, discount |
| Road Crew | ~10k | Road-game presale, members' channel |
| Bench | ~1,000 | Courtside lottery entry, shootaround access |
| Founders Circle | ~100 | Bench seat, team bus, film room, name on the floor |
| ⭐ **GM of the Game** | **1 per game** | Sits with Norman, **appears in the episode** |

**The five mechanics that make it work:**
1. ⭐ **A public leaderboard.** Visible status is the whole engine.
2. ⭐⭐ **Top rewards are earn-only, never purchasable.** If courtside can be bought, the status is
   worthless. **This is the single most important rule.** The money tiers (§B) buy *different*
   perks, never rank.
3. **Referral multipliers** — the viral loop.
4. **Permanent legacy badges** — "2027 Founding Season" kept forever, even after a seasonal reset.
5. ⭐ **The top fan appears on camera.** The ranking system becomes content, which costs nothing and
   is the most valuable prize available.

Plus **regional leaderboards** to manufacture city-vs-city rivalry.

## ⭐ The Kickstarter model — what fans are actually paying for

**Rewards-based crowdfunding: a pre-purchase of a product or experience. No equity, no profit share,
therefore not a security** — there is no expectation of financial return. Legally it is commerce.

⚠️ **And you do not need Kickstarter.** Kickstarter's terms are built for creative projects and a
basketball roster may not qualify. **Selling merch, experiences and naming rights is just a store.**
The campaign framing is marketing, not a legal requirement — self-host and avoid platform rules
entirely.

**The framing that matters: fund a named line item, not "the team."**
*"This campaign funds the charter flight to the conference tournament — $180,000."* With a counter.

**Illustrative tiers:**

| | |
|---|---|
| **$25** | Founding Member kit — numbered card, sticker, name on the digital wall |
| **$50** | First-drop tee + name in the docuseries credit crawl |
| **$100** | Jersey + name on the floorboard graphic |
| **$250** | Signed team photo + a live Q&A with Norman |
| **$500** | ⭐ **You fund the pregame meal for a named road game** — your name on that night's broadcast, with a certificate saying which game |
| **$1,000** | You fund a specific item — a film-room session, a recovery day, an hour on the shooting machine. Named plaque |
| **$2,500** | Two tickets + pregame shootaround + the team bus to a road game |
| **$5,000** | Name permanently on the court or a banner |
| **$10,000** | Associate Producer credit on an episode + bench seat for a home game |

⭐ **Every tier states exactly what the money bought.** That attribution is the emotional payload,
and it is the thing a profit share cannot deliver.
