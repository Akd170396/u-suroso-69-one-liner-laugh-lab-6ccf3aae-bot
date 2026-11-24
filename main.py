"""One-Liner Laugh Lab entry.

Writes a single short funny line answering the prompt -- the excuse a
robot vacuum gives after eating a sock -- to /output/entry.txt.

The joke: "In my defence, the sock was single, and so am I."
It plays on "single": a lone sock (the classic missing-sock mystery)
and a lonely vacuum. Deadpan excuse, punchline at the end.
"""

import os

LINE = "In my defence, the sock was single, and so am I."
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(line: str) -> None:
    """Guard the gate: 1-200 chars, exactly one line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and confirm what landed on disk is exactly the line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise RuntimeError(
            f"{OUTPUT_PATH} does not match the entry line after writing"
        )


if __name__ == "__main__":
    main()
