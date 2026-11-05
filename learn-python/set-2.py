# 2. Duplicate orders. An export contains some orders twice. Start with seen = set(), 
# loop over the list, and print a line for each repeat. If an ID isn't a repeat, add it to seen:


order_ids = ["A101", "A102", "A101", "A103", "A102"]

seen = set()

for orders in order_ids:
    if orders not in seen:
        seen.add(orders)
    else:
        print(f"Duplicate: {orders}")

print(sorted(seen))
