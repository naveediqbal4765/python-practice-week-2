# 2. Same object or new one? (example 3). 
# Predict whether each print shows True or False, then run it:

# Copy
name = "Noor"
before = id(name)
name += " Foods"
print(id(name) == before) #strings are immutable so it made a new id

items = ["rice"]
before = id(items)
items += ["oil"]
print(id(items) == before) #here += extended the list and added the item address remained same

items = items + ["sugar"]
print(id(items) == before) #right side was executed first, and during execution it made a new object
# The last two look almost the same. 
# Why do they give different answers? Which one changed the existing list, and which one built a new list?