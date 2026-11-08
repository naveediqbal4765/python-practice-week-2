# Counting tickets by priority. Using the TaskPriority enum from this page, 
# count how many tickets there are at each priority:

# Start with a dictionary that has every priority as a key and 0 as its count, 
# built by looping over TaskPriority, not typed by hand. 
# Then convert each ticket's priority to the enum and add 1 to its count.
from enum import StrEnum, auto


class TaskPriority(StrEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    URGENT = auto()


tickets = [
    {"id": "T1", "priority": "high"},
    {"id": "T2", "priority": "low"},
    {"id": "T3", "priority": "urgent"},
    {"id": "T4", "priority": "critical"},
    {"id": "T5", "priority": "high"},
    {"id": "T6", "priority": "medium"},
]

counts = {}
for priority in TaskPriority:
    counts[priority] = 0

for ticket in tickets:
    if ticket["priority"] not in counts:
        print(f"{ticket['id']}: unknown priority '{ticket['priority']}'")
        continue
    else:
        counts[TaskPriority(ticket["priority"])] += 1 

for key, value in counts.items():
    print(f"{key}: {value}") 

# expected output:
# T4: unknown priority 'critical'
# low: 1
# medium: 1
# high: 2
# urgent: 1
