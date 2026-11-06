# Finding an order. Write find_order(orders, order_id) with full type hints. 
# It should return the matching order, or None if there isn't one. Test it with both cases:

orders = [
    {"id": "A101", "status": "pending"},
    {"id": "A102", "status": "delivered"},
]


def find_order(orders: list[dict[str, str]], order_id: str) -> dict[str, str] | None:
    for order in orders:
        if order["id"] == order_id:
            return order
        
    return None


print(find_order(orders, "A101")) 
print(find_order(orders, "8689"))   