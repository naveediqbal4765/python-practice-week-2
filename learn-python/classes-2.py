class Order:
    currency = "Rs"

    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def label(self):
        return f"{self.customer}: {self.currency} {self.total}"


a = Order("Noor Foods", 4500)
b = Order("Bilal Traders", 12800)

print(a.label())
Order.currency = "PKR"
print(b.label())
print(a.label())
# Which attributes belong to each order, and which one is shared?
# customer and total belong to each value, and currency is shared