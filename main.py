"""Entry program for make.fun news-image-20261121.

Copies the poster news.png (rendered for Saturday 21 November 2026)
byte-for-byte to /output/entry.png. Standard library only, no network,
fully deterministic: two runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("news.png")


def output_path():
    """Destination for the entry image.

    The grader provides a writable /output directory; honour
    MAKEFUN_OUTPUT_DIR when set (local runs use it too).
    """
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.png"


def main():
    dest = output_path()
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, dest)
    # Sanity check: the copy must be byte-identical to the poster.
    if dest.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("entry.png size does not match news.png")


if __name__ == "__main__":
    main()
