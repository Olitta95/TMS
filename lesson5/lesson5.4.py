from datetime import datetime

def decorator_time(function):
    def wrapper(*args, **kvargs):
        time = datetime.now()
        result = function(*args, **kvargs)
        print("Used time:", time)
        return result
    return wrapper
@decorator_time
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(1, 5))