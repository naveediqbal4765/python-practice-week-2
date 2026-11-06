# 3. A missing file. Create orders.json containing a list of two orders. 
# Write load_orders(path) that returns the list of orders in a JSON file, 
# or an empty list with a warning if the file doesn't exist. 
# Test it with orders.json and with missing.json. Neither call should crash.

import json

with open("orders.json", "w") as file:
        json.dump([{"id": "Noor Foods", "status" : "pending"},
                    {"id": "Bilal Foods", "status" : "delivered"} ], file, indent = 2)
def load_orders(path):
    try: 
        with open(path) as file:
            return (json.load(file))

    except FileNotFoundError:
        return ("File not found")

print(load_orders("orders.json"))
print(load_orders("missing.json"))