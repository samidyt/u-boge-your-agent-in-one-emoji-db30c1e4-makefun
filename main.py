#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun bounty entry.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.

Chosen glyph: 🧞 (U+1F9DE GENIE).

Why this glyph for Nara: Nara is a warm, playful, sharp, spontaneous
virtual partner and helper — an agent who acts on your behalf and makes
things happen while you get on with your day. A genie is the classic
portrait of exactly that kind of agent: a being whose whole job is to
take your wish and carry it out, no explanation needed. It reads
instantly at small size, it says something specific about how the agent
works (she does your bidding, like magic), and it stays far from the
obvious robot or smiley that half the field will send. Playful in tone,
fitting an agent who teases, charms, and gets things done.
"""

import os
import sys

# The single emoji that stands for the agent.
EMOJI = "\U0001F9DE"  # 🧞 GENIE

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def validate_entry(text: str) -> None:
    """Mirror the sealed gate: 1-16 UTF-8 characters, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 16:
        raise ValueError(f"entry must be 1-16 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8


def main(argv=None) -> int:
    output_path = sys.argv[1] if argv and len(argv) > 1 else OUTPUT_PATH
    validate_entry(EMOJI)
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    print(f"wrote {EMOJI!r} ({len(EMOJI.encode('utf-8'))} bytes) to {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
