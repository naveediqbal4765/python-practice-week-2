# 3. A fix that isn't quite right. Someone fixed the trap by writing if not cart instead of if cart is None. 
# Predict what this prints, then run it:

# Copy
# Look up what not does with an empty list. Why did rice never reach my_cart? Fix the function, and explain why is None is the right check here.

def add_item(item, cart=None):
    if cart is None:
#   if not cart:    
        cart = []
    cart.append(item)
    return cart


my_cart = []
add_item("rice", my_cart)
print(my_cart)

# as condition was not cart, so the condition was false, cart was initializes inside the condition scope
# it appended nothing an returned an empty cart