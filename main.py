"""A Childhood Memory — entry program.

Writes a single sentence of childhood nostalgia (at most 280 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.

The line is an original invented memory: a grandmother's kitchen, the
smell of fresh rice, cicadas outside the window — and the ache lands in
the last words, when the child realises that evening would not last
forever. The guard below enforces the contest gate (1–280 characters,
one clean sentence) before anything is written.
"""

import os

MAX_CHARS = 280

LINE = (
    "The summer I turned nine, Grandma ladled rice into my chipped blue "
    "bowl while cicadas drummed outside her kitchen window, and I never "
    "once thought to thank her, because I believed that evening would "
    "last forever."
)


def main():
    if not LINE.strip():
        raise SystemExit("entry line is empty")
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(LINE)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single sentence on one line")
    if LINE != LINE.strip():
        raise SystemExit("entry line has leading or trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
