# MAKING CINDERELLA — Concept Sizzle Reel
### Script, outline, AI-generation prompt kit, and OpenArt step-by-step
_Draft 2026-08-07 (rev. 2026-08-08 — tightened narration). Target runtime 2:30–2:45. This is a
**concept/tone teaser**, not represented as real footage._
**New to OpenArt? Jump to §7 for the click-by-click walkthrough.**

---

## 0. Read this first (framing + guardrails)

- **The thesis:** big money has put the Cinderella story on life support. Making Cinderella asks the
  only question left — if money is what wins now, can money bring the underdog *back*? Someone who
  loves a small school more than anyone bets it can, and we film everyone it touches.
- **Position it honestly.** Open on a 1.5s super: _"Concept visualization."_ Protects credibility.
- **NO real likenesses.** No Steph, Simu, Woody, or any real person. Anonymous players and a
  **silhouetted/backlit "believer"** figure — kept generic so it reads as alum *or* adopted celebrity.
  The star names live in the deck, not on screen.
- **NO real marks.** Generic solid-color uniforms, blank courts, invented town names. No real logos.
- **Consistency is everything.** Append the **Style Block** (§3) to every prompt.

---

## 1. Cost strategy (the part that actually controls spend)

**Engine split — reserve the expensive engine for the moments that need it.**

| Use | Engine | Why |
|---|---|---|
| Hero close-ups, the buzzer, the horn, the bookend — native audio + max realism | Veo 3.1 Quality — 4 shots | Highest cost; save it |
| Single-subject cinematic b-roll + the quiet portraits | Veo 3.1 Fast/Lite — ~10 shots | Cheaper Veo tier |
| Crowds, weight room, court-storm, town, money-arena, montages | Kling — ~14 shots | Cheapest for multi-person motion |

**Six rules:** (1) nail the prompt → fewer re-rolls (~2 gens/shot); (2) generate at ≈4–5s, extend in
the edit; (3) image-to-video for the pricey shots (still first, §4b); (4) reuse b-roll; (5) do audio/
music/VO in the edit; (6) skip Quality Veo unless it's a "hero."

---

## 2. The script (the spine)

One idea per beat; the narration should flow as a single spare read, not seven separate statements.

| # | Beat | ~Time | Narration / on-screen text |
|---|---|---|---|
| 1 | **The danger** | 0:00–0:18 | _"March used to belong to the underdog. Then the money came — and the Cinderella story started to vanish."_ · TEXT: **"CINDERELLA IS DYING."** |
| 2 | **The believer** | 0:18–0:40 | _"Every forgotten school has someone who loves it more than anyone. What if they stopped funding buildings — and built a team instead?"_ |
| 3 | **The bet** | 0:40–1:05 | _"If money is what wins now — why not aim it at a school worth rooting for?"_ |
| 4 | **The build** | 1:05–1:40 | _"Money can buy a roster. It can't buy the rest. Can it build a Cinderella anyway? We're going to find out."_ |
| 5 | **The untold ones** | 1:40–2:05 | _"A Cinderella team is never just the players — the families, the professors, the alumni. A hundred stories the country only sees for one week in March. If ever."_ |
| 6 | **March** | 2:05–2:25 | _"And somewhere in March… a miracle stops being an accident."_ |
| 7 | **Title / tag** | 2:25–2:45 | TITLE: **MAKING CINDERELLA** · TAG: _"Cinderella always had to be home by midnight. Not this time."_ |

_Alt danger-card line if "dying" reads too hard: **"CINDERELLA IS ON LIFE SUPPORT."**_
_Alt tags (midnight / the dance): "Every Cinderella gets one dance. We're building hers." · "This time, the dance doesn't end at midnight." · "The clock strikes twelve. We strike back."_

**Music:** spare, aching piano/strings under 1–2; a low pulse enters on the "money" turn; Americana
post-rock build through 3–5; trailer orchestral+drums for 6; big hit on the title. **License before use.**

---

## 3. The Style Block (paste at the end of EVERY prompt)

> Cinematic documentary style, anamorphic widescreen 2.39:1, shot on Arri Alexa with vintage
> anamorphic lenses, subtle 35mm film grain, shallow depth of field, naturalistic motivated lighting,
> high dynamic range, photoreal. Anonymous subjects, generic solid-color athletic uniforms, no logos,
> no text, no recognizable real people.

**Palette modifiers:**
- **BEFORE** (beats 1–2): _add_ "desaturated cold steel-blue palette, overcast, melancholy, still air."
- **RISE** (beats 4–7): _add_ "warm amber and gold palette, golden-hour glow, volumetric light, energy."

