# THE GRASS

*A vertical tutorial slice of a medieval fantasy sandbox visual novel.*

**Faeblue · the borderlands of Hella · the stormy season**

---

## Play it

The playable build is a browser game. From the repository root:

```bash
cd the-grass-web
python3 build.py --serve
# open http://localhost:8000
```

`build.py` assembles `the-grass-web/dist/` from the game sources and the
Ren'Py 8.5.3 WebAssembly runtime, then serves it. The folder is a plain
static site — you can drop it on any web host.

> First load takes a few seconds: the browser downloads the engine
> (~40 MB) and compiles the game's `.rpy` sources in-page. Saves live in
> the browser's IndexedDB, so they survive a reload but live on that
> machine.

To work on the game itself, edit the `.rpy` files in `the-grass/game/` and
re-run `python3 build.py`.

---

## What it is

Ten **interconnected, navigable locations**, each with its own background
and its own people:

| # | Location | Who is there |
|---|----------|--------------|
| 1 | **The East Gate** | Corin, the gateward · Harrow, an orkish drover |
| 2 | **Market Row** | Marta, the innkeeper · Seppa, a caravan trader |
| 3 | **The Moot Hall** | Elandi, the late mayor's wife |
| 4 | **The Salt & Lantern** | Marta · Corin, off duty |
| 5 | **The Witches' School** | Sister Ivo, storm-warden · Tamsin, third-year |
| 6 | **The Mayor's House** | Elandi |
| 7 | **The Long Pass** | Tamsin · Harrow |
| 8 | **The Watchtower** | Master Oren, of the border watch · Seppa |
| 9 | **The Great Dead Grass** | Vashk, a Ravager scout |
| 10 | **The Caravan Camp** | Vashk · Seppa |

You can walk between them from the start. There is no fixed order.

### The loop

- **Map** — travel to any location. Travel costs a bell; twelve bells make
  a storm day.
- **People** — everyone present is listed on the left with a portrait.
  Click one to open their topics.
- **Look** — a longer description of the place, which changes as the
  season does.
- **Notes** — everything Alexandria is told goes into her notebook. This is
  the tutorial's memory: topics unlock from what is in it.
- **World** — a short glossary of Faeblue, the Grass, the Ravagers, the
  moot, and the rest.

The sandbox **responds to time**. On the second day of the storm the
Western caravan comes in off the Grass — whether you are at the gate or
not. The season ends with the fifth storm, and where you have been and
who you have listened to decides how the slice closes.

---

## The world

**Faeblue** is a high-fantasy world where humans and elves are the most
numerous of the speaking peoples. Along its north-eastern edge the fertile
coastal belt gives way, all at once, to **the Great Dead Grass**: a vast
expanse of thick grey weeds that cannot be farmed, cannot be tamed, and
cannot be crossed quickly.

Beyond the Grass live the **Ravager tribes** — orkish and beastmen bands
that roam it, and that in a hard season move through the borderlands. They
are the standing adversary of the human and elven realms, and the Grass is
the moat between them.

**Hella** sits where a long thin pass comes down out of the mountain
chains. It is defended by a timber palisade, governed by a moot, and —
unusually for a border village — *prosperous*, because it hosts a
**preparatory school for undergraduate witches**. The school, not the
farming, is what keeps Hella fed.

Every fortnight or so in the stormy season, a caravaner brave and lucky
enough to make it through the Grass arrives with goods from the Western
coasts. They almost always wait out the storms and sail back West.
Some say half of them get lost in the Grass.
Some say half is optimistic.

**Alexandria** is the daughter of **Elandi**, the late mayor's wife and now
the de-facto leader of Hella. She is not the mayor. She is the mayor's
daughter, which in Hella is a different and more tiring thing.

---

## How it is built

```
the-grass/                 the Ren'Py project
  game/
    script.rpy             prologue, ending, character/sprite definitions
    world.rpy              the ten locations, the cast, the clock, the lore
    people.rpy             every topic for every character
    explore.rpy            the sandbox loop: travel, look, wait, talk
    events.rpy             story events: the caravan, the fifth storm
    screens.rpy            the vertical HUD, map, topics, notebook
    gui.rpy                the visual identity
    images/bg/             ten 720x1280 backgrounds
    images/char/           ten 320x320 sprites
    images/portrait/       ten 256x256 headshots for the HUD
    fonts/                 Cinzel + Alegreya (SIL OFL)

the-grass-web/
  build.py                 assembles dist/ from the game + the runtime
  runtime/                 the Ren'Py 8.5.3 WebAssembly engine

the-grass-art/
  raw/                     the full-size generated backgrounds
  tools/build_assets.py    backgrounds -> game art, LPC layers -> sprites
  tools/fetch_assets.sh    fetches the LPC sprite bank
  DESIGN.md                the design document
  CREDITS.md               attribution
```

### Why a vertical stage

The game runs at **720x1280**. The background art is generated at 9:16, so
a vertical stage uses the whole composition instead of cropping the top and
bottom off it — which is what a 16:9 stage would do. It also matches how
most people will actually play it: a phone held upright.

### Regenerating the art

The backgrounds in `the-grass/game/images/bg/` are downscaled derivatives
of `the-grass-art/raw/*.png`:

```bash
cd the-grass-art/tools
python3 build_assets.py bg
```

The ten character sprites are composited from the **Universal LPC
Spritesheet** bank and recoloured onto the ULPC palette ramps:

```bash
./fetch_assets.sh          # sparse checkout into /tmp/lpcgen
python3 build_assets.py char
```

Every character is a list of LPC layers in `build_assets.py` — body, head,
hair, clothes, boots, hat — with a palette ramp per layer. Change the list
and rebuild to change the cast.

---

## Credits

Backgrounds are AI-generated for this project. The cast uses the
Universal LPC Spritesheet pack (**CC-BY-SA 3.0 / GPL 3.0**), and the fonts
are Cinzel and Alegreya under the SIL Open Font License. Full attribution
and the upstream author list are in **[`the-grass-art/CREDITS.md`](the-grass-art/CREDITS.md)**.

Engine: **Ren'Py 8.5.3** (MIT).
