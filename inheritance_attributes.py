"""
Inheritance: Defining classes than inherit attributes
and methods from other class.

Classes usually inherit from more general classes that represent more 
abstract concepts.

Add new functionality or customize the existing one in the child class.
Eg: truck is a vehicle, meaning truck can be a child class of vehicle.

A class can inherit from multiple classes and multiple classes can inherit from the same class.
vehicle -> landvehicle -> car and truck

Parent Class (SUPERCLASS):
The class from which other classes inherit attributes and methods. 
E.g. Dog

Child Class (SUBCLASS)
The class that inherits attributes and methods from another class.
E.g: Poodle and Pintcher
"""

# This is an example how inherintance class work.
class Polygon:
    pass

class Triangle(Polygon):
    pass

class Square(Polygon):
    pass

class Aninal:
    def __init__(self, age):
        self.age = age

class Dog(Aninal):

    def __init__(self, name, age):
        Aninal.__init__(self, age)
        self.name = name

print(issubclass(Dog, Aninal))

class Polygon:
    
    def __init__(self, num_sides, color):
        # These are the instances attributes
        self.num_sides = num_sides
        self.color = color

class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        # These are the instances attributes
        self.base = base
        self.height = height


my_triangle = Triangle(5, 4, "Blue")

print(my_triangle.num_sides)
print(my_triangle.color)
print(my_triangle.base)
print(my_triangle.height)

print("-----------------------")
print("\n")

class Employee:

    def __init__(self, full_name, salary):
        # These are the attributes
        self.full_name = full_name
        self.salary = salary

class Programmer(Employee):

    
    def __init__(self, full_name, salary, programming_language):
        # Getting all the attributes class from the super class Employee
        Employee.__init__(self, full_name, salary)
        self.programming_language = programming_language

# This is the programmer instance
nora = Programmer("Nora Nav", 6000, "Python")

# Printing the instances attributes
print(nora.full_name)
print(nora.salary)
print(nora.programming_language)
print("-----------------------")
print("\n")

class Character:
    def __init__(self, x, y, num_lives):
        # These are the instances attributes
        self.x = x
        self.y = y
        self.num_lives = num_lives

# This class inherites Character class
class Player(Character):

    INITIAL_X = 0
    INITIAL_Y = 0
    INITIAL_NUM_LIVES = 10

    def __init__(self, score=0):
        Character.__init__(self, Player.INITIAL_X, Player.INITIAL_Y, Player.INITIAL_NUM_LIVES)
        self.score = score

class Enemy(Character):

    # Initialize the class Enemy with default values to x, y and num_lives
    def __init__(self, x=15, y=15, num_lives=8, is_poisonous=False):
        Character.__init__(self, x, y, num_lives)
        self.is_poisonous = is_poisonous

# Creating a player instance
my_player = Player()
print(my_player.score)
print(my_player.x)
print(my_player.y)
print(my_player.num_lives)
print("-----------------------")
print("\n")

# Customize the num_lives to this enemy
easy_enemy = Enemy(num_lives=1)
# Customize the num_lives and poisonous to this enemy
hard_enemy = Enemy(num_lives=56, is_poisonous=True)


# Value customized above
print(hard_enemy.is_poisonous)
# Print the default value defined in the class
print(hard_enemy.x)
# Print the default value defined in the class
print(hard_enemy.y)
# Value customized above
print(hard_enemy.num_lives)
print("-----------------------")
print("\n")

class Vehicle:
    def __init__(self, color, speed, fuel_type):
        self.color = color
        self.speed = speed
        self.fuel_type = fuel_type

# Define a Car class that inherits from the Vehicle class.
class Car(Vehicle):

    # Add a default_speed class attribute to the Car class.
    default_speed = 100

    def __init__(self, color, speed, fuel_type, num_doors, is_electric=False):
        Vehicle.__init__(self, color, speed, fuel_type)
        # Add these instance attributes to the Car class such that only the instances 
        # of this class have these attributes: num_doors, is_electric.
        self.num_doors = num_doors
        self.is_electric = is_electric

my_car = Car("Blue", 120, "gas", 2, False)
print(my_car.color)
print(my_car.speed)
print(my_car.fuel_type)
print(my_car.num_doors)
print(my_car.is_electric)
print("-----------------------")
print("\n")

class ElectronicDevice:

    def __init__(self, voltage, weight, height, color):
        self.voltage = voltage
        self.weight = weight
        self.height = height
        self.color = color

class TV(ElectronicDevice):

    def __init__(self, voltage, weight, height, color, max_num_channels):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.max_num_channels = max_num_channels

class Computer(ElectronicDevice):

    def __init__(self, voltage, weight, height, color, memory, hard_drive):
        ElectronicDevice.__init__(self, voltage, weight, height, color)
        self.memory = memory
        self.hard_drive = hard_drive

class Desktop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive, monitor_size):
        Computer.__init__(self, voltage, weight, height, color, memory, hard_drive)
        self.monitor_size = monitor_size

class Laptop(Computer):

    def __init__(self, voltage, weight, height, color, memory, hard_drive, has_mouse_pad):
        Laptop.__init__(self, voltage, weight, height, color, memory, hard_drive)
        self.has_mouse_pad = has_mouse_pad

# In the code editor, you will find a Pizza class already defined.
class Pizza:

    def __init__(self, size, toppings, price, ratings):
        self.size = size
        self.toppings = toppings
        self.price = price
        self.ratings = ratings

# Define two classes called Margherita and Marinara.
# Define the hierarchy by making Margherita and Marinara inherit the attributes of the Pizza class.
class Margherita(Pizza):
    
    def __init__(self, size, toppings, price, ratings, has_extra_cheese=False):
        Pizza.__init__(self, size, toppings, price, ratings)
        # Add the instance attribute has_extra_cheese to the Margherita class.
        # THIS IS AN INSTANCE ATTRIBUTE.
        self.has_extra_cheese = has_extra_cheese


class Marinara(Pizza):

    # Add the instance attribute has_extra_oregano to the Marinara class.
    def __init__(self, size, toppings, price, ratings, has_extra_oregano=False):
        Pizza.__init__(self, size, toppings, price, ratings)
        # THIS IS AN INSTANCE ATTRIBUTE
        self.has_extra_oregano = has_extra_oregano

# Create an instance of the Margherita class and assign it to the variable margherita.
margherita = Margherita("big", "chocolate", 5.00, "very good", True)

# Create an instance of the Marinara class and assign it to the variable marinara.
marinara = Marinara("small", "spice", 5.00, "very good", True)

print(margherita.size)
print(margherita.toppings)

print(marinara.ratings)
print(marinara.has_extra_oregano)

