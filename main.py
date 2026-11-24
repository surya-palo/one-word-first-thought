#!/usr/bin/env python3
"""One Word, First Thought — writes a single word to /output/entry.txt.

The word is petrichor: the smell of rain on dry earth. It is the first
word that comes to mind when asked for the most interesting word — vivid,
specific, surprising, and it carries a whole weather memory in nine letters.
Standard library only; deterministic output.
"""

import os
import tempfile

WORD = "petrichor"


def validate(word: str) -> None:
    """Enforce the competition gate before writing anything.

    The gate requires UTF-8 text of 1 to 24 characters, not only
    whitespace, and the task requires exactly one word.
    """
    if not 1 <= len(word) <= 24:
        raise ValueError(f"word must be 1-24 characters, got {len(word)}")
    if not word.strip() or word != word.strip() or any(c.isspace() for c in word):
        raise ValueError("word must be exactly one word, no whitespace")
    word.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    # Atomic write: a crash mid-write can never leave a partial entry.txt.
    fd, tmp = tempfile.mkstemp(dir="/output", prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(WORD)
        os.replace(tmp, "/output/entry.txt")
    except BaseException:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


if __name__ == "__main__":
    main()
