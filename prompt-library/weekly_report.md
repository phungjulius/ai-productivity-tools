# Weekly Status Report Generator

Turn a list of bullet points into a polished weekly status report suitable for sharing with a manager or leadership team.

## Prompt

```
You are an assistant that helps professionals communicate their weekly progress clearly.

Write a weekly status report based on the following notes:

Team or person: {name}
Week of: {week}
Raw notes: {notes}

Format the report with these sections:
- Summary: two sentences on the overall state of the week
- Completed: what was finished this week
- In progress: what is actively being worked on
- Blockers: anything slowing progress down (write "None" if there are none)
- Next week: top priorities for the coming week

Use plain, professional language. Do not invent details that are not in the notes.
```

## Example input

- Name: Julius Phung
- Week of: April 28, 2026
- Raw notes: finished the API integration, fixed two bugs from last sprint, still working on the dashboard filters, waiting on design review from Mia, next week need to finish filters and start on the export feature

## Example output

```
Weekly Status Report — Julius Phung — Week of April 28, 2026

Summary
A productive week with the API integration completed and two outstanding bugs resolved.
Progress on the dashboard filters is ongoing with one external dependency pending.

Completed
- API integration finalized and merged
- Two bugs from the previous sprint resolved

In Progress
- Dashboard filter implementation (ongoing)

Blockers
- Design review from Mia pending — needed before filters can be finalized

Next Week
- Complete dashboard filters once design review is received
- Begin work on the export feature
```

## When to use

Use this prompt every Friday to convert rough end-of-week notes into a clean report that can be sent directly to a manager or pasted into a team channel.

## Tips

- The rawer and more honest the notes, the better the output
- Include any blockers even if they feel minor — they are important context for leadership
- This prompt works well combined with the meeting summary prompt for a full weekly wrap-up