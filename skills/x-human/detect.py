#!/usr/bin/env python3
"""Scan text for AI-writing tells. Stdlib only.

Usage:
    python detect.py <file>
    cat file | python detect.py

Prints each tell found, how many times, and the total. Exits 1 if any tell is
found, 0 if clean, so it can gate a pipeline.
"""

import json
import os
import re
import sys


def load_slop():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "slop.json"), encoding="utf-8") as fh:
        return json.load(fh)


def read_text(argv):
    if len(argv) > 1:
        with open(argv[1], encoding="utf-8") as fh:
            return fh.read()
    return sys.stdin.read()


def count_term(low, needle, key):
    if key == "punctuation_tells":
        return low.count(needle)
    return len(re.findall(r"\b" + re.escape(needle) + r"\b", low))


def find(text, slop):
    low = text.lower()
    hits = []
    for key in ("words", "phrases", "openers", "closers", "punctuation_tells"):
        for term in slop.get(key, []):
            n = count_term(low, term.lower(), key)
            if n:
                hits.append((key, term, n))
    return hits


def structural(text):
    """Sentence-level tells the word list cannot catch."""
    flags = []
    for pat, label in (
        (
            r"\b(is ?n[o']t|not)\s+(just|only|merely)\b.{0,80}\b(but|it'?s|its|rather)\b",
            "not-X-but-Y contrast",
        ),
        (
            r"\b(stands? as a|serves? as|a testament to|plays? a (key|vital|pivotal) role)\b",
            "inflated significance",
        ),
        (
            r"\b(let that sink in|read that again|that'?s the real win)\b",
            "one-line closer",
        ),
    ):
        if re.search(pat, text, re.I):
            flags.append(label)
    if re.search(
        r"\b(nice|good|great|smart|big)\b[^.\n]{0,20}\b(win|move|call)\b", text, re.I
    ):
        flags.append("vague praise closer")
    for line in text.splitlines():
        s = line.strip()
        if s and len(s) < 40 and s.endswith(".") and s.count(" ") < 6:
            flags.append('short standalone line: "%s"' % s)
    return flags


def main():
    slop = load_slop()
    text = read_text(sys.argv)
    hits = find(text, slop)
    print("=== word and phrase tells ===")
    total = 0
    for key, term, n in sorted(hits, key=lambda x: (-x[2], x[1])):
        print("  %-18s %-38s x%d" % (key, term, n))
        total += n
    if not hits:
        print("  (none)")
    flags = structural(text)
    print("=== structural tells ===")
    if flags:
        for f in flags:
            print("  " + f)
    else:
        print("  (none)")
    print(
        "=== total word/phrase hits: %d, structural flags: %d ===" % (total, len(flags))
    )
    return 1 if (total or flags) else 0


if __name__ == "__main__":
    sys.exit(main())
