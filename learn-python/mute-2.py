# 2. Cleaning names. Loop over [" amna ", "BILAL", " zara khan"] and 
# build a new list of cleaned names using .strip() and .title().
# Print it (expected: ['Amna', 'Bilal', 'Zara Khan']). 

names = [" amna ", "BILAL", " zara khan"]
cleaned = []

for name in names:
    cleaned.append(name.strip().title())

print(cleaned)

# Why do you need a new list instead of changing each string where it is?
# Strings are immutable so strip and title cant change the original