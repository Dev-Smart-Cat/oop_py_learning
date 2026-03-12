# THIS IS THE OBJECT
my_list = [6, 2, 8, 2]

def print_data(seq):
    print("Inside function: ", id(seq))
    for elem in seq:
        print(elem)

def multiply_by_two(seq):
    print("Inside the function:", id(seq))
    for i in range(len(seq)):
        seq[i] *= 2


class Sale:
    
    def __init__(self, amount):
        self.amount = amount

    @property
    def print_sale(self):
        return print(self.amount)

def find_total(sales_list):
    total = 0

    # sale is the object
    for sale in sales_list:
        print("New sale")
        print(sale.amount)
        # amount WITHOUT following self can be used this way 
        # because it is OUTSIDE THE CLASS. 
        total += sale.amount
    
    return total

sale_one = Sale(1000)
sale_one.print_sale

# These are the objects created using Sale class
jan_sales = [Sale(400), Sale(345), Sale(45)]

print(find_total(jan_sales))


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


a = 257
b = 257
print(a is b)
print("\n")

#---------------------------------------------------------#

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


#--------------------------------------------------------------------#

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
