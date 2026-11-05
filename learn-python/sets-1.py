# 1. Unique cities. Using ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"], 
# print how many different cities there are (expected: 3) and then the cities in alphabetical order.


cities = ["Karachi", "Lahore", "Karachi", "Multan", "Lahore"]
uniqueCities = set(cities)

print (f"different cities: {len(uniqueCities)}")
print(f"Sorted: {sorted(uniqueCities)}")