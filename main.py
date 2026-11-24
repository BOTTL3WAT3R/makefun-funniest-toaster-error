#!/usr/bin/env python3
"""The Funniest Toaster Error Message - a make.fun entry.

Writes one line to /output/entry.txt: the error message a kitchen
toaster shows its owner when something goes wrong.
"""

import os

ENTRY = "CRUMB TRAY FULL. So is my patience. Empty one of us."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
