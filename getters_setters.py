"""
Getters and setters are members of a class, that is, they are methods.

Methods are like functions associated to a specific object or class.

Getters and setters let us get and set the valur of an instance attribute.

Getters => Get a value of an attribute.

Setters => Set the value of an attribute.

We can make the attributes non-public and still provide a way to work with them indirectly.

GETTERS:
get_name, get address, get_color, get_age, get_id 

"""

class Movie:

    def __init__(self, title, rating):
        # The instance attribute title will be non-public _title
        self._title = title
        self.rating = rating

    # This is the getter to get the value of the instance attribute
    def get_title(self):
        return self._title

# Create a movie instance
my_movie = Movie("The Godfather", 4.8)

# Getter should follow bt (), e.g. getter()
print(my_movie.get_title())
print("------------------")
print("\n")

#--------------------------------------------------------------------------------#
"""
Setters => methods that we can call to set the value an instance attribute = self.instance_attribute = instance_attribute.

With setters we can validate the new value before assigning it to the attribute.

set_ + <attribute> e.g: set_name, set_address, set_color, set_age, set_id
"""

class Dog:

    def __init__(self, name, age):
        # These are the instances attributes
        self._name = name
        self.age = age

    # Define the GETTER
    def get_name(self):
        # Return because this method will access the name
        return self._name
    
    # Define the SETTER. And new name is a parameter that will replace the original name
    def set_name(self, new_name):
        # Confirm whether the name is string and has only lettters => isalpha()
        if isinstance(new_name, str) and new_name.isalpha():
            # Update the old name for the new name
            self._name = new_name
        else:
            print("Please enter a valid name.")

my_dog = Dog("Nora", 8)

# Getter MUST BE follwed by (), class_instance.getter()
print("Dog's name: ", my_dog.get_name())

# Update the name
my_dog.set_name("Norita4556")
# Getter MUST BE follwed by (), class_instance.getter()
print("New name: ", my_dog.get_name())
print("------------------")
print("\n")

#--------------------------------------------------------------------------------#

class Backpack:

    def __init__(self):
        self._items = []

    # This is a getter
    def get_items(self):
        # Return because this getter will access the instance attribute
        return self._items
    
    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items")

my_backpack = Backpack()
print(my_backpack.get_items())

# Use [] because the setter set_items() requires a list
# and the method was not defined using @property
print("This is a valid list")
my_backpack.set_items(["bottle", "bag", "canddy"])
print(my_backpack.get_items())

print("This IS NOT a valid list of items")
my_backpack.set_items("Hello, world!")
print("------------------")
print("\n")

#--------------------------------------------------------------------------------#
class Circle:

    def __init__(self, radious):
        # This is an instance attribute
        self._radious = radious

    # This is the getter
    def get_radious(self):
        return self._radious
    
    # This is the setter
    def set_radious(self, new_radious):
        if isinstance(new_radious, float) and new_radious > 0:
            self._radious = new_radious
        else:
            print("Please enter a valid radious.")

print("ORIGINAL radious.")
# Pass a value to the class because the aergument is radious
my_circle = Circle(2.5)
print(my_circle.get_radious())

my_circle.set_radious(1)

print("Update the radious")
my_circle.set_radious(3.0)
print(my_circle.get_radious())

print("------------------")
print("\n")

#--------------------------------------------------------------------------------#
class Dog:

    def __init__(self, age):
        # This is an instance attribute non-public _age
        self._age = age

    def get_age(self):
        print("Calling the getter...")
        return self._age
    
    def set_age(self, new_age):
        print("Calling the setter...")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age
        else:
            print("Please enter a valid age.")

    # Here use property to access the age and set the age.
    # This way, there is need to access the age and set the age by using set_age and get_age methods
    age = property(get_age, set_age)

my_dog = Dog(8)

# Here do not use get_age() method
print(f"My dog is {my_dog.age} year old.")
print("One year later.")

my_dog.age += 1  # or my_dog.age = my_dog.age + 1
# Here do not use the get_age() method
print(f"Now my dog is {my_dog.age}")
print("------------------")
print("\n")
#--------------------------------------------------------------------------------#

class Circle:

    # Define a class constant or class attributes
    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radious, color):
        # These are the instances attributes
        self._radious = radious
        self._color = color

    # getter to access the radious value
    def get_radious(self):
        return self._radious
    
    def set_radious(self, new_radious):
        if isinstance(new_radious, int) and new_radious > 0:
            self._radious = new_radious
        else:
            print("Please enter a valid radious")

    # Define the radious property
    radious = property(get_radious, set_radious)

    def get_color(self):
        return self._color
    
    def set_color(self, new_color):
        # use Cicle.VALID_COLORS because VALID_COLORS is a class attribute 
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color.")

    color = property(get_color, set_color)



# Define an instance of circle
one_circle = Circle(5.5, "Blue")
# Access the radious through the property
print(one_circle.radious)
# Update the radious
one_circle.radious = 100
print(one_circle.radious)


# Access the color through the property
print(one_circle.color)
# Update the color
one_circle.color = "Green"
print(one_circle.color)
print("------------------")
print("\n")
#--------------------------------------------------------------------------------#

"""
@property => A function that takes a function and extends its behavior without explicitly modifying it.
- Cleaner and more compact.
- Easier to read and understand
- Avoids calling property() directly.
"""

class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    # This is the getter using the @property decorator
    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating
    
    # This is the setter, that is, the method to update the rating value
    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please, enter a valid rating.")

# Define an instance of movie
one_movie = Movie("Titanic", 4.3)
# Getting the rating
print(one_movie.rating)

# Update the rating
one_movie.rating = 4.9
print(one_movie.rating)

print("------------------")
print("\n")
#--------------------------------------------------------------------------------#

print("Backpack class using @property")

class Backpack:

    def __init__(self):
        # This is a instance attribute, but there is no argument 
        # because it is a list  
        self._items = []

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, new_item):
        if isinstance(new_item, list):
            self._items = new_item
        else:
            print("This item is already in the backpack" \
            "please, enter anoter item.")

# Define the class instance
one_backpack = Backpack()
print(one_backpack)

# Updating the list and the list is after igual alone because IT MUST be a list
one_backpack.items = ["Bag", "Bottle"]
print(one_backpack.items)