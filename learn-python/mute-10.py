# 1. An order line. Store one order line as a tuple: line = ("Rice", 2, 1450), 
# meaning the item, the quantity and the unit price. Using indexes, print 2 x Rice = Rs 2,900. 
# Then try to change the quantity to 3 and read the error. Create a new tuple with the new quantity instead.

line = ("Rice", 2, 1450)
print(f"2 x {line[0]} = Rs {2 * line[2]}")

# line[1] = 3
# print(line) TypeError: 'tuple' object does not support item assignment

newLine = (line[0], 3, line[2])
print(newLine)