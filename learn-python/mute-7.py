# 1. Predict the result. Predict whether each print shows True or False, then run it:

# Copy
status = "pending"
before = id(status)
status = status.upper()
print(id(status) == before)

order = {"status": "pending"}
before = id(order)
order["status"] = "delivered"
print(id(order) == before)