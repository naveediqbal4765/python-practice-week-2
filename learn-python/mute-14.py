# 3. When it doesn't happen. Predict what both print calls show, then run it:

# Copy
city = "Karachi"
branch = city
branch = branch + " Branch"
print(city)

orders = [4500]
report = orders
report = report + [2300]
print(orders)
# Neither original changed. Why not, when append() in problem 1 did change the original?
#neither original changed because + creates a new object in both cases
#append() works in mutable variables not strings, ints 