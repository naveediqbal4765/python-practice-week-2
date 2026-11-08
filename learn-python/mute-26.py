# 3. A tuple that can change. Predict what this prints and where it fails, then run it:

# Tuples can't change, so how did "DHA" get in? Why does Python refuse this tuple as a key 
# when it accepted ("Karachi", "Clifton") in the example? Fix it so branch can be used as a key.

# branch = ("Karachi", ["Clifton", "Saddar"])
branch = ("Karachi", "Clifton", "Saddar")
# branch[1].append("DHA")
print(branch)

stock = {branch: 12}
print(stock)

# we didnt change the tuple, we just changed an element inside the nested list in tuple, so the structire of tuple
# remained same, python refuses this tuple as key because it got a list in it (TypeError: cannot use 'tuple' as a dict key (unhashable type: 'list'))