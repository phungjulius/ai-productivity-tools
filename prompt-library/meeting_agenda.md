# Meeting Agenda Generator

Generate a structured meeting agenda from a brief description of the meeting purpose.

## Prompt

```
You are an assistant that helps professionals run effective meetings.

Create a structured meeting agenda based on the following details:

Meeting purpose: {purpose}
Duration: {duration}
Attendees: {attendees}

Format the agenda with:
- A short meeting title
- Time allocations for each section (must add up to the total duration)
- A clear objective for each section
- A final section for next steps and owners

Keep it practical and focused. Do not pad with unnecessary items.
```

## Example input

- Purpose: Align on Q3 product priorities and decide which features to cut
- Duration: 60 minutes
- Attendees: Product manager, engineering lead, design lead, CEO

## Example output

```
Meeting Title: Q3 Product Priorities Alignment

[ 5 min]  Welcome and context setting
[20 min]  Review of current Q3 feature list — PM presents, open for questions
[20 min]  Discussion: which features to cut or defer, decision criteria
[10 min]  Final decisions and prioritised list confirmation
[ 5 min]  Next steps and owners

Objective: Leave the meeting with a confirmed Q3 scope that the full team has agreed on.
```

## When to use

Use this prompt before scheduling a meeting to ensure the time is well structured and attendees know what to expect.

## Tips

- Be specific about the purpose — vague inputs produce generic agendas
- Include the decision-maker in the attendees list so the agenda reflects their role
- For recurring meetings, adjust the duration to match your usual slot