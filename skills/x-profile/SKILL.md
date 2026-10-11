---
name: x-profile
description: >-
  Audit and rewrite an X (Twitter) profile so a stranger who clicks from a
  reply or a post decides to follow. Use when the user wants to fix their bio,
  name, pinned post, or link, asks why their profile does not convert, or says
  people visit but do not follow. Produces a pass/fail score on seven checks
  and rewritten name, bio, and pinned post.
---

# x-profile

On X, the profile is the landing page. A reply or a good post earns the click;
the profile decides whether the click becomes a follower. Most accounts leak
followers here and never see it, because they never look at their own profile
the way a stranger does.

## Before you write

1. Ask for the current profile: name field, handle, bio, location, link, pinned
   post, follower and following counts, and the last ten posts.
2. Read the voice profile (`templates/voice.md`), or infer the voice from those posts.
3. Read `rubric.json` in this folder. Seven checks, each pass or fail, each
   with the failure it catches and the fix.

## The one test that matters

A stranger lands on the profile. Give them three seconds. They are asking two
questions, in this order: "what will I get if I follow?" and "is this person
real?" Everything on the profile either answers those or wastes the three
seconds.

## The loop

**1. Score the profile** against all seven checks in `rubric.json`. Show it as
a table: check, pass or fail, the specific reason. Be blunt. A passing badge on
a weak profile helps no one.

**2. Fix the fails, in order.** Name field first if it fails (it is the search
surface), then bio line 1, then the pinned post. Give the rewritten text, not
advice about it.

**3. Rewrite the bio** as one version, not three. A bio is not a place to A/B
test; it is a place to say what you do. Format:

```
Line 1   who you help + do what, or plainly what you post about.
Line 2   proof, or the specific result you produce.
Line 3   optional: a light human detail, or a call to the link/pinned post.
```

**4. Rewrite or replace the pinned post.** If the account has a strong recent
post, pin it. If not, write a short "start here" post: one line on what the
account is about and one line pointing to the best thing they have.

**5. Humanize** the bio and pinned post (`x-human`). A bio that reads as AI
undoes the trust the rest of the profile is trying to build.

## Rules of thumb

- The name field is search. Put the category in it, e.g. `Sam | SEO for SaaS`.
- The bio is for the reader, not the owner. "I help X do Y" beats "passionate
  about Y".
- One proof point beats three adjectives. A number, a name, or a link.
- No hashtags in the bio. No emoji walls. No "DM me to grow your account".
- The link, if present, should be the most useful single page, not a homepage.

## Failure modes

- Writing a clever bio that sounds great and communicates nothing.
- Rewriting the bio while the pinned post still shows a dead launch from
  eight months ago.
- Adding more claims when the problem was the absence of proof.
- Changing the name field to a joke and losing the search keyword.
- Optimizing the profile while the timeline has nothing a new follower wants.
