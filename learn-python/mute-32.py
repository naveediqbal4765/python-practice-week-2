# 6. A branch copy (example 7). Noor Foods is opening a Lahore branch, 
# and you want to start its record as a copy of the main one:

# Predict which of the three changes also show up in customer, then run it. 
# Fix it with deepcopy() so customer stays exactly as it started, and explain 
# why changing name was safe even with .copy().
import copy
customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "tags": ["wholesale"],
}

branch = copy.deepcopy(customer)
branch["name"] = "Noor Foods Lahore"
branch["address"]["city"] = "Lahore"
branch["tags"].append("new")
print(customer)

#as it was shallow copied to branch dict, but nested dict and list needed deepcopy (both dicts 
# were sharing the same add)