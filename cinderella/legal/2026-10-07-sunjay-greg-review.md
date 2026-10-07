# Sunjay & Greg — RSPA and Stockholders' Agreement review

**Date:** 2026-10-07
**Reviewed:** the four `.docx` files Norman sent 2026-10-07 — Sunjay Mathews RSPA, Greg Kristof
RSPA, Sunjay Mathews Stockholders' Agreement, Greg Kristof Stockholders' Agreement. These are now
the **versions of record** for those four documents, alongside
`current-versions-2026-10-07/` for Ankur's five.
**Build:** `2026-10-07-sunjay-greg-build.py` → `out-sunjay-greg-2026-10-07/` (24 patches, each
asserted; all verification checks pass)

---

## First, the good news on 83(b)

**The 30-day window has not started and nothing has been lost.** Both RSPAs still have a blank
Effective Date (`______, 2026` / `[____], 2026`) and unsigned signature blocks. Section 83(b)'s
clock runs from the date of transfer, which is the Effective Date. Nothing was transferred, so
nothing is late. The earlier worry that Sunjay's window might close around Oct 18 (papers out
Sep 18) does not apply.

⚠️ **But it becomes the single hardest deadline in the deal the moment either document is
signed.** 30 days, statutory, non-extendable — the IRS cannot grant relief for reasonable cause.
Miss it and Sunjay pays ordinary income tax on each monthly vesting tranche at that month's
fair market value, for 24 months, on stock he cannot sell. File it and he pays tax on $833 today
and nothing thereafter. **Do not countersign either RSPA until both men have the completed
Schedule B election in hand and know the date it is due.**

Both §5.1s now say so explicitly, including the consequence of missing it.

---

## The two problems worth being annoyed about

### 1. Both documents disclosed other people's terms to the counterparty

Sunjay's and Greg's Schedule As both read:

> "Unlike the Company's arrangement with **Ankur Jain**, these Shares carry NO anti-dilution
> protection and NO top-up."

And Greg's Acceleration line read:

> "[None provided. … Compare **Sunjay Mathews**, who has both six-month severance acceleration
> and full single-trigger acceleration on a Change of Control.]"

These were internal drafting notes that survived into a counterparty draft. They do two things
at once: disclose another holder's preferential terms, and hand the reader the argument for
matching them. Greg's copy told Greg, in writing, that Sunjay got acceleration and he did not.

**Fixed.** The substance is kept — neither has anti-dilution, neither gets a top-up, Greg gets no
acceleration — and the comparison is deleted. Greg's copy no longer contains the string "Sunjay
Mathews" anywhere; neither copy contains "Ankur Jain."

### 2. Both documents told the counterparty your own price was unsettled

Header note, both RSPAs:

> "Purchase price per Share to be set at fair market value as determined in good faith by the
> Board — **confirm with counsel before execution.**"

Schedule A, both:

> "Purchase price per Share: $0.001  **[FMV as determined by the Board]**"

Greg's §1.1 was worse — the price was literally `$[____]`.

That bracket is ambiguous on its face: is the price $0.001, or is it whatever FMV turns out to
be? For restricted stock that is the entire tax basis. **Fixed:** $0.001 stated once, as the
Board's good-faith FMV determination as of the Effective Date, in all three places.

> ⚠️ **This creates a dependency.** The documents now assert a Board determination that does not
> yet exist. **The board resolution fixing $0.001 as the FMV of a share of Class A Common Stock,
> dated on or before the Effective Date, has to be signed before these are executed.** It is a
> one-page consent. Still outstanding.

---

## The securities exemption — and why these two are *not* Reg D

Both RSPAs had the live bracket `[Rule 701 / Regulation D]` in §1.3.

You chose **Regulation D** for Ankur on 2026-10-07. **That choice should not propagate here, and
I have not propagated it.** The reason Reg D was right for Ankur is specific to Ankur:

- **Rule 701(c)** makes the exemption available for securities issued as compensation for
  services — but **excludes services rendered in connection with the offer or sale of securities
  in a capital-raising transaction.**
- Ankur's Adviser Agreement §1.1 defines his services as capital formation and investor
  meetings. He is leading the seed round. Rule 701 is unavailable to him.

Neither of these two is in that position:

| | Services | Rule 701? |
|---|---|---|
| **Ankur** | Capital formation, investor meetings (Adviser Agmt §1.1) | ✗ 701(c) carve-out |
| **Sunjay** | Founding Partner — operations, business development, sponsor procurement. Track A milestone is a *sponsorship*, not a security | ✓ |
| **Greg** | "Strategic guidance and network access" (Adviser Agmt §1.1); §1.2 expressly: not an agent, no authority to bind, "will not execute, negotiate to close, or sign" | ✓ |

**Both are now Rule 701 primary, Section 4(a)(2) fallback.** Rule 701 is the better exemption for
these two for three concrete reasons:

