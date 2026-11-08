# 1. Predict the output. What do the three print calls show? Predict first, then run it:

# Copy
# def add_tag(tag, tags=[]):
#     tags.append(tag)
#     return tags


# first = add_tag("new")
# second = add_tag("vip")
# print(first)
# print(second)
# print(first is second)
# first was created before "vip" was added, so why does it contain "vip"?

def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags


first = add_tag("new")
second = add_tag("vip")
print(first)
print(second)
print(first is second)

# as python reads the code in sequence, the function got executed and appended the first line, 
# then second, after that it printed the call, we already know list is mutable whenever function is called
# it appended the tag 