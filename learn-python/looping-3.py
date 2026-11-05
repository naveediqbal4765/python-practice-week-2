# Orders by customer. Each customer's value is a list of order totals. Loop over the dictionary 
# and print one line per customer:

orders = {
    "Noor Foods": [4500, 2300],
    "Bilal Traders": [7600],
    "Karachi Crafts": [12800, 3900],
}

for key, value in orders.items():
    total = sum(value)
    print(f"{key}: {len(value)} order(s), Rs {total:,}")
