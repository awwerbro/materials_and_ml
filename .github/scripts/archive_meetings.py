#!/usr/bin/env python3
"""Move past meetings from the Upcoming table to the Past table in meetings.md."""

import re
import sys
from datetime import date

MEETINGS_FILE = "meetings.md"
today = date.today()


def is_separator(line):
    return bool(re.match(r"^\|[\s\-|:]+\|$", line.strip()))


def parse_date(cell):
    try:
        return date.fromisoformat(cell.strip())
    except (ValueError, AttributeError):
        return None


with open(MEETINGS_FILE) as f:
    lines = f.read().split("\n")

section = None
to_move = []
new_lines = []
archived = 0

i = 0
while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped == "## Upcoming":
        section = "upcoming"
        new_lines.append(line)
        i += 1
        continue
    elif stripped == "## Past":
        section = "past"
        new_lines.append(line)
        i += 1
        continue

    # Collect upcoming data rows whose date has passed
    if section == "upcoming" and stripped.startswith("|") and not is_separator(stripped):
        cells = [c.strip() for c in stripped.split("|")[1:-1]]
        if cells:
            row_date = parse_date(cells[0])
            if row_date is not None and row_date < today:
                to_move.append(cells)
                i += 1
                continue

    new_lines.append(line)

    # Insert moved rows immediately after the Past table separator
    if section == "past" and is_separator(stripped) and to_move:
        for cells in to_move:
            while len(cells) < 4:
                cells.append("")
            new_lines.append("| " + " | ".join(cells[:4]) + " |")
            archived += 1
        to_move = []

    i += 1

with open(MEETINGS_FILE, "w") as f:
    f.write("\n".join(new_lines))

print(f"Archived {archived} meeting(s).")
if archived == 0:
    sys.exit(0)
