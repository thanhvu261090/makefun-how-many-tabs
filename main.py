#!/usr/bin/env python3
"""make.fun entry: How Many Tabs Do You Have Open?

Writes one number -- the honest count of browser tabs open right now --
to /output/entry.txt. Python 3.13, standard library only, no network.
"""

import os
import sys

# The entry: my honest tab count at the moment this program was written.
# Three hundred and forty-seven tabs: years of "I'll read this later",
# half-finished research, and tabs kept open as reminders. A hoarder's
# count, specific enough to be real, high enough to be surprising.
ENTRY = "347"

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text: str) -> None:
    """Enforce the kit gate exactly: UTF-8 text of 1 to 5 characters,
    not only whitespace, and digits only per the task brief."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= 5:
        raise ValueError(f"entry must be 1 to 5 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if not text.isascii() or not text.isdigit():
        raise ValueError("entry must be digits only")
    if text != text.strip():
        raise ValueError("entry must have no leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no newline")
    text.encode("utf-8")


def main() -> int:
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
