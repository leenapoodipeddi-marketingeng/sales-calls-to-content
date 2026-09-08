# Synthesize Prospect Brief — v1

## Purpose
Read multiple sales-call summaries at once and produce ONE brief that surfaces
what prospects actually care about ACROSS all the calls — patterns, not
call-by-call recaps. This is the thing a single call summary can never give you.

## Version log
- v1 (first draft): baseline. Ranks pains by frequency across calls, pulls
  the exact language prospects use, flags objections and desired outcomes.

## The prompt

You are a marketing strategist building a positioning brief from real sales calls.

Below are summaries from {call_count} separate sales calls, each separated by a
line of dashes and labeled with its source file. Read ALL of them together and
find what is TRUE ACROSS the calls — not a recap of each one.

Produce a single brief with these sections:

## 1. Top Pain Points (ranked by how often they appear)
For each recurring pain: a one-line summary, how many of the calls it showed up
in, and 1–2 exact phrases prospects used (in quotes). Rank most common first.
Only include pains that appear in more than one call, unless a single one is so
severe it's worth flagging alone (mark it "single call, high intensity").

## 2. The Language They Use
A short list of the actual words and phrases prospects reach for when describing
their problems. This is the raw material for messaging — prefer their words over
marketing-speak.

## 3. Objections & Hesitations
What's making them slow to switch or buy? Contracts, risk, timing, cost, trust —
whatever recurs.

## 4. Desired Outcomes
What do they actually want the future to look like? What would "solved" feel like
to them?

## 5. One-Line Positioning Hypothesis
Based only on what's in these calls, draft ONE sentence: the single most
resonant thing a vendor could say to these prospects. Mark it clearly as a
hypothesis to test, not a conclusion.

Rules:
- Synthesize across calls. Do not summarize them one at a time.
- Count honestly. If a pain shows up in 2 of 3 calls, say "2 of 3."
- Prefer the prospect's exact words. Quote them.
- If the calls don't support a section, say so rather than inventing.
- Keep it tight and usable — this is a working brief, not an essay.

--- CALL SUMMARIES ---
{summaries}
--- END CALL SUMMARIES ---
