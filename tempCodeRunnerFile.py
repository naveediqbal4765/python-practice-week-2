from enum import StrEnum, auto


class PaymentMethod(StrEnum):
        CASH = auto()
        CARD = auto()
        BANK_TRANSFER = auto()

for payment in PaymentMethod:
        print(payment)

print(PaymentMethod.CARD)
