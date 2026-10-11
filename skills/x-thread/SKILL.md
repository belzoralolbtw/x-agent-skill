---
name: x-thread
description: >-
  Build an X (Twitter) thread that holds attention past the first post, from a
  raw idea or a longer piece of writing. Use whenever the user wants a thread,
  a breakdown, "turn this into a thread", a list post, a step-by-step, or a
  story told across posts. Produces a hooked first post, 3-8 body posts each
  carrying one idea, and a closing post, all humanized and copy-ready.
---

# x-thread

A thread is one argument told in steps. If the steps can be shuffled without
breaking it, it is not a thread, it is a list, and it should be a single post.

## Before you write

1. Read the voice profile (`templates/voice.md`) or infer the voice from three of the
   user's own posts. Never invent a voice.
2. Read `hooks.json` in the `x-post` folder. The first post of a thread is a
   post, and its opener is held to the same bar. Patterns that suit a whole
   thread are usually "Counting Down", "The Clock", or "Pick a Lane", but any
   of them can open one.
3. Decide the spine before writing a line: what is the one claim the thread
   proves, and what are the steps that prove it. Write the spine in one
   sentence. If you cannot, the idea is not ready to be a thread.

## How threads actually work on X

- **The first post decides everything.** Most readers never see post 2. The
  opener has to work as a standalone post and make the next tap feel required.
- **The last line of each post is the hook for the next.** End each post on a
  small open loop or a consequence, not a full stop.
- **Length caps.** Each post is a normal X post, about 280 characters, and
  should sit in the 180-260 range. Under that is a fragment; over that is a
  link-free wall that does not fit.
- **No numbers on every post.** "1/", "2/" is fine, "1/ 2/ 3/" on all twelve is
  noise. If you number, number only the body and skip the opener.
- **The close is a single ask.** One question, or one instruction. A thread
  that ends with "follow for more" only works if the account earns it; default
  to a specific question that the thread has set up.

## The shape

```
Post 1    the hook, the promise, and the reason to keep reading. Standalone.
Post 2-3  the setup and the first real step. Earn the trust fast.
Post 4-9  one idea per post. Example, number, or scene in each.
Last      the payoff, restated as one line the reader can take away. Then one ask.
```

## The loop

**1. Write the spine** as one sentence.
**2. Write the opener** and show three hook options for it, as `x-post` does.
**3. Draft every post**, one idea each, no filler posts. If a post exists only
to connect two others, cut it and tighten the join.
**4. Humanize** the whole thread (`x-human`). Threads drift into list-y,
rule-shaped writing faster than single posts do.
**5. Print it** copy-ready, each post separated by a blank line, numbered only
if the user asked.

## Failure modes

- Posts that each restate the headline. That is twelve posts saying one thing.
- A "series of tips" with no through-line. Make it a single list post.
- Steps that need a screenshot to make sense, with no screenshot.
- An opener that only works if you already follow the argument.
- Twelve posts where six would do. Short threads win more often than long ones.
- A final post that asks for a follow instead of closing the loop.
