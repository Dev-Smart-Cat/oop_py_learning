result = 5 + 6
print(result)

result = (5).__add__(6)
print(result)
print("\n")


"""__str__ method"""
class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
my_point = Point2D(56, 60)
print(my_point)
print("\n")

class Student:

    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa

    def __str__(self):
        return f"Student ID: {self.student_id} | Student: {self.name} | Age: {self.age} | GPA: {self.gpa}"
        
student = Student("12AB9", "Nora Nav", 34, 3.76)
print(student)
print("\n")

"""__len__ method"""

# Check the length of the string
print("Check the length of the string:")
my_string = "Hello, world!"
print(len(my_string))
print(my_string.__len__())
print("\n")

# Check the length of the list
my_list = [1, 2, 3, 4, 5]
print(len(my_list))
print(my_list.__len__())
print("\n")

# Check the length of the tuple
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))
print(my_tuple.__len__())
print("\n")

# Check the length of the dict
my_dict = {"a": 1, "b": 2, "c": 3}
print(len(my_dict))
print(my_dict.__len__())
print("\n")

class Backpack:

    def __init__(self):
        self.items = []

    # Define a method to add an item in the backpack.
    def add_item(self, item):
       self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not in the list.")

    def __len__(self):
        # Check the numbers of items in the backpack
        return len(self.items)

my_backpack = Backpack()
my_backpack.add_item("Bottle")
my_backpack.add_item("First kit")
my_backpack.add_item("Sleeping bag")
my_backpack.add_item("Candy")

print("Check the number of items in the backpack:")
print(len(my_backpack))

my_backpack.remove_item("Sleeping bag")
print(len(my_backpack))
print("\n")

"""__add__ method"""

print("__add__ method")
print(3 + 4)
print((3).__add__(4))

print("Hello" + "World!")
print(("Hello").__add__("World!"))

print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3].__add__([4, 5, 6]))
print("\n")

class Point2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point2D(new_x, new_y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
pointA = Point2D(5, 6)
print(pointA)

pointB = Point2D(2 ,3)
print(pointB)

pointC = pointA + pointB
print(pointC)
print("\n")

"""__getitem__ method"""

print("__getitem__ method")
print("\n")

one_list = ["a", "b", "c", "d"]
print("Print the item of the list")
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print("\n")

print("Print the element from the list using __getitem__()")
print(my_list.__getitem__(0))
print(my_list.__getitem__(1))
print(my_list.__getitem__(2))
print(my_list.__getitem__(3))
print("\n")

print("Print the letter of the string using __getitem__():")
one_string = "Word"

print(one_string[0])
print(one_string[1])
print(one_string[2])
print(one_string[3])
print("\n")

print(one_string.__getitem__(0))
print(one_string.__getitem__(1))
print(one_string.__getitem__(2))
print(one_string.__getitem__(3))
print("\n")

#---------------------------------------------------------#
class Bookshelf:

    # Initialize the constructor
    def __init__(self):
        self.content = [[],
                        [],
                        []]
    
    def add_book(self, book, location):
        self.content[location].append(book)

    def take_book(self, book, location):
        self.content[location].remove(book)

    def __getitem__(self, location):
        return self.content[location]
    
my_bookshelf = Bookshelf()
my_bookshelf.add_book("Les Miserables", 0)
my_bookshelf.add_book("Pride and Prejudice", 0)
my_bookshelf.add_book("Frankenstein", 0)

my_bookshelf.add_book("Sense and Sensibility", 1)
my_bookshelf.add_book("Jana Eyre", 1)
my_bookshelf.add_book("The Little Prince", 1)

my_bookshelf.add_book("Mobby Dick", 2)
my_bookshelf.add_book("The Adventure of Huckleberry Finn", 2)
my_bookshelf.add_book("Dracula", 2)

print(my_bookshelf[2])
print("\n")
"""__bool__ method"""

print("__bool__ method")
print("\n")

class BanckAccount:

    def __init__(self, account_owner, account_nmumber, initial_balance):
        self.account_owner = account_owner
        self.account_nmumber = account_nmumber
        self.balance = initial_balance

    # This is a method
    def  make_deposit(self, amount):
        self.balance += amount

    # This is a method
    def make_withdrawal(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def __bool__(self):
        return self.balance > 0


my_account = BanckAccount("Nora Nav", "356-2456-2455", 45045.23)
print(my_account.account_owner)
print(my_account.balance)

if my_account:
    print(True)
else:
    print(False)

# Updating the balance attribute
my_account.balance = 0
print(my_account.balance)
print(bool(my_account))
print("\n")

#---------------------------------------------------------------#
print("Rich Comparison methods")

print(15 <= 8)
print(4 > 4)
print(5 == 5)
print(6 != 8)

print("hello" < "world")
print("Python" >= "Java")
print("Hello" == "Hello")

print([1, 2, 3, 4] < [1, 2, 3, 5])
print([4, 5, 6] > [1, 2, 3, 4])
print("\n")

#-------------------------------------#

class Circle:
    """A class that represents a circle.

    Attributes:
        radious (float): the disctance from the center
            of the circle to its circumference.
        color (string): the color of the circle.
    """

    def __init__(self, radious, color):
        self.radious = radious
        self.color = color

    def __lt__(self, other):
        # Comparing if a circle is greater than another circle
        return self.radious < other.radious
    
    def __le__(self, other):
        return (self.radious <= other.radious
                and self.color == other.color)
    def __gt__(self, other):
        return self.radious > other.radious
    
    def __ge__(self, other):
        return (self.radious >= other.radious
                and self.color)
    def __eq__(self, other):
        return (self.radious >= other.radious
                and self.color == other.color)
    
    # Either one of the conditions is not true
    def __ne__(self, other):
        return (self.radious != other.radious
                or self.color != other.color)
    
circleA = Circle(5, "Blue")
circleB = Circle(5, "Green")
circleC = Circle(5, "Read")
circleD = Circle(5, "Blue")

print(circleA < circleB)
print(circleA <= circleB)
print(circleA != circleD)
print("\n")

#----------------------------------------------------------#

class Bubble:
    """A class that represents a bubble.
    
    This class have rich comparison methods that allow to 
    compare the size of the bubbles.

    Attributes:
        size (int): the size of the bubble.
        color (string): the color of the bubble.
        price (int): the price of the bubble.
    """

    def __init__(self, size, color, price):
        self.size = size
        self.color = color
        self.price = price

    def __lt__(self, other):
        return self.size < other.size
    
    def __le__(self, other):
        return self.size <= other.size
    
    def __eq__(self, other):
        return self.size == other.size
    
    def __ne__(self, other):
        return self.size != other.size
    
    def __gt__(self, other):
        return self.size > other.size
    
    def __ge__(self, other):
        return self.size >= other.size
    
bubble1 = Bubble(6, "Blue", 67)
bubble2 = Bubble(9, "Red", 34)

print("Using rich comparison to compare the size attribute of the bubbles:")
print(bubble1 < bubble2)
print(bubble1 <= bubble2)
print(bubble1 == bubble2)
print(bubble1 != bubble2)
print(bubble1 > bubble2)
print(bubble1 >= bubble2)
