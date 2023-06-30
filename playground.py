def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=10, multiply=5)


class Car():
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

        # Tömbbel is lehet, de így crash -elni fog, ha nem lett inicializálva és lekéred
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)

your_car = Car(make="Ford")
print(your_car.make)
print(your_car.model)

