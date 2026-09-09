# Marketing Engine

A version-controlled system that turns raw sales calls into shippable marketing
content. Built as a working example of *marketing engineering*: treating
marketing workflows as reproducible, composable pipelines instead of one-off tasks.

Vendor-neutral and industry-agnostic — the pattern works for any B2B company
doing customer discovery.

> **Note:** All data in this repo is fictional sample data (Northwind, Contoso).
> Real customer information is kept out of version control by design — see
> `.gitignore`.

## The pipeline

```
sales calls  ->  extract pains  ->  synthesize a brief  ->  generate content in a voice
 (.txt)          (extract.py)       (synthesize.py)         (generate_posts_voiced.py)
                                                                    ^
                                                            founder-voice/ profile
```

Each stage writes a file the next stage reads. Prompts live as versioned `.md`
files, treated as code — improve one, commit it, and every future run uses the
new logic.

## What each piece does

**`customer-truth/extract.py`** — reads one call transcript and pulls the 2-3
pain points the prospect expressed, in their own words.

**`customer-truth/synthesize.py`** — reads a whole folder of call summaries and
produces ONE positioning brief showing what prospects care about *across* calls:
ranked pains with frequency counts, the language they actually use, objections,
and a positioning hypothesis. A single call summary can't give you this.

**`content-engine/generate_posts.py`** — reads a brief and drafts LinkedIn posts
anchored in the real pains and real language the brief captured — not generic
talking points. Configurable per business via a company-context block in the prompt.

**`founder-voice/build_voice.py`** — studies real writing samples and builds a
reusable *voice profile*. The voice-aware generator
(`content-engine/generate_posts_voiced.py`) then writes posts in that specific
person's voice — the difference between drafts you rewrite and drafts you ship.
Ships with a fictional sample profile; real writing samples stay out of version control.

## Try it

First, install dependencies and add your API key:

```bash
pip install anthropic python-dotenv

# create a file named .env in the repo root containing:
#   ANTHROPIC_API_KEY=sk-ant-...
# (.env is gitignored, so your key is never committed)
```

Then run the three stages. Each one writes a file the next stage reads:

```bash
cd customer-truth

# 1. Extract pain points from one call.
#    Prints the pains from the sample transcript.
python extract.py interviews/sample-call.txt

# 2. Synthesize a brief across all summaries in the summaries/ folder.
#    Saves the brief to synthesis/brief-<today>.md
python synthesize.py summaries

# 3. Turn a brief into LinkedIn posts.
#    Point it at the brief from step 2 (or the included sample brief).
cd ../content-engine
python generate_posts.py ../customer-truth/synthesis/brief-sample.md 3
```

Prefer to just see the output? The [`examples/`](examples/) folder has real
pipeline output, pre-generated from the sample data:

- [`examples/example-pain-extraction.md`](examples/example-pain-extraction.md) — pains pulled from one call
- [`examples/example-linkedin-posts.md`](examples/example-linkedin-posts.md) — finished posts from the brief

## Why a pipeline instead of a chatbot?

A chat is great for one-off drafts. A pipeline gives you four things a chat can't:
consistent versioned prompts, scale (a folder of 3 or 300 calls, same command),
automation (it can run without a human), and composition (each step's output
feeds the next). The chat is the R&D lab; the repo is the production line.

## Design principles

- **Prompts are code.** Versioned `.md` files, improved deliberately, not buried
  in chat history.
- **Customer truth feeds everything.** Content is grounded in what prospects
  actually said, not assumptions.
- **Sensitive data never enters version control.** A whitelist `.gitignore`
  blocks all real transcripts and briefs by default; only named sample files pass.

## Roadmap

See `LEARNING.md` for the skill-by-skill build path. Next up: a voice layer so
generated content matches a specific person's tone, and scheduled automation so
briefs regenerate as new calls land.
