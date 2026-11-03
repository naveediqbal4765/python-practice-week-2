# Payment methods. Create a StrEnum called PaymentMethod with the options CASH, 
# CARD and BANK_TRANSFER, using auto(). Loop over it and print each option. 
# Then print whether PaymentMethod.CARD == "card"

from enum import StrEnum, auto


class PaymentMethod(StrEnum):
        CASH = auto()
        CARD = auto()
        BANK_TRANSFER = auto()

for payment in PaymentMethod:
        print(payment)

print(PaymentMethod.CASH)
