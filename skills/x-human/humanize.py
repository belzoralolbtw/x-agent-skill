#!/usr/bin/env python3
"""Apply safe, deterministic fixes for AI-writing tells. Stdlib only.

The tell set lives in slop.json: `replacements` for word and phrase swaps,
`openers`/`closers` for chatbot wrappers to strip, and `punctuation_tells` for
dashes to normalize. This is a first pass, not the whole job: it does not
rewrite sentence structure or rhythm. That is the agent's work, guided by
SKILL.md. Always read the output before shipping it.

Usage:
    python humanize.py <file>
    cat file | python humanize.py
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


def strip_wrappers(text, slop):
    out = text
    for w in slop.get("openers", []) + slop.get("closers", []):
        out = re.sub(re.escape(w) + r"[^\n]*\n?", "", out, flags=re.I)
    return out


def swap(text, slop):
    swaps = slop.get("replacements", {})
    out = text
    for bad in sorted(swaps, key=len, reverse=True):
        good = swaps[bad]
        out = re.sub(r"\b" + re.escape(bad) + r"\b", good, out, flags=re.I)
    return out


def fix_dashes(text, slop):
    out = text
    for tell in slop.get("punctuation_tells", []):
        pat = r"[ \t]*" + re.escape(tell.strip()) + r"[ \t]*"
        out = re.sub(pat, ", ", out)
    return out


def cleanup(out):
    out = re.sub(r"\s+([,.;:!?])", r"\1", out)
    out = re.sub(r"([,;:])\s*([.!?])", r"\2", out)
    out = re.sub(r"([.!?])\s*([.!?,;:])", r"\1", out)
    out = re.sub(r"[ \t]{2,}", " ", out)
    out = re.sub(r"[ \t]+$", "", out, flags=re.M)
    out = re.sub(r"\n{3,}", "\n\n", out)
    out = re.sub(r"(^|\n)[ \t]*,[ \t]*", r"\1", out)
    return out.strip()


def main():
    slop = load_slop()
    text = read_text(sys.argv)
    out = strip_wrappers(text, slop)
    out = swap(out, slop)
    out = fix_dashes(out, slop)
    out = cleanup(out)
    sys.stdout.write(out + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
