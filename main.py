#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.
Stdlib only, no network, deterministic.
"""

import os

WORD = "Discontinued"
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    assert 1 <= len(WORD) <= 111, "word must be 1-111 characters"
    assert WORD.strip(), "word must not be whitespace only"
    assert " " not in WORD, "entry must be exactly one word"
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "written entry differs from the word"
    assert 1 <= len(written) <= 111 and written.strip()


if __name__ == "__main__":
    main()
