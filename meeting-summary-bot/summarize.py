import os
import sys
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


SUMMARY_PROMPT = """You are an assistant that summarizes meeting transcripts for busy professionals.

Given the transcript below, produce a clean, structured summary with the following sections:

1. Meeting Overview — one or two sentences on what the meeting was about
2. Key Decisions — bullet list of decisions made
3. Action Items — bullet list, each with the responsible person and a deadline if mentioned
4. Open Questions — anything left unresolved or requiring follow-up

Be concise. Use plain language. Do not invent information that is not in the transcript.

Transcript:
{transcript}
"""


def load_transcript(filepath: str) -> str:
    path = Path(filepath)
    if not path.exists():
        print(f"Error: file not found — {filepath}")
        sys.exit(1)
    if path.suffix.lower() != ".txt":
        print("Warning: expected a .txt file. Proceeding anyway.")
    return path.read_text(encoding="utf-8").strip()


def summarize_with_claude(transcript: str, model: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    prompt = SUMMARY_PROMPT.format(transcript=transcript)
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def summarize_with_openai(transcript: str, model: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    prompt = SUMMARY_PROMPT.format(transcript=transcript)
    response = client.chat.completions.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def summarize(transcript: str, provider: str, model: str) -> str:
    if provider == "claude":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return summarize_with_claude(transcript, model)
    elif provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return summarize_with_openai(transcript, model)
    else:
        print(f"Error: unknown provider '{provider}'. Use 'claude' or 'openai'.")
        sys.exit(1)


def save_output(summary: str, input_path: str, output_dir: str) -> str:
    stem = Path(input_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{stem}_summary_{timestamp}.md"
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(summary, encoding="utf-8")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Summarize a meeting transcript using Claude or OpenAI."
    )
    parser.add_argument(
        "transcript",
        help="Path to the transcript .txt file",
    )
    parser.add_argument(
        "--provider",
        default="claude",
        choices=["claude", "openai"],
        help="AI provider to use: 'claude' (default) or 'openai'",
    )
    parser.add_argument(
        "--model",
        default=None,
        help=(
            "Model to use. Defaults: claude-opus-4-5 for Claude, gpt-4o for OpenAI. "
            "Override with any valid model name from your provider."
        ),
    )
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where the summary file will be saved (default: output/)",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        dest="print_output",
        help="Print the summary to the terminal in addition to saving it",
    )

    args = parser.parse_args()

    # set default model based on provider if not specified
    if args.model is None:
        args.model = "claude-opus-4-5" if args.provider == "claude" else "gpt-4o"

    print(f"Loading transcript: {args.transcript}")
    transcript = load_transcript(args.transcript)

    print(f"Generating summary using {args.provider} ({args.model})...")
    summary = summarize(transcript, provider=args.provider, model=args.model)

    saved_path = save_output(summary, args.transcript, args.output_dir)
    print(f"Summary saved to: {saved_path}")

    if args.print_output:
        print("\n" + summary)


if __name__ == "__main__":
    main()
