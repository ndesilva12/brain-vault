# Fan membership + ranking — platform stack and verification

_2026-09-30. What to actually run the Founders Club and leaderboard on, and how each action gets
verified. Companion to `2026-09-30-gamestop-engagement-playbook.md`._

---

## The honest answer up front

⚠️ **No single platform does this.** Anyone selling one is selling. The points logic and the
leaderboard are the *differentiated* part of the product, and no off-the-shelf loyalty tool will
match the design — especially the rule that **top rewards are earn-only**.

⭐ **Recommendation: own the system of record, rent everything else.** Norman already runs a Vercel
app in Claude Code, so the build cost here is low.

## The stack

| Layer | Use | Why |
|---|---|---|
| ⭐ **System of record** | **Next.js on Vercel + Postgres (Supabase/Neon)** | The points engine, tiers and leaderboard are the product. Cheap, already in Norman's toolchain |
| **Identity** | Clerk, or Supabase Auth | Phone or email. Lowest friction wins — every extra field costs members |
| ⭐ **Commerce** | **Shopify** | Merch, experiences, naming rights, the crowdfunding tiers. Webhooks → points. **Verification is perfect because we own the store** |
| ⭐ **Community** | **Discord** | Where this audience already lives. **Tiers = roles**, synced from the app. Free |
| **Attendance** | QR + geofenced check-in in the app · **POAP** for the collectible layer | See below |
| **Attribution** | **Dub.co** or Branch.io | Referral codes and share tracking |
| **Voting** | In-app for real votes · Discord polls for low-stakes | Keep the audit trail on votes that matter |
| **Token gating** *(later)* | **Collab.Land** or **Guild.xyz** | Only if a non-economic NFT membership ships |

### Buy-instead-of-build options, and their costs

- **Zealy** or **Galxe** — genuinely built for quests, points and leaderboards, cheap, fast.
  ⚠️ **Looks like a crypto airdrop farm**, which is probably the wrong brand for a college program.
- **Talon.One** or **Antavo** — serious loyalty engines. Enterprise sales cycle and pricing; overkill
  at launch.
- **Smile.io / LoyaltyLion / Yotpo** on Shopify — 20 minutes to stand up, handles purchase points and
  tiers well, **cannot do attendance or social actions at all.**

## ⭐ Verification, honestly graded

| Action | Method | Reliability |
|---|---|---|
| **Merch purchase** | Shopify webhook | ✅ **Perfect** — we own the store |
| **Referral signup** | Attributed link (Dub.co) | ✅ Strong |
| **Vote cast** | In-app | ✅ Perfect |
| **UGC submitted** | In-app upload | ✅ Perfect |
| **UGC used in the show** | Our editorial decision | ✅ Perfect |
| **Game attendance** | QR at a fan-zone table **+ geofence + time window** | ⚠️ **Good, spoofable.** Excellent only if the school shares ticket-scan data |
| **Social share** | Attributed clicks, **not** posts | ⚠️ **Weak** — measure clicks delivered, never "did you post" |
| ❌ **Watch time on Netflix / Paramount+** | — | ❌ **Impossible. Streamers share no viewership data.** Drop it |

### Attendance — the one that needs a decision

The school controls ticketing (**Paciolan** dominates college athletics; also Ticketmaster/Archtics,
Hometown, AudienceView). **A data feed would be ideal and they will probably not give us one.**

**So run our own check-in:** a QR code at a branded fan-zone table plus a geofenced in-app check-in
valid only during the game window. Spoofable, but good enough for points — and **pair it with a
second signal before awarding a scarce reward.**

⭐ **POAP** (proof-of-attendance protocol) is purpose-built for exactly this: scan at the gate, mint
a badge. Cheap, collectible, no KYC, and it gives the crypto texture Norman wants **without touching
securities law**, because it is a commemorative with no economics.

### ⚠️ Watch time — flag this now

If the series lands on Netflix or Paramount+, **we get zero viewership data.** Streamers do not share
it, ever. Watch-time points only work on surfaces we own — our own player, YouTube, Twitch. **Design
the ranking system so it does not depend on the streamer.**

## ⚠️ Two things that will bite

1. **Every points system gets gamed**, and our top rewards are genuinely valuable (bench seat, team
   bus). Needs rate limits, device fingerprinting, duplicate-account detection, and ⭐ **manual review
   of the top of the leaderboard before any scarce reward is awarded.**
2. **Collecting fan data at scale triggers privacy obligations** — CCPA, and GDPR if any EU members.
   Minor but real: a privacy policy, deletion requests, and a lawful basis for the data.

## ⭐ Phasing — build bottom-up

| Phase | Build | Cost |
|---|---|---|
| **1 — prove demand** | **Shopify + Discord.** Roles by hand, points in a sheet, votes as Discord polls | **~$0** |
| **2 — the real thing** | Custom app as system of record · Shopify webhooks · QR + geofence check-in · referral links · public leaderboard | Low — days of build |
| **3 — collectible layer** | POAP per game · optional non-economic NFT membership · token-gated Discord roles | Low |

**Do not buy an enterprise loyalty platform before Phase 1 proves anyone wants this.**
