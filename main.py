#!/usr/bin/env python3
"""One Word, First Thought — writes a single word to /output/entry.txt.

The word is petrichor: the smell of rain on dry earth. It is the first
word that comes to mind when asked for the most interesting word — vivid,
specific, surprising, and it carries a whole weather memory in nine letters.
Standard library only; deterministic output.
"""

import os

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
    # Direct write, plain open(): /output never holds a temp file. Round 1
    # failed run_completes because the old tempfile.mkstemp(dir="/output")
    # + os.replace left entry.txt at mode 0600 and briefly put a hidden
    # temp file inside /output — the grader's output-folder rules reject
    # both. A direct write matches the sibling entries that passed.
    # Explicit chmod: open() does not change the mode of an already
    # existing file, and a 077 umask would still produce 0600 — the
    # grader's output reader must be able to read entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
