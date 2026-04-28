# Onboarding Guide Generator

Generate a structured onboarding plan for a new team member based on their role and team context.

## Prompt

```
You are an assistant that helps managers and team leads onboard new team members effectively.

Create a one-week onboarding plan based on the following details:

New team member name: {name}
Role: {role}
Team: {team}
Key tools and systems they will use: {tools}
Main contacts they should meet: {contacts}

Format the plan day by day (Monday to Friday) with:
- A focus theme for each day
- Two to four specific activities or meetings for that day
- One clear goal the new team member should achieve by end of day

Keep it practical and welcoming. Avoid overwhelming the first day.
```

## Example input

- Name: Sara
- Role: Business Analyst
- Team: Nordic Claims Unit
- Tools: Microsoft Teams, Excel, SharePoint, Power BI
- Contacts: Team lead, IT support, HR, two senior analysts

## Example output

```
Onboarding Plan — Sara, Business Analyst, Nordic Claims Unit

Monday — Orientation
- Meet with HR to complete paperwork and review policies
- Set up access to Teams, SharePoint, and Power BI with IT support
- Introductory call with team lead to discuss the role and first-week expectations
Goal: Accounts and tools set up and ready to use by end of day

Tuesday — Team and context
- 30-minute intro calls with two senior analysts
- Review the team's SharePoint documentation and recent reports
- Shadow a team standup meeting
Goal: Understand the team's current priorities and how the unit is structured

Wednesday — Tools and workflows
- Walkthrough of Power BI dashboards with a senior analyst
- Review two recent Excel reports to understand data sources and formats
- Identify any access gaps and flag to IT
Goal: Comfortable navigating the main data tools and reports

Thursday — First contribution
- Review one live project or ongoing analysis
- Draft a short summary of findings or observations from the week
- Share summary with team lead for feedback
Goal: Produce a first piece of work, however small

Friday — Reflection and alignment
- Review feedback from team lead on Thursday's summary
- List open questions and schedule follow-ups for next week
- End-of-week check-in with team lead
Goal: Clear picture of priorities for week two
```

## When to use

Use this prompt when a new team member is joining and you want to give them a structured, welcoming first week without spending hours planning it manually.

## Tips

- Adjust the pace based on the complexity of the role — technical roles may need more tool setup time early on
- Include social touchpoints (team lunch, informal coffee chats) to help the new person feel welcome
- Share the plan with the new team member before their first day so they know what to expect