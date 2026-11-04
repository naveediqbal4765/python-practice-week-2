# Counting tickets by priority. Using the TaskPriority enum from this page, 
# count how many tickets there are at each priority:

# Start with a dictionary that has every priority as a key and 0 as its count, 
# built by looping over TaskPriority, not typed by hand. 
# Then convert each ticket's priority to the enum and add 1 to its count. E


from enum import StrEnum, auto


class taskPriority(StrEnum):
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

priority = {}

for x in taskPriority:
    priority[x.value] = 0

for x in tickets:
 if x["priority"] not in priority:
    print(f"{x["id"]}: unknown priority {x["priority"]}")

 else:
    priority[x["priority"]] +=1 
    

for key, value in priority.items():
   print(f"{key}: {value}")
 
# expected output:
# Copy
# T4: unknown priority 'critical'
# low: 1
# medium: 1
# high: 2
# urgent: 1
