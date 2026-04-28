# Decision Brief Generator

Summarize a complex decision into a structured one-page brief that can be shared with stakeholders or leadership before a meeting.

## Prompt

```
You are an assistant that helps professionals communicate decisions clearly to stakeholders.

Write a concise decision brief based on the following input:

Decision to be made: {decision}
Background: {background}
Options being considered: {options}
Recommendation (if any): {recommendation}

Format the brief with:
- Decision title
- Background: two to three sentences of context
- Options considered: a short description and the key trade-off for each option
- Recommendation: the suggested path forward with a one-sentence rationale
- Next step: what needs to happen to move forward

Keep the brief to one page. Use plain language. Avoid jargon.
```

## Example input

- Decision: Whether to migrate our data pipeline to a cloud-based solution or maintain the current on-premise setup
- Background: The current on-premise pipeline is reaching capacity and requires expensive hardware upgrades. The team has evaluated two cloud providers over the past month.
- Options: (1) Migrate to AWS — higher upfront cost, better scalability. (2) Stay on-premise — lower short-term cost, limited growth ceiling.
- Recommendation: Migrate to AWS

## Example output

```
Decision Brief: Data Pipeline Migration

Background
The current on-premise data pipeline is approaching capacity limits and will require
significant hardware investment to scale. Over the past month, the team evaluated
two alternatives to address this constraint.

Options Considered

Option 1 — Migrate to AWS
Higher upfront migration cost but provides elastic scalability, managed infrastructure,
and lower long-term operational overhead. Trade-off: requires a 3-month migration effort.

Option 2 — Stay on-premise
Lower short-term cost with no migration disruption. Trade-off: limited scalability ceiling
and ongoing hardware maintenance costs that will increase over time.

Recommendation
Migrate to AWS. The long-term scalability and reduction in operational overhead outweigh
the short-term migration cost, particularly given projected data growth over the next 18 months.

Next Step
Approve budget for migration in the Q3 planning cycle and assign a technical lead by May 15.
```

## When to use

Use this prompt when preparing for a decision-making meeting with leadership or when you need to communicate a complex trade-off clearly to non-technical stakeholders.

## Tips

- Be specific about the options — vague descriptions produce weak briefs
- Include a recommendation even if it is tentative — it makes the brief more actionable
- Keep the background short — the brief is not a full report, just enough context to make a decision