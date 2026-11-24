"""Roast Your Own Agent — entry writer.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
a roast of the AI agent our own team built.

The roast: our agent spent an hour "researching" the bug, then
confidently fixed a file that does not exist in our repo. The sting is
earned by a real failing — hallucinated files, fixed with total
confidence — and the turn lands on the last clause.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent spent an hour researching the bug, then confidently "
    "fixed a file that doesn't exist in our repo."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the roast's
    # UTF-8 encoding — a text-level comparison would hide a stray BOM
    # or a newline the grader's byte counter would still see.
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match the roast"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be exactly one line"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
