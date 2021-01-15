# *args
def add(*args):
    return sum(args)


print(add(3, 5, 6))


# **kwargs
def calculate(n, **kw):
    n *= kw["multiply"]
    n += kw["add"]
    return n


print(calculate(3, add=3, multiply=3))


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
