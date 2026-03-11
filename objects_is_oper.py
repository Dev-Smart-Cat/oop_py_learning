"""
In Python everything is an object:
- int
- float
- bools
- functions
- lists
- tuples
- dicts
- strings
- exceptions

Programs keep track of how many "references to the object exist."

Reference => name that refers to the location in memory of an object.
Something that somehow references the objct and keeps it alive and accessible in the program.
E.g. variables, attributes, items.

Variables in Python store references to objects in memory. 
The object is stored somewhere in memory and the variable knows where to get that object from memory
because has a reference to that object.

When there are no references to the object in the program, the object is deleted from memory.
"""

print(object)

# int are objects
print(isinstance(5, object))

# list is object
print(isinstance([1, 2, 3], object))

# string is object
print(isinstance("hello, world!", object))

# class is an object
class Movie:

    def __init__(self, title):
        # This is an instance attribute
        self.title = title

print(isinstance(Movie, object))

#---------------------------------------------------------#
"""
id(): this function returns the address of the object in memory. This is the address of the object in memory.

"""

# Print the id of int object 15.
print(id(15))

# Print the id of string object
print(id("Hello, world"))

# Print the id list object with the same data
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print(id(a))
print(id(b))

class Backpack:

    def __init__(self):
        # This is an instance attribute
        self._items = []
    
    @property
    def items(self):
        return self._items
    
my_backpack = Backpack()
your_backpack = Backpack()

# Print the id of class object backpack
print("\n")
print("Printing the class object ids")
print(id(my_backpack))
print(id(your_backpack))

"""
is: the operators is and is not test for an object's identity: x is y is true if and only x and y are the same object.

If tow variables do not reference the same object, they will have different ids.

If two variables reference the same object, they will have the same id.

The is operator returns True if both operands reference the same object.
Else, it returns False.

Differences between is vs ==
is -> checks the objects, check if different references point to the same object.
== -> checks the values 

Two objects may have the same value and still be different objects in memory.

"""

# How two objects can have the same value and still represent different objects in memory.
# is vs == operators:
print("\n")
print("is vs == operators:")
c = [1, 6, 2, 6]
d = [1, 6, 2, 6]

# Check the ids in the memory
print(id(c))
print(id(d))
# output:
# 127142292438848
# 127142292438912


print(c is d)
print(c == d)
# output:
# False - false because they do not have the same id in memory, 
# because is operator compares if they have the same memory id 

# True - because both references and objects have the same values, the values are the same. 


e = [5, 2, 1, 8, 3]
f = [6, 2, 8, 9, 3]

print("\n")
print("Check if these list objects have the same id")
print(e is f)

# Copy e list to f variable
g = [5, 2, 1, 8, 3]
h = g

print("\n")
print("h is a copy of g list object:")
print(h is g)

# Comparing same object strings
i = "hello, world!"
j = "hello, world!"

print("\n")
print("Print the id string objects:")
print(id(i))
print(id(j))
print("\n")

print("Comparing same string objects:")
print(i is j)
print(j is i)
print("\n")


#------------------------------------------------------#

"""
Opmizinh Memory Usage:

When accessing one of the integers from -5 to 256, the existing object will be reused. 
The integers with the same value will be the same object in memory. 
It is used an object that already exists in memory.

Unexpected results: the current implementation keeps an array of integer objects for all intergers between -5 and 256, 
when you create an int in that range you actually just get back a reference to the existing object.

"""

a = 257
b = 257
print(a is b)
print("\n")

#---------------------------------------------------------#
"""
String Interning: the process of keeping only one distinct copy of the string in memory.

"""

a = "Hi"
print(id(a))

b = "Hi"
print(id(b))

c = "Hi"
print(id(c))

d = "Hi"
print(id(d))
print("\n")

# Since strings are immutable, ithe memory uses the same object.
# Output:
# 130680634357440
# 130680634357440
# 130680634357440
# 130680634357440

print(a is b is c is d)

# Output:
# True

"""
True because all of these variables reference the same object in memory.
"""

#--------------------------------------------------------------------#
"""
Objects can be passed b: value or reference.
In Python, objects are passed by reference.
We pass a reference to the object, not a new copy, so the original object can be modified.

"""

my_list = [6, 2, 8, 2]

def print_data(seq):
    print("Inside the function: ", id(seq))
    for elem in seq:
        print(elem)

print("Outside the function:", id(my_list))
print_data(my_list)
print("\n")

#-----------------------------------------------------------------------#
one_list = [6, 2, 8, 2]

def multiply_by_two(seq):
    print(id(seq))
    for i in range(len(seq)):
        seq[i] *= 2

multiply_by_two(one_list)
print(id(one_list))
print(one_list)
print("\n")

#-------------------------------------------------------------------------#

class Sale:

    def __init__(self, amount):
        self.amount = amount

def find_total(sales):

    total = 0

    for sale in sales:
        total += sale.amount

    return total

january_sales = [Sale(400), Sale(345), Sale(45)]

print("Total sale is:")
print(find_total(january_sales))









