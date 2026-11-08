# THE GRASS

**A vertical sandbox visual novel — Faeblue, the borderland of Hella**

Tutorial slice / prototype. Ten interconnected locations, ten characters,
one fortnight in the stormy season.

---

## The world

**Faeblue** is a high-fantasy world where humans and elves are the most
numerous of the speaking peoples. Along its north-eastern edge, the fertile
coastal belt gives way, all at once, to **the Great Dead Grass**: a vast
expanse of thick grey weeds that cannot be farmed, cannot be tamed, and
cannot be crossed quickly.

Beyond the Grass live the **Ravager tribes** — orkish and beastmen warbands
that raid the borderlands in the stormy season. They are the standing
adversary of both the human and elven realms; the Grass is the moat between
the two.

## Hella

**Hella** is a border village built where a long, thin pass comes down
out of the mountain chains to meet the coastal road. It is defended by a
timber palisade, governed by a moot, and — unusually for a border village —
*prosperous*, because it hosts a **preparatory school for undergraduate
witches**. Families from the coasts send their daughters up the pass to be
taught weather-sense, sigils and storm-warding; the school, not the farming,
is what keeps Hella fed.

Every fortnight or so in the stormy season, a caravaner brave and lucky
enough to make it through the Grass arrives with a load of goods from the
Western coasts. They almost always wait out the storms and sail back West.
Some say half of them get lost in the Grass. Some say half is optimistic.

**Alexandria** is the daughter of **Elandi**, the late mayor's wife and now
the de-facto leader of Hella. She is not the mayor. She is the mayor's
daughter, which in Hella is a different and more tiring thing.

## The slice

The game opens on the first day of the stormy season, with a caravan
overdue and a Ravager sign-scare in the Grass. The player has until the
caravan must leave to decide what kind of person Alexandria is going to be
in her mother's village, and to find out what is actually walking in the
weeds.

Ten locations, freely navigable from the start after the prologue. Each has
its own background, its own people, its own small economy of rumours, and
at least one thing that only becomes available after somewhere else has
been visited.

### The ten locations

| # | Location | Background | Cast |
|---|----------|-----------|------|
| 1 | The Gate | `bg_gate` | Corin (gateward), Harrow (orkish drover) |
| 2 | Market Row | `bg_market` | Marta (innkeeper), Seppa (orkish trader) |
| 3 | The Moot Hall | `bg_moot` | Elandi (Alexandria's mother) |
| 4 | The Salt & Lantern | `bg_inn` | Marta, Corin (off duty) |
| 5 | The Witches' School | `bg_school` | Sister Ivo, Tamsin (student) |
| 6 | The Mayor's House | `bg_house` | Elandi, Alexandria's own room |
| 7 | The Pass | `bg_pass` | Tamsin, Harrow |
| 8 | The Watchtower | `bg_watchtower` | Master Oren, Seppa |
| 9 | The Grass | `bg_grass` | Vashk (beastman scout) |
| 10 | The Caravan Camp | `bg_camp` | Vashk, the caravan-master |

### Loop

- **Move** between locations from the map screen, or by walking the
  location links (the gate leads to the pass, the pass to the Grass).
- **Talk** to whoever is present; each character has a small set of
  topics that unlock as you learn things elsewhere.
- **Time** advances one bell per action; the storm clock runs for a
  fortnight of twelve bells. The slice ends when the caravan sails.
- **Notes** — everything you are told goes into Alexandria's notebook,
  which is the tutorial's way of teaching Ren'Py state: flags, variables
  and conditional dialogue.

### Tone

Quiet, wet, grey-green, and dryly funny. The Grass is not a monster; it is
a place where the map stops being useful. The Ravagers are not monsters
either, which is the problem.

---

## Implementation

- Ren'Py 8.5.3, vertical stage **720x1280**.
- All ten backgrounds are AI-generated (see `the-grass-art/raw/`).
- Characters are composited from the **Universal LPC Spritesheet** pack
  (CC-BY-SA 3.0 / GPL 3.0), recoloured onto the ULPC palette ramps.
- Fonts: Cinzel (display), Alegreya (body), both SIL OFL.
- Build output: a browser-playable Ren'Py web build in `the-grass-web/`.
