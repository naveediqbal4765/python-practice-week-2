# 1. Which keys work? Predict which of these lines fail, then run them. 
# An error stops the script, so comment out each failing line to reach the next one:

# Copy
# a = {"A101": "pending"}
# b = {42: "pending"}
# c = {(24.86, 67.01): "Karachi warehouse"}
# d = {["rice", "oil"]: 2}
# e = {{"id": "A101"}: "pending"}
# What do the keys that work have in common?

a = {"A101": "pending"}
b = {42: "pending"}
c = {(24.86, 67.01): "Karachi warehouse"}
d = {["rice", "oil"]: 2} #TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
e = {{"id": "A101"}: "pending"} #TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')

# string, int, and tuple keys work

