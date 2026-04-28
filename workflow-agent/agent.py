import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# step 1: read and parse raw input items from a text file
# each non-empty line is treated as one item
def load_items(filepath: str) -> list[str]:
    path = Path(filepath)
    if not path.exists():
        print(f"Error: file not found — {filepath}")
        sys.exit(1)
    lines = path.read_text(encoding="utf-8").splitlines()
    items = [line.strip() for line in lines if line.strip()]
    if not items:
        print("Error: input file is empty.")
        sys.exit(1)
    return items


# step 2: send items to the AI for processing
# the agent classifies, prioritises, and summarises each item
AGENT_PROMPT = """You are a productivity assistant that helps professionals manage their workload.

You will receive a list of tasks, emails, or action items. For each item, do the following:
1. Assign a priority: High, Medium, or Low
2. Assign a category: Action, Decision, Information, or Waiting
3. Write a one-sentence summary of what needs to happen

Then, at the end, write a short "Today's Focus" section recommending the top three items to tackle first and why.

Input items:
{items}

Respond in the following JSON format and nothing else:
{{
  "processed_items": [
    {{
      "item": "original item text",
      "priority": "High | Medium | Low",
      "category": "Action | Decision | Information | Waiting",
      "summary": "one sentence describing what needs to happen"
    }}
  ],
  "focus": {{
    "top_three": ["item 1", "item 2", "item 3"],
    "reasoning": "two to three sentences explaining why these three items are the priority"
  }}
}}
"""


def process_with_claude(items: list[str], model: str) -> dict:
    import anthropic
    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    numbered = "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
    prompt = AGENT_PROMPT.format(items=numbered)
    message = client.messages.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = message.content[0].text.strip()
    return json.loads(raw)


def process_with_openai(items: list[str], model: str) -> dict:
    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    numbered = "\n".join(f"{i+1}. {item}" for i, item in enumerate(items))
    prompt = AGENT_PROMPT.format(items=numbered)
    response = client.chat.completions.create(
        model=model,
        max_tokens=2048,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content.strip()
    return json.loads(raw)


def process_items(items: list[str], provider: str, model: str) -> dict:
    if provider == "claude":
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("Error: ANTHROPIC_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return process_with_claude(items, model)
    elif provider == "openai":
        if not os.environ.get("OPENAI_API_KEY"):
            print("Error: OPENAI_API_KEY is not set. Check your .env file.")
            sys.exit(1)
        return process_with_openai(items, model)
    else:
        print(f"Error: unknown provider '{provider}'. Use 'claude' or 'openai'.")
        sys.exit(1)


# step 3: render the structured result into a readable markdown report
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}
PRIORITY_LABEL = {"High": "🔴 High", "Medium": "🟡 Medium", "Low": "🟢 Low"}


def render_report(result: dict, input_path: str, provider: str, model: str) -> str:
    timestamp = datetime.now().strftime("%B %d, %Y at %H:%M")
    lines = []

    lines.append(f"# Workflow Report")
    lines.append(f"\nGenerated on {timestamp} using {provider} ({model})")
    lines.append(f"\nSource: `{input_path}`")

    lines.append("\n## Today's Focus\n")
    focus = result.get("focus", {})
    for i, top_item in enumerate(focus.get("top_three", []), 1):
        lines.append(f"{i}. {top_item}")
    lines.append(f"\n{focus.get('reasoning', '')}")

    lines.append("\n## All Items\n")
    lines.append("| Priority | Category | Item | Action needed |")
    lines.append("|---|---|---|---|")

    processed = result.get("processed_items", [])
    sorted_items = sorted(processed, key=lambda x: PRIORITY_ORDER.get(x["priority"], 99))

    for entry in sorted_items:
        priority = PRIORITY_LABEL.get(entry["priority"], entry["priority"])
        category = entry.get("category", "")
        item = entry.get("item", "").replace("|", "-")
        summary = entry.get("summary", "").replace("|", "-")
        lines.append(f"| {priority} | {category} | {item} | {summary} |")

    return "\n".join(lines)


# step 4: save the report to the output folder
def save_report(report: str, input_path: str, output_dir: str) -> str:
    stem = Path(input_path).stem
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{stem}_report_{timestamp}.md"
    output_path = Path(output_dir) / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Process a list of tasks or action items using an AI agent."
    )
    parser.add_argument(
        "input",
        help="Path to a .txt file containing tasks or action items, one per line",
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
    parser.add_argument(
        "--output-dir",
        default="output",
        help="Directory where the report will be saved (default: output/)",
    )
    parser.add_argument(
        "--print",
        action="store_true",
        dest="print_output",
        help="Print the report to the terminal in addition to saving it",
    )

    args = parser.parse_args()

    if args.model is None:
        args.model = "claude-opus-4-5" if args.provider == "claude" else "gpt-4o"

    print(f"Loading items from: {args.input}")
    items = load_items(args.input)
    print(f"Found {len(items)} item(s). Processing with {args.provider} ({args.model})...")

    result = process_items(items, provider=args.provider, model=args.model)

    report = render_report(result, args.input, args.provider, args.model)
    saved_path = save_report(report, args.input, args.output_dir)
    print(f"Report saved to: {saved_path}")

    if args.print_output:
        print("\n" + report)


if __name__ == "__main__":
    main()