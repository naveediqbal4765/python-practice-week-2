# 2. Same list or a copy? Run this and explain each result:

# Copy
# a = [4500, 12800]
# b = a
# c = a.copy()
# print(id(a) == id(b), id(a) == id(c))
# Then look up Python's is operator and rewrite the last line to use it instead of comparing id() values.

a = [4500, 12800]
b = a
c = a.copy()
print(id(a) == id(b), id(a) == id(c))

# as a and b variables pointing at same id they print true, and c made a copy the values are copied to
# another ,thats the reason it prints False

print(a is b, a is c)