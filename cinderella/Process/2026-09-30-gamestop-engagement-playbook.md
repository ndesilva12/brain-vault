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
