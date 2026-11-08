# 3. A price rise that doesn't work. This loop is meant to raise every price by 10%, '
# 'but the list doesn't change. Run it and explain why:

# prices = [850, 1200, 400]
# for price in prices:
#     price = price * 1.1
# print(prices)
# Look up range() and len() together, then rewrite the loop so it changes 
# each item in the list by its position. Use round() so it prints [935, 1320, 440].

prices = [850, 1200, 400]
for p in range(len(prices)):
    prices[p] = round(prices[p] * 1.1)

print(prices)