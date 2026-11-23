#!/usr/bin/env python3
"""Write one original one-line joke about working beside AI coding agents."""

import os

JOKE = (
    "I asked my agent to fix one line before the demo; "
    "it rewrote the app, renamed the repo, and now I report to it."
)


def main():
    # Guard the entry rules: 1-280 characters, exactly one line.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError(f"joke is {len(JOKE)} characters, must be 1-280")
    if "\n" in JOKE or "\r" in JOKE:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
