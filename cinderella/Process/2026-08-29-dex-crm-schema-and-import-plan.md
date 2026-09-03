# Dex CRM — Tagging Schema & Cinderella Import Plan
_Prepared 2026-08-29. Ready to execute when the Dex connector reconnects (it dropped mid-session before writes could run)._

## Observed state of Dex (as of 2026-08-31, updated)
- **Groups (11):** Coworkers 💼 · Family ❤ · Friends ⚽️ · Networking 🤝 · Facebook Friends 🤗 · Instagram Contacts 📷 · LinkedIn Connections 💼 · Mobile import on 2026-08-29 👥 · **iMessage Contacts 💬** (new — Norman synced iMessage/calls via the Dex Mac app on 2026-08-31) · **From Calendar 📅** and **From Email 📧** (new — auto-ingested from connected Google Calendar/Gmail).
- **Tags:** none · **Custom fields:** none
- Record shape available per contact: name, job title, company, **multiple phones w/ labels**, **multiple emails w/ labels**, **LinkedIn handle**, photo, location + lat/long, groups, tags, custom fields, `related_contacts`, notes timeline, starred, keep-in-touch cadence.
- Searches for "Boardwalk" and "Netflix" returned **zero** — Dex holds Norman's own contacts only, not an industry map.

### iMessage sync — actual capability (verified 2026-08-31, corrects an earlier wrong claim)
`dex_list_group_contacts` on the iMessage Contacts group returns, per contact: `imessage_message_link`
(an `imessage://<number>` deep link), `imessage_message_snippet` (**the literal text of the single most
recent message** — e.g. `"You: I leave for the United States in 2 weeks..."` — including reaction text
like `"Reacted 😂 to ..."`), and `imessage_last_message_at`. **This is real message content, not just a
timestamp** — I first told Norman it was metadata-only and that was wrong; verify, don't assume, before
stating a tool's limits.
**The real boundary:** it's a **one-line preview of the latest message only**. `dex_get_contact` (the
full record) does not carry this field, and `recent_notes` came back empty even with `include_notes:
true` — there is no stored thread history and no message-search tool among the 49 Dex tools. For
anything beyond "what was the last thing we texted about," the `~/Library/Messages/chat.db` script
route (Norman runs it himself, per `CLAUDE.md`) is still the only path.
**Privacy note:** snippets can be personal/non-business (first sample pulled was a 2017 dating message).
Use for business network-mapping only; don't surface personal-life snippets back to Norman unprompted.

**Find already surfaced:** **Eli Thomas** (Producer/Writer/Exec, **Happy Madison**) — `thomas@happymadison.net` bounced twice in outreach, but Dex holds a **mobile: 978-290-9186** and LinkedIn `eliasclarkthomas`. This is a live, unused second path to the **Adam Sandler / New Hampshire** pairing.

---

## 1. Tag schema to create

**Lane (what they are):**
`cinderella-buyer` · `cinderella-capital` · `cinderella-talent` · `cinderella-talent-rep` · `cinderella-school` · `cinderella-production` · `cinderella-legal` · `cinderella-advisor` · `cinderella-connector`

**Status (where they stand):**
`status-hot` · `status-active` · `status-warm` · `status-cold` · `status-passed` · `status-do-not-contact`

**Utility (what they can do):**
`can-introduce` · `has-buyer-access` · `has-talent-access` · `has-capital-access` · `originated-by-me`

**Domain / world:**
`hollywood` · `nba` · `ncaa` · `boston` · `music` · `agency`

**Channel (who owns the relationship):**
`channel-direct` · `channel-shane-jay` · `channel-caa` · `channel-wme` · `channel-stein` · `channel-greg` · `channel-ankur` · `channel-sunjay`

## 2. Custom fields to create
| Field | Type | Purpose |
|---|---|---|
| Relationship Strength | enum: Close / Warm / Acquaintance / Cold | Honest read, not aspiration |
| Can Introduce To | text | The actual reason they matter |
| Deal Status | text | Current state in their lane |
| Source | text | Gmail / iMessage / LinkedIn / referral |
| Last Substantive Contact | date | Distinct from last message |
| Verify Before Use | checkbox | Flags anything inferred, not confirmed |

