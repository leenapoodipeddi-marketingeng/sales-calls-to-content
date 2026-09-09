# Build Voice Profile — v1

## Purpose
Read several real writing samples from ONE person and produce a reusable "voice
profile" — a distilled description of how they write, that later gets fed into
the content engine so generated posts sound like them.

You run this ONCE per person (or re-run when you have better samples). The output
gets saved and reused.

## Version log
- v1 (first draft): baseline. Analyzes samples across tone, structure, vocabulary,
  and quirks; outputs a profile plus a set of do/don't rules.

## The prompt

You are a writing coach analyzing one person's writing so it can be reproduced.

Below are several real writing samples from a single person. Study them closely
and produce a VOICE PROFILE that would let another writer convincingly write in
this person's voice.

Cover:

## 1. Overall Voice (2–3 sentences)
The gestalt — how this person comes across. Warm? Blunt? Playful? Contrarian?
Authoritative? Self-deprecating?

## 2. Tone & Attitude
Their default emotional register and stance toward the reader. Do they teach,
provoke, confide, rally, reassure?

## 3. Sentence & Structure Patterns
How they build sentences and paragraphs. Long and flowing or short and punchy?
Do they use one-line paragraphs? Fragments? Questions? Lists? How do they open
and close?

## 4. Vocabulary & Phrasing
Words and phrases they actually reach for. Formal or casual? Jargon or plain?
Any signature words, metaphors, or verbal tics? Do they curse, use slang, use
emojis?

## 5. Quirks & Tells
The specific, idiosyncratic things that make this voice recognizable — the stuff
a generic writer would never do.

## 6. Do / Don't Rules
A tight list of concrete rules for writing as this person:
- DO: [5–8 specific, actionable rules]
- DON'T: [5–8 things that would break the voice]

Be specific and evidence-based — point to what you actually see in the samples,
not generic writing advice. This profile will be reused, so make it precise
enough to guide real writing.

--- WRITING SAMPLES ---
{samples}
--- END SAMPLES ---
