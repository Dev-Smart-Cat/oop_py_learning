class Circle:

    def __int__(self, radious):
        self.radious = radious

    # Define a method
    def find_diameter(self):
        print(f"Diameter: {self.radious * 2}")

    def return_diameter(self):
        return self.radious * 2
    
class Backpack:

    def __init__(self):
        self._items = []

    # This is the getter
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item.")

    # Method to remove item
    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0
        
    # Method to confirm if the backpack has that item
    def has_item(self, item):
        return item in self._items
    
my_backpack = Backpack()
print(my_backpack.items())

my_backpack.add_item("bottle")
print(my_backpack.items())

my_backpack.add_item("bag")
print(my_backpack.items())

# To see the result wif the backpack has item,
# assign the returned value to a variable and print the variable
has_bottle = my_backpack.has_item("bottle")
# Print the variable to see the result whether true or false
print(has_bottle)

my_backpack.remove_item("bag")
print(my_backpack.items())

my_backpack.remove_item("bottle")
print(my_backpack.items())


# my_backpack.remove_item("bottle")
# print(my_backpack.items())

print("------------------")
print("\n")

#-----------------------------------------------------------#


class Circle:

    def __init__(self, radious):
        self.radious = radious

    def find_diameter(self):
        return self.radious * 2
    
one_circle = Circle(5)
diameter = one_circle.find_diameter()

print(diameter)

#--------------------------------------------------------------------#
class Player:

    def __init__(self, x, y):
        # These are instances attributes
        self.x = x
        self.y = y

    # Assign a default value for change argument
    def move_up(self, change=5):
        self.y += change

    def move_down(self, change=5):
        self.y -= change

    def move_right(self, change=2):
        self.x += change

    def move_left(self, change=2):
        self.x -= change

# Create the Player instance
my_player = Player(5, 10)

# Print the value y as it was passed as argument when defining the class instance
print(my_player.x)
# Update the y value because when calling the method moving_down, 
# it increments the value passed above + whether a passed value or the default value defined when creating the method.
my_player.move_right(5)
print(my_player.x)

print("------------------")
print("\n")

#-----------------------------------------------------------#

class Mochila:

    def __init__(self):
        self._items = []

    # This is the getter to get the items in the backpack
    @property
    def items(self):
        return self._items
    
    def add_multiple_items(self, items):
        """Method to demonstrate how to call a method from another method"""

        """self.add_new_items => is the instance of backpack"""
        for item in items:
            """for every item in the list of items (items is the memories' reference, 
            where the list is located), we are going to add that item.
            """
            self.add_new_items(item)
        

    
    # This is a method to add items and has an item as argument
    def add_new_items(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please enter a valid item.")

    # This is a method to remove an item and has item as argument
    def remove_one_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0
    # This is a method to confirm whether or not an item is in the backpack
    # and has item as argument to confirm whether or it is inside the backpack.
    def has_one_item(self, item):
        return item in self._items
    
    # This method sort the items in the list in alphabetical order
    def show_items(self, sort_list=False):
        if sort_list:
            print(sorted(self._items))
        else:
            print(self._items)
            

"""
sec_backpack = Mochila()
sec_backpack.add_new_items("bottle")
sec_backpack.add_new_items("bag")
sec_backpack.add_new_items("canddy")

print("Items not sorted:")
sec_backpack.show_items()

print("Sorted:")
sec_backpack.show_items(sort_list=True)
"""

sec_backpack = Mochila()

# Assigning list of items to a variable
empty_list_variable = sec_backpack.items
# Print the empty list
print(empty_list_variable)

# Add multiple items to the backpack
sec_backpack.add_multiple_items(["Bottle", "Bag", "Candy"])
# Print the variable with multiple items added
print(sec_backpack.items)

# object = list of items.
# variable = label the memory address where the list is located.
# memory = keep an object
# memory address = where the object is located.


