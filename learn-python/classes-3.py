# 3. Payments with a rule. Create an Order class with customer and total attributes, 
# and a paid attribute that starts at 0. Give it three methods:

# remaining() returns how much is still owed.
# is_paid() returns True when nothing is owed.
# pay(amount) adds amount to paid, but first raises a ValueError if amount is more than what's still owed.

class Order:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total 
        self.paid = 0

    def remaining(self):
        return self.total - self.paid
    
    def is_paid(self):
        if self.remaining() == 0:
            return True

    def pay(self, amount):
        if amount <= self.remaining(): 
            self.paid += amount
        else:
            raise ValueError(f"ValueError: {self.customer} owes Rs {self.remaining()}, can't pay Rs {amount}")
               
order = Order("Noor Foods", 4500)

order.pay(2000)
print(order.remaining())

order.pay(2500)
print(order.is_paid())

try:
 order.pay(100)
except ValueError as error:
    print(f"{error}")