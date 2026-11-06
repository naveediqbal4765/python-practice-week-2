# 2. The missing return. This decorator has a bug. The function should give back 1350,
# but it doesn't. Run it, explain what happened and fix it:


def log_call(func):
    def wrapper(total):
        print("Calling the function")
        return func(total)
    return wrapper


@log_call
def add_delivery(total):
    return total + 350


print(add_delivery(1000))

# wrapper function wasnt returning none as we didnt return anything 