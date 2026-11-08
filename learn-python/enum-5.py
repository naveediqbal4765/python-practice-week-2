# 5. Overdue tasks. Each task below has a status and a due date, as text:

# Copy
# tasks = [
#     {"name": "Send invoices", "status": "done", "due": "2026-10-28"},
#     {"name": "Update price list", "status": "in_progress", "due": "2026-10-30"},
#     {"name": "Call Noor Foods", "status": "planned", "due": "2026-11-05"},
#     {"name": "Fix delivery report", "status": "blocked", "due": "2026-10-31"},
# ]
# Using the TaskStatus enum from this page, print every task that is not done and 
# whose due date has passed, with how many days overdue it is. Look up date.fromisoformat() 
# to turn the text into a date. Subtracting one date from another gives you a gap of time: look up its
# .days attribute. To get the expected output, use today = date(2026, 11, 2) instead of date.today():

from datetime import date
from enum import StrEnum, auto

tasks = [
    {"name": "Send invoices", "status": "done", "due": "2026-10-28"},
    {"name": "Update price list", "status": "in_progress", "due": "2026-10-30"},
    {"name": "Call Noor Foods", "status": "planned", "due": "2026-11-05"},
    {"name": "Fix delivery report", "status": "blocked", "due": "2026-10-31"},
]

class TaskStatus(StrEnum):
    DONE = auto()
    IN_PROGRESS = auto()
    PLANNED = auto()
    BLOCKED = auto()

for task in tasks:
    dateCheck = date.fromisoformat(task["due"])
    today = date(2026, 11, 2)
    if task["status"] != TaskStatus.DONE and dateCheck < today:
        timeGape = today - dateCheck
        print(f"overdue by {timeGape.days} days: {task["name"]} ({task["status"]})")