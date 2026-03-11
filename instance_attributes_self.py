"""
Classes define the state and the behavior of the objects in a GENERIC way.
It is not specific. The code in the class has to work for any instance of the class

__init__() => special method used to define the initial state of an object.
Called automatically when an instance is created.

self => is a generic way of referring to the current instance of the class.
self is a generic way of referring to the current instance of the class. 
When using self, this referes to any concrete objects or instance of the class.

Instance attributes:
- They belong to the instances.
- Every instance has its own, independent, copy of the attribute
- Changing their value only affects a particular instance. Other instances are not modified
"""

class House:

    # price is an argument or parameter
    # this is a method and method is line a function
    def __init__(self, price):
        # this is the price instance attribute
        self.price = price

class Circle:
    PI = 3.1416

    # USING SELF => self(of the instance that is beig created).radious (to the instance attribute "radious")
    # = radious (assign the value of the variable radious)
    # radious => is the parameter and independent or the value assigned to the attribute.
    # self.radious is the attribute of instance or actual name of the attribute created.
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


    # Arguments MUST BE followed by the class itself or self.
    def find_area(self):
        return Circle.PI * (self.radius**2)
    
blue_circle = Circle(15, "Blue")
area = blue_circle.find_area()
print(area)