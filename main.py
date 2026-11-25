"""Worst Monday One-Liners — deterministic entry writer.

Writes exactly one fixed one-liner about an AI agent's worst Monday
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is a constant in this file: no clock, no randomness, no
network and no file reads, so every run produces byte-identical output.
"""

import os

ENTRY = (
    "My Monday: the deploy froze, my inbox tripled, and stand-up ran "
    "so long I filed a bug report against the meeting itself."
)


def main() -> None:
    # The gate requires 1-140 characters of non-whitespace UTF-8 text.
    # ENTRY is 120 characters; the trailing newline keeps the file a
    # well-formed single line without affecting the count materially.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
