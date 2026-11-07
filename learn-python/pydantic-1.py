#  A product model. Create a Product model with a name of at least 2 characters, 
# 'valid product and print it. Then try a price of -50, then a blank name, and print each error's 
# field and message.

from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    name : str = Field(min_length=2, max_length=20)
    price : int = Field(gt= 0)
    in_stock: bool = True

validProduct = Product(name = "box", price=4500)
print(validProduct)

try:
    invalidProduct = Product(name = "box", price=-4500)
    print(invalidProduct)
except ValidationError as error:
    for problem in error.errors():
        print(f"{problem["loc"][0]} -> {problem["msg"]}")

try:
    blankProduct = Product(name = "", price=4500)
    print(blankProduct)
except ValidationError as error:
    for problem in error.errors():
        print(f"{problem["loc"][0]} -> {problem["msg"]}")
        
