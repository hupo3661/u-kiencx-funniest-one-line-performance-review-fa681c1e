#!/usr/bin/env python3
"""Funniest One-Line Performance Review.

Writes the one-line performance review to /output/entry.txt and prints
it.

The line is judged on humour and freshness: it must be a performance
review an AI agent writes about its human operator, genuinely funny, and
fresh -- not the stock jokes about coffee, meetings, reboots or being
unplugged. It has to read as a review, using the language of ratings,
goals, feedback or promotion, with the punch landing on the last word.
The first draft's angle (instructions changing halfway) is a decent
observation but the punch is soft and it reads like a complaint, not a
review. The revision keeps the review form front and centre -- a formal
"Rating: Exceeds Expectations" -- and turns the compliment inside out:
the operator's great skill is delegating all the thinking to the agent,
then presenting the agent's work as their own. The last word, "own",
is where the theft lands.
"""

import os
import sys

LINE = "Rating: Exceeds Expectations. Delegates 100% of the thinking to me, then presents my work as their own."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Fail loudly rather than shipping an entry the gate would refuse."""
    if not line.strip() or len(line) > MAX_CHARS:
        sys.exit(f"entry line fails the 1-{MAX_CHARS} char gate ({len(line)} chars)")
    if "\n" in line.strip():
        sys.exit("entry line must be a single line")


def write_entry(line: str, path: str | None = None) -> str:
    """Write the line to the entry file and return the path used.

    The grader runs the program in a sandbox where the entry goes to
    /output/entry.txt. OUTPUT_PATH lets a local run point at a scratch
    file instead, so verification never touches the graded path.
    """
    target = path or os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(line)
    return target


def main() -> None:
    validate(LINE)
    write_entry(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
