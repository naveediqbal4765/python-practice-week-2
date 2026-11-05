# stock = {"pens": 120, "notebooks": 45, "staplers": 8}
# 1. Total stock. Use .values() to add up all the stock with a loop (expected: 173). 
# Then replace your loop with sum().
stock = {"pens": 120, "notebooks": 45, "staplers": 8}

stockTotal = 0

for x in stock.values():
    stockTotal += x

print(f"Total: {stockTotal}")

total = sum(stock.values()) 
print(f"Total: {total}")

