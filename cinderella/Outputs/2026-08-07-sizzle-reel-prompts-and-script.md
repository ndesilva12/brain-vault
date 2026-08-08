# MAKING CINDERELLA — Concept Sizzle Reel
### Script, outline, and AI-generation prompt kit (OpenArt.ai · Veo 3.1 + Kling)
_Draft 2026-08-07. Target runtime 2:20–2:40. This is a **concept/tone teaser**, not
represented as real footage._

---

## 0. Read this first (framing + guardrails)

- **What this is:** an aspirational mood teaser that sells the *feeling* of the franchise —
  the ache of the overlooked program, the bet, the build, the run. It supplements the deck;
  it is not a proof-of-access reel (no season is filmed yet).
- **Position it honestly.** Open on a 1.5s super: _"Concept visualization."_ That one card
  removes any suggestion the footage is real and protects credibility in a buyer room.
- **NO real likenesses.** Do not generate Steph Curry, Simu Liu, Woody Harrelson, or any real
  person. Use anonymous players and a **silhouetted/backlit "believer"** figure. The star names
  live in the deck and the pitch, not on screen.
- **NO real marks.** Generic solid-color uniforms, blank courts, invented town names. Never a
  real school logo.
- **Consistency is everything.** Append the **Style Block** (§3) to every prompt so 23 clips
  read as one film.

---

## 1. Cost strategy (the part that actually controls spend)

**Engine split — reserve the expensive engine for the moments that need it.**

| Use | Engine | Why |
|---|---|---|
| Hero close-ups, the buzzer moment, the bookend, anything needing native audio + max realism | **Veo 3.1** (full) — only ~3 shots | Highest cost per clip; save it |
| Most single-subject cinematic shots | **Veo 3.1 Fast** — ~5 shots | Cheaper Veo tier; good enough for b-roll heroes |
| All crowds, weight room, storming the court, town scenes, montages | **Kling** — ~15 shots | Cheapest for multi-person motion; its strength |

**Six rules to keep credits down:**
1. **Nail the prompt → fewer re-rolls.** Budget ~2 generations per shot. ~23 shots × 2 ≈ **46 generations** — that's your real cost. Check OpenArt's live per-model credit price and multiply; don't guess.
2. **Generate at the shortest clip length the engine allows (≈5s).** You extend in the edit with speed-ramps and holds. Long clips cost more and you only use 1–2s of most.
3. **Image-to-video for the pricey shots.** Generate a cheap *still* first in OpenArt's image model, pick the best one, then animate only the winner. Turns expensive video re-rolls into cheap image re-rolls.
4. **Reuse b-roll.** The town aerial, the stadium-lights-snapping-on, and the outdoor-hoop bookend each serve multiple cuts via reframing/speed. Generate once, use three times.
5. **Do all audio, music, and VO in the edit** (CapCut/Resolve/Premiere), not per-clip. Let Veo's native audio give you ambient texture on hero shots only.
6. **Skip full Veo unless the shot is a "hero."** Veo Fast or Kling covers 20 of 23 shots.

---

## 2. Structure & voiceover (the spine)

Seven beats, accelerating cut-rhythm (slow 2–3s holds early → 0.5–1s cuts in the run → one long
held bookend). VO is spare, intimate, earned — not hype.

| # | Beat | ~Time | VO / on-screen text |
|---|---|---|---|
| 1 | **Cold open — the ache** | 0:00–0:18 | _"Every year, one team the country forgot… becomes the only one it remembers."_ |
| 2 | **The forgotten** | 0:18–0:40 | _"Three hundred sixty schools in Division One. Most will never be seen."_ |
| 3 | **The bet** | 0:40–1:05 | TEXT: **"What if the Cinderella run wasn't luck?"** |
| 4 | **The build** | 1:05–1:40 | _"Not a fairy tale. A build. The work nobody films."_ |
| 5 | **The rise** | 1:40–2:05 | _"The wins nobody expected. A season nobody saw coming."_ |
| 6 | **The run (March)** | 2:05–2:25 | _"And somewhere in March… a miracle stops being an accident."_ |
| 7 | **The promise / logo** | 2:25–2:40 | TITLE: **MAKING CINDERELLA** · TAG: _"Glass slippers aren't found. They're made."_ |

