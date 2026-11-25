"""Out-of-office reply, served by the world's least reliable intern.

The reply itself lives in entry.txt, one line, no decoration. This module
only loads it, tidies the edges, and prints it verbatim.
"""

import sys
from pathlib import Path

ENTRY_FILE = Path(__file__).resolve().with_name("entry.txt")


def read_reply() -> str:
    """Return the out-of-office line, stripped of surrounding whitespace."""
    return ENTRY_FILE.read_text(encoding="utf-8").strip()


def main(argv: list[str] | None = None) -> int:
    _ = argv  # no flags; the reply is the whole program
    sys.stdout.write(read_reply() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
