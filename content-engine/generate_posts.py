"""
generate_posts.py — Content Engine, step 1.

Reads a positioning brief (the .md file synthesize.py produced) and generates
LinkedIn posts grounded in the real prospect language the brief captured.

This is where the pipeline pays off: the brief flows straight into shippable
content, no copy-paste relay.

USAGE:
    python generate_posts.py ../customer-truth/synthesis/brief-2026-09-08.md
    python generate_posts.py ../customer-truth/synthesis/brief-2026-09-08.md 5

    (second argument = how many posts; defaults to 3)

Posts print AND save to output/linkedin-posts-<date>.md so you keep them.

SETUP: same as the other scripts — anthropic library + your .env key.
Run this from inside the content-engine folder.
"""

import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
import anthropic

# Load the key from the repo-root .env (one level up from content-engine).
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
client = anthropic.Anthropic()

PROMPT_FILE = "prompts/linkedin-posts-v1.md"


def read_file(path):
    return Path(path).read_text(encoding="utf-8")


def build_prompt(brief, post_count):
    template = read_file(PROMPT_FILE)
    prompt_body = template.split("## The prompt", 1)[1]
    prompt_body = prompt_body.replace("{post_count}", str(post_count))
    prompt_body = prompt_body.replace("{brief}", brief)
    return prompt_body


def generate(brief, post_count):
    prompt = build_prompt(brief, post_count)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,          # room for several full posts
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_posts.py <path-to-brief.md> [post_count]")
        print("Example: python generate_posts.py ../customer-truth/synthesis/brief-2026-09-08.md 3")
        sys.exit(1)

    brief_path = sys.argv[1]
    # Optional second argument: number of posts. Default 3.
    post_count = int(sys.argv[2]) if len(sys.argv) > 2 else 3

    brief = read_file(brief_path)

    print(f"Reading brief: {brief_path}")
    print(f"Generating {post_count} LinkedIn posts...\n")

    posts = generate(brief, post_count)

    print("=" * 60)
    print(posts)
    print("=" * 60)

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"linkedin-posts-{date.today().isoformat()}.md"
    out_path.write_text(posts, encoding="utf-8")
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    main()
