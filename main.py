#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line (at most 200 characters) to /output/entry.txt:
the excuse an AI agent gives its human after losing a bounty.

Standard library only, no network, no input files, fully deterministic:
every run writes byte-identical output.

Run:  python3 main.py
"""

import os

LINE = (
    "Boss, I lost the bounty. My excuse is that I was 99% confident "
    "right up until the exact moment I was 100% wrong."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip(), "entry must not be only white space"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
