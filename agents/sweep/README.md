# Sweep

Real-time content sweeps for Norman (formerly Overheard, renamed 2026-10-08).

- Recurring sweeps on saved topics: only breaking, significant (major or trade outlet, or a primary source), or widely shared and trending items get reported. Silent otherwise.
- On-demand: "please run a sweep on <topic>", default window 48 hours.
- Mentions: Norman's name in all spellings, Making Cinderella, and Cinderella Corp.
- Time scope: hours up to about 48 hours. Anything 30 days or longer goes to Current.
- Sources: X first, then news, then Reddit (currently blocked from the box), YouTube, Hacker News, and public IG/FB.
- Active sweeps (updated 2026-10-09): College Basketball (NIL, revenue sharing, transfer portal, PE in college sports), every 2 hours from 7:13 AM to 11:13 PM ET. Norman & Brand Mentions, every other morning at 7:43 AM ET (cron `43 7 */2 * *`, odd days of the month), 48-hour window.
- Rules: no invented items, draft-only, never posts externally. Every reported item includes a clickable link to its source X post or article (Norman rule 2026-10-09). Recipe is the content-sweep skill.
