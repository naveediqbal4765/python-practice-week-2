# 2. Validating orders. Write validate_order(order) that raises a ValueError with a clear message 
# when an order has no id, a total that isn't a number or isn't more than 0, or a status that 
# isn't "pending", "delivered" or "cancelled". Look up isinstance() to check for numbers. 
# Then loop over this list, catch each error and print it:

def validate_order(order):
    if "id" not in order:
        raise ValueError(f"Order {index}: missing id")
    elif not isinstance(order["total"], int):
        raise ValueError(f"Order {order["id"]}: total must be a number")
    elif int(order["total"]) < 0:
        raise ValueError(f"{order["id"]} total must be more than 0")
    elif order["status"] != "pending" and order["status"] != "delivered" and order["status"] != "cancelled":
        raise ValueError(f"{order["id"]}: unknown status {order["status"]} ")
    
    return order        


orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": -200, "status": "pending"},
    {"total": 2300, "status": "delivered"},
    {"id": "A104", "total": "7600", "status": "delivered"},
    {"id": "A105", "total": 3900, "status": "lost"},
    {"id": "A106", "total": 6100, "status": "pending"},
]

valid = 0
total = 0
for index, order in enumerate(orders, start=1):
    total += 1 
    try:
        validate_order(order)
        valid += 1
    except ValueError as error:
        print(error)
        
print(f"{valid} out of {total} are valid\n")

