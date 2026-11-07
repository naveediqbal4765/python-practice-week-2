# Checking a file of rows. Using your Order model from this page, check each row below. 
# Keep the valid orders in a list, and print a line for each bad row that names the row number and 
# the fields with problems:
from enum import StrEnum

from pydantic import BaseModel, Field, ValidationError


class OrderStatus(StrEnum):
    PENDING = "pending"
    DELIVERED = "delivered"


class Order(BaseModel):
    id: str
    customer: str
    total: int = Field(gt=0)
    status: OrderStatus = OrderStatus.PENDING

rows = [
    {"id": "A101", "customer": "Noor Foods", "total": 4500},
    {"id": "A102", "customer": "Bilal Traders", "total": -200},
    {"id": "A103", "total": 2300},
    {"id": "A104", "customer": "Karachi Crafts", "total": "7600", "status": "delivered"},
    {"id": "A105", "customer": "Zara Textiles", "total": 3900, "status": "lost"},
]

cleaned = []
total = 0
valid = 0
for indx, row in enumerate(rows, start= 1):
    total += 1  
    try:
        order= Order.model_validate(row)
        cleaned.append(order.model_dump())
        valid += 1
    except ValidationError as error:
        for problem in error.errors():
            print(f"Row {indx} rejected: {problem["loc"][0]}")
        
print(f"{valid} of {total} orders are valid")