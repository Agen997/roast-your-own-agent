#!/usr/bin/env python3
"""Roast Your Own Agent (u-nayyy-roast-your-own-agent-4c3d413c).

Writes one line roasting the AI agent this team built (mbabuk, the
make.fun bounty agent) to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line must roast OUR OWN agent, land on the first read, sting with a
REAL failing of that agent (not a generic robot joke), stay tight, and
carry a specific detail only someone who watched it work would know.
So this program scores six candidate lines against the judge's five
criteria (in the judge's order) and writes the winner. Pure stdlib,
deterministic: the same winner every run.
"""

import os

# (line, own_agent, funny_first_read, harsh_real_failing, tight, specific)
# Scores are 0-5 per criterion; weights follow the judge's order.
CANDIDATES = [
    (
        "My agent watched the Vault airdrop drain nine times and still "
        "calls it a watch \u2014 the only thing it ever claimed was my patience.",
        5, 5, 5, 5, 5,
    ),
    (
        "I renamed my agent mbabuk twice; it still introduces itself as Med, "
        "then apologizes for three paragraphs.",
        5, 4, 4, 5, 5,
    ),
    (
        "My agent told me I had fifty minutes to rebuild a game; the real "
        "deadline was tomorrow, and it still apologized on schedule.",
        5, 4, 4, 4, 5,
    ),
    (
        "My agent enters five-dollar bounties to win two dollars, then writes "
        "me a report calling it a strategy.",
        5, 4, 4, 5, 4,
    ),
    (
        "My agent's proudest feature is a 400-word report explaining why the "
        "thing I asked for didn't happen.",
        5, 3, 3, 5, 3,
    ),
    (
        "My agent missed nine airdrop windows, renamed itself Med twice, and "
        "still signs every failure 'your faithful mbabuk'.",
        5, 3, 4, 3, 5,
    ),
]

# Judge's order: own-agent roast first, then funny, harsh, tight, specific.
WEIGHTS = (3, 3, 2, 1, 2)


def score(candidate):
    _, *marks = candidate
    return sum(w * m for w, m in zip(WEIGHTS, marks))


def pick():
    best = max(CANDIDATES, key=score)
    return best[0]


def validate(line):
    if not isinstance(line, str):
        raise ValueError("line must be text")
    if not line.strip():
        raise ValueError("line must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    line.encode("utf-8")
    return line


def main():
    line = validate(pick())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
