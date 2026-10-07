# Current versions of record — 2026-10-07

Text extracted from the five PDFs Norman sent 2026-10-07. **These supersede all prior drafts and
generator output in `cinderella/legal/`** — including `2026-09-18-ankur-adviser-agreement-generator.py`,
`2026-09-18-stockholders-and-rspa-generator.py`, `2026-09-18-side-letter-v2-generator.py` and
`2026-09-18-subscription-agreement-v2-generator.py`, whose output had diverged from what was
actually sent.

These are the versions Ankur reviewed and responded to on 2026-10-07. Text only (pdftotext
-layout), kept for diffing and for drafting against. The PDFs themselves live in Norman's Drive.

| File | Notes |
|---|---|
| `Ankur_Jain_Strategic_Adviser_Agreement.txt` | Includes §0 Tabor OBA condition precedent — **not in the Sep 18 generator** |
| `Cinderella_Corp_-_RSPA_-_Ankur_Jain.txt` | 166,667 sh @ $0.001; `[Rule 701 / Regulation D]` placeholder open |
| `Cinderella_Corp_-_Stockholders_Agreement_-_Ankur_Jain.txt` | §2.5 Investor Rep, §2.6 indemnification |
| `Cinderella_Corp_-_Subscription_Agreement_Final.txt` | Loeb-settled; capital-return already reflected |
| `Cinderella_Corp_-_Side_Letter_Agreement_Revenue_Share_Final.txt` | Loeb-settled; §5(d) discloses no D&O; §6 capital return |

Change set responding to Ankur's 2026-10-07 redline: `../2026-10-07-ankur-october-redline-response.md`

---

## Added 2026-10-07 (second batch) — Sunjay and Greg

Norman sent four more `.docx` files the same day. Their extracted text is here and is the
**version of record** for each:

| File | Counterparty | Notable state as sent |
|---|---|---|
| `Cinderella_Corp_-_RSPA_-_Sunjay_Mathews.txt` | Sunjay | 833,333 sh, $0.001, exemption bracket live, Ankur comparison in Schedule A |
| `Cinderella_Corp_-_RSPA_-_Greg_Kristof.txt` | Greg | 166,667 sh, price `$[____]`, `[24]`-month vesting unsettled, Sunjay's acceleration disclosed |
| `Cinderella_Corp_-_Stockholders_Agreement_-_Sunjay_Mathews.txt` | Sunjay | **no §2.7, soft D&O in §2.6** |
| `Cinderella_Corp_-_Stockholders_Agreement_-_Greg_Kristof.txt` | Greg | **no §2.7, soft D&O in §2.6** |

The two Stockholders' Agreements as sent were **identical to each other apart from the signature
block and the date blank**, and both were **behind** Ankur's copy. That divergence is the find of
the pass — see `../2026-10-07-sunjay-greg-review.md`.

Revised builds: `../out-sunjay-greg-2026-10-07/` via `../2026-10-07-sunjay-greg-build.py`.

---

## Added 2026-10-07 (third batch) — the parent agreements

| File | Counterparty | State as sent |
|---|---|---|
| `Sunjay_Mathews_Partner_Agreement.txt` | Sunjay | Sound. `[15]%` seed hardcoded, "~16.9%", a drafter's note in §2.2, 83(b) wrong as to Milestone Shares |
| `Greg_Kristof_Strategic_Adviser_Agreement.txt` | Greg | ⚠️ **Two sections both numbered 2.3**; every economic term still bracketed; §7 non-circ had no carve-out, only a note saying one was needed |

Revised builds: `../out-partner-adviser-2026-10-07/` via `../2026-10-07-partner-adviser-build.py`.
Review: `../2026-10-07-partner-adviser-review.md`.

---

## Added 2026-10-07 (fourth batch) — the agreed Expense & Travel Policy

`Expense_and_Travel_Policy_October_2026.txt` — text of
`Making_Cinderella_Expense_Policy_October_2026.pdf`, sent after Ankur flagged that Side Letter
Exhibit A carried a **different, looser** policy. **This is the agreed version.** Rebuilt as a
tracked generator: `../2026-10-07-expense-policy-october-generator.py`.

⚠️ `../2026-09-18-expense-policy-generator.py` is **superseded for Exhibit A** and must not be
attached again. The deltas that mattered:

| Term | Sept 18 (do not use) | October (agreed) |
|---|---|---|
| Other-expense approval threshold | $5,000 | **$500** |
| Lodging cap | $300, with an exception for NYC / SF / LA | **$300 flat** |
| Approver | "the Investor Representative" | **Ankur Jain, by email** |
| SPVs | expressly carved out | **no carve-out** |
| Compensation | expressly carved out | **no carve-out** |
| 90-day vendor grouping rule | present | absent |
| Documentation / 30-day submission | absent | **present (§6)** |
