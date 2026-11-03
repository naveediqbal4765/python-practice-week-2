# A safe discount. Write apply_discount(prices, rate) that returns a new list of discounted prices 
# and leaves the original list unchanged. 
# Test it with [1000, 2500, 400] and 0.1, then print both lists to prove the original didn't change.

def apply_discount(prices, rate):
    price = prices.copy()

    for i,x in enumerate(price):
        discounted = x - rate
        price[i] = discounted
    
    return price

rate = 0.1
prices = [1000, 2500, 400]

print(prices)
print(f"Discounted prices:{apply_discount(prices, rate)}")