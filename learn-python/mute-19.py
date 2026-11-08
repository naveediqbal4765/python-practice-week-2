# 2. A test run. You want to try out a status change without touching the real orders. 
# Predict what this prints, then run it:

# Copy
# orders = [
#     {"id": "A101", "status": "pending"},
#     {"id": "A102", "status": "pending"},
# ]

# test_orders = orders.copy()
# for order in test_orders:
#     order["status"] = "delivered"

# print(orders)
# Which object did .copy() create, and which objects are still shared? 
# Fix it so orders stays pending while test_orders becomes delivered.
import copy

orders = [
    {"id": "A101", "status": "pending"},
    {"id": "A102", "status": "pending"},
]

test_orders = copy.deepcopy(orders)
for order in test_orders:
    order["status"] = "delivered"

print(orders)
print(test_orders)

# copy created the list elements(dictionaries), as it was a shallow copy, but didnt copy the dictionaries elements cz they were nested in list