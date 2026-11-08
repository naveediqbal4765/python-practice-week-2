# 2. Looking up prices. Prices are stored by product and size, but the order arrives from JSON, 
# which has no tuples, so each item is a list:

# Loop over items and try prices[item]. Read the error. Then look up the built-in tuple() function, 
# use it to convert each item, and print the order total (expected: 4900).


prices = {("Rice", "5kg"): 1450, ("Rice", "10kg"): 2800, ("Oil", "1L"): 650}
items = [["Rice", "10kg"], ["Oil", "1L"], ["Rice", "5kg"]]

total = 0
for item in items:
    item = tuple(item)
    total += prices[item]

print(total)
