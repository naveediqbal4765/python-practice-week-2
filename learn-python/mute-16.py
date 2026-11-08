# 2. Replacing isn't changing. Predict what both print calls show, then run it:

# Copy

# The cart is a list, so why didn't empty_cart() empty it? '
# 'What's the difference between cart = [] and cart.append(...) inside a function?

def rename(customer):
    customer = "Bilal Traders"


def empty_cart(cart):
    cart = []


name = "Noor Foods"
rename(name)
print(name)

cart = ["rice", "oil"]
# print(empty_cart(cart))
print(cart)

# both funcs calls None cz the fuctions are exexuting but they dont print or return anything
# cart = [] is just initializing a variable in scope of function as list, python takes it like local var
# while cart.append() adds values to a list named cart