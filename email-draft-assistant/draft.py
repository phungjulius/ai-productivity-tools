import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()


TONES = {
    "formal": "formal and professional — suitable for executive or client communication",
    "concise": "concise and direct — short sentences, no filler, get to the point quickly",
    "followup": "friendly but professional — appropriate for following up on a previous conversation",
}

DRAFT_PROMPT = """You are an assistant that writes professional emails for busy professionals.

Write an email based on the following details:

Situation: {situation}
Tone: {tone_description}
{recipient_line}
{sender_line}

Requirements:
- Write a clear and relevant subject line
- Keep the email focused and easy to read
- Match the tone exactly as described
- Do not add unnecessary filler or pleasantries beyond what is appropriate for the tone
- Output format: start with "Subject: ..." on the first line, leave a blank line, then write the email body

Write only the email. Do not add any explanation or commentary.
"""


def build_prompt(situation: str, tone: str, recipient: str, sender: str) -> str:
    tone_description = TONES.get(tone, TONES["formal"])
    recipient_line = f"Recipient: {recipient}" if recipient else ""
    sender_line = f"Sender name (for sign-off): {sender}" if sender else ""
    return DRAFT_PROMPT.format(
        situation=situation,
        tone_description=tone_description,
        recipient_line=recipient_line,
        sender_line=sender_line,
    )


def draft_with_claude(prompt: str, model: str) -> str:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def draft_with_openai(prompt: str, model: str) -> str:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model=model,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def draft(prompt: str, provider: str, model: str) -> str:
    if provider == "claude":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return draft_with_claude(prompt, model)
    elif provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return draft_with_openai(prompt, model)
    else:
        print(f"Error: unknown provider '{provider}'. Use 'claude' or 'openai'.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Draft a professional email using Claude or OpenAI."
    )
    parser.add_argument(
        "situation",
        help=(
            "A plain-language description of what the email should communicate. "
            "Example: 'Follow up on last week's project status meeting and ask for an updated timeline.'"
        ),
    )
    parser.add_argument(
        "--tone",
        default="formal",
        choices=["formal", "concise", "followup"],
        help="Tone of the email: formal (default), concise, or followup",
    )
    parser.add_argument(
        "--recipient",
        default=None,
        help="Name or role of the recipient, e.g. 'the engineering team' or 'Anna from HR'",
    )
    parser.add_argument(
        "--sender",
        default=None,
        help="Your name for the sign-off line",
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
        help="Model to use. Defaults: claude-opus-4-5 for Claude, gpt-4o for OpenAI.",
    )

    args = parser.parse_args()

    if args.model is None:
        args.model = "claude-opus-4-5" if args.provider == "claude" else "gpt-4o"

    prompt = build_prompt(
        situation=args.situation,
        tone=args.tone,
        recipient=args.recipient,
        sender=args.sender,
    )

    print(f"Drafting email using {args.provider} ({args.model})...\n")
    result = draft(prompt, provider=args.provider, model=args.model)
    print(result)


if __name__ == "__main__":
    main()