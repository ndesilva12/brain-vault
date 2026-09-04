# Network system (Option 1)

**Chosen 2026-09-04.** One private Google Sheet is the source of truth for Norman's complete network (all layers, full PII). The public vault never holds phones, emails, addresses, Dex dumps, or NCD rows.

Dex is **cancelled**. Historical Dex (NCD + Sweep) was bootstrapped into the master. New people come from phone / Google Contacts exports — see Drive doc *Network Master — refresh process*.

## Source of truth (private)

**Master sheet:** [Norman Network Master](https://docs.google.com/spreadsheets/d/1pq0AdfTDbIvfnLX6-fOK9oiaNg-2LqkP5aUHi2QbXE/edit)  
File id: `1pq0AdfTDbIvfnLX6-fOK9oiaNg-2LqkP5aUHi2QbXE`  
Folder: [Jimmy network](https://drive.google.com/drive/folders/1sUlaC2KwkIax7avJ79txFX3yH05qkuot)

- One tab / one row per person. Layers are **labels on the row**, not separate sheets.
- Bootstrap + org-merge 2026-09-04: **12,174** rows.

### Tiers (effective column `tier`)
| Tier | Meaning |
|------|--------|
| 1 | Call-anytime |
| 2 | Warm |
| 3 | Cold dump |

- `tier_auto` — rules + email/SMS frequency (do not hand-edit)
- `tier_manual` — **your override**: type `1`/`2`/`3` on the sheet, or leave blank to follow auto. Refreshes never overwrite a filled `tier_manual`.
- `tier` — manual if set, else auto
- Frequency fields: `email_90d`, `email_6mo`, `sms_90d`, `sms_6mo`, `freq_score`, `last_comm` (iMessage 6mo full; Gmail sample is partial)

### Layers (tags)
`inner_circle` · `sweep_working` · `ncd_dump` · `google_contacts` · `phone` · `family` · `friend` · `cinderella` · `investor` · `agent_wme_caa` · `college_hoops` · `media` · `legal`

### Feeds
- Dex Contact Sweep (frozen) — `1Ni-x4eBgFYW4spDV2LFOnR9WcYHlv54UbVPAY_X_-eY`
- NCD (frozen) — `1w5rhIP2TYBrYutO8V6WrUDS1oZ-_3z1K94DhlW-ILEU`
- Google Contacts CSV → Drive `Jimmy network` (merged 2026-09-04)
- Inner circle long-form: `people.md` / `network/notable.md` (no phones in public repo)

### Refresh
1. Phone → Google Contacts → export Google CSV → `imports/`.
2. Jimmy match phone, then email, then name; never delete (`archived=true`).
3. Recompute `tier_auto` + frequency; **preserve `tier_manual`**.
4. 8am brief nags if newest Contacts import is older than 14 days.

### TrackApp cleanup (applied 2026-09-04)
Whole-word `Track` / `.trackapp.io` stripped on Master and Google Contacts. Dirty Track-prefix Google cards moved to Trash after clean re-import.

---

## Vault mirror (public — no PII)

| Path | What |
|---|---|
| `network/README.md` | This file |
| `network/notable.md` | Curated long profiles (~22+) for AIs without Drive |
| `people.md` | Inner-circle narrative; phones stripped |
| Drive basics sheet | PII-free mirror id `1CzrdTSm8yHWXLtOReBLt0Q2v064kJjhmsYFz_eXdaEI` — do not commit 12k names here |

**Do not** put phones/emails/NCD dumps in this public repo.

---

## For a stranger AI

1. Read this + `network/notable.md` + `people.md`.
2. Open the private Master (Drive) for dial/email, tiers, frequency, full graph.
3. Respect `tier_manual` over `tier_auto`. Treat layers as filters, not separate worlds.
