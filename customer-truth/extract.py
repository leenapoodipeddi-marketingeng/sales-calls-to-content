"""
extract.py — Customer Truth pipeline, step 1.

Reads a sales-call transcript from a .txt file, sends it to Claude with the
pain-point extraction prompt, and prints 2-3 pain points.

This is Path A: you paste your Fathom transcript into a .txt file by hand,
then run this. Automating the Fathom pull comes later (Phase 4).

USAGE:
    python extract.py interviews/sample-call.txt

SETUP (one time):
    pip install anthropic python-dotenv
    Create a file named .env in the repo root containing:
        ANTHROPIC_API_KEY=sk-ant-your-key-here
    (.env is already in .gitignore, so your key never gets committed.)
"""

import sys
from pathlib import Path

from dotenv import load_dotenv   # loads your .env so the key is available
import anthropic

# Load ANTHROPIC_API_KEY from the .env file into the environment.
load_dotenv()

# The Anthropic client automatically reads ANTHROPIC_API_KEY from the environment.
client = anthropic.Anthropic()

# Which prompt version we're using. Bump this when you write v2.
PROMPT_FILE = "prompts/extract-pain-points-v1.md"


def read_file(path):
    """Read a text file and return its contents as a string."""
    return Path(path).read_text(encoding="utf-8")


def build_prompt(transcript):
    """Load the prompt template and drop the transcript into the {transcript} slot."""
    template = read_file(PROMPT_FILE)
    # We only want the part of the .md file after the '## The prompt' heading.
    prompt_body = template.split("## The prompt", 1)[1]
    return prompt_body.replace("{transcript}", transcript)


def extract_pain_points(transcript):
    """Send the transcript to Claude and return the extracted pain points."""
    prompt = build_prompt(transcript)

    message = client.messages.create(
        model="claude-sonnet-4-6",   # good balance of quality and cost
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    # The response text lives in the first content block.
    return message.content[0].text


def main():
    # sys.argv is the list of words you typed. argv[0] is the script name,
    # argv[1] is the transcript path you passed in.
    if len(sys.argv) < 2:
        print("Usage: python extract.py <path-to-transcript.txt>")
        sys.exit(1)

    transcript_path = sys.argv[1]
    transcript = read_file(transcript_path)

    print(f"Reading: {transcript_path}")
    print(f"Using prompt: {PROMPT_FILE}\n")
    print("Extracting pain points...\n")

    result = extract_pain_points(transcript)

    print("=" * 60)
    print(result)
    print("=" * 60)


if __name__ == "__main__":
    main()
