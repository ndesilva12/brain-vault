# Cinderella Corp — Contract Register
_Master list of every agreement the structure requires. Status as of 2026-09-03. Update as documents are drafted, negotiated, and executed._

**Structural principle:** the **SPV is the contracting hub** for each school project. **Cinderella Corp sits above** as owner of the Format/Franchise IP and as an equity holder. Every counterparty contracts with the SPV, and the SPV holds only a limited, revocable, single-project **Format License**. No counterparty can therefore acquire the franchise.

**2026-09-03 corrections (Jimmy):** (a) Layer 1.1 is the *filed* 6M Class A / 4M Class B amendment, not the unfiled 20M A&R. (b) 1.7 Sunjay Partner Agreement is drafted, not executed — revised version in flight after the Sep 1 call. (c) 1.12 founder RSA was accelerated and signed; Aug 11 83(b) already mailed. Detail: `2026-09-03-founder-rsa-acceleration.md` and `Process/2026-09-03-jimmy-working-state.md`.

> ⭐ **2026-10-07 — VERSIONS OF RECORD.** `current-versions-2026-10-07/` holds the text of the
> **nine** documents Norman actually sent out, and supersedes the Sep 18 generators wherever they
> disagree (the sent Ankur Adviser Agreement carries a **§0 Tabor OBA condition precedent** the
> generator never had). Revised builds: `out-2026-10-07/` (Ankur, 5 docs) and
> `out-sunjay-greg-2026-10-07/` (Sunjay + Greg, 4 docs). Memos:
> `2026-10-07-ankur-october-redline-response.md`, `2026-10-07-sunjay-greg-review.md`.
>
> ⚠️ **THE STOCKHOLDERS' AGREEMENT IS ONE AGREEMENT.** Everybody signs that one text or a joinder
> to it. On 2026-10-07 three divergent copies were in flight — Ankur's carried a firm D&O trigger
> in §2.6 and a new §2.7 (no personal liability of the Investor Representative) that Sunjay's and
> Greg's did not. §2.7 works by consent, so it would have been unenforceable against the two who
> signed without it, **and Sunjay is the Class A majority (71% pre-Seed), whose consent §9.2 makes
> necessary to amend.** All three were conformed and §2.6/§2.7 are now character-identical across
> them, verified programmatically. **Never issue a per-person copy of this agreement again without
> diffing it against the others.**
>
> ⭐ **2026-10-07 STAGE 2 — Ankur's final cleanup list applied.** `out-2026-10-07-final/`
> supersedes `out-2026-10-07/`; built by `2026-10-07-ankur-final-build.py`, chained off stage 1.
> **83(b) removed from his RSPA** (§5.1 restated, Schedule B deleted) — fully vested shares are not
> substantially nonvested property, so no election applies; now consistent with Adviser Agmt §2.7.
> **Expense & Travel Policy actually attached** as Side Letter Exhibit A (40 paragraphs, not a
> placeholder). **Side Letter dated October.** **Cap table reconciled in full** in RSPA Schedule A.
>
> ⭐ **THE SEED ROUND IS NO LONGER 15 × $100K.** At Ankur's request the Subscription Agreement now
> describes **an offering of up to $1,500,000 at $2.025/share — no minimum aggregate raise, may close
> for less, no minimum individual subscription, one or more closings**, with officers and affiliates
> able to subscribe on the same terms, which covers the **$50K each from Norman and Sunjay**.
> Deleted: the $100,000 minimum allocation, "approximately one percent (1.0%)", and "15 such
> allocations … representing 15% of the Company". **Ownership now follows shares purchased and the
> final post-close cap table, nothing else.** Stage 1's size-agnostic §2.5 is what makes this work;
> the old "(the $1,500,000 / 15% raise)" wording would now be wrong.
>
> **Math, verified:** pre-Seed FD 4,166,667 = 3,000,000 Founder (B) + 833,333 Sunjay + 166,667 Ankur
> + 166,667 Greg. At a full raise: 740,741 sh × $2.025 = $1,500,000; post-Seed FD 4,938,272
> (= 4,000,000 / 0.81); Norman 60.750 / Sunjay 16.875 / Ankur 4.000 (after a 30,864 top-up) / Greg
> 3.375 / seed 15.000 = 100.000%. Partial raise of $X: S = floor(X / 2.025), Ankur's post-Seed total
> = (4,000,000 + S) / 24. ⚠️ The sent Subscription Agreement said 740,74**5** — a rounding error,
> now moot.
>
> ⚠️ **THREE BLOCKERS BEFORE ANY OF THESE EXECUTE.** (1) The **board resolution fixing $0.001 as the
> FMV of a Class A share**, dated on or before the Effective Date — all four RSPAs now assert that
> determination and it does not yet exist. (2) **83(b) elections prepared before countersignature**
> — Sunjay's and Greg's shares vest, so the 30-day statutory window is non-extendable and the IRS
> grants no reasonable-cause relief. Both Effective Dates are still blank, so nothing is late yet.
> (3) ⚠️ **The filed Certificate of Incorporation must be inserted as Subscription Agreement
> Exhibit A.** It is NOT in the vault, so it could not be built in — the exhibit is now a clean cover
> page reading "follows this page" rather than a drafting instruction. **Norman has to drop the
> Delaware-stamped PDF in before this goes to any investor;** §1 contains an investor representation
> pointing at that exhibit.
>
> ⚠️ **Still open on Ankur's side:** the **Tabor OBA Approval**, a condition precedent to his
> *entire* agreement under §0, remains undelivered — and the two capital-return asks to him
> (30 days' notice; sunset on a priced round) have not been put.
>
> **Securities exemption splits by person, deliberately:** **Ankur → Reg D 506(b) / §4(a)(2)**,
> because Rule 701(c) excludes services rendered in connection with a capital-raising transaction
> and his §1.1 services *are* capital formation. **Sunjay and Greg → Rule 701 primary, §4(a)(2)
> fallback** — neither raises capital, and 701 avoids the accredited-investor question (Greg's
> status is still unconfirmed) and the Form D. Rule 701 and Reg D offerings do not integrate.

---

## LAYER 1 — Parent company (Cinderella Corp.)

| # | Agreement | Parties | Status | File |
|---|---|---|---|---|
| 1.1 | Certificate of Incorporation + Class A/B amendment | Delaware / Company | ✅ COI filed 2026-04-13 File 10581972 (10M common). Amendment **FILED 2026-08-12** SR 20264045049: 6M Class A + 4M Class B. Draft A&R 20M (15A+5B) was **never filed** | *(Delaware; stamped cert sent to Loeb)* |
| 1.2 | Bylaws | Company | ❌ Confirm exists / board size = 3 | — |
| 1.3 | Seed Term Sheet | Company ↔ Investors | ✅ Drafted (clean) | `clean/Term_Sheet.md` |
| 1.4 | Stock Purchase Agreement (+ accredited questionnaire, risk factors) | Company ↔ each Investor | ✅ Drafted (clean). Loeb investor-doc package due **Fri 2026-09-05** | `clean/Stock_Purchase_Agreement.md` |
| 1.5 | **Revenue-Share Agreement** | Company ↔ each Investor | ✅ Drafted (clean) | `clean/Revenue_Share_Agreement.md` |
| 1.6 | Stockholders' Agreement | Company / Founder / Holders / Investors | ✅ Drafted. **ONE agreement — all holders sign this text or a joinder.** Revised 2026-10-07: §2.6 D&O a firm obligation at Seed close, new §2.7 exculpating the Investor Representative. **All three copies (Ankur / Sunjay / Greg) conformed and verified character-identical.** ⚠️ "Seed Round" and "Investors" are used but never defined — Loeb cleanup, fix in all three at once | `out-2026-10-07/` · `out-sunjay-greg-2026-10-07/` · `clean/Stockholders_Agreement.md` |
| 1.7 | Sunjay Mathews — Partner Agreement | Company ↔ Sunjay | ⚠️ Drafted; **not executed**. Sep 1 call: original too aggressive. Revised dated draft in Drive Legal > Seed Round (do not overwrite original). Norman sent 2026-09-03. **DRAFT 5 generated 2026-09-18** (accruing vesting, narrowed Cause, §2.6 acceleration, exact post-Seed dilution table). **Partner + Stockholder + RSPA emailed Sep 18 — watching signed return** | `2026-08-25-sunjay-partner-agreement.md` · `2026-09-10-sunjay-partner-agreement-DRAFT5-generator.py` |
| 1.8 | Ankur Jain — Strategic Adviser Agreement | Company ↔ Ankur | 🔄 Drafted; Norman moved to this after RSA signing 2026-09-03. **Revised 2026-09-18** post-redline — 4% fully vested, tiered platform milestone grid with a 5% aggregate cap, 12-month tail, Item 2 approval rights, automatic board seat. **Sep 18 redlines (immediate vesting / Tabor) still to fold — open** | `2026-09-18-ankur-adviser-agreement-generator.py` (notes: `2026-08-15-ankur-strategic-adviser-agreement.md`) |
| 1.9 | Greg Kristof — Strategic Adviser Agreement | Company ↔ Greg | ⚠️ **OUT OF SYNC WITH HIS RSPA — conform next.** Greg agreed $4k/mo Aug 30. The brackets were settled in his RSPA on 2026-10-07 (**4%, 24 months, no cliff, no acceleration, 3.375% post-Seed, Rule 701**) but this agreement still reads `[4]%` / `[24]` / `[Optional: acceleration — confirm]` / `[Rule 701 / Reg D]`, and its §2.2 says `[3.4]%` where the RSPA says 3.375%. **Not yet rebuilt** | `2026-08-15-greg-strategic-adviser-agreement.md` |
| 1.10 | Greg Kristof — Consulting Agreement (from 1/1/27) | Company ↔ Greg | ✅ Drafted | `2026-08-15-greg-consulting-agreement.md` |
| 1.11 | **Shane Duffy / Jay Jackson — Finder & Producer Agreement** | Company or SPV ↔ Shane & Jay | ❌ **NOT DRAFTED — needed soon.** SPV equity + $100K fee per attachment sourced; cap it, tie to deals they actually source, no parent equity | — |
| 1.12 | Restricted Stock Purchase Agreements + 83(b) | Company ↔ each holder | ✅ **Founder:** Aug 11 RSPA + 83(b) mailed; acceleration signed 2026-09-03. 🔄 **Ankur / Sunjay / Greg — all three revised 2026-10-07.** Share counts 166,667 · 833,333 · 166,667 (ties to 4,166,667 pre-Seed FD). **Price now stated as $0.001 = Board FMV in all three** (was blank / `$[____]` / bracketed). Exemption resolved: Ankur Reg D, Sunjay + Greg Rule 701. 83(b) §5.1 rewritten for Sunjay and Greg to state the 30-day window is non-extendable and what missing it costs. Ankur's shares are fully vested so 83(b) is moot for him. ⚠️ **BLOCKED on the Board FMV resolution; do not countersign Sunjay's or Greg's until their 83(b) elections are prepared.** Effective Dates still blank, so nothing is late | **Ankur's 83(b) language and Schedule B deleted entirely 2026-10-07 at his request** — moot for fully vested shares | `out-2026-10-07-final/` · `out-sunjay-greg-2026-10-07/` · `2026-10-07-sunjay-greg-review.md` |
| 1.13 | Mutual NDA / Non-Circumvention | Company ↔ counterparties | ✅ Exists (5-yr term, 3-yr non-circ tail, NY law) — regenerate file | — |
| 1.14 | Option pool / equity incentive plan | Company | ⏸ **Deliberately deferred** — creating it later dilutes everyone pro rata rather than founders alone | — |
| 1.15 | Loeb & Loeb engagement | Company ↔ Loeb | ✅ Engagement letter cleared 2026-09-02 (Brian Socolow, Evan Saunders) | — |

---

## LAYER 2 — Parent ↔ SPV (per school)

| # | Agreement | Parties | Status | File |
|---|---|---|---|---|
| 2.1 | **Format License** ⭐ | Cinderella Corp → SPV | ✅ Drafted. ⚠️ **OPEN 2026-09-30 — licenses the format but is silent on the AUDIENCE.** Add the fan membership data and the fan-facing channels as licensed assets alongside the format, revocable on the same terms, so a franchise-held member list carries to the next school instead of dying with the SPV. Rationale: `Process/2026-09-30-social-platforms-and-membership-ownership.md` | `2026-08-29-format-license-cinderella-to-spv.md` |
| 2.2 | SPV Certificate of Formation | Delaware | ❌ Per school | — |
| 2.3 | **SPV Operating Agreement** | All SPV members (Cinderella 40% · Talent 30% · Capital 30%) | ❌ **Core document — not drafted** | — |
| 2.4 | Management Services Agreement (2.5% annual fee) | Cinderella Corp ↔ SPV | ❌ Not drafted | — |
| 2.5 | Franchise fee (5% of capital called) | — | ✅ Covered in Format License §4.1 | — |

---

## LAYER 3 — SPV ↔ counterparties (per school project)

| # | Agreement | Parties | Status | File |
|---|---|---|---|---|
| 3.1 | **Term Sheet — Davidson Project (talent attachment)** ⭐ | Cinderella / SPV ↔ Unanimous + Curry | ✅ Drafted. Styled as a term sheet for signability; §2 Binding Effect makes it enforceable notwithstanding the caption. **Live status 2026-09-03: Curry attachment is a stalemate, not cleanly attached** | `2026-08-29-curry-conditional-attachment-agreement.md` |
| 3.2 | **Long-form Talent Services Agreement** | SPV ↔ talent loan-out | ❌ Follows the Trigger Date (45 days per §11) | — |
| 3.3 | **Talent Inducement Letter** | Individual talent (personal) | ❌ Accompanies 3.2 — talent personally guarantees the loan-out's performance | — |
| 3.4 | **Producer Agreement — talent's prodco** (e.g. Unanimous) | SPV ↔ prodco | ❌ **Keep SEPARATE from 3.2.** Davidson project only; no Franchise or format rights | — |
| 3.5 | School LOI | SPV/Company ↔ institution | ✅ **Davidson signed · St. Joseph's signed (SJU CFO)**; Merrimack & Belmont drafts out | — |
| 3.6 | **Definitive School Agreement** | SPV ↔ institution | ❌ Converts the LOI: access, rights, baseline, incremental revenue share, attribution, term, NCAA compliance | — |
| 3.7 | **Capital Subscription Agreement** | Capital partner (TCG / RedBird / Tabor) ↔ SPV | ❌ Not drafted. **Capital partner is deliberately NOT a party to 3.1** — its participation is a condition only, so sources can be swapped | — |
| 3.8 | **Production Services Agreement** | SPV ↔ ProdCo | ❌ Fee-for-service. No IP, no format rights, bounded season backend only. *See EWS redlines* | `2026-08-27-everwonder-counter-redline-memo.md` |
| 3.9 | Shopping / packaging agreement *(if any)* | Company ↔ producer | ⚠️ **EWS draft received 2026-08-26 — NOT SIGNED, counter issued.** Aug 27 concerns mail unanswered ~1 week as of 2026-09-03. Ownership + reversion are threshold items | `2026-08-27-everwonder-counter-redline-memo.md` |
| 3.10 | **Distribution / License Agreement** | SPV ↔ streamer | ❌ SPV collects the license fee; Cinderella retains the Format. Target a **license**, not a buyout | `Process/2026-08-15-streamer-deal-playbook.md` |
| 3.11 | **Athlete NIL Agreements** | SPV ↔ individual athletes | ❌ FMV for genuine content services; NIL Go / clearinghouse | `Process/2026-08-11-commercial-vs-revenue-rights-and-donor-path-memo.md` |
| 3.12 | **Sponsorship Agreements** | SPV (or Company, if franchise-wide) ↔ sponsors | ❌ Note: a **franchise-wide** master sponsorship contracts at the **parent**, not the SPV | — |
| 3.13 | Live-game / MTE agreements | SPV ↔ streamer / event operator | ❌ Per the model (live games, in-season tournament) | — |
| 3.14 | Merchandise / licensing | SPV or Company ↔ licensee | ❌ Confirm whether merch sits at SPV or parent | — |
| 3.15 | E&O insurance, D&O insurance | Company / SPV ↔ insurer | ❌ D&O promised in Ankur's agreement §4 | — |

---

## Priority order

1. **Founder RSA acceleration (1.12)** — signed 2026-09-03. File the signed PDFs in Drive Legal. Do not file Delaware.
2. **Sunjay revised Partner Agreement (1.7)** — send the new dated draft; leave the original.
3. **Ankur paper (1.8)** — in flight 2026-09-03.
4. **Loeb investor-doc package (1.4–1.6)** — due Fri 2026-09-05.
5. **SPV Operating Agreement (2.3)** — nothing at Layer 3 can close without it.
6. **Definitive School Agreement (3.6)** — converts the signed Davidson and SJU LOIs into real rights.
7. **Shane & Jay finder agreement (1.11)** — they are actively sourcing talent with no paper in place.
8. **Greg advisor paper (1.9)** — he is waiting.
9. **Capital Subscription (3.7)** — ready when a partner confirms.
10. **Long-form talent + inducement (3.2 / 3.3)** — triggered by the conditional attachment.

## Cap table (target, not all papered)

After Sunjay + Ankur + Greg grants: **Norman 72 / Sunjay 20 / Ankur 4 / Greg 4**. Then 15% seed dilutes Norman, Sunjay, and Greg; **Ankur stays 4%**. Post-seed: **Norman 60.75 / Sunjay 16.875 / Ankur 4 / Greg 3.375 / seed 15**. Ankur's non-dilution through seed must be in his agreement.

## Standing drafting rules
- **Format and Franchise IP never leave Cinderella Corp.** Counterparties attach to an SPV holding a single-project license.
- **Attach talent to the *school project*, never to "the project," "the series," or "Season 1."**
- **Keep talent-services and prodco-producer agreements separate**, even for the same party.
- **Sequencing authority stays with the parent** (Format License §2.3(d)).
- **Every downstream agreement carries the flow-through clause** (Format License §3.3).
- **"Created by Norman de Silva," first position**, on every project.