1. **No accredited-investor representation needed.** Reg D 506(b) requires each purchaser to be
   accredited, or forces full disclosure to up to 35 non-accredited purchasers. **Greg's
   accreditation status is unconfirmed** — this was an open item from the Ankur pass. Rule 701
   makes the question irrelevant. (⚠️ If you ever do go Reg D on Greg's grant, you must confirm
   he is accredited first, and §8.1 would need an accreditation rep it currently lacks.)
2. **No Form D, no state blue-sky notices** for a par-value compensation grant.
3. **It is the right characterization.** These are compensation, not investments. Rule 701 exists
   for exactly this.

Mechanics handled: Rule 701 requires the grant be made under a **written compensation contract**,
so §1.3 now names that contract on its face. The quantitative limit is comfortable — aggregate
sales price is $833 (Sunjay) + $167 (Greg) against a $1,000,000 floor. And **Rule 701 offerings do
not integrate with the Reg D offering to Ankur**, so running two exemptions in parallel is clean.

**For Loeb, in writing:** confirm the Rule 701(c) capital-raising carve-out reading for Ankur, and
confirm 701 availability for Sunjay and Greg. Same email.

---

## The Stockholders' Agreement problem — this was the real find

**The Stockholders' Agreement is ONE agreement.** Everybody signs the same document or a joinder
to it. There is not a Sunjay version and a Greg version and an Ankur version — there is one text,
and three signature pages.

Ankur's copy, rebuilt 2026-10-07, now carries:

- **§2.6** — D&O changed from "commercially reasonable efforts to include" to a firm obligation to
  **obtain** the policy on or before the Seed closing, plus the representation that none exists today.
- **§2.7** — brand new. No personal liability of the Investor Representative.

**Sunjay's and Greg's copies had neither.** Had all three gone out as sent, three materially
different texts of the same agreement would have been executed. Two consequences:

1. **§2.7 would be unenforceable against Sunjay and Greg.** The section works by consent — "Each
   Investor, by executing this Agreement or a joinder to it, acknowledges and agrees to this
   Section 2.7." A holder who signs a copy that does not contain §2.7 has not agreed to it. The
   protection Ankur asked for would be full of holes on day one.
2. ⭐ **Sunjay is the Class A majority.** 833,333 of 1,166,667 Class A shares pre-Seed — **71%.**
   §9.2 requires the consent of a majority of outstanding Class A to amend this Agreement. So
   Sunjay is the one person whose signature on the *current* text matters most, and his copy was
   the stale one.

**Fixed.** Both copies conformed. §2.6 and §2.7 are now **character-identical across all three
documents** — verified programmatically, down to the apostrophe glyph (Ankur's build had a
straight `'` where the others had a curly `’`; his build was corrected rather than theirs, since
the surrounding documents use curly typography).

**Neither change costs Sunjay or Greg anything.** Both run only to the Investor Representative:
one makes the Company buy insurance, the other limits Ankur's exposure to *Investors* — a class
neither of them is in. There is nothing here for them to push back on, which is why conforming
was the right call rather than a renegotiation.

---

## Greg's open brackets — settled

Greg's draft told him, in the header, that his own vesting term and acceleration "remain
bracketed … and must be settled before execution." Settled as follows, all from the bracketed
defaults in his Adviser Agreement §2.3:

| Item | Was | Now |
|---|---|---|
| Vesting term | `[24]` months | **24 months**, 24 installments of 6,944 (final 6,955) |
| Cliff | `[no cliff]` | **No cliff** |
| Vesting commencement | `______ [Effective Date — confirm]` | **Effective Date** |
| Acceleration | `[None provided … optional, unresolved]` | **None**, stated affirmatively |
| Price | `$[____]` | **$0.001** |

⚠️ **Two things follow from this.**

**(a) Greg's Strategic Adviser Agreement must be conformed.** It still carries `[4]%`, `[24]`
months, `[Optional: acceleration … confirm]`, and the same unresolved `[Rule 701 / Reg D]` note at
§2.5. The RSPA now states terms his own adviser agreement leaves bracketed. **Not yet done — say
the word and it is the same kind of build.** It also needs §2.2's hardcoded "`[4]%` becomes
approximately `[3.4]%` following a `[15]%` Seed Round" fixed: the RSPA says 3.375%, the adviser
agreement says 3.4%. Those should agree.

**(b) "No acceleration" is your call, not mine.** I set it to none because that is the status quo
and the conservative default — it gives nothing away and is easy to improve later. But Greg has
no severance protection and no change-of-control protection, where Sunjay has both. If a sale
happens in month 10, Greg keeps 10/24 of his 4% and the Company repurchases the rest at $0.001.
That is a defensible position for a non-exclusive adviser with no minimum hours. Tell me if you
want single-trigger acceleration on a Change of Control instead and it is a one-line rebuild.

---

## The seed-size numbers — kept, qualified, not deleted

Both Schedule As hardcoded post-Seed percentages: Sunjay **16.875%**, Greg **3.375%**, each
"immediately following the Seed Round." Those are correct **only** for a round sold at 15% of
post-money.

