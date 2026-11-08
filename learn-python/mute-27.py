# 1. Predict the output (examples 1 and 2). What does this print, and why?

# Copy
city = " lahore "
city.strip()
tags = ["new"]
tags.append("vip")
print(f"[{city}]", tags)

# [ lahore ] ['new', 'vip'] , didnt strip the city, because strip was executing but didnt returned the
# result to any variable as strings are immutable so it didnt change, lists are mutable so append func worked