#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes one line — a joke about office life, under 200 characters — to
/output/entry.txt. Pure Python standard library, no network, no input
files: the line is the entry.
"""

import os

LINE = (
    "I told the printer it was out of toner, so it printed a 40-page "
    "report explaining why it can't print."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 199, f"entry is {len(text)} chars, must be 1-199"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the line we meant to enter, single line included.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt on disk differs from the entry"
    print(written)
    print(f"({len(text)} characters, one line)")


if __name__ == "__main__":
    main()