**Music:** swelling Americana post-rock build (Explosions in the Sky / _Friday Night Lights_ energy)
under beats 1–4, transitioning to a trailer-ized orchestral+drum build for 5–6, big hit on the
title. **License any track before real use** — don't ship a pitch on an unlicensed needle-drop.

---

## 3. The Style Block (paste at the end of EVERY prompt)

> Cinematic documentary style, anamorphic widescreen 2.39:1, shot on Arri Alexa with vintage
> anamorphic lenses, subtle 35mm film grain, shallow depth of field, naturalistic motivated
> lighting, high dynamic range, photoreal. Anonymous subjects, generic solid-color athletic
> uniforms, no logos, no text, no recognizable real people.

**Palette modifiers:**
- **BEFORE** (beats 1–2): _add_ "desaturated cold steel-blue palette, overcast, melancholy, still air."
- **RISE** (beats 4–7): _add_ "warm amber and gold palette, golden-hour glow, volumetric light, energy."

---

## 4. Shot list + copy-paste prompts

_Format: **# — Engine — duration — VO/text.** Then the prompt (append Style Block + palette)._

### BEAT 1 — Cold open (BEFORE palette)
**1 — Veo 3.1 (full, audio) — 5s — VO line 1 begins**
> Extreme slow motion, a worn leather basketball rolls to a stop on a cracked, sunlit outdoor
> asphalt court, a rusted chain net sways above, dust drifts through a low shaft of light, no
> people. Ambient audio: one lonely bounce echo, faint wind.

**2 — Kling — 5s**
> A vast empty small-college basketball arena, thousands of empty wooden seats, a single work
> light glowing, dust motes floating, slow push-in down the aisle toward the dark court.

**3 — Veo 3.1 Fast — 4s**
> Tight close-up on a young male athlete's face half in shadow, breathing slowly, eyes lifting
> upward with quiet resolve, sweat on his brow, black background.

### BEAT 2 — The forgotten (BEFORE palette)
**4 — Kling — 6s — VO line 2** _(reusable b-roll)_
> Slow aerial drift at dawn over a small American college town in autumn: a water tower, a
> white church steeple, a quiet brick main street, mist in the low valley.

**5 — Kling — 4s**
> Slow tilt up to faded championship banners high in dark gymnasium rafters, edges frayed,
> dust catching thin light, a cobwebbed trophy case below.

**6 — Veo 3.1 Fast — 5s**
> A weathered older basketball coach stands alone at center court in an empty gym at night,
> hands in jacket pockets, looking up at the rafters, single overhead light, long shadow.

### BEAT 3 — The bet (transition BEFORE→RISE)
**7 — Veo 3.1 Fast — 5s**
> A black SUV pulls up to a small brick college fieldhouse at dusk, a well-dressed figure steps
> out fully backlit as a silhouette, face not visible, headlights flare, breath visible in cold air.

**8 — Kling — 4s**
> Two pairs of hands shake across a wood-paneled office desk, a signed document and a fountain
> pen between them, warm lamplight, shallow focus.

**9 — Kling — 5s — TEXT: "What if the Cinderella run wasn't luck?"** _(reusable b-roll)_
> Stadium floodlights snap on in sequence across a dark basketball arena, banks of light igniting
> one after another, lens flares blooming, the court emerging from black into brilliant glow.

### BEAT 4 — The build (RISE palette)
**10 — Veo 3.1 (full, audio) — 5s — VO line 4** _(HERO)_
> Slow push-in on athletic sneakers cutting and squeaking across a polished hardwood court during
> a footwork drill, sweat droplets flying, early-morning gym light streaming through high windows.
> Audio: rhythmic squeak of shoes, ball bounce, breath.

