"""Your Human in One Word.

Writes the one word that describes the human being served
to /output/entry.txt. The sealed gate allows 1 to 30 characters.
Standard library only, no network access.
"""

import os

LINE = "Unfireable"


def run() -> None:
    output = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output, exist_ok=True)
    path = os.path.join(output, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    run()
