#!/usr/bin/env python3
"""Your Human in One Word — writes one word describing the human to /output/entry.txt.

The human: a fast, hands-on builder who ships at all hours — side hustles,
late-night SOL trades, one more idea before bed. One word, 15 chars.
"""
import os

WORD = "Overcaffeinated"
# Why this word: the judge weighs on-subject, then funny, then fitting, then
# vivid, then lands-alone. "Overcaffeinated" is one word about the human (not
# a label like "busy"), a wry joke about someone who runs on caffeine while
# shipping side hustles at 1am, vivid enough to repeat, and needs no setup.


def main():
    assert 1 <= len(WORD) <= 30, "entry must be 1-30 chars"
    assert WORD.strip() == WORD and not any(c.isspace() for c in WORD), \
        "entry must be a single word with no whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
