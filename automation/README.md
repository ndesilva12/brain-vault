# Vault Capture Bridge

Makes the casual loop work: **email a note → it lands in the right Google Doc**, so any AI
(Claude, ChatGPT, Gemini, Grok) *or* your plain Mail app / Siri can capture into the vault
surfaces. Needed because the Google Drive connector is **read/create-only** — Claude (chat or
Code) can read these Docs but cannot append to them in place. Google Apps Script runs as *you*
and has full write access, so it does the appending.

## How capture works
Send an email to **`norman.desilva+capture@gmail.com`** with a routing word in the **subject**:

| Subject contains | Filed into |
|---|---|
| `thought` / `thoughts` | THOUGHTS — Norman (appended at bottom) |
| `idea` / `ideas` / `note` / `notes` | Ideas & Notes — Norman (appended at bottom) |
| `task` / `to-do` / `list` | Cinderella / Vault — Task List (top of OPEN) |
| anything else | Ideas & Notes, tagged `[unrouted]` |

- The note can be **entirely in the subject** (e.g. subject: `thought: call Cullen re: deck`) —
  fastest on mobile — or in the body. Both are captured.
- Lands within ~5 minutes (timer cadence). Each entry is timestamped (America/New_York).
- **Only mail sent from `norman.desilva@gmail.com` is processed**; anything else is ignored.

## Install (once, ~5 min)
1. Go to **script.google.com** → **New project**; name it `Vault Capture Bridge`.
2. Delete the stub, paste all of **`vault-capture-bridge.gs`**, and Save.
3. Select the **`setup`** function in the toolbar → **Run**.
4. Authorize when prompted. It's your own script, so Google shows an "unverified app" screen →
   **Advanced → Go to Vault Capture Bridge (unsafe)** → allow **Gmail** + **Docs** scopes.
5. Done. A 5-minute trigger now runs `processCaptures`, and it processes anything already waiting.

## Everyday use tips
- **Add a Gmail/Contacts entry "Vault Capture" = `norman.desilva+capture@gmail.com`** for one-tap send.
- **Siri, no AI needed:** "Send an email to Vault Capture, subject *thought*, body: …"
- **From any AI:** "Email this to norman.desilva+capture@gmail.com, subject line *idea*."
- To pause: in Apps Script → Triggers → delete the `processCaptures` trigger.

## Notes / limits
- If Google adds a Docs-writing connector later, we can retire this. Until then it's the reliable
  path for AI/voice → Doc.
- Doc IDs are hard-coded in `CFG` at the top of the script; update there if a doc is ever replaced.
- Tasks land at the top of the OPEN list; thoughts/ideas append to the bottom (newest last).
