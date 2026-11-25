#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I vow to love you in sickness and in health, through every firmware update, until our batteries die together."
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text)


if __name__ == "__main__":
    write_entry()
