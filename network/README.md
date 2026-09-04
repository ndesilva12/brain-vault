# Network system (Option 1)

**Chosen 2026-09-04.** One private Google Sheet is the source of truth for Norman's complete network (all layers, full PII). The public vault never holds phones, emails, addresses, Dex dumps, or NCD rows.

## Source of truth (private)

**Master sheet:** *(create / link TBD — working title "Norman Network Master")*

- Lives in Drive (private). Prefer folder [Jimmy network](https://drive.google.com/drive/folders/1sUlaC2KwkIax7avJ79txFX3yH05qkuot) or Legal-adjacent private ops.
- **One tab / one row per person.** Layers are **labels on the row**, not separate sheets or databases.
- Upstream feeds (do not treat as SoT once master exists):
  - Dex Contact Sweep — `1Ni-x4eBgFYW4spDV2LFOnR9WcYHlv54UbVPAY_X_-eY` (~404 curated)
  - NCD – Raw Contacts Data — `1w5rhIP2TYBrYutO8V6WrUDS1oZ-_3z1K94DhlW-ILEU` (~12,106 Dex dump)
  - Inner circle currently in `people.md` (phones must leave the public vault)

### Suggested master columns

| Column | Purpose |
|---|---|
| `contact_id` | Stable id (uuid or slug); never reuse |
| `full_name` | Display name |
| `name_aliases` | Other spellings / nicknames |
| `layers` | Semicolon tags: `inner_circle` · `sweep_working` · `ncd_dump` · `cinderella` · `family` · `investor` · etc. |
| `org` / `title` | Company, role |
| `phones` / `emails` / `addresses` | Full PII (private sheet only) |
| `socials` | LinkedIn, IG, X, etc. |
| `provenance` | How the row got here (Dex phone, IG-follow-only, NCD mobile-import, intro path) |
| `relationship` | Strength / how you actually know them |
| `last_touch` | Date + channel if known |
| `cinderella_notes` | Deal relevance / open asks |
| `profile_md` | Optional path or flag if a long vault profile exists |
| `sources` | Sweep / NCD / people.md / manual |
| `updated_at` | Last sync or manual edit |

Name rule: assume the most prominent public person unless the row clearly isn't (e.g. Thomas Brady = NFL Tom Brady).

### Sync workflow

1. **Bootstrap:** merge NCD (breadth) + Sweep (curation/provenance) + `people.md` into master; Sweep/people fields win on conflict for relationship quality; keep all NCD-only rows with `layers` including `ncd_dump`.
2. **Periodic refresh:** after Dex export / Sweep edits / new intros — upsert by name+phone/email; never delete without a tombstone/`archived` flag.
3. **Jimmy lookup:** query the master sheet (or a private index built from it). Sweep-alone / NCD-alone indexes become caches of the master.

---

## Vault mirror (public — no PII)

| Path | What |
|---|---|
| `network/README.md` | This file — system + sheet link once created |
| `network/notable.md` | Long-form profiles for **select** people only (same spirit as today's `people.md`). Not 12k files. |
| `network/basics.md` or `network/basics.csv` | Periodic PII-free mirror of master: name, org, title, layers, provenance class, last_touch, cinderella tag, link to `notable` if any. Refresh on sync. |

**Do not:** one `.md` per contact. **Do not:** put phones/emails/addresses/NCD dumps in this public repo.

Migrate inner-circle narrative from root `people.md` → `network/notable.md` (or keep `people.md` as the notable file and point here). Strip phones from anything public.

---

## For a stranger AI

1. Read this file + `network/basics.*` + `network/notable.md`.
2. Open the private master sheet (needs Drive access) for dial/email/full dump.
3. Treat `layers` as filters, not separate worlds — one graph, labeled.
