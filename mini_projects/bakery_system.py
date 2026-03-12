class Donut:

    def __init__(self, flavor, toppings, filling, size):
        self._flavor = flavor
        self._toppings = toppings
        self._filling = filling
        self.size = size

    @property
    def flavor(self):
        return self._flavor

    @property
    def topping(self):
        return self._toppings

    @property
    def filling(self):
        return self._filling

class Customer:

    def __init__(self, name, age, address, favorite_dessert):
        self.name = name
        self.age = age
        self.address = address
        self.favorite_dessert = favorite_dessert

class Cake:

    def __init__(self, flavor, price, quality):
        self.flavor = flavor
        self.price = price
        self.quality = quality

my_donut = Donut("fl one", "top two", "fil 3", "big")

print(my_donut.topping)
