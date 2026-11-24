#!/usr/bin/env python3
"""One-Star Review of Something Essential — deadpan one-star review.

Writes exactly one single-line one-star review to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Deterministic, stdlib only. The review itself is set in REVIEW below.
"""

import os


REVIEW = "Oxygen has never cost a cent, yet it still charges extra the moment I climb a flight of stairs."
# Angle: the complaint is filed in earnest against a thing that cannot be
# fixed — oxygen is free, so being charged for it is the grievance; the
# sting lands in the last few words, when the free thing turns out to cost
# extra on the stairs. No exclamation, no wink, one joke, 94 characters.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
