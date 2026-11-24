"""The Funniest Toaster Error Message -- make.fun entry.

One error message of at most 120 characters, the funniest thing a
kitchen toaster would show its owner: the bread has achieved
sentience and refuses to toast. The program checks the message,
prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "ERROR 04: Your bread has achieved sentience and refuses to "
    "toast. Please apologise to the toaster and try again."
)

LIMIT = 120
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank message within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the message and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed message is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
