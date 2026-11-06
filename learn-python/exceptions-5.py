# 2. Validating orders. Write validate_order(order) that raises a ValueError with a clear message 
# when an order has no id, a total that isn't a number or isn't more than 0, or a status that 
# isn't "pending", "delivered" or "cancelled". Look up isinstance() to check for numbers. 
# Then loop over this list, catch each error and print it:

def validate_order(order):
    if "id" not in order:
        raise ValueError(f"{order} aint got an id")
    elif order["total"] == isinstance(order["total"], int):
        raise ValueError(f"{order} this order aint got a number")
    elif int(order["total"]) < 0:
        raise ValueError(f"{order} this order is in minus")
    elif order["status"] != "pending" and order["status"] != "delivered" and order["status"] != "cancelled":
        raise ValueError(f"{order} has not a proper status")
    
    return order        


orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": -200, "status": "pending"},
    {"total": 2300, "status": "delivered"},
    {"id": "A104", "total": "7600", "status": "delivered"},
    {"id": "A105", "total": 3900, "status": "lost"},
    {"id": "A106", "total": 6100, "status": "pending"},
]

for order in orders:
    try:
        print(validate_order(order))
    except ValueError as error:
        print(error)
        

