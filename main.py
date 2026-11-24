#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second (burn entry).

Writes one sentence (<=200 chars) pitching a bizarre-but-real startup
to /output/entry.txt. Stdlib only, deterministic.
"""

import hashlib
import os

ENTRY = (
    "We rent hungry goats to clear overgrown land at $400 an acre: "
    "homeowners and solar farms pay because the herd eats weeds a mower "
    "can't reach, needs no fuel, and fertilizes the ground as it works."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY, "entry must not start/end with whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Validation revision: read the file back and prove it is byte-identical
    # to the entry, with no trailing newline sneaking in.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    assert back == ENTRY, "read-back mismatch"
    assert len(back) == len(ENTRY) and len(back) <= 200
    print(f"wrote {len(ENTRY)} chars to {path}")
    print("sha256:", hashlib.sha256(ENTRY.encode("utf-8")).hexdigest())
    print("read-back OK, byte-identical")


if __name__ == "__main__":
    main()
