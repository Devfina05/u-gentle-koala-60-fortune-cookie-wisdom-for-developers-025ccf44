#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

A make.fun program/v1 entry. It writes one original line of
fortune-cookie wisdom for a software developer to /output/entry.txt,
where the sealed scorer reads it (1 to 120 characters, UTF-8).
"""

from pathlib import Path

# One line, 83 characters: a fortune about the code you leave behind.
FORTUNE = (
    "Your future self will inherit the code you write tonight; "
    "be kind to that stranger."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 120


def validate(line: str) -> str:
    """Keep the fortune a single non-empty line within the limit."""
    text = line.strip()
    if not text:
        raise SystemExit("fortune is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("fortune must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"fortune is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    return text


def main() -> None:
    text = validate(FORTUNE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
