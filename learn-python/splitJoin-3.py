# Showing a sum. Using totals = [4500, 12800, 2300], try " + ".join(totals) and read the error. 
# Fix it by building a list of strings first, so that it prints 4500 + 12800 + 2300 = 19600, 
# with the total calculated by your code.

totals = [4500, 12800, 2300]

# total = "+".join(totals)
# error: TypeError: sequence item 0: expected str instance, int found 

newList = []
for x in totals:
    newList.append(str(x))

newList = "+".join(newList)

print(f"{newList} = {sum(totals)}")