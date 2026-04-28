# AI Productivity Tools

A collection of Python tools that use AI APIs to automate common productivity tasks — meeting summaries, email drafting, prompt workflows, and business automation. Each tool is self-contained and can be used independently.

All tools support both the **Claude API** (Anthropic) and **OpenAI**, switchable via a command-line flag.

## Tools

### [Meeting Summary Bot](./meeting-summary-bot/)
Takes a plain-text meeting transcript and generates a structured summary with key decisions, action items with owners, and open questions. Useful for turning raw notes into actionable briefs that can be shared across a team.

```bash
python meeting-summary-bot/summarize.py transcript.txt --print
```

### [Email Draft Assistant](./email-draft-assistant/)
Describe what you need to say and get a professional email draft back. Supports three tone modes — formal, concise, and follow-up — and works with both Claude and OpenAI.

```bash
python email-draft-assistant/draft.py "Follow up on the project status meeting" --tone followup --sender "Julius"
```

### [Business Prompt Library](./prompt-library/)
A structured collection of tested, documented prompts for common business tasks: meeting agendas, weekly status reports, decision briefs, email thread summaries, and onboarding guides. Each prompt includes a full example input and output — copy, fill in the blanks, and run in any AI tool.

### [Workflow Automation Agent](./workflow-agent/)
A lightweight AI agent that reads a list of tasks or action items, classifies each one by priority and category, writes a one-sentence action summary for each, and produces a structured markdown report with a recommended daily focus.

```bash
python workflow-agent/agent.py tasks.txt --print
```

## Getting started

Each tool has its own folder with a README, setup instructions, and example files. Clone the full repo and navigate to the tool you want:

```bash
git clone https://github.com/phungjulius/ai-productivity-tools.git
cd ai-productivity-tools/meeting-summary-bot
```

## Requirements

- Python 3.9 or higher
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com)) for Claude
- An OpenAI API key ([platform.openai.com](https://platform.openai.com/api-keys)) for OpenAI

Each tool has its own `requirements.txt` and `.env.example`.

## Repository structure

```
ai-productivity-tools/
├── README.md
├── meeting-summary-bot/      # transcript → structured summary
├── email-draft-assistant/    # description → professional email draft
├── prompt-library/           # tested prompts for common business tasks
└── workflow-agent/           # multi-step AI task prioritisation agent
```

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com