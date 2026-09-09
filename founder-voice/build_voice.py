"""
build_voice.py — Founder Voice, step 1 (run once per person).

Reads real writing samples from the samples/ folder and produces a reusable
VOICE PROFILE describing how that person writes. The profile gets saved to
voice-profile.md and reused by the content engine.

USAGE:
    python build_voice.py samples

    (put 3-8 real writing samples as .txt files in the samples/ folder first:
     old LinkedIn posts, emails, Slack messages, anything they actually wrote)

The profile prints AND saves to voice-profile.md.

SETUP: same as the other scripts — anthropic library + your .env key.
Run from inside the founder-voice folder.
"""

import sys
from pathlib import Path

from dotenv import load_dotenv
import anthropic

# Load key from repo-root .env (one level up).
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")
client = anthropic.Anthropic()

PROMPT_FILE = "prompts/build-voice-profile-v1.md"


def read_file(path):
    return Path(path).read_text(encoding="utf-8")


def load_samples(folder):
    """Read every .txt writing sample from the folder."""
    files = sorted(Path(folder).glob("*.txt"))
    if not files:
        print(f"No .txt samples found in '{folder}'.")
        print("Add 3-8 real writing samples (posts, emails, messages) as .txt files.")
        sys.exit(1)

    blocks = []
    for i, f in enumerate(files, 1):
        blocks.append(f"--- SAMPLE {i} ({f.name}) ---\n{read_file(f)}")
    return "\n\n".join(blocks), len(files)


def build_prompt(samples):
    template = read_file(PROMPT_FILE)
    body = template.split("## The prompt", 1)[1]
    return body.replace("{samples}", samples)


def build_profile(samples):
    prompt = build_prompt(samples)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def main():
    folder = sys.argv[1] if len(sys.argv) > 1 else "samples"
    samples, count = load_samples(folder)

    print(f"Analyzing {count} writing samples from '{folder}'...\n")
    profile = build_profile(samples)

    print("=" * 60)
    print(profile)
    print("=" * 60)

    out_path = Path("voice-profile.md")
    out_path.write_text(profile, encoding="utf-8")
    print(f"\nSaved voice profile to: {out_path}")
    print("The content engine will use this to write in your voice.")


if __name__ == "__main__":
    main()
