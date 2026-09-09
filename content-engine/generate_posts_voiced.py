"""
generate_posts_voiced.py — Content Engine, step 1 (voice-aware version).

Like generate_posts.py, but writes in a SPECIFIC person's voice using the voice
profile that build_voice.py produced.

USAGE:
    python generate_posts_voiced.py <brief.md> <voice-profile.md> [post_count]

    Example:
    python generate_posts_voiced.py ../customer-truth/synthesis/brief-2026-09-08.md ../founder-voice/voice-profile.md 3

Posts print AND save to output/linkedin-posts-voiced-<date>.md

SETUP: anthropic library + .env key. Run from inside content-engine.
"""

import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
import anthropic

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
client = anthropic.Anthropic()

PROMPT_FILE = "prompts/linkedin-posts-v2.md"


def read_file(path):
    return Path(path).read_text(encoding="utf-8")


def build_prompt(brief, voice_profile, post_count):
    template = read_file(PROMPT_FILE)
    body = template.split("## The prompt", 1)[1]
    body = body.replace("{post_count}", str(post_count))
    body = body.replace("{voice_profile}", voice_profile)
    body = body.replace("{brief}", brief)
    return body


def generate(brief, voice_profile, post_count):
    prompt = build_prompt(brief, voice_profile, post_count)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=3000,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_posts_voiced.py <brief.md> <voice-profile.md> [post_count]")
        sys.exit(1)

    brief = read_file(sys.argv[1])
    voice_profile = read_file(sys.argv[2])
    post_count = int(sys.argv[3]) if len(sys.argv) > 3 else 3

    print(f"Brief: {sys.argv[1]}")
    print(f"Voice: {sys.argv[2]}")
    print(f"Generating {post_count} posts in voice...\n")

    posts = generate(brief, voice_profile, post_count)

    print("=" * 60)
    print(posts)
    print("=" * 60)

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"linkedin-posts-voiced-{date.today().isoformat()}.md"
    out_path.write_text(posts, encoding="utf-8")
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    main()
