# 3. Customers we lost. Using the two sets below, print which customers stopped ordering,
# which are new and which stayed, each as a sorted list:

# Copy
#
# Then try {["rice", "oil"]} and read the error. Which rule from Example 9 does this remind you of?

last_month = {"Noor Foods", "Bilal Traders", "Zara Textiles"}
this_month = {"Noor Foods", "Karachi Crafts"}

print(f"{sorted(last_month - this_month)} stopped ordering")
print(f"{sorted(this_month & last_month)} stayed")
print(f"{sorted(this_month - last_month)} new customers")

