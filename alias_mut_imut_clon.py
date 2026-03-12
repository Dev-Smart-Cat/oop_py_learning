a = [1, 2, 3, 4]

b = a
c = b
d = c

# These two variables (a and b) are 2 aliases to the same object.
# That is, they have the same object in memory and the same id.
print(a is b is c is d)
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print("\n")

#------------------------------------------------------------------------------#
"""Alias with Classes"""

class Circle:

    def __init__(self, radious):
        # This is a instance attribute
        self.radious = radious

my_circle = Circle(4)
your_circle = my_circle

print("Before")
print(my_circle.radious)
print(your_circle.radious)
print("\n")

your_circle.radious = 18
print("After")
print(my_circle.radious)
print(your_circle.radious)
print("\n")

#------------------------------------------------------------------------------#
"""Alias with class"""

class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        if isinstance(item) in self._items:
            self._items.remove(item)
        else:
            print("This item is not in the list")


my_backpack = Backpack()
your_backpack = my_backpack
her_backpack = your_backpack

print("This reference the same object in memory for the 3 variables.")
print(my_backpack is your_backpack is her_backpack)
print("\n")

# Add items to the backpack
my_backpack.add_item("Bottle")
my_backpack.add_item("Candy")
# Show the items in the backpack and all the 3 backpacks will have the same items
print(my_backpack.items)
print(your_backpack.items)
print(her_backpack.items)
print("\n")

#--------------------------------------------------------------------------#
# Create a list
a = [7, 3, 2, 1]

# Update the first element
a[0] = 5

print(a)
print("\n")

# Tuples CANNOT BE updated.
tup = (7 , 3, 2, 1)
# tup[0] = 5

# Strings cannot be updated
string = "Hello, world!"

def add_aboslute_values(seq):
    for i in range(len(seq)):
        # abs() function considers the number without + or -
        seq[i] = abs(seq[i])
    return sum(seq)

# Print the values before calling the function
values = [-5, -6, -7, -8]
print("Values Before calling the function:", values)

# Print the values after calling the function
add_aboslute_values(values)
print("After calling the function: ", values)
print("\n")

# Mutate an object through alias
a = [1, 2, 3, 4]
# Create an alias to the list of objects assigning the a to b variable
b = a

b[0] = 15
print(b)
print(a)


# Create a tuple
a = (1, 2, 3, 4)
print(id(a))

# Access the value of the tuple
print(a[2:])

# Create a new object in memory
# between values 2 and 3 (2, 7, 3)
a = a[:2] + (7,) + a[2:]

print(id(a))
# Output:
# 140606020032512
# 140606020034272
print("\n")
#-------------------------------------------------------------------------------#

def remove_even_values(dictionary):
    # Use copy() of the dict to clone it and make modifications without affecting the original dict
    for key, value in dictionary.copy().items():
        if value % 2 == 0:
            del dictionary[key]

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
remove_even_values(my_dict)

print(my_dict)

a = [1, 2, 3, 4]
# Create a clone of the list without affecting the original list
b = a[:]

# Update the list
b[0] = 15
print(a)
print(b)