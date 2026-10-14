# -*- coding: utf-8 -*-
"""Build the seven NEW slides for the Netflix version of the Making Cinderella deck.

These are drop-ins for the existing deck, matched to its visual language (16:9 at 720x405pt,
letterspaced caps header rule, heavy black headline, cyan accent, navy title treatment). They are
NOT a replacement for the real deck — Norman has a designed Google Slides file; these carry the
content and approximate the style so the slides can be rebuilt there quickly.

Rationale for each slide is in ../Outputs/2026-10-14-netflix-deck-rebuild.md.

Renders via Chromium headless (LibreOffice cannot open or produce anything in this container).
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "2026-10-14-Making-Cinderella-NEW-SLIDES-Netflix.pdf"

CHROME = next((c for c in ["/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
                           "/opt/pw-browsers/chromium/chrome-linux/chrome",
                           "/usr/bin/chromium"] if Path(c).exists()), None)
assert CHROME, "no chromium"

ACCENT = "#1E9BF0"
NAVY = "#0A2A4A"
INK = "#111111"
MUTE = "#6B7684"

CSS = """
@page { size: 10in 5.625in; margin: 0; }
* { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: "Liberation Sans", Arial, Helvetica, sans-serif; color: %(ink)s; }
.slide { position: relative; width: 10in; height: 5.625in; page-break-after: always;
         background: #fff; padding: 0.42in 0.55in 0.4in 0.55in; overflow: hidden; }
.hdr { display: flex; justify-content: space-between; align-items: baseline;
       border-bottom: 1px solid #D5DBE2; padding-bottom: 7pt; }
.hdr .l, .hdr .r { font-size: 9.5pt; font-weight: 700; letter-spacing: .20em; }
.hdr .r { color: %(ink)s; }
h1 { font-size: 27pt; font-weight: 800; letter-spacing: -.012em; margin: 20pt 0 4pt 0;
     line-height: 1.04; }
h1.sm { font-size: 22pt; }
.sub { font-size: 11.5pt; color: %(mute)s; margin: 0 0 14pt 0; font-weight: 600; }
.acc { color: %(acc)s; }
.pg { position: absolute; right: 0.3in; bottom: 0.2in; font-size: 9pt; color: #9AA5B1; }

/* three-column story blocks */
.cols { display: flex; gap: 16pt; margin-top: 8pt; }
.col { flex: 1; }
.col .k { font-size: 10pt; font-weight: 800; letter-spacing: .13em; color: %(acc)s;
          margin-bottom: 5pt; }
.col .kk { font-size: 9pt; color: %(mute)s; font-weight: 600; margin-bottom: 7pt; }
.col p { font-size: 10pt; line-height: 1.44; margin: 0 0 7pt 0; }

/* rows */
.row { display: flex; gap: 12pt; align-items: flex-start; margin-bottom: 9pt; }
.row .lbl { flex: 0 0 1.45in; font-size: 9.5pt; font-weight: 800; letter-spacing: .09em;
            color: %(navy)s; padding-top: 1pt; }
.row .val { flex: 1; font-size: 10.2pt; line-height: 1.42; }

/* big numbered beats */
.beats { display: flex; gap: 18pt; margin-top: 14pt; }
.beat { flex: 1; border-top: 3px solid %(acc)s; padding-top: 9pt; }
.beat .t { font-size: 9pt; font-weight: 800; letter-spacing: .15em; color: %(mute)s;
           margin-bottom: 6pt; }
.beat p { font-size: 10.2pt; line-height: 1.45; margin: 0; }

.kicker { margin-top: auto; background: %(navy)s; color: #fff; padding: 11pt 14pt;
          font-size: 11pt; font-weight: 600; line-height: 1.4; border-radius: 3pt; }
.kicker .acc { color: #6CC4FF; }
.quote { text-align: center; font-size: 15pt; font-style: italic; color: %(navy)s;
         margin: 16pt 0 0 0; font-weight: 600; }
.flexcol { display: flex; flex-direction: column; height: 100%%; }

.ask { display: flex; gap: 14pt; margin-top: 12pt; }
.ask .a { flex: 1; border: 1.5px solid %(acc)s; border-radius: 5pt; padding: 12pt; }
.ask .n { font-size: 20pt; font-weight: 800; color: %(acc)s; line-height: 1; }
.ask .h { font-size: 11pt; font-weight: 800; margin: 6pt 0 5pt 0; }
.ask p { font-size: 9.6pt; line-height: 1.4; margin: 0; color: #333; }

.seasons { display: flex; gap: 14pt; margin: 14pt 0 10pt 0; }
.season { flex: 1; background: #F3F7FB; border-left: 4px solid %(acc)s; padding: 10pt 12pt; }
.season .y { font-size: 9pt; font-weight: 800; letter-spacing: .12em; color: %(mute)s; }
.season .w { font-size: 11.5pt; font-weight: 800; margin-top: 4pt; line-height: 1.25; }
ul { margin: 6pt 0 0 0; padding-left: 14pt; }
li { font-size: 10pt; line-height: 1.5; margin-bottom: 4pt; }
.warn { font-size: 8.6pt; color: #B4452F; margin-top: 8pt; font-weight: 600; }
""" % dict(acc=ACCENT, navy=NAVY, ink=INK, mute=MUTE)


def slide(right, body, n):
    return f'''<div class="slide"><div class="flexcol">
      <div class="hdr"><div class="l">MAKING CINDERELLA</div><div class="r">{right}</div></div>
      {body}</div><div class="pg">{n}</div></div>'''


S = []

# ── 4 · THE SHOW ────────────────────────────────────────────────────────────────
S.append(slide("THE SHOW", '''
<h1>TWO SEASONS OF TELEVISION<br>FROM ONE SEASON OF BASKETBALL</h1>
<div class="sub">8&ndash;10 episodes &middot; two drops &middot; one continuous story</div>
<div class="cols">
  <div class="col">
    <div class="k">PART ONE &mdash; THE BUILD</div>
    <div class="kk">4&ndash;6 EPISODES &middot; RELEASED OCTOBER, BEFORE THE FIRST GAME</div>
    <p>The assembly. A celebrity alumnus returns to a program that has not mattered in twenty
    years and is handed a top-ten budget. An NBA scout hunts the portal for players the system
    overlooked. Coaches, families, agents, money.</p>
    <p><b>Ends on the roster being finished &mdash; and the first game unplayed.</b></p>
  </div>
  <div class="col">
    <div class="k">PART TWO &mdash; THE SEASON</div>
    <div class="kk">4&ndash;6 EPISODES &middot; RELEASED MARCH, INTO THE TOURNAMENT</div>
    <p>What the money bought. Chemistry, injury, pressure, and a campus that has never carried
    expectation before.</p>
    <p><b>Ends in March &mdash; on a result nobody involved can script.</b></p>
  </div>
</div>
<div class="kicker"><b class="acc">Why the split works.</b> Part One turns the audience into
stakeholders <i>before the outcome exists</i>. They watch the season in real time having already
chosen a side &mdash; so the show builds its own live audience for the games.</div>''', 4))

# ── 5 · EPISODE ONE ─────────────────────────────────────────────────────────────
S.append(slide("EPISODE ONE", '''
<h1>THE COLD OPEN</h1>
<div class="beats">
  <div class="beat"><div class="t">MINUTE ONE</div>
    <p>March 2008. Davidson, a 10-seed, beats Gonzaga, Georgetown and Wisconsin. Stephen Curry,
    20 years old, outscores entire teams. One basket from the Final Four.</p></div>
  <div class="beat"><div class="t">MINUTE THREE</div>
    <p>The same gym, empty. Seventeen seasons. No tournament wins. A coach explaining that his
    best player left in April for a school that offered $800,000.</p></div>
  <div class="beat"><div class="t">MINUTE FIVE</div>
    <p>Curry walks back into that gym &mdash; and this time he has a checkbook.</p></div>
</div>
<div class="quote">&ldquo;Everybody loves a Cinderella.<br>Nobody noticed that we killed her.&rdquo;</div>
<div class="kicker">The tournament&rsquo;s best story has been quietly defunded.
<b class="acc">This is the first attempt to buy it back.</b></div>''', 5))

# ── 7 · ACCESS ──────────────────────────────────────────────────────────────────
S.append(slide("ACCESS", '''
<h1 class="sm">WE CONTROL THE ROOM</h1>
<div style="margin-top:12pt">
  <div class="row"><div class="lbl">THE SCHOOL</div><div class="val">Signed LOI and exclusivity
    with Davidson. Campus, locker room, film sessions, admissions, faculty, the town.</div></div>
  <div class="row"><div class="lbl">THE LEAD</div><div class="val">Stephen Curry &mdash; verbally
    committed, and <b>Assistant GM at Davidson</b>. The athletic director, the head coach and
    Curry are former teammates.</div></div>
  <div class="row"><div class="lbl">THE FRONT OFFICE</div><div class="val">We <i>are</i> the front
    office. Roster construction, agent calls and NIL negotiations happen inside our entity &mdash;
    <b>the cameras are already in the room where the decisions get made.</b></div></div>
  <div class="row"><div class="lbl">THE PLAYERS</div><div class="val">Participation is contracted
    at signing. Access is a term of the deal, not a favour asked later.</div></div>
  <div class="row"><div class="lbl">THE MONEY</div><div class="val"><b>Open books.</b> The fan
    platform publishes roster spend in real time. No sports documentary has ever had this.</div></div>
</div>
<div class="kicker"><i>Last Chance U</i> had to ask permission to film.
<b class="acc">We own the building.</b></div>''', 7))

# ── 9 · WHO'S MAKING IT ─────────────────────────────────────────────────────────
S.append(slide("PRODUCTION", '''
<h1 class="sm">WHO&rsquo;S MAKING IT</h1>
<div style="margin-top:12pt">
  <div class="row"><div class="lbl">PRODUCTION</div><div class="val">
    <b>[ BOARDWALK PICTURES ]</b> &nbsp;<span style="color:#6B7684">Last Chance U &middot; Cheer
    &middot; Chef&rsquo;s Table</span></div></div>
  <div class="row"><div class="lbl">SHOWRUNNER</div><div class="val"><b>[ TBD ]</b></div></div>
  <div class="row"><div class="lbl">EXEC PRODUCERS</div><div class="val">Stephen Curry &middot;
    Norman de Silva &middot; Sunjay Mathews</div></div>
  <div class="row"><div class="lbl">NORMAN DE SILVA</div><div class="val">NBA scout &mdash;
    Celtics, Spurs, Rockets, 76ers. Coached in China (Foshan &mdash; subject of an Amazon
    documentary), Japan and Spain. <b>The on-screen evaluator, and the person who actually builds
    the roster.</b></div></div>
  <div class="row"><div class="lbl">SUNJAY MATHEWS</div><div class="val">Sports media executive
    &mdash; FanDuel, DAZN.</div></div>
</div>
<div class="warn">&#9888; DO NOT PRESENT THIS SLIDE WITH TBDs. If the producer is not attached, cut
the slide and handle it verbally. Netflix buys from producers with a track record.</div>''', 9))

# ── 11 · AUDIENCE ───────────────────────────────────────────────────────────────
S.append(slide("AUDIENCE", '''
<h1 class="sm">WHO SHOWS UP</h1>
<div class="sub">Three audiences that do not normally overlap.</div>
<div class="cols">
  <div class="col"><div class="k">COLLEGE BASKETBALL</div>
    <p>68 teams, every region. March Madness is the most geographically distributed audience in
    American sport &mdash; and every one of those schools has an alumni base that has been told
    for fifteen years that it cannot compete.</p></div>
  <div class="col"><div class="k">THE LEAD&rsquo;S AUDIENCE</div>
    <p>Which is not a sports audience. Curry&rsquo;s following is global, and skews younger and
    more female than college basketball&rsquo;s.</p></div>
  <div class="col"><div class="k">THE UNDERDOG DOC</div>
    <p>The <i>Wrexham</i> crossover &mdash; proof the format travels to people with no prior
    interest in the sport or the league.</p></div>
</div>
<div class="kicker"><b class="acc">The structural advantage:</b> a franchise where every season
recruits a new regional fanbase &mdash; Charlotte, then Philadelphia, then Boston &mdash; and keeps
the previous one.</div>
<div class="warn">&#9888; ADD CURRENT HOURS-VIEWED FOR QUARTERBACK / FULL SWING / STARTING 5 /
WREXHAM BEFORE THE MEETING. Netflix thinks in hours viewed &mdash; speak their unit.</div>''', 11))

# ── 14 · THE FRANCHISE ──────────────────────────────────────────────────────────
S.append(slide("FRANCHISE", '''
<h1 class="sm">THIS IS NOT ONE SHOW</h1>
<div class="seasons">
  <div class="season"><div class="y">SEASON 1 &middot; 2027&ndash;28</div>
    <div class="w">Davidson &times; Curry</div>
    <div style="font-size:9.5pt;color:#6B7684;margin-top:4pt">A second school in parallel</div></div>
  <div class="season"><div class="y">SEASON 2 &middot; 2028&ndash;29</div>
    <div class="w">Two more schools</div>
    <div style="font-size:9.5pt;color:#6B7684;margin-top:4pt">Women&rsquo;s basketball</div></div>
  <div class="season"><div class="y">SEASON 3 &middot; 2029&ndash;30</div>
    <div class="w">New sports, new tiers</div>
    <div style="font-size:9.5pt;color:#6B7684;margin-top:4pt">D3 reclassification &middot; hockey
    &middot; lacrosse</div></div>
</div>
<div style="display:flex;gap:20pt">
  <div style="flex:1">
    <div class="k" style="font-size:10pt;font-weight:800;letter-spacing:.13em;color:#1E9BF0;margin-bottom:6pt">WHY IT COMPOUNDS</div>
    <ul>
      <li><b>The format is the asset, not the school.</b> New campus, new lead, new region &mdash;
      same engine.</li>
      <li><b>~300 eligible programs.</b> The supply does not run out.</li>
      <li><b>Every season recruits a new regional audience</b> and keeps the last one.</li>
      <li><b>An immovable annual finale.</b> The tournament sets the date.</li>
    </ul>
  </div>
</div>
<div class="kicker"><i>Welcome to Wrexham</i> found one club.
<b class="acc">There are three hundred.</b></div>''', 14))

# ── 15 · THE ASK ────────────────────────────────────────────────────────────────
S.append(slide("THE ASK", '''
<h1 class="sm">WHAT WE&rsquo;RE ASKING FOR</h1>
<div class="ask">
  <div class="a"><div class="n">01</div><div class="h">SERIES ORDER &mdash; SEASON 1</div>
    <p>Two parts, 8&ndash;10 episodes, global.</p></div>
  <div class="a"><div class="n">02</div><div class="h">FIRST LOOK ON THE FRANCHISE</div>
    <p>Right of first refusal across Seasons 2 and 3.</p></div>
  <div class="a"><div class="n">03</div><div class="h">THE LIVE GAMES</div>
    <p>Three marquee non-conference matchups built for this purpose. Davidson vs. Kansas (2008
    rematch), vs. North Carolina (1969 rematch), vs. Duke (<b>Stephen vs. Seth Curry</b>). Dates
    and venues controlled by us, scheduled around the series.</p></div>
</div>
<div class="kicker"><b class="acc">What you get that is not available anywhere else:</b> the only
sports documentary where the production company <i>is</i> the front office &mdash; with a
live-event package attached and a finale date set by the NCAA tournament.</div>
<div class="warn">&#9888; FILL IN THE NUMBER BEFORE YOU WALK IN. Decide whether it goes on the
slide or is delivered verbally, depending on where the producer conversation stands.</div>''', 15))

html = (f"<!doctype html><html><head><meta charset='utf-8'><title>Making Cinderella — new slides</title>"
        f"<style>{CSS}</style></head><body>{''.join(S)}</body></html>")

tmp = Path("/tmp/mc_slides.html")
tmp.write_text(html, encoding="utf-8")
r = subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={OUT}", f"file://{tmp}"],
                   capture_output=True, text=True, timeout=300)
assert OUT.exists(), f"chromium produced nothing:\n{r.stdout}\n{r.stderr}"

n = int(subprocess.run(["pdfinfo", str(OUT)], capture_output=True, text=True
                       ).stdout.split("Pages:")[1].split()[0])
assert n == len(S), f"expected {len(S)} slides, got {n}"
print(f"wrote {OUT.name}  ({n} slides)")
