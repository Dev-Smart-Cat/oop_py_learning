# Basic sintax of how implement inheritance
class Superclass:
    pass

class Subclass(Superclass):
    pass


class Polygon:

    def __init__(self, num_sides, color):
        # These are the instance attributes
        self.num_sides = num_sides
        self.color = color

    def describe_polygon(self):
        print(f"This polygon has {self.num_sides} side and it's {self.color}")

class Triangle(Polygon):

    NUM_SIDES = 3

    def __init__(self, base, height, color):
        Polygon.__init__(self, Triangle.NUM_SIDES, color)
        self.base = base
        self.height = height

    def find_area(self):
        return (self.base * self.height) / 2

class Square(Polygon):

    NUM_SIDES = 4

    def __init__(self, side_lenght, color):
        Polygon.__init__(self, Square.NUM_SIDES, color)
        self.side_lenght = side_lenght

    def find_area(self):
        return self.side_lenght ** 2

my_triangle = Triangle(5, 4, "Blue")
my_triangle.describe_polygon()
print(my_triangle.find_area())
print("\n")

my_square = Square(4, "Green")
my_square.describe_polygon()
print(my_square.find_area())
print("\n")

#-----------------------------------------------------#

class Professor:
    
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet_students(self):
        print("Welcome to class!")

# Define a subclass
class ScienceProfessor(Professor):

    def __init__(self, name, age, course):
        Professor.__init__(self, name, age, course)

    def greet_students(self):
        print("Hi everyone! It's a great day to study Science!")
        # Define the greet_students method from Professor class.
        Professor.greet_students(self)


# Create an instance
science_professor = ScienceProfessor("Teacher", 32, "Classes")
science_professor.greet_students()
print("\n")

"""
Method Overriding => used to customize or extend the functionality of a method that is already defined in the superclass.

"""

class Teacher:

    def __init__(self, full_name, teacher_id):
        self.full_name = full_name
        self.teacher_id = teacher_id

    def welcome_students(self):
        print(f"Welcome! I'm {self.full_name}")

class ScienceTeacher(Teacher):

    def welcome_students(self):
        print("Science is amazing.")
        print(f"Welcome. I'm {self.full_name}")

my_science_teacher = ScienceTeacher("Nora Nav", 123)
my_science_teacher.welcome_students()
print("\n")

#-------------------------------------------------------#
# Another method metodo to call a method from superclass
class Anotherteacher:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def welcome(self):
        print(f"Welcome {self.name}")

class Anotherprofessor(Anotherteacher):

    def welcome(self):
        print("Another teacher message!")
        # A sintax to call a method from the superclass
        Anotherteacher.welcome(self)
        # Sintax to call a method from the superclass, 
        # DOES NOT use self
        super().welcome()

my_professor = Anotherprofessor("Another Professor", 22)
my_professor.welcome()
print("\n")

#-------------------------------------------------------#

class Backpack:

    def __init__(self):
        self.items = []

    def add_snack(self, snack):
        print("Add the snack...")
        self.items.append(snack)
        print(f"{snack.capitalize()} was added!")

class SchoolBackpack(Backpack):

    def add_snack(self, snack):
        print("Go school")
        # Calling the method from the super class
        # Backpack.add_snack(self, snack)
        super().add_snack(snack)
        print(f"Your backpack has: {self.items}")

my_backpack = SchoolBackpack()
my_backpack.add_snack("Candy")
print(my_backpack.items)
print("\n")

#-------------------------------------------------------#
class BanckAccount:

    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds available.")
        else:
            self.balance -= amount

class CheckingAccount(BanckAccount):

    # Overdraft limit is a service that allows withdraw funds more than the limit
    def __init__(self, number, balance, overdraft_limit):
        BanckAccount.__init__(self, number, balance)
        self.overdraft_limit = overdraft_limit

    # Create a override method from withdraw method
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            print("Not enough funds available.")
        else:
            self.balance -= amount

checking_account = CheckingAccount("4552 2325 3566 3423", 4500, 500)
checking_account.withdraw(4900)


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

