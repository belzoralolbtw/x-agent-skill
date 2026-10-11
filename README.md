# The X agent

[![skills.sh](https://skills.sh/b/belzoralolbtw/x-agent-skill)](https://skills.sh/belzoralolbtw/x-agent-skill)

Ten agent skills that run an X (Twitter) account. Open source under MIT.
There is nothing to sign up for and no API key to paste: the skills write, and
you post.

One builds the voice the others write in. One drafts posts from 21 opener
patterns. One is the reply game, which is how almost every account under 10k
followers actually grows. One scores your profile the way a stranger decides in
three seconds. In between, the others build threads, plan the week, mine your
old content for posts, audit your numbers, write DMs that get answers, and
clear the AI giveaways from every draft before it ships.

Works with [CC], Codex, Cursor, Gemini CLI, and any agent that supports the
open [Agent Skills](https://agentskills.io) format.

## The skills

```
x-setup       Build the voice profile and a starter content base. Run first.
x-profile     Score and fix the name, bio, pinned post, and link.
x-reply       The growth engine: reply to the accounts whose audience you want.
x-post        Draft a post from 21 opener patterns, in your voice, cleaned.
x-thread      Build a thread that holds attention past post one.
x-plan        A weekly plan at a cadence you can actually keep.
x-repurpose   Mine content you already made for posts that stand alone.
x-audit       Read your analytics and name the one bottleneck to fix.
x-dm          Outreach DMs that get replies, plus one follow-up.
x-human       Strip AI tells from any draft and score it on five checks.
```

## Install

As a plugin, in [CC]:

```
/plugin marketplace add belzoralolbtw/x-agent-skill
/plugin install x-agent@x-agent-skill
```

[CC] namespaces plugin skills, so installed as a plugin they show up as
`/x-agent:x-post` and so on. Copy the folders instead if you want plain
`/x-post`:

```bash
git clone https://github.com/belzoralolbtw/x-agent-skill.git
cp -r x-agent-skill/skills/x-* ~/.claude/skills/
```

Other agents, via the Skills CLI:

```bash
npx skills add belzoralolbtw/x-agent-skill --global --agent '*'
```

## Usage

Start with setup, once:

```
/x-setup
```

Then fix the profile and start reaching people:

```
/x-profile
/x-reply
```

And when you need to post:

```
/x-post I finally shipped the pricing change
```

Every draft comes back humanized and copy-ready. Nothing gets posted anywhere;
these skills write, you decide.

## How it works

Each skill is a folder with one `SKILL.md` file, plain markdown in the Agent
Skills format. They load only when relevant, so the whole pack costs almost
nothing in context until you use a part of it. No code to run, no credentials,
no data leaves your machine, except a couple of small Python helpers in
`x-human` you can run yourself to scan a draft for AI tells.

## The ideas it is built on

- Replies, not posts, are how small accounts grow. The pack treats replying as
  the main job, not an afterthought.
- The profile is the landing page. A good post earns a click; the profile
  decides whether it becomes a follower.
- Every draft is humanized, because a timeline is people talking, and anything
  that reads as composed loses.
- One specific true thing beats a general truth. The skills ask for the number,
  the name, the date, and refuse to invent one.

## Licence

MIT. Use it, fork it, ship your own version.

Built on the open [Agent Skills](https://agentskills.io) standard.
