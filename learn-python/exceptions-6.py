# 1. Predict the output. What does this print? Predict first, then run it:

print("start")

try:
    total = int("abc")
    print("converted")
except ValueError as error:
    print(type(error))

print("done")

try:
    total = int("47")
    print("converted")
except ValueError as error:
    print(type(error))

print("done")

# Now change "abc" to "42". What prints this time?
# converted, done