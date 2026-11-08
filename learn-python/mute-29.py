# 3. Stock by branch (examples 4 and 9). 
# A shop keeps its stock in a dictionary with a (city, area) tuple as each key:


# Add a new branch, ("Lahore", "DHA"), with 25 in stock. 
# Then loop over stock.items() and add up the stock for every Karachi branch (expected: 42). 
# Use key[0] to get the city from each tuple. Finally, try to change the city inside one of the keys. 
# What error do you get, and why does Python stop you?

stock = {
    ("Karachi", "Clifton"): 12,
    ("Karachi", "Saddar"): 30,
    ("Lahore", "Gulberg"): 18,
}

stock[("lahore", "DHA")] =  25

total = 0
for key, value in stock.items():
    # key[0] = "blah" TypeError: 'tuple' object does not support item assignment
    if key[0].lower() == "karachi":
        total += value

print(total)
# tuples areeeeeee immutableeeee