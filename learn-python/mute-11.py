# 2. Unpacking. Look up tuple unpacking, for example item, quantity, price = line. 
# Then loop over this list of order lines, unpack each one, and print the order total (expected: 5480):

lines = [("Rice", 2, 1450), ("Oil", 1, 2100), ("Sugar", 3, 160)]

total = 0
for line in lines:
    lineTotal = line[1] * line[2]
    total += lineTotal 

print(total)