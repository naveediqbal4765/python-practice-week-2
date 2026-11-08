# 3. Change or return. Write two functions and test both on the same starting cart:

# add_item(cart, item) adds the item to the cart itself and returns nothing.
# with_item(cart, item) returns a new cart with the item added and leaves the original unchanged.
# Print the cart after each call to prove which one changed it. 
# Write a comment explaining how each function's name tells the caller what to expect.

def add_item(cart, item):
    cart.append(item)          

def with_item(cart, item):
    cart = cart.copy()
    cart.append(item)
    return cart

cart = ["rice", "oil"]

# print(add_item(cart, "sugar"))
# print(cart)

print(with_item(cart, "sugar"))
print(cart)