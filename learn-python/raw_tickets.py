# A support inbox exported these tickets:

# Copy
# raw_tickets = [
#     {"title": " refund not received ", "priority": "High", "open": 1},
#     {"title": "late delivery", "priority": " urgent ", "open": 0},
#     {"title": "WRONG ITEM SENT", "priority": "MEDIUM", "open": 1},
#     {"title": "Late delivery ", "priority": "low", "open": 1},
# ]
# Write a function clean_tickets(raw_tickets) that returns a new list,
# with each title stripped and in sentence case (look up .capitalize()), 
# each priority stripped and in lowercase, and open as True or False. Then use it to print:

raw_tickets = [
    {"title": " refund not received ", "priority": "High", "open": 1},
    {"title": "late delivery", "priority": " urgent ", "open": 0},
    {"title": "WRONG ITEM SENT", "priority": "MEDIUM", "open": 1},
    {"title": "Late delivery ", "priority": "low", "open": 1},]


def cleanTickets(raw_tickets):
    newList = []
    for tickets in raw_tickets:
      newList.append(
            {
                "title" : tickets["title"].strip().capitalize(),
                "priority" : tickets["priority"].lower(),
                "open" : bool(tickets["open"])
            }
        )
    return newList

print(cleanTickets(raw_tickets))