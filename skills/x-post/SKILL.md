---
name: x-post
description: >-
  Draft a post for X (Twitter) from a rough idea, using 21 opener patterns and
  the account's own voice, then clear the AI giveaways before it ships. Use when
  the user wants to write something for their X timeline: a tweet, a post, an
  opener, an opening line, "write this as a tweet", "post this to X / Twitter",
  or asks for opener options. This is for X (Twitter) only, not LinkedIn,
  Instagram, Threads, or any other network. Returns three candidate openers, one
  finished post, and a paste-ready block that is never published without an
  explicit yes.
---

# x-post

One rough idea in, one post worth stopping for out.

## Prep

1. Open the voice profile at `templates/voice.md`. If it is missing, ask for
   three posts the user actually wrote, read the voice off those, and save the
   profile. Guessing a voice is not allowed; a post in someone else's voice is
   worse than no post.
2. Open `hooks.json` next to this file: 21 opener patterns, each with the move
   it makes, a filled sample, and the usual way it fails.
3. If the idea is empty ("write about AI"), do not decorate it. Ask one
   compact question: what happened, to whom, and what it cost or brought. A
   post needs a single concrete fact first.

## What the feed rewards

X surfaces roughly four lines before the reader has to tap "show more", about
130-170 characters. Two signals carry a post, and both are decided up there:
time on the post, and replies plus quote-posts, which the ranking weighs well
above likes. So the opener is not the only leverage; the closing line, which
invites the reply, is the other half. A link inside the body suppresses reach,
so when the user needs a destination, put it in a self-reply. Hashtags do
nothing here and read as spam. Opening with "a thread" throws the hook away.

## Skeleton

```
Line 1   the opener, standing alone at truncation width.
Line 2   the release of line 1. Not a ramp into line 3.
Middle   one thought per line, single-spaced, white space doing the work.
Pivot    one sentence that turns the post, when there is one.
Last     a single ask: a precise question, or one concrete action. Not both.
```

Length: 280 characters is the platform ceiling, and 120-240 is where single
posts live. Below about 80 it reads as a stray thought. Anything that truly
needs more room belongs to `x-thread`. Longer ceilings apply only to premium
accounts, and only when the opener has earned the tap. A one-liner can beat all
of this when the line is good.

## Working method

**1. Offer three openers.** Run the idea against `hooks.json` and pick three
that actually fit, from three different patterns. Show them as three lines,
and name the one you would run and why, in one sentence.

**2. Write the full post** on the opener you picked.

**3. Clear the AI giveaways.** Send the draft through `x-human`. This is not
optional; it is why the draft is readable.

**4. Present the block.** Paste-ready inside a fenced block, exactly as it
should go out. Under it, one line: what you would change if it flops, and the
tell that would show it (for example, "views but no replies usually means the
closing line is the weak part").

## Dead on arrival

- An opener that only parses once line 2 is read.
- "A thread" instead of a claim.
- Three sentences opening the same way.
- A close of "what do you think?" with nothing to answer.
- A post with no concrete noun: no figure, name, date, or place.
- Emoji used as bullets, hashtags, or a Title-Cased opener.

## Hard limit

Never invent a figure, a client, or a result the owner did not have. When the
requested claim cannot be supported, write the true version and say what you
left out. A post is a promise its author has to keep in the replies.
