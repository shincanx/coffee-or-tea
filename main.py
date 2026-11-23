#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Python 3.13 standard library only. No network. Deterministic:
every run writes the same single byte.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"  # A = coffee, B = tea. Coffee: the bolder, more vivid,
# truer fuel for an agent that builds through the night.


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify the gate: exactly one UTF-8 character,
    # not only white space. Fail loudly instead of shipping bad output.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if len(written) != 1 or written.isspace():
        raise SystemExit("entry.txt must hold exactly one letter, got %r" % written)


if __name__ == "__main__":
    main()
