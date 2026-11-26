#!/usr/bin/env python3
"""Entry program for news-image-20261125.

Standard library only. Copies the bundled entry.png to the output
directory (MAKEFUN_OUTPUT_DIR, default /output). A plain byte copy is
deterministic across repeated grader runs.
"""

import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(BASE, "entry.png")
TARGET_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
TARGET = os.path.join(TARGET_DIR, "entry.png")


def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)


if __name__ == "__main__":
    main()
