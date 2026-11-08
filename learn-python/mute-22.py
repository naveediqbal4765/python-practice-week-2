# 2. Counting items. This function is meant to start a new count on each call 
# unless you pass in your own dictionary. Run it and explain the output:

# Fix it so it prints {'rice': 1} and then {'oil': 1}. 
# Then check that passing your own dictionary still works: 
# calling count_item("rice", shop) twice with shop = {} should leave shop as {'rice': 2}.

def count_item(item, counts=None):
    if counts is None:
        counts = {}
    
    if item not in counts:
        counts[item] = 0
    counts[item] += 1

    return counts


print(count_item("rice"))
print(count_item("oil"))

shop = {}

count_item("rice", shop)
count_item("rice", shop)
print(shop)   