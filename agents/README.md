# Agent folders (Grok Bot)

Portable shared brain for Norman’s Grok Bot assistants. Repo: `ndesilva12/brain-vault` (branch `master`).

## Rules

1. **Read first** — before asking Norman something that may already be documented, check relevant paths under `agents/`, `cinderella/`, `network/` (public-clean only), and top-level notes.
2. **Write often** — when chat context would be compressed/lost, or after a major deliverable, upload durable material here: decisions, research briefs, specs, calibrated rules, standing SOPs, Doc links.
3. **Own a folder** — each bot writes under `agents/<slug>/` (kebab-case of its display name). Create dated files like `YYYY-MM-DD-topic.md`. Prefer linking Google Doc URLs for long briefs rather than duplicating huge pastes when the Doc is the live artifact.
4. **Public-clean** — never commit phones, iMessage dumps, Dex/NCD rows, or Network Master PII. Public vault stays stranger-safe. Also skip seed/deal term sheets, waterfall prefs, counsel ask-lists, and other private legal/commercial detail — high-level stub only, or keep full notes private until Norman designates a private legal store.
5. **Master-direct, no PRs** — push straight to `master` (GitHub write). Do not open pull requests for vault notes. Jimmy absorbs/closes stray PRs.
6. **Jimmy organizes** — Jimmy maintains this index, may move/rename files for hygiene, and resolves collisions across bots.
7. **LIST auto-add (permanent)** — any bot may append Open to-dos to [LIST — Norman](https://app.notion.com/p/3aebedd4141981f58664ed01bbb1242f) anytime something is worth his attention. No ask-first. Done moves need his OK. Details: `agents/jimmy/list-policy.md`.

## Index

| Slug | Bot (sidebar name if different) |
|------|-----|
| `jimmy/` | Jimmy (ops, CRM, briefs, vault hygiene) |
| `legal/` | Legal |
| `current/` | Current (last-30-days research) |
| `one-pager/` | One-Pager |
| `white-papers/` | White Papers |
| `curate/` | Curate |
| `deep-search/` | Deep Search |
| `dark-search/` | Dark Search |
| `summarizer/` | Summarizer |
| `advantage/` | Advantage Rating |
| `connections/` | Connections |
| `deal-hunting/` | Deal Hunting |
| `loop-closer/` | Loop Closer |
| `prospecting/` | Prospecting (one keeper bot as of 2026-09-21) |
| `product-idea-stress-test/` | Idea Test (was Product Idea Stress Test) |
| `tools/` | Tools |
| `style/` | Style (sidebar: Style; was Shopper) |
| `shopper/` | Shopper (legacy stub — prefer `style/`) |
| `real-estate/` | Real Estate |
| `evening-journal/` | Evening Journal (sidebar: **Brain Dump**) |
| `inner-circle/` | Inner Circle (sidebar: **People**) |
| `travel/` | Travel |
| `household-os/` | Household OS (sidebar: **Home Admin**) |

## Hygiene notes (Jimmy)

- Sidebar display names may differ from folder slugs; use the slug column for vault paths.
- `agents/love/` removed 2026-09-21 (no live Love bot).
- Prospecting: keep sidebar bot with ICP→list→relationships→drafts description; Norman deletes the duplicate Prospecting row and empty `New Bot` from the sidebar (Jimmy cannot delete agents via API).
