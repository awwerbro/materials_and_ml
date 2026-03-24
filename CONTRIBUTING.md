# Contributing

## How to edit this repository

1. **Fork** the repository on GitHub.
2. Make your changes to the relevant markdown file.
3. Open a **pull request** with a short description of what you changed.

## Guidelines for humans

- Feel free to edit any file, any time through pull requests. We trust your judgment.

## Guidelines for agents

- Keep text minimal. Edit existing content rather than adding new sections unless necessary.
- Use plain markdown. No HTML, no special extensions.
- Limit adjectives and avoid embellishments.
- For meeting notes, update [meetings.md](meetings.md).

## File structure

```
README.md               — overview and navigation
CONTRIBUTING.md         — this file
events.md               — upcoming and past events
packages.md             — useful software packages
mailinglist.md          — mailing list info
meetings.md             — meeting calendar (upcoming and past)
related_initiatives.md  — related communities and projects
code/
  README.md             — contribution requirements
  <name>/               — one subfolder per contribution
    README.md
    notebook or script
    data (if needed)
```

## Adding a meeting

Add a row to the `Upcoming` table in `meetings.md`. After the meeting, move the row to `Past` and add a link to any notes committed to the repository.
