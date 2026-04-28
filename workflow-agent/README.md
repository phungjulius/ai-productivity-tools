# Workflow Automation Agent

A command-line AI agent that reads a list of tasks or action items, processes them intelligently, and produces a structured markdown report — with priority levels, categories, one-line action summaries, and a "Today's Focus" recommendation for where to start.

Supports both the Claude API (Anthropic) and OpenAI. Designed for professionals and teams who want a fast, structured way to turn a messy list of tasks into a clear daily plan.

## What it does

The agent runs in four steps:

1. **Read** — loads tasks from a plain text file, one item per line
2. **Process** — sends items to the AI, which classifies each one by priority and category and writes a one-sentence action summary
3. **Prioritise** — identifies the top three items to focus on today with a short rationale
4. **Report** — saves a structured markdown report to the output folder

Each item in the report is assigned:

- **Priority** — High, Medium, or Low
- **Category** — Action, Decision, Information, or Waiting
- **Summary** — one sentence describing what needs to happen

## Requirements

- Python 3.9 or higher
- An Anthropic API key ([console.anthropic.com](https://console.anthropic.com)) and/or an OpenAI API key ([platform.openai.com](https://platform.openai.com/api-keys))

## Setup

1. Clone the repository

```bash
git clone https://github.com/phungjulius/ai-productivity-tools.git
cd ai-productivity-tools/workflow-agent
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

Create a `.txt` file with your tasks, one per line:

```
Follow up with Anna on the vendor contract
Review and approve the Q2 budget proposal before Friday
The analytics dashboard is showing incorrect data for March
```

Then run:

```bash
python agent.py path/to/tasks.txt
```

**Options**

| Flag | Description | Default |
|---|---|---|
| `--provider` | AI provider: `claude` or `openai` | `claude` |
| `--model` | Model name to use | `claude-opus-4-5` / `gpt-4o` |
| `--output-dir` | Folder where the report is saved | `output/` |
| `--print` | Print the report to the terminal as well | off |

**Examples**

Process a task list and print the report:

```bash
python agent.py examples/team_tasks.txt --print
```

Use OpenAI instead of Claude:

```bash
python agent.py examples/project_actions.txt --provider openai
```

Save the report to a custom folder:

```bash
python agent.py examples/team_tasks.txt --output-dir reports
```

## Example output

```markdown
# Workflow Report

Generated on April 28, 2026 at 10:30 using claude (claude-opus-4-5)
Source: examples/team_tasks.txt

## Today's Focus

1. The analytics dashboard is showing incorrect data for March — needs investigation
2. Send the updated project timeline to the client by end of day
3. Follow up with Anna on the vendor contract

The analytics dashboard issue risks affecting business decisions if left unresolved,
making it the top priority. The client timeline is time-sensitive and blocks external
stakeholders. The vendor contract follow-up has already been delayed three days and
needs to be unblocked.

## All Items

| Priority  | Category    | Item                                              | Action needed                                      |
|-----------|-------------|---------------------------------------------------|----------------------------------------------------|
| 🔴 High   | Action      | Analytics dashboard showing incorrect data        | Investigate the data pipeline for March and fix    |
| 🔴 High   | Action      | Send updated project timeline to client           | Finalise and send the timeline document today      |
| 🔴 High   | Action      | Follow up with Anna on vendor contract            | Send a follow-up message and request a response    |
| 🟡 Medium | Decision    | Renew cloud storage or switch providers           | Review options and make a decision before May 5    |
| 🟡 Medium | Action      | Approve Q2 budget proposal                        | Review the proposal and approve or flag issues     |
| 🟢 Low    | Waiting     | Legal sign-off on NDA                             | Check status with legal and follow up if needed    |
| 🟢 Low    | Information | Read new data privacy policy update               | Read and acknowledge the policy update from IT     |
```

## Project structure

```
workflow-agent/
├── agent.py              # main script
├── requirements.txt      # dependencies
├── .env.example          # API key template
├── .gitignore
├── README.md
├── examples/
│   ├── team_tasks.txt    # example task list
│   └── project_actions.txt
└── output/               # generated reports (git-ignored)
```

## Notes

- Input files should be plain `.txt` with one task or action item per line
- Items work best when they describe a concrete situation, not just a topic
- Only the API key for the provider you use needs to be set in `.env`
- Reports are saved as markdown and can be pasted into Notion, Teams, or any documentation tool

## Author

Julius Phung — [github.com/phungjulius](https://github.com/phungjulius) — phungjulius@gmail.com