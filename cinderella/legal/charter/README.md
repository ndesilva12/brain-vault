# Cinderella Corp — filed Delaware charter

The authoritative corporate documents, received from Norman 2026-10-07. Both are **scans with no
text layer**, so they are stored here as PDFs and bound into the Subscription Agreement as pages
rather than rebuilt as text.

| File | What | Filed | Pages |
|---|---|---|---|
| `01-certificate.pdf` | Certificate of Incorporation — File No. 10581972 | 04/13/2026 | 1 (Letter) |
| `02-amendment.pdf` | Certificate of Amendment, adopted under DGCL §242 | 08/12/2026 | 2 (A4) |

**The amendment is the operative capital-stock provision.** It replaces Article FOURTH in its
entirety:

- **6,000,000 Class A + 4,000,000 Class B**, $0.001 par, 10,000,000 total — **no preferred**
- Class A **1 vote**, Class B **10 votes**, voting together as a single class
- All common outstanding immediately before effectiveness **reclassified as Class B**
- Class B **converts automatically** to Class A on any transfer other than a Permitted Transfer,
  and converted shares are retired
- **Permitted Transfer** = a transfer by Norman C. de Silva to a revocable living trust or other
  estate-planning vehicle he controls, or to an entity wholly owned by him, in each case only
  while he retains exclusive voting power
- **Protective provision:** no amendment adversely affecting Class B without a majority of Class B
- **Article SIXTH** — limitation of director liability
- **Article SEVENTH** — indemnification and advancement for directors and officers

## How this ties to the agreement set

| Charter | Agreement |
|---|---|
| 6,000,000 / 4,000,000 / $0.001 | Stockholders' Agreement §1.1 ✓ |
| 1 vote / 10 votes | SHA §1.2 ✓ |
| Automatic conversion on non-Permitted Transfer | SHA §1.4 ✓ |
| Permitted Transfer defined for Class B | SHA §3.2 defers to the Certificate ✓ — no gap |
| No preferred authorized | Subscription Agmt "Governing Corporate Documents" ✓ |
| **Article SEVENTH indemnification** | ⭐ independently supports **SHA §2.6** (indemnification of the Investor Representative), alongside the D&O policy Norman agreed to bind at Seed close |

## Execution PDF

`2026-10-07-subscription-execution-pdf.py` renders the Subscription Agreement to PDF and splices
these two files in **directly after the Exhibit A cover page** — not at the end, because Exhibit A
precedes Exhibit B (Risk Factors) and the cover says the charter "follows this page". Output:
`out-2026-10-07-final/Cinderella_Corp_-_Subscription_Agreement_EXECUTION_with_Exhibit_A.pdf`
(10 agreement pages + 3 charter pages = 13).

⚠️ Page sizes differ (Letter vs A4). Left alone deliberately — rescaling a filed charter is worse
than a page-size change mid-exhibit.

⚠️ The amendment's own footer reads "NOT legal advice". That is in the **filed** document and
cannot be changed; it is odd in an investor exhibit but the filing is what it is.
