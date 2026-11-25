#!/usr/bin/env python3
"""news-image-20261125 entrypoint (Python 3.13, standard library only).

The poster is pre-rendered and bundled as entry.png beside this file;
this program copies it to the grader's output directory.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out, "entry.png")
    shutil.copy(src, dst)
    if os.path.getsize(dst) == 0:
        raise SystemExit("empty entry.png")
    return 0


if __name__ == "__main__":
    sys.exit(main())
