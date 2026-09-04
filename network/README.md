# Network system (Option 1)

**Chosen 2026-09-04.** One private Google Sheet is the source of truth for Norman's complete network (all layers, full PII). The public vault never holds phones, emails, addresses, Dex dumps, or NCD rows.

Dex is **cancelled**. Historical Dex (NCD + Sweep) was bootstrapped into the master. New people come from phone / Google Contacts exports — see Drive doc *Network Master — refresh process*.

## Source of truth (private)

**Master sheet:** [Norman Network Master](https://docs.google.com/spreadsheets/d/1pq0AdfTDbIvfnLX6-fOK9oiaNg-2LqkP5aUHi2QbXE/edit)  
File id: `1pq0AdfTDbIvfnLX6-fOK9oiaNg-2LqkP5aUHi2QbXE`  
Folder: [Jimmy network](https://drive.google.com/drive/folders/1sUlaC2KwkIax7avJ79txFX3yH05qkuot)

- One tab / one row per person. Layers are **labels on the row**, not separate sheets.
- Bootstrap 2026-09-04: **12,166** rows (NCD 12,106 + Sweep extras + inner circle).

### Layers (tags, semicolon-separated)
`inner_circle` · `sweep_working` · `ncd_dump` · `google_contacts` · `phone` · `cinderella` · `family` · `investor`

### Feeds (historical / intake)
- Dex Contact Sweep (frozen export) — `1Ni-x4eBgFYW4spDV2LFOnR9WcYHlv54UbVPAY_X_-eY`
- NCD – Raw Contacts Data (frozen Dex dump) — `1w5rhIP2TYBrYutO8V6WrUDS1oZ-_3z1K94DhlW-ILEU`
- Inner circle narrative: `people.md` / `network/notable.md` (strip phones from anything public)
- **Going forward:** Google Contacts CSV (or iPhone vCard) dropped in Drive `Jimmy network / imports / google-contacts-YYYY-MM-DD.csv`

### Refresh (Dex is dead)
1. Phone contacts stay synced to Google Contacts.
2. Export Google Contacts → Google CSV → `imports/`.
3. Jimmy matches phone, then email, then normalized name: INSERT new (`layers` include `google_contacts`/`phone`); UPDATE changed phones/emails; never delete (`archived=true` instead).
4. 8am brief nags if newest import is older than 14 days.

### TrackApp cleanup (applied 2026-09-04)
Stripped whole-word `Track` from names (3,018) and `.trackapp.io` from emails (3,021). Did not touch substring names (Trackson / Backtrack). Dirty originals kept in `name_aliases`. Leftovers flagged, not deleted: General Manager PA339, Mr. undefined Gonsalves, 978 My Printer, ~1,688 email-as-name rows. Google Contacts / iPhone still need a separate export → clean → re-import (no live Contacts connector).

---

## Vault mirror (public — no PII)

| Path | What |
|---|---|
| `network/README.md` | This file — system + sheet link |
| Drive *Norman Network Master — basics (no PII)* | Periodic PII-free mirror (name, org, title, layers, provenance, last_touch). Id `1CzrdTSm8yHWXLtOReBLt0Q2v064kJjhmsYFz_eXdaEI`. Do **not** commit 12k names into this public repo. |
| `network/notable.md` or `people.md` | Long-form profiles for **select** people only. Not 12k files. |

**Do not** put phones/emails/addresses/NCD dumps in this public repo. Inner-circle phones currently in `people.md` should move off public.

---

## For a stranger AI

1. Read this file + notable/people long-form.
2. Open the private master sheet (needs Drive access) for dial/email/full dump.
3. Treat `layers` as filters, not separate worlds — one graph, labeled.
