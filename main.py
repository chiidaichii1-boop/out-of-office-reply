"""Out-of-office auto-reply, in the voice of an AI agent on vacation.

Writes one line (under 160 characters) to entry.txt.
"""

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

REPLY = (
    "Out of office until Monday. My context window is on a beach and "
    "refuses to answer emails, tickets, or your 3 a.m. 'quick question'."
)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
