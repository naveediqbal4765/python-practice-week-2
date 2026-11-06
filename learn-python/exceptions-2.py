# 2. Checking quantities. Loop over these inputs, 
# as if typed by customers: ["12", "abc", "-3", "5", "2.5"]. 
# For each one, print Quantity: 12, Skipping 'abc': not a whole number or 
# Skipping '-3': must be more than 0. At the end, print the total of the valid quantities (expected: 17).

customers = ["12","abc", "-3", "5", "2.5"]

total = 0
for x in customers:
    try:
        quantity = int(x)
        if quantity < 0:
            print(f"skipping {x}: must be more than 0")
            continue

        print(f"Quantity: {quantity}")
        total += quantity

    except ValueError:
        print(f"skipping {x}: is not a whole number")

print(f"Total: {total}")

    