def announce(func):
    def wrapper(total):
        print("before")
        result = func(total)
        print("after")
        return result

    return wrapper


@announce
def add_delivery(total):
    print("inside")
    return total + 350


print(add_delivery(1000))
