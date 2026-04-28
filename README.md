# AI Productivity Tools

A collection of Python tools that use AI APIs to automate common productivity tasks — meeting summaries, email drafting, prompt workflows, and business automation. Each tool is self-contained and can be used independently.

All tools support both the **Claude API** (Anthropic) and **OpenAI**, switchable via a command-line flag.

## Tools

### [Meeting Summary Bot](./meeting-summary-bot/)
Takes a plain-text meeting transcript and generates a structured summary with key decisions, action items with owners, and open questions. Useful for turning raw notes into actionable briefs that can be shared across a team.

```bash
python meeting-summary-bot/summarize.py transcript.txt --print
```

### [Email Draft Assistant](./email-draft-assistant/) *(coming soon)*
Describe what you need to say and get a professional email draft back. Supports tone options — formal, concise, or follow-up — and works with both Claude and OpenAI.

### [Business Prompt Library](./prompt-library/) *(coming soon)*
A structured collection of tested, documented prompts for common business tasks: summarization, weekly reports, meeting agendas, and decision briefings. Designed to help teams adopt AI tools with ready-made, reliable prompts.

### [Workflow Automation Agent](./workflow-agent/) *(coming soon)*
A lightweight Python agent that chains multiple AI steps together — reads a list of tasks or emails, processes and prioritizes them using an AI API, and outputs a structured markdown report.

## Getting started

Each tool has its own folder with a README, setup instructions, and example files. Clone the full repo and navigate to the tool you want to use:

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
├── email-draft-assistant/    # description → professional email
├── prompt-library/           # tested prompts for business use cases
└── workflow-agent/           # multi-step AI automation pipeline
```

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com
