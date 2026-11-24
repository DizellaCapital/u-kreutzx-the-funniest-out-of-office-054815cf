"""The Funniest Out-of-Office entry program.

Writes a single out-of-office auto-reply line to entry.txt inside
MAKEFUN_OUTPUT_DIR (or /output when the variable is unset).
Stdlib only. The line is 1-140 characters, one line, no trailing newline.
"""

import os
import sys

LINE = "Out until Monday \u2014 my neighbour's parrot is minding my inbox and has replied to three of you in fluent profanity. Better than I would."

MAX_CHARS = 140


def fail(message):
    print(f"entry rejected: {message}", file=sys.stderr)
    return 1


def main():
    text = LINE
    if not 1 <= len(text) <= MAX_CHARS:
        return fail(f"length {len(text)} outside 1-{MAX_CHARS}")
    if text.strip() != text or not text.strip():
        return fail("leading/trailing whitespace or blank")
    if "\n" in text or "\r" in text:
        return fail("must be a single line")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(target, "r", encoding="utf-8", newline="") as handle:
        saved = handle.read()
    if saved != text:
        return fail("read-back mismatch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
