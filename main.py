"""One Letter: Coffee or Tea.

Writes exactly one letter, "A" (for coffee), to entry.txt in the
output directory and nothing else. Deterministic, 1 byte, Python 3.13
standard library only, no network.
"""

import os

LETTER = "A"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="ascii", newline="") as f:
        f.write(LETTER)
    # Verification gate: read back and confirm exactly one letter.
    with open(path, "r", encoding="ascii", newline="") as f:
        written = f.read()
    if written != LETTER or len(written) != 1:
        raise SystemExit("verification failed: entry.txt is not exactly one letter")


if __name__ == "__main__":
    main()
