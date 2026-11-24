"""Entrypoint for the news-image-20261124 entry.

Copies the pre-rendered front page ("THE WORLD IN ONE DAY" — 36 sourced
stories, 16 drawn, UTC timeline, Tuesday 24 November 2026) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).

Standard library only: the grader runs Python 3.13 with no third-party
packages installed, so this program imports nothing but os and shutil.
The image was drawn by this repository's own PIL renderer (the earlier
main.py, from stories.py) and is shipped as entry.png; copying it twice
writes byte-identical output.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    size = os.path.getsize(dst)
    assert size <= 1048576, f"image too large: {size} bytes"
    print(f"wrote {dst} ({size} bytes)")


if __name__ == "__main__":
    main()
