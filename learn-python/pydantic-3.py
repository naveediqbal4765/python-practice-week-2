# 3. A nested model. A field's type can be another model. Create a Line model with item, '
# 'quantity and unit_price, and an Invoice model with customer and lines: list[Line]. '
# 'Add a method total() to Invoice that adds up each line's quantity times its unit price. 
# Check it with this data, then print Noor Foods: Rs 5,480:
from pydantic import BaseModel, ValidationError


class Line(BaseModel):
    item: str
    quantity: int
    unit_price: int

class Invoice(BaseModel):
    customer: str
    lines: list[Line]
    def total(self):
        result = 0
        for addUp in self.lines:
            result += addUp.unit_price * addUp.quantity
        return result


data = {
    "customer": "Noor Foods",
    "lines": [
        {"item": "Rice", "quantity": 2, "unit_price": 1450},
        {"item": "Oil", "quantity": 1, "unit_price": 2100},
        {"item": "Sugar", "quantity": 3, "unit_price": 160},
    ],
}

invoice = Invoice.model_validate(data)
print(f"{invoice.customer}: {invoice.total()}")


# Now change one line's quantity to "many". What does the error's loc show, 
# and how does that help you find the problem?

invalidData= data["lines"][1]["quantity"]= "many"

try:
    invoice = Invoice.model_validate(invalidData)
except ValidationError as error:
    for prob in error.errors():
        print(f"{prob}")

# error: {'type': 'int_parsing', 'loc': ('lines', 1, 'quantity'), 
# 'msg': 'Input should be a valid integer, unable to parse string as an integer',
#  'input': 'many', 'url': 'https://errors.pydantic.dev/2.14/v/int_parsing'}