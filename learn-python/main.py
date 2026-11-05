raw_orders = [
    {"customer": " noor foods ", "status": "Delivered", "paid": 1},
    {"customer": "BILAL TRADERS", "status": " pending ", "paid": 0},
    {"customer": "noor foods", "status": "PENDING", "paid": 0},
]

orders = []

for order in raw_orders:
    orders.append(
        {
            "customer": order["customer"].strip().title(),
            "status" : order["status"].lower().strip(),
            "paid": bool(order["paid"])
        }
    )

print(orders)

customers = set()

for x in orders:
    customers.add(x["customer"])

print(sorted(customers))