---

## 4. Shot list + copy-paste prompts

_Format: **# — Engine — duration.** Then the prompt (append Style Block + palette). New shots this
rev carry a letter suffix so numbering stays stable._

### BEAT 1 — The danger (BEFORE)  ·  _VO: "March used to belong to the underdog…"_
**1 — Veo 3.1 Quality (audio) — 5s** _(HERO)_
> Extreme slow motion, a worn leather basketball rolls to a stop on a cracked, sunlit outdoor asphalt
> court, a rusted chain net sways above, dust drifts through a low shaft of light, no people. Ambient
> audio: one lonely bounce echo, faint wind.

**1A — Kling — 4s** _("Then the money came" — the antagonist)_
> A gleaming, sold-out blue-blood basketball mega-arena at night, cold blue light, a giant LED ring
> streaming sponsor logos and glowing numbers, overwhelming corporate scale, the crowd a faceless sea.

**2 — Kling — 5s** _(the casualty)_
> A vast empty small-college basketball arena, thousands of empty wooden seats, a single work light
> glowing, dust motes floating, slow push-in down the aisle toward the dark court.

**3 — Veo 3.1 Fast — 4s** _(what we're losing) → cut to TEXT: "CINDERELLA IS DYING."_
> Tight close-up on a young male athlete's face half in shadow, breathing slowly, eyes lifting upward
> with quiet resolve, sweat on his brow, black background.

### BEAT 2 — The believer (BEFORE→warmth)  ·  _VO: "…someone who loves it more than anyone…"_
**3A — Veo 3.1 Fast — 5s** _(the believer returns — kept generic: alum OR adopted)_
> A well-dressed figure walks alone into a dim, empty college gym and stops beneath faded championship
> banners, reaching up to touch one, seen from behind, a single shaft of light, dust in the air.

**4 — Kling — 6s** _(reusable b-roll)_
> Slow aerial drift at dawn over a small American college town in autumn: a water tower, a white church
> steeple, a quiet brick main street, mist in the low valley.

**5 — Kling — 4s**
> Slow tilt up to faded championship banners high in dark gymnasium rafters, edges frayed, dust catching
> thin light, a cobwebbed trophy case below.

**6 — Veo 3.1 Fast — 5s**
> A weathered older basketball coach stands alone at center court in an empty gym at night, hands in
> jacket pockets, looking up at the rafters, single overhead light, long shadow.

### BEAT 3 — The bet (transition)  ·  _VO: "If money is what wins now — why not aim it at a school worth rooting for?"_
**7 — Veo 3.1 Fast — 5s**
> A black SUV pulls up to a small brick college fieldhouse at dusk, a well-dressed figure steps out
> fully backlit as a silhouette, face not visible, headlights flare, breath visible in cold air.

**8 — Kling — 4s**
> Two pairs of hands shake across a wood-paneled office desk, a signed document and a fountain pen
> between them, warm lamplight, shallow focus.

**9 — Kling — 5s** _(reusable b-roll — the lights come back on)_
> Stadium floodlights snap on in sequence across a dark basketball arena, banks of light igniting one
> after another, lens flares blooming, the court emerging from black into brilliant glow.

### BEAT 4 — The build (RISE)  ·  _VO: "Money can buy a roster. It can't buy the rest…"_
**10 — Veo 3.1 Quality (audio) — 5s** _(HERO)_
> Slow push-in on athletic sneakers cutting and squeaking across a polished hardwood court during a
> footwork drill, sweat droplets flying, early-morning gym light streaming through high windows. Audio:
> rhythmic squeak of shoes, ball bounce, breath.

**11 — Kling — 5s**
> A college weight room at dawn, several anonymous athletes in matching plain uniforms grinding through
> lifts in unison, chalk dust in shafts of light, steam, intensity.

**12 — Kling — 5s**
> A team bus rolls down an empty rural highway at dusk, headlights on, rolling farmland and a pink-orange
> sky behind, low tracking shot alongside.

**13 — Veo 3.1 Fast — 4s**
> Macro close-up of an athlete's hands wrapping white tape around a wrist, then gripping a basketball
> hard, tendons flexing, warm side light.

**14 — Kling — 4s**
> Workers on a lift hang a fresh new championship-style banner in gymnasium rafters, another repaints a
> blank center-court circle, warm afternoon light through windows.

### BEAT 5 — The untold ones (RISE)  ·  _VO: "…the families, the professors, the alumni…"_
**15 — Kling — 5s**
> Time-lapse of a small-college arena filling with fans, seats going from half-empty to packed, a wave
> of color and motion, energy building, warm arena glow.

**15A — Veo 3.1 Fast — 4s** _(the janitor)_
> An older janitor slowly sweeps the empty hardwood court at dawn, alone, long shadow, warm light
> through high windows, quiet dignity and routine.

**15B — Veo 3.1 Fast — 4s** _(the professor)_
> A professor writes on a chalkboard in a near-empty lecture hall, chalk dust drifting in a beam of
> morning light, seen from the back rows, quiet devotion.

**15C — Kling — 5s** _(the families)_
> A mother and two young children in packed arena stands, faces tight with hope then leaping up in joy;
> intercut a single child shooting at a worn driveway hoop at dusk in a small town.

**16 — Veo 3.1 Quality (audio) — 5s — the dagger** _(HERO)_
> Slow motion, an anonymous player rises for a long three-pointer at the buzzer, ball spinning off the
> fingertips, a blurred roaring crowd behind, golden light. Audio: swelling crowd, then a beat of
> silence as the ball hangs.

**17 — Kling — 5s**
> A packed student section erupts and storms forward in pandemonium, bodies leaping, arms up, confetti
> and thrown cups, chaotic joy, handheld energy.

**18 — Kling — 4s**
> Inside a small-town diner, a dozen locals leap up from booths cheering at a TV, coffee spilling, an
> old man throws his cap, warm nostalgic light.

### BEAT 6 — March (RISE)  ·  _VO: "And somewhere in March… a miracle stops being an accident."_
**19 — Kling — 5s**
> A massive tournament arena packed to the rafters, confetti cannons, generic-uniformed players
> mid-celebration on court, a bracket-style graphic motif in the LED ring, blinding lights.

**20 — Veo 3.1 Quality (audio) — 5s — the horn** _(HERO)_
> Slow motion final buzzer, anonymous players collapse to the floor in ecstatic disbelief, the coach
> drops to his knees with arms raised, confetti rains. Audio: final horn blast, eruption.

**21 — Veo 3.1 Fast — 5s**
> Slow motion, a player rides teammates' shoulders holding scissors after cutting down the net, a ladder
> against the hoop, ticker-tape falling through golden spotlight.

### BEAT 7 — Title / tag (RISE)
**22 — Kling — 6s**
> A dark map of the United States, points of golden light igniting one by one across many small towns
> until the whole country glows, cinematic, symbolic of a spreading movement.

**23 — Veo 3.1 Fast — 6s — bookend** _(callback to Shot 1)_
> The same worn outdoor asphalt basketball court from before, now at golden hour with a full cheering
> crowd blurred behind the rim, the chain net swaying, warm light, hopeful, alive.

**TITLE CARD (edit, not generated):** black → **MAKING CINDERELLA** in your Cormorant Garamond
letterhead face → tag _"Cinderella always had to be home by midnight. Not this time."_ → hold → cut.

---

## 4b. Image-to-video still prompts (money-saver for the Veo shots)

**Workflow:** generate the **still** in OpenArt's cheap image model → curate 2–3 → upload the winner as
the **first-frame** into Veo (image-to-video) → apply the motion from the matching §4 prompt. Append the
**Style Block + palette**. Stills describe a *frozen composition* — no motion words.

**Still 1** > A worn leather basketball at rest on a cracked, sunlit outdoor asphalt court, a rusted chain net hanging above, dust suspended in a low shaft of light, no people, ball in the lower third, negative space above. Static first frame.

**Still 3** > Tight close-up of a young male athlete's face half in shadow, eyes lifting upward with quiet resolve, sweat beading on his brow, black background, Rembrandt lighting. Static first frame.

**Still 3A** (the believer) > A well-dressed figure stands alone beneath faded championship banners in a dim empty gym, hand raised toward a frayed banner, seen from behind, single shaft of light, dust in the air. Static first frame.

**Still 6** > Wide shot, a weathered older coach stands alone at center court in an empty gym at night, hands in jacket pockets, a single overhead light pooling around him, long shadow, faded banners in the dark rafters above. Static first frame.

**Still 7** > A black SUV parked at a small brick college fieldhouse at dusk, a well-dressed figure silhouetted stepping out, fully backlit by headlights, face not visible, visible cold breath, lens flare. Static first frame.

**Still 10** > Low macro of athletic sneakers planted on polished hardwood mid-drill, single sweat droplet suspended, warm morning light from high gym windows, soft court reflections. Static first frame.

**Still 13** > Macro close-up of hands wrapping white athletic tape around a wrist and gripping a basketball, tendons flexed, warm side light, dark background. Static first frame.

**Still 15A** (janitor) > An older janitor mid-sweep on an empty hardwood court at dawn, alone, long shadow, warm light through high windows, quiet dignity. Static first frame.

**Still 15B** (professor) > A professor at a chalkboard in a near-empty lecture hall, chalk dust in a morning light beam, seen from the back rows. Static first frame.

**Still 16** (HERO) > Low hero angle, an anonymous player frozen at the peak of a jump-shot release, ball balanced on the fingertips, a blurred packed crowd behind, golden rim-light, apex of the leap. Static first frame.

**Still 20** (HERO) > An anonymous player collapsed to the court floor in ecstatic disbelief, the coach on his knees with arms raised just behind, confetti suspended mid-air, blinding arena lights. Static first frame.

**Still 21** > A player lifted on teammates' shoulders holding scissors beside a hoop with a ladder, a cut net in hand, ticker-tape suspended in a golden spotlight. Static first frame.

**Still 23** (bookend, match Still 1) > The same worn outdoor asphalt court, now at golden hour with a full cheering crowd blurred behind the rim, the chain net still, warm hopeful light, composition mirroring the opening frame. Static first frame.

---

## 5. Assembly notes
- **Edit software:** CapCut (free, fast) or DaVinci Resolve (free, more control). Color-match Veo↔Kling.
- **Cut rhythm:** 2.5s holds in beats 1–2, tightening to ~1s by beat 4, 0.5–0.75s rapid cuts in beats
  5–6, then the held 3s+ bookend. Cut on the music's beat.
- **VO:** spare, low, intimate read (AI VO for the draft; real VO for the final buyer version). Leave air.
- **Text cards:** two only — "CINDERELLA IS DYING." and the title. Restraint reads premium.

## 6. Do-not-ship checklist
- [ ] "Concept visualization" super at head
- [ ] Zero real faces (talent lives in the deck, not the reel)
- [ ] Zero real logos/marks
- [ ] Music licensed (or clearly a temp track flagged as temp)
- [ ] Runtime ≤ 2:45

---

## 7. OpenArt — step by step (do this)

_Verified against OpenArt's current flow, Aug 2026. Credit numbers are list values — confirm the live
cost on the generate screen before you batch; all models draw from **one shared credit pool**._

### A. Setup (once)
1. Go to **openart.ai**, sign up / log in. New accounts get free starter credits.
2. **Get a paid plan for the real push** — the free tier caps how many clips/day you can make on the
   top Veo tier. A paid plan lifts the caps.
3. **Know the three Veo tiers by cost:** **Lite ≈ 10 cr** (cheap b-roll), **Fast ≈ 20 cr** (mid),
   **Quality ≈ 100 cr** (reserve for the 4 hero shots). **Kling** = your crowd engine.

### B. Generate the STILLS first — for the Veo shots (the money-saver)
1. Open the **Image** generator.
2. Paste a **Still prompt (§4b)** + **Style Block (§3)** + palette line.
3. Aspect ratio **16:9** (OpenArt video is 16:9 or 9:16 — there is **no 2.39:1**; you'll crop in the edit).
4. Generate 2–4 variations, **download the single best.** Images are cheap — re-roll here, not in video.

### C. Animate them — Image-to-Video (Veo 3.1)
1. **Video → Image-to-Video → select Veo 3.1.**
2. **Upload your chosen still** as the first frame.
3. Paste the matching **§4 video prompt** (the motion).
4. Settings: **Audio ON** for the 4 hero shots (1, 10, 16, 20), **OFF** for the rest · **1080p** ·
   **Aspect 16:9** · **Duration 4–6s** · **Video Mode = Quality** for the heroes, **Fast/Lite** otherwise.
5. Generate. If it's close, re-roll **once**. Download.

### D. The Kling shots — Text-to-Video (no still needed)
1. **Video → Text-to-Video → select Kling.**
2. Paste the **§4 prompt** + **Style Block** + palette.
3. **Aspect 16:9 · Duration 5s.** Generate 1–2, keep the winner.

### E. Budget reality (ballpark, list credits)
- 4 heroes × 2 × 100 = **800** · ~10 Veo-fast × 2 × ~15 = **~300** · ~14 Kling × 2 × ~25 = **~700** ·
  stills = cheap. **First full pass ≈ 1,900–2,700 credits** with normal re-rolls.
- Buy a credit pack / plan sized to that, and **watch daily clip caps** on the Quality tier.

### F. Assemble
CapCut or DaVinci Resolve → **crop every 16:9 clip to 2.39:1** → color-match Veo↔Kling → cut to the
beat → drop in VO + licensed track → add the "Concept visualization" head super and the title card. Export 1080p.
