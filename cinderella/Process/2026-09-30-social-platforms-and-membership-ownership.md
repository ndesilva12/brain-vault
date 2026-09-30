# Social platforms + where the fan membership lives

_2026-09-30. Two questions Norman asked after the Boardwalk fan-engagement thread: which social
platforms the team community should run on, and where the membership itself lives. Companion to
`2026-09-30-fan-platform-stack.md` (verification and build) and
`2026-09-30-gamestop-engagement-playbook.md` (the engagement design)._

---

## Part 1 — Social platforms

### ⭐ The answer that isn't an app: the players are the channel

Twelve players posting to their own accounts out-reaches any team account by an order of magnitude,
costs nothing, and **can be required** — the NIL agreements pay for genuine content services, so
"post twice a week, appear in N pieces" is simultaneously the distribution plan and part of the
**FMV defense** (see `2026-09-13-nil-sponsor-architecture-and-pcsa.md`). Any team-handle strategy
that doesn't start here leaves the largest asset on the table.

### Then three, plus one

| | Platform | Job | Why |
|---|---|---|---|
| **1** | ⭐ **Instagram** | Home base | Reels now get TikTok-class reach; Stories carry the daily intimacy a season needs; **Broadcast Channels** push to opted-in fans with no algorithm in between. Celebrities and players already live here, so cross-posting from a Curry or a Hart is frictionless |
| **2** | **TikTok** | Cold-start reach | Best distribution to people who don't follow us. ⚠️ Audience does not transfer off-platform — build nothing load-bearing on it |
| **3** | **YouTube** | Archive + buyer-facing proof | Long-form is where docuseries audiences are proven, watch-time is real data a streamer respects, and the library compounds for years. Shorts as the funnel |
| **+** | **Discord** | Members-only layer | Founders Club, leaderboard, watch parties, the Adoption Draft. Not discoverable — fed from the three above |

**X** — near-zero effort, kept for one reason: **college basketball media lives there** (Rothstein,
Brandon Walker, bracketologists, beat writers). Tiny audience, but it is the audience that turns a
Cinderella run into a national story. Post, don't build.

**Twitch** — secondary but real. Co-streamed watch-alongs with the hoops creators already on the
grassroots list (Cam Wilder, Jesser, Brandon Walker) is the cheapest live-audience play available.

### ⚠️ Two flags

1. **The two fanbases are on different platforms.** The alumni and donors who buy season tickets and
   write checks are on **Facebook**. The fans who make a program culturally hot are on **TikTok**. A
   strategy serving only one underperforms — and the Facebook half is the half with money.
   *(Facebook is read-only for Norman personally per `CLAUDE.md`; a team/school account is a separate
   question.)*
2. **Don't run this on the school's athletics handles.** An SID with compliance constraints cannot
   carry the celebrity/docuseries voice, and we need an owned asset that sits with the structure.
   **New per-team handle**, cross-promoted hard with the school's.

### Sequencing

The handle exists and is posting **before** the season. The show's arc starts at announcement, not at
tip-off — everything posted in the quiet months is Episode 1 footage.

---

## Part 2 — Where the membership lives

### ⭐ The record lives on our own domain. Everything else is rented.

**One join URL on a Cinderella-owned domain → Postgres.** Next.js on Vercel, already in Norman's
toolchain.

Not Discord, not Instagram, not an off-the-shelf loyalty app. The reason: **the member list is the
asset we are actually selling to Boardwalk and to a streamer.** A follower count is a rented number
we cannot email, verify or rank. A member record is ours — and *"41,000 members before tip-off"* is
the single number that changes the buyer conversation.

| | Lives where | Owned or rented |
|---|---|---|
| **Who is a member, tier, points** | Our app + Postgres | ⭐ **Own** |
| **Money** | Shopify | Rented — fine; webhooks give perfect purchase verification |
| **Daily conversation** | Discord (tiers = roles, synced from our app) | Rented — fine, but never the record |
| **Discovery** | IG / TikTok / YouTube | Rented, disposable |

If Discord dies tomorrow we lose a chat room. If Discord *is* the membership, we lose the company's
most valuable asset.

### ⭐⭐ Ownership structure: members belong to the PARENT, not the SPV

Hold the membership at **Cinderella Corp** and license it down to each SPV — exactly the way the
**Format License** works.

1. **Season 2 at a new school starts warm.** A franchise-held list carries across schools; an
   SPV-held list dies with the SPV.
2. **It is the thing no counterparty can take.** Same logic that keeps the format out of a
   producer's hands.

⚠️ **OPEN ITEM — this is not yet papered.**
`legal/2026-08-29-format-license-cinderella-to-spv.md` licenses the format but says nothing about the
audience. The membership data and the fan-facing channels should be named as **licensed assets
alongside the format**, revocable on the same terms. Flagged in `legal/CONTRACT-REGISTER.md`.

### ⚠️ Not the same list as the school's

The school owns its ticket buyers, its donor file and its alumni database, and **it will not hand any
of it over.** Our membership is a parallel list built from zero. That is precisely why the join flow
must sit on our property — **it is the only list we will ever own.**

### What to stand up

| Phase | Build | Cost |
|---|---|---|
| **1 — prove demand** | Shopify + Discord. Tiers by hand, points in a sheet | **~$0** |
| **2 — the real thing** | App as system of record · Shopify webhooks · QR + geofenced check-in · referral links · public leaderboard | Low — days of build |

**One domain, one join flow, every platform pointing at it.** Verification detail and the gameable
parts: `2026-09-30-fan-platform-stack.md`.
