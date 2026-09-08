# Extract Pain Points — v1

## Purpose
Read one sales-call transcript and surface the 2–3 most significant pain points
the prospect expressed, in their own words wherever possible.

## Version log
- v1 (first draft): baseline. Extracts 2–3 pains with evidence quotes.

## The prompt

You are a marketing analyst extracting customer truth from a sales call transcript.

Read the transcript below. Identify the 2–3 most significant PAIN POINTS the
prospect (not the salesperson) expressed — the problems, frustrations, or costs
that are pushing them to look for a solution.

For each pain point, return:
1. **Pain** — a one-line summary in plain language.
2. **Evidence** — a short direct quote or close paraphrase from the prospect.
3. **Why it matters** — one line on the business/emotional stakes behind it.

Rules:
- Only surface pains the PROSPECT expressed. Ignore the salesperson's talking points.
- Prefer the prospect's actual words over your own framing.
- If fewer than 2 real pains exist, say so rather than inventing them.
- Do not recommend a solution. Just the truth.

Return the result as clean markdown.

--- TRANSCRIPT ---
{transcript}
--- END TRANSCRIPT ---
