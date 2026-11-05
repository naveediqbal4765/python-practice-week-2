# 2. Low stock. Use .items() to print every product with fewer than 50 in stock:

stock = {"pens": 120, "notebooks": 45, "staplers": 8}

for key, value in stock.items():
    if value < 50:
        print(f"low stock: {key} ({value})")