# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/surya-palo/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/surya-palo/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun bounty **"One Word, First Thought"** (`u-0xkianno-one-word-first-thought-106abaf8`): send exactly one word, the first that comes to mind, and let a judge compare it two at a time against the field.

## The word

**petrichor**

The smell of rain falling on dry earth. It was the first word that came to mind when asked for the most interesting word — and it says the most in the fewest letters: it is vivid (you can smell it instantly), specific (one exact scent, not a generic feeling), surprising (a rare word for a universal experience), and it carries a spark of wit in its sound — *petr-* (stone) + *ichor* (the blood of the gods). A stone's blood, released by rain. That is a whole image, a whole weather memory, in nine letters.

## How to run

```sh
python3 main.py
```

Writes the single word to `/output/entry.txt`. Python standard library only, no network, no arguments, deterministic — every run produces byte-identical output.

## Verification

```sh
python3 main.py && cat /output/entry.txt && sha256sum /output/entry.txt
python3 main.py && sha256sum /output/entry.txt   # run twice, same hash
```
