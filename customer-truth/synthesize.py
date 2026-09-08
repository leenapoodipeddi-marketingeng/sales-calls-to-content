"""
synthesize.py — Customer Truth pipeline, step 2.

Reads ALL call summaries from a folder, sends them to Claude together, and
produces ONE brief on what prospects care about across all the calls.

This is the step Fathom can't do: it finds patterns ACROSS calls, not a
recap of each one.

USAGE:
    python synthesize.py summaries

    (where 'summaries' is the folder holding your .txt call summaries)

The brief is printed AND saved to synthesis/brief-<date>.md so you keep it.

SETUP: same as extract.py — needs the anthropic library and your .env key.
"""

import sys
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

PROMPT_FILE = "prompts/synthesize-brief-v1.md"


def read_file(path):
    return Path(path).read_text(encoding="utf-8")


def load_summaries(folder):
    """Read every .txt file in the folder. Return combined text + the count."""
    folder_path = Path(folder)
    txt_files = sorted(folder_path.glob("*.txt"))

    if not txt_files:
        print(f"No .txt files found in '{folder}'.")
        print("Put your Fathom summaries there as .txt files and try again.")
        sys.exit(1)

    # Stitch each summary together with a labeled separator so the model
    # can tell them apart.
    blocks = []
    for f in txt_files:
        text = read_file(f)
        blocks.append(f"--- SOURCE: {f.name} ---\n{text}")

    combined = "\n\n".join(blocks)
    return combined, len(txt_files)


def build_prompt(summaries, call_count):
    template = read_file(PROMPT_FILE)
    prompt_body = template.split("## The prompt", 1)[1]
    prompt_body = prompt_body.replace("{call_count}", str(call_count))
    prompt_body = prompt_body.replace("{summaries}", summaries)
    return prompt_body


def synthesize(summaries, call_count):
    prompt = build_prompt(summaries, call_count)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,          # bigger, since a brief is longer than an extraction
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def main():
    if len(sys.argv) < 2:
        print("Usage: python synthesize.py <folder-with-summaries>")
        print("Example: python synthesize.py summaries")
        sys.exit(1)

    folder = sys.argv[1]
    summaries, call_count = load_summaries(folder)

    print(f"Found {call_count} call summaries in '{folder}'.")
    print("Synthesizing brief across all of them...\n")

    brief = synthesize(summaries, call_count)

    print("=" * 60)
    print(brief)
    print("=" * 60)

    # Save the brief so you keep it.
    out_dir = Path("synthesis")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / f"brief-{date.today().isoformat()}.md"
    out_path.write_text(brief, encoding="utf-8")
    print(f"\nSaved to: {out_path}")


if __name__ == "__main__":
    main()
