#  Capital letters first. Run print(sorted(["noor", "Bilal", "amna"])). 
# Why isn't the result alphabetical? Look up the key parameter of sorted() and use str.lower to get 
# ['amna', 'Bilal', 'noor']. Are the names themselves changed?

print(sorted(["noor", "Bilal", "amna"]))
# as we know the ascii code of capital letters is smaller than lower, sorted() turns the list in ascending
# order which is why it seems unsorted
sort = ["noor", "Bilal", "amna"]
cleaned = []
for x in sort:
    cleaned.append(x.lower())

print(sorted(cleaned))