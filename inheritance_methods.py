"""
Define common functionality in the superclass and subclasses will have to these methods.

"""

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

"""
Overriding => involves modifying the behavior of a method within a hierarchy. When a method is overriden, 
its new inmplementation takes precedence over previous implementations located higher in the hierarchy.
"""
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