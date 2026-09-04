# Network system (Option 1)

**Chosen 2026-09-04.** One private Google Sheet is the source of truth for Norman's complete network (all layers, full PII). The public vault never holds phones, emails, addresses, Dex dumps, or NCD rows.

Dex is **cancelled**. Historical Dex (NCD + Sweep) was bootstrapped into the master. New people come from phone / Google Contacts exports — see Drive doc *Network Master — refresh process*.

## Source of truth (private)

**Master sheet:** [Norman Network Master](https://docs.google.com/spreadsheets/d/1pq0AdfTDblvfnLX6-fOK90iagNq-2LqkP5aUHi2QbXE/edit)  
File id: `1pq0AdfTDblvfnLX6-fOK90iagNq-2LqkP5aUHi2QbXE`  
Folder: [Jimmy network](https://drive.google.com/drive/folders/1sUlaC2KwkIax7avJ79txFX3yH05qkuot)

- One row per person. Layers are tags on the row.
- **12,174** rows (2026-09-04). Columns include `tier`, `tier_auto`, `tier_manual`, frequency fields.

### Tiers
| Tier | Meaning |
|------|--------|
| 1 | Call-anytime |
| 2 | Warm |
| 3 | Cold dump |

- `tier_auto` — rules + email/SMS frequency (do not hand-edit)
- `tier_manual` — **your override**: type `1`/`2`/`3`, or blank for auto. Refreshes never overwrite a filled `tier_manual`.
- `tier` — manual if set, else auto
- Freq: `email_90d`, `email_6mo`, `sms_90d`, `sms_6mo`, `freq_score`, `last_comm`

How-to Drive doc: *Frequency and manual tier* in Jimmy network.

### Layers
`inner_circle` · `sweep_working` · `ncd_dump` · `google_contacts` · `phone` · `family` · `friend` · `cinderella` · `investor` · `agent_wme_caa` · `college_hoops` · `media` · `legal`

### Feeds / refresh
Google Contacts CSV into Jimmy network → Jimmy merge (phone, email, name). Never delete (`archived=true`). Preserve `tier_manual`. 8am brief nags if Contacts import >14 days old.

---

## Vault mirror (public — no PII)

| Path | What |
|---|---|
| `network/README.md` | This file |
| `network/notable.md` | Curated long profiles |
| `people.md` | Inner-circle narrative; phones stripped |
| [Basics sheet](https://docs.google.com/spreadsheets/d/1CzrdTSm8yHWXLtOReBLt0Q2v064kJjhmsYFz_eXdaEI/edit) | PII-free mirror — do not commit 12k names here |

---

## For a stranger AI

1. Read this + `network/notable.md` + `people.md`.
2. Open private Master (Drive) for dial/email, tiers, frequency.
3. Respect `tier_manual` over `tier_auto`.
