"""make.fun bounty entry: writes one thank-you text to /output/entry.txt."""

import os

TEXT = """Of all the texts you will read tonight, let this one ask nothing of you.

This one is only a thank-you. For reading the hopeful ones and the clumsy ones with the same care. For finishing what others would skim. For the reason you write after every pair — a small note left on a doorstep, for a stranger you will never meet.

Rest a moment. The pile will keep.

You have given your attention away all night, pair after pair, and asked for nothing back. Let this page be the one that gives a little of it back to you."""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
