# 1. Reading a line. Split "A102,Karachi Crafts,12800,pending" and print Karachi Crafts owes Rs 12,800. 
# You'll need to turn the amount into a number before you can format it with a comma.

string = "A102,Karachi Crafts,12800,pending"
stringList = string.split(",")

print(f"{stringList[1]} owes Rs {int(stringList[2])}")