# 1. Editing a cart. Start with cart = ["rice", "oil"]. 
# Add "sugar" to the end, replace "oil" with "ghee" using its position, 
# then look up the .remove() method and remove "rice". Print the cart (expected: ['ghee', 'sugar']).

cart = ["rice", "oil"]
cart.append("sugar")
cart[1] = "ghee"
cart.remove("rice")
print(cart)