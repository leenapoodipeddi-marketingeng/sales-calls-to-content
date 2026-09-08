# Examples

Real output from the pipeline, generated from the fictional sample data in this
repo — so you can see what each stage produces without running anything.

- **`example-pain-extraction.md`** — output of `extract.py` on one sample call.
- **`example-linkedin-posts.md`** — output of `generate_posts.py` from the sample brief.

The synthesized brief that sits between these two stages lives at
`../customer-truth/synthesis/brief-sample.md`.

Together these three files show the full flow:
**one call → extracted pains → cross-call brief → shippable posts.**
