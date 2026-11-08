# 4. One template, two orders (example 5). What does this print? Predict it first:


# Fix it so it prints 4500 12800 0, changing only the two lines that create the orders.


template = {"status": "pending", "total": 0}

order_a = template.copy()
order_a["total"] = 4500

order_b = template.copy()
order_b["total"] = 12800

print(order_a["total"], order_b["total"], template["total"])