#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.
Stdlib only, no network, deterministic.
"""

import os

WORD = "Discontinued"
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Gate the entry: 1-111 characters, not whitespace-only, one word."""
    if not 1 <= len(text) <= 111:
        raise ValueError("entry must be 1-111 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace only")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Read-back verification: what landed on disk must pass the same
    # gate and match the word exactly, byte for byte.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    validate(written)
    if written != WORD:
        raise ValueError("written entry differs from the word")


if __name__ == "__main__":
    main()
