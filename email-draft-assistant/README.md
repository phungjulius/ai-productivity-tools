# Email Draft Assistant

A command-line tool that takes a plain-language description of what you need to say and returns a ready-to-send professional email — including a subject line. Supports three tone modes and works with both the Claude API (Anthropic) and OpenAI.

Built for professionals who want to cut the time spent staring at a blank compose window.

## What it does

Describe the situation in plain language and the tool handles the rest:

- Writes a clear, relevant subject line
- Drafts the full email body matched to the requested tone
- Supports three tone modes: `formal`, `concise`, and `followup`
- Accepts optional recipient and sender names for a personalised result

## Requirements

- Python 3.9 or higher
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com)) and/or an OpenAI API key ([platform.openai.com](https://platform.openai.com/api-keys))

## Setup

1. Clone the repository

```bash
git clone https://github.com/phungjulius/ai-productivity-tools.git
cd ai-productivity-tools/email-draft-assistant
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
python draft.py "your situation here"
```

**Options**

| Flag | Description | Default |
|---|---|---|
| `--tone` | Email tone: `formal`, `concise`, or `followup` | `formal` |
| `--recipient` | Name or role of the recipient | none |
| `--sender` | Your name for the sign-off | none |
| `--provider` | AI provider: `claude` or `openai` | `claude` |
| `--model` | Model name to use | `claude-opus-4-5` / `gpt-4o` |

## Tone modes

| Tone | When to use |
|---|---|
| `formal` | Executive communication, client emails, first contact |
| `concise` | Internal updates, quick requests, busy recipients |
| `followup` | Checking in after a meeting, nudging on a pending response |

## Examples

Draft a formal email requesting a project update:

```bash
python draft.py "Request a status update on the Q2 delivery timeline from the engineering team" \
  --tone formal \
  --recipient "the engineering team" \
  --sender "Julius"
```

Draft a concise internal follow-up:

```bash
python draft.py "Remind the team that the design review is tomorrow at 10am and ask them to come prepared" \
  --tone concise \
  --sender "Julius"
```

Use OpenAI instead of Claude:

```bash
python draft.py "Follow up on a job application submitted two weeks ago" \
  --tone followup \
  --provider openai \
  --sender "Julius"
```

## Example output

```
Subject: Request for Q2 Delivery Timeline Update

Dear Engineering Team,

I am writing to request an update on the current status of the Q2 delivery timeline.
As we approach the end of the quarter, it would be helpful to have a clear picture
of where things stand and whether any adjustments are needed.

Could you please share an updated timeline at your earliest convenience? I am happy
to schedule a brief call if that would be easier.

Thank you for your continued work on this.

Best regards,
Julius
```

## Project structure

```
email-draft-assistant/
├── draft.py          # main script
├── requirements.txt  # dependencies
├── .env.example      # API key template
├── .gitignore
└── README.md
```

## Notes

- The situation argument works best when it describes the context and goal clearly
- Only the API key for the provider you use needs to be set in `.env`
- API usage is billed to your account based on token count

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com