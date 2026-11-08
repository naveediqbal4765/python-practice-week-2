# 2. Dictionaries change too. Start with stock = {"pens": 120, "notebooks": 45}. 
# Record a sale of 20 pens, add "markers" with 60 in stock, then look up the del keyword and 
# remove "notebooks". Print the dictionary (expected: {'pens': 100, 'markers': 60}).

stock = {"pens": 120, "notebooks": 45}
stock["pens"] -= 20
stock["markers"] = 60

del stock["notebooks"]
print(stock)