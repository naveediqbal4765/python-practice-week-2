# Best three days. Using sales = [18500, 22300, 19800, 25400, 31200], print the three highest values,
# biggest first (expected: [31200, 25400, 22300]), and leave sales in its original order.
# Look up list slicing, and print sales at the end to prove it hasn't changed.

sales = [18500, 22300, 19800, 25400, 31200]

bestDays = sorted(sales)
bestDays.reverse()

print(sales)
print(bestDays[:3])