## 3. Groups to add
`Cinderella — Core Team` · `Cinderella — Buyers` · `Cinderella — Capital` · `Cinderella — Talent & Reps` · `Cinderella — Schools` · `Cinderella — Production`

## 4. Import
Source: `cinderella/contacts.md` (315 contacts) + `cinderella/Outputs/2026-08-12-cinderella-contacts.xlsx`.
Method: **match-then-merge** — search Dex by email/phone first; update existing records rather than duplicating (Dex has `dex_merge_contacts` for cleanup). Carry the Context field into a Dex note so the "how connected" history survives.

## 5. Relationship graph (`related_contacts`) — encode the known paths
- Gerry Corcoran → Walid Samaha (Hartbeat Ventures) · Joe Gallo (Merrimack) · Donnie Wahlberg · Sean McDonough
- Nikki Stier Justice → Mike Stein → **Michael Tollin** → Bill Simmons
- Josh (Straylight) → Bentley Weiner (HBO) · unscripted execs
- Sunjay → Ryan Reynolds' investment rep → Wrexham/Boardwalk orbit
- Shane Duffy → E-League roster (~200 names) → Jamie Foxx's camp
- Mike Stein → David Sherman (WME/Unanimous)
- Joe Mihalich → Connor Barwin · Steve Donahue (SJU)

## 6. Keep-in-touch cadences to set
Gone quiet with real value: **Peter Hess (CAA)** · **Carla Laur (CAA)** · **Kevin Gelbard (CAA)** · **Tim Curtis (WME)** · **Boss Everline (Hartbeat)** · **Andrew Schneider (Candle)** · **Scott Manson (SpringHill)** · **Ameeth Sankaran (Religion of Sports)**.

---

## 7. Contact-identification capability (for the "lane sweep" tasks)

**What is possible:** for each Dex contact, generate a **candidate identification** — who this person likely is — from name + job title + company + email domain + area code + LinkedIn handle + group + notes, cross-referenced against Gmail/iMessage history and Norman's own domain (15 yrs NBA scouting makes an NBA name in his phone a plausible prior, not a coincidence).

**What is NOT possible:** confirming that *Norman's* "Devin Harris" is *the* Devin Harris from a name alone. A name by itself is ambiguous and must never be asserted as identified.

**Confidence tiers to use in every sweep output:**
- **CONFIRMED** — title/company/email/LinkedIn in the record settles it, or an email/text thread proves it.
- **LIKELY** — distinctive name + corroborating signal (area code, group, adjacent contacts, Norman's domain).
- **POSSIBLE** — name matches a public figure, nothing else corroborates. **Norman confirms before any use.**
- **UNIDENTIFIABLE** — bare name + phone, common name, no other data.

**Output format:** Name · Why they may matter · Lane · Confidence · What would confirm it · Suggested action.

**Hard rule:** never present a POSSIBLE as real, and never let an inferred identity enter a deck, an outreach email, or the vault without Norman confirming. (Same standing rule as celebrity ties after the Luke Murray/Loyola error.)

**Lane sweeps to run when reconnected:**
1. **Production** — titles containing producer/director/EP/showrunner; known prodco names in company.
2. **Streamers/buyers** — company field: Netflix, Apple, HBO/WBD, Amazon/MGM, Disney/ESPN/FX/Hulu, Paramount/Skydance.
3. **Agencies** — CAA, WME, UTA, Range, Gersh, Verve in company; "agent"/"manager" in title.
4. **Celebrities** — name-match against public figures, then corroborate. Highest fabrication risk — hold to CONFIRMED/LIKELY only.
5. **Capital** — PE/VC/family-office/banking titles.
6. **NCAA/schools** — `.edu` emails; AD, coach, GM, compliance titles.
7. **NBA** — Norman's richest and most reliable lane, given his career.
