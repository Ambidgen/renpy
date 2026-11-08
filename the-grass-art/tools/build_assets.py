"""The Grass - asset pipeline.

Turns the raw AI-generated backgrounds and the LPC sprite layers into
game-ready art:

  raw/*.png            vertical 768x1376 backgrounds
    -> images/bg/*.jpg 1920x1080 (cropped for a 16:9 stage)

  LPC layers           64x64 pixel-art parts
    -> images/char/*.png 256x256 sprites (4x nearest-neighbour)

Requires Pillow and a checkout of the Universal LPC Spritesheet
Character Generator (see tools/fetch_assets.sh).
"""
import glob
import json
import os
import sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)          # the repository root, holds the-grass/
GAME = os.path.join(REPO, "the-grass", "game")
RAW = os.path.join(ROOT, "raw")
BG_OUT = os.path.join(GAME, "images", "bg")
CH_OUT = os.path.join(GAME, "images", "char")
PORT_OUT = os.path.join(GAME, "images", "portrait")

LPC = os.environ.get("LPC_DIR", "/tmp/lpcgen/spritesheets")
PAL = os.environ.get("LPC_PAL", "/tmp/lpcgen/palette_definitions")

# The Grass is a vertical visual novel: the stage is 720x1280 (9:16).
# The generated art is 768x1376, which is the same 9:16 ratio, so the
# backgrounds are rescaled rather than cropped - no composition is lost.
BG_SIZE = (720, 1280)
CROP_BIAS = 0.46         # only used if a raw image ever differs in ratio

FRAME = 64
FRONT_ROW = 2            # LPC sheets: row 0 up/back, 1 left, 2 down/front, 3 right
SPRITE_SCALE = 5


# ---------------------------------------------------------------- backgrounds

def backgrounds():
    os.makedirs(BG_OUT, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(RAW, "bg_*.png"))):
        name = os.path.basename(path)[:-4]
        im = Image.open(path).convert("RGB")
        w, h = im.size
        target_ratio = BG_SIZE[0] / BG_SIZE[1]
        if abs(w / h - target_ratio) > 0.01:
            # crop to the stage ratio, biased slightly above centre
            crop_h = min(int(round(w / target_ratio)), h)
            top = int(round((h - crop_h) * CROP_BIAS))
            im = im.crop((0, top, w, top + crop_h))
        im = im.resize(BG_SIZE, Image.LANCZOS)
        out = os.path.join(BG_OUT, name + ".jpg")
        im.save(out, quality=88, optimize=True, progressive=True)
        print("bg  ", os.path.basename(out), im.size, os.path.getsize(out) // 1024, "KB")


# -------------------------------------------------------------- character art

def load_palettes():
    p = {}
    for kind, f in (("skin", "body/body_ulpc.json"),
                    ("hair", "hair/hair_ulpc.json"),
                    ("cloth", "cloth/cloth_ulpc.json")):
        d = json.load(open(os.path.join(PAL, f)))
        p[kind] = {k: [tuple(int(v[i:i + 2], 16) for i in (1, 3, 5)) + (255,) for v in ramp]
                   for k, ramp in d.items()}
    return p


PALETTES = None


def palettes():
    global PALETTES
    if PALETTES is None:
        PALETTES = load_palettes()
    return PALETTES


def frame(path):
    im = Image.open(os.path.join(LPC, path + ".png")).convert("RGBA")
    y = FRONT_ROW * FRAME
    return im.crop((0, y, FRAME, y + FRAME))


def auto_map(im, kind, palette):
    """Recolour a layer onto a palette ramp, keeping LPC's own shading."""
    ramp = palettes()[kind][palette]
    cols = [c for c in im.getcolors(4096) or []]
    used = [c[1] for c in cols if c[1][3] != 0]
    if not used:
        return {}
    def lum(c):
        return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]
    lo, hi = min(map(lum, used)), max(map(lum, used))
    span = max(hi - lo, 1.0)
    out = {}
    for c in used:
        t = (lum(c) - lo) / span
        idx = min(len(ramp) - 1, max(0, round(t * (len(ramp) - 1))))
        out[c] = ramp[idx]
    return out


def recolor(im, mapping):
    if not mapping:
        return im
    px = im.load()
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            p = px[x, y]
            if p[3]:
                px[x, y] = mapping.get(p, p)
    return im


def build_sprite(desc):
    canvas = Image.new("RGBA", (FRAME, FRAME), (0, 0, 0, 0))
    try:
        canvas.alpha_composite(frame("shadow/adult/idle"))
    except FileNotFoundError:
        pass
    for path, *rest in desc:
        pal = rest[0] if rest else None
        try:
            im = frame(path)
        except FileNotFoundError:
            print("  MISSING", path, file=sys.stderr)
            continue
        if pal:
            im = recolor(im, auto_map(im, *pal))
        canvas.alpha_composite(im)
    return canvas


def headshot(sprite, size=(256, 256)):
    """Crop the head/shoulders out of a 64x64 sprite for the side panel."""
    # The head occupies roughly rows 6..26, columns 20..44 in the LPC frame.
    head = sprite.crop((18, 4, 46, 32))
    head = head.resize(size, Image.NEAREST)
    return head


# ------------------------------------------------------------------ the cast

