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