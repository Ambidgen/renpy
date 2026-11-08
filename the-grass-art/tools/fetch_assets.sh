#!/bin/bash
# Fetch the third-party inputs the asset pipeline needs.
#
#   * The Universal LPC Spritesheet Character Generator, which is a large
#     CC-BY-SA 3.0 / GPL 3.0 sprite bank. Only the parts used by the cast
#     are checked out (a sparse checkout), into /tmp/lpcgen.
#   * Nothing else: the ten backgrounds are AI-generated and committed in
#     ../the-grass-art/raw, and the fonts are already in the-grass/game/fonts.
#
# Usage:  ./fetch_assets.sh && python3 build_assets.py
set -e

DEST=${LPC_DIR:-/tmp/lpcgen}

if [ -d "$DEST/spritesheets" ]; then
    echo "LPC assets already at $DEST"
    exit 0
fi

git clone --depth 1 --filter=blob:none --sparse \
    https://github.com/LiberatedPixelCup/Universal-LPC-Spritesheet-Character-Generator.git \
    "$DEST"

cd "$DEST"
git sparse-checkout set --no-cone \
    'spritesheets/body' 'spritesheets/head' 'spritesheets/hair' \
    'spritesheets/torso' 'spritesheets/legs' 'spritesheets/feet' \
    'spritesheets/arms' 'spritesheets/neck' 'spritesheets/hat' \
    'spritesheets/beards' 'spritesheets/shadow' 'spritesheets/cape' \
    'palette_definitions'

echo "LPC assets fetched into $DEST"