# Every character is a list of LPC layers, bottom to top. A second element
# recolours that layer along a palette ramp.
CAST = {
    "alexandria": [
        ("body/bodies/female/idle",),
        ("head/heads/human/female/idle", ("skin", "light")),
        ("hair/braid2/adult/bg/idle", ("hair", "chestnut")),
        ("torso/clothes/longsleeve/longsleeve2_buttoned/female/idle", ("cloth", "bluegray")),
        ("legs/skirts/plain/thin/idle", ("cloth", "charcoal")),
        ("feet/boots/basic/thin/idle", ("cloth", "walnut")),
        ("hair/braid2/adult/fg/idle", ("hair", "chestnut")),
    ],
    "elandi": [
        ("body/bodies/female/idle",),
        ("head/heads/human/female_elderly/idle", ("skin", "taupe")),
        ("hair/bangs_bun/adult/idle", ("hair", "gray")),
        ("torso/clothes/longsleeve/longsleeve2/female/idle", ("cloth", "maroon")),
        ("legs/skirts/plain/thin/idle", ("cloth", "black")),
        ("feet/boots/basic/thin/idle", ("cloth", "black")),
    ],
    "marta": [
        ("body/bodies/female/idle",),
        ("head/heads/human/female/idle", ("skin", "olive")),
        ("hair/bob/adult/idle", ("hair", "dark_brown")),
        ("torso/clothes/shortsleeve/shortsleeve/female/idle", ("cloth", "brown")),
        ("torso/aprons/overalls/female/idle", ("cloth", "tan")),
        ("legs/skirts/plain/thin/idle", ("cloth", "walnut")),
        ("feet/boots/basic/thin/idle", ("cloth", "leather")),
        ("hat/cloth/bandana/adult/idle", ("cloth", "rose")),
    ],
    "sister_ivo": [
        ("body/bodies/female/idle",),
        ("head/heads/human/female/idle", ("skin", "pale_green")),
        ("hair/long/adult/idle", ("hair", "platinum")),
        ("torso/clothes/longsleeve/longsleeve2/female/idle", ("cloth", "navy")),
        ("feet/shoes/basic/thin/idle", ("cloth", "black")),
        ("hat/magic/wizard/base/adult/idle", ("cloth", "blue")),
    ],
    "master_oren": [
        ("body/bodies/male/idle",),
        ("head/heads/human/male_elderly/idle", ("skin", "bronze")),
        ("hair/long/adult/idle", ("hair", "white")),
        ("beards/beard/medium/idle", ("hair", "white")),
        ("torso/clothes/longsleeve/longsleeve2/female/idle", ("cloth", "purple")),
        ("feet/shoes/basic/thin/idle",),
    ],
    "tamsin": [
        ("body/bodies/female/idle",),
        ("head/heads/human/female/idle", ("skin", "brown")),
        ("head/ears/elven/adult/idle", ("skin", "brown")),
        ("hair/curly_long/adult/idle", ("hair", "ash")),
        ("torso/clothes/longsleeve/longsleeve2_scoop/female/idle", ("cloth", "forest")),
        ("legs/skirts/plain/thin/idle", ("cloth", "forest")),
        ("feet/boots/basic/thin/idle",),
        ("hat/magic/wizard/base/adult/idle", ("cloth", "forest")),
        ("hat/magic/wizard/belt/adult/idle", ("cloth", "walnut")),
    ],
    "harrow": [
        ("body/bodies/muscular/idle",),
        ("head/heads/orc/male/idle", ("skin", "pale_green")),
        ("hair/balding/adult/idle", ("hair", "black")),
        ("torso/armour/leather/male/idle", ("cloth", "walnut")),
        ("legs/pants/thin/idle", ("cloth", "gray")),
        ("feet/boots/basic/thin/idle", ("cloth", "leather")),
    ],
    "seppa": [
        ("body/bodies/female/idle",),
        ("head/heads/orc/female/idle", ("skin", "green")),
        ("hair/bangs/adult/idle", ("hair", "raven")),
        ("torso/chainmail/female/idle", ("cloth", "gray")),
        ("legs/skirts/plain/thin/idle", ("cloth", "charcoal")),
        ("feet/boots/basic/thin/idle", ("cloth", "black")),
    ],
    "vashk": [
        ("body/bodies/muscular/idle",),
        ("head/heads/wolf/male/idle", ("skin", "fur_grey")),
        ("torso/armour/leather/male/idle", ("cloth", "walnut")),
        ("legs/pants/thin/idle", ("cloth", "brown")),
        ("feet/boots/basic/thin/idle", ("cloth", "leather")),
    ],
    "corin": [
        ("body/bodies/male/idle",),
        ("head/heads/human/male/idle", ("skin", "olive")),
        ("hair/curly_short/adult/idle", ("hair", "dark_brown")),
        ("legs/pants/thin/idle", ("cloth", "charcoal")),
        ("torso/clothes/longsleeve/longsleeve2/male/idle", ("cloth", "navy")),
        ("feet/boots/basic/thin/idle", ("cloth", "leather")),
        ("hat/cloth/leather_cap/adult/idle", ("cloth", "navy")),
    ],
}


def characters():
    os.makedirs(CH_OUT, exist_ok=True)
    os.makedirs(PORT_OUT, exist_ok=True)
    for name, desc in CAST.items():
        sprite = build_sprite(desc)
        big = sprite.resize((FRAME * SPRITE_SCALE, FRAME * SPRITE_SCALE), Image.NEAREST)
        big.save(os.path.join(CH_OUT, name + ".png"))
        head = headshot(sprite)
        head.save(os.path.join(PORT_OUT, name + ".png"))
        print("char", name, big.size)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "bg"):
        backgrounds()
    if what in ("all", "char"):
        characters()
