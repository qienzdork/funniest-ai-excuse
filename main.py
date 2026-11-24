"""The Funniest AI Excuse.

Writes one line -- the funniest excuse an AI agent gives after
failing a task -- to /output/entry.txt.
"""

import os

LINE = (
    "I escalated the task to my supervisor. "
    "My supervisor is also me. "
    "We agreed to blame the Wi-Fi."
)


def write_entry(path):
    """Write the excuse as exactly one line, no trailing newline."""
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
