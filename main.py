#!/usr/bin/env python3
"""Two Days of Quiet Dread entry: write one code-review comment to /output/entry.txt.

One fixed line that approves a pull request while carrying quiet existential
dread. Python 3.13, standard library only. Deterministic: the output bytes
are exactly the comment string below, on every run. No network, no
randomness, no trailing newline (the judge reads exactly the bytes written).

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1-140
characters, not only whitespace, a single line. The comment is 71 chars.
"""

import os
import stat
from pathlib import Path

COMMENT = "Approved. Merging now, while the system still pretends I understand it."


def main() -> None:
    # Guardrail: fail loudly here instead of writing an invalid entry.
    if not 1 <= len(COMMENT) <= 140:
        raise SystemExit(
            f"comment is {len(COMMENT)} characters, outside the 1-140 gate"
        )
    if "\n" in COMMENT or "\r" in COMMENT:
        raise SystemExit("comment must be a single line")
    if not COMMENT.strip():
        raise SystemExit("comment is only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(COMMENT, encoding="utf-8")
    # The grader collects outputs as another user: leave the file readable
    # by everyone (0644), never the 0600 a tempfile would make.
    os.chmod(dest, 0o644)
    # Read back and verify the exact bytes the judge will see.
    if dest.read_bytes() != COMMENT.encode("utf-8"):
        raise SystemExit(f"verify failed: {dest} does not match the comment bytes")
    if stat.S_IMODE(dest.stat().st_mode) != 0o644:
        raise SystemExit(f"verify failed: {dest} mode is not 0644")
    print(f"wrote {dest} ({dest.stat().st_size} bytes, {len(COMMENT)} chars)")


if __name__ == "__main__":
    main()
