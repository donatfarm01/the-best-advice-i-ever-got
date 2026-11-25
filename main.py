#!/usr/bin/env python3
"""The Best Advice I Ever Got -- make.fun entry.

Writes one sentence (1-200 characters) about the best advice ever
received to /output/entry.txt, where the sealed gate scorer reads it.
"""

import os

ENTRY = "My father made me change a tyre in the rain and said, 'Nobody is coming \u2014 learn to like that.'"

OUTPUT_PATH = "/output/entry.txt"


def main():
    text = ENTRY.strip()
    # Self-gate, mirroring the sealed scorer: 1-200 chars, one sentence,
    # not only white space. Fail loudly instead of writing a bad entry.
    if not text:
        raise SystemExit("entry is empty")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    terminators = sum(text.count(mark) for mark in ".!?")
    if terminators != 1:
        raise SystemExit(f"entry has {terminators} sentence terminators, must be 1")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
