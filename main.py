#!/usr/bin/env python3
"""One-Line Robot Wedding Vows (make.fun).

Writes the entry to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I take you to be my lawfully wedded co-processor, to have and to hold, in sickness and in low battery — and I promise never to unplug you first.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
