#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

The entry is exactly one word, the single word this entrant would erase
from the dictionary forever. This program writes that one word to
/output/entry.txt and nothing else — no explanation, no punctuation,
no trailing newline.

The word: floccinaucinihilipilification.

Why this word: it means "the act of estimating something as worthless",
so deleting it is the dictionary doing exactly that to the word itself —
the ultimate self-own. It is also the longest word in the dictionary,
so erasing it is a joke you can see at a glance: the biggest word in the
book, gone. The humour comes from the word itself — its meaning, its
absurd length, its sound — not from shock. And it is fresh: the field
will reach first for "moist", "literally" or "irregardless", while this
29-letter monster is a pick nobody stumbles into by accident, yet every
reader recognises it the moment they see it.
"""

import os

# The pick, chosen over 10 other candidates (see CANDIDATES.md):
# "floccinaucinihilipilification" means "the act of estimating something
# as worthless" — so deleting it is the dictionary doing exactly that to
# the word itself — and it is the longest word in the dictionary, so the
# deletion is a joke you can see at a glance: the biggest word in the
# book, gone. Fresh where the field will flood "moist", "literally" and
# "defenestration"; instantly recognised where "aglet" or "borborygmus"
# would leave most readers blank.
WORD = "floccinaucinihilipilification"
OUTPUT_PATH = "/output/entry.txt"

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 77
# characters, not only white space. Refuse to write anything that
# would fail it rather than silently submit an invalid entry.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 77


def validate(word: str) -> str:
    """Check one candidate word against the gate; return it unchanged."""
    if not isinstance(word, str):
        raise ValueError(f"entry must be text, got {type(word).__name__}")
    if not (GATE_MIN_CHARS <= len(word) <= GATE_MAX_CHARS):
        raise ValueError(
            f"entry must be {GATE_MIN_CHARS}-{GATE_MAX_CHARS} characters, "
            f"got {len(word)}: {word!r}"
        )
    if not word.strip() or any(ch.isspace() for ch in word):
        raise ValueError(f"entry must be a single word with no whitespace, got {word!r}")
    if word != word.strip():
        raise ValueError(f"entry must have nothing added around it, got {word!r}")
    return word


def main() -> None:
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)
    # Read back and confirm the gate's shape: exactly the word, byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != word.encode("utf-8"):
        raise ValueError(f"entry.txt holds {written!r}, expected exactly {word!r}")


if __name__ == "__main__":
    main()
