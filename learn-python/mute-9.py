# 3. Two ways to sort. Look up the list .sort() method and the built-in sorted() function. 
# Start with prices = [1200, 400, 850], save its id(), and sort it with prices.sort(). 
# Is it still the same list? Now try prices = sorted(prices, reverse=True). 
# Is it still the same list? Which one changes the list, and which one creates a new one?

prices = [1200, 400, 850]
# before sort() method
prices = [1200, 400, 850]
print(prices, id(prices))   
# after sort()
prices.sort()
print(prices, id(prices))   

# after sorted() function
prices = sorted(prices)
print(prices, id(prices))

# sort() method changes the original list (it sorts the original list), sorted func is opposite of that