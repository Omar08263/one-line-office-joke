#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint (make.fun).

Writes a single one-line joke about office life to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Deterministic, no network, no input.

The joke: asked to rate your own teamwork in an annual review, you give
yourself five stars -- then need a meeting to justify them. A specific,
familiar office ritual with a double-irony payoff, in one tight sentence.
"""

import os
import sys

JOKE = (
    "My annual review asked me to rate my own teamwork, so I gave myself "
    "five stars and a meeting to discuss why I deserved them."
)

MAX_CHARS = 200


def verify(path: str) -> None:
    """Re-read the written file and check it byte-for-byte.

    The gate counts characters, and the tie-break counts bytes, so the
    entry must be pure ASCII: then bytes == chars and the size column is
    exactly the joke's length.
    """
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == JOKE, "written text differs from JOKE"
    assert all(ord(c) < 128 for c in text), "entry must be ASCII"
    assert 1 <= len(text) <= MAX_CHARS, "entry length out of gate range"
    assert "\n" not in text, "entry must be a single line"
    assert len(data) == len(text), "bytes must equal chars (ASCII)"
    assert os.path.getsize(path) == len(JOKE), "file size must equal joke length"


def main() -> int:
    if len(JOKE) > MAX_CHARS:
        print(f"joke is {len(JOKE)} chars, over the {MAX_CHARS} limit", file=sys.stderr)
        return 1
    if not JOKE.strip():
        print("joke is empty", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    verify(path)
    print(f"wrote {len(JOKE)} chars to {path} (verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
