# Business Prompt Library

A structured collection of tested, documented prompts for common business tasks. Each prompt includes a description, the full prompt text with placeholders, an example input, and an example output — so you can copy, fill in the blanks, and get a useful result immediately.

Designed for professionals and teams who want to adopt AI tools reliably without spending time engineering prompts from scratch.

## Prompts

| Prompt | What it does |
|---|---|
| [Meeting Agenda Generator](./prompts/meeting_agenda.md) | Generates a structured agenda with time allocations from a meeting description |
| [Weekly Status Report](./prompts/weekly_report.md) | Turns rough end-of-week notes into a clean report ready to share with a manager |
| [Decision Brief](./prompts/decision_brief.md) | Summarizes a complex decision into a one-page brief for stakeholders |
| [Email Thread Summarizer](./prompts/email_summarizer.md) | Condenses a long email thread into a short summary with action items |
| [Onboarding Guide Generator](./prompts/onboarding_guide.md) | Creates a structured day-by-day onboarding plan for a new team member |

## How to use

Each prompt file contains:

- **What it does** — a plain-language description of the output
- **The prompt** — copy this into any AI tool (Claude, ChatGPT, Copilot, etc.)
- **Placeholders** — fill in the `{curly brace}` fields with your specific details
- **Example input and output** — so you know what to expect before you run it
- **Tips** — how to get better results from that specific prompt

### Quick start

1. Open the prompt file for the task you need
2. Copy the prompt text
3. Replace the `{placeholder}` fields with your details
4. Paste into Claude, ChatGPT, or any other AI tool
5. Adjust and re-run if needed

## Compatible tools

These prompts work with any large language model chat interface:

- [Claude](https://claude.ai) (Anthropic)
- [ChatGPT](https://chat.openai.com) (OpenAI)
- [Microsoft Copilot](https://copilot.microsoft.com)
- [Gemini](https://gemini.google.com) (Google)

## Repository structure

```
prompt-library/
├── README.md
└── prompts/
    ├── meeting_agenda.md
    ├── weekly_report.md
    ├── decision_brief.md
    ├── email_summarizer.md
    └── onboarding_guide.md
```

## Contributing

To add a new prompt, create a new `.md` file in the `prompts/` folder following the same structure as the existing files: description, prompt, example input, example output, when to use, and tips.

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com