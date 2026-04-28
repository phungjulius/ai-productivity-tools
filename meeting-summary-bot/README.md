# Meeting Summary Bot

A command-line tool that reads a meeting transcript and generates a structured summary — including key decisions, action items with owners, and open questions. Supports both the Claude API (Anthropic) and OpenAI.

Built for teams that want to turn raw meeting notes into clean, actionable briefs without manual effort.

## What it does

Given a plain-text transcript, the tool produces a markdown summary with four sections:

- **Meeting Overview** — a short description of what the meeting covered
- **Key Decisions** — a bullet list of decisions made during the meeting
- **Action Items** — each item with the responsible person and deadline if mentioned
- **Open Questions** — anything unresolved or requiring follow-up

Summaries are saved as markdown files in the `output/` folder, named automatically with a timestamp.

## Requirements

- Python 3.9 or higher
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com)) and/or an OpenAI API key ([platform.openai.com](https://platform.openai.com/api-keys))

## Setup

1. Clone the repository

```bash
git clone https://github.com/phungjulius/ai-productivity-tools.git
cd ai-productivity-tools/meeting-summary-bot
```

2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Add your API keys

```bash
cp .env.example .env
```

Open `.env` and fill in your Anthropic and/or OpenAI API key.

## Usage

```bash
python summarize.py path/to/transcript.txt
```

By default the tool uses Claude. Switch to OpenAI with `--provider openai`.

**Options**

| Flag | Description | Default |
|---|---|---|
| `--provider` | AI provider: `claude` or `openai` | `claude` |
| `--model` | Model name to use | `claude-opus-4-5` / `gpt-4o` |
| `--output-dir` | Folder where summaries are saved | `output/` |
| `--print` | Print the summary to the terminal as well | off |

**Examples**

Summarize using Claude and print the result:

```bash
python summarize.py transcripts/examples/product_review.txt --print
```

Summarize using OpenAI:

```bash
python summarize.py transcripts/examples/team_standup.txt --provider openai
```

Use a specific model:

```bash
python summarize.py transcripts/examples/product_review.txt --provider openai --model gpt-4-turbo
```

Save to a custom output folder:

```bash
python summarize.py transcripts/examples/team_standup.txt --output-dir my_summaries
```

## Project structure

```
meeting-summary-bot/
├── summarize.py                  # main script
├── requirements.txt              # dependencies
├── .env.example                  # API key template
├── .gitignore
├── transcripts/
│   └── examples/
│       ├── product_review.txt    # example transcript
│       └── team_standup.txt      # example transcript
└── output/                       # generated summaries (git-ignored)
```

## Example output

Input: `transcripts/examples/product_review.txt`

```
## Meeting Overview
The team aligned on Q2 deliverables, confirmed the search feature release timeline,
and officially moved the onboarding redesign to Q3.

## Key Decisions
- Search feature build must be delivered by May 1 to allow QA a two-week window
- Onboarding flow redesign is deferred to Q3
- David takes ownership of the release checklist process

## Action Items
- David: notify the engineering team of the May 1 build deadline — today
- Sara: review Mia's revised onboarding wireframes — by Thursday
- Sara: decide on analytics provider and share recommendation — by next Monday

## Open Questions
- Which analytics provider will be selected for search feature instrumentation?
```

## Notes

- Transcripts should be plain `.txt` files
- The tool works best when speaker names are included in the transcript
- Only the API key for the provider you use needs to be set in `.env`
- API usage is billed to your account based on token count

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com
