# 1. Predict the output. What does this print?

# Copy
# def close_order(order):
#     order["status"] = "closed"


# order = {"id": "A101", "status": "pending"}
# close_order(order)
# print(order["status"])
# Now write closed_copy(order), which returns a closed copy of the order and 
# leaves the original as pending. Print both to check.

# def close_order(order):
#     order["status"] = "closed"

def closed_copy(order):
    copiedOrder = order.copy()
    copiedOrder["status"] = "closed"

    return copiedOrder["status"]

order = {"id": "A101", "status": "pending"}
# close_order(order)
print(order["status"])
print(closed_copy(order))