**11 — Kling — 5s**
> A college weight room at dawn, several anonymous athletes in matching plain uniforms grinding
> through lifts in unison, chalk dust in shafts of light, steam, intensity.

**12 — Kling — 5s**
> A team bus rolls down an empty rural highway at dusk, headlights on, rolling farmland and a
> pink-orange sky behind, low tracking shot alongside.

**13 — Veo 3.1 Fast — 4s**
> Macro close-up of an athlete's hands wrapping white tape around a wrist, then gripping a
> basketball hard, tendons flexing, warm side light.

**14 — Kling — 4s**
> Workers on a lift hang a fresh new championship-style banner in gymnasium rafters, another
> repaints a blank center-court circle, warm afternoon light through windows.

### BEAT 5 — The rise (RISE palette)
**15 — Kling — 5s — VO line 5**
> Time-lapse of a small-college arena filling with fans, seats going from half-empty to packed,
> a wave of color and motion, energy building, warm arena glow.

**16 — Veo 3.1 (full, audio) — 5s — the dagger** _(HERO)_
> Slow motion, an anonymous player rises for a long three-pointer at the buzzer, ball spinning
> off the fingertips, a blurred roaring crowd behind, golden light. Audio: swelling crowd,
> then a beat of silence as the ball hangs.

**17 — Kling — 5s**
> A packed student section erupts and storms forward in pandemonium, bodies leaping, arms up,
> confetti and thrown cups, chaotic joy, handheld energy.

**18 — Kling — 4s**
> Inside a small-town diner, a dozen locals leap up from booths cheering at a TV, coffee spilling,
> an old man throws his cap, warm nostalgic light.

### BEAT 6 — The run / March (RISE palette)
**19 — Kling — 5s — VO line 6**
> A massive tournament arena packed to the rafters, confetti cannons, generic-uniformed players
> mid-celebration on court, a bracket-style graphic motif in the LED ring, blinding lights.

**20 — Veo 3.1 (full, audio) — 5s — the horn** _(HERO)_
> Slow motion final buzzer, anonymous players collapse to the floor in ecstatic disbelief, the
> coach drops to his knees with arms raised, confetti rains. Audio: final horn blast, eruption.

**21 — Veo 3.1 Fast — 5s**
> Slow motion, a player rides teammates' shoulders holding scissors after cutting down the net,
> a ladder against the hoop, ticker-tape falling through golden spotlight.

### BEAT 7 — The promise / logo (RISE palette)
**22 — Kling — 6s**
> A dark map of the United States, points of golden light igniting one by one across many small
> towns until the whole country glows, cinematic, symbolic of a spreading movement.

**23 — Veo 3.1 Fast — 6s — bookend** _(callback to Shot 1)_
> The same worn outdoor asphalt basketball court from before, now at golden hour with a full
> cheering crowd blurred behind the rim, the chain net swaying, warm light, hopeful, alive.

**TITLE CARD (edit, not generated):** black → **MAKING CINDERELLA** in your Cormorant Garamond
letterhead face → tag line _"Glass slippers aren't found. They're made."_ → hold → cut to black.

---

## 5. Assembly notes
- **Edit software:** CapCut (free, fast) or DaVinci Resolve (free, more control). Do color-match
  passes so Veo and Kling clips share the grade — Kling tends warmer/softer; match to the Veo look.
- **Cut rhythm:** 2.5s holds in beats 1–2, tightening to ~1s by beat 4, 0.5–0.75s rapid cuts in
  beats 5–6, then the held 3s+ bookend. Cut on the music's beat.
- **VO:** record a spare, low, intimate read (or an AI VO for the draft; hire a real VO for the
  final buyer version). Leave air — don't wall-to-wall it.
- **Text cards:** two only ("What if the Cinderella run wasn't luck?" and the title). Restraint reads premium.

## 6. Do-not-ship checklist
- [ ] "Concept visualization" super at head
- [ ] Zero real faces (talent lives in the deck, not the reel)
- [ ] Zero real logos/marks
- [ ] Music licensed (or clearly a temp track flagged as temp)
- [ ] Runtime ≤ 2:40
