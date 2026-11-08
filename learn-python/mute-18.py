# 1. Predict the output. What do both print calls show? Predict first, then run it:

# Copy
# prices = [850, 1200]
# prices_copy = prices.copy()
# prices_copy.append(400)
# print(prices)

# price_lists = [[850, 1200], [400]]
# lists_copy = price_lists.copy()
# lists_copy[0].append(3100)
# print(price_lists)
# Both use .copy(). Why did the first original stay the same while the second changed?

prices = [850, 1200]
prices_copy = prices.copy()
prices_copy.append(400)
print(prices)

price_lists = [[850, 1200], [400]]
lists_copy = price_lists.copy()
lists_copy[0].append(3100)
print(price_lists)

# original staayed same because it copied all the items via shallow copy, 
# while the second one needs deep copy because its a nested list and the values of nested 
# elements share the same address