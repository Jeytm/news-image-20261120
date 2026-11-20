#!/usr/bin/env python3
"""Entry point: copy entry.png to the output directory (stdlib only).

Validates the image first: it must exist and start with the PNG magic
bytes, so a missing or corrupt entry fails loudly instead of shipping
a bad file to the gate.
"""
import os
import shutil
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("entry.png missing next to main.py", file=sys.stderr)
        return 1
    with open(src, "rb") as f:
        head = f.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    print("copied", src, "->", out_dir, os.path.getsize(src), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
