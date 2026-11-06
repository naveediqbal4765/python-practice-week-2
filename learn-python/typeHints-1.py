# Add the hints. Add type hints to these functions, then run them to check they still work:


def format_rupees(amount: int) -> str:
    return f"Rs {amount:,}"


def is_large(total: int, limit: int=10000) -> int:
    return total >= limit


def total_sales(sales: list[int]) -> int:
    return sum(sales)

print(format_rupees(399))
print(is_large(43))
print(total_sales([45,65,77,32,23]))

# yes they all work