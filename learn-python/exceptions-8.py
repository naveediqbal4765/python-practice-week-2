# 3. Adding information. Each line below holds an order ID and a total, separated by a comma:

# Copy
# lines = ["A101,4500", "A102,abc", "A103,2300"]
# Write load_totals(lines), which returns a list of the totals as whole numbers. Use .split(",") 
# to separate each line. If a total can't be converted, raise a ValueError that names the line number and 
# the bad value, using from error. Look up enumerate() to get line numbers starting from 
# 1. Call the function inside a try statement, so that it prints:

# Could not load file: line 2: total 'abc' is not a whole number
# Then remove the bad line and check that it prints [4500, 2300]. 
# What would the error have told you without your extra information?

lines = ["A101,4500", "A102,abc", "A103,2300"]
newList = []
def load_totals(lines):
   
    for x, line in enumerate(lines):
        strID, total = lines.split(",")
    try:
        convert = int(total)
        newList.append(convert)
        print(newList)
    except ValueError:
         return ("not a number")
         

    try:
        print(load_totals(lines))
    except ValueError as error:
        print(f"{error}")
