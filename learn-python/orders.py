def apply_discount(total, rate):
    if rate < 0 or rate > 1:
        raise ValueError(f"Discount rate must be between 0 and 1, got {rate}")
    return total - total * rate


def is_large(total):
    """An order of Rs 10,000 or more is large."""
    return total > 10000