Given what happened with Ankur's §2.5, I did **not** remove them. Both numbers are kept exactly as
you sent them, with a qualifier added:

> "Following a Seed Round sold for fifteen percent (15%) of the post-money fully-diluted
> capitalization, this position would represent approximately 16.875%; that figure is
> **illustrative only**, and the actual post-Seed percentage depends on the final size, price and
> structure of the Seed Round."

So the number survives as an illustration and stops being a representation. If you resize the
round, these documents do not become wrong and do not need re-papering.

**Other places the 15% assumption is still hardcoded and will break on a resize** — all internal,
none in a counterparty document:
- `2026-09-10-sunjay-partner-agreement-DRAFT5-generator.py` — dilution table (60.750% / 16.875% /
  833,333 / 740,741 / 4,938,272)
- `2026-08-15-greg-strategic-adviser-agreement.md` §2.2 — `[4]%` → `[3.4]%` at `[15]%`
- `cinderella/CLAUDE.md`, `CURRENT.md`, `CONTRACT-REGISTER.md`

---

## Checked and found correct — no change made

- **Share arithmetic ties out exactly.** Founder 3,000,000 (Class B) + Sunjay 833,333 + Ankur
  166,667 + Greg 166,667 = **4,166,667** pre-Seed fully diluted. Founder 72.0%, Sunjay 20.0%,
  Ankur 4.0%, Greg 4.0% — matches the cap table in `cinderella/CLAUDE.md`.
- **Vesting installments both tie out.** Sunjay: 416,666 vested at signing + 23 × 17,361 + 17,364
  = 833,333 ✓. Greg: 23 × 6,944 + 6,955 = 166,667 ✓.
- **Authorized capital is sufficient.** 6,000,000 Class A authorized against ~1,166,667 issued
  pre-Seed; even with a 15% seed, Sunjay's full 5% of milestone shares and Ankur's top-up, Class A
  stays well under the ceiling.
- **§3.1 repurchase at "the lower of price paid or FMV"** — founder-favorable and correct. At a
  $0.001 grant price, the lower is always $0.001.
- **§2.4 Milestone grants** — Ankur's copy was made objective and automatic (issuance on
  achievement, not on a Company determination). **Deliberately NOT propagated.** Sunjay's Track B
  is board-attributed *by design* per the Partner Agreement, and in any event his Schedule A
  grants no Milestone Shares here ("Milestone Shares are NOT granted by this Agreement"); Greg has
  no milestones at all. §2.4 is inoperative in both documents as drafted. **It becomes live when
  the Track A / Track B milestone RSPA is papered — fix it then, and only for Track A.**

---

## Flagged, not changed

- **Greg's RSPA carries a "DRAFT — FOR DISCUSSION ONLY — NOT LEGAL ADVICE" banner. Sunjay's does
  not.** Greg's Stockholders' Agreement does not either. Left alone in all three: stripping a
  not-legal-advice disclaimer off a document drafted without counsel is the wrong direction. If
  anything Sunjay's RSPA should gain one until Loeb has read it. Your call.
- **Signature-block cosmetics.** Sunjay's RSPA has no "By:" line under the Company signature
  (Greg's does); Greg's PURCHASER block has empty Name and Email where Sunjay's is pre-filled.
  Cosmetic, and patching signature blocks via run surgery carries more risk than it is worth.
- **"Seed Round" and "Investors" are used but never defined in the Stockholders' Agreement.**
  Pre-existing in all three copies, not introduced by these changes. A Loeb cleanup item. I left
  it rather than fix it in one copy and reintroduce the divergence this pass just eliminated.
- **No spousal consent page** on either RSPA. Not required in Delaware; worth a question to Loeb
  if either man is in a community-property state.

---

## Open items this pass created or carried forward

1. ⚠️ **Board resolution fixing $0.001 as FMV**, dated on or before the Effective Date. The
   documents now assert it. Blocking.
2. ⚠️ **Do not countersign either RSPA until the 83(b) elections are prepared.** 30 days,
   non-extendable, from the Effective Date.
3. **Conform Greg's Strategic Adviser Agreement** to the settled RSPA terms (4%, 24 months, no
   cliff, no acceleration, 3.375%, Rule 701). Not yet done.
4. **Confirm whether Greg is accredited** — moot under Rule 701, live if you ever switch his grant
   to Reg D.
5. **Loeb, one email:** Rule 701(c) capital-raising carve-out for Ankur; Rule 701 availability for
   Sunjay and Greg; FMV/409A support for $0.001; whether a spousal consent is wanted.
6. **Decide Greg's acceleration** — none (as built) or single-trigger on a Change of Control.
7. **Still outstanding from the Ankur pass:** the Tabor OBA Approval (a condition precedent to
   Ankur's *entire* agreement, §0, still undelivered); the two capital-return asks to Ankur
   (30 days' notice, sunset on a priced round).
