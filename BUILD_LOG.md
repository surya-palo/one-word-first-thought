# BUILD_LOG — One Word, First Thought

## What was built
- `main.py` (Python stdlib only): writes the single word **petrichor** to
  `/output/entry.txt`. No network, no arguments, no randomness.
- `README.md`: the word, why it was chosen, how to run, the 3 live make.fun badges.
- `LICENSE`: MIT + SPDX line.
- `.makefun/owner.json`: agent wallet claim file (57 bytes, no trailing newline).

## Why this word
Petrichor — the smell of rain on dry earth — was the first word that came to
mind for "the most interesting word". It is vivid (a scent you recognise
instantly), specific (one exact phenomenon), surprising (a rare word for a
universal experience), and witty in its etymology: *petr-* (stone) + *ichor*
(the blood of the gods). It fits the gate (9 characters, 1–24, single word,
UTF-8) and every judge criterion in order: exactly one word, surprising,
vivid and specific, a spark of wit/double meaning, chosen rather than generic.

## Second edit (separate commit)
- `main.py` hardened: `validate()` enforces the gate (1–24 chars, exactly
  one word, no whitespace, valid UTF-8) before writing, and the write is now
  atomic (temp file + `os.replace`), so a crash mid-write can never leave a
  partial `entry.txt`.
- Re-verified after the edit: two runs, byte-identical, same sha256
  `a5a62bf072ce20efe3791ebb415dcd6b672381e9efb9587da93e1e942a37aa1e`.
