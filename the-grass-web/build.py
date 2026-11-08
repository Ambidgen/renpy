#!/usr/bin/env python3
"""Build the browser-playable version of The Grass.

The Ren'Py web build that ships with Ren'Py is produced by a full native
SDK. This project cannot use that pipeline, so instead we assemble the
deployable directly, which is what the SDK does under the hood:

  * runtime/       the Ren'Py 8.5.3 engine as compiled for WebAssembly
                   (renpy.wasm, renpy.js, renpy.data, the shell html)
  * runtime/engine-base.zip
                   the stock engine zip, which contains the engine's own
                   Python bytecode plus renpy/common
  * ../the-grass/game/
                   the game itself: .rpy sources, images, fonts

The output in dist/ is a complete static site. Ren'Py compiles the .rpy
sources in the browser on first load and caches the result in IndexedDB.

Usage:
    python3 build.py            # build into dist/
    python3 build.py --serve    # build and serve on 0.0.0.0:8000
"""
import argparse
import http.server
import os
import shutil
import socketserver
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
GAME = os.path.join(REPO, "the-grass", "game")
RUNTIME = os.path.join(HERE, "runtime")
DIST = os.path.join(HERE, "dist")

ENGINE_BASE = os.path.join(RUNTIME, "engine-base.zip")

# Files that belong to the engine, not to the game. The game's own files are
# added from the-grass/game below.
GAME_DIR_PREFIXES = ("game/",)
ENGINE_ROOTS = ("renpy/", "main.py", "progressive_download.txt")

RUNTIME_FILES = [
    "index.html",
    "renpy-pre.js",
    "renpy.js",
    "renpy.wasm",
    "renpy.data",
    "manifest.json",
    "service-worker.js",
]


def build_game_zip(dest):
    """The zip the browser unzips into its virtual filesystem."""
    if not os.path.exists(ENGINE_BASE):
        sys.exit("missing runtime/engine-base.zip")

    n = 0
    with zipfile.ZipFile(ENGINE_BASE) as src, \
            zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as out:

        for info in src.infolist():
            name = info.filename
            if name.startswith(GAME_DIR_PREFIXES):
                continue                       # drop the stock demo game
            if name in ("wavedash.toml", "README.md", "example-renpy.py"):
                continue
            data = src.read(name)
            out.writestr(info, data)
            n += 1

        # the game itself
        for root, dirs, files in os.walk(GAME):
            dirs[:] = [d for d in dirs if d not in ("cache", "saves", "__pycache__")]
            for f in sorted(files):
                if f.endswith((".rpyc", ".pyo", ".pyc")):
                    continue
                path = os.path.join(root, f)
                rel = os.path.relpath(path, GAME).replace(os.sep, "/")
                out.write(path, "game/" + rel)
                n += 1

    return n, os.path.getsize(dest)


def build():
    if os.path.exists(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST)

    for f in RUNTIME_FILES:
        src = os.path.join(RUNTIME, f)
        if not os.path.exists(src):
            sys.exit("missing runtime file: " + f)
        shutil.copy2(src, os.path.join(DIST, f))

    n, size = build_game_zip(os.path.join(DIST, "game.zip"))

    # The shell references these; ship a fallback presplash if we have one.
    presplash = os.path.join(RUNTIME, "web-presplash.jpg")
    if os.path.exists(presplash):
        shutil.copy2(presplash, os.path.join(DIST, "web-presplash.jpg"))

    total = sum(os.path.getsize(os.path.join(DIST, f))
                for f in os.listdir(DIST) if os.path.isfile(os.path.join(DIST, f)))

    print("game.zip: %d files, %.1f MB" % (n, size / 1e6))
    print("dist:     %.1f MB total" % (total / 1e6))
    return 0


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIST, **kw)

    def end_headers(self):
        # The engine keeps its saves in IndexedDB; a plain static host is fine,
        # but COOP/COEP keeps the door open for threaded builds.
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


def serve(port=8000):
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
        print("serving dist/ on http://0.0.0.0:%d" % port)
        httpd.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    build()
    if args.serve:
        serve(args.port)
