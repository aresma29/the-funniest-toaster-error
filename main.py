#!/usr/bin/env python3
"""Print the toaster error message entry."""
import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().strip()
    # Write exactly the line plus one newline; no extra output.
    sys.stdout